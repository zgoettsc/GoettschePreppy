// Source fetch and USGS map fetch tests. No network: upstream is a mock fetch.
import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { makeHandler, assertPublicHttpUrl, MAP_HOSTS } from "../src/relay.js";
import { KEY_ALICE, makeEnv, ctxMock, post, mockFetch, streamOf } from "./_util.mjs";

const SOURCES = {
  "usda-canning": "https://nchfp.example.gov/guide1.pdf",
  "redirects": "https://pub.example.org/a",
  "plain-http": "http://old.example.edu/doc.html",
};

const PDF = new Uint8Array([0x25, 0x50, 0x44, 0x46, 0x2d, 0x31, 0x2e, 0x37, 0x0a]);

function pdfResponse(extraHeaders = {}) {
  return new Response(PDF, { status: 200, headers: { "content-type": "application/pdf", "set-cookie": "a=b", ...extraHeaders } });
}

const redirect = (to, status = 302) => new Response(null, { status, headers: { location: to } });

function fetchBody(source_key) {
  return post("/api/v1/fetch", { access_key: KEY_ALICE, source_key });
}

// --- /fetch --------------------------------------------------------------

test("fetch: known key streams the bytes with upstream content-type", async () => {
  const f = mockFetch(() => pdfResponse());
  const h = makeHandler({ fetch: f, sourceUrls: SOURCES });
  const ctx = ctxMock();
  const env = makeEnv();
  const r = await h(fetchBody("usda-canning"), env, ctx);
  assert.equal(r.status, 200);
  assert.equal(r.headers.get("content-type"), "application/pdf");
  assert.equal(r.headers.get("set-cookie"), null);
  assert.deepEqual(new Uint8Array(await r.arrayBuffer()), PDF);
  assert.equal(f.calls[0].url, SOURCES["usda-canning"]);
  assert.equal(f.calls[0].init.redirect, "manual");
  assert.equal(f.calls[0].init.method, "GET");
  const sentHeaders = JSON.stringify(f.calls[0].init.headers);
  assert.ok(!sentHeaders.includes(KEY_ALICE) && !/cookie|authorization|x-api-key/i.test(sentHeaders));
  await ctx.settle();
  assert.equal(env.COUNTS.store.size, 1);
});

test("fetch: unknown key is 404 and nothing is fetched", async () => {
  const f = mockFetch(() => assert.fail("no upstream"));
  const h = makeHandler({ fetch: f, sourceUrls: SOURCES });
  for (const k of ["nope", "__proto__", "constructor", "toString"]) {
    const r = await h(fetchBody(k), makeEnv());
    assert.equal(r.status, 404, k);
  }
  const r = await h(fetchBody(undefined), makeEnv());
  assert.equal(r.status, 400);
});

test("fetch: a raw url field is ignored; only source_key selects", async () => {
  const f = mockFetch(() => pdfResponse());
  const h = makeHandler({ fetch: f, sourceUrls: SOURCES });
  const r = await h(post("/api/v1/fetch", { access_key: KEY_ALICE, source_key: "usda-canning", url: "https://evil.example/x" }), makeEnv());
  await r.arrayBuffer();
  assert.equal(f.calls[0].url, SOURCES["usda-canning"]);
});

test("fetch: bad access key is 401 and nothing is fetched", async () => {
  const f = mockFetch(() => assert.fail("no upstream"));
  const h = makeHandler({ fetch: f, sourceUrls: SOURCES });
  const r = await h(post("/api/v1/fetch", { access_key: "wrong-wrong-wrong-wrong", source_key: "usda-canning" }), makeEnv());
  assert.equal(r.status, 401);
});

test("fetch: follows up to 3 redirects (relative and absolute)", async () => {
  const f = mockFetch((url, init, n) => {
    if (n === 1) return redirect("/b", 301);
    if (n === 2) return redirect("https://cdn.example.net/c", 307);
    if (n === 3) return redirect("https://cdn.example.net/final.pdf", 308);
    return pdfResponse();
  });
  const h = makeHandler({ fetch: f, sourceUrls: SOURCES });
  const r = await h(fetchBody("redirects"), makeEnv());
  assert.equal(r.status, 200);
  await r.arrayBuffer();
  assert.deepEqual(
    f.calls.map((c) => c.url),
    ["https://pub.example.org/a", "https://pub.example.org/b", "https://cdn.example.net/c", "https://cdn.example.net/final.pdf"],
  );
});

test("fetch: a 4th redirect fails", async () => {
  const f = mockFetch((url, init, n) => redirect(`https://pub.example.org/r${n}`));
  const h = makeHandler({ fetch: f, sourceUrls: SOURCES });
  const r = await h(fetchBody("redirects"), makeEnv());
  assert.equal(r.status, 502);
  assert.equal(f.calls.length, 4);
});

test("fetch: redirects to non-http(s), private, loopback and internal hosts are refused", async () => {
  const targets = [
    "file:///etc/passwd",
    "ftp://pub.example.org/x",
    "javascript:alert(1)",
    "http://127.0.0.1/",
    "http://2130706433/",
    "http://0x7f.0.0.1/",
    "http://10.0.0.5/x",
    "http://172.20.1.1/",
    "http://192.168.1.1/",
    "http://169.254.169.254/latest/meta-data/",
    "http://100.64.0.1/",
    "http://0.0.0.0/",
    "http://[::1]/",
    "http://[::ffff:127.0.0.1]/",
    "http://[fd00::1]/",
    "http://localhost/",
    "http://printer.local/",
    "http://metadata.google.internal/",
    "http://intranet/",
    "https://pub.example.org:8443/x",
    "https://user:pw@pub.example.org/x",
  ];
  for (const t of targets) {
    const f = mockFetch((url, init, n) => (n === 1 ? redirect(t) : assert.fail(`followed to ${t}`)));
    const h = makeHandler({ fetch: f, sourceUrls: SOURCES });
    const r = await h(fetchBody("redirects"), makeEnv());
    assert.equal(r.status, 403, t);
    assert.equal(f.calls.length, 1, t);
  }
});

test("fetch: plain http sources are allowed", async () => {
  const f = mockFetch(() => new Response("<html></html>", { headers: { "content-type": "text/html; charset=utf-8" } }));
  const h = makeHandler({ fetch: f, sourceUrls: SOURCES });
  const r = await h(fetchBody("plain-http"), makeEnv());
  assert.equal(r.status, 200);
  assert.equal(r.headers.get("content-type"), "text/html; charset=utf-8");
  assert.equal(await r.text(), "<html></html>");
});

test("fetch: missing content-type becomes application/octet-stream", async () => {
  const f = mockFetch(() => new Response(streamOf([PDF])));
  const h = makeHandler({ fetch: f, sourceUrls: SOURCES });
  const r = await h(fetchBody("usda-canning"), makeEnv());
  assert.equal(r.headers.get("content-type"), "application/octet-stream");
  await r.arrayBuffer();
});

test("fetch: content-length over FETCH_MAX_MB is 413", async () => {
  const f = mockFetch(() => new Response(streamOf(["x"]), { headers: { "content-type": "application/pdf", "content-length": String(61 * 1024 * 1024) } }));
  const h = makeHandler({ fetch: f, sourceUrls: SOURCES });
  const r = await h(fetchBody("usda-canning"), makeEnv());
  assert.equal(r.status, 413);
});

test("fetch: a stream without length is cut at the cap", async () => {
  const chunk = new Uint8Array(512 * 1024);
  const f = mockFetch(() => new Response(streamOf([chunk, chunk, chunk]), { headers: { "content-type": "application/pdf" } }));
  const h = makeHandler({ fetch: f, sourceUrls: SOURCES });
  const r = await h(fetchBody("usda-canning"), makeEnv({ FETCH_MAX_MB: "1" }));
  assert.equal(r.status, 200);
  await assert.rejects(r.arrayBuffer());
});

test("fetch: under the cap without length streams fully", async () => {
  const chunk = new Uint8Array(256 * 1024).fill(7);
  const f = mockFetch(() => new Response(streamOf([chunk, chunk]), { headers: { "content-type": "application/pdf" } }));
  const h = makeHandler({ fetch: f, sourceUrls: SOURCES });
  const r = await h(fetchBody("usda-canning"), makeEnv({ FETCH_MAX_MB: "1" }));
  assert.equal((await r.arrayBuffer()).byteLength, 512 * 1024);
});

test("fetch: upstream 403/404/500 becomes 502 with the upstream status", async () => {
  for (const s of [403, 404, 500]) {
    const f = mockFetch(() => new Response("blocked page with details", { status: s }));
    const h = makeHandler({ fetch: f, sourceUrls: SOURCES });
    const r = await h(fetchBody("usda-canning"), makeEnv());
    assert.equal(r.status, 502);
    const t = await r.text();
    assert.ok(!t.includes("details"));
    assert.equal(JSON.parse(t).error.upstream_status, s);
  }
});

test("fetch: network failure is a generic 502", async () => {
  const f = mockFetch(() => {
    throw new TypeError("getaddrinfo ENOTFOUND internal-detail");
  });
  const h = makeHandler({ fetch: f, sourceUrls: SOURCES });
  const r = await h(fetchBody("usda-canning"), makeEnv());
  assert.equal(r.status, 502);
  assert.ok(!(await r.text()).includes("internal-detail"));
});

test("fetch: the bundled index is keys to http(s) URLs only", () => {
  const urls = JSON.parse(readFileSync(new URL("../src/source-urls.json", import.meta.url), "utf8"));
  const entries = Object.entries(urls);
  assert.ok(entries.length > 0, "run node scripts/build-worker-index.mjs");
  for (const [k, v] of entries) {
    assert.equal(typeof k, "string");
    const u = new URL(v);
    assert.doesNotThrow(() => assertPublicHttpUrl(u), `${k}: ${v}`);
  }
});

// --- /fetch-map ----------------------------------------------------------

const TOPO = "https://prd-tnm.s3.amazonaws.com/StagedProducts/Maps/USTopo/PDF/SD/SD_Harrisburg_20210621_TM_geo.pdf";

function mapBody(url) {
  return post("/api/v1/fetch-map", { access_key: KEY_ALICE, url });
}

test("fetch-map: USGS topo GeoPDF on prd-tnm streams through", async () => {
  const f = mockFetch(() => pdfResponse({ "content-length": String(PDF.byteLength) }));
  const h = makeHandler({ fetch: f });
  const ctx = ctxMock();
  const env = makeEnv();
  const r = await h(mapBody(TOPO), env, ctx);
  assert.equal(r.status, 200);
  assert.equal(r.headers.get("content-type"), "application/pdf");
  assert.equal(r.headers.get("content-length"), String(PDF.byteLength));
  assert.deepEqual(new Uint8Array(await r.arrayBuffer()), PDF);
  assert.equal(f.calls[0].url, TOPO);
  await ctx.settle();
  assert.equal(env.COUNTS.store.size, 1);
});

test("fetch-map: every allowlisted host and prefix works", async () => {
  const urls = [
    "https://prd-tnm.s3.us-west-2.amazonaws.com/StagedProducts/Maps/HistoricalTopo/PDF/IL/24000/IL_Example_1950.pdf",
    "https://tnmaccess.nationalmap.gov/api/v1/products?datasets=US%20Topo%20Current&bbox=-96.8,43.5,-96.7,43.6",
    "https://rockyweb.usgs.gov/vdelivery/Datasets/Staged/Elevation/x.zip",
  ];
  for (const u of urls) {
    const f = mockFetch(() => pdfResponse());
    const h = makeHandler({ fetch: f });
    const r = await h(mapBody(u), makeEnv());
    assert.equal(r.status, 200, u);
    await r.arrayBuffer();
  }
  assert.deepEqual(Object.keys(MAP_HOSTS).sort(), [
    "prd-tnm.s3.amazonaws.com",
    "prd-tnm.s3.us-west-2.amazonaws.com",
    "rockyweb.usgs.gov",
    "tnmaccess.nationalmap.gov",
  ]);
});

test("fetch-map: other hosts, other paths, http and lookalikes are refused", async () => {
  const bad = [
    "https://example.com/StagedProducts/Maps/x.pdf",
    "http://prd-tnm.s3.amazonaws.com/StagedProducts/Maps/x.pdf",
    "https://prd-tnm.s3.amazonaws.com/private/x.pdf",
    "https://prd-tnm.s3.amazonaws.com.evil.example/StagedProducts/x.pdf",
    "https://evilprd-tnm.s3.amazonaws.com/StagedProducts/x.pdf",
    "https://other-bucket.s3.amazonaws.com/StagedProducts/x.pdf",
    "https://tnmaccess.nationalmap.gov/admin",
    "https://user:pw@prd-tnm.s3.amazonaws.com/StagedProducts/x.pdf",
    "https://prd-tnm.s3.amazonaws.com:444/StagedProducts/x.pdf",
    "https://169.254.169.254/StagedProducts/x",
    "not a url",
  ];
  for (const u of bad) {
    const f = mockFetch(() => assert.fail(`fetched ${u}`));
    const h = makeHandler({ fetch: f });
    const r = await h(mapBody(u), makeEnv());
    assert.ok(r.status === 403 || r.status === 400, `${u} -> ${r.status}`);
    assert.equal(f.calls.length, 0);
  }
});

test("fetch-map: redirects must stay on the allowlist", async () => {
  let f = mockFetch((url, init, n) => (n === 1 ? redirect("https://evil.example/StagedProducts/x.pdf") : assert.fail()));
  let h = makeHandler({ fetch: f });
  let r = await h(mapBody(TOPO), makeEnv());
  assert.equal(r.status, 403);
  f = mockFetch((url, init, n) =>
    n === 1 ? redirect("https://prd-tnm.s3.us-west-2.amazonaws.com/StagedProducts/Maps/USTopo/PDF/SD/x.pdf") : pdfResponse(),
  );
  h = makeHandler({ fetch: f });
  r = await h(mapBody(TOPO), makeEnv());
  assert.equal(r.status, 200);
  await r.arrayBuffer();
});

test("fetch-map: content-length over MAP_MAX_MB is 413", async () => {
  const f = mockFetch(() => new Response(streamOf(["x"]), { headers: { "content-length": String(3 * 1024 * 1024) } }));
  const h = makeHandler({ fetch: f });
  const r = await h(mapBody(TOPO), makeEnv({ MAP_MAX_MB: "2" }));
  assert.equal(r.status, 413);
});

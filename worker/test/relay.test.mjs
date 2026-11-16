// Relay tests: access keys, CORS, Messages pass-through, counter, routing.
// Run: npm run test:worker   (or: node --test worker/test/*.mjs)
import { test, beforeEach, afterEach } from "node:test";
import assert from "node:assert/strict";
import worker from "../src/index.js";
import {
  makeHandler,
  timingSafeEqualStr,
  sha256Hex,
  counterKey,
  MODEL,
  ANTHROPIC_URL,
  DEFAULT_ANTHROPIC_VERSION,
} from "../src/relay.js";
import { ORIGIN, KEY_ALICE, KEY_BOB, sha, makeEnv, ctxMock, post, mockFetch, streamOf } from "./_util.mjs";

// Fail any test that makes the relay write to the console (it must never log).
const consoleCalls = [];
const saved = {};
beforeEach(() => {
  consoleCalls.length = 0;
  for (const m of ["log", "info", "warn", "error", "debug"]) {
    saved[m] = console[m];
    console[m] = (...a) => consoleCalls.push([m, a]);
  }
});
afterEach(() => {
  for (const m of Object.keys(saved)) console[m] = saved[m];
  assert.deepEqual(consoleCalls, [], "relay wrote to the console");
});

const SSE = [
  'event: message_start\ndata: {"type":"message_start","message":{"id":"msg_1","model":"claude-opus-5-5","usage":{"input_tokens":10,"cache_read_input_tokens":9000}}}\n\n',
  'event: content_block_delta\ndata: {"type":"content_block_delta","index":0,"delta":{"type":"text_delta","text":"Hello"}}\n\n',
  'event: message_stop\ndata: {"type":"message_stop"}\n\n',
];

function sseUpstream() {
  return mockFetch(
    () =>
      new Response(streamOf(SSE), {
        status: 200,
        headers: { "content-type": "text/event-stream", "request-id": "req_123", "set-cookie": "x=y" },
      }),
  );
}

function msgRequest(over = {}) {
  return {
    model: MODEL,
    max_tokens: 1000,
    stream: true,
    system: [{ type: "text", text: "Frozen corpus", cache_control: { type: "ephemeral", ttl: "1h" } }],
    messages: [{ role: "user", content: "Write page 01-01." }],
    ...over,
  };
}

// --- helpers -------------------------------------------------------------

test("timingSafeEqualStr compares whole strings", () => {
  const a = sha("x");
  assert.equal(timingSafeEqualStr(a, a), true);
  assert.equal(timingSafeEqualStr(a, sha("y")), false);
  assert.equal(timingSafeEqualStr(a, a.slice(0, 63)), false);
  assert.equal(timingSafeEqualStr(a.slice(0, 63), a), false);
  assert.equal(timingSafeEqualStr(a, undefined), false);
});

test("sha256Hex matches node:crypto", async () => {
  assert.equal(await sha256Hex(KEY_ALICE), sha(KEY_ALICE));
});

// --- /check --------------------------------------------------------------

test("check: valid key returns its label", async () => {
  const h = makeHandler({ fetch: mockFetch(() => assert.fail("no upstream")) });
  const r = await h(post("/api/v1/check", { access_key: KEY_BOB }), makeEnv(), ctxMock());
  assert.equal(r.status, 200);
  assert.deepEqual(await r.json(), { ok: true, label: "bob" });
  assert.equal(r.headers.get("access-control-allow-origin"), ORIGIN);
});

test("check: hash is case-insensitive in ACCESS_KEYS", async () => {
  const h = makeHandler({ fetch: mockFetch(() => assert.fail()) });
  const env = makeEnv({ ACCESS_KEYS: JSON.stringify([{ label: "carol", sha256: sha(KEY_ALICE).toUpperCase() }]) });
  const r = await h(post("/api/v1/check", { access_key: KEY_ALICE }), env);
  assert.equal(r.status, 200);
});

test("check: wrong, short and missing keys are 401 with a generic body", async () => {
  const h = makeHandler({ fetch: mockFetch(() => assert.fail()) });
  for (const access_key of ["gpk_wrong_0123456789abcdefghijklmnop", "short", undefined, 42]) {
    const r = await h(post("/api/v1/check", { access_key }), makeEnv());
    assert.equal(r.status, 401);
    const j = await r.json();
    assert.equal(j.type, "error");
    assert.equal(j.error.type, "unauthorized");
    assert.ok(!JSON.stringify(j).includes("alice"));
  }
});

test("check: missing or broken ACCESS_KEYS is a generic 500", async () => {
  const h = makeHandler({ fetch: mockFetch(() => assert.fail()) });
  for (const ACCESS_KEYS of [undefined, "", "not json", "{}", "[]", '[{"label":"x","sha256":"abc"}]']) {
    const r = await h(post("/api/v1/check", { access_key: KEY_ALICE }), makeEnv({ ACCESS_KEYS }));
    assert.equal(r.status, 500);
    assert.equal((await r.json()).error.type, "not_configured");
  }
});

test("check: non-JSON content type and invalid JSON are 400", async () => {
  const h = makeHandler({});
  let r = await h(post("/api/v1/check", null, { headers: { "content-type": "text/plain" }, raw: "{}" }), makeEnv());
  assert.equal(r.status, 400);
  r = await h(post("/api/v1/check", null, { raw: "{not json" }), makeEnv());
  assert.equal(r.status, 400);
  r = await h(post("/api/v1/check", null, { raw: "[1,2]" }), makeEnv());
  assert.equal(r.status, 400);
});

test("small endpoints reject bodies over 16 KB", async () => {
  const h = makeHandler({});
  const r = await h(post("/api/v1/check", { access_key: KEY_ALICE, pad: "x".repeat(20000) }), makeEnv());
  assert.equal(r.status, 413);
});

// --- CORS ----------------------------------------------------------------

test("CORS: preflight from PAGES_ORIGIN is allowed", async () => {
  const h = makeHandler({});
  const req = new Request("https://relay.example.workers.dev/api/v1/messages", {
    method: "OPTIONS",
    headers: { origin: ORIGIN, "access-control-request-method": "POST" },
  });
  const r = await h(req, makeEnv());
  assert.equal(r.status, 204);
  assert.equal(r.headers.get("access-control-allow-origin"), ORIGIN);
  assert.match(r.headers.get("access-control-allow-methods"), /POST/);
  assert.match(r.headers.get("access-control-allow-headers"), /content-type/);
});

test("CORS: other origins are refused, before any key check", async () => {
  const f = mockFetch(() => assert.fail("no upstream"));
  const h = makeHandler({ fetch: f });
  const r = await h(post("/api/v1/check", { access_key: KEY_ALICE }, { origin: "https://evil.example" }), makeEnv());
  assert.equal(r.status, 403);
  assert.equal(r.headers.get("access-control-allow-origin"), null);
  const pre = await h(
    new Request("https://relay.example.workers.dev/api/v1/check", { method: "OPTIONS", headers: { origin: "https://evil.example" } }),
    makeEnv(),
  );
  assert.equal(pre.status, 403);
});

test("CORS: unset PAGES_ORIGIN refuses every browser origin", async () => {
  const h = makeHandler({});
  const r = await h(post("/api/v1/check", { access_key: KEY_ALICE }), makeEnv({ PAGES_ORIGIN: "" }));
  assert.equal(r.status, 403);
});

test("CORS: PAGES_ORIGIN may list several origins; trailing slash ignored", async () => {
  const h = makeHandler({});
  const env = makeEnv({ PAGES_ORIGIN: "https://a.pages.dev/, https://b.pages.dev" });
  const r = await h(post("/api/v1/check", { access_key: KEY_ALICE }, { origin: "https://a.pages.dev" }), env);
  assert.equal(r.status, 200);
  const r2 = await h(post("/api/v1/check", { access_key: KEY_ALICE }, { origin: "https://b.pages.dev" }), env);
  assert.equal(r2.status, 200);
});

test("no Origin header (script, curl): allowed, no CORS headers", async () => {
  const h = makeHandler({});
  const r = await h(post("/api/v1/check", { access_key: KEY_ALICE }, { origin: null }), makeEnv());
  assert.equal(r.status, 200);
  assert.equal(r.headers.get("access-control-allow-origin"), null);
});

// --- /messages -----------------------------------------------------------

test("messages: forwards to Anthropic with owner key and streams SSE back byte for byte", async () => {
  const f = sseUpstream();
  const h = makeHandler({ fetch: f });
  const ctx = ctxMock();
  const env = makeEnv();
  const request = msgRequest();
  const r = await h(post("/api/v1/messages", { access_key: KEY_ALICE, request }), env, ctx);
  assert.equal(r.status, 200);
  assert.equal(r.headers.get("content-type"), "text/event-stream");
  assert.equal(r.headers.get("request-id"), "req_123");
  assert.equal(r.headers.get("set-cookie"), null);
  assert.equal(r.headers.get("access-control-allow-origin"), ORIGIN);
  assert.equal(await r.text(), SSE.join(""));

  assert.equal(f.calls.length, 1);
  const { url, init } = f.calls[0];
  assert.equal(url, ANTHROPIC_URL);
  assert.equal(init.method, "POST");
  assert.equal(init.headers["x-api-key"], "sk-ant-test-not-a-real-key");
  assert.equal(init.headers["anthropic-version"], DEFAULT_ANTHROPIC_VERSION);
  assert.equal(init.headers["anthropic-beta"], undefined);
  const sent = JSON.parse(init.body);
  assert.deepEqual(sent, request, "request body forwarded unchanged (cache_control included)");
  assert.equal(sent.access_key, undefined, "access key never forwarded");
  assert.ok(!init.body.includes(KEY_ALICE));

  await ctx.settle();
  assert.equal(env.COUNTS.store.get(counterKey({ label: "alice", sha256: sha(KEY_ALICE) })), "1");
});

test("messages: body key order is preserved (cache prefix stability)", async () => {
  const f = sseUpstream();
  const h = makeHandler({ fetch: f });
  const raw = `{"access_key":"${KEY_ALICE}","request":{"model":"${MODEL}","system":"S","max_tokens":5,"messages":[{"role":"user","content":"hi"}],"stream":true}}`;
  await (await h(post("/api/v1/messages", null, { raw }), makeEnv())).text();
  assert.equal(f.calls[0].init.body, `{"model":"${MODEL}","system":"S","max_tokens":5,"messages":[{"role":"user","content":"hi"}],"stream":true}`);
});

test("messages: max_tokens above MAX_TOKENS is capped (default 32000)", async () => {
  const f = sseUpstream();
  const h = makeHandler({ fetch: f });
  let r = await h(post("/api/v1/messages", { access_key: KEY_ALICE, request: msgRequest({ max_tokens: 128000 }) }), makeEnv());
  await r.text();
  assert.equal(JSON.parse(f.calls[0].init.body).max_tokens, 32000);
  assert.equal(r.headers.get("x-relay-max-tokens"), "32000");

  r = await h(
    post("/api/v1/messages", { access_key: KEY_ALICE, request: msgRequest({ max_tokens: 9000 }) }),
    makeEnv({ MAX_TOKENS: "8000" }),
  );
  await r.text();
  assert.equal(JSON.parse(f.calls[1].init.body).max_tokens, 8000);

  r = await h(post("/api/v1/messages", { access_key: KEY_ALICE, request: msgRequest({ max_tokens: 100 }) }), makeEnv());
  await r.text();
  assert.equal(JSON.parse(f.calls[2].init.body).max_tokens, 100);
  assert.equal(r.headers.get("x-relay-max-tokens"), null);
});

test("messages: only claude-opus-5-5 is accepted", async () => {
  const f = mockFetch(() => assert.fail("must not reach upstream"));
  const h = makeHandler({ fetch: f });
  for (const model of ["claude-sonnet-5-5", "claude-fable-5-2", "claude-opus-5-5-20260401", undefined]) {
    const r = await h(post("/api/v1/messages", { access_key: KEY_ALICE, request: msgRequest({ model }) }), makeEnv());
    assert.equal(r.status, 400);
    assert.equal((await r.json()).error.type, "invalid_request");
  }
});

test("messages: bad key is 401 before any validation or upstream call", async () => {
  const f = mockFetch(() => assert.fail("must not reach upstream"));
  const h = makeHandler({ fetch: f });
  const r = await h(post("/api/v1/messages", { access_key: "nope-nope-nope-nope", request: msgRequest({ model: "x" }) }), makeEnv());
  assert.equal(r.status, 401);
});

test("messages: refuses thread, mcp_servers, container, fast mode, open fallbacks", async () => {
  const f = mockFetch(() => assert.fail("must not reach upstream"));
  const h = makeHandler({ fetch: f });
  const bad = [
    { thread: { id: "t" } },
    { mcp_servers: [{ type: "url", url: "https://x", name: "x" }] },
    { container: { skills: [] } },
    { speed: "fast" },
    { fallbacks: "default" },
    { fallbacks: [{ model: "claude-fable-5-2" }] },
    { max_tokens: -1 },
    { max_tokens: "100" },
    { messages: [] },
  ];
  for (const over of bad) {
    const r = await h(post("/api/v1/messages", { access_key: KEY_ALICE, request: msgRequest(over) }), makeEnv());
    assert.equal(r.status, 400, JSON.stringify(over));
  }
  const r = await h(post("/api/v1/messages", { access_key: KEY_ALICE, request: "string" }), makeEnv());
  assert.equal(r.status, 400);
});

test("messages: allowed fallbacks and fast mode with ALLOW_FAST_MODE=1 pass", async () => {
  const f = sseUpstream();
  const h = makeHandler({ fetch: f });
  let r = await h(
    post("/api/v1/messages", {
      access_key: KEY_ALICE,
      betas: ["server-side-fallback-2026-07-01"],
      request: msgRequest({ fallbacks: [{ model: "claude-opus-4-8" }] }),
    }),
    makeEnv(),
  );
  assert.equal(r.status, 200);
  await r.text();
  assert.equal(f.calls[0].init.headers["anthropic-beta"], "server-side-fallback-2026-07-01");
  r = await h(post("/api/v1/messages", { access_key: KEY_ALICE, request: msgRequest({ speed: "fast" }) }), makeEnv({ ALLOW_FAST_MODE: "1" }));
  assert.equal(r.status, 200);
  await r.text();
});

test("messages: anthropic-beta from header and body are merged and validated", async () => {
  const f = sseUpstream();
  const h = makeHandler({ fetch: f });
  let r = await h(
    post(
      "/api/v1/messages",
      { access_key: KEY_ALICE, betas: ["task-budgets-2026-03-13", "a-b"], request: msgRequest() },
      { headers: { "anthropic-beta": "a-b, compact-2026-01-12" } },
    ),
    makeEnv(),
  );
  await r.text();
  assert.equal(f.calls[0].init.headers["anthropic-beta"], "a-b,compact-2026-01-12,task-budgets-2026-03-13");
  r = await h(post("/api/v1/messages", { access_key: KEY_ALICE, betas: ["bad value\r\nx-api-key: y"], request: msgRequest() }), makeEnv());
  assert.equal(r.status, 400);
  r = await h(post("/api/v1/messages", { access_key: KEY_ALICE, betas: "x", request: msgRequest() }), makeEnv());
  assert.equal(r.status, 400);
});

test("messages: ANTHROPIC_VERSION var overrides the version header", async () => {
  const f = sseUpstream();
  const h = makeHandler({ fetch: f });
  await (await h(post("/api/v1/messages", { access_key: KEY_ALICE, request: msgRequest() }), makeEnv({ ANTHROPIC_VERSION: "2023-06-01" }))).text();
  assert.equal(f.calls[0].init.headers["anthropic-version"], "2023-06-01");
});

test("messages: body over MAX_BODY_MB is 413 (content-length and streamed)", async () => {
  const f = mockFetch(() => assert.fail("must not reach upstream"));
  const h = makeHandler({ fetch: f });
  const big = msgRequest({ messages: [{ role: "user", content: "x".repeat(1_200_000) }] });
  let r = await h(post("/api/v1/messages", { access_key: KEY_ALICE, request: big }), makeEnv({ MAX_BODY_MB: "1" }));
  assert.equal(r.status, 413);
  // Without content-length: a streamed body is counted as it is read.
  const req = new Request("https://relay.example.workers.dev/api/v1/messages", {
    method: "POST",
    headers: { "content-type": "application/json", origin: ORIGIN },
    body: streamOf([JSON.stringify({ access_key: KEY_ALICE, request: big })]),
    duplex: "half",
  });
  r = await h(req, makeEnv({ MAX_BODY_MB: "1" }));
  assert.equal(r.status, 413);
});

test("messages: upstream errors pass through with status and provider body", async () => {
  const body = '{"type":"error","error":{"type":"rate_limit_error","message":"Rate limited"}}';
  const f = mockFetch(() => new Response(body, { status: 429, headers: { "content-type": "application/json", "retry-after": "17" } }));
  const h = makeHandler({ fetch: f });
  const r = await h(post("/api/v1/messages", { access_key: KEY_ALICE, request: msgRequest() }), makeEnv());
  assert.equal(r.status, 429);
  assert.equal(r.headers.get("retry-after"), "17");
  assert.equal(await r.text(), body);
});

test("messages: upstream 401 (owner key bad) becomes a generic 502", async () => {
  const f = mockFetch(() => new Response('{"type":"error","error":{"type":"authentication_error","message":"invalid x-api-key"}}', { status: 401 }));
  const h = makeHandler({ fetch: f });
  const r = await h(post("/api/v1/messages", { access_key: KEY_ALICE, request: msgRequest() }), makeEnv());
  assert.equal(r.status, 502);
  const t = await r.text();
  assert.ok(!t.includes("x-api-key"));
  assert.equal(JSON.parse(t).error.type, "not_configured");
});

test("messages: upstream network failure is a generic 502", async () => {
  const f = mockFetch(() => {
    throw new Error("ECONNRESET secret detail");
  });
  const h = makeHandler({ fetch: f });
  const r = await h(post("/api/v1/messages", { access_key: KEY_ALICE, request: msgRequest() }), makeEnv());
  assert.equal(r.status, 502);
  assert.ok(!(await r.text()).includes("secret detail"));
});

test("messages: missing ANTHROPIC_API_KEY is not_configured", async () => {
  const h = makeHandler({ fetch: mockFetch(() => assert.fail()) });
  const r = await h(post("/api/v1/messages", { access_key: KEY_ALICE, request: msgRequest() }), makeEnv({ ANTHROPIC_API_KEY: undefined }));
  assert.equal(r.status, 500);
  assert.equal((await r.json()).error.type, "not_configured");
});

// --- counter -------------------------------------------------------------

test("counter: per key per month, works without KV, survives KV failure", async () => {
  const f = sseUpstream();
  const h = makeHandler({ fetch: f });
  const env = makeEnv();
  for (let i = 0; i < 3; i++) {
    const ctx = ctxMock();
    await (await h(post("/api/v1/messages", { access_key: KEY_BOB, request: msgRequest() }), env, ctx)).text();
    await ctx.settle();
  }
  const k = counterKey({ label: "bob", sha256: sha(KEY_BOB) });
  assert.match(k, /^count:\d{4}-\d{2}:bob:[0-9a-f]{8}$/);
  assert.equal(env.COUNTS.store.get(k), "3");
  assert.equal(env.COUNTS.store.size, 1, "the counter is the only thing stored");
  for (const v of env.COUNTS.store.values()) assert.match(v, /^\d+$/);

  // /check does not count.
  await h(post("/api/v1/check", { access_key: KEY_BOB }), env, ctxMock());
  assert.equal(env.COUNTS.store.get(k), "3");

  // No KV binding.
  let r = await h(post("/api/v1/messages", { access_key: KEY_BOB, request: msgRequest() }), makeEnv({ COUNTS: undefined }));
  assert.equal(r.status, 200);
  await r.text();

  // Broken KV.
  const broken = { get: async () => { throw new Error("kv down"); }, put: async () => {} };
  const ctx = ctxMock();
  r = await h(post("/api/v1/messages", { access_key: KEY_BOB, request: msgRequest() }), makeEnv({ COUNTS: broken }), ctx);
  assert.equal(r.status, 200);
  await r.text();
  await ctx.settle();
});

test("counterKey sanitises labels", () => {
  const k = counterKey({ label: "Aunt May / phone", sha256: "ab".repeat(32) }, new Date("2026-11-16T00:00:00Z"));
  assert.equal(k, "count:2026-11:Aunt_May___phone:abababab");
});

// --- routing -------------------------------------------------------------

test("routing: unknown path 404, wrong method 405, health has no secrets", async () => {
  const h = makeHandler({});
  let r = await h(post("/api/v1/nope", {}), makeEnv());
  assert.equal(r.status, 404);
  r = await h(new Request("https://relay.example.workers.dev/api/v1/check", { method: "GET", headers: { origin: ORIGIN } }), makeEnv());
  assert.equal(r.status, 405);
  r = await h(new Request("https://relay.example.workers.dev/api/v1/health"), makeEnv());
  assert.equal(r.status, 200);
  const t = await r.text();
  const j = JSON.parse(t);
  assert.equal(j.configured.anthropic_api_key, true);
  assert.equal(j.configured.access_keys, 2);
  assert.ok(j.configured.sources > 0);
  assert.ok(!t.includes("sk-ant") && !t.includes(sha(KEY_ALICE)));
});

test("default export uses globalThis.fetch", async () => {
  const realFetch = globalThis.fetch;
  const f = sseUpstream();
  globalThis.fetch = f;
  try {
    const r = await worker.fetch(post("/api/v1/messages", { access_key: KEY_ALICE, request: msgRequest() }), makeEnv(), ctxMock());
    assert.equal(r.status, 200);
    assert.equal(await r.text(), SSE.join(""));
    assert.equal(f.calls.length, 1);
  } finally {
    globalThis.fetch = realFetch;
  }
});

test("source contains no console calls", async () => {
  const { readFile } = await import("node:fs/promises");
  for (const f of ["../src/index.js", "../src/relay.js"]) {
    const src = await readFile(new URL(f, import.meta.url), "utf8");
    assert.ok(!/console\s*\./.test(src), f);
  }
});

test("entry module exports only the default handler (Workers rule)", async () => {
  const mod = await import("../src/index.js");
  assert.deepEqual(Object.keys(mod), ["default"]);
  assert.equal(typeof mod.default.fetch, "function");
});

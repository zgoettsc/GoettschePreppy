// GoettschePreppy relay logic. worker/src/index.js is the Worker entry point.
// One Cloudflare Worker, no storage except a per-key monthly request counter in
// Workers KV (binding COUNTS, optional).
//
// Routes (all POST, JSON body, CORS restricted to env PAGES_ORIGIN):
//   /api/v1/check      {access_key}                  -> 200 {ok:true,label} | 401
//   /api/v1/messages   {access_key, request, betas?} -> Anthropic Messages API, streamed back unchanged
//   /api/v1/fetch      {access_key, source_key}      -> bytes of a source in the bundled index
//   /api/v1/fetch-map  {access_key, url}             -> bytes of a USGS topo map (host allowlist)
//   GET /api/v1/health                               -> {ok:true, configured:{...}} (no secrets)
//
// Privacy rules this file keeps (decision G18, NOTICE-TO-USERS.md):
//   - It never logs. There is no console call anywhere in this file.
//   - It never stores a request or response body. The only write is the counter.
//   - Errors are generic: {type:"error", error:{type, message}}; no stack, no internals.
//
// Secrets (wrangler secret put): ANTHROPIC_API_KEY, ACCESS_KEYS (JSON array of {label, sha256}).
// Vars (wrangler.toml [vars]): PAGES_ORIGIN, MAX_TOKENS, FETCH_MAX_MB, MAP_MAX_MB, MAX_BODY_MB,
//   ANTHROPIC_VERSION, ALLOW_FAST_MODE, FALLBACK_MODELS.

import BUNDLED_SOURCE_URLS from "./source-urls.json" with { type: "json" };

export const MODEL = "claude-opus-5-5";
export const ANTHROPIC_URL = "https://api.anthropic.com/v1/messages";
export const DEFAULT_ANTHROPIC_VERSION = "2026-10-21";
const DEFAULT_MAX_TOKENS = 32000;
const DEFAULT_FETCH_MAX_MB = 60;
const DEFAULT_MAP_MAX_MB = 100;
const DEFAULT_MAX_BODY_MB = 8; // a Messages request with the cached template corpus
const SMALL_BODY_BYTES = 16 * 1024; // check / fetch / fetch-map bodies
const MAX_REDIRECTS = 3;
const HEADER_TIMEOUT_MS = 60_000; // time allowed for an upstream source to start answering
const DEFAULT_FALLBACK_MODELS = ["claude-opus-5", "claude-opus-4-8"];
const FETCH_USER_AGENT = "Mozilla/5.0 (compatible; offline-binder-relay/1.0)";

// Request fields the relay refuses outright. `thread` keeps the conversation on
// the provider's side (storage); `mcp_servers` and `container` would let a
// caller point the model at arbitrary servers or run billed sandboxes.
const FORBIDDEN_REQUEST_FIELDS = ["thread", "mcp_servers", "container"];

// USGS topo map download hosts (decision G16). Checked for the first URL and
// for every redirect. See docs/10-deploy.md, "Map hosts".
//   prd-tnm.s3.amazonaws.com            The National Map staged products bucket. US Topo
//                                       GeoPDFs: /StagedProducts/Maps/USTopo/PDF/<ST>/...,
//                                       historical topos: /StagedProducts/Maps/HistoricalTopo/...
//                                       (the TNM Access API returns these as downloadURL).
//   prd-tnm.s3.us-west-2.amazonaws.com  Same bucket, regional endpoint name.
//   tnmaccess.nationalmap.gov           TNM Access API (JSON search: /api/v1/products?...).
//   rockyweb.usgs.gov                   Legacy staged-products mirror (/vdelivery/Datasets/Staged/...).
export const MAP_HOSTS = {
  "prd-tnm.s3.amazonaws.com": ["/StagedProducts/"],
  "prd-tnm.s3.us-west-2.amazonaws.com": ["/StagedProducts/"],
  "tnmaccess.nationalmap.gov": ["/api/v1/"],
  "rockyweb.usgs.gov": ["/vdelivery/"],
};

// ---------------------------------------------------------------------------
// Errors

class RelayError extends Error {
  constructor(status, type, message, extra) {
    super(message);
    this.status = status;
    this.type = type;
    this.extra = extra;
  }
}

const GENERIC = {
  invalid_request: "The request was not valid.",
  unauthorized: "Access key not recognised.",
  forbidden: "Not allowed.",
  not_found: "Not found.",
  method_not_allowed: "Method not allowed.",
  payload_too_large: "Too large.",
  not_configured: "The relay is not set up yet. Tell the owner.",
  upstream_error: "The upstream service did not answer correctly.",
  internal: "Something went wrong in the relay.",
};

function err(status, type, message, extra) {
  return new RelayError(status, type, message || GENERIC[type] || GENERIC.internal, extra);
}

function jsonResponse(status, obj, headers = {}) {
  return new Response(JSON.stringify(obj), {
    status,
    headers: { "content-type": "application/json; charset=utf-8", "cache-control": "no-store", ...headers },
  });
}

function errorResponse(e) {
  if (e instanceof RelayError) {
    return jsonResponse(e.status, { type: "error", error: { type: e.type, message: e.message, ...(e.extra || {}) } });
  }
  return jsonResponse(500, { type: "error", error: { type: "internal", message: GENERIC.internal } });
}

// ---------------------------------------------------------------------------
// Small helpers

function numEnv(env, name, dflt) {
  const v = env && env[name] !== undefined && env[name] !== "" ? Number(env[name]) : NaN;
  return Number.isFinite(v) && v > 0 ? v : dflt;
}

function hex(buf) {
  const b = new Uint8Array(buf);
  let s = "";
  for (let i = 0; i < b.length; i++) s += b[i].toString(16).padStart(2, "0");
  return s;
}

export async function sha256Hex(text) {
  return hex(await crypto.subtle.digest("SHA-256", new TextEncoder().encode(text)));
}

// Constant-time comparison of two equal-length strings (hex digests). Runs over
// every character regardless of where the first difference is.
export function timingSafeEqualStr(a, b) {
  if (typeof a !== "string" || typeof b !== "string") return false;
  let diff = a.length ^ b.length;
  for (let i = 0; i < a.length; i++) {
    diff |= a.charCodeAt(i) ^ (i < b.length ? b.charCodeAt(i) : 0);
  }
  return diff === 0;
}

let keysCache = { raw: null, list: null };
function accessKeyList(env) {
  const raw = env && env.ACCESS_KEYS;
  if (typeof raw !== "string" || !raw.trim()) throw err(500, "not_configured");
  if (keysCache.raw === raw) return keysCache.list;
  let parsed;
  try {
    parsed = JSON.parse(raw);
  } catch {
    throw err(500, "not_configured");
  }
  if (!Array.isArray(parsed)) throw err(500, "not_configured");
  const list = [];
  for (const e of parsed) {
    if (!e || typeof e.sha256 !== "string" || !/^[0-9a-fA-F]{64}$/.test(e.sha256)) continue;
    list.push({ label: typeof e.label === "string" && e.label ? e.label : "friend", sha256: e.sha256.toLowerCase() });
  }
  if (list.length === 0) throw err(500, "not_configured");
  keysCache = { raw, list };
  return list;
}

// Returns the matching {label, sha256} or throws 401. Compares against every
// entry (no early exit) in constant time per entry.
async function authenticate(env, accessKey) {
  const list = accessKeyList(env);
  if (typeof accessKey !== "string" || accessKey.length < 16 || accessKey.length > 256) throw err(401, "unauthorized");
  const h = await sha256Hex(accessKey);
  let found = null;
  for (const entry of list) {
    const eq = timingSafeEqualStr(h, entry.sha256);
    if (eq && found === null) found = entry;
  }
  if (!found) throw err(401, "unauthorized");
  return found;
}

function monthKey(date = new Date()) {
  return date.toISOString().slice(0, 7);
}

// count:<YYYY-MM>:<label>:<first 8 hex of the key hash>. A count, nothing else.
export function counterKey(entry, date) {
  const label = entry.label.replace(/[^A-Za-z0-9_.-]/g, "_").slice(0, 40);
  return `count:${monthKey(date)}:${label}:${entry.sha256.slice(0, 8)}`;
}

function bumpCounter(env, ctx, entry) {
  const kv = env && env.COUNTS;
  if (!kv || typeof kv.get !== "function") return;
  const key = counterKey(entry);
  const work = (async () => {
    try {
      const n = Number(await kv.get(key)) || 0;
      await kv.put(key, String(n + 1));
    } catch {
      // A counter failure must never fail the request.
    }
  })();
  if (ctx && typeof ctx.waitUntil === "function") ctx.waitUntil(work);
  return work;
}

async function readBodyCapped(request, cap) {
  const cl = request.headers.get("content-length");
  if (cl !== null && Number(cl) > cap) throw err(413, "payload_too_large");
  if (!request.body) return "";
  const reader = request.body.getReader();
  const chunks = [];
  let total = 0;
  for (;;) {
    const { done, value } = await reader.read();
    if (done) break;
    total += value.byteLength;
    if (total > cap) {
      try {
        await reader.cancel();
      } catch {}
      throw err(413, "payload_too_large");
    }
    chunks.push(value);
  }
  const all = new Uint8Array(total);
  let off = 0;
  for (const c of chunks) {
    all.set(c, off);
    off += c.byteLength;
  }
  return new TextDecoder().decode(all);
}

async function readJson(request, cap) {
  const ct = request.headers.get("content-type") || "";
  if (!/^application\/json\b/i.test(ct)) throw err(400, "invalid_request", "Send JSON (content-type: application/json).");
  const text = await readBodyCapped(request, cap);
  let body;
  try {
    body = JSON.parse(text);
  } catch {
    throw err(400, "invalid_request", "The body is not valid JSON.");
  }
  if (!body || typeof body !== "object" || Array.isArray(body)) throw err(400, "invalid_request");
  return body;
}

// ---------------------------------------------------------------------------
// CORS

function allowedOrigins(env) {
  return String((env && env.PAGES_ORIGIN) || "")
    .split(",")
    .map((s) => s.trim().replace(/\/+$/, ""))
    .filter(Boolean);
}

// Returns {ok, headers}. A request with no Origin header (curl, scripts) is not
// a browser request; CORS does not apply and no CORS headers are sent. A
// browser request from any origin other than PAGES_ORIGIN is refused.
function cors(request, env) {
  const origin = request.headers.get("origin");
  if (!origin) return { ok: true, headers: {} };
  if (!allowedOrigins(env).includes(origin)) return { ok: false, headers: {} };
  return {
    ok: true,
    headers: {
      "access-control-allow-origin": origin,
      "access-control-allow-methods": "POST, GET, OPTIONS",
      "access-control-allow-headers": "content-type, anthropic-beta",
      "access-control-expose-headers": "content-type, content-length, request-id, retry-after, x-relay-max-tokens",
      "access-control-max-age": "600",
      vary: "Origin",
    },
  };
}

function withHeaders(response, extra) {
  const h = new Headers(response.headers);
  for (const [k, v] of Object.entries(extra)) h.set(k, v);
  return new Response(response.body, { status: response.status, statusText: response.statusText, headers: h });
}

// ---------------------------------------------------------------------------
// URL safety

function ipv4Private(host) {
  const m = /^(\d+)\.(\d+)\.(\d+)\.(\d+)$/.exec(host);
  if (!m) return false;
  const [a, b] = [Number(m[1]), Number(m[2])];
  return (
    a === 0 ||
    a === 10 ||
    a === 127 ||
    (a === 100 && b >= 64 && b <= 127) ||
    (a === 169 && b === 254) ||
    (a === 172 && b >= 16 && b <= 31) ||
    (a === 192 && b === 168) ||
    (a === 192 && b === 0) ||
    (a === 198 && (b === 18 || b === 19)) ||
    a >= 224
  );
}

// Throws unless the URL is http(s), on a default port, without credentials,
// and not a loopback / private / link-local / internal address. IPv6 literals
// are refused entirely (no source in the index uses one). Cloudflare Workers
// cannot reach private networks anyway; this is the second lock.
export function assertPublicHttpUrl(u, { httpsOnly = false } = {}) {
  if (!(u instanceof URL)) throw err(400, "invalid_request");
  if (u.protocol !== "https:" && (httpsOnly || u.protocol !== "http:")) throw err(403, "forbidden");
  if (u.username || u.password || u.port) throw err(403, "forbidden");
  const host = u.hostname.toLowerCase();
  if (!host || host.startsWith("[") || host.includes(":")) throw err(403, "forbidden");
  if (ipv4Private(host)) throw err(403, "forbidden");
  if (!host.includes(".")) throw err(403, "forbidden");
  if (
    host === "localhost" ||
    /\.(localhost|local|internal|lan|home\.arpa|intranet|corp)$/.test(host)
  )
    throw err(403, "forbidden");
  return u;
}

function mapUrlAllowed(u) {
  if (u.protocol !== "https:") return false;
  const prefixes = MAP_HOSTS[u.hostname.toLowerCase()];
  if (!prefixes) return false;
  return prefixes.some((p) => u.pathname.startsWith(p));
}

const REDIRECTS = new Set([301, 302, 303, 307, 308]);

// GET with manual redirects: at most MAX_REDIRECTS, each hop re-checked.
async function fetchFollowing(fetchImpl, startUrl, checkHop) {
  let current = startUrl;
  for (let hop = 0; ; hop++) {
    checkHop(current);
    const ac = new AbortController();
    const timer = setTimeout(() => ac.abort(), HEADER_TIMEOUT_MS);
    let res;
    try {
      res = await fetchImpl(current.href, {
        method: "GET",
        redirect: "manual",
        signal: ac.signal,
        headers: { "user-agent": FETCH_USER_AGENT, accept: "*/*" },
      });
    } catch {
      throw err(502, "upstream_error");
    } finally {
      clearTimeout(timer);
    }
    if (REDIRECTS.has(res.status)) {
      const loc = res.headers.get("location");
      try {
        if (res.body) await res.body.cancel();
      } catch {}
      if (!loc || hop >= MAX_REDIRECTS) throw err(502, "upstream_error", "Too many redirects.");
      let next;
      try {
        next = new URL(loc, current);
      } catch {
        throw err(502, "upstream_error");
      }
      next.hash = "";
      current = next;
      continue;
    }
    return res;
  }
}

function capStream(body, maxBytes) {
  let seen = 0;
  return body.pipeThrough(
    new TransformStream({
      transform(chunk, controller) {
        seen += chunk.byteLength;
        if (seen > maxBytes) {
          controller.error(new Error("size cap"));
          return;
        }
        controller.enqueue(chunk);
      },
    }),
  );
}

// Stream the upstream bytes back with its content-type, under a size cap.
function passBytes(res, maxBytes, corsHeaders) {
  if (!res.ok) {
    try {
      if (res.body) res.body.cancel();
    } catch {}
    throw err(502, "upstream_error", GENERIC.upstream_error, { upstream_status: res.status });
  }
  const headers = {
    "content-type": res.headers.get("content-type") || "application/octet-stream",
    "cache-control": "no-store",
    "x-content-type-options": "nosniff",
    ...corsHeaders,
  };
  const cl = res.headers.get("content-length");
  if (cl !== null && /^\d+$/.test(cl)) {
    if (Number(cl) > maxBytes) {
      try {
        if (res.body) res.body.cancel();
      } catch {}
      throw err(413, "payload_too_large", "The document is larger than the relay's size limit.");
    }
    // Length is known and under the cap: pass the stream straight through
    // (no per-chunk JavaScript, which keeps Worker CPU time near zero).
    headers["content-length"] = cl;
    return new Response(res.body, { status: 200, headers });
  }
  return new Response(res.body ? capStream(res.body, maxBytes) : null, { status: 200, headers });
}

// ---------------------------------------------------------------------------
// Messages

const BETA_TOKEN = /^[a-z0-9][a-z0-9-]{0,63}$/;

function betaHeader(request, body) {
  const list = [];
  const fromHeader = request.headers.get("anthropic-beta");
  if (fromHeader) list.push(...fromHeader.split(","));
  if (Array.isArray(body.betas)) list.push(...body.betas);
  else if (body.betas !== undefined) throw err(400, "invalid_request", "betas must be an array of strings.");
  const clean = [];
  for (const raw of list) {
    if (typeof raw !== "string") throw err(400, "invalid_request", "betas must be an array of strings.");
    const t = raw.trim();
    if (!t) continue;
    if (!BETA_TOKEN.test(t)) throw err(400, "invalid_request", "A beta name is not valid.");
    if (!clean.includes(t)) clean.push(t);
  }
  if (clean.length > 10) throw err(400, "invalid_request", "Too many betas.");
  return clean.join(",");
}

export function vetMessagesRequest(req, env) {
  if (!req || typeof req !== "object" || Array.isArray(req)) throw err(400, "invalid_request", "request must be a Messages API body.");
  if (req.model !== MODEL) throw err(400, "invalid_request", `model must be "${MODEL}".`);
  if (!Array.isArray(req.messages) || req.messages.length === 0) throw err(400, "invalid_request", "request.messages is required.");
  for (const f of FORBIDDEN_REQUEST_FIELDS) {
    if (req[f] !== undefined) throw err(400, "invalid_request", `request.${f} is not allowed through this relay.`);
  }
  if (req.speed !== undefined && req.speed !== "standard" && String(env.ALLOW_FAST_MODE || "") !== "1") {
    throw err(400, "invalid_request", "Fast mode is not allowed through this relay.");
  }
  if (req.fallbacks !== undefined) {
    const allowed = String(env.FALLBACK_MODELS || "").trim()
      ? String(env.FALLBACK_MODELS).split(",").map((s) => s.trim()).filter(Boolean)
      : DEFAULT_FALLBACK_MODELS;
    if (!Array.isArray(req.fallbacks) || req.fallbacks.some((f) => !f || !allowed.includes(f.model))) {
      throw err(400, "invalid_request", `fallbacks must be an array naming only: ${allowed.join(", ")}.`);
    }
  }
  const cap = Math.floor(numEnv(env, "MAX_TOKENS", DEFAULT_MAX_TOKENS));
  if (!Number.isInteger(req.max_tokens) || req.max_tokens < 0) throw err(400, "invalid_request", "request.max_tokens must be a whole number.");
  let capped = false;
  if (req.max_tokens > cap) {
    req.max_tokens = cap;
    capped = true;
  }
  return { capped, cap };
}

async function handleMessages(request, env, ctx, deps, corsHeaders) {
  const body = await readJson(request, Math.floor(numEnv(env, "MAX_BODY_MB", DEFAULT_MAX_BODY_MB) * 1024 * 1024));
  const entry = await authenticate(env, body.access_key);
  if (typeof env.ANTHROPIC_API_KEY !== "string" || !env.ANTHROPIC_API_KEY) throw err(500, "not_configured");
  const req = body.request;
  const { capped, cap } = vetMessagesRequest(req, env);
  const beta = betaHeader(request, body);

  const headers = {
    "content-type": "application/json",
    "x-api-key": env.ANTHROPIC_API_KEY,
    "anthropic-version": (env.ANTHROPIC_VERSION && String(env.ANTHROPIC_VERSION)) || DEFAULT_ANTHROPIC_VERSION,
  };
  if (beta) headers["anthropic-beta"] = beta;

  bumpCounter(env, ctx, entry);

  let upstream;
  try {
    // JSON.stringify of the parsed body keeps key order and every field
    // (cache_control breakpoints included), so prompt caching is unaffected.
    upstream = await deps.fetch(ANTHROPIC_URL, { method: "POST", headers, body: JSON.stringify(req) });
  } catch {
    throw err(502, "upstream_error");
  }

  if (upstream.status === 401 || upstream.status === 403) {
    // The owner's API key is wrong or revoked. Do not pass the provider's
    // message through; say only that the owner must fix it.
    try {
      if (upstream.body) upstream.body.cancel();
    } catch {}
    throw err(502, "not_configured", "The relay's API key was refused. Tell the owner.");
  }

  // Everything else (2xx SSE or JSON, 400, 413, 429, 500, 529) passes through
  // unchanged: same status, same body bytes. The browser needs the provider's
  // error type (rate_limit_error, overloaded_error, invalid_request_error).
  const out = new Headers({ "cache-control": "no-store", ...corsHeaders });
  for (const h of ["content-type", "request-id", "retry-after", "x-should-retry"]) {
    const v = upstream.headers.get(h);
    if (v !== null) out.set(h, v);
  }
  if (!out.has("content-type")) out.set("content-type", "application/json");
  if (capped) out.set("x-relay-max-tokens", String(cap));
  return new Response(upstream.body, { status: upstream.status, headers: out });
}

// ---------------------------------------------------------------------------
// Router

export function makeHandler(deps = {}) {
  const getFetch = () => deps.fetch || globalThis.fetch.bind(globalThis);
  const sourceUrls = deps.sourceUrls || BUNDLED_SOURCE_URLS;

  return async function fetchHandler(request, env = {}, ctx) {
    const c = cors(request, env);
    try {
      const url = new URL(request.url);
      if (!c.ok) throw err(403, "forbidden", "This origin may not use the relay.");

      if (request.method === "OPTIONS") {
        return new Response(null, { status: 204, headers: c.headers });
      }

      const path = url.pathname;
      const run = deps.fetch ? deps : { ...deps, fetch: getFetch() };

      if (path === "/api/v1/health") {
        if (request.method !== "GET") throw err(405, "method_not_allowed");
        let keys = 0;
        try {
          keys = accessKeyList(env).length;
        } catch {}
        return jsonResponse(
          200,
          {
            ok: true,
            configured: {
              anthropic_api_key: typeof env.ANTHROPIC_API_KEY === "string" && env.ANTHROPIC_API_KEY.length > 0,
              access_keys: keys,
              counts: !!(env.COUNTS && typeof env.COUNTS.get === "function"),
              pages_origin: allowedOrigins(env).length > 0,
              sources: Object.keys(sourceUrls).length,
            },
          },
          c.headers,
        );
      }

      const routes = ["/api/v1/check", "/api/v1/messages", "/api/v1/fetch", "/api/v1/fetch-map"];
      if (!routes.includes(path)) throw err(404, "not_found");
      if (request.method !== "POST") throw err(405, "method_not_allowed");

      if (path === "/api/v1/messages") return await handleMessages(request, env, ctx, run, c.headers);

      const body = await readJson(request, SMALL_BODY_BYTES);
      const entry = await authenticate(env, body.access_key);

      if (path === "/api/v1/check") {
        return jsonResponse(200, { ok: true, label: entry.label }, c.headers);
      }

      if (path === "/api/v1/fetch") {
        const key = body.source_key;
        if (typeof key !== "string" || !key || key.length > 200) throw err(400, "invalid_request", "source_key is required.");
        if (!Object.prototype.hasOwnProperty.call(sourceUrls, key)) throw err(404, "not_found", "Unknown source.");
        let start;
        try {
          start = new URL(sourceUrls[key]);
        } catch {
          throw err(404, "not_found", "Unknown source.");
        }
        bumpCounter(env, ctx, entry);
        const res = await fetchFollowing(run.fetch, start, (u) => assertPublicHttpUrl(u));
        return passBytes(res, numEnv(env, "FETCH_MAX_MB", DEFAULT_FETCH_MAX_MB) * 1024 * 1024, c.headers);
      }

      // /api/v1/fetch-map
      if (typeof body.url !== "string" || body.url.length > 2048) throw err(400, "invalid_request", "url is required.");
      let start;
      try {
        start = new URL(body.url);
      } catch {
        throw err(400, "invalid_request", "url is not valid.");
      }
      const checkMap = (u) => {
        assertPublicHttpUrl(u, { httpsOnly: true });
        if (!mapUrlAllowed(u)) throw err(403, "forbidden", "Only USGS map hosts are allowed.");
      };
      checkMap(start);
      bumpCounter(env, ctx, entry);
      const res = await fetchFollowing(run.fetch, start, checkMap);
      return passBytes(res, numEnv(env, "MAP_MAX_MB", DEFAULT_MAP_MAX_MB) * 1024 * 1024, c.headers);
    } catch (e) {
      const r = errorResponse(e);
      return Object.keys(c.headers).length ? withHeaders(r, c.headers) : r;
    }
  };
}


// Shared test helpers. No network: every upstream call goes to a mock fetch.
import { createHash } from "node:crypto";

export const ORIGIN = "https://goettschepreppy.pages.dev";
export const KEY_ALICE = "gpk_alice_0123456789abcdefghijklmnopqrstuvwxyz";
export const KEY_BOB = "gpk_bob_0123456789abcdefghijklmnopqrstuvwxyzAB";
export const sha = (s) => createHash("sha256").update(s, "utf8").digest("hex");

export function kvMock() {
  const store = new Map();
  return {
    store,
    async get(k) {
      return store.has(k) ? store.get(k) : null;
    },
    async put(k, v) {
      store.set(k, v);
    },
  };
}

export function makeEnv(over = {}) {
  return {
    ANTHROPIC_API_KEY: "sk-ant-test-not-a-real-key",
    ACCESS_KEYS: JSON.stringify([
      { label: "alice", sha256: sha(KEY_ALICE) },
      { label: "bob", sha256: sha(KEY_BOB) },
    ]),
    PAGES_ORIGIN: ORIGIN,
    COUNTS: kvMock(),
    ...over,
  };
}

export function ctxMock() {
  const pending = [];
  return {
    pending,
    waitUntil(p) {
      pending.push(p);
    },
    async settle() {
      await Promise.all(pending);
    },
  };
}

export function post(path, body, { origin = ORIGIN, headers = {}, raw } = {}) {
  const h = { "content-type": "application/json", ...headers };
  if (origin) h.origin = origin;
  return new Request(`https://relay.example.workers.dev${path}`, {
    method: "POST",
    headers: h,
    body: raw !== undefined ? raw : JSON.stringify(body),
  });
}

// A mock fetch that records calls and answers from a route function.
export function mockFetch(route) {
  const calls = [];
  const fn = async (url, init = {}) => {
    calls.push({ url: String(url), init });
    return route(String(url), init, calls.length);
  };
  fn.calls = calls;
  return fn;
}

export function streamOf(chunks) {
  const enc = new TextEncoder();
  return new ReadableStream({
    start(c) {
      for (const ch of chunks) c.enqueue(typeof ch === "string" ? enc.encode(ch) : ch);
      c.close();
    },
  });
}

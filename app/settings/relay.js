// Access-key check against the relay (docs: notes/APP-BRIEF.md, Relay interface).
// POST {relayBase}/api/v1/check {access_key} -> 200 {ok:true,label} | 401.
// The key is sent only to the relay and kept only in this tab's memory.

import { config } from './config.js';

export async function checkAccessKey(accessKey, { signal } = {}) {
  let res;
  try {
    res = await fetch(`${config.relayBase}/api/v1/check`, {
      method: 'POST',
      headers: { 'content-type': 'application/json' },
      body: JSON.stringify({ access_key: accessKey }),
      cache: 'no-store',
      credentials: 'omit',
      signal,
    });
  } catch (err) {
    if (err && err.name === 'AbortError') throw err;
    return { ok: false, reason: 'unreachable' };
  }
  if (res.status === 401) return { ok: false, reason: 'rejected' };
  // 403 = the relay refused this page's address (its PAGES_ORIGIN does not list this site)
  if (res.status === 403) return { ok: false, reason: 'forbidden' };
  if (!res.ok) return { ok: false, reason: 'unreachable', status: res.status };
  let body = {};
  try { body = await res.json(); } catch { /* empty body */ }
  if (body && body.ok === true) return { ok: true, label: typeof body.label === 'string' ? body.label : '' };
  return { ok: false, reason: 'rejected' };
}

// relay-dryrun.js — a fake relay for tests and for trying the settings page without a key.
//
//   createDryRunRelay(opts) → same interface as createRelay() (relay-client.js)
//
// It is not a mock of the client: it is a fake *server* (a fetch function) that answers the four
// relay endpoints, and the real relay client talks to it. So every test run exercises the client's
// request building, SSE parsing (events are cut into random-sized chunks) and retries.
//
// Canned answers:
//   /check      any key of 8+ characters is accepted, except "bad-key-0000".
//   /messages   structured-output requests (output_config.format) → {"findings": [...]} with one
//               mechanical finding when the batch contains the text "DRYRUN-TYPO"; other requests
//               → a short plain paragraph built only from the request's own words (no digits).
//               The first request is answered 529 overloaded once to exercise the retry path when
//               opts.flaky is set.
//   /fetch      public-domain-ish keys → a small HTML document; keys containing "pdf" → a tiny PDF;
//               licence class "blocked" (per opts.blocked set) → 403.
//   /fetch-map  → 403 (maps are never faked).

import { createRelay } from './relay-client.js';

const enc = new TextEncoder();

function sseResponse(events, seed = 1) {
  const text = events.map(([ev, data]) => `event: ${ev}\ndata: ${JSON.stringify(data)}\n\n`).join('');
  let s = seed;
  const rnd = () => (s = (s * 1103515245 + 12345) % 2147483648) / 2147483648;
  const stream = new ReadableStream({
    start(c) {
      let i = 0;
      while (i < text.length) { const n = 1 + Math.floor(rnd() * 90); c.enqueue(enc.encode(text.slice(i, i + n))); i += n; }
      c.close();
    },
  });
  return new Response(stream, { status: 200, headers: { 'content-type': 'text/event-stream' } });
}

function messageEvents(text, { thinking = true } = {}) {
  const ev = [['message_start', { type: 'message_start', message: { id: 'msg_dryrun', type: 'message', role: 'assistant', model: 'claude-opus-5-5', content: [], usage: { input_tokens: 10, cache_read_input_tokens: 0, output_tokens: 1 } } }]];
  let idx = 0;
  if (thinking) {
    ev.push(['content_block_start', { type: 'content_block_start', index: idx, content_block: { type: 'thinking', thinking: '' } }]);
    ev.push(['content_block_delta', { type: 'content_block_delta', index: idx, delta: { type: 'signature_delta', signature: 'dryrun' } }]);
    ev.push(['content_block_stop', { type: 'content_block_stop', index: idx }]);
    idx++;
  }
  ev.push(['content_block_start', { type: 'content_block_start', index: idx, content_block: { type: 'text', text: '' } }]);
  ev.push(['ping', { type: 'ping' }]);
  for (let i = 0; i < text.length; i += 17) ev.push(['content_block_delta', { type: 'content_block_delta', index: idx, delta: { type: 'text_delta', text: text.slice(i, i + 17) } }]);
  ev.push(['content_block_stop', { type: 'content_block_stop', index: idx }]);
  ev.push(['message_delta', { type: 'message_delta', delta: { stop_reason: 'end_turn', stop_sequence: null }, usage: { output_tokens: Math.ceil(text.length / 4) } }]);
  ev.push(['message_stop', { type: 'message_stop' }]);
  return ev;
}

const TINY_PDF = '%PDF-1.4\n1 0 obj<</Type/Catalog/Pages 2 0 R>>endobj 2 0 obj<</Type/Pages/Count 0/Kids[]>>endobj\ntrailer<</Root 1 0 R>>\n%%EOF\n';

export function dryRunFetch(opts = {}) {
  const calls = { check: 0, messages: 0, fetch: 0, map: 0, requests: [] };
  let flaky = !!opts.flaky;
  const fn = async (url, init) => {
    const path = String(url).replace(/^.*\/api\/v1/, '');
    const body = JSON.parse(init.body);
    if (!body.access_key || body.access_key.length < 8 || body.access_key === 'bad-key-0000')
      return new Response(JSON.stringify({ error: 'unauthorised' }), { status: 401 });
    if (path === '/check') { calls.check++; return Response.json({ ok: true, label: 'dry-run' }); }
    if (path === '/messages') {
      calls.messages++;
      const req = body.request;
      calls.requests.push(req);
      if (req.model !== 'claude-opus-5-5') return new Response(JSON.stringify({ error: { type: 'invalid_request_error', message: 'model' } }), { status: 400 });
      if (flaky) { flaky = false; return new Response(JSON.stringify({ error: { type: 'overloaded_error', message: 'Overloaded' } }), { status: 529 }); }
      const userText = JSON.stringify(req.messages);
      let out;
      if (req.output_config?.format) {
        const findings = [];
        const m = /"page_id\\?":\s*\\?"([0-9]{2}-[0-9]{2}-[a-z0-9-]+)\\?"/.exec(userText) || /PAGE ([0-9]{2}-[0-9]{2}-[a-z0-9-]+)/.exec(userText);
        if (userText.includes('DRYRUN-TYPO')) findings.push({ page_id: m ? m[1] : '', pass: 'readability', severity: 'info', fixable: true, message: 'Dry run: a typo marker was found and fixed.', find: 'DRYRUN-TYPO', replace: 'dry-run check' });
        if (m) findings.push({ page_id: m[1], pass: 'consistency', severity: 'info', fixable: false, message: 'Dry run: no real review was done. This note proves the review notes page is wired.', find: '', replace: '' });
        out = JSON.stringify({ findings });
      } else {
        const id = (/Write the block "([a-z0-9-]+)"/.exec(userText) || [])[1] || 'block';
        out = `This paragraph is a dry-run stand-in for the "${id}" block. In a real build the model writes it from the household's own answers only, adding no numbers, phone numbers, laws or procedures of its own.`;
      }
      return sseResponse(messageEvents(out), calls.messages);
    }
    if (path === '/fetch') {
      calls.fetch++;
      const k = body.source_key;
      if (opts.blocked?.has(k) || /blocked/.test(k)) return new Response('refused', { status: 403 });
      if (/pdf/.test(k)) return new Response(enc.encode(TINY_PDF), { headers: { 'content-type': 'application/pdf' } });
      const html = `<html><head><title>${k}</title><script>var x=1</script></head><body><nav>menu</nav><h1>Dry-run copy of ${k}</h1><p>This stands in for the publisher's page. <a href="https://example.org/x">A link that must disappear</a> and www.example.org too.</p><ul><li>Item one</li></ul></body></html>`;
      return new Response(html, { headers: { 'content-type': 'text/html; charset=utf-8' } });
    }
    if (path === '/fetch-map') { calls.map++; return new Response('no', { status: 403 }); }
    return new Response('not found', { status: 404 });
  };
  fn.calls = calls;
  return fn;
}

export function createDryRunRelay(opts = {}) {
  const f = dryRunFetch(opts);
  const relay = createRelay({ base: 'dryrun:/api/v1', accessKey: opts.accessKey || 'dry-run-key-1234', fetch: f, backoffMs: 5 });
  relay.calls = f.calls;
  relay.dryRun = true;
  return relay;
}

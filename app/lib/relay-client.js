// relay-client.js — the browser's only door to the network: the A1 relay (worker/).
//
//   const relay = createRelay({ base: '/api/v1' | 'https://<worker>/api/v1', accessKey, fetch })
//   await relay.check()                                   → { ok, label }
//   await relay.messages(request, { onText, signal })     → final Message (content, stop_reason, usage)
//   await relay.fetchSource(key, { signal })              → { ok, status, contentType, bytes }
//   await relay.fetchMap(url, { signal })                 → same
//
// `request` is a Messages API body. The relay forwards it to the Anthropic API unchanged (after
// checking the key, the model and max_tokens) and streams the SSE response back unchanged, so this
// file parses Messages API server-sent events itself: message_start, content_block_start,
// content_block_delta (text_delta, thinking_delta, signature_delta, input_json_delta),
// content_block_stop, message_delta (stop_reason, usage), message_stop, ping, error.

export const MODEL = 'claude-opus-5-5';

export class RelayError extends Error {
  constructor(message, { status = 0, type = 'relay_error', retryable = false } = {}) {
    super(message); this.name = 'RelayError'; this.status = status; this.type = type; this.retryable = retryable;
  }
}

// ---- SSE ---------------------------------------------------------------------------------------
// Feed text chunks in any split; get whole events out.
export function createSSEParser(onEvent) {
  let buf = '';
  const flush = block => {
    let event = 'message', data = [];
    for (const line of block.split(/\r?\n/)) {
      if (!line || line.startsWith(':')) continue;
      const i = line.indexOf(':');
      const field = i < 0 ? line : line.slice(0, i);
      let value = i < 0 ? '' : line.slice(i + 1);
      if (value.startsWith(' ')) value = value.slice(1);
      if (field === 'event') event = value;
      else if (field === 'data') data.push(value);
    }
    if (data.length) onEvent(event, data.join('\n'));
  };
  return {
    push(chunk) {
      buf += chunk;
      let m;
      while ((m = /\r?\n\r?\n/.exec(buf))) { flush(buf.slice(0, m.index)); buf = buf.slice(m.index + m[0].length); }
    },
    end() { if (buf.trim()) flush(buf); buf = ''; },
  };
}

// Accumulate Messages API stream events into the final Message object.
export function createMessageAccumulator({ onText } = {}) {
  const msg = { id: null, model: null, role: 'assistant', content: [], stop_reason: null, stop_details: null, usage: {} };
  const json = [];
  let error = null;
  return {
    event(type, dataText) {
      if (type === 'ping') return;
      let d;
      try { d = JSON.parse(dataText); } catch { throw new RelayError(`Bad JSON in stream event ${type}`); }
      switch (d.type || type) {
        case 'message_start':
          Object.assign(msg, { id: d.message.id, model: d.message.model, usage: { ...(d.message.usage || {}) } });
          break;
        case 'content_block_start':
          msg.content[d.index] = { ...d.content_block };
          if (d.content_block.type === 'tool_use') json[d.index] = '';
          break;
        case 'content_block_delta': {
          const b = msg.content[d.index] || (msg.content[d.index] = { type: 'text', text: '' });
          const dl = d.delta;
          if (dl.type === 'text_delta') { b.text = (b.text || '') + dl.text; onText?.(dl.text); }
          else if (dl.type === 'thinking_delta') b.thinking = (b.thinking || '') + dl.thinking;
          else if (dl.type === 'signature_delta') b.signature = (b.signature || '') + dl.signature;
          else if (dl.type === 'input_json_delta') json[d.index] = (json[d.index] || '') + dl.partial_json;
          break;
        }
        case 'content_block_stop':
          if (json[d.index] !== undefined) { try { msg.content[d.index].input = JSON.parse(json[d.index] || '{}'); } catch { msg.content[d.index].input = null; } }
          break;
        case 'message_delta':
          if (d.delta?.stop_reason !== undefined) msg.stop_reason = d.delta.stop_reason;
          if (d.delta?.stop_details !== undefined) msg.stop_details = d.delta.stop_details;
          if (d.usage) Object.assign(msg.usage, d.usage);
          break;
        case 'message_stop': break;
        case 'error':
          error = new RelayError(d.error?.message || 'stream error', { type: d.error?.type || 'api_error',
            retryable: ['overloaded_error', 'api_error', 'rate_limit_error'].includes(d.error?.type) });
          break;
      }
    },
    finish() { if (error) throw error; return msg; },
  };
}

export const messageText = msg => (msg.content || []).filter(b => b && b.type === 'text').map(b => b.text).join('');

async function readStream(res, onChunk, signal) {
  if (res.body && res.body.getReader) {
    const reader = res.body.getReader();
    const dec = new TextDecoder();
    for (;;) {
      if (signal?.aborted) { try { reader.cancel(); } catch {} throw new DOMException('Aborted', 'AbortError'); }
      const { value, done } = await reader.read();
      if (done) break;
      onChunk(dec.decode(value, { stream: true }));
    }
    onChunk(dec.decode());
  } else onChunk(await res.text());
}

const sleep = (ms, signal) => new Promise((ok, no) => {
  const t = setTimeout(ok, ms);
  signal?.addEventListener?.('abort', () => { clearTimeout(t); no(new DOMException('Aborted', 'AbortError')); }, { once: true });
});

export function createRelay({ base = '/api/v1', accessKey, fetch: fetchImpl = globalThis.fetch?.bind(globalThis), retries = 3, backoffMs = 1000 } = {}) {
  if (!fetchImpl) throw new Error('No fetch available');
  const url = p => base.replace(/\/$/, '') + p;
  const post = (p, body, signal) => fetchImpl(url(p), {
    method: 'POST', headers: { 'content-type': 'application/json' }, body: JSON.stringify(body), signal,
    credentials: 'omit', referrerPolicy: 'no-referrer', cache: 'no-store',
  });

  async function errorFrom(res) {
    let msg = `relay HTTP ${res.status}`, type = 'relay_error';
    try { const j = await res.json(); msg = j.error?.message || j.error || j.message || msg; type = j.error?.type || type; } catch {}
    if (res.status === 401) msg = 'The access key was not accepted.';
    return new RelayError(String(msg), { status: res.status, type, retryable: res.status === 429 || res.status >= 500 });
  }

  return {
    async check({ signal } = {}) {
      const res = await post('/check', { access_key: accessKey }, signal);
      if (!res.ok) throw await errorFrom(res);
      return res.json();
    },

    async messages(request, { onText, signal } = {}) {
      const body = { ...request, model: MODEL, stream: true };
      let attempt = 0;
      for (;;) {
        try {
          const res = await post('/messages', { access_key: accessKey, request: body }, signal);
          if (!res.ok) throw await errorFrom(res);
          const acc = createMessageAccumulator({ onText });
          const sse = createSSEParser((ev, data) => acc.event(ev, data));
          await readStream(res, c => sse.push(c), signal);
          sse.end();
          return acc.finish();
        } catch (e) {
          if (e.name === 'AbortError' || !(e instanceof RelayError) || !e.retryable || attempt >= retries) throw e;
          attempt++;
          await sleep(backoffMs * 2 ** attempt, signal);
        }
      }
    },

    async fetchSource(key, { signal } = {}) { return bytes(await post('/fetch', { access_key: accessKey, source_key: key }, signal)); },
    async fetchMap(mapUrl, { signal } = {}) { return bytes(await post('/fetch-map', { access_key: accessKey, url: mapUrl }, signal)); },
  };
}

async function bytes(res) {
  if (!res.ok) return { ok: false, status: res.status, contentType: null, bytes: null };
  const buf = new Uint8Array(await res.arrayBuffer());
  return { ok: true, status: res.status, contentType: (res.headers.get('content-type') || '').split(';')[0].trim(), bytes: buf };
}

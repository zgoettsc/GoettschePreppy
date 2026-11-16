import test from 'node:test';
import assert from 'node:assert/strict';
import { createSSEParser, createMessageAccumulator, messageText } from '../../app/lib/relay-client.js';
import { createDryRunRelay } from '../../app/lib/relay-dryrun.js';
import { applyFinding, checkAiText, localChecks, ownerTokenRegexes, parseFindings, reviewRequest, FINDINGS_SCHEMA } from '../../app/lib/review.js';
import { htmlToReadable, toBase64 } from '../../app/lib/sources.js';

test('SSE parser survives arbitrary chunk boundaries', () => {
  const text = 'event: a\ndata: {"x":1}\n\n: comment\n\nevent: b\ndata: {"y":\ndata: 2}\n\n';
  for (let cut = 1; cut < text.length; cut++) {
    const got = [];
    const p = createSSEParser((e, d) => got.push([e, d]));
    p.push(text.slice(0, cut)); p.push(text.slice(cut)); p.end();
    assert.deepEqual(got, [['a', '{"x":1}'], ['b', '{"y":\n2}']]);
  }
});

test('message accumulator builds text, thinking, tool input and stop reason', () => {
  const acc = createMessageAccumulator();
  const ev = (t, d) => acc.event(t, JSON.stringify({ type: t, ...d }));
  ev('message_start', { message: { id: 'm', model: 'claude-opus-5-5', usage: { input_tokens: 3 } } });
  ev('content_block_start', { index: 0, content_block: { type: 'thinking', thinking: '' } });
  ev('content_block_delta', { index: 0, delta: { type: 'thinking_delta', thinking: 'hm' } });
  ev('content_block_stop', { index: 0 });
  ev('content_block_start', { index: 1, content_block: { type: 'text', text: '' } });
  ev('content_block_delta', { index: 1, delta: { type: 'text_delta', text: 'Hel' } });
  ev('content_block_delta', { index: 1, delta: { type: 'text_delta', text: 'lo' } });
  ev('content_block_start', { index: 2, content_block: { type: 'tool_use', id: 't', name: 'x', input: {} } });
  ev('content_block_delta', { index: 2, delta: { type: 'input_json_delta', partial_json: '{"a":' } });
  ev('content_block_delta', { index: 2, delta: { type: 'input_json_delta', partial_json: '1}' } });
  ev('content_block_stop', { index: 2 });
  ev('message_delta', { delta: { stop_reason: 'end_turn' }, usage: { output_tokens: 9 } });
  acc.event('ping', '{"type":"ping"}');
  const msg = acc.finish();
  assert.equal(messageText(msg), 'Hello');
  assert.equal(msg.content[0].thinking, 'hm');
  assert.deepEqual(msg.content[2].input, { a: 1 });
  assert.equal(msg.stop_reason, 'end_turn');
  assert.equal(msg.usage.output_tokens, 9);
  const bad = createMessageAccumulator();
  bad.event('error', JSON.stringify({ type: 'error', error: { type: 'overloaded_error', message: 'busy' } }));
  assert.throws(() => bad.finish(), /busy/);
});

test('dry-run relay: check, retry on 529, streamed structured output, fetch', async () => {
  const relay = createDryRunRelay({ flaky: true });
  assert.deepEqual(await relay.check(), { ok: true, label: 'dry-run' });
  const req = reviewRequest([{ id: '03-01-x', layer: 'core', title: 'T', md: 'text DRYRUN-TYPO here' }], { system: 'S', digest: 'D' });
  assert.equal(req.model, 'claude-opus-5-5');
  assert.equal(req.output_config.format.type, 'json_schema');
  assert.equal(req.system[0].cache_control.type, 'ephemeral');
  assert.ok(!('temperature' in req));
  const msg = await relay.messages(req);
  assert.equal(relay.calls.messages, 2, 'one 529 then success');
  const f = parseFindings(msg);
  assert.equal(f.ok, true);
  assert.equal(f.findings[0].find, 'DRYRUN-TYPO');
  assert.equal(relay.calls.requests[1].stream, true);
  const doc = await relay.fetchSource('some-key');
  assert.equal(doc.ok, true);
  assert.equal(doc.contentType, 'text/html');
  assert.equal((await relay.fetchSource('x-blocked')).ok, false);
  const bad = createDryRunRelay({ accessKey: 'bad-key-0000' });
  await assert.rejects(bad.check(), /access key/);
});

test('findings schema is valid for structured outputs (no unsupported keywords)', () => {
  const s = JSON.stringify(FINDINGS_SCHEMA);
  for (const k of ['minLength', 'maxLength', 'minimum', 'maximum', 'pattern']) assert.ok(!s.includes(`"${k}"`), k);
  assert.ok(s.includes('"additionalProperties":false'));
});

test('applyFinding: only exact, unique, number-free replacements', () => {
  const md = 'Store 14 gallons. Teh water. Teh end.';
  assert.equal(applyFinding(md, { fixable: true, find: 'Teh water', replace: 'The water' }).md, 'Store 14 gallons. The water. Teh end.');
  assert.equal(applyFinding(md, { fixable: true, find: 'Teh', replace: 'The' }).applied, false, 'not unique');
  assert.equal(applyFinding(md, { fixable: true, find: 'Store 14 gallons', replace: 'Store 20 gallons' }).applied, false, 'adds a number');
  assert.equal(applyFinding(md, { fixable: true, find: 'Store 14 gallons', replace: 'Keep 14 gallons' }).applied, true, 'keeps a number');
  assert.equal(applyFinding(md, { fixable: false, find: 'Teh water', replace: 'x' }).applied, false);
});

test('ai text checks reject new numbers and addresses', () => {
  assert.deepEqual(checkAiText('Drive the 140 miles to Aunt Rosa.', { miles: 140 }), []);
  assert.equal(checkAiText('Call 555-0199 first.', { miles: 140 }).length, 1);
  assert.equal(checkAiText('See www.example.org.', {}).length, 1);
});

test('local checks: URLs removed, owner tokens unless the household typed them, required blanks', () => {
  const tokenRes = ownerTokenRegexes({ words: ['Lucy', 'Sioux Falls'], patterns: ['\\b605[-. )]\\s?\\d{3}'] });
  const r = localChecks({ id: '00-04-x', md: 'Go to https://example.com now. Lucy and Sioux Falls. Call 605-555-1212.' }, { tokenRes, profileText: '{"label":"Lucy"}', blanks: ['home.county', 'home.town'] });
  assert.ok(!/example\.com/.test(r.md));
  const passes = r.findings.map(f => f.pass + ':' + (f.message.match(/"([^"]+)"/) || [])[1]);
  assert.ok(passes.includes('urls:undefined'));
  assert.ok(passes.includes('personal-tokens:Sioux Falls'));
  assert.ok(!passes.includes('personal-tokens:Lucy'), 'the household typed Lucy itself');
  assert.ok(r.findings.some(f => f.pass === 'slots' && /home\.county/.test(f.message) && !/home\.town/.test(f.message)));
  const s31 = localChecks({ id: '31-01-x', md: 'Lucy' }, { tokenRes });
  assert.equal(s31.findings.length, 0, 'Section 31 is exempt');
});

test('htmlToReadable strips scripts, links, attributes and addresses', () => {
  const out = htmlToReadable('<html><head><script>alert(1)</script><style>p{}</style></head><body><nav>menu</nav><h1 class="x" onclick="y()">Title</h1><p>See <a href="https://x.org/a">this page</a> or www.x.org/b &amp; more.</p><img src="https://x.org/i.png"><table><tr><td>a</td></tr></table></body></html>');
  assert.ok(!/script|alert|menu|href|onclick|https?:|www\./i.test(out), out);
  assert.match(out, /<h1>Title<\/h1>/);
  assert.match(out, /this page/);
  assert.match(out, /&amp; more/);
  assert.match(out, /<td>a<\/td>/);
  assert.equal(toBase64(new Uint8Array([104, 105])), 'aGk=');
});

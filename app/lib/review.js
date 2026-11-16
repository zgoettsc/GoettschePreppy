// review.js — the review passes run on every generated binder (decision G6, docs/01 §3).
//
// Local passes (no model, always run):
//   urls             no URL or web address anywhere (G8); mechanical fix: the address is removed
//   personal-tokens  nothing from the owner household (scripts/owner-tokens.json) unless the
//                    household typed the same word itself (a friend's child may be called Lucy)
//   slots            no blank in a slot the profile requires; template errors; unknown choices
//   ai-blocks        model-written text adds no number, phone, or address that is not in its inputs
//
// Model passes (through the relay, structured outputs, one request per batch of pages):
//   consistency      one rule, one number, one name everywhere; matches the household digest
//                    (decision-card choices, derived numbers) and never states a different rule
//                    from a decision card or a floor
//   source-trace     on critical pages, every number traces to the page text as authored, a
//                    profile value, or a dataset value; flags numbers that do not
//   personal-tokens  names, places or details that look like they belong to another household
//   readability      novice level: undefined jargon, long sentences in emergency steps
// Findings come back as a JSON list. A finding marked fixable with an exact `find` that occurs
// once on the page, and whose `replace` adds no digit or address, is applied; everything else is
// listed on the generated Review notes page.
//
// Which pages go to the model: every page whose text depends on the household (template tags or
// ai blocks), and every household-layer page. Frozen kit text with no slots (most core pages and
// all of Section 31) is identical in every binder and is reviewed when the kit is built, not per
// household; the Review notes page says so.

import { MODEL } from './relay-client.js';

export const URL_RE = /https?:\/\/[^\s"'<>)\]]*|\bwww\.[a-z0-9-]+\.[a-z][^\s"'<>)\]]*/gi;

export const REQUIRED_PATHS = new Set([
  'home.state', 'home.state_name', 'home.county', 'home.setting', 'dwelling.type', 'dwelling.water_supply',
  'dwelling.sewer', 'dwelling.primary_heat', 'household.size', 'household.labels', 'household.adults',
  'derived.water.floor_gal_day', 'derived.water.plan_gal_day', 'derived.water.two_weeks_gal',
]);

export const FLOORS = [
  'Never run a generator, charcoal, or any engine indoors, in a garage, or near an open window.',
  'Never connect a generator to house wiring without a transfer switch, interlock, or a cord-and-plug conversion with the main breaker locked off. Never backfeed through an outlet.',
  'Never loosen a tourniquet once placed; mark the time.',
  'Low-acid foods are pressure-canned to the published time and pressure, or not canned.',
  'No wild plant or mushroom is eaten on a "test"; identification or nothing.',
  'Fuel is never stored or transferred near an open flame or a running appliance.',
  'A frozen-then-thawed insulin vial or pen is discarded.',
  'Bleach or pool shock is never mixed with ammonia, acids or other cleaners.',
  'Children do not have access to firearms, fuel, medications or chlorine products.',
];

// ---- helpers -----------------------------------------------------------------------------------
export const numbersIn = s => (String(s).match(/\d+(?:[.,]\d+)*/g) || []).map(n => n.replace(/,/g, ''));

export function addsNumbers(text, allowedText) {
  const allowed = new Set(numbersIn(allowedText));
  return numbersIn(text).filter(n => !allowed.has(n));
}

const countOf = (hay, needle) => { if (!needle) return 0; let n = 0, i = 0; while ((i = hay.indexOf(needle, i)) >= 0) { n++; i += needle.length; } return n; };

export function ownerTokenRegexes(tokens) {
  if (!tokens) return [];
  const escRe = w => w.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  return [
    ...(tokens.words || []).map(w => ({ token: w, re: new RegExp(`(^|[^A-Za-z0-9])${escRe(w)}([^A-Za-z0-9]|$)`) })),
    ...(tokens.patterns || []).map(p => ({ token: p, re: new RegExp(p) })),
  ];
}

// ---- local checks -------------------------------------------------------------------------------
// page: { id, layer, md }  → { md (possibly fixed), findings: [] }
export function localChecks(page, { tokenRes = [], profileText = '', blanks = [] } = {}) {
  const findings = [];
  let md = page.md;
  const urls = md.match(URL_RE);
  if (urls) {
    md = md.replace(URL_RE, '[address removed]');
    findings.push({ page: page.id, pass: 'urls', severity: 'warning', fixed: true, message: `Removed ${urls.length} web address(es); the binder carries no links.` });
  }
  if (!page.id.startsWith('31-')) {
    const prof = profileText.toLowerCase();
    for (const { token, re } of tokenRes) {
      if (re.test(md) && !prof.includes(token.toLowerCase()))
        findings.push({ page: page.id, pass: 'personal-tokens', severity: 'error', fixed: false, message: `Text that belongs to another household ("${token}") appears on this page. Cross it out.` });
    }
  }
  const req = [...new Set(blanks.filter(b => REQUIRED_PATHS.has(b)))];
  if (req.length) findings.push({ page: page.id, pass: 'slots', severity: 'error', fixed: false, message: `Required answer(s) printed blank: ${req.join(', ')}. Fill them in by hand.` });
  return { md, findings };
}

// ai block text: reject anything that adds a number or an address not present in its inputs.
export function checkAiText(text, inputs) {
  const problems = [];
  const added = addsNumbers(text, JSON.stringify(inputs));
  if (added.length) problems.push(`adds numbers not in its inputs (${added.slice(0, 5).join(', ')})`);
  if (URL_RE.test(text)) problems.push('contains a web address');
  URL_RE.lastIndex = 0;
  if (/\{\{|\}\}/.test(text)) problems.push('contains template syntax');
  return problems;
}

// ---- model review -------------------------------------------------------------------------------
export const PASSES = ['consistency', 'source-trace', 'personal-tokens', 'readability'];

export const FINDINGS_SCHEMA = {
  type: 'object',
  additionalProperties: false,
  required: ['findings'],
  properties: {
    findings: {
      type: 'array',
      items: {
        type: 'object',
        additionalProperties: false,
        required: ['page_id', 'pass', 'severity', 'fixable', 'message', 'find', 'replace'],
        properties: {
          page_id: { type: 'string', description: 'The PAGE id the finding is about.' },
          pass: { type: 'string', enum: PASSES },
          severity: { type: 'string', enum: ['info', 'warning', 'error'] },
          fixable: { type: 'boolean', description: 'True only for a mechanical fix: an exact text replacement that needs no judgement and adds no new fact.' },
          message: { type: 'string', description: 'One or two plain sentences for the household.' },
          find: { type: 'string', description: 'Exact text copied from the page (when fixable), else empty.' },
          replace: { type: 'string', description: 'Replacement text (when fixable), else empty.' },
        },
      },
    },
  },
};

export function reviewSystemPrompt(kit) {
  const cards = (kit.cards || []).map(c => `${c.id}: ${c.title || ''}`).join('\n');
  return `You are the review pass of GoettschePreppy, a kit that generates an offline emergency-preparedness binder for one US household. No human reviews the binder; you are the check. You review pages after they were filled from the household's profile.

Run these passes on every page you are given and report findings:
1. consistency: one rule, one number, one name everywhere. Numbers and choices must match the HOUSEHOLD DIGEST. A page may describe a decision-card trade-off neutrally and point to the card, but must never state a different rule from the household's choice or from a floor, and must never present a risky option as the default.
2. source-trace (pages marked critical): every number must come from the page's own authored text, the household digest, or a named published source cited on the page. Flag any number in model-written text (marked as such) that has no such origin. Never supply a number yourself.
3. personal-tokens: names, places, phone numbers, gear models or rules that look like they belong to a different household than the digest describes.
4. readability: the reader has never prepped. Flag jargon used without explanation, and emergency steps that are too long to follow under stress.

Rules for your findings:
- Report only real problems. An empty list is a good result.
- Blanks printed as "__________ (fill in)" are intentional: the household fills them by hand. Do not report them.
- "fixable" is true only for a mechanical fix: a typo, a doubled word, a wrong household label, a number that contradicts the digest where the digest value is the fix. The "find" text must be copied exactly from the page and be long enough to occur once. The "replace" text must not add any new number, phone number, law, dose or procedure.
- Never propose a medical dose, a ratio, or a schedule. Never relax a floor.
- Write messages in plain words for the household, one or two sentences.

THE FLOORS (rules with no options; a page must never weaken them):
${FLOORS.map(f => '- ' + f).join('\n')}

DECISION CARDS (each household picks an option; pages refer to the card):
${cards || '(card pages not in this kit build yet)'}
`;
}

export function householdDigest(ctx) {
  const d = {
    household: ctx.household, home: ctx.home, dwelling: ctx.dwelling,
    members: ctx.members.map(m => ({ label: m.label, role: m.role, age: m.age_text })),
    derived: { water: ctx.derived.water, calories: ctx.derived.calories, station_fridge_days: ctx.derived.station_fridge_days },
    decision_card_choices: ctx._choices,
    destinations: ctx.destinations.map(x => ({ name: x.name, state: x.state_name, county: x.county, status: x.status_text })),
  };
  return `HOUSEHOLD DIGEST (the facts every page must agree with):\n${JSON.stringify(d, null, 1)}`;
}

export function batchPages(pages, maxChars = 60000) {
  const batches = [];
  let cur = [], n = 0;
  for (const p of pages) {
    const len = p.md.length + 200;
    if (cur.length && n + len > maxChars) { batches.push(cur); cur = []; n = 0; }
    cur.push(p); n += len;
  }
  if (cur.length) batches.push(cur);
  return batches;
}

export function reviewRequest(batch, { system, digest, effort = 'high' }) {
  const text = batch.map(p => `===== PAGE ${p.id} | layer ${p.layer} | ${p.danger_level || 'none'} | ${p.title}\n${p.md}`).join('\n\n');
  return {
    model: MODEL,
    max_tokens: 32000,
    thinking: { type: 'adaptive' },
    output_config: { effort, format: { type: 'json_schema', schema: FINDINGS_SCHEMA } },
    system: [
      { type: 'text', text: system, cache_control: { type: 'ephemeral' } },
      { type: 'text', text: digest, cache_control: { type: 'ephemeral' } },
    ],
    messages: [{ role: 'user', content: `Review these ${batch.length} page(s). Model-written paragraphs are inside <div class="aiblock">. Return the findings JSON.\n\n${text}` }],
  };
}

// Apply a model finding if it is mechanical and safe. Returns { md, applied }.
export function applyFinding(md, f) {
  if (!f.fixable || !f.find) return { md, applied: false };
  if (countOf(md, f.find) !== 1) return { md, applied: false };
  if (addsNumbers(f.replace, f.find).length) return { md, applied: false };
  URL_RE.lastIndex = 0;
  if (URL_RE.test(f.replace)) { URL_RE.lastIndex = 0; return { md, applied: false }; }
  return { md: md.replace(f.find, () => f.replace), applied: true };
}

export function parseFindings(msg) {
  if (msg.stop_reason === 'refusal') return { ok: false, reason: 'the model declined to review this batch' };
  if (msg.stop_reason === 'max_tokens') return { ok: false, reason: 'the review answer was cut off' };
  const text = (msg.content || []).filter(b => b.type === 'text').map(b => b.text).join('');
  try {
    const j = JSON.parse(text);
    if (!Array.isArray(j.findings)) throw new Error('no findings array');
    return { ok: true, findings: j.findings };
  } catch (e) { return { ok: false, reason: 'the review answer was not valid JSON' }; }
}

// Run the model passes over pages [{id, layer, danger_level, title, md}].
// Returns { pages: Map id→md, findings: [], fixes: [] }.
export async function modelReview(pages, { relay, kit, ctx, signal, onProgress, concurrency = 2, fallback }) {
  const system = reviewSystemPrompt(kit);
  const digest = householdDigest(ctx);
  const byId = new Map(pages.map(p => [p.id, p]));
  const batches = batchPages(pages);
  const findings = [], fixes = [];
  let done = 0;
  const runOne = async batch => {
    signal?.throwIfAborted?.();
    let res;
    try {
      const msg = await relay.messages(reviewRequest(batch, { system, digest }), { signal, fallback });
      res = parseFindings(msg);
    } catch (e) {
      if (e.name === 'AbortError') throw e;
      res = { ok: false, reason: `the review request failed (${e.message})` };
    }
    if (!res.ok) {
      for (const p of batch) findings.push({ page: p.id, pass: 'review', severity: 'warning', fixed: false, message: `Not reviewed by the model: ${res.reason}. Read this page with extra care.` });
    } else {
      for (const f of res.findings) {
        const p = byId.get(f.page_id) || batch.find(b => b.md.includes(f.find || '\u0000')) || null;
        if (p) {
          const { md, applied } = applyFinding(p.md, f);
          if (applied) { p.md = md; fixes.push({ page: p.id, find: f.find, replace: f.replace }); }
          findings.push({ page: p.id, pass: f.pass, severity: f.severity, fixed: applied, message: f.message });
        } else findings.push({ page: f.page_id || '', pass: f.pass, severity: f.severity, fixed: false, message: f.message });
      }
    }
    done++;
    onProgress?.({ phase: 'review', done, total: batches.length, message: `Reviewed batch ${done} of ${batches.length}` });
  };
  const queue = batches.slice();
  await Promise.all(Array.from({ length: Math.min(concurrency, queue.length) }, async () => { while (queue.length) await runOne(queue.shift()); }));
  return { findings, fixes };
}

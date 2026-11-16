// generate.js — profile + kit → one offline binder file.
//
//   const blob = await generateBinder(profile, kit, { relay, size, onProgress, signal, loadAsset })
//   blob.report → { pages, aiBlocks, findings, fixes, sources, bytes, modelCalls }
//
// Steps (docs/01-architecture.md §3, notes/APP-BRIEF.md):
//   1. context (context.js)                          5. local checks + model review (review.js)
//   2. page set, order, promotion                    6. Large: bind sources (kit assets or relay)
//   3. render every page's template (render.js)      7. Review notes + Sources not captured pages
//   4. {{ai}} blocks through the relay               8. assemble the HTML (app/binder/shell.js)
//
// opts:
//   relay        createRelay() or createDryRunRelay() (relay-client.js, relay-dryrun.js)
//   size         'small' | 'large' | 'everything' (decision G25; sources.js SIZES): Large binds the
//                documents cited by the life-safety sections (LIFE_SAFETY_SECTIONS) and lists the
//                rest as "in the Everything download"; Everything binds every cited document.
//                Large and Everything both carry topo maps (G16).
//   onProgress   ({ phase, done, total, message }) => void
//   signal       AbortSignal (cancel)
//   loadAsset    async (path relative to app/build/) → Uint8Array | null. Default: fetch() relative
//                to opts.assetBase (default './build/' from the settings page).
//   previous     an earlier binder file from the same profile (text, or a Blob/File): its ai blocks
//                and review results are reused when unchanged, and the source documents it already
//                binds are reused without fetching or rendering them again. Small → Large →
//                Everything upgrades make no model calls.
//   pdfRender    async (Uint8Array, {signal}) → {pages, total, truncated}; default: vendored pdf.js
//                in the browser (pdf-render.js); false = keep PDFs as files with an open button
//   pdfToText    optional async (Uint8Array) → string, used only when rendering is unavailable
//   routeMaps    true = also topo maps for the counties between home and destinations (opt-in)
//   now          Date for the build stamp (tests)
//   modelReview  false to skip the model passes (local passes always run)

import { buildContext, STATE_NAMES } from './context.js';
import { renderPageMarkdown, markdownToHtml, articleHtml, buildLabels, esc } from './render.js';
import { localChecks, checkAiText, modelReview, ownerTokenRegexes, URL_RE } from './review.js';
import { MODEL, messageText, createRelay } from './relay-client.js';
import { sourceBlock, toBase64, normalizeSize, bindsSources, sourcesForSize, extractBoundSources, reusedSourceBlock, SIZE_LABEL } from './sources.js';
import { mapTargets, fetchTopoMaps, mapPlan as mapPlanFor } from './maps.js';
import { renderPdfPages, canRenderPdf } from './pdf-render.js';
import { shellParts, jsonEmbed } from '../binder/shell.js';

export const REVIEW_NOTES_ID = '25-11-review-notes';
export const NOT_CAPTURED_ID = '25-12-sources-not-captured';
const FRONT = ['00-05', '00-09', '00-10'];

const tick = () => new Promise(r => setTimeout(r, 0));
const hash = s => { let h = 2166136261; for (let i = 0; i < s.length; i++) { h ^= s.charCodeAt(i); h = Math.imul(h, 16777619); } return (h >>> 0).toString(36); };
const stable = v => JSON.stringify(v, (k, x) => (x && typeof x === 'object' && !Array.isArray(x) ? Object.fromEntries(Object.keys(x).sort().map(key => [key, x[key]])) : x));

async function pool(items, n, fn) {
  const q = items.map((x, i) => [x, i]);
  await Promise.all(Array.from({ length: Math.max(1, Math.min(n, q.length)) }, async () => { while (q.length) { const [x, i] = q.shift(); await fn(x, i); } }));
}

function mimeOf(path) {
  const ext = path.split('.').pop().toLowerCase();
  return { jpg: 'image/jpeg', jpeg: 'image/jpeg', png: 'image/png', webp: 'image/webp', gif: 'image/gif', svg: 'image/svg+xml',
    pdf: 'application/pdf', html: 'text/html', htm: 'text/html', txt: 'text/plain', md: 'text/plain' }[ext] || 'application/octet-stream';
}

// Default: app/build/ next to app/lib/ (the settings page is served from the same site).
export function defaultLoadAsset(assetBase) {
  const base = assetBase ? new URL(assetBase, globalThis.location?.href) : new URL('../build/', import.meta.url);
  return async p => {
    const res = await fetch(new URL(p, base), { credentials: 'omit' });
    return res.ok ? new Uint8Array(await res.arrayBuffer()) : null;
  };
}

// ---- sizes (shown on the download screen before anything is fetched) --------------------------
// Bytes before maps (scripts/build-kit.mjs measures them); kit.sizes.<size> carries MB ranges with
// the usual two maps included, and mapPlan() gives this household's own map count.
export function estimateSizes(kit) {
  const s = kit.sizes || {};
  return { small: s.small_bytes || 0, large: s.large_bytes || 0, everything: s.everything_bytes || 0, note: s.note || '' };
}

// Topo maps before generating (Large): counts and MB for home + destinations, and for the
// optional route counties ({ routeMaps: true }), so the download screen can show the size.
export function mapPlan(profile, kit, { maxMaps = 12 } = {}) { return mapPlanFor(kit, buildContext(profile, kit, { size: 'large' }), { maxMaps }); }

// ---- page set ----------------------------------------------------------------------------------
function promotedFor(page, ctx) {
  const st = page._state;
  if (st && (st === ctx.home.state || ctx.destinations.some(d => d.region?.state === st))) return true;
  if (page.condition && ctx.has.condition[page.condition]) return true;
  return (page.promote_when || []).some(f => {
    const neg = f.startsWith('!'); const v = f.replace(/^!/, '').split('.').reduce((o, k) => o?.[k], ctx);
    return neg ? !v : !!(Array.isArray(v) ? v.length : v);
  });
}

function fallbackPage(id, title, body, extra = {}) {
  return { id, section: '', title, version: 1, revised: '', layer: 'generated', danger_level: 'none', sources: [], body, ...extra };
}

export function selectPages(kit, ctx, size) {
  const pages = (kit.pages || []).map(p => ({ ...p }));
  const have = new Set(pages.map(p => p.id.slice(0, 5)));
  const notice = kit.notice_md || '';
  if (!have.has('00-05')) {
    const part = /## What this binder is, and is not[\s\S]*/.exec(notice);
    pages.push(fallbackPage('00-05-safety-disclaimer', 'Safety disclaimer: read this first',
      `# Safety disclaimer\n\n${part ? part[0] : 'This binder was assembled and checked by an AI. No professional has reviewed your copy.'}\n`, { danger_level: 'critical' }));
  }
  if (!have.has('00-09')) {
    const body = notice.replace(/^[\s\S]*?\n---\n/, '');
    pages.push(fallbackPage('00-09-private-copy-notice', 'Your private copy: what this file is and why it is not for sharing',
      `# Private copy notice\n\n{{#if size.large}}{{else}}> **This is the Small binder.** It holds only GoettschePreppy's own text and public-domain material; no publisher's document is inside it. The copyright part of the notice below applies in full to the Large download.\n\n{{/if}}${body}\n`));
  }
  for (const p of pages) {
    p._state = (p.tags || []).map(t => /^state-([a-z]{2})$/.exec(t)).filter(Boolean).map(m => m[1].toUpperCase())[0] || null;
    if (!p._state && p.id.startsWith('32-')) {
      const slug = p.id.slice(6);
      const hit = Object.entries(STATE_NAMES).find(([, n]) => n.toLowerCase().replace(/[^a-z]+/g, '-') === slug);
      if (hit) p._state = hit[0];
    }
    p._promoted = promotedFor(p, ctx);
  }
  const rank = p => {
    const pre = p.id.slice(0, 5), sec = p.id.slice(0, 2);
    if (sec === '00') { const f = FRONT.indexOf(pre); return f >= 0 ? f : (pre === '00-00' ? 3 : 4); }
    if (p.id.slice(3, 5) === '00') return 0;
    return p._promoted ? 1 : 2;
  };
  pages.sort((a, b) => a.id.slice(0, 2).localeCompare(b.id.slice(0, 2)) || rank(a) - rank(b) || a.id.localeCompare(b.id));
  return pages;
}

function sectionTitle(kit, n, pages) {
  const s = kit.sections?.[n];
  if (s?.title) return s.title;
  const intro = pages.find(p => p.id.startsWith(`${n}-00`));
  return intro ? intro.title.replace(/\s*[—:-]\s*section overview$/i, '') : (s?.folder || n).replace(/^\d\d-/, '').replace(/-/g, ' ');
}

function emergencyRow(pages, ctx) {
  const by = new Map(pages.map(p => [p.id.slice(0, 5), p.id]));
  const want = ['00-02', '12-02', '08-02'];
  if (ctx.has.anaphylaxis) want.push('02-03');
  for (const [id, on] of Object.entries(ctx.has.condition)) if (on) want.push(`02-${id.slice(3)}`);
  want.push('27-04', '00-04');
  if (ctx.is.tornado_region) want.push('17-06');
  return [...new Set(want)].map(x => by.get(x)).filter(Boolean).slice(0, 8);
}

// ---- assets ------------------------------------------------------------------------------------
function createAssets(kit, loadAsset, notes) {
  const plateCss = new Map(); // src → { cls, rule }
  const figureCache = new Map();
  return {
    async preloadPlates(keys) {
      const srcs = new Set();
      for (const k of keys) for (const pl of kit.plates?.[k]?.plates || []) if (pl.src) srcs.add(pl.src);
      await pool([...srcs], 6, async src => {
        let bytes = null;
        try { bytes = await loadAsset(src); } catch {}
        if (!bytes) { notes.push({ page: '', pass: 'plates', severity: 'info', fixed: false, message: `Plate image ${src} could not be loaded.` }); return; }
        const cls = 'pl' + hash(src);
        plateCss.set(src, { cls, rule: `.${cls}{background-image:url(data:${mimeOf(src)};base64,${toBase64(bytes)})}` });
      });
    },
    async preloadFigures(ids) {
      await pool([...ids], 6, async id => {
        const f = kit.figures?.[id];
        if (!f) return;
        if (f.svg) { figureCache.set(id, { ...f }); return; }
        if (!f.src) return;
        let bytes = null;
        try { bytes = await loadAsset(f.src); } catch {}
        if (!bytes) return;
        const cls = 'fg' + hash(f.src);
        plateCss.set(f.src, { cls, rule: `.${cls}{background-image:url(data:${mimeOf(f.src)};base64,${toBase64(bytes)});background-size:contain;background-repeat:no-repeat}` });
        figureCache.set(id, { ...f, cls });
      });
    },
    plateClass: src => plateCss.get(src)?.cls || null,
    figure: id => figureCache.get(id) || null,
    css: () => [...plateCss.values()].map(x => x.rule).join('\n'),
  };
}

// ---- ai blocks ---------------------------------------------------------------------------------
export function aiSystemPrompt(kit) {
  const specs = Object.entries(kit.ai_blocks || {}).sort(([a], [b]) => a.localeCompare(b))
    .map(([id, s]) => `### BLOCK SPEC ${id}\n${s.text}`).join('\n\n');
  return `You write short passages for GoettschePreppy, an offline emergency binder for one US household. The household has no internet when it reads this. Each request names one block, gives its spec, and gives the INPUTS: the only facts you may use.

Hard rules (the binder is checked against them and a block that breaks one is thrown away):
- Use only facts present in the INPUTS. Do not add any number, quantity, distance, time, phone number, address, name, law, regulation, medical dose or safety procedure that is not in the INPUTS. If something the spec asks for is missing from the INPUTS, say plainly that the household should fill it in by hand.
- Never write a web address or tell the reader to look something up online.
- Plain words for someone who has never prepared for an emergency. Short sentences. Calm, direct, not alarmist, not cute.
- Output Markdown body text only: no title, no front matter, no template braces, no preamble or sign-off.
- Stay within the spec's length.

${specs || '(No block specs in this kit build.)'}`;
}

function aiRequest(job, system, pageTitle) {
  return {
    model: MODEL,
    max_tokens: 16000,
    thinking: { type: 'adaptive' },
    output_config: { effort: 'medium' },
    system: [{ type: 'text', text: system, cache_control: { type: 'ephemeral' } }],
    messages: [{ role: 'user', content: `Write the block "${job.id}" for the page "${pageTitle}" (${job.page}).\n\nINPUTS (JSON):\n${JSON.stringify(job.inputs, null, 1)}` }],
  };
}

// ---- previous binder (reuse) -------------------------------------------------------------------
export function extractGenerated(html) {
  const m = /<script type="application\/json" id="gp-generated">([\s\S]*?)<\/script>/.exec(String(html || ''));
  if (!m) return null;
  try { return JSON.parse(m[1]); } catch { return null; }
}

// For the Generate screen, before an upgrade: what an earlier binder file is. `html` may be the
// whole file or only its end (the record sits near the end of the file).
// → null (not a GoettschePreppy binder) | { size, built, sameAnswers, documents }
export function describePrevious(html, profile) {
  const g = extractGenerated(html);
  if (!g) return null;
  return { size: normalizeSize(g.size), built: g.built || '', sameAnswers: !!profile && g.profile_hash === hash(stable({ ...profile, access: undefined })),
    documents: (String(html).match(/<section class="srcdoc" id="src-(?!map-)/g) || []).length };
}

// ---- notes pages -------------------------------------------------------------------------------
function reviewNotesMarkdown(findings, fixes, stats) {
  const sev = { error: 0, warning: 1, info: 2 };
  const open = findings.filter(f => !f.fixed).sort((a, b) => sev[a.severity] - sev[b.severity] || a.page.localeCompare(b.page));
  const fixed = findings.filter(f => f.fixed);
  const line = f => `- **${f.severity.toUpperCase()}**${f.page ? ` → ${f.page.slice(0, 5)}` : ''} (${f.pass}): ${f.message.replace(URL_RE, '')}`;
  return `# Review notes

**What this page is for.** No person checked this binder. An AI did, page by page, after it was filled in from your answers (→ 29-15). This page lists what the checks found that you should look at yourself, worst first, and what they corrected automatically.

> **SAFETY.** The checks catch most slips, not all. They cannot catch a mistake that every public source makes the same way. Where a page and a professional disagree, the professional is right.

## Summary

- Pages in this binder: ${stats.pages}. Pages checked by the model: ${stats.modelPages}${stats.modelSkipped ? ` (${stats.modelSkipped})` : ''}. Every page had the local checks (no web addresses, nothing from another household, required answers present).
- Pages with frozen kit text and no household slots are the same in every binder; they were reviewed when the kit was built.
- Findings to look at: ${open.length}. Corrected automatically: ${fixed.length}.
- Cross-references to pages not in this build yet: ${stats.missingRefs}.

## Look at these

${open.length ? open.map(line).join('\n') : 'Nothing. The checks found no problem that needs you.'}

## Corrected automatically

${fixed.length ? fixed.map(line).join('\n') : 'Nothing needed correcting.'}
`;
}

function notCapturedMarkdown(rows, size, elsewhere = []) {
  const cell = s => String(s || '').replace(/\|/g, '/');
  const cites = r => r.citedBy.map(id => '→ ' + id.slice(0, 5)).join(' ');
  const intro = {
    small: 'This is the Small binder: it carries citations only (title, publisher, date) and binds no documents. The Large download binds the documents cited by the life-safety sections (medical, water, food storage and canning, fire and fuel, heating, power, hazards, kids, CBRN, decisions and floors), and the Everything download binds every cited document. You can upgrade from your saved answers file and this binder file without paying for the writing again.',
    large: 'This is the Large binder: it binds the documents cited by the life-safety sections (medical conditions, water, food storage and canning, fire and fuel, heating, power, first aid, hazards, kids, CBRN, decisions and floors). Documents cited only by other sections are listed further down as "in the Everything download".',
    everything: 'This is the Everything binder: every document the binder cites should be bound inside it, behind the page that cites it.',
  }[size];
  const missing = size === 'small' ? 'Nothing to list in the Small binder.'
    : rows.length ? `The documents below could not be fetched when this file was made (the publisher refused automated download, or the request failed). The pages that cite them still stand on their own text. While the internet works, download these yourself by title and keep them with this file.\n\n| Document | Publisher | Why it is missing | Cited by |\n|---|---|---|---|\n${rows.map(r => `| ${cell(r.title)} | ${cell(r.org)} | ${r.reason} | ${cites(r)} |`).join('\n')}`
    : 'Every document this download binds was captured.';
  const other = size === 'large' ? `\n\n## In the Everything download\n\nNot in this download: these ${elsewhere.length} documents are cited only outside the life-safety sections. The Everything download (the largest file, meant for a laptop) binds them; the pages that cite them stand on their own text.\n\n${elsewhere.length
    ? `| Document | Publisher | Date | Cited by |\n|---|---|---|---|\n${elsewhere.map(r => `| ${cell(r.title)} | ${cell(r.org)} | ${cell(r.date)} | ${cites(r)} |`).join('\n')}` : 'None: every cited document is in this download.'}` : '';
  return `# Sources not captured

**What this page is for.** ${intro}

## Not captured

${missing}${other}
`;
}

// ---- main --------------------------------------------------------------------------------------
export async function generateBinder(profile, kit, opts = {}) {
  const size = normalizeSize(opts.size);
  const { signal } = opts;
  // relay: a relay object, or the relay's base address as a string ('' = same origin), as the
  // settings page passes it (app/settings/config.js relayBase)
  const relay = typeof opts.relay === 'string'
    ? createRelay({ base: opts.relay.replace(/\/$/, '') + '/api/v1', accessKey: profile?.access?.access_key })
    : opts.relay;
  const loadAsset = opts.loadAsset || defaultLoadAsset(opts.assetBase);
  // phases and their share of the progress bar
  const SPAN = { context: [0, 0.01], assets: [0.01, 0.05], render: [0.05, 0.15], ai: [0.15, 0.35], review: [0.35, 0.7], sources: [0.7, 0.95], assemble: [0.95, 0.99], done: [1, 1] };
  const progress = (phase, done, total, message) => {
    const [a, b] = SPAN[phase] || [0, 1];
    opts.onProgress?.({ phase, stage: message, done, total, message, fraction: a + (b - a) * (total ? done / total : 1) });
  };
  const now = opts.now || new Date();
  const built = now.toISOString().slice(0, 10);
  const abort = () => signal?.throwIfAborted?.();
  const report = { size, pages: 0, aiBlocks: 0, findings: [], fixes: [], sources: { bound: 0, missing: 0, reused: 0, elsewhere: 0 }, modelCalls: 0, bytes: 0 };
  const prevText = typeof opts.previous === 'string' ? opts.previous
    : opts.previous && typeof opts.previous.text === 'function' ? await opts.previous.text() : null;
  const prev = prevText ? extractGenerated(prevText) : null;
  const countCalls = relay ? { ...relay, messages: (...a) => { report.modelCalls++; return relay.messages(...a); } } : null;

  // 1. context
  progress('context', 0, 1, 'Reading your answers');
  const ctx = buildContext(profile, kit, { size });
  abort();

  // 2. page set
  const pages = selectPages(kit, ctx, size);
  const notes = [];
  const missingRefs = new Set();
  const reviewNotesPage = fallbackPage(REVIEW_NOTES_ID, 'Review notes: what the AI checks found', '', { danger_level: 'caution' });
  const notCapturedPage = fallbackPage(NOT_CAPTURED_ID, 'Sources not captured', '');
  for (const p of [reviewNotesPage, notCapturedPage, ...pages]) if (p.layer === 'generated' && !p.revised) p.revised = built;
  const all = pages.filter(p => p.id !== REVIEW_NOTES_ID && p.id !== NOT_CAPTURED_ID);
  // the two notes pages go at the end of section 25 (or the end of the binder)
  const at = (() => { let i = -1; all.forEach((p, k) => { if (p.id.slice(0, 2) <= '25') i = k; }); return i + 1; })();
  all.splice(at, 0, reviewNotesPage, notCapturedPage);
  const labels = buildLabels(all);
  const sections = [...new Set(all.map(p => p.id.slice(0, 2)))].map(n => ({ n, t: sectionTitle(kit, n, all) }));

  // assets
  const assets = createAssets(kit, loadAsset, notes);
  progress('assets', 0, 1, 'Loading plates and figures');
  // every binder carries every plate (G21); each image is stored once as a CSS class
  await assets.preloadPlates(new Set([...Object.keys(kit.plates || {}), ...all.flatMap(p => p.plates || [])]));
  await assets.preloadFigures(new Set(all.flatMap(p => p.figures || [])));
  abort();

  // 3. render templates
  const env = { kit, ctx, profile, labels, assets, notes, aiJobs: [], size, missingRefs, meta: {}, reviewDate: built, boundSources: new Map(), sourceTier: new Map() };
  const rendered = new Map(); // id → { page, md, blanks }
  let i = 0;
  for (const page of all) {
    if (page === reviewNotesPage || page === notCapturedPage) continue;
    let md, blanks = [];
    try { ({ md, blanks } = renderPageMarkdown(page, env)); }
    catch (e) {
      notes.push({ page: page.id, pass: 'slots', severity: 'error', fixed: false, message: `This page's template could not be filled (${e.message}); it is shown as written.` });
      md = String(page.body || '').replace(/\{\{[\s\S]*?\}\}/g, '__________');
    }
    // section intros: add the household's promoted pages
    if (/^\d\d-00-/.test(page.id)) {
      const promo = all.filter(p => p._promoted && p.id.slice(0, 2) === page.id.slice(0, 2) && p.id !== page.id);
      if (promo.length) md += `\n\n## For your household, start with\n\n${promo.map(p => `- → ${p.id.slice(0, 5)} ${esc(p.title)}`).join('\n')}\n`;
    }
    rendered.set(page.id, { page, md, blanks });
    if (++i % 25 === 0) { progress('render', i, all.length, 'Filling in pages'); await tick(); abort(); }
  }
  progress('render', all.length, all.length, 'Pages filled in');

  // 4. ai blocks
  const aiText = {};
  const jobs = env.aiJobs;
  report.aiBlocks = jobs.length;
  if (jobs.length) {
    const system = aiSystemPrompt(kit);
    let done = 0;
    await pool(jobs, 3, async job => {
      abort();
      const key = `${job.id}|${job.page}|${hash(stable(job.inputs))}`;
      job.key = key;
      let text = prev?.ai?.[key] ?? null;
      if (text === null && job.spec && countCalls) {
        try {
          const msg = await countCalls.messages(aiRequest(job, system, rendered.get(job.page)?.page.title || job.page), { signal, fallback: opts.refusalFallback });
          if (msg.stop_reason === 'refusal') notes.push({ page: job.page, pass: 'ai-blocks', severity: 'warning', fixed: false, message: `The model declined to write the "${job.id}" passage; fill it in by hand.` });
          else if (msg.stop_reason === 'max_tokens') notes.push({ page: job.page, pass: 'ai-blocks', severity: 'warning', fixed: false, message: `The "${job.id}" passage was cut off and left out; fill it in by hand.` });
          else text = messageText(msg).trim();
        } catch (e) {
          if (e.name === 'AbortError') throw e;
          notes.push({ page: job.page, pass: 'ai-blocks', severity: 'warning', fixed: false, message: `The "${job.id}" passage could not be written (${e.message}); fill it in by hand.` });
        }
      } else if (!job.spec) notes.push({ page: job.page, pass: 'ai-blocks', severity: 'info', fixed: false, message: `No spec for the "${job.id}" passage in this kit build; left blank.` });
      if (text) {
        const problems = checkAiText(text, job.inputs);
        if (problems.length) { notes.push({ page: job.page, pass: 'ai-blocks', severity: 'warning', fixed: true, message: `A model-written passage ("${job.id}") was thrown away because it ${problems.join(' and ')}. Fill it in by hand.` }); text = null; }
      }
      aiText[key] = text;
      progress('ai', ++done, jobs.length, 'Writing your household pages');
    });
    for (const r of rendered.values()) {
      if (!r.md.includes('GPAIBLOCK')) continue;
      r.md = r.md.replace(/GPAIBLOCK(\d+)X/g, (m, n) => {
        const job = jobs[+n]; const t = aiText[job.key];
        return t ? `\n\n<div class="aiblock"><span class="ailabel">Written by the AI from your answers</span>\n\n${t}\n\n</div>\n\n` : '<span class="blank">__________<small> (fill in)</small></span>';
      });
    }
  }
  abort();

  // 5. review: local checks on every page, model passes on household-dependent pages
  const tokenRes = ownerTokenRegexes(kit.owner_tokens);
  // The household's own answers and its own region values (home and destinations, public data
  // such as an NWS office "Sioux Falls, SD") are not another household's details.
  const profileText = JSON.stringify({ ...profile, access: undefined }) + JSON.stringify([ctx.region.home, ...ctx.destinations.map(d => d.region)]);
  for (const r of rendered.values()) {
    const { md, findings } = localChecks({ id: r.page.id, layer: r.page.layer, md: r.md }, { tokenRes, profileText, blanks: r.blanks });
    r.md = md; notes.push(...findings);
  }
  const toModel = [...rendered.values()].filter(r => !r.page.id.startsWith('31-') && r.page.layer !== 'generated' &&
    (r.page.layer === 'household' || /\{\{/.test(r.page.body || '')));
  let modelSkipped = '';
  if (prev && prev.profile_hash === hash(stable({ ...profile, access: undefined }))) {
    for (const f of prev.fixes || []) { const r = rendered.get(f.page); if (r && r.md.split(f.find).length === 2) { r.md = r.md.replace(f.find, () => f.replace); report.fixes.push(f); } }
    notes.push(...(prev.findings || []).filter(f => f.pass !== 'urls' && f.pass !== 'slots' && f.pass !== 'personal-tokens'));
    modelSkipped = 'results reused from the earlier build of the same answers';
  } else if (opts.modelReview !== false && countCalls && toModel.length) {
    const reviewPages = toModel.map(r => ({ id: r.page.id, layer: r.page.layer, danger_level: r.page.danger_level, title: r.page.title, md: r.md }));
    const res = await modelReview(reviewPages, { relay: countCalls, kit, ctx, signal, onProgress: e => progress('review', e.done, e.total, e.message), fallback: opts.refusalFallback });
    for (const p of reviewPages) rendered.get(p.id).md = p.md;
    notes.push(...res.findings); report.fixes.push(...res.fixes);
  } else modelSkipped = countCalls ? 'model review switched off for this build' : 'no relay: model review not run';
  abort();

  // 6. sources
  const cited = new Map(); // key → [page ids] in binder order
  for (const p of all) for (const k of p.sources || []) { if (!cited.has(k)) cited.set(k, []); cited.get(k).push(p.id); }
  const notCaptured = [];
  const srcParts = new Map(); // section → [parts]
  // the smallest download that carries each cited document (for the citation lines)
  const inLarge = sourcesForSize(cited, 'large').bind;
  for (const key of cited.keys()) env.sourceTier.set(key, inLarge.has(key) ? 'large' : 'everything');
  const elsewhereRows = [];
  if (bindsSources(size)) {
    const { bind, elsewhere } = sourcesForSize(cited, size);
    for (const [key, citedBy] of elsewhere) { const s = kit.sources?.[key] || {}; elsewhereRows.push({ key, title: s.title || key, org: s.org || '', date: s.date || '', citedBy }); }
    report.sources.elsewhere = elsewhere.size;
    const reuse = prevText ? extractBoundSources(prevText) : new Map();
    const keys = [...bind.keys()];
    let done = 0;
    await pool(keys, 3, async key => {
      abort();
      const src = kit.sources?.[key];
      const { citedBy, section: sec } = bind.get(key);
      if (src && reuse.has(key)) {
        // already bound in the earlier file: no fetch, no rendering
        if (!srcParts.has(sec)) srcParts.set(sec, []);
        srcParts.get(sec).push({ key, parts: reusedSourceBlock(key, src, reuse.get(key), { citedBy, sectionNo: sec }) });
        env.boundSources.set(key, true);
        report.sources.bound++; report.sources.reused++;
        progress('sources', ++done, keys.length, 'Binding source documents');
        return;
      }
      let doc = null, reason = '';
      try {
        if (!src) reason = 'not in the source index';
        else if (src.shipped) {
          const bytes = await loadAsset(src.shipped);
          if (bytes) doc = { key, src, bytes, contentType: mimeOf(src.shipped) };
          else reason = 'the kit copy could not be loaded';
        }
        if (!doc && src && relay) {
          const r = await relay.fetchSource(key, { signal });
          if (r.ok) doc = { key, src, bytes: r.bytes, contentType: r.contentType };
          else reason = r.status === 403 ? 'the publisher refused automated download' : `download failed (HTTP ${r.status})`;
        } else if (!doc && !reason) reason = 'no relay';
      } catch (e) { if (e.name === 'AbortError') throw e; reason = `download failed (${e.message})`; }
      if (doc && doc.contentType === 'application/pdf') {
        // render pages to images (vendored pdf.js, browser); on failure keep the PDF and a button
        const renderer = opts.pdfRender === false ? null : (opts.pdfRender || (canRenderPdf() ? renderPdfPages : null));
        if (renderer) {
          try { doc.rendered = await renderer(doc.bytes, { signal }); }
          catch (e) {
            if (e.name === 'AbortError') throw e;
            notes.push({ page: citedBy[0], pass: 'sources', severity: 'info', fixed: false, message: `"${src?.title || key}" is bound as a PDF file (open it from its page); it could not be turned into pictures (${e.message}).` });
          }
        }
        if (!doc.rendered && opts.pdfToText) { try { doc.text = await opts.pdfToText(doc.bytes); } catch {} }
        if (doc.rendered) report.sources.rendered = (report.sources.rendered || 0) + 1;
      }
      if (doc) {
        if (!srcParts.has(sec)) srcParts.set(sec, []);
        srcParts.get(sec).push({ key, parts: sourceBlock(doc, { citedBy, sectionNo: sec }) });
        env.boundSources.set(key, true);
        report.sources.bound++;
      } else {
        notCaptured.push({ key, title: src?.title || key, org: src?.org || '', reason, citedBy });
        report.sources.missing++;
      }
      progress('sources', ++done, keys.length, 'Binding source documents');
    });
    // maps (G16): home county, destinations and the counties on the straight line between
    const maps = await fetchTopoMaps(relay, mapTargets(kit, ctx, { route: !!opts.routeMaps }), { maxMaps: opts.maxMaps ?? 12, signal });
    maps.forEach((m, n) => {
      if (m.ok) {
        if (!srcParts.has('25')) srcParts.set('25', []);
        srcParts.get('25').push({ key: `map-${String(n).padStart(2, '0')}`, parts: sourceBlock({ key: `map-${String(n).padStart(2, '0')}`, src: { title: m.title, org: 'U.S. Geological Survey', date: m.date || '', licence_note: `Public domain. ${m.why}.` }, bytes: m.bytes, contentType: m.contentType }, { citedBy: [], sectionNo: '25' }) });
        report.maps = (report.maps || 0) + 1;
      } else notCaptured.push({ key: `map-${n}`, title: m.title, org: 'U.S. Geological Survey', reason: `${m.reason} (${m.why})`, citedBy: [] });
    });
  } else {
    for (const [key, citedBy] of cited) { const s = kit.sources?.[key]; if (!s) notes.push({ page: citedBy[0], pass: 'sources', severity: 'info', fixed: false, message: `Cited source "${key}" is not in the source index.` }); }
  }
  for (const v of srcParts.values()) v.sort((a, b) => a.key.localeCompare(b.key));
  abort();

  // 7. the two notes pages
  report.findings = notes;
  const stats = { pages: all.length, modelPages: toModel.length, modelSkipped, missingRefs: 0 };
  elsewhereRows.sort((a, b) => a.title.localeCompare(b.title));
  rendered.set(NOT_CAPTURED_ID, { page: notCapturedPage, md: notCapturedMarkdown(notCaptured.sort((a, b) => a.title.localeCompare(b.title)), size, elsewhereRows), blanks: [] });
  rendered.set(REVIEW_NOTES_ID, { page: reviewNotesPage, md: '', blanks: [] });

  // 8. assemble
  progress('assemble', 0, 1, 'Putting the file together');
  for (const p of all) env.meta[p.id] = { st: p._state, pr: p._promoted };
  const htmlById = new Map();
  for (const p of all) {
    if (p.id === REVIEW_NOTES_ID) continue;
    htmlById.set(p.id, markdownToHtml(rendered.get(p.id).md, env));
  }
  stats.missingRefs = missingRefs.size;
  htmlById.set(REVIEW_NOTES_ID, markdownToHtml(reviewNotesMarkdown(notes, report.fixes, stats), env));

  const bodyParts = [];
  const sectionsSeen = [];
  for (let k = 0; k < all.length; k++) {
    const p = all[k];
    bodyParts.push(articleHtml(p, htmlById.get(p.id), env));
    const sec = p.id.slice(0, 2);
    const lastOfSection = k === all.length - 1 || all[k + 1].id.slice(0, 2) !== sec;
    if (lastOfSection) { sectionsSeen.push(sec); for (const sp of srcParts.get(sec) || []) bodyParts.push(...sp.parts); }
  }
  // bound sources for sections that have no page (should not happen) go at the end
  for (const [sec, v] of srcParts) if (!sectionsSeen.includes(sec)) for (const sp of v) bodyParts.push(...sp.parts);

  const DB = { critical: ' <span class="badge b-crit">CRITICAL</span>', caution: ' <span class="badge b-caut">CAUTION</span>' };
  const tocHtml = sections.map(s => {
    const rows = all.filter(p => p.id.slice(0, 2) === s.n);
    return `<details class="sec" id="sec-${s.n}"${s.n === '00' ? ' open' : ''}><summary><span class="pid">${s.n}</span> <strong>${esc(s.t)}</strong> <span class="dim">${rows.length} pages</span></summary><ul>${rows.map(p =>
      `<li><a href="#${p.id}"><span class="pid">${p.id.slice(0, 5)}</span> ${esc(p.title)}</a>${DB[p.danger_level] || ''}${p._promoted ? ' <span class="badge b-star">FOR YOU</span>' : ''}</li>`).join('')}</ul></details>`;
  }).join('\n');

  const title = `GoettschePreppy binder: ${ctx.household.name}`;
  const stamp = 'AI-reviewed, not human-verified.';
  const meta = {
    title, built, stamp, size, file_base: 'goettschepreppy-binder',
    pages: all.map(p => ({ id: p.id, t: p.title, d: p.danger_level || 'none', s: p.id.slice(0, 2), g: (p.tags || []).join(' ').toLowerCase(), st: p._state || null, stn: p._state ? STATE_NAMES[p._state] : null, c: p.condition || null, pr: !!p._promoted })),
    sections, emergency: emergencyRow(all, ctx),
    promoted: all.filter(p => p._promoted && !/^\d\d-00-/.test(p.id) && !p.id.startsWith('32-')).map(p => p.id),
    home_state: ctx.home.state, dest_states: ctx.destinations.map(d => d.region?.state).filter(Boolean),
    conditions: Object.entries(ctx.has.condition).filter(([, v]) => v).map(([k]) => k),
  };
  const generated = { version: 1, built, size, profile_hash: hash(stable({ ...profile, access: undefined })), ai: aiText,
    fixes: report.fixes, findings: notes.filter(f => f.pass !== 'urls') };
  bodyParts.push(`<script type="application/json" id="gp-generated">${jsonEmbed(generated)}</script>`);

  let parts = shellParts({ title, meta, tocHtml, bodyParts, extraCss: assets.css(), built, stamp });
  // safety net: no web address leaves this function (base64 cannot contain one: no ':' or '.')
  let redacted = 0;
  parts = parts.map(s => (typeof s === 'string' ? s.replace(URL_RE, () => { redacted++; return '[address removed]'; }) : s));
  if (redacted) report.findings.push({ page: '', pass: 'urls', severity: 'warning', fixed: true, message: `${redacted} web address(es) removed at assembly.` });
  report.pages = all.length;
  report.missingRefs = [...missingRefs].sort();
  const blob = new Blob(parts, { type: 'text/html' });
  report.bytes = blob.size;
  blob.report = report;
  progress('done', 1, 1, 'Your binder is ready');
  return blob;
}


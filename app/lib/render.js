// render.js — one kit page → binder HTML.
//
//   renderPageMarkdown(page, ctx, env)  template → Markdown (ai blocks left as tokens)
//   markdownToHtml(md, env)             Markdown → HTML, `→ NN-MM` turned into in-file links
//   articleHtml(page, bodyHtml, env)    the <article> with header, sources and the AI-reviewed stamp
//
// env = { kit, profile, ctx, pagesById (binder pages), labels, assets: { plateClass(src), figure(id) },
//         notes: [] (review notes collector), aiJobs: [] (ai block jobs collector), size, boundSources }

import { render as renderTemplate, BLANK_HTML, escapeValue } from './template.js';
import { pickInputs } from './context.js';
import { Marked } from './vendor/marked.esm.js';

export const esc = s => String(s ?? '').replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));

const marked = new Marked({ gfm: true, breaks: false });
// No autolinking of bare addresses: the binder carries no links (decision G8).
marked.use({ tokenizer: { url() { return undefined; } } });

export const cardPageId = (dc, pagesById) => {
  const n = +dc.slice(3) + 1;
  const pre = `30-${String(n).padStart(2, '0')}`;
  return pre;
};

// ---- short titles for cross-references (SHTF scripts/lib.mjs shortTitle) ------------------------
const TRAIL_WORDS = /\s+(?:&|and|the|for|of|in|a|an|to|from|with|without|by|on|at|when|into|per|—|→)$/;
export function shortTitle(title) {
  let t = String(title).trim().replace(/\s*—\s*section overview$/i, '');
  const cands = [t];
  for (const sep of [' (', ' — ', ': ', ', ', ' & ', ' and ']) { const i = t.indexOf(sep); if (i >= 6) cands.push(t.slice(0, i)); }
  let trunc = '';
  for (const w of t.split(/\s+/)) { if ((trunc + ' ' + w).trim().length > 34) break; trunc = (trunc + ' ' + w).trim(); }
  while (TRAIL_WORDS.test(trunc)) trunc = trunc.replace(TRAIL_WORDS, '');
  if (trunc.length >= 6) cands.push(trunc);
  const fit = cands.filter(c => c.length <= 34).sort((a, b) => b.length - a.length);
  return (fit[0] || t.slice(0, 34)).replace(/[·,;:]+$/, '');
}
export const titleWords = t => String(t).toLowerCase().split(/[^a-z0-9]+/).filter(w => w.length >= 4);

export function buildLabels(pages) {
  const labels = {};
  for (const p of pages) {
    const pre = p.id.slice(0, 5);
    if (!labels[pre]) labels[pre] = { id: p.id, short: shortTitle(p.title), words: titleWords(p.title) };
  }
  return labels;
}

// ---- hooks for the special template forms -------------------------------------------------------
function cardFor(kit, dc) { return (kit.cards || []).find(c => c.id === dc) || null; }

function choiceLine(dc, env) {
  const choice = env.ctx._choices?.[dc];
  const card = cardFor(env.kit, dc);
  const ref = `→ ${cardPageId(dc)}`;
  if (!choice || choice === 'undecided') return `<span class="choice">Not decided yet ${ref}</span>`;
  const opt = card?.options?.find(o => o.id === choice);
  const label = opt ? opt.label : choice.replace(/-/g, ' ');
  if (!opt && card) env.notes.push({ page: env.page?.id, kind: 'local', severity: 'warning', pass: 'slots', message: `Decision ${dc}: the saved choice "${choice}" is not one of the card's options.` });
  return `<span class="choice">Our choice (${dc}): <strong>${escapeValue(label)}</strong> ${ref}</span>`;
}

function cardBox(dc, env) {
  const card = cardFor(env.kit, dc);
  const choice = env.ctx._choices?.[dc];
  const opts = (card?.options || []).map(o =>
    `<div class="opt${o.id === choice ? ' sel' : ''}">${o.id === choice ? '&#9745;' : '&#9744;'} <strong>${escapeValue(o.label)}</strong>: ${escapeValue(o.summary)}</div>`).join('');
  const chosen = !choice || choice === 'undecided' ? 'Not decided yet. Read the card, then tick one option by hand.' : `Chosen in settings: <strong>${escapeValue(card?.options?.find(o => o.id === choice)?.label || choice)}</strong>`;
  return `\n\n<div class="cardbox"><div><strong>Our choice: ${dc}${card?.title ? ' · ' + escapeValue(card.title) : ''}</strong></div>${opts || '<div class="opt">(Options are printed on the card page.)</div>'}<div class="opt">${chosen}</div><div class="opt dim">Changed by hand to: __________________ Date: __________ Initials: ______</div></div>\n\n`;
}

// One photo per slot id across the whole binder: a slot id used on several pages (station-ports,
// kit-locations) shows the same photo everywhere. The photo itself lives once, as a CSS rule in
// <style id="gp-photos"> (written by the binder runtime), so it is stored a single time.
function photoSlot(id, env) {
  const slot = (env.page.photo_slots || []).find(s => s.id === id);
  const cap = slot?.caption || id;
  return `\n\n<figure class="photo phf-${id}" data-slot="${id}" data-caption="${esc(cap)}"><div class="phimg ph-${id}" role="img" aria-label="${esc(cap)}"></div><div class="frame">Add a photo in the app: ${esc(cap)}<br>Photos stay on this device and are never uploaded.</div><figcaption>${esc(cap)}</figcaption></figure>\n\n`;
}

function figureBlock(id, env) {
  const f = env.assets.figure(id);
  if (!f) {
    env.notes.push({ page: env.page.id, kind: 'local', severity: 'info', pass: 'figures', message: `Figure ${id} is not drawn yet; a captioned placeholder is shown.` });
    return `\n\n<figure class="fig"><div class="frame dim">Figure not drawn yet: ${esc(id)}</div><figcaption>${esc(id)}</figcaption></figure>\n\n`;
  }
  const inner = f.svg ? f.svg : f.cls ? `<div class="plimg ${f.cls}" role="img" aria-label="${esc(f.alt || f.caption || id)}" style="aspect-ratio:${f.width || 3}/${f.height || 2}"></div>` : '';
  return `\n\n<figure class="fig" id="${esc(id)}-${env.page.id.slice(0, 5)}">${inner}<figcaption>${esc(f.caption || '')}${f.credit ? `<span class="credit">${esc(f.credit)}</span>` : ''}</figcaption></figure>\n\n`;
}

const PLATE_BADGE = { deadly: 'DEADLY', lookalike: 'LOOK-ALIKE', caution: 'CAUTION', edible: 'USEFUL', firewood: 'FIREWOOD', medicinal: 'MEDICINAL' };
export function platesHtml(keys, env) {
  const blocks = (keys || []).map(key => {
    const plant = env.kit.plates?.[key];
    if (!plant) { env.notes.push({ page: env.page?.id, kind: 'local', severity: 'info', pass: 'plates', message: `Plate ${key} is not in this kit build.` }); return `<div class="plant"><h3>${esc(key)}</h3><p class="dim">Identification photographs not in this build. Never identify a plant from text alone.</p></div>`; }
    const label = PLATE_BADGE[plant.class];
    const figs = (plant.plates || []).map(pl => {
      const cls = env.assets.plateClass(pl.src);
      const cap = esc(pl.shows || '') + (pl.credit || pl.provider ? `<span class="credit">${esc([pl.credit, pl.provider].filter(Boolean).join(' · '))}</span>` : '');
      return cls ? `<figure><div class="plimg ${cls}" role="img" aria-label="${esc(plant.common)}: ${esc(pl.shows || '')}" style="aspect-ratio:${pl.width || 3}/${pl.height || 2}"></div><figcaption>${cap}</figcaption></figure>`
        : `<figure><figcaption><strong>Photo not in this build.</strong> ${cap}</figcaption></figure>`;
    }).join('');
    return `<div class="plant" id="plant-${esc(key)}-${env.page.id.slice(0, 5)}"><h3>${esc(plant.common)} <em>${esc(plant.scientific || '')}</em>${label ? ` <span class="badge b-${plant.class}">${label}</span>` : ''}</h3>${plant.note ? `<p class="dim">${esc(plant.note)}</p>` : ''}<div class="figs">${figs}</div></div>`;
  }).join('');
  if (!blocks) return '';
  return `\n\n<section class="platesec">${blocks}<p class="dim">Real photographs from the credited public-domain sources, never AI-generated. Photographs support recognition; certainty needs the full description. No wild plant is eaten on a test (→ 30-01).</p></section>\n\n`;
}

// ai blocks: a token now, the model's text later (generate.js substitutes before Markdown).
function aiToken(id, scopes, env) {
  const spec = env.kit.ai_blocks?.[id];
  const n = env.aiJobs.length;
  const token = `GPAIBLOCK${n}X`;
  if (env.page.layer !== 'household') {
    env.notes.push({ page: env.page.id, kind: 'local', severity: 'warning', pass: 'slots', message: `{{ai ${id}}} on a ${env.page.layer} page; ai blocks are allowed only on household pages. Left blank.` });
    return BLANK_HTML;
  }
  const inputs = spec ? pickInputs(env.ctx, spec.inputs, scopes) : {};
  env.aiJobs.push({ token, id, page: env.page.id, spec, inputs });
  return token;
}

export function renderPageMarkdown(page, env) {
  env.page = page;
  const blanks = [];
  const md = renderTemplate(page.body || '', env.ctx, {
    choice: id => choiceLine(id, env),
    card: id => cardBox(id, env),
    photo: id => photoSlot(id, env),
    figure: id => figureBlock(id, env),
    plates: () => platesHtml(page.plates, env),
    ai: (id, scopes) => aiToken(id, scopes, env),
    onBlank: p => blanks.push(p),
  });
  return { md, blanks };
}

// ---- Markdown → HTML ----------------------------------------------------------------------------
export function linkXrefs(html, env) {
  return html.replace(/→(?:\s|&nbsp;)?(\d{2}-\d{2})(?!\d)(?=([\s\S]{0,48}))/g, (m, pre, after) => {
    const info = env.labels[pre];
    if (!info) {
      env.missingRefs?.add(pre);
      return `→ <span class="xref missing" title="not in this binder yet">${pre}</span>`;
    }
    const ctxText = after.split('→')[0].replace(/<[^>]+>/g, ' ').toLowerCase();
    const described = info.words.some(w => ctxText.includes(w));
    return `→ <a class="xref" href="#${info.id}">${pre}${described ? '' : `<span class="xt">${esc(info.short)}</span>`}</a>`;
  });
}

export function markdownToHtml(md, env) {
  let html = marked.parse(md);
  html = html.replace(/^\s*<h1[^>]*>[\s\S]*?<\/h1>/, ''); // the article header carries the title
  return linkXrefs(html, env);
}

// ---- the article -------------------------------------------------------------------------------
const DBADGE = { critical: '<span class="badge b-crit">CRITICAL</span>', caution: '<span class="badge b-caut">CAUTION</span>' };

export function citeLine(key, env) {
  const s = env.kit.sources?.[key];
  if (!s) return `<li>${esc(key)} <span class="dim">(source record missing)</span></li>`;
  const bound = env.boundSources?.get(key);
  const where = bound ? ` <a href="#src-${esc(key)}">Read it in this binder</a>`
    : env.size === 'large' ? ' <span class="dim">(not captured; see the Sources not captured page)</span>'
    : ' <span class="dim">(cited; the document itself is in the Large download)</span>';
  return `<li>${esc(s.title)}. ${esc(s.org || '')}${s.date ? ', ' + esc(s.date) : ''}.${where}</li>`;
}

export function articleHtml(page, bodyHtml, env) {
  const m = env.meta[page.id] || {};
  const cites = (page.sources || []).length
    ? `<aside class="cites"><h2>Sources for this page</h2><ul>${page.sources.map(k => citeLine(k, env)).join('')}</ul></aside>` : '';
  const cls = ['page', page.id.endsWith('-00-section-intro') || /^\d\d-00-/.test(page.id) ? 'tab' : ''].filter(Boolean).join(' ');
  const attrs = [`id="${page.id}"`, `class="${cls}"`, `data-sec="${page.id.slice(0, 2)}"`,
    m.st ? `data-state="${m.st}"` : '', page.condition ? `data-cond="${page.condition}"` : ''].filter(Boolean).join(' ');
  return `<article ${attrs}>
<div class="ph"><span class="pid">${page.id.slice(0, 5)}</span> <h1>${esc(page.title)}</h1> ${DBADGE[page.danger_level] || ''}${m.pr ? ' <span class="badge b-star">FOR YOU</span>' : ''}</div>
${bodyHtml}
${cites}
<p class="stamp"><strong>AI-reviewed, not human-verified.</strong> ${esc(page.id)} · v${esc(page.version ?? 1)} · ${esc(page.revised || '')} · reviewed ${esc(env.reviewDate)} · <a href="#toc">Contents</a></p>
</article>
`;
}

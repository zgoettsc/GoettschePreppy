// sources.js — binding cited documents into a Large binder (docs/07-sources-and-fetch.md).
//
//   htmlToReadable(html)   publisher HTML → a plain readable article: headings, paragraphs, lists,
//                          tables, preformatted text. Scripts, styles, navigation, forms, images,
//                          every attribute and every link target are dropped; any web address in the
//                          text is removed (the binder carries no links, G8).
//   toBase64(u8)           works in the browser and in node
//   sourceBlock(...)       the <section class="srcdoc"> placed behind the citing section

import { URL_RE } from './review.js';

// ---- download sizes (decisions G11, G25) -------------------------------------------------------
//   small       pages, plates, figures; every citation as title, publisher and date; no documents
//   large       + the documents cited by the life-safety sections below, + topo maps (G16)
//   everything  + every cited document (about 1 GB in the owner's estimate; meant for a laptop)
// ctx flags: size.large is true for Large AND Everything; size.everything only for Everything.
export const SIZES = Object.freeze(['small', 'large', 'everything']);
export const LIFE_SAFETY_SECTIONS = Object.freeze(['02', '03', '04', '06', '08', '09', '12', '17', '20', '27', '30']);
export const SIZE_LABEL = Object.freeze({ small: 'Small', large: 'Large', everything: 'Everything' });
export const normalizeSize = s => (SIZES.includes(s) ? s : 'small');
export const bindsSources = size => normalizeSize(size) !== 'small';
export const isLifeSafetyPage = id => LIFE_SAFETY_SECTIONS.includes(String(id).slice(0, 2));

// Which cited documents a download binds. `cited` is Map(key → [citing page ids in binder order]).
// → { bind: Map(key → { citedBy, section }), elsewhere: Map(key → citedBy) }
//   bind       the documents this size carries; `section` is where the document is placed: the
//              section of the first citing page (Large: the first citing life-safety page)
//   elsewhere  Large only: documents cited only outside the life-safety sections; they are listed
//              by title as "in the Everything download"
export function sourcesForSize(cited, size) {
  size = normalizeSize(size);
  const bind = new Map(), elsewhere = new Map();
  if (size === 'small') return { bind, elsewhere };
  for (const [key, citedBy] of cited) {
    const ls = citedBy.filter(isLifeSafetyPage);
    if (size === 'everything') bind.set(key, { citedBy, section: String(citedBy[0]).slice(0, 2) });
    else if (ls.length) bind.set(key, { citedBy, section: ls[0].slice(0, 2) });
    else elsewhere.set(key, citedBy);
  }
  return { bind, elsewhere };
}

const esc = s => String(s ?? '').replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));

export function toBase64(u8) {
  if (typeof Buffer !== 'undefined') return Buffer.from(u8.buffer, u8.byteOffset, u8.byteLength).toString('base64');
  let s = '';
  for (let i = 0; i < u8.length; i += 0x8000) s += String.fromCharCode.apply(null, u8.subarray(i, i + 0x8000));
  return btoa(s);
}

const KEEP = new Set(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'ul', 'ol', 'li', 'table', 'thead', 'tbody', 'tr', 'td', 'th',
  'pre', 'blockquote', 'br', 'strong', 'b', 'em', 'i', 'dl', 'dt', 'dd', 'sup', 'sub', 'caption', 'hr']);
const DROP_WITH_CONTENT = ['script', 'style', 'noscript', 'nav', 'header', 'footer', 'form', 'svg', 'iframe', 'object', 'embed', 'template', 'button', 'select', 'aside', 'canvas', 'video', 'audio', 'head'];

export function decodeEntities(s) {
  return s.replace(/&(#x[0-9a-f]+|#\d+|[a-z]+);/gi, (m, e) => {
    if (e[0] === '#') { const n = e[1] === 'x' || e[1] === 'X' ? parseInt(e.slice(2), 16) : parseInt(e.slice(1), 10); return Number.isFinite(n) && n > 0 && n < 0x110000 ? String.fromCodePoint(n) : ''; }
    return { amp: '&', lt: '<', gt: '>', quot: '"', apos: "'", nbsp: ' ', mdash: '—', ndash: '–', hellip: '…', rsquo: '’', lsquo: '‘', rdquo: '”', ldquo: '“', deg: '°', copy: '©', reg: '®', trade: '™' }[e.toLowerCase()] ?? m;
  });
}

export function htmlToReadable(html) {
  let s = String(html);
  // prefer the main article when the page marks one
  const main = /<(main|article)\b[^>]*>([\s\S]*?)<\/\1>/i.exec(s);
  if (main && main[2].length > 500) s = main[2];
  s = s.replace(/<!--[\s\S]*?-->/g, '').replace(/<!\[CDATA\[[\s\S]*?\]\]>/g, '');
  for (const t of DROP_WITH_CONTENT) s = s.replace(new RegExp(`<${t}\\b[\\s\\S]*?<\\/${t}\\s*>`, 'gi'), ' ');
  s = s.replace(/<(script|style|link|meta|img|input|source|track|base)\b[^>]*>/gi, ' ');
  // tags: keep a small set without attributes; everything else becomes its text
  s = s.replace(/<\/?([a-z][a-z0-9]*)\b[^>]*>/gi, (m, tag) => {
    tag = tag.toLowerCase();
    if (!KEEP.has(tag)) return /^(div|section|li|tr|dd|dt)$/.test(tag) ? '\n' : ' ';
    return m[1] === '/' ? `</${tag}>` : `<${tag}>`;
  });
  s = s.replace(/<[^>]*$/, '');
  // text: decode then re-escape (so nothing executable survives), drop addresses
  s = s.split(/(<\/?[a-z0-9]+>)/i).map((part, i) => i % 2 ? part : esc(decodeEntities(part)).replace(URL_RE, '[address removed]')).join('');
  return s.replace(/[ \t ]+/g, ' ').replace(/\n\s*\n+/g, '\n').replace(/<p>\s*<\/p>/g, '').trim();
}

export function textToReadable(text) {
  return `<pre>${esc(String(text).replace(URL_RE, '[address removed]'))}</pre>`;
}

const MB = n => (n / 1e6).toFixed(1) + ' MB';

// One bound document. `doc` = { key, src (kit source record), contentType, bytes, text? }
// Returns an array of string parts.
function srcHead(key, s, { citedBy = [], sectionNo }) {
  return `<section class="srcdoc" id="src-${esc(key)}" data-sec="${esc(sectionNo)}">
<div class="srchead">Bound source, for this household's private copy (do not share): <strong>${esc(s.title || key)}</strong>. ${esc(s.org || '')}${s.date ? ', ' + esc(s.date) : ''}.${s.licence_note ? ' ' + esc(String(s.licence_note).replace(URL_RE, '')) : ''}
${citedBy.length ? ' Cited by: ' + citedBy.map(id => `→ <a class="xref" href="#${id}">${id.slice(0, 5)}</a>`).join(' ') : ''}</div>
<div class="srcbody">`;
}
const SRC_TAIL = `</div></section>\n`;

// ---- upgrade: reuse the documents an earlier binder already holds -------------------------------
// Large → Everything (or a rebuild) binds the documents the earlier file carries without fetching
// or rendering them again. → Map(key → inner HTML of its <div class="srcbody">). The earlier file
// is the household's own, but it is checked like any input: a body that holds anything but text
// markup, page pictures (data: images) and the embedded-PDF block is not reused.
export function extractBoundSources(html) {
  const out = new Map();
  const s = String(html || '');
  const re = /<section class="srcdoc" id="src-([a-z0-9-]+)"[^>]*>/g;
  let m;
  while ((m = re.exec(s))) {
    const open = s.indexOf('<div class="srcbody">', m.index);
    if (open < 0) break;
    const end = s.indexOf(SRC_TAIL.trim(), open);
    if (end < 0) break;
    const body = s.slice(open + '<div class="srcbody">'.length, end);
    if (!m[1].startsWith('map-') && safeReusedBody(body)) out.set(m[1], body);
    re.lastIndex = end;
  }
  return out;
}
export function safeReusedBody(body) {
  const rest = String(body)
    .replace(/<script type="application\/pdf" id="pdf-[a-z0-9-]+">[A-Za-z0-9+/=]*<\/script>/g, '')
    .replace(/\ssrc="data:image\/(jpeg|png|webp|gif);base64,[A-Za-z0-9+/=]*"/g, '');
  return !/<(script|iframe|object|embed|link|style|meta|base|form|svg|math|template)\b|\son[a-z]+\s*=|javascript:|\s(src|href|srcset|action|formaction|xlink:href)\s*=/i.test(rest);
}
export function reusedSourceBlock(key, src, body, where) {
  return [srcHead(key, src || {}, where), body, SRC_TAIL];
}

export function sourceBlock(doc, { citedBy = [], sectionNo }) {
  const s = doc.src || {};
  const head = srcHead(doc.key, s, { citedBy, sectionNo });
  const tail = SRC_TAIL;
  const ct = doc.contentType || '';
  if (ct.includes('html')) return [head, htmlToReadable(new TextDecoder().decode(doc.bytes)), tail];
  if (ct.startsWith('text/')) return [head, textToReadable(new TextDecoder().decode(doc.bytes)), tail];
  if (ct === 'application/pdf' && doc.rendered?.pages?.length) {
    // rendered pages: readable and printable everywhere; the PDF itself is kept only when the
    // document was too long to render in full
    const r = doc.rendered;
    const out = [head, `<p class="dim">${r.total} page${r.total === 1 ? '' : 's'}${r.truncated ? `; the first ${r.pages.length} are shown as pictures, the whole document is inside this file` : ''}.</p>`];
    r.pages.forEach((pg, i) => out.push(`<img class="pdfpage" loading="lazy" alt="${esc(s.title || doc.key)}, page ${i + 1}" width="${pg.width}" height="${pg.height}" src="data:image/jpeg;base64,`, toBase64(pg.bytes), `">`));
    if (r.truncated) {
      const id = `pdf-${doc.key}`;
      out.push(`<p><button type="button" class="jsonly" data-open-pdf="${esc(id)}" data-name="${esc(doc.key)}.pdf">Open the whole document</button></p>`, `<script type="application/pdf" id="${esc(id)}">`, toBase64(doc.bytes), `</script>`);
    }
    out.push(tail);
    return out;
  }
  if (ct === 'application/pdf') {
    const id = `pdf-${doc.key}`;
    return [head,
      `<p><button type="button" class="jsonly" data-open-pdf="${esc(id)}" data-name="${esc(doc.key)}.pdf">Open the document</button> PDF, ${MB(doc.bytes.length)}. In a reader that cannot run the app, open this file in a browser to open the PDF.</p>`,
      doc.text ? textToReadable(doc.text) : '<p class="dim">The full document is inside this file; its text is not shown here.</p>',
      `<script type="application/pdf" id="${esc(id)}">`, toBase64(doc.bytes), `</script>`, tail];
  }
  if (ct.startsWith('image/')) {
    return [head, `<img alt="${esc(s.title || doc.key)}" src="data:${esc(ct)};base64,`, toBase64(doc.bytes), `">`, tail];
  }
  return [head, `<p class="dim">A ${esc(ct || 'binary')} document (${MB(doc.bytes.length)}) is bound here but cannot be shown.</p>`, tail];
}

// shell.js — the offline binder file around the pages: head, header bar, static contents, footer,
// the metadata block and the runtime. Adapted from the household binder (SHTF build-app.mjs).
//
// shellParts({ title, meta, tocHtml, bodyParts, extraCss, built, stamp }) → array of strings,
// in order, for `new Blob(parts)`. Nothing here references anything outside the file.

import { BINDER_CSS } from './styles.js';
import { binderRuntime } from './runtime.js';

export const escHtml = s => String(s ?? '').replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
export const jsonEmbed = o => JSON.stringify(o).replace(/</g, '\\u003c');

export function shellParts({ title, meta, tocHtml, bodyParts, extraCss = '', built, stamp }) {
  const head = `<!doctype html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="color-scheme" content="dark light">
<meta name="referrer" content="no-referrer">
<title>${escHtml(title)}</title>
<style>${BINDER_CSS}</style>
<style>${extraCss}</style>
</head><body>
<header class="top"><div id="modebar">READING MODE: this viewer shows the whole binder but cannot run the app.
For search, the region and condition pickers and photos, open this file in Safari, Chrome or Firefox.
Here, <a href="#toc">Contents</a> navigates and every page ends with a link back.</div>
<div class="bar">
<a id="back" class="hbtn" href="#toc" aria-label="Back">&#9776;</a>
<input id="q" type="search" placeholder="Search the binder (e.g. water heater, CO alarm)" autocomplete="off" aria-label="Search">
<button id="pin" class="jsonly gp-ui-keep" aria-label="Pin this page" hidden>&#9734;</button>
<button id="print" class="jsonly" aria-label="Print or save as PDF" title="Print or save as PDF">&#9113;</button>
<button id="theme" aria-label="Light or dark">&#9680;</button>
</div><div id="err"></div></header>
<main>
<div id="view"></div>
<div id="staticnote" class="note"><strong>${escHtml(title)}</strong>, offline edition. Everything is in this one file:
use the contents below or your reader's find-in-page. If the search box does nothing, this viewer is not running the
app; open the file in Safari, Chrome or Firefox for search. <span class="dim">${escHtml(stamp)}</span></div>
<nav id="tocwrap"><h1 id="toc">Contents</h1>
${tocHtml}
</nav>
<div id="pages">
`;
  const tail = `
</div>
</main>
<div id="savebar" class="gp-ui-keep">You added or removed photos. They are only in this open copy until you save.
<button id="savecopy" type="button">Save a new copy</button></div>
<footer>${escHtml(title)} · built ${escHtml(built)} · ${meta.pages.length} pages · ${escHtml(stamp)}<br>
Works with no network. Keep a copy on every phone and laptop, and print the pages that matter.</footer>
<script type="application/json" id="gp-meta">${jsonEmbed(meta)}</script>
<script>(${binderRuntime.toString()})();</script>
</body></html>
`;
  return [head, ...bodyParts, tail];
}

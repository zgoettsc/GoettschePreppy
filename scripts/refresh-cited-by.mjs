// refresh-cited-by.mjs: recompute sources/index.json `cited_by` from page frontmatter.
//   node scripts/refresh-cited-by.mjs
import fs from 'node:fs';
import path from 'node:path';
import url from 'node:url';
import yaml from 'js-yaml';
const ROOT = path.resolve(path.dirname(url.fileURLToPath(import.meta.url)), '..');
const idx = JSON.parse(fs.readFileSync(path.join(ROOT, 'sources/index.json'), 'utf8'));
const cites = {};
const C = path.join(ROOT, 'content/sections');
for (const d of fs.readdirSync(C)) for (const f of fs.readdirSync(path.join(C, d))) {
  if (!f.endsWith('.md')) continue;
  const m = /^---\n([\s\S]*?)\n---/.exec(fs.readFileSync(path.join(C, d, f), 'utf8'));
  if (!m) continue;
  const fm = yaml.load(m[1], { schema: yaml.JSON_SCHEMA }) || {};
  for (const k of fm.sources || []) (cites[k] ??= []).push(fm.id);
}
for (const x of idx) x.cited_by = (cites[x.key] || []).sort();
fs.writeFileSync(path.join(ROOT, 'sources/index.json'), JSON.stringify(idx, null, 1));
const byClass = {}; let uncited = 0;
for (const x of idx) { if (!x.cited_by.length) { uncited++; continue; } byClass[x.licence_class] = (byClass[x.licence_class] || 0) + 1; }
const missing = Object.keys(cites).filter(k => !idx.some(x => x.key === k));
console.log('cited by class', byClass, 'uncited', uncited, 'missing keys', missing.length);

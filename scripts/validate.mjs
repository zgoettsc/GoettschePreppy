// validate.mjs: check every kit page against the authoring spec.
//   node scripts/validate.mjs [path-prefix]
// Fails (exit 1) on: bad frontmatter, URLs or external links, owner tokens, unknown
// template paths/flags/lists, unknown card/explainer/condition ids, bad cross-refs
// syntax, ai blocks outside household pages, unknown source keys.
import fs from 'node:fs';
import path from 'node:path';
import url from 'node:url';
import yaml from 'js-yaml';
import Ajv from 'ajv';

const ROOT = path.resolve(path.dirname(url.fileURLToPath(import.meta.url)), '..');
const CONTENT = path.join(ROOT, 'content', 'sections');
const only = process.argv[2] || '';
const schema = JSON.parse(fs.readFileSync(path.join(ROOT, 'schema/page.schema.json'), 'utf8'));
const ctx = JSON.parse(fs.readFileSync(path.join(ROOT, 'schema/context.json'), 'utf8'));
const tokens = JSON.parse(fs.readFileSync(path.join(ROOT, 'scripts/owner-tokens.json'), 'utf8'));
const srcIndex = fs.existsSync(path.join(ROOT, 'sources/index.json'))
  ? JSON.parse(fs.readFileSync(path.join(ROOT, 'sources/index.json'), 'utf8')) : [];
const srcKeys = new Set(srcIndex.map(s => s.key));
const addDir = path.join(ROOT, 'sources/additions');
if (fs.existsSync(addDir)) for (const f of fs.readdirSync(addDir)) if (f.endsWith('.json'))
  for (const s of JSON.parse(fs.readFileSync(path.join(addDir, f), 'utf8'))) srcKeys.add(s.key);

const ajv = new Ajv({ allErrors: true });
const check = ajv.compile(schema);

const valuePaths = new Set(Object.keys(ctx.values));
const flags = new Set(Object.keys(ctx.flags));
for (let i = 1; i <= 26; i++) flags.add(`has.condition.CL-${String(i).padStart(2, '0')}`);
const lists = new Set(Object.keys(ctx.lists));
const isFlag = f => flags.has(f.replace(/^!/, ''));
const regionField = p => /^region\.(home|dest)\./.test(p) && valuePaths.has(p.replace(/^region\.dest\./, 'region.dest.'));

const wordRe = tokens.words.map(w => new RegExp(`(^|[^A-Za-z0-9])${w.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}([^A-Za-z0-9]|$)`));
const patRe = tokens.patterns.map(p => new RegExp(p));

const errors = [], warnings = [];
let n = 0;
const ids = new Set();
const pages = [];
for (const dir of fs.existsSync(CONTENT) ? fs.readdirSync(CONTENT).sort() : []) {
  const abs = path.join(CONTENT, dir);
  if (!fs.statSync(abs).isDirectory()) continue;
  for (const f of fs.readdirSync(abs).sort()) {
    if (!f.endsWith('.md')) continue;
    const rel = path.join('content/sections', dir, f);
    if (only && !rel.includes(only)) continue;
    pages.push({ rel, dir, f, text: fs.readFileSync(path.join(abs, f), 'utf8') });
  }
}
for (const p of pages) {
  const m = /^---\r?\n([\s\S]*?)\r?\n---\r?\n?([\s\S]*)$/.exec(p.text);
  if (m) { try { ids.add((yaml.load(m[1], { schema: yaml.JSON_SCHEMA }) || {}).id); } catch {} }
}
for (const { rel, dir, f, text } of pages) {
  n++;
  const err = msg => errors.push(`${rel}: ${msg}`);
  const warn = msg => warnings.push(`${rel}: ${msg}`);
  const m = /^---\r?\n([\s\S]*?)\r?\n---\r?\n?([\s\S]*)$/.exec(text);
  if (!m) { err('no frontmatter'); continue; }
  let data;
  try { data = yaml.load(m[1], { schema: yaml.JSON_SCHEMA }) || {}; } catch (e) { err('YAML: ' + e.message); continue; }
  const body = m[2];
  if (!check(data)) for (const e of check.errors) err(`frontmatter ${e.instancePath || '/'} ${e.message}`);
  if (data.id && f !== `${data.id}.md`) err(`filename does not match id ${data.id}`);
  if (data.section && data.section !== dir) err(`section ${data.section} does not match folder ${dir}`);
  if (data.id && data.id.slice(0, 2) !== dir.slice(0, 2)) err('id prefix does not match section number');
  const exempt = dir.startsWith('31-') || dir.startsWith('32-');
  // links
  if (/https?:\/\/|www\.[a-z0-9-]+\.[a-z]/i.test(text)) err('contains a URL (no links anywhere)');
  if (/\]\((?!#)[^)]*\)/.test(body)) err('contains a Markdown link (cross-reference with → NN-MM instead)');
  // owner tokens
  if (!exempt) {
    tokens.words.forEach((w, i) => { if (wordRe[i].test(text)) err(`owner token "${w}"`); });
    tokens.patterns.forEach((pt, i) => { if (patRe[i].test(text)) err(`owner pattern /${pt}/`); });
  }
  // template tags
  const loopVars = new Set();
  for (const t of body.matchAll(/\{\{\s*([^}]*?)\s*\}\}/g)) {
    const tag = t[1];
    let mm;
    if ((mm = /^#if\s+(\S+)$/.exec(tag))) { if (!isFlag(mm[1]) && !loopVars.has(mm[1].replace(/^!/, '').split('.')[0])) err(`unknown flag ${mm[1]}`); }
    else if (tag === 'else' || tag === '/if' || tag === '/each' || tag === 'plates') {}
    else if ((mm = /^#each\s+(\S+)\s+as\s+([a-z_]+)$/.exec(tag))) { const head = mm[1].split('.')[0]; if (!lists.has(mm[1]) && !loopVars.has(head)) err(`unknown list ${mm[1]}`); loopVars.add(mm[2]); }
    else if ((mm = /^(choice|card)\s+(DC-\d{2})$/.exec(tag))) { const k = +mm[2].slice(3); if (k < 1 || k > 29) err(`unknown card ${mm[2]}`); if (mm[1] === 'card' && !['card', 'generated', 'household'].includes(data.layer)) warn(`{{card}} outside a card page`); }
    else if ((mm = /^photo\s+([a-z0-9-]+)$/.exec(tag))) { if (!(data.photo_slots || []).some(s => s.id === mm[1])) err(`photo slot ${mm[1]} not declared in photo_slots`); }
    else if ((mm = /^figure\s+(fig-[a-z0-9-]+)$/.exec(tag))) { if (!(data.figures || []).includes(mm[1])) err(`figure ${mm[1]} not declared in figures`); }
    else if ((mm = /^ai\s+([a-z0-9-]+)$/.exec(tag))) { if (data.layer !== 'household') err('{{ai}} allowed only on household pages'); if (!fs.existsSync(path.join(ROOT, 'content/ai-blocks', mm[1] + '.md'))) warn(`ai block spec content/ai-blocks/${mm[1]}.md missing`); }
    else if (/^[a-z_]+(\.[A-Za-z0-9_\-\[\]]+)*$/.test(tag)) {
      const head = tag.split('.')[0];
      if (loopVars.has(head)) continue;
      if (!valuePaths.has(tag) && !regionField(tag)) err(`unknown path ${tag}`);
    }
    else err(`unrecognised template tag {{${tag}}}`);
  }
  const opens = (body.match(/\{\{#if /g) || []).length, closes = (body.match(/\{\{\/if\}\}/g) || []).length;
  if (opens !== closes) err(`#if/\/if mismatch (${opens}/${closes})`);
  const eo = (body.match(/\{\{#each /g) || []).length, ec = (body.match(/\{\{\/each\}\}/g) || []).length;
  if (eo !== ec) err(`#each/\/each mismatch (${eo}/${ec})`);
  // references
  for (const k of data.sources || []) if (srcKeys.size && !srcKeys.has(k)) err(`unknown source key ${k}`);
  for (const r of data.related || []) if (!ids.has(r)) warn(`related page ${r} not (yet) present`);
  if (data.danger_level === 'critical' && !(data.sources || []).length) err('critical page with no sources');
  if (data.danger_level === 'critical' && !/>\s*\*\*SAFETY/.test(body)) warn('critical page without a > **SAFETY** callout');
  if (!exempt && /\b(Novolog|Humalog|Lantus)\b.*\b\d+(\.\d+)?\s*(U|units)\b/.test(body)) warn('looks like a dose; check the no-derived-dosing rule');
}
for (const w of warnings) console.log('WARN  ' + w);
for (const e of errors) console.log('ERROR ' + e);
console.log(`${n} pages checked, ${errors.length} errors, ${warnings.length} warnings`);
process.exit(errors.length ? 1 : 0);

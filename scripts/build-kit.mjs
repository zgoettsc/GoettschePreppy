// build-kit.mjs — everything the browser needs to generate a binder, built from the repo.
//
//   npm run build:kit          → app/build/kit.json, app/build/regions-lite.json,
//                                app/build/plates/**, app/build/figures/**, app/build/sources/**
//
// Reads: content/sections/** (pages), content/ai-blocks/*.md, sources/index.json (+ additions),
// sources/archive/<key>.* (kit-shipped PD/open documents), data/regions/** (D1), images/index.json
// (D2 plates), figures/index.json, data/page-plan.json, scripts/owner-tokens.json,
// NOTICE-TO-USERS.md. File formats: notes/workers/A3.md §1. Every input except content/ is
// optional; the build degrades and says what is missing.
//
// Generates `layer: generated` pages: section intros (NN-00), 00-03 master index, 00-08 binder
// map, 25-06 bibliography, and (when no Section 32 pages are authored) one page per state plus the
// national plate pages, from data/regions/ and images/.
//
// No URL is written into kit.json except kit.maps (USGS map addresses for the relay's fetch-map;
// never printed). Pages are carried as template Markdown; the browser fills them.

import fs from 'node:fs';
import path from 'node:path';
import url from 'node:url';
import { execFileSync } from 'node:child_process';
import yaml from 'js-yaml';

const ROOT = path.resolve(path.dirname(url.fileURLToPath(import.meta.url)), '..');
// Test hooks: GP_DATA_ROOT replaces the folder that holds data/regions/, images/ and figures/;
// GP_KIT_OUT replaces app/build/ (scripts/test-generate.mjs uses both with tests/fixtures/).
const OUT = process.env.GP_KIT_OUT ? path.resolve(process.env.GP_KIT_OUT) : path.join(ROOT, 'app', 'build');
const DATA = process.env.GP_DATA_ROOT ? path.resolve(process.env.GP_DATA_ROOT) : ROOT;
const existsD = p => fs.existsSync(path.join(DATA, p));
const readJsonD = (p, d = null) => { try { return JSON.parse(fs.readFileSync(path.join(DATA, p), 'utf8')); } catch (e) { if (existsD(p)) warn(`${p}: ${e.message}`); return d; } };
const rel = p => path.relative(ROOT, p);
const exists = p => fs.existsSync(path.join(ROOT, p));
const readJson = (p, d = null) => { try { return JSON.parse(fs.readFileSync(path.join(ROOT, p), 'utf8')); } catch (e) { if (exists(p)) warn(`${p}: ${e.message}`); return d; } };
const warnings = [];
const warn = m => warnings.push(m);
const TODAY = new Date().toISOString().slice(0, 10);
const URL_RE = /https?:\/\/[^\s"'<>)\]]*|\bwww\.[a-z0-9-]+\.[a-z][^\s"'<>)\]]*/gi;
const stripUrls = s => (typeof s === 'string' ? s.replace(URL_RE, '').replace(/\s{2,}/g, ' ').trim() : s);

import { STATE_NAMES } from '../app/lib/context.js';

fs.mkdirSync(OUT, { recursive: true });

// ---- section titles ----------------------------------------------------------------------------
const plan = readJson('data/page-plan.json', { sections: {}, from_household: [], new_pages: [] });
const SECTION_TITLES = {
  '00': 'Front matter', '01': 'Phase playbooks', '02': 'Medical conditions', '03': 'Water',
  '04': 'Food storage and preservation', '05': 'Food production and foraging', '06': 'Fire and fuel',
  '07': 'Cooking off-grid', '08': 'Heating and cold-weather shelter', '09': 'Power and energy', '10': 'Lighting',
  '11': 'Clothing and personal warmth', '12': 'Medical and first aid', '13': 'Sanitation and waste',
  '14': 'Security and defense', '15': 'Communications', '16': 'Tools and repair', '17': 'Weather and regional hazards',
  '18': 'Community, barter and governance', '19': 'Finances and documents', '20': 'Kids and family',
  '21': 'Morale and mental health', '22': 'Master lists: acquire and scavenge', '23': 'Depletion and substitution',
  '24': 'Skills to practise now', '25': 'Reference and appendices', '26': 'Pre-disaster acquisition checklist',
  '27': 'CBRN and EMP', '28': 'Gear reference', '29': 'Explainers', '30': 'Decisions and floors',
  '31': 'SERE field reference (Air Force Handbook 10-644)', '32': 'Region appendix',
};
const sections = {};
for (const [n, folder] of Object.entries(plan.sections || {})) sections[n] = { folder, title: SECTION_TITLES[n] || folder.slice(3).replace(/-/g, ' ') };
for (const [n, t] of Object.entries(SECTION_TITLES)) if (!sections[n]) sections[n] = { folder: null, title: t };

// ---- pages -------------------------------------------------------------------------------------
const pages = [];
const CONTENT = path.join(ROOT, 'content', 'sections');
for (const dir of fs.existsSync(CONTENT) ? fs.readdirSync(CONTENT).sort() : []) {
  const abs = path.join(CONTENT, dir);
  if (!fs.statSync(abs).isDirectory()) continue;
  if (sections[dir.slice(0, 2)]) sections[dir.slice(0, 2)].folder = dir;
  for (const f of fs.readdirSync(abs).sort()) {
    if (!f.endsWith('.md')) continue;
    const text = fs.readFileSync(path.join(abs, f), 'utf8');
    const m = /^---\r?\n([\s\S]*?)\r?\n---\r?\n?([\s\S]*)$/.exec(text);
    if (!m) { warn(`${dir}/${f}: no frontmatter, skipped`); continue; }
    let data;
    try { data = yaml.load(m[1], { schema: yaml.JSON_SCHEMA }) || {}; } catch (e) { warn(`${dir}/${f}: YAML error, skipped (${e.message.split('\n')[0]})`); continue; }
    if (!data.id || !/^\d{2}-\d{2}-[a-z0-9-]+$/.test(data.id) || !data.title) { warn(`${dir}/${f}: missing or bad id/title, skipped`); continue; }
    if (URL_RE.test(text)) { warn(`${data.id}: contains a URL; the generator will remove it`); URL_RE.lastIndex = 0; }
    pages.push({ ...data, section: data.section || dir, body: m[2] });
  }
}
const have = new Set(pages.map(p => p.id.slice(0, 5)));
console.log(`pages: ${pages.length} authored`);

// ---- sources -----------------------------------------------------------------------------------
const srcList = [...(readJson('sources/index.json', []) || [])];
if (exists('sources/additions')) for (const f of fs.readdirSync(path.join(ROOT, 'sources/additions')).sort()) if (f.endsWith('.json')) {
  for (const s of readJson(`sources/additions/${f}`, []) || []) if (!srcList.some(x => x.key === s.key)) srcList.push(s);
}
const sources = {};
const archiveDir = path.join(ROOT, 'sources', 'archive');
const archived = fs.existsSync(archiveDir) ? fs.readdirSync(archiveDir) : [];
fs.mkdirSync(path.join(OUT, 'sources'), { recursive: true });
for (const s of srcList) {
  const file = archived.find(f => f.replace(/\.[^.]+$/, '') === s.key);
  let shipped = null;
  if (file && ['public-domain', 'open'].includes(s.licence_class)) {
    const dest = path.join(OUT, 'sources', file);
    const srcPath = path.join(archiveDir, file);
    if (!fs.existsSync(dest) || fs.statSync(dest).mtimeMs < fs.statSync(srcPath).mtimeMs) fs.copyFileSync(srcPath, dest);
    shipped = `sources/${file}`;
  }
  sources[s.key] = { title: stripUrls(s.title), org: stripUrls(s.org || ''), date: s.date || '', licence_class: s.licence_class,
    licence_note: stripUrls(s.licence_note || ''), shipped, bytes: shipped ? fs.statSync(path.join(OUT, shipped)).size : 0, cited_by: [] };
}
for (const p of pages) for (const k of p.sources || []) if (sources[k]) sources[k].cited_by.push(p.id); else warn(`${p.id}: unknown source key ${k}`);

// ---- regions -----------------------------------------------------------------------------------
const regions = {};
const maps = {};
function addState(obj, file) {
  if (!obj || typeof obj !== 'object' || !/^[A-Z]{2}$/.test(obj.state || '')) return false;
  const st = { state: obj.state, state_name: obj.state_name || STATE_NAMES[obj.state], state_em: stripUrls(obj.state_em || null),
    sources: obj.sources || [], defaults: obj.defaults || {}, counties: {} };
  for (const [name, c] of Object.entries(obj.counties || {})) {
    const { topo_maps, ...rest } = c || {};
    if (Array.isArray(topo_maps) && topo_maps.length) ((maps[obj.state] ||= {})[name] = topo_maps.map(m => ({ title: stripUrls(m.title || 'USGS topographic map'), url: m.url, date: m.date || '' })));
    st.counties[name] = JSON.parse(JSON.stringify(rest), (k, v) => (typeof v === 'string' ? stripUrls(v) : v));
  }
  regions[obj.state] = st;
  return true;
}
for (const dir of ['data/regions/states', 'data/regions']) {
  if (!existsD(dir)) continue;
  for (const f of fs.readdirSync(path.join(DATA, dir)).sort()) {
    if (!f.endsWith('.json') || f === 'ecoregions.json') continue;
    const st = f.replace(/\.json$/, '').toUpperCase();
    if (regions[st]) continue;
    addState(readJsonD(`${dir}/${f}`), `${dir}/${f}`);
  }
}
const ecoregions = readJsonD('data/regions/ecoregions.json', {}) || {};
console.log(`regions: ${Object.keys(regions).length} states with data, ${Object.keys(ecoregions).length} ecoregions`);
if (!Object.keys(regions).length) warn('data/regions/: no state files yet; regions-lite has empty county lists and region slots print blank');

const lite = {};
for (const [code, name] of Object.entries(STATE_NAMES).sort((a, b) => a[1].localeCompare(b[1])))
  lite[code] = { name, counties: Object.keys(regions[code]?.counties || {}).sort() };
fs.writeFileSync(path.join(OUT, 'regions-lite.json'), JSON.stringify(lite));

// ---- plates ------------------------------------------------------------------------------------
const hasConvert = (() => { try { execFileSync('convert', ['-version'], { stdio: 'ignore' }); return true; } catch { return false; } })();
const plates = {};
const imgIdx = readJsonD('images/index.json');
let plateBytes = 0;
for (const pl of imgIdx?.plants || []) {
  const out = { common: pl.common, scientific: pl.scientific || null, class: pl.class || 'other', note: stripUrls(pl.note || ''),
    lookalikes: pl.lookalikes || [], ecoregions: pl.ecoregions || [], plates: [] };
  for (const im of pl.plates || []) {
    if (!im.file) continue;
    const srcAbs = path.join(DATA, im.file);
    if (!fs.existsSync(srcAbs)) { warn(`plate ${pl.key}: ${im.file} missing`); continue; }
    const base = path.basename(im.file).replace(/\.[^.]+$/, '');
    const destRel = `plates/${pl.key}/${base}.jpg`;
    const dest = path.join(OUT, destRel);
    fs.mkdirSync(path.dirname(dest), { recursive: true });
    if (!fs.existsSync(dest) || fs.statSync(dest).mtimeMs < fs.statSync(srcAbs).mtimeMs) {
      if (hasConvert) execFileSync('convert', [srcAbs + '[0]', '-auto-orient', '-resize', '720x720>', '-strip', '-sampling-factor', '4:2:0', '-quality', '62', '-interlace', 'JPEG', dest]);
      else fs.copyFileSync(srcAbs, dest);
    }
    let w = im.width, h = im.height;
    if (hasConvert) { try { [w, h] = execFileSync('identify', ['-format', '%w %h', dest]).toString().split(' ').map(Number); } catch {} }
    plateBytes += fs.statSync(dest).size;
    out.plates.push({ src: destRel, shows: stripUrls(im.shows || ''), credit: stripUrls(im.credit || ''), provider: stripUrls(im.provider || ''),
      license: stripUrls(im.license || imgIdx.collections?.[im.collection]?.license || ''), width: w || 3, height: h || 2 });
  }
  plates[pl.key] = out;
}
console.log(`plates: ${Object.keys(plates).length} species, ${(plateBytes / 1e6).toFixed(1)} MB after recompression${hasConvert ? '' : ' (convert not found: copied as-is)'}`);

// ---- figures -----------------------------------------------------------------------------------
export function sanitizeSvg(svg) {
  let s = String(svg)
    .replace(/<\?xml[\s\S]*?\?>/g, '').replace(/<!DOCTYPE[\s\S]*?>/gi, '').replace(/<!--[\s\S]*?-->/g, '')
    .replace(/<(script|foreignObject)\b[\s\S]*?<\/\1\s*>/gi, '').replace(/<metadata\b[\s\S]*?<\/metadata\s*>/gi, '')
    .replace(/\s(on[a-z]+)\s*=\s*("[^"]*"|'[^']*')/gi, '')
    .replace(/\sxmlns(:[a-z]+)?\s*=\s*("[^"]*"|'[^']*')/gi, '')
    .replace(/\s(xlink:)?href\s*=\s*("(?!#)[^"]*"|'(?!#)[^']*')/gi, '')
    .replace(/\s[a-z:-]+\s*=\s*("[^"]*https?:[^"]*"|'[^']*https?:[^']*')/gi, '')
    .replace(/\s(sodipodi|inkscape):[a-z-]+\s*=\s*("[^"]*"|'[^']*')/gi, '')
    .replace(/<(sodipodi|inkscape):[\s\S]*?(\/>|<\/\1:[a-z]+>)/gi, '');
  return s.replace(URL_RE, '').trim().replace(/^<svg\b/, '<svg role="img"');
}
const figures = {};
const figIdxRaw = readJsonD('figures/index.json');
const figEntries = Array.isArray(figIdxRaw) ? figIdxRaw.map(f => [f.id, f]) : Object.entries(figIdxRaw?.figures || figIdxRaw || {});
for (const [id, f] of figEntries) {
  if (!/^fig-[a-z0-9-]+$/.test(id || '') || !f?.file) continue;
  const abs = path.join(DATA, f.file);
  if (!fs.existsSync(abs)) { warn(`figure ${id}: ${f.file} missing`); continue; }
  const meta = { caption: stripUrls(f.caption || ''), alt: stripUrls(f.alt || f.caption || ''), credit: stripUrls(f.credit || '') };
  if (f.file.endsWith('.svg')) figures[id] = { ...meta, svg: sanitizeSvg(fs.readFileSync(abs, 'utf8')) };
  else {
    const destRel = `figures/${path.basename(f.file)}`;
    fs.mkdirSync(path.join(OUT, 'figures'), { recursive: true });
    fs.copyFileSync(abs, path.join(OUT, destRel));
    figures[id] = { ...meta, src: destRel, width: f.width || 4, height: f.height || 3 };
  }
}
console.log(`figures: ${Object.keys(figures).length}`);

// ---- ai block specs ----
// The "## Inputs" section of a spec (content/ai-blocks/README.md): each bullet names backticked
// context paths. A bullet whose first backticked token is `list[]` projects that list to the
// backticked field names that follow; after `region`, names are fields of the item's region.
export function parseAiInputs(md) {
  const sec = /^##\s+Inputs\b[^\n]*\n([\s\S]*?)(?=^##\s|(?![\s\S]))/m.exec(md);
  if (!sec) return [];
  // a parenthesis that says "not" excludes the names inside it: (do **not** use `strength`)
  const bullets = sec[1].split(/\n(?=\s*[-*]\s)/).map(b => b.replace(/\s+/g, ' ').replace(/\([^)]*\bnot\b[^)]*\)/gi, ''));
  const out = [];
  const isPath = t => /^[a-z_][a-z0-9_]*(\.[A-Za-z0-9_-]+)*$/.test(t);
  for (const b of bullets) {
    const toks = [...b.matchAll(/`([^`]+)`/g)].map(x => x[1].trim());
    if (!toks.length) continue;
    const lm = /^([a-z_][a-z0-9_.]*)\[\]$/.exec(toks[0]);
    if (lm) {
      const spec = { list: lm[1], fields: [], region: [] };
      let inRegion = false;
      for (const t of toks.slice(1)) {
        if (t === 'region') { inRegion = true; continue; }
        if (/^[a-z_][a-z0-9_]*$/.test(t)) (inRegion ? spec.region : spec.fields).push(t);
      }
      out.push(spec);
      continue;
    }
    for (let t of toks) {
      t = t.replace(/\.CL-NN$/, '');
      if (isPath(t) && !out.includes(t)) out.push(t);
    }
  }
  return out;
}
const ai_blocks = {};
if (exists('content/ai-blocks')) for (const f of fs.readdirSync(path.join(ROOT, 'content/ai-blocks')).sort()) {
  if (!f.endsWith('.md') || f === 'README.md') continue;
  const text = fs.readFileSync(path.join(ROOT, 'content/ai-blocks', f), 'utf8');
  const m = /^---\r?\n([\s\S]*?)\r?\n---\r?\n?([\s\S]*)$/.exec(text);
  let fm = {};
  try { fm = m ? yaml.load(m[1], { schema: yaml.JSON_SCHEMA }) || {} : {}; } catch (e) { warn(`ai block ${f}: ${e.message}`); }
  const id = fm.id || f.replace(/\.md$/, '');
  const inputs = fm.inputs || parseAiInputs(m ? m[2] : text);
  if (!inputs.length) warn(`ai block ${id}: no inputs found (see content/ai-blocks/README.md)`);
  ai_blocks[id] = { inputs, text: stripUrls(text) };
}

// ---- cards -------------------------------------------------------------------------------------
const cards = pages.filter(p => p.card || p.layer === 'card').map(p => ({
  id: p.card || ('DC-' + String(+p.id.slice(3, 5) - 1).padStart(2, '0')), page_id: p.id, title: p.title,
  options: p.options || [], settings_summary: p.settings_summary || '',
})).sort((a, b) => a.id.localeCompare(b.id));

// ---- generated pages ---------------------------------------------------------------------------
const gen = [];
const genPage = (id, title, body, extra = {}) => ({ id, section: sections[id.slice(0, 2)]?.folder || `${id.slice(0, 2)}-generated`, title, version: 1, revised: TODAY,
  layer: 'generated', danger_level: 'none', phase: ['A', 'B', 'C'], tags: [], derived_from: [], sources: [], related: [], photo_slots: [], figures: [], plates: [], ...extra, body });
const mdEsc = s => String(s).replace(/([|*_`[\]])/g, '\\$1');

// Section 32 from data/regions/ when nobody authored it
const authored32 = pages.some(p => p.id.startsWith('32-') && !p.id.startsWith('32-00'));
if (!authored32 && Object.keys(regions).length) {
  const order = Object.keys(STATE_NAMES).sort((a, b) => STATE_NAMES[a].localeCompare(STATE_NAMES[b]));
  const classes = [['32-60-plates-deadly-plants-and-look-alikes', 'Plates: deadly plants and look-alikes', p => ['deadly', 'lookalike', 'caution'].includes(p.class)],
    ['32-61-plates-safe-starter-edibles', 'Plates: safe starter edibles', p => ['edible', 'medicinal'].includes(p.class)],
    ['32-62-plates-firewood-trees', 'Plates: firewood trees', p => p.class === 'firewood'],
    ['32-63-plates-other-plants', 'Plates: other plants', p => !['deadly', 'lookalike', 'caution', 'edible', 'medicinal', 'firewood'].includes(p.class)]];
  const plateRef = key => { const p = plates[key]; if (!p) return mdEsc(key.replace(/-/g, ' ')); const c = classes.find(x => x[2](p)); return `${mdEsc(p.common)} (→ ${c[0].slice(0, 5)})`; };
  order.forEach((code, i) => {
    const st = regions[code];
    if (!st) return;
    const id = `32-${String(i + 1).padStart(2, '0')}-${STATE_NAMES[code].toLowerCase().replace(/[^a-z]+/g, '-')}`;
    const counties = Object.entries(st.counties).sort((a, b) => a[0].localeCompare(b[0]));
    const val = (c, k) => { const v = c[k] ?? st.defaults[k]; return v === undefined || v === null || v === '' ? '' : mdEsc(v); };
    const top = c => Object.entries(c.hazards || st.defaults.hazards || {}).filter(([, r]) => r >= 3).map(([h]) => h.replace(/_/g, ' ')).join(', ');
    const nwr = new Map();
    for (const [name, c] of counties) for (const t of c.nwr || []) { const k = `${t.call}|${t.freq}`; if (!nwr.has(k)) nwr.set(k, { ...t, counties: [] }); nwr.get(k).counties.push(name.replace(/ County$/, '')); }
    const ecos = [...new Set(counties.map(([, c]) => c.ecoregion).filter(Boolean))].sort();
    const body = `# ${STATE_NAMES[code]}: region data

**What this page is for.** The facts that depend on where you are in ${STATE_NAMES[code]}: frost dates, cold and heat, hazards, weather radio, and the plants of each ecoregion. Your own county's values also fill the pages that use them (→ 17-00, → 25-01, → 25-03).

- State emergency management: ${st.state_em ? mdEsc(st.state_em) : '__________'}
- Poison Help line (national, any state): 1-800-222-1222

## Counties

| County | Zone | Last frost | First frost | Jan low °F | Jul high °F | Snow in | NWS office | High hazards |
|---|---|---|---|---|---|---|---|---|
${counties.map(([name, c]) => `| ${mdEsc(name)} | ${val(c, 'zone')} | ${val(c, 'last_frost')} | ${val(c, 'first_frost')} | ${val(c, 'jan_low_f')} | ${val(c, 'jul_high_f')} | ${val(c, 'snow_in')} | ${val(c, 'nws_office')} | ${mdEsc(top(c))} |`).join('\n')}

## NOAA Weather Radio transmitters

${nwr.size ? `| Call sign | Frequency (MHz) | SAME code | Counties |\n|---|---|---|---|\n${[...nwr.values()].map(t => `| ${mdEsc(t.call || '')} | ${mdEsc(t.freq || '')} | ${mdEsc(t.same || '')} | ${mdEsc(t.counties.slice(0, 12).join(', '))}${t.counties.length > 12 ? ' and others' : ''} |`).join('\n')}` : 'Not in this build of the region data.'}

## Plants by ecoregion

${ecos.length ? ecos.map(e => { const eco = ecoregions[e] || {}; return `### ${mdEsc(e)}\n\n- Deadly plants and look-alikes: ${(eco.plants?.deadly || []).map(plateRef).join(', ') || 'not listed yet'}\n- Safe starter edibles: ${(eco.plants?.edible || []).map(plateRef).join(', ') || 'not listed yet'}\n- Firewood trees: ${(eco.trees?.firewood || []).map(plateRef).join(', ') || 'not listed yet'}`; }).join('\n\n') : 'Not in this build of the region data.'}

> **SAFETY.** No wild plant or mushroom is eaten on a "test"; identification or nothing (→ 30-01).
`;
    gen.push(genPage(id, `${STATE_NAMES[code]}: region data`, body, { layer: 'generated', tags: ['region', `state-${code.toLowerCase()}`, STATE_NAMES[code].toLowerCase()], sources: (st.sources || []).filter(k => sources[k]) }));
  });
  for (const [id, title, test] of classes) {
    const keys = Object.entries(plates).filter(([, p]) => test(p)).sort((a, b) => a[1].common.localeCompare(b[1].common)).map(([k]) => k);
    if (!keys.length) continue;
    gen.push(genPage(id, title, `# ${title}\n\n**What this page is for.** Identification photographs for the whole country, so you can recognise these plants wherever you end up. Each state page lists which ones grow in its ecoregions.\n\n> **SAFETY.** No wild plant or mushroom is eaten on a "test"; identification or nothing (→ 30-01). A photograph helps you recognise a plant; certainty needs every feature in the description.\n\n{{plates}}\n`, { plates: keys, tags: ['plants', 'plates', 'foraging'], danger_level: id.startsWith('32-60') ? 'critical' : 'caution' }));
  }
}

const allPages = () => [...pages, ...gen];
const intro = n => {
  const list = allPages().filter(p => p.id.slice(0, 2) === n && !p.id.startsWith(`${n}-00`)).sort((a, b) => a.id.localeCompare(b.id));
  const purpose = p => {
    const m = /\*\*What this page is for\.?\*\*\s*([^\n]+(?:\n(?!\n)[^\n]+)*)/.exec(p.body || '');
    if (!m) return '';
    const first = m[1].replace(/\{\{[\s\S]*?\}\}/g, '').replace(/\s+/g, ' ').split(/(?<=[.!?])\s/)[0];
    return first.length > 160 ? first.slice(0, 157) + '…' : first;
  };
  return genPage(`${n}-00-section-intro`, `${sections[n]?.title || n}: section overview`, `# ${sections[n]?.title || n}

**What this section holds.** ${list.length} page${list.length === 1 ? '' : 's'} in this build. Pages marked FOR YOU matter most for your household and come first.

${list.map(p => `- → ${p.id.slice(0, 5)} **${mdEsc(p.title)}**${purpose(p) ? ': ' + purpose(p) : ''}`).join('\n') || 'No pages in this section yet.'}
`, { tags: ['section intro'] });
};

const pageSecs = [...new Set(allPages().map(p => p.id.slice(0, 2)))].sort();
for (const n of pageSecs) if (!have.has(`${n}-00`)) gen.push(intro(n));

if (!have.has('00-08')) {
  const secs = [...new Set([...pageSecs, '00'])].sort();
  gen.push(genPage('00-08-binder-map', 'Map of the binder', `# Map of the binder

**What this page is for.** Every section on one page, so you know where to look. In the app, the search box finds any word; on paper, the section number is on every page.

| Section | What is in it | Pages |
|---|---|---|
${secs.map(n => { const ps = allPages().filter(p => p.id.slice(0, 2) === n && !p.id.endsWith('-section-intro')); return `| → ${n}-00 | ${mdEsc(sections[n]?.title || n)}: ${mdEsc(ps.slice(0, 4).map(p => p.title).join('; '))}${ps.length > 4 ? '; and more' : ''} | ${ps.length} |`; }).join('\n')}
`, { tags: ['index', 'map'] }));
}

if (!have.has('00-03')) {
  const idx = new Map();
  for (const p of allPages()) for (const t of p.tags || []) {
    const k = String(t).toLowerCase().trim();
    if (!k || /^state-|^(sere|verbatim|reference|afh10-644|usaf|survival|section intro)$/.test(k)) continue;
    if (!idx.has(k)) idx.set(k, []);
    idx.get(k).push(p.id.slice(0, 5));
  }
  const rows = [...idx.entries()].filter(([, ids]) => ids.length <= 15).sort((a, b) => a[0].localeCompare(b[0]));
  gen.push(genPage('00-03-master-index', 'Master index', `# Master index

**What this page is for.** Topics from A to Z with the pages that cover them. In the app the search box is faster; this index is for paper.

${rows.map(([k, ids]) => `- **${mdEsc(k)}**: ${[...new Set(ids)].map(i => '→ ' + i).join(', ')}`).join('\n') || 'No topics yet.'}
`, { tags: ['index'] }));
}

if (!have.has('25-06')) {
  const citedKeys = Object.keys(sources).filter(k => sources[k].cited_by.length).sort((a, b) => (sources[a].org || '').localeCompare(sources[b].org || '') || sources[a].title.localeCompare(sources[b].title));
  gen.push(genPage('25-06-source-bibliography', 'Source bibliography', `# Source bibliography

**What this page is for.** Every document this binder cites, by publisher, title and date. There are no web addresses: in the Large download each document is bound behind the page that cites it; in the Small download it is cited here only.

| Publisher | Title | Date | Kind |
|---|---|---|---|
${citedKeys.map(k => { const s = sources[k]; return `| ${mdEsc(s.org || '')} | ${mdEsc(s.title)} | ${mdEsc(s.date || '')} | ${{ 'public-domain': 'public domain', open: 'open licence', restricted: 'copyrighted, private copy', blocked: 'copyrighted, private copy' }[s.licence_class] || ''} |`; }).join('\n')}
`, { tags: ['sources', 'bibliography'] }));
}

// ---- sizes -------------------------------------------------------------------------------------
const textBytes = allPages().reduce((n, p) => n + Buffer.byteLength(p.body || ''), 0);
const figBytes = Object.values(figures).reduce((n, f) => n + (f.svg ? f.svg.length : 0), 0);
const small = Math.round(textBytes * 1.35 + plateBytes * 1.34 + figBytes + 200e3);
const citedAll = Object.values(sources).filter(s => s.cited_by.length);
const shippedBytes = citedAll.reduce((n, s) => n + (s.bytes || 0), 0);
const fetched = citedAll.filter(s => !s.shipped).length;
const large = Math.round(small + shippedBytes * 1.34 + fetched * 1.5e6 * 1.34);

// ---- write -------------------------------------------------------------------------------------
const kit = {
  version: 1, built: TODAY,
  sections, pages: allPages().sort((a, b) => a.id.localeCompare(b.id)), cards, sources, regions, ecoregions, maps,
  plates, figures, ai_blocks,
  owner_tokens: readJson('scripts/owner-tokens.json', { words: [], patterns: [] }),
  notice_md: exists('NOTICE-TO-USERS.md') ? fs.readFileSync(path.join(ROOT, 'NOTICE-TO-USERS.md'), 'utf8') : '',
  sizes: { small_bytes: small, large_bytes: large,
    small: { min_mb: Math.max(1, Math.round(small * 0.9 / 1e6)), max_mb: Math.max(2, Math.round(small * 1.2 / 1e6)) },
    large: { min_mb: Math.round(large * 0.6 / 1e6), max_mb: Math.round(large * 1.3 / 1e6) }, note: `Large is an estimate: ${fetched} cited documents are fetched per household at about 1.5 MB each on average.` },
  warnings,
};
const check = JSON.stringify({ ...kit, maps: null, owner_tokens: null });
const leaks = check.match(URL_RE);
if (leaks) { console.error(`ERROR kit.json would contain ${leaks.length} URL(s), e.g. ${leaks[0]}`); process.exit(1); }
fs.writeFileSync(path.join(OUT, 'kit.json'), JSON.stringify(kit));
for (const w of warnings.slice(0, 30)) console.log('WARN  ' + w);
if (warnings.length > 30) console.log(`WARN  … and ${warnings.length - 30} more (kit.json .warnings)`);
console.log(`✓ ${rel(path.join(OUT, 'kit.json'))}: ${kit.pages.length} pages (${gen.length} generated), ${cards.length} cards, ${Object.keys(sources).length} sources, ${(fs.statSync(path.join(OUT, 'kit.json')).size / 1e6).toFixed(1)} MB; estimated binder Small ${(small / 1e6).toFixed(0)} MB, Large ${(large / 1e6).toFixed(0)} MB`);

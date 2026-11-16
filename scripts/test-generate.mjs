// test-generate.mjs — end-to-end test of the generator with the dry-run relay, then an offline
// browser smoke test of the binder file.
//
//   npm run test:generate            unit tests, build:kit, generate every tests/profiles/*.json
//                                    (Small; the first profile also Large and a reuse upgrade),
//                                    static checks, Playwright (Chromium, offline)
//   node scripts/test-generate.mjs --no-browser     skip Playwright
//
// Output: build/test-generate/<profile>-<size>.html. Exit code 1 on any failure.
// Works with partial content: checks adapt to whichever pages exist.

import fs from 'node:fs';
import path from 'node:path';
import url from 'node:url';
import { spawnSync } from 'node:child_process';
import { createRequire } from 'node:module';
import { generateBinder, mapPlan } from '../app/lib/generate.js';
import { createDryRunRelay } from '../app/lib/relay-dryrun.js';
import { buildContext } from '../app/lib/context.js';
const kitFor = new Map(); // profile → kit used (fixture runs use the fixture kit)

const ROOT = path.resolve(path.dirname(url.fileURLToPath(import.meta.url)), '..');
const OUT = path.join(ROOT, 'build', 'test-generate');
const noBrowser = process.argv.includes('--no-browser');
fs.mkdirSync(OUT, { recursive: true });

let failures = 0;
const ok = (cond, msg) => { if (cond) console.log('  ok   ' + msg); else { failures++; console.log('  FAIL ' + msg); } };

// ---- 1. unit tests and kit build ---------------------------------------------------------------
const unitFiles = fs.readdirSync(path.join(ROOT, 'tests/unit')).filter(f => f.endsWith('.test.mjs')).map(f => path.join('tests/unit', f));
const unit = spawnSync(process.execPath, ['--test', ...unitFiles], { cwd: ROOT, encoding: 'utf8' });
const summary = (unit.stdout.match(/^# (pass|fail) \d+$/gm) || []).join(', ');
console.log(`unit tests: ${summary}`);
ok(unit.status === 0, 'unit tests pass');
if (unit.status !== 0) console.log(unit.stdout.split('\n').filter(l => /not ok|Error|expected|actual/.test(l)).slice(0, 30).join('\n'));

const kb = spawnSync(process.execPath, ['scripts/build-kit.mjs'], { cwd: ROOT, encoding: 'utf8' });
console.log(kb.stdout.trim().split('\n').filter(l => !l.startsWith('WARN')).join('\n'));
ok(kb.status === 0, 'build:kit succeeds');
if (kb.status !== 0) { console.log(kb.stderr); process.exit(1); }
const kit = JSON.parse(fs.readFileSync(path.join(ROOT, 'app/build/kit.json'), 'utf8'));
const lite = JSON.parse(fs.readFileSync(path.join(ROOT, 'app/build/regions-lite.json'), 'utf8'));
ok(Object.keys(lite).length === 51, 'regions-lite has 50 states + DC');
ok(!/https?:\/\//.test(JSON.stringify({ ...kit, maps: null })), 'kit.json carries no URL (outside maps)');

const loadAsset = async p => { try { return new Uint8Array(fs.readFileSync(path.join(ROOT, 'app/build', p))); } catch { return null; } };

// ---- 2. static checks on a binder file ---------------------------------------------------------
const EXT_URL = /https?:\/\/|\bwww\.[a-z0-9-]+\.[a-z]|\/\/[a-z0-9-]+\.[a-z]{2,}\//i;
function staticChecks(name, html, report, profile) {
  ok(!EXT_URL.test(html), `${name}: no external URL anywhere in the file`);
  const badRefs = [...html.matchAll(/\s(?:src|href|action|poster|data)=["']?([^"'\s>]+)/gi)].map(m => m[1]).filter(v => !/^(#|data:|blob:)/.test(v));
  ok(badRefs.length === 0, `${name}: every src/href is in-file (#…, data:) ${badRefs.slice(0, 3).join(' ')}`);
  const articles = [...html.matchAll(/<article [^>]*id="([^"]+)"/g)].map(m => m[1]);
  ok(articles.length === report.pages && articles.length > 20, `${name}: ${articles.length} pages in the static body`);
  ok(articles[0]?.startsWith('00-05') && articles[1]?.startsWith('00-09'), `${name}: page one is the disclaimer, page two the private-copy notice (${articles[0]}, ${articles[1]})`);
  const second = html.slice(html.indexOf(`id="${articles[1]}"`), html.indexOf('</article>', html.indexOf(`id="${articles[1]}"`)));
  ok(/private/i.test(second) && /shar/i.test(second), `${name}: page two tells the household the copy is private and not for sharing`);
  const stamps = (html.match(/AI-reviewed, not human-verified\.<\/strong>/g) || []).length;
  ok(stamps === articles.length, `${name}: AI-reviewed stamp on every page (${stamps}/${articles.length})`);
  ok(articles.includes('25-11-review-notes') && articles.includes('25-12-sources-not-captured'), `${name}: Review notes and Sources not captured pages present`);
  ok(!/\{\{|GPAIBLOCK/.test(html.replace(/<script[\s\S]*?<\/script>/g, '')), `${name}: no unfilled template syntax`);
  const tokens = JSON.parse(fs.readFileSync(path.join(ROOT, 'scripts/owner-tokens.json'), 'utf8'));
  // Exempt: Section 31 (verbatim handbook), Section 32 (national region appendix: public place
  // names such as towns and ecoregions), generated pages and citation lists (publisher titles).
  // Every other section is still checked.
  const body = html.replace(/<article [^>]*id="(31-|32-|25-06|25-11|25-12)[\s\S]*?<\/article>/g, '').replace(/<aside class="cites">[\s\S]*?<\/aside>/g, '')
    .replace(/<section class="srcdoc"[\s\S]*?<\/section>/g, '').replace(/<script[\s\S]*?<\/script>/g, '');
  // the household's own answers and its own home/destination region values are allowed
  const own = buildContext(profile, kitFor.get(profile) || kit);
  const prof = (JSON.stringify(profile) + JSON.stringify([own.region.home, ...own.destinations.map(d => d.region)])).toLowerCase();
  const leaked = tokens.words.filter(w => new RegExp(`(^|[^A-Za-z0-9])${w.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}([^A-Za-z0-9]|$)`).test(body) && !prof.includes(w.toLowerCase()));
  ok(leaked.length === 0, `${name}: no owner-household token outside Section 31 ${leaked.join(', ')}`);
  ok(/<nav id="tocwrap">/.test(html) && /<details class="sec"/.test(html), `${name}: static contents for readers without JavaScript`);
}

// ---- 3. generate ------------------------------------------------------------------------------
const profiles = fs.readdirSync(path.join(ROOT, 'tests/profiles')).filter(f => f.endsWith('.json')).sort();
ok(profiles.length >= 3, `${profiles.length} test profiles`);
const outputs = [];
for (const [i, f] of profiles.entries()) {
  const profile = JSON.parse(fs.readFileSync(path.join(ROOT, 'tests/profiles', f), 'utf8'));
  const name = f.replace(/\.json$/, '');
  const relay = createDryRunRelay({ flaky: i === 0 });
  const phases = new Set();
  const t0 = Date.now();
  const blob = await generateBinder(profile, kit, { relay, size: 'small', loadAsset, onProgress: p => phases.add(p.phase), now: new Date('2026-11-16T12:00:00Z') });
  const html = await blob.text();
  const file = path.join(OUT, `${name}-small.html`);
  fs.writeFileSync(file, html);
  const r = blob.report;
  console.log(`\n${name} (Small): ${r.pages} pages, ${(r.bytes / 1e6).toFixed(2)} MB, ${r.aiBlocks} ai blocks, ${r.modelCalls} model calls, ${r.findings.length} review findings, ${Date.now() - t0} ms`);
  ok(phases.has('render') && phases.has('done'), `${name}: progress reported (${[...phases].join(', ')})`);
  ok(relay.calls.requests.every(q => q.model === 'claude-opus-5-5' && q.stream === true && !('temperature' in q)), `${name}: every request is claude-opus-5-5, streamed, no sampling params`);
  ok(relay.calls.requests.every(q => q.system?.[0]?.cache_control?.type === 'ephemeral'), `${name}: stable system prompt marked for caching`);
  ok(relay.calls.requests.filter(q => q.output_config?.format).every(q => q.output_config.format.type === 'json_schema'), `${name}: review passes use structured outputs`);
  staticChecks(name, html, r, profile);
  outputs.push({ name, file, profile, html });

  if (i === 0) {
    // Large, then an upgrade from the Small file (no new model calls) and a cancel
    const citedKeys = [...new Set(kit.pages.flatMap(p => p.sources || []))].filter(k => kit.sources[k] && !kit.sources[k].shipped);
    const relayL = createDryRunRelay({ blocked: new Set(citedKeys.filter(k => kit.sources[k].licence_class === 'blocked').concat(citedKeys).slice(0, 2)) });
    const big = await generateBinder(profile, kit, { relay: relayL, size: 'large', loadAsset, now: new Date('2026-11-16T12:00:00Z') });
    const bigHtml = await big.text();
    fs.writeFileSync(path.join(OUT, `${name}-large.html`), bigHtml);
    console.log(`${name} (Large): ${(big.report.bytes / 1e6).toFixed(2)} MB, ${big.report.sources.bound} sources bound, ${big.report.sources.missing} not captured`);
    ok(big.report.sources.bound > 0 && /<section class="srcdoc"/.test(bigHtml), `${name}: Large binds sources behind the citing sections`);
    ok(big.report.sources.missing >= 1 && /refused automated download/.test(bigHtml), `${name}: refused sources listed on Sources not captured`);
    staticChecks(`${name} (Large)`, bigHtml, big.report, profile);
    const relayU = createDryRunRelay();
    const up = await generateBinder(profile, kit, { relay: relayU, size: 'large', loadAsset, previous: html, now: new Date('2026-11-16T12:00:00Z') });
    ok(up.report.modelCalls === 0, `${name}: Small → Large upgrade from the saved file makes no model calls (${up.report.modelCalls})`);
    const ac = new AbortController();
    const p = generateBinder(profile, kit, { relay: createDryRunRelay(), size: 'small', loadAsset, signal: ac.signal, onProgress: e => { if (e.phase === 'render') ac.abort(); } });
    let aborted = false; try { await p; } catch (e) { aborted = e.name === 'AbortError'; }
    ok(aborted, `${name}: cancel stops generation`);
  }
}

// ---- 3b. region data, plates, figures and maps from fixtures (D1/D2 formats, notes/workers/A3.md)
{
  const fxOut = path.join(OUT, 'kit-fixture');
  const fb = spawnSync(process.execPath, ['scripts/build-kit.mjs'], { cwd: ROOT, encoding: 'utf8', env: { ...process.env, GP_DATA_ROOT: 'tests/fixtures', GP_KIT_OUT: fxOut } });
  ok(fb.status === 0, 'fixture kit builds from tests/fixtures (regions, plates, figures)');
  const fkit = JSON.parse(fs.readFileSync(path.join(fxOut, 'kit.json'), 'utf8'));
  // state pages may be authored (content/) or generated from data/regions/; plate pages are always generated
  ok(fkit.pages.some(p => p.id.startsWith('32-42-')) && fkit.pages.some(p => p.id.startsWith('32-28-')), 'fixture: Section 32 state pages present (authored or generated)');
  ok(fkit.pages.some(p => p.id.startsWith('32-60-') && (p.plates || []).includes('test-hemlock')), 'fixture: national plate page generated with every plate');
  ok(!/never-copied|xmlns|<script|onload/.test(JSON.stringify(fkit.plates) + fkit.figures['fig-fixture'].svg), 'fixture: plate URLs dropped, SVG sanitised');
  const fxLite = JSON.parse(fs.readFileSync(path.join(fxOut, 'regions-lite.json'), 'utf8'));
  ok(fxLite.SD.counties.includes('Beadle County'), 'fixture: regions-lite lists counties');
  const profile = JSON.parse(fs.readFileSync(path.join(ROOT, 'tests/profiles/sd-rural-farm-infant-well.json'), 'utf8'));
  const relay = createDryRunRelay();
  const plan = mapPlan(profile, fkit);
  ok(plan.base.count === 2 && plan.route.count >= 1 && plan.route.max_mb > 0, `fixture: map plan home+destination ${plan.base.count}, route counties ${plan.route.count} (${plan.route.min_mb}-${plan.route.max_mb} MB, opt-in)`);
  kitFor.set(profile, fkit);
  const fx = await generateBinder(profile, fkit, { relay, size: 'large', routeMaps: true, loadAsset: async p => { try { return new Uint8Array(fs.readFileSync(path.join(fxOut, p))); } catch { return null; } } });
  const fhtml = await fx.text();
  fs.writeFileSync(path.join(OUT, 'fixture-sd-large.html'), fhtml);
  const meta = JSON.parse(/<script type="application\/json" id="gp-meta">([\s\S]*?)<\/script>/.exec(fhtml)[1].replace(/\\u003c/g, '<'));
  ok(meta.home_state === 'SD' && meta.pages.find(p => p.id === '32-42-south-dakota')?.pr, 'fixture: home state region page promoted');
  ok(meta.pages.find(p => p.id === '32-28-nebraska')?.pr, 'fixture: destination state region page promoted');
  const plateRules = (fhtml.match(/\.pl[a-z0-9]+\{background-image:url\(data:image\/jpeg;base64,/g) || []).length;
  ok(plateRules === 2, `fixture: each plate image stored once as CSS (${plateRules} rules for 2 images)`);
  ok(/\b4q\b/.test(fhtml), 'fixture: region values (home zone 4q) reach the pages');
  ok(/Plates for your home area \(Fixture Plains\)/.test(fhtml) && /aria-label="Test hemlock/.test(fhtml), 'fixture: {{plates}} with empty plates: shows the home ecoregion plates');
  ok(relay.calls.map >= 3 && /on the way to Grandparents/.test(fhtml), `fixture: topo maps requested for home, destination and route counties (${relay.calls.map} map calls)`);
  staticChecks('fixture-sd (Large)', fhtml, fx.report, profile);
  outputs.push({ name: 'fixture-sd', file: path.join(OUT, 'fixture-sd-large.html'), profile, html: fhtml });
}

// ---- 4. browser smoke test ---------------------------------------------------------------------
if (!noBrowser) {
  let chromium;
  try { chromium = createRequire(import.meta.url)('playwright').chromium; }
  catch { try { chromium = createRequire('/opt/node22/lib/node_modules/')('playwright').chromium; } catch {} }
  if (!chromium) { ok(false, 'playwright is available'); }
  else {
    const browser = await chromium.launch();
    try {
      await browserGenerate(browser);
      for (const { name, file, html } of outputs) await browserChecks(browser, name, file, html);
      await noJsChecks(browser, outputs[0]);
    } finally { await browser.close(); }
  }
}

async function browserChecks(browser, name, file, html) {
  console.log(`\nbrowser: ${name}`);
  const context = await browser.newContext({ offline: true, viewport: { width: 375, height: 760 }, acceptDownloads: true });
  const external = [];
  await context.route('**/*', route => { const u = route.request().url(); if (u.startsWith('file:') || u.startsWith('data:') || u.startsWith('blob:')) route.continue(); else { external.push(u); route.abort(); } });
  const page = await context.newPage();
  const errors = [];
  page.on('pageerror', e => errors.push(e.message));
  await page.goto(url.pathToFileURL(file).href);
  await page.waitForFunction(() => document.body.classList.contains('app'));
  ok(await page.isHidden('#err') || !(await page.textContent('#err')), `${name}: app started without errors`);
  ok(await page.locator('.qrow .card').count() > 0, `${name}: emergency row on the home screen`);

  // search
  await page.fill('#q', 'water');
  await page.waitForSelector('#view .card');
  const hits = await page.locator('#view a.card').count();
  ok(hits > 0, `${name}: search "water" finds ${hits} page(s)`);
  await page.locator('#view a.card').first().click();
  await page.waitForSelector('article.page.active');
  ok(true, `${name}: search result opens a page`);
  await page.fill('#q', '');

  // cross-reference
  const xref = await page.evaluate(() => { const a = document.querySelector('article.page a.xref'); return a ? { href: a.getAttribute('href'), from: a.closest('article').id } : null; });
  if (xref) {
    await page.evaluate(id => { location.hash = '#' + id; }, xref.from);
    await page.waitForSelector(`article[id="${xref.from}"].active`);
    await page.locator(`article[id="${xref.from}"] a.xref[href="${xref.href}"]`).first().click();
    await page.waitForSelector(`[id="${xref.href.slice(1)}"].active`);
    ok(true, `${name}: cross-reference ${xref.from.slice(0, 5)} ${xref.href} opens its target`);
    await page.click('#back');
    await page.waitForSelector(`article[id="${xref.from}"].active`);
    ok(true, `${name}: back returns to the page`);
  } else ok(false, `${name}: a cross-reference exists to test`);

  // the notice on page two
  const second = await page.evaluate(() => document.querySelectorAll('article.page')[1].id);
  await page.evaluate(id => { location.hash = '#' + id; }, second);
  await page.waitForSelector(`article[id="${second}"].active`);
  ok(/private/i.test(await page.textContent(`article[id="${second}"]`)), `${name}: notice page (${second}) readable in the app`);

  // pickers
  await page.evaluate(() => { location.hash = '#s/02'; });
  await page.waitForSelector('#view h1');
  ok(await page.locator('#condpick').count() === 1, `${name}: Section 02 condition picker`);
  await page.evaluate(() => { location.hash = '#s/32'; });
  await page.waitForSelector('#view h1');
  ok(await page.locator('#statepick').count() === 1 || /No state region pages/.test(await page.textContent('#view')), `${name}: Section 32 region picker (or its empty state)`);

  // photo slot: attach, shared across pages, save a new copy
  const slot = await page.evaluate(() => { const f = document.querySelector('figure.photo'); return f ? { id: f.getAttribute('data-slot'), page: f.closest('article').id } : null; });
  if (slot) {
    await page.evaluate(p => { location.hash = '#' + p; }, slot.page);
    await page.waitForSelector(`article[id="${slot.page}"].active`);
    const png = Buffer.from('iVBORw0KGgoAAAANSUhEUgAAAAIAAAACCAIAAAD91JpzAAAAFklEQVR4nGP4z8DAwMDAxMDAwMDAAAANHQEDK+mmyAAAAABJRU5ErkJggg==', 'base64');
    await page.locator(`article[id="${slot.page}"] figure.photo[data-slot="${slot.id}"] input[type=file]`).first().setInputFiles({ name: 'p.png', mimeType: 'image/png', buffer: png });
    await page.waitForFunction(() => document.body.classList.contains('dirty'));
    const shown = await page.evaluate(id => [...document.querySelectorAll(`.ph-${id}`)].every(el => getComputedStyle(el).display === 'block'), slot.id);
    ok(shown, `${name}: photo "${slot.id}" shows on every page that has the slot`);
    const [dl] = await Promise.all([page.waitForEvent('download'), page.click('#savecopy')]);
    const saved = fs.readFileSync(await dl.path(), 'utf8');
    const photoCss = (/<style id="gp-photos">([\s\S]*?)<\/style>/.exec(saved) || [])[1] || '';
    ok(photoCss.includes(`.ph-${slot.id}{display:block`) && (photoCss.match(/data:image\/jpeg;base64/g) || []).length === 1 && (saved.match(/data:image\/jpeg;base64/g) || []).length === (html.match(/data:image\/jpeg;base64/g) || []).length + 1, `${name}: "Save a new copy" writes the photo into the file once`);
    ok(!EXT_URL.test(saved) && !/class="[^"]*\bactive\b/.test(saved) && !/<body class="[^"]+"/.test(saved), `${name}: saved copy is clean (no URL, no app state)`);
    fs.writeFileSync(path.join(OUT, `${name}-saved-copy.html`), saved);
  } else console.log(`  skip ${name}: no photo slot in this build`);

  // print / PDF export: every page and bound source visible
  await page.emulateMedia({ media: 'print' });
  const hiddenInPrint = await page.evaluate(() => [...document.querySelectorAll('article.page, section.srcdoc')].filter(a => getComputedStyle(a).display === 'none').length);
  ok(hiddenInPrint === 0, `${name}: print CSS shows every page (${hiddenInPrint} hidden)`);
  await page.emulateMedia({ media: 'screen' });

  ok(external.length === 0, `${name}: no network request attempted (${external.slice(0, 2).join(' ')})`);
  ok(errors.length === 0, `${name}: no script errors ${errors.slice(0, 2).join(' | ')}`);
  await context.close();
}

// Large generated in a real browser (the way the settings page runs it): PDF sources are rendered
// to page images by the vendored pdf.js, so the binder shows and prints them with no PDF viewer.
async function browserGenerate(browser) {
  console.log('\nbrowser: generate Large in the page (pdf.js rendering)');
  const http = await import('node:http');
  const TYPES = { '.js': 'text/javascript', '.mjs': 'text/javascript', '.json': 'application/json', '.html': 'text/html', '.jpg': 'image/jpeg', '.pfb': 'application/octet-stream', '.ttf': 'font/ttf' };
  const server = http.createServer((req, res) => {
    const u = decodeURIComponent(new URL(req.url, 'http://x').pathname);
    if (u === '/__blank') { res.writeHead(200, { 'content-type': 'text/html' }); return res.end('<!doctype html><title>t</title>'); }
    const f = path.join(ROOT, u);
    if (!f.startsWith(ROOT) || !fs.existsSync(f) || fs.statSync(f).isDirectory()) { res.writeHead(404); return res.end(); }
    res.writeHead(200, { 'content-type': TYPES[path.extname(f)] || 'application/octet-stream' });
    fs.createReadStream(f).pipe(res);
  });
  await new Promise(r => server.listen(0, '127.0.0.1', r));
  const base = `http://127.0.0.1:${server.address().port}`;
  const page = await browser.newPage();
  const errors = [];
  page.on('pageerror', e => errors.push(e.message));
  try {
    await page.goto(base + '/__blank');
    const profile = JSON.parse(fs.readFileSync(path.join(ROOT, 'tests/profiles/sd-rural-farm-infant-well.json'), 'utf8'));
    const kitRel = '/' + path.relative(ROOT, path.join(OUT, 'kit-fixture')).split(path.sep).join('/') + '/';
    const r = await page.evaluate(async ({ profile, kitRel }) => {
      const { generateBinder } = await import('/app/lib/generate.js');
      const { createDryRunRelay } = await import('/app/lib/relay-dryrun.js');
      const kit = await (await fetch(kitRel + 'kit.json')).json();
      const cited = [...new Set(kit.pages.flatMap(p => p.sources || []))].filter(k => kit.sources[k] && !kit.sources[k].shipped).slice(0, 2);
      const relay = createDryRunRelay({ pdfKeys: new Set(cited) });
      const blob = await generateBinder(profile, kit, { relay, size: 'large', assetBase: kitRel });
      const html = await blob.text();
      return { rendered: blob.report.sources.rendered || 0, imgs: (html.match(/<img class="pdfpage"/g) || []).length, buttons: (html.match(/data-open-pdf=/g) || []).length, bytes: blob.size, html };
    }, { profile, kitRel });
    ok(r.rendered === 2 && r.imgs === 2 && r.buttons === 0, `browser Large: 2 PDF sources rendered to page images (${r.rendered} rendered, ${r.imgs} images, ${r.buttons} open buttons)`);
    const file = path.join(OUT, 'browser-generated-large.html');
    fs.writeFileSync(file, r.html);
    ok(!EXT_URL.test(r.html), 'browser Large: no external URL');
    ok(errors.length === 0, `browser Large: no script errors ${errors.slice(0, 2).join(' | ')}`);
  } finally { await page.close(); server.close(); }
}

async function noJsChecks(browser, { name, file }) {
  const context = await browser.newContext({ javaScriptEnabled: false, offline: true });
  const page = await context.newPage();
  await page.goto(url.pathToFileURL(file).href);
  ok(await page.isVisible('#tocwrap') && await page.isVisible('#modebar'), `${name} without JavaScript: contents and reading-mode note visible`);
  const visible = await page.evaluate(() => [...document.querySelectorAll('article.page')].filter(a => getComputedStyle(a).display !== 'none').length);
  ok(visible > 20, `${name} without JavaScript: all ${visible} pages readable in the static body`);
  await context.close();
}

console.log(failures ? `\n${failures} check(s) FAILED` : '\nall checks passed');
process.exit(failures ? 1 : 0);

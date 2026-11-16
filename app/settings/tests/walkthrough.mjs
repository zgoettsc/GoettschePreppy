// End-to-end check of the settings page with Playwright (Chromium is preinstalled; no install).
//
//   node app/settings/tests/walkthrough.mjs
//
// Serves the repository on a random local port, mocks the relay's /api/v1/check, and:
//   A. with app/build/* and app/lib/generate.js absent (as today): walks steps 0 to 8 with a test
//      household, checks errors, notices, 375 px layout and tap targets, saves profile.json and
//      validates it with ajv against schema/profile.schema.json, generates with the stub, cancels,
//      reloads, loads the file back and compares, and checks the opt-in browser storage.
//   B. with kit.json, regions-lite.json and generate.js supplied by route mocks: county pickers
//      become lists, cards come from the kit, and generateBinder receives the documented arguments.
// Screenshots at 375 px go to build/settings-shots/.

import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import assert from 'node:assert/strict';
import { fileURLToPath } from 'node:url';
import { createRequire } from 'node:module';
import Ajv2020Mod from 'ajv/dist/2020.js';

const require = createRequire(import.meta.url);
let playwright;
try { playwright = require('playwright'); } catch { playwright = require('/opt/node-tools/node_modules/playwright'); }
const { chromium } = playwright;

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../../..');
const SHOTS = path.join(ROOT, 'build', 'settings-shots');
const OUT = path.join(ROOT, 'build', 'settings-test');
fs.mkdirSync(SHOTS, { recursive: true });
fs.mkdirSync(OUT, { recursive: true });

const Ajv2020 = Ajv2020Mod.default || Ajv2020Mod;
const schema = JSON.parse(fs.readFileSync(path.join(ROOT, 'schema/profile.schema.json'), 'utf8'));
const validateProfile = new Ajv2020({ allErrors: true, strict: false }).compile(schema);

const GOOD_KEY = 'test-key-1234567890';
const TYPES = { '.html': 'text/html', '.js': 'text/javascript', '.mjs': 'text/javascript', '.css': 'text/css', '.json': 'application/json' };

function serve() {
  return new Promise(resolve => {
    const srv = http.createServer((req, res) => {
      const u = decodeURIComponent(req.url.split('?')[0]);
      let f = path.join(ROOT, u);
      if (u.endsWith('/')) f = path.join(f, 'index.html');
      if (!f.startsWith(ROOT) || !fs.existsSync(f) || fs.statSync(f).isDirectory()) { res.writeHead(404); res.end('not found'); return; }
      res.writeHead(200, { 'content-type': TYPES[path.extname(f)] || 'application/octet-stream' });
      fs.createReadStream(f).pipe(res);
    }).listen(0, '127.0.0.1', () => resolve(srv));
  });
}

let failures = 0;
async function step(name, fn) {
  try { await fn(); console.log('  ok  ', name); } catch (e) { failures++; console.log('  FAIL', name, '\n      ', e.message.split('\n').slice(0, 6).join('\n        ')); }
}

const sel = {
  input: (p) => `#f-${p}`,
  radio: (p, v) => `input[name="f-${p}"][value="${v}"]`,
  check: (p, v) => (v === undefined ? `#f-${p}` : `input[id^="f-${p}"][value="${v}"]`),
};

async function shot(page, name) {
  await page.screenshot({ path: path.join(SHOTS, `${name}.png`), fullPage: true });
}
async function layoutChecks(page, label) {
  const r = await page.evaluate(() => {
    const vw = document.documentElement.clientWidth;
    const overflow = document.documentElement.scrollWidth - vw;
    const small = [];
    for (const el of document.querySelectorAll('.btn, .choice, input[type=text], input[type=password], input[type=tel], select, textarea, summary')) {
      const b = el.getBoundingClientRect();
      if (b.width === 0 && b.height === 0) continue; // not rendered (collapsed details)
      if (b.height < 43.5) small.push(`${el.tagName}.${el.className}#${el.id} h=${b.height.toFixed(0)}`);
    }
    const wide = [...document.querySelectorAll('main *')].filter(el => el.getBoundingClientRect().right > vw + 1).map(el => `${el.tagName}.${el.className}#${el.id}`).slice(0, 5);
    const notice = document.querySelector('.never-stored');
    return { overflow, small: small.slice(0, 5), wide, notice: !!notice && notice.getBoundingClientRect().height > 0 && /never stored/.test(notice.textContent) };
  });
  assert.ok(r.overflow <= 0, `${label}: horizontal overflow ${r.overflow}px: ${r.wide.join(', ')}`);
  assert.deepEqual(r.small, [], `${label}: tap targets under 44px`);
  assert.ok(r.notice, `${label}: never-stored notice not visible`);
}
async function next(page) {
  await page.click('#next-btn');
  await page.waitForFunction(() => document.activeElement && document.activeElement.id === 'step-title');
}
async function saveProfile(page, file) {
  const [dl] = await Promise.all([page.waitForEvent('download'), page.click('#final-save-btn')]);
  await dl.saveAs(file);
  return JSON.parse(fs.readFileSync(file, 'utf8'));
}

async function mockRelay(context, calls) {
  await context.route('**/api/v1/check', async (route) => {
    const body = JSON.parse(route.request().postData() || '{}');
    calls.push(body);
    if (body.access_key === GOOD_KEY) await route.fulfill({ status: 200, contentType: 'application/json', body: JSON.stringify({ ok: true, label: 'Test friend' }) });
    else await route.fulfill({ status: 401, contentType: 'application/json', body: '{"ok":false}' });
  });
}

// ---------------------------------------------------------------------------------------------
async function scenarioA(browser, base) {
  console.log('Scenario A: kit not built yet (fixtures, free-text county, stub generator)');
  const context = await browser.newContext({ viewport: { width: 375, height: 812 }, acceptDownloads: true, colorScheme: 'dark' });
  const relayCalls = [];
  await mockRelay(context, relayCalls);
  const page = await context.newPage();
  const pageErrors = [];
  page.on('pageerror', e => pageErrors.push(e.message));
  page.on('dialog', d => d.accept());
  await page.goto(base);
  await page.waitForSelector('#step-title');

  await step('keyboard: first Tab reaches the skip link', async () => {
    await page.keyboard.press('Tab');
    assert.equal(await page.evaluate(() => document.activeElement.className), 'skip');
  });

  await step('step 0: Next with nothing filled shows plain-words errors', async () => {
    await page.click('#next-btn');
    await page.waitForSelector('.err-summary');
    const txt = await page.textContent('.err-summary');
    assert.match(txt, /need a look/);
    assert.match(await page.textContent('#f-access-access_key-err'), /Please answer this one/);
    assert.equal(await page.textContent('#step-title'), 'Access and privacy');
    await shot(page, '00-access-errors');
  });

  await step('step 0: wrong key rejected, right key accepted via POST /api/v1/check', async () => {
    await page.fill(sel.input('access-access_key'), 'wrong-key-000000');
    await page.click('#check-key-btn');
    await page.waitForFunction(() => /not accepted/.test(document.querySelector('#key-status').textContent));
    await page.fill(sel.input('access-access_key'), GOOD_KEY);
    await page.click('#check-key-btn');
    await page.waitForFunction(() => /Key accepted \(Test friend\)/.test(document.querySelector('#key-status').textContent));
    assert.deepEqual(relayCalls.at(-1), { access_key: GOOD_KEY });
  });

  await step('step 0: notice, private-copy notice, keep toggle defaults off', async () => {
    await page.check(sel.check('access-acknowledged_notice'));
    await page.check(sel.check('access-save_profile_locally'));
    assert.equal(await page.isChecked('#keep-toggle'), false);
    assert.ok(await page.isVisible('.notice.private-copy'));
    assert.equal(await page.evaluate(() => localStorage.length), 0);
    await layoutChecks(page, 'step 0');
    await shot(page, '00-access');
    await next(page);
  });

  await step('step 1: home base (free-text county with warning)', async () => {
    assert.equal(await page.textContent('#step-title'), 'Home base');
    await page.selectOption(sel.input('home-state'), 'SD');
    assert.match(await page.textContent('.q .warn'), /type the county name/);
    await page.fill(sel.input('home-county'), 'Minnehaha County');
    await page.fill(sel.input('home-nearest_town'), 'Testville');
    await page.check(sel.radio('home-setting', 'suburban'));
    await page.selectOption(sel.input('home-elevation_band'), 'low');
    assert.ok(await page.isVisible('.notice-more'), 'collapsed second paragraph');
    await layoutChecks(page, 'step 1');
    await shot(page, '01-home');
    await next(page);
  });

  await step('step 2: dwelling, with follow-up questions and a vehicle', async () => {
    await page.check(sel.radio('dwelling-dwelling_type', 'detached-house'));
    await page.fill(sel.input('dwelling-stories'), '2');
    await page.selectOption(sel.input('dwelling-basement'), 'full');
    await page.check(sel.radio('dwelling-windowless_interior_room-present', 'true'));
    await page.fill(sel.input('dwelling-windowless_interior_room-which'), 'Downstairs bathroom');
    await page.check(sel.radio('dwelling-water_supply', 'private-well'));
    await page.check(sel.radio('dwelling-sewer', 'septic'));
    await page.selectOption(sel.input('dwelling-primary_heat'), 'propane-furnace');
    await page.selectOption(sel.input('dwelling-gas_service-kind'), 'propane-tank');
    await page.fill(sel.input('dwelling-gas_service-tank_gallons'), '500');
    await page.selectOption(sel.input('dwelling-cooking_fuel'), 'propane');
    await page.selectOption(sel.input('dwelling-water_heater-kind'), 'tank-gas');
    await page.fill(sel.input('dwelling-water_heater-gallons'), '50');
    await page.check(sel.check('dwelling-fire_features', 'wood-stove'));
    await page.check(sel.check('dwelling-fire_features', 'fire-pit'));
    await page.selectOption(sel.input('dwelling-pool_or_hot_tub-kind'), 'none');
    await page.selectOption(sel.input('dwelling-garden_space'), 'large-yard');
    await page.check(sel.radio('dwelling-attached_garage', 'true'));
    await page.click('#f-dwelling-vehicles-add');
    await page.selectOption(sel.input('dwelling-vehicles-0-type'), 'pickup');
    await page.selectOption(sel.input('dwelling-vehicles-0-fuel'), 'diesel');
    await page.check(sel.check('dwelling-vehicles-0-four_wheel_drive'));
    await page.check(sel.check('dwelling-vehicles-0-can_tow'));
    await page.selectOption(sel.input('dwelling-trailer'), 'open-utility');
    await layoutChecks(page, 'step 2');
    await shot(page, '02-dwelling');
    await next(page);
  });

  await step('step 3: members, conditions, medicines, allergies, add and remove', async () => {
    await page.fill(sel.input('members-0-label'), 'Alex');
    await page.check(sel.radio('members-0-role', 'adult'));
    await page.fill(sel.input('members-0-age-value'), '41');
    await page.fill(sel.input('members-0-weight-value'), '180');
    await page.selectOption(sel.input('members-0-sex'), 'male');
    assert.equal(await page.$(sel.input('members-0-pregnant_or_nursing')), null, 'pregnancy hidden for male');
    await page.click('.item details.more > summary');
    const names = await page.$$eval('input[id^="f-members-0-conditions"]', els => els.map(e => e.closest('label').textContent));
    assert.equal(names.length, 26);
    assert.match(names[0], /Type 1 diabetes/);
    await page.check(sel.check('members-0-conditions', 'CL-09'));
    await page.click('#f-members-0-medications-add');
    await page.fill(sel.input('members-0-medications-0-name'), 'Lisinopril');
    await page.fill(sel.input('members-0-medications-0-strength'), '10 mg');
    await page.fill(sel.input('members-0-medications-0-schedule'), 'once a day');
    await page.check(sel.radio('members-0-medications-0-refrigerated', 'false'));
    await page.fill(sel.input('members-0-medications-0-if_missed'), 'Blood pressure rises over days; call the doctor.');
    await page.click('#f-members-0-allergies-add');
    await page.fill(sel.input('members-0-allergies-0-allergen'), 'Penicillin');
    await page.check(sel.radio('members-0-allergies-0-severity', 'severe'));
    await page.check(sel.check('members-0-skills', 'ham-licence'));
    await page.fill(sel.input('members-0-ham_callsign'), 'KD0ABC');

    await page.click('#f-members-add');
    await page.fill(sel.input('members-1-label'), 'Sam');
    await page.check(sel.radio('members-1-role', 'child'));
    await page.fill(sel.input('members-1-age-value'), '7');
    await page.fill(sel.input('members-1-weight-value'), '50');
    await page.selectOption(sel.input('members-1-sex'), 'female');
    assert.equal(await page.$(sel.input('members-1-pregnant_or_nursing')), null, 'pregnancy hidden for a child');
    await page.locator('.item').nth(1).locator('details.more > summary').first().click();
    await page.check(sel.check('members-1-conditions', 'CL-03'));
    await page.check(sel.check('members-1-conditions', 'CL-04'));
    await page.click('#f-members-1-allergies-add');
    await page.fill(sel.input('members-1-allergies-0-allergen'), 'Peanuts');
    await page.check(sel.radio('members-1-allergies-0-severity', 'anaphylaxis'));
    await page.check(sel.radio('members-1-allergies-0-carries_epinephrine', 'true'));
    await page.check(sel.check('members-1-mobility_or_sensory', 'glasses-contacts'));

    await page.click('#f-members-add');
    assert.equal(await page.$$eval('section.item[aria-labelledby$="-head"]', els => els.filter(e => /^f-members-\d+-head$/.test(e.getAttribute('aria-labelledby'))).length), 3);
    await page.click('button[aria-label="Remove person 3"]');
    assert.equal(await page.$(sel.input('members-2-label')), null, 'third person removed');
    await layoutChecks(page, 'step 3');
    await shot(page, '03-members');
    await next(page);
  });

  await step('step 4: pets and livestock', async () => {
    await page.click('#f-pets-add');
    await page.selectOption(sel.input('pets-0-type'), 'dog');
    await page.fill(sel.input('pets-0-count'), '2');
    await page.fill(sel.input('pets-0-food_per_day'), '2 cups dry food');
    await page.click('#f-livestock-add');
    await page.selectOption(sel.input('livestock-0-type'), 'chickens');
    await page.fill(sel.input('livestock-0-count'), '6');
    await layoutChecks(page, 'step 4');
    await shot(page, '04-animals');
    await next(page);
  });

  await step('step 5: a destination', async () => {
    await page.click('#f-destinations-add');
    await page.fill(sel.input('destinations-0-name'), "Grandma's farm");
    await page.selectOption(sel.input('destinations-0-state'), 'IL');
    await page.fill(sel.input('destinations-0-county'), 'Champaign County');
    await page.check(sel.radio('destinations-0-status', 'agreed'));
    await page.fill(sel.input('destinations-0-how_to_reach_them'), 'Phone, then letter');
    await page.fill(sel.input('destinations-0-route_notes'), 'Avoid the river bridge.');
    await page.fill(sel.input('destinations-0-approximate_miles'), '600');
    await layoutChecks(page, 'step 5');
    await shot(page, '05-destinations');
    await next(page);
  });

  await step('step 6: contacts and meeting places', async () => {
    await page.fill(sel.input('contacts-out_of_area_contact-name'), 'Pat');
    await page.fill(sel.input('contacts-out_of_area_contact-relationship'), 'Aunt');
    await page.fill(sel.input('contacts-out_of_area_contact-phone'), '555-0100');
    await page.fill(sel.input('contacts-meeting_place_near_home'), 'Mailbox at the corner');
    await page.fill(sel.input('contacts-utilities-electric-provider'), 'Test Electric Co-op');
    await page.fill(sel.input('contacts-utilities-electric-outage_phone'), '555-0199');
    await page.click('#f-contacts-local_contacts-add');
    await page.fill(sel.input('contacts-local_contacts-0-name'), 'Dr. Lee');
    await page.fill(sel.input('contacts-local_contacts-0-relationship'), 'Family doctor');
    await layoutChecks(page, 'step 6');
    await shot(page, '06-contacts');
    await next(page);
  });

  await step('step 7: gear', async () => {
    await page.click('#f-gear-power_stations-add');
    await page.fill(sel.input('gear-power_stations-0-model'), 'Generic 1000');
    await page.fill(sel.input('gear-power_stations-0-wh'), '1024');
    await page.check('#f-has-generator');
    await page.selectOption(sel.input('gear-generator-fuel'), 'dual-fuel');
    await page.fill(sel.input('gear-generator-watts'), '3500');
    await page.selectOption(sel.input('gear-house_connection'), 'interlock');
    await page.click('#f-gear-heaters-add');
    await page.selectOption(sel.input('gear-heaters-0-kind'), 'portable-propane');
    await page.fill(sel.input('gear-fuel_on_hand-gasoline_gal'), '15');
    await page.fill(sel.input('gear-fuel_on_hand-propane_20lb'), '3');
    await page.fill(sel.input('gear-water-stored_gal'), '30');
    await page.click('#f-gear-water-filters-add');
    await page.fill(sel.input('gear-water-filters-0'), 'Gravity filter');
    await page.check(sel.check('gear-water-bleach_or_shock'));
    await page.check(sel.check('gear-cooking', 'camp-stove-propane'));
    await page.check(sel.check('gear-comms-noaa_radio'));
    await page.selectOption(sel.input('gear-safety-first_aid_tier'), 'basic');
    await page.fill(sel.input('gear-safety-co_alarms'), '2');
    await page.check(sel.radio('gear-firearms-owned', 'true'));
    await page.fill(sel.input('gear-firearms-platforms_and_calibers'), '12-gauge shotgun');
    await page.fill(sel.input('gear-food-pantry_days'), '14');
    await page.check(sel.check('gear-food-canning', 'water-bath'));
    await page.check(sel.check('gear-transport', 'bicycles'));
    await layoutChecks(page, 'step 7');
    await shot(page, '07-gear');
    await next(page);
  });

  await step('step 8: experience, decision cards from the fixture, notes', async () => {
    await page.waitForSelector('.card');
    const n = await page.$$eval('.card', els => els.length);
    assert.equal(n, 24, 'all 24 cards shown (DC-05 because of the attached garage)');
    assert.match(await page.textContent('.card'), /unvented heater/i);
    assert.ok(await page.isChecked(sel.radio('decision_cards-DC-02', 'undecided')), 'undecided by default');
    await page.check(sel.radio('experience', 'some'));
    await page.check(sel.radio('decision_cards-DC-01', 'never'));
    await page.check(sel.radio('decision_cards-DC-05', 'outbuilding-only'));
    assert.match(await page.textContent('.card.worksheet'), /worksheet/);
    await page.fill(sel.input('notes_for_the_binder'), 'Water shutoff is behind the furnace.');
    await layoutChecks(page, 'step 8');
    await shot(page, '08-decisions');
    await next(page);
  });

  let saved;
  await step('final: all answers good, private-copy notice, save profile.json that validates', async () => {
    assert.equal(await page.textContent('#step-title'), 'Make your binder');
    assert.match(await page.textContent('#final-check'), /All needed answers are filled in/);
    assert.ok(await page.isVisible('.notice.private-copy'));
    assert.ok(await page.isVisible('.notice.never-stored'));
    await layoutChecks(page, 'final');
    saved = await saveProfile(page, path.join(OUT, 'profile-a.json'));
    const ok = validateProfile(saved);
    assert.ok(ok, 'schema errors: ' + JSON.stringify(validateProfile.errors, null, 1));
    assert.equal(saved.access.access_key, GOOD_KEY);
    assert.equal(saved.members.length, 2);
    assert.equal(saved.members[1].pregnant_or_nursing, undefined);
    assert.deepEqual(saved.members[0].age, { value: 41, unit: 'years' });
    assert.equal(saved.members[0].ham_callsign, 'KD0ABC');
    assert.equal(saved.decision_cards['DC-01'], 'never');
    assert.equal(saved.decision_cards['DC-05'], 'outbuilding-only');
    assert.equal(saved.decision_cards['DC-02'], 'undecided');
    assert.equal(Object.keys(saved.decision_cards).length, 24);
    assert.equal(saved.gear.generator.fuel, 'dual-fuel');
    assert.equal(saved.dwelling.gas_service.tank_gallons, 500);
    assert.equal(saved.home.county, 'Minnehaha County');
  });

  await step('final: Small vs Large estimates, generate with stub (progress, then download)', async () => {
    const txt = await page.textContent('.sizes');
    assert.match(txt, /Small.*about 30 to 60 MB/s);
    assert.match(txt, /Large.*about 200 to 400 MB/s);
    await page.waitForSelector('#gen-panel .warn'); // test-mode banner (no generate.js yet)
    await page.check('#size-large');
    await page.click('#generate-btn');
    await page.waitForSelector('#gen-progress');
    await shot(page, '09-generate-progress');
    await page.waitForSelector('#download-link', { timeout: 10000 });
    const [dl] = await Promise.all([page.waitForEvent('download'), page.click('#download-link')]);
    assert.equal(dl.suggestedFilename(), 'goettschepreppy-binder-large.html');
    const file = path.join(OUT, 'binder-stub.html');
    await dl.saveAs(file);
    assert.match(fs.readFileSync(file, 'utf8'), /Placeholder, not a binder/);
    await shot(page, '09-generate-done');
  });

  await step('final: cancel stops a run', async () => {
    await page.click('#generate-btn');
    await page.waitForSelector('#cancel-btn');
    await page.click('#cancel-btn');
    await page.waitForFunction(() => /Cancelled/.test(document.querySelector('#gen-panel').textContent));
  });

  await step('nothing was written to browser storage or cookies', async () => {
    assert.equal(await page.evaluate(() => localStorage.length + sessionStorage.length), 0);
    assert.equal((await context.cookies()).length, 0);
  });

  await step('reload loses answers; Load answers restores them exactly', async () => {
    await page.reload();
    await page.waitForSelector('#step-title');
    assert.equal(await page.inputValue(sel.input('access-access_key')), '');
    await page.setInputFiles('#load-file', path.join(OUT, 'profile-a.json'));
    await page.waitForFunction(() => /Loaded your answers/.test(document.querySelector('#toolbar-status').textContent));
    assert.equal(await page.inputValue(sel.input('access-access_key')), GOOD_KEY);
    await page.evaluate(() => window.__settings.goto(3));
    assert.equal(await page.inputValue(sel.input('members-1-label')), 'Sam');
    await page.evaluate(() => window.__settings.goto(9));
    const again = await saveProfile(page, path.join(OUT, 'profile-a2.json'));
    assert.deepEqual(again, saved);
  });

  await step('Load answers rejects a non-profile file without changing anything', async () => {
    const bad = path.join(OUT, 'not-a-profile.json');
    fs.writeFileSync(bad, '[1,2,3]');
    await page.evaluate(() => window.__settings.goto(0));
    await page.setInputFiles('#load-file', bad);
    await page.waitForFunction(() => /Nothing was changed/.test(document.querySelector('#toolbar-status').textContent));
    assert.equal(await page.inputValue(sel.input('access-access_key')), GOOD_KEY);
  });

  await step('a partial profile loads and its gaps are marked', async () => {
    const partial = path.join(OUT, 'partial.json');
    fs.writeFileSync(partial, JSON.stringify({ schema_version: 1, home: { state: 'SD' }, members: [{ label: 'Jo' }] }));
    await page.setInputFiles('#load-file', partial);
    await page.waitForFunction(() => /need a look/.test(document.querySelector('#toolbar-status').textContent));
    await page.evaluate(() => window.__settings.goto(1));
    assert.match(await page.textContent('#f-home-county-err'), /Please answer/);
    await shot(page, '01-home-partial-load');
  });

  await step('keep-in-browser toggle: opt-in, never stores the key, restores, erases', async () => {
    await page.setInputFiles('#load-file', path.join(OUT, 'profile-a.json'));
    await page.evaluate(() => window.__settings.goto(0));
    await page.check('#keep-toggle');
    const stored = await page.evaluate(() => Object.keys(localStorage).map(k => [k, localStorage.getItem(k)]));
    assert.equal(stored.length, 1);
    assert.ok(!stored[0][1].includes(GOOD_KEY), 'access key must not be stored');
    assert.ok(stored[0][1].includes('Minnehaha County'));
    await page.reload();
    await page.waitForSelector('#step-title');
    assert.match(await page.textContent('#toolbar-status'), /restored from this browser/);
    assert.equal(await page.isChecked('#keep-toggle'), true);
    assert.equal(await page.inputValue(sel.input('access-access_key')), '');
    await page.evaluate(() => window.__settings.goto(1));
    assert.equal(await page.inputValue(sel.input('home-county')), 'Minnehaha County');
    await page.evaluate(() => window.__settings.goto(0));
    await page.uncheck('#keep-toggle');
    assert.equal(await page.evaluate(() => localStorage.length), 0);
  });

  await step('light theme renders (screenshot)', async () => {
    await page.click('#theme-btn'); // auto -> dark
    await page.click('#theme-btn'); // dark -> light
    assert.equal(await page.evaluate(() => document.documentElement.dataset.theme), 'light');
    await shot(page, '00-access-light');
  });

  assert.deepEqual(pageErrors, [], 'page errors: ' + pageErrors.join('; '));
  await context.close();
  return saved;
}

// ---------------------------------------------------------------------------------------------
async function scenarioB(browser, base) {
  console.log('Scenario B: kit.json, regions-lite.json and generate.js present (route mocks)');
  const context = await browser.newContext({ viewport: { width: 375, height: 812 }, acceptDownloads: true, colorScheme: 'light' });
  await mockRelay(context, []);
  await context.route('**/app/build/regions-lite.json', r => r.fulfill({ contentType: 'application/json',
    body: JSON.stringify({ SD: ['Lincoln County', 'Minnehaha County'], IL: [{ name: 'Champaign County', fips: '17019' }, { name: 'Cook County' }] }) }));
  await context.route('**/app/build/kit.json', r => r.fulfill({ contentType: 'application/json',
    body: JSON.stringify({ size_estimates: { small: { minMB: 41, maxMB: 41 }, large: { minMB: 260, maxMB: 300 } },
      pages: [{ id: '30-02-dc01', frontmatter: { card: 'DC-01', title: 'Kit card one', settings_summary: 'Summary from the kit.', options: [{ id: 'never', label: 'Never', summary: 'From kit.' }] } }] }) }));
  await context.route('**/app/lib/generate.js', r => r.fulfill({ contentType: 'text/javascript', body: `
    export async function generateBinder(profile, kit, opts) {
      window.__genArgs = { members: profile.members.length, kitPages: kit && kit.pages.length, relay: opts.relay, size: opts.size,
        hasProgress: typeof opts.onProgress === 'function', hasSignal: opts.signal instanceof AbortSignal };
      opts.onProgress({ done: 1, total: 2, stage: 'Halfway' });
      await new Promise(r => setTimeout(r, 200));
      opts.onProgress(1);
      return new Blob(['<!doctype html><title>real</title>'], { type: 'text/html' });
    }` }));
  const page = await context.newPage();
  const pageErrors = [];
  page.on('pageerror', e => pageErrors.push(e.message));
  page.on('dialog', d => d.accept());
  await page.goto(base);
  await page.waitForSelector('#step-title');

  await step('county picker is a list when regions-lite.json exists', async () => {
    await page.evaluate(() => window.__settings.goto(1));
    await page.selectOption(sel.input('home-state'), 'SD');
    const opts = await page.$$eval(`${sel.input('home-county')} option`, os => os.map(o => o.value));
    assert.deepEqual(opts, ['', 'Lincoln County', 'Minnehaha County']);
    await shot(page, '01-home-county-list');
  });

  await step('a loaded profile keeps its county selected; destination counties too', async () => {
    await page.setInputFiles('#load-file', path.join(OUT, 'profile-a.json'));
    await page.waitForFunction(() => /Loaded your answers/.test(document.querySelector('#toolbar-status').textContent));
    await page.evaluate(() => window.__settings.goto(1));
    assert.equal(await page.inputValue(sel.input('home-county')), 'Minnehaha County');
    await page.evaluate(() => window.__settings.goto(5));
    assert.equal(await page.inputValue(sel.input('destinations-0-county')), 'Champaign County');
    // changing state clears a county that is not in the new list
    await page.selectOption(sel.input('destinations-0-state'), 'SD');
    assert.equal(await page.inputValue(sel.input('destinations-0-county')), '');
    await page.selectOption(sel.input('destinations-0-state'), 'IL');
    await page.selectOption(sel.input('destinations-0-county'), 'Champaign County');
  });

  await step('decision cards come from kit.json when it has card pages', async () => {
    await page.evaluate(() => window.__settings.goto(8));
    await page.waitForSelector('.card');
    assert.match(await page.textContent('.card'), /Summary from the kit/);
    assert.equal(await page.$$eval('.card', els => els.length), 1);
  });

  await step('generate calls generateBinder(profile, kit, {relay,size,onProgress,signal})', async () => {
    await page.evaluate(() => window.__settings.goto(9));
    assert.match(await page.textContent('.sizes'), /about 41 MB/);
    assert.equal(await page.$('#gen-panel .warn'), null, 'no test-mode banner when generate.js exists');
    await page.click('#generate-btn');
    await page.waitForSelector('#download-link', { timeout: 10000 });
    const args = await page.evaluate(() => window.__genArgs);
    assert.deepEqual(args, { members: 2, kitPages: 1, relay: '', size: 'small', hasProgress: true, hasSignal: true });
    await shot(page, '09-generate-real-adapter');
  });

  assert.deepEqual(pageErrors, [], 'page errors: ' + pageErrors.join('; '));
  await context.close();
}

// ---------------------------------------------------------------------------------------------
const srv = await serve();
const base = `http://127.0.0.1:${srv.address().port}/app/settings/`;
const browser = await chromium.launch();
try {
  await scenarioA(browser, base);
  await scenarioB(browser, base);
} finally {
  await browser.close();
  srv.close();
}
console.log(failures ? `\n${failures} check(s) failed` : '\nAll settings checks passed. Screenshots: build/settings-shots/');
process.exit(failures ? 1 : 0);

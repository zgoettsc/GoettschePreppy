import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import url from 'node:url';
import { water, calories, dgaModerate, stationFridgeDays } from '../../app/lib/derive.js';
import { buildContext, resolveRegion, normCounty } from '../../app/lib/context.js';

const DIR = path.join(path.dirname(url.fileURLToPath(import.meta.url)), '..', 'profiles');
const load = f => JSON.parse(fs.readFileSync(path.join(DIR, f), 'utf8'));

test('water formula (schema/context.json)', () => {
  // 4 people, 1 nursing, 1 infant, 2 dogs: 4 + 0.5 + 0.5 + 0.5 = 5.5
  const p = load('sd-rural-farm-infant-well.json');
  const w = water(p);
  assert.equal(w.floor_gal_day, 5.5);
  assert.equal(w.plan_gal_day, 7.25);           // 7.15 → nearest 0.25
  assert.equal(w.two_weeks_gal, 105);           // 101.5 → up to 5
  assert.equal(w.stored_days, 5.5);             // 30 / 5.5 = 5.45 → 5.5
  assert.equal(water({ members: [] }).floor_gal_day, null);
});

test('DGA 2020-2025 moderately active calories', () => {
  assert.equal(dgaModerate({ age: { value: 38, unit: 'years' }, sex: 'female' }), 2000);
  assert.equal(dgaModerate({ age: { value: 41, unit: 'years' }, sex: 'male' }), 2600);
  assert.equal(dgaModerate({ age: { value: 78, unit: 'years' }, sex: 'male' }), 2200);
  assert.equal(dgaModerate({ age: { value: 9, unit: 'years' }, sex: 'male' }), 1800);
  assert.equal(dgaModerate({ age: { value: 8, unit: 'months' } }), null);
  assert.equal(dgaModerate({ age: { value: 18, unit: 'months' } }), 1000);
  assert.equal(dgaModerate({ age: { value: 44, unit: 'years' }, sex: 'not-said' }), 2600);
  const c = calories(load('sd-rural-farm-infant-well.json'));
  // Anna 31 F 2000 + nursing 330 (DGA 2020-2025, first 6 months), Ben 33 M 2600, Clara 6 F 1400, Theo under 12 months left out
  assert.equal(c.day, 2330 + 2600 + 1400);
  assert.equal(c.two_weeks, c.day * 14);
  assert.deepEqual(c.left_out, ['Baby Theo']);
});

test('station fridge days', () => {
  assert.equal(stationFridgeDays({ gear: { power_stations: [{ wh: 2048 }, { wh: 512 }] } }), 1.8);
  assert.equal(stationFridgeDays({ gear: {} }), null);
});

test('context flags and lists from each test profile', () => {
  const il = buildContext(load('il-urban-apartment-t2d-elder.json'), {});
  assert.equal(il.has.apartment, true);
  assert.equal(il.has.diabetes, true);
  assert.equal(il.has.food_allergy, false);
  assert.equal(il.has.hybrid, true);
  assert.equal(il.has.elder, true);
  assert.equal(il.has.condition['CL-05'], true);
  assert.equal(il.has.condition['CL-01'], false);
  assert.equal(il.is.urban, true);
  assert.equal(il.home.state_name, 'Illinois');
  assert.equal(il.meds.length, 2);
  assert.equal(il.meds[0].days_on_hand, 45);
  assert.equal(il.elders.length, 1);
  assert.equal(il.agreed_destinations.length, 1);
  assert.equal(il.contacts.utility.gas.phone, '555-0101');
  const sd = buildContext(load('sd-rural-farm-infant-well.json'), {});
  for (const f of ['infant', 'young_child', 'child', 'nursing', 'well', 'septic', 'dogs', 'chickens', 'livestock', 'generator', 'house_connection', 'wood_stove', 'outdoor_fire', 'unvented_heater', 'propane_heater', 'firearms', 'diesel_vehicle', '4wd', 'trailer', 'pressure_canner', 'canning', 'propane_service', 'garage', 'basement', 'acreage'])
    assert.equal(sd.has[f], true, f);
  assert.equal(sd.is.rural, true);
  assert.equal(sd.has.school_age, true);   // Clara, 6
  assert.equal(sd.has.preschool, false);
  assert.equal(sd.infants.length, 1);
  assert.equal(sd.children.length, 2);
  assert.equal(sd.has.agreed_destination, false);
  const oh = buildContext(load('oh-suburban-allergy-generator.json'), {}, { size: 'large' });
  for (const f of ['anaphylaxis', 'epinephrine', 'pool', 'inverter_generator', 'power_station', 'solar', 'ev', 'teen', 'fireplace', 'food_allergy', 'adult_over_40'])
    assert.equal(oh.has[f], true, f);
  assert.equal(oh.gear.station_wh_total, 2560);
  assert.equal(oh.gear.solar_w_total, 400);
  assert.equal(oh.size.large, true);
  assert.equal(oh.size.everything, false);
  const ev = buildContext(load('oh-suburban-allergy-generator.json'), {}, { size: 'everything' });
  assert.deepEqual(ev.size, { large: true, everything: true }); // G25: size.large stays true for Everything
  assert.deepEqual(buildContext(load('oh-suburban-allergy-generator.json'), {}, { size: 'small' }).size, { large: false, everything: false });
  assert.equal(oh.experience.experienced, true);
  assert.equal(oh.dwelling.pool_gallons, 18000);
  const roof = buildContext({ ...load('oh-suburban-allergy-generator.json'), dwelling: { ...load('oh-suburban-allergy-generator.json').dwelling, roof_area_sqft: 1500 } }, {});
  assert.equal(roof.derived.rain_gal_per_inch, 935);
  assert.equal(roof.dwelling.roof_area_sqft, 1500);
  assert.equal(oh.derived.rain_gal_per_inch, null);
});

test('region resolution and county matching', () => {
  const kit = {
    regions: { SD: { state: 'SD', state_name: 'South Dakota', state_em: 'SD Emergency Management', defaults: { zone: '4b' },
      counties: { 'Beadle County': { jan_low_f: 2, record_low_f: -40, jul_high_f: 86, snow_in: 38, ecoregion: 'Northern Glaciated Plains',
        hazards: { tornado: 3, blizzard: 3, hurricane: 1 }, nwr: [{ call: 'WXL00', freq: '162.400', same: '046005' }] } } } },
    ecoregions: { 'Northern Glaciated Plains': { plants: { deadly: ['water-hemlock'], edible: [] }, trees: { firewood: [] } } },
    plates: { 'water-hemlock': { common: 'Water hemlock', scientific: 'Cicuta maculata' } },
  };
  assert.equal(normCounty('Beadle county'), 'beadle');
  const r = resolveRegion(kit, 'SD', 'beadle');
  assert.equal(r.county, 'Beadle County');
  assert.equal(r.zone, '4b');
  assert.equal(r.hazards[0].rating, 3);
  assert.equal(r.plants.deadly[0].text, 'Water hemlock (Cicuta maculata)');
  for (const f of ['key', 'common_name', 'scientific_name', 'look_alike_of']) assert.ok(f in r.plants.deadly[0], f);
  const ctx = buildContext(load('sd-rural-farm-infant-well.json'), kit);
  assert.equal(ctx.is.cold_winters, true);
  assert.equal(ctx.is.extreme_cold, true);
  assert.equal(ctx.is.tornado_region, true);
  assert.equal(ctx.is.hurricane_region, false);
  assert.equal(ctx.is.snow_region, true);
  assert.equal(ctx.is.coastal, false);
  assert.equal(ctx.is.drought_region, false);
  assert.equal(ctx.region.home.state_em, 'SD Emergency Management');
  const none = resolveRegion({}, 'IL', 'Cook County');
  assert.equal(none.state_name, 'Illinois');
  assert.equal(none.zone, null);
});

test('every path, flag and list in schema/context.json exists in a built context', () => {
  const schema = JSON.parse(fs.readFileSync(path.join(DIR, '..', '..', 'schema', 'context.json'), 'utf8'));
  const ctx = buildContext(load('sd-rural-farm-infant-well.json'), {});
  const get = (o, p) => p.split('.').reduce((v, k) => (v == null ? undefined : v[k]), o);
  const has = (o, p) => { const parts = p.split('.'); const last = parts.pop(); const parent = parts.length ? get(o, parts.join('.')) : o; return parent != null && Object.prototype.hasOwnProperty.call(parent, last); };
  const missing = [];
  for (const p of Object.keys(schema.values)) {
    if (p.startsWith('region.dest.')) { if (!has(ctx.destinations[0].region, p.slice(12))) missing.push(p); }
    else if (!has(ctx, p)) missing.push(p);
  }
  for (const f of Object.keys(schema.flags)) {
    if (f === 'has.condition.CL-NN') { if (typeof ctx.has.condition['CL-26'] !== 'boolean') missing.push(f); continue; }
    if (typeof get(ctx, f) !== 'boolean') missing.push(f);
  }
  for (const [l, def] of Object.entries(schema.lists)) {
    const v = get(ctx, l);
    if (!Array.isArray(v)) { missing.push('list ' + l); continue; }
    for (const item of v) for (const f of def.fields) if (!(f in item)) missing.push(`${l}[].${f}`);
  }
  assert.deepEqual(missing, []);
});

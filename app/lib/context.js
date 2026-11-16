// context.js — profile + kit region data → the context object of schema/context.json.
//
// Shape: nested objects, so the template path `has.condition.CL-01` is ctx.has.condition['CL-01']
// and `region.home.zone` is ctx.region.home.zone. Lists are arrays of plain objects. Every value
// not answered is null (prints the fill-in blank). Flags are always booleans.
//
// buildContext(profile, kit, { size }) → ctx
// resolveRegion(kit, state, county) → region object (fields in schema/context.json `region.home.*`)

import { deriveAll, ageMonths, stationWhTotal } from './derive.js';

export const STATE_NAMES = {
  AL: 'Alabama', AK: 'Alaska', AZ: 'Arizona', AR: 'Arkansas', CA: 'California', CO: 'Colorado',
  CT: 'Connecticut', DE: 'Delaware', DC: 'District of Columbia', FL: 'Florida', GA: 'Georgia',
  HI: 'Hawaii', ID: 'Idaho', IL: 'Illinois', IN: 'Indiana', IA: 'Iowa', KS: 'Kansas', KY: 'Kentucky',
  LA: 'Louisiana', ME: 'Maine', MD: 'Maryland', MA: 'Massachusetts', MI: 'Michigan', MN: 'Minnesota',
  MS: 'Mississippi', MO: 'Missouri', MT: 'Montana', NE: 'Nebraska', NV: 'Nevada', NH: 'New Hampshire',
  NJ: 'New Jersey', NM: 'New Mexico', NY: 'New York', NC: 'North Carolina', ND: 'North Dakota',
  OH: 'Ohio', OK: 'Oklahoma', OR: 'Oregon', PA: 'Pennsylvania', RI: 'Rhode Island',
  SC: 'South Carolina', SD: 'South Dakota', TN: 'Tennessee', TX: 'Texas', UT: 'Utah', VT: 'Vermont',
  VA: 'Virginia', WA: 'Washington', WV: 'West Virginia', WI: 'Wisconsin', WY: 'Wyoming',
};

// docs/04-condition-library.md
export const CONDITIONS = {
  'CL-01': 'Type 1 diabetes (injections)', 'CL-02': 'Type 1 diabetes with pump and CGM',
  'CL-03': 'Anaphylaxis', 'CL-04': 'Food allergy', 'CL-05': 'Type 2 diabetes',
  'CL-06': 'Type 2 diabetes on insulin', 'CL-07': 'Asthma', 'CL-08': 'COPD and oxygen',
  'CL-09': 'High blood pressure and heart disease', 'CL-10': 'Blood thinners',
  'CL-11': 'Epilepsy and seizures', 'CL-12': 'Pregnancy, birth and postpartum',
  'CL-13': 'Infant feeding', 'CL-14': 'Thyroid disease', 'CL-15': 'Kidney disease and dialysis',
  'CL-16': 'Mental-health medications', 'CL-17': 'Opioid dependence and chronic pain',
  'CL-18': 'Immunosuppression and transplant', 'CL-19': 'Celiac and severe GI disease',
  'CL-20': 'Adrenal insufficiency', 'CL-21': 'Dementia and elderly care', 'CL-22': 'Mobility impairment',
  'CL-23': 'Hearing and vision aids', 'CL-24': 'Sleep apnea (CPAP)',
  'CL-25': 'Contraception and menstrual health', 'CL-26': 'Severe obesity and bariatric surgery',
};

export const HAZARDS = ['tornado', 'blizzard', 'ice_storm', 'flood', 'wildfire', 'earthquake', 'hurricane',
  'extreme_heat', 'extreme_cold', 'drought', 'volcano', 'tsunami', 'landslide'];
const HAZARD_NAMES = { ice_storm: 'Ice storm', extreme_heat: 'Extreme heat', extreme_cold: 'Extreme cold' };
const RATING_TEXT = { 1: 'low', 2: 'moderate', 3: 'high' };

const W = {
  setting: { urban: 'urban', suburban: 'suburban', 'small-town': 'small town', rural: 'rural', remote: 'remote' },
  dwelling: { 'detached-house': 'detached house', 'townhouse-duplex': 'townhouse or duplex', apartment: 'apartment',
    'mobile-manufactured': 'mobile or manufactured home', 'farm-ranch': 'farm or ranch house', other: 'other dwelling' },
  basement: { none: 'no basement', full: 'full basement', walkout: 'walkout basement', crawlspace: 'crawlspace' },
  water: { municipal: 'municipal (city) water', 'private-well': 'private well', 'shared-well': 'shared well',
    'cistern-haul': 'cistern or hauled water', other: 'other water supply' },
  sewer: { municipal: 'municipal sewer', septic: 'septic system', other: 'other sewer' },
  heat: { 'natural-gas-furnace': 'natural-gas furnace', 'propane-furnace': 'propane furnace', 'heating-oil': 'heating oil',
    'electric-resistance': 'electric resistance heat', 'heat-pump': 'heat pump', 'wood-stove': 'wood stove or insert',
    'pellet-stove': 'pellet stove', other: 'other heat' },
  role: { adult: 'adult', teen: 'teen', child: 'child', 'infant-toddler': 'infant or toddler', elder: 'elder' },
  sex: { female: 'female', male: 'male', 'not-said': 'not said' },
  pn: { no: 'no', pregnant: 'pregnant', nursing: 'nursing', both: 'pregnant and nursing' },
  genFuel: { gasoline: 'gasoline', propane: 'propane', 'dual-fuel': 'dual fuel (gasoline or propane)',
    'tri-fuel': 'tri-fuel (gasoline, propane or natural gas)', diesel: 'diesel' },
  conn: { none: 'no house connection (extension cords only)', interlock: 'interlock kit on the main panel',
    'cord-and-plug': 'cord-and-plug conversion', 'transfer-switch': 'transfer switch' },
  status: { agreed: 'Agreed with the people there', unannounced: 'Not asked: we would arrive unannounced',
    'property-only': 'Nobody there: property only', undecided: 'Undecided' },
  heater: { 'portable-propane': 'portable propane heater', 'wick-kerosene': 'wick kerosene heater',
    'ducted-diesel-kerosene': 'ducted diesel or kerosene heater', 'wood-stove': 'wood stove',
    'pellet-stove': 'pellet stove', 'electric-only': 'electric space heater' },
  destWater: { municipal: 'municipal (city) water', well: 'a well', 'spring-or-surface': 'a spring or surface water', cistern: 'a cistern', unknown: 'not known' },
  destSewer: { municipal: 'municipal sewer', septic: 'septic system', outhouse: 'outhouse', 'none-or-unknown': 'none or not known' },
  vtype: { car: 'car', suv: 'SUV', pickup: 'pickup', van: 'van', motorcycle: 'motorcycle', other: 'vehicle' },
  vfuel: { gasoline: 'gasoline', diesel: 'diesel', hybrid: 'hybrid', ev: 'electric (EV)' },
  skill: { 'medical-professional': 'medical professional', 'nurse-emt': 'nurse or EMT', electrician: 'electrician',
    mechanic: 'mechanic', hunter: 'hunter', 'ham-licence': 'HAM licence', 'farmer-gardener': 'farmer or gardener',
    'firearms-trained': 'firearms trained', none: null },
};
const word = (map, v) => (v == null ? null : (map[v] ?? v));
const nz = v => (v === undefined || v === '' ? null : v);
const num = v => (typeof v === 'number' && Number.isFinite(v) ? v : null);

// ---- regions -----------------------------------------------------------------------------------
export function normCounty(s) {
  return String(s || '').toLowerCase().replace(/\./g, '').replace(/\s+/g, ' ').trim()
    .replace(/\s+(county|parish|borough|census area|municipality|city and borough|city|municipio)$/, '').trim();
}

export function findCounty(stateObj, county) {
  if (!stateObj || !stateObj.counties || !county) return null;
  if (stateObj.counties[county]) return { name: county, data: stateObj.counties[county] };
  const want = normCounty(county);
  for (const [name, data] of Object.entries(stateObj.counties)) if (normCounty(name) === want) return { name, data };
  return null;
}

function plantList(keys, kit) {
  return (keys || []).map(k => {
    const p = kit?.plates?.[k];
    const common = p?.common || k.replace(/-/g, ' ');
    return { key: k, common, scientific: p?.scientific || null, text: p?.scientific ? `${common} (${p.scientific})` : common };
  });
}

export function resolveRegion(kit, state, county) {
  const st = kit?.regions?.[state] || null;
  const hit = findCounty(st, county);
  const d = { ...(st?.defaults || {}), ...(hit?.data || {}) };
  const eco = d.ecoregion && kit?.ecoregions?.[d.ecoregion];
  const plants = d.plants || eco?.plants || {};
  const trees = d.trees || eco?.trees || {};
  const hz = d.hazards || {};
  const hazards = HAZARDS.filter(h => typeof hz[h] === 'number').map(h => {
    const name = HAZARD_NAMES[h] || h.charAt(0).toUpperCase() + h.slice(1);
    return { key: h, name, rating: hz[h], rating_text: RATING_TEXT[hz[h]] || null, text: `${name} (${RATING_TEXT[hz[h]] || hz[h]})` };
  }).sort((a, b) => b.rating - a.rating);
  return {
    state,
    state_name: st?.state_name || STATE_NAMES[state] || null,
    county: hit?.name || nz(county) || null,
    county_found: !!hit,
    zone: nz(d.zone) ?? null,
    last_frost: nz(d.last_frost) ?? null,
    first_frost: nz(d.first_frost) ?? null,
    growing_days: num(d.growing_days),
    jan_low_f: num(d.jan_low_f),
    jul_high_f: num(d.jul_high_f),
    record_low_f: num(d.record_low_f),
    record_high_f: num(d.record_high_f),
    precip_in: num(d.precip_in),
    snow_in: num(d.snow_in),
    elevation_ft: num(d.elevation_ft),
    ecoregion: nz(d.ecoregion) ?? null,
    nws_office: nz(d.nws_office) ?? null,
    nwr: (d.nwr || []).map(t => ({ call: t.call ?? null, freq: t.freq ?? null, same: t.same ?? null, text: [t.call, t.freq && `${t.freq} MHz`, t.same && `SAME ${t.same}`].filter(Boolean).join(' ') })),
    state_em: nz(st?.state_em) ?? nz(d.state_em) ?? null,
    hazards,
    hazard_rating: Object.fromEntries(HAZARDS.map(h => [h, typeof hz[h] === 'number' ? hz[h] : null])),
    plants: { deadly: plantList(plants.deadly, kit), edible: plantList(plants.edible, kit) },
    trees: { firewood: plantList(trees.firewood, kit) },
    sun_hours_dec: num(d.sun_hours_dec),
    sun_hours_jun: num(d.sun_hours_jun),
    latitude: num(d.latitude) ?? (Array.isArray(d.centroid) && typeof d.centroid[0] === 'number' ? Math.round(d.centroid[0] * 10) / 10 : null),
    coastal: d.coastal === true ? true : d.coastal === false ? false : null,
    text: [hit?.name || county, st?.state_name || STATE_NAMES[state]].filter(Boolean).join(', '),
  };
}

// ---- context -----------------------------------------------------------------------------------
function ageText(m) {
  const a = m.age; if (!a) return null;
  if (a.unit === 'months') return `${a.value} month${a.value === 1 ? '' : 's'}`;
  return `${a.value} year${a.value === 1 ? '' : 's'}`;
}

function contact(c) {
  return c ? { name: nz(c.name) ?? null, relationship: nz(c.relationship) ?? null, phone: nz(c.phone) ?? null,
    notes: nz(c.notes) ?? null, text: nz(c.name) ?? null } : { name: null, relationship: null, phone: null, notes: null };
}

export function buildContext(profile, kit = {}, opts = {}) {
  const p = profile || {};
  const home = p.home || {}, dw = p.dwelling || {}, gear = p.gear || {}, contacts = p.contacts || {};
  const membersRaw = p.members || [];
  const derived = deriveAll(p);

  // members and the cross-member lists
  const meds = [], allergies = [];
  const members = membersRaw.map(m => {
    const mMeds = (m.medications || []).map(x => ({
      member: m.label, name: nz(x.name) ?? null, strength: nz(x.strength) ?? null, schedule: nz(x.schedule) ?? null,
      refrigerated: x.refrigerated === true ? 'yes' : x.refrigerated === false ? 'no' : null,
      if_missed: nz(x.if_missed) ?? null,
      days_on_hand: num(x.days_on_hand),
      where_kept: nz(x.where_kept) ?? null, expiry: nz(x.expiry) ?? null,
      text: [x.name, x.strength].filter(Boolean).join(' '),
    }));
    const mAll = (m.allergies || []).map(x => ({
      member: m.label, allergen: x.allergen, severity: x.severity,
      carries_epinephrine: x.carries_epinephrine === true ? 'yes' : x.carries_epinephrine === false ? 'no' : null,
      text: x.allergen, // formatting.nested: names only
    }));
    meds.push(...mMeds); allergies.push(...mAll);
    const conds = (m.conditions || []).map(id => CONDITIONS[id] || id); // formatting.nested: names, not ids
    if (m.conditions_other) conds.push(m.conditions_other);
    return {
      label: m.label, role: word(W.role, m.role), age_text: ageText(m), age_months: ageMonths(m),
      weight_text: m.weight ? `${m.weight.value} ${m.weight.unit}` : null,
      sex: word(W.sex, m.sex) ?? null, pregnant_or_nursing: word(W.pn, m.pregnant_or_nursing) ?? null,
      conditions: conds, allergies: mAll, meds: mMeds,
      skills: (m.skills || []).map(s => word(W.skill, s)).filter(Boolean),
      text: m.label,
    };
  });

  const regHome = resolveRegion(kit, home.state, home.county);
  // derived.solar_wh_dec / _jun: solar_w_total x sun hours x 0.75 (system losses), rounded
  const solarW = (gear.solar_panels || []).reduce((n, x) => n + (Number(x.watts) || 0) * (x.count || 1), 0);
  derived.solar_wh_dec = solarW && typeof regHome.sun_hours_dec === 'number' ? Math.round(solarW * regHome.sun_hours_dec * 0.75) : null;
  derived.solar_wh_jun = solarW && typeof regHome.sun_hours_jun === 'number' ? Math.round(solarW * regHome.sun_hours_jun * 0.75) : null;
  const destinations = (p.destinations || []).map(d => {
    const r = resolveRegion(kit, d.state, d.county);
    return {
      name: d.name, state_name: r.state_name, county: r.county, status: d.status, status_text: word(W.status, d.status),
      who_is_there: nz(d.who_is_there) ?? null, how_to_reach_them: nz(d.how_to_reach_them) ?? null,
      route_notes: nz(d.route_notes) ?? null, approximate_miles: num(d.approximate_miles), region: r, text: d.name,
      water_source_text: word(W.destWater, d.water_source) ?? null, sewer_text: word(W.destSewer, d.sewer) ?? null,
    };
  });

  const pets = (p.pets || []).map(x => ({ type: x.type, count: x.count, medications: nz(x.medications) ?? null,
    food_per_day: nz(x.food_per_day) ?? null, text: `${x.count} ${x.type}${x.count > 1 && x.type !== 'other' ? 's' : ''}` }));
  const livestock = (p.livestock || []).map(x => ({ type: x.type, count: x.count, text: `${x.count} ${x.type}` }));
  const heaters = (gear.heaters || []).map(h => ({ kind: h.kind, kind_text: word(W.heater, h.kind), model: nz(h.model) ?? null,
    text: [word(W.heater, h.kind), h.model].filter(Boolean).join(': ') }));
  const stations = (gear.power_stations || []).map(s => ({ model: nz(s.model) ?? null, wh: num(s.wh),
    pv_input_max_v: num(s.pv_input_max_v), pv_input_max_w: num(s.pv_input_max_w), text: [s.model, s.wh && `${s.wh} Wh`].filter(Boolean).join(', ') }));
  const panels = (gear.solar_panels || []).map(s => ({ model: nz(s.model) ?? null, watts: num(s.watts), count: s.count ?? null,
    voc: num(s.voc), isc: num(s.isc), text: nz(s.model) ?? null }));
  const vehicles = (dw.vehicles || []).map(v => ({ type: v.type, fuel: v.fuel, type_text: word(W.vtype, v.type), fuel_text: word(W.vfuel, v.fuel),
    four_wheel_drive: v.four_wheel_drive ? 'yes' : 'no', can_tow: v.can_tow ? 'yes' : 'no', text: `${word(W.vtype, v.type)} (${word(W.vfuel, v.fuel)})` }));
  const local_contacts = (contacts.local_contacts || []).map(contact);

  // ---- flags -----------------------------------------------------------------------------------
  const ages = membersRaw.map(ageMonths);
  const anyAge = f => ages.some(a => a !== null && f(a));
  const allSkills = membersRaw.flatMap(m => m.skills || []);
  const mob = membersRaw.flatMap(m => m.mobility_or_sensory || []);
  const ff = dw.fire_features || [];
  const heatKinds = heaters.map(h => h.kind);
  const gen = gear.generator || null;
  const hasGen = !!(gen && (gen.fuel || gen.watts || gen.model || gen.inverter));
  const gasKind = dw.gas_service?.kind;
  const pool = dw.pool_or_hot_tub?.kind;
  const canning = gear.food?.canning || [];
  const comms = gear.comms || {};
  const hz = regHome.hazard_rating;
  const conditionFlags = {};
  for (let i = 1; i <= 26; i++) {
    const id = `CL-${String(i).padStart(2, '0')}`;
    conditionFlags[id] = membersRaw.some(m => (m.conditions || []).includes(id));
  }
  const has = {
    infant: anyAge(a => a < 24) || membersRaw.some(m => m.role === 'infant-toddler' && ageMonths(m) === null),
    toddler: anyAge(a => a >= 12 && a <= 47),
    young_child: anyAge(a => a < 72),
    child: anyAge(a => a < 156),
    teen: anyAge(a => a >= 156 && a < 216) || membersRaw.some(m => m.role === 'teen'),
    elder: anyAge(a => a > 840) || membersRaw.some(m => m.role === 'elder'),
    adult_over_40: anyAge(a => a >= 480),
    pregnant: membersRaw.some(m => m.pregnant_or_nursing === 'pregnant' || m.pregnant_or_nursing === 'both'),
    nursing: membersRaw.some(m => m.pregnant_or_nursing === 'nursing' || m.pregnant_or_nursing === 'both'),
    pets: pets.length > 0,
    dogs: pets.some(x => x.type === 'dog'),
    cats: pets.some(x => x.type === 'cat'),
    livestock: livestock.length > 0,
    chickens: livestock.some(x => x.type === 'chickens'),
    condition: conditionFlags,
    refrigerated_meds: membersRaw.some(m => (m.medications || []).some(x => x.refrigerated === true)),
    anaphylaxis: membersRaw.some(m => (m.allergies || []).some(x => x.severity === 'anaphylaxis')),
    epinephrine: membersRaw.some(m => (m.allergies || []).some(x => x.carries_epinephrine === true)),
    oxygen: mob.includes('oxygen'),
    cpap: mob.includes('cpap'),
    mobility_aid: mob.includes('wheelchair-walker'),
    basement: ['full', 'walkout'].includes(dw.basement),
    walkout: dw.basement === 'walkout',
    shelter_room: !!(dw.windowless_interior_room?.present),
    apartment: dw.dwelling_type === 'apartment',
    mobile_home: dw.dwelling_type === 'mobile-manufactured',
    garage: dw.attached_garage === true,
    well: ['private-well', 'shared-well'].includes(dw.water_supply),
    septic: dw.sewer === 'septic',
    municipal_water: dw.water_supply === 'municipal',
    natural_gas: gasKind === 'natural-gas',
    propane_service: gasKind === 'propane-tank',
    gas_any: gasKind === 'natural-gas' || gasKind === 'propane-tank',
    water_heater_tank: ['tank-gas', 'tank-electric'].includes(dw.water_heater?.kind),
    pool: ['chlorine-pool', 'saltwater-pool'].includes(pool),
    saltwater_pool: pool === 'saltwater-pool',
    hot_tub: pool === 'hot-tub',
    fireplace: ff.includes('indoor-fireplace'),
    wood_stove: ff.includes('wood-stove') || dw.primary_heat === 'wood-stove' || heatKinds.includes('wood-stove'),
    outdoor_fire: ff.includes('outdoor-fireplace') || ff.includes('fire-pit'),
    garden: !!dw.garden_space && dw.garden_space !== 'none',
    yard: ['small-yard', 'large-yard', 'acreage'].includes(dw.garden_space),
    acreage: dw.garden_space === 'acreage',
    generator: hasGen,
    inverter_generator: hasGen && gen.inverter === true,
    house_connection: ['interlock', 'cord-and-plug', 'transfer-switch'].includes(gear.house_connection),
    power_station: stations.length > 0,
    solar: panels.length > 0,
    propane_heater: heatKinds.includes('portable-propane'),
    kerosene_heater: heatKinds.includes('wick-kerosene'),
    diesel_heater: heatKinds.includes('ducted-diesel-kerosene'),
    unvented_heater: heatKinds.includes('portable-propane') || heatKinds.includes('wick-kerosene'),
    firearms: gear.firearms?.owned === true,
    safe: gear.firearms?.safe === true,
    ham: comms.ham === true || allSkills.includes('ham-licence') || membersRaw.some(m => m.ham_callsign),
    gmrs: comms.frs_gmrs === true || comms.gmrs_licence === true,
    noaa_radio: comms.noaa_radio === true,
    satellite: comms.satellite_messenger === true || comms.starlink === true,
    vehicle: vehicles.length > 0,
    diesel_vehicle: vehicles.some(v => v.fuel === 'diesel'),
    ev: vehicles.some(v => v.fuel === 'ev'),
    hybrid: vehicles.some(v => v.fuel === 'hybrid'),
    '4wd': vehicles.some(v => v.four_wheel_drive === 'yes'),
    trailer: !!dw.trailer && dw.trailer !== 'none',
    destinations: destinations.length > 0,
    agreed_destination: destinations.some(d => d.status === 'agreed'),
    canning: canning.length > 0,
    pressure_canner: canning.some(c => c.startsWith('pressure')),
  };
  const ge = (v, n) => typeof v === 'number' && v >= n;
  const is = {
    urban: ['urban', 'suburban'].includes(home.setting),
    rural: ['rural', 'remote'].includes(home.setting),
    cold_winters: typeof regHome.jan_low_f === 'number' && regHome.jan_low_f < 20,
    extreme_cold: typeof regHome.record_low_f === 'number' && regHome.record_low_f < -20,
    hot_summers: typeof regHome.jul_high_f === 'number' && regHome.jul_high_f > 90,
    high_altitude: typeof regHome.elevation_ft === 'number' ? regHome.elevation_ft > 5000 : home.elevation_band === 'high',
    tornado_region: ge(hz.tornado, 2),
    hurricane_region: ge(hz.hurricane, 2),
    wildfire_region: ge(hz.wildfire, 2),
    earthquake_region: ge(hz.earthquake, 2),
    flood_region: ge(hz.flood, 2),
    tsunami_region: ge(hz.tsunami, 2),
    volcano_region: ge(hz.volcano, 2),
    landslide_region: ge(hz.landslide, 2),
    drought_region: ge(hz.drought, 2),
    coastal: regHome.coastal === true,
    snow_region: typeof regHome.snow_in === 'number' && regHome.snow_in > 20,
  };
  const experience = { new: p.experience === 'new', some: p.experience === 'some', experienced: p.experience === 'experienced' };

  const fuel = gear.fuel_on_hand || {};
  const util = contacts.utilities || {};
  const u = k => ({ provider: nz(util[k]?.provider) ?? null, phone: nz(util[k]?.outage_phone) ?? null });
  const adults = membersRaw.filter(m => m.role === 'adult' || m.role === 'elder').length;

  return {
    household: {
      name: 'Our household',
      size: membersRaw.length || null,
      adults: membersRaw.length ? adults : null,
      children: membersRaw.length ? membersRaw.length - adults : null,
      labels: membersRaw.map(m => m.label).join(', ') || null,
    },
    home: {
      state: home.state || null,
      state_name: STATE_NAMES[home.state] || null,
      county: regHome.county,
      town: nz(home.nearest_town) ?? regHome.county,
      setting: word(W.setting, home.setting) ?? null,
    },
    dwelling: {
      type: word(W.dwelling, dw.dwelling_type) ?? null,
      basement: word(W.basement, dw.basement) ?? null,
      shelter_room: dw.windowless_interior_room?.present ? (nz(dw.windowless_interior_room.which) ?? null) : null,
      water_supply: word(W.water, dw.water_supply) ?? null,
      sewer: word(W.sewer, dw.sewer) ?? null,
      primary_heat: word(W.heat, dw.primary_heat) ?? null,
      roof_area_sqft: num(dw.roof_area_sqft),
      water_heater_gallons: ['tank-gas', 'tank-electric'].includes(dw.water_heater?.kind) ? num(dw.water_heater?.gallons) : null,
      pool_gallons: pool && pool !== 'none' ? num(dw.pool_or_hot_tub?.gallons) : null,
    },
    contacts: {
      out_of_area: contact(contacts.out_of_area_contact),
      meet: { near_home: nz(contacts.meeting_place_near_home) ?? null, in_town: nz(contacts.meeting_place_in_town) ?? null,
        out_of_town: nz(contacts.meeting_place_out_of_town) ?? null },
      utility: { electric: u('electric'), gas: u('gas'), water: u('water') },
    },
    gear: {
      station_wh_total: stationWhTotal(p),
      solar_w_total: panels.length ? panels.reduce((n, x) => n + (x.watts || 0) * (x.count || 1), 0) || null : null,
      generator_watts: hasGen ? num(gen.watts) : null,
      generator_fuel: hasGen ? word(W.genFuel, gen.fuel) ?? null : null,
      generator_volts: hasGen ? ({ '120': '120 V only', '120-240': '120/240 V' }[gen.volts] ?? null) : null,
      house_connection: word(W.conn, gear.house_connection) ?? null,
      co_alarms: num(gear.safety?.co_alarms),
      smoke_alarms: num(gear.safety?.smoke_alarms),
      extinguishers: num(gear.safety?.extinguishers),
      fuel: {
        gasoline_gal: num(fuel.gasoline_gal), diesel_gal: num(fuel.diesel_gal), kerosene_gal: num(fuel.kerosene_gal),
        propane_1lb: num(fuel.propane_1lb), propane_20lb: num(fuel.propane_20lb), firewood_cords: num(fuel.firewood_cords),
      },
      water: { stored_gal: num(gear.water?.stored_gal) },
      food: { pantry_days: num(gear.food?.pantry_days), freeze_dried_servings: num(gear.food?.freeze_dried_servings) },
    },
    derived,
    region: { home: regHome },
    members, meds, allergies, pets, livestock, destinations, local_contacts, heaters, stations, panels, vehicles,
    // member subsets (same fields as members)
    adults: members.filter(m => ['adult', 'elder'].includes(membersRaw[members.indexOf(m)].role)),
    children: members.filter(m => (m.age_months ?? 999) < 156 || ['child', 'infant-toddler'].includes(membersRaw[members.indexOf(m)].role)),
    infants: members.filter(m => m.age_months !== null ? m.age_months < 24 : membersRaw[members.indexOf(m)].role === 'infant-toddler'),
    teens: members.filter(m => (m.age_months !== null && m.age_months >= 156 && m.age_months < 216) || membersRaw[members.indexOf(m)].role === 'teen'),
    elders: members.filter(m => (m.age_months ?? 0) > 840 || membersRaw[members.indexOf(m)].role === 'elder'),
    refrigerated_meds: meds.filter(x => x.refrigerated === 'yes'),
    agreed_destinations: destinations.filter(d => d.status === 'agreed'),
    has, is, experience,
    size: { large: opts.size === 'large' },
    // not template paths; used by generate.js
    _choices: p.decision_cards || {},
    _notes: nz(p.notes_for_the_binder) ?? null,
  };
}

// The subset of a context a model may see for an ai block: only the declared inputs.
// inputs: [ 'path.to.value', { list, fields: [...], region: [...] } ] (build-kit parseAiInputs).
// Values that do not exist are dropped. `text` helper fields are dropped. Selected condition
// modules are always added as `condition_pages` so a block can point to them.
export function pickInputs(ctx, inputs, scopes = []) {
  const out = {};
  const get = path => {
    const parts = path.split('.');
    let v;
    for (let i = scopes.length - 1; i >= 0 && v === undefined; i--) if (scopes[i] && Object.prototype.hasOwnProperty.call(scopes[i], parts[0])) v = parts.reduce((o, k) => o?.[k], scopes[i]);
    if (v === undefined) v = parts.reduce((o, k) => o?.[k], ctx);
    return v;
  };
  const clean = v => JSON.parse(JSON.stringify(v ?? null, (k, x) => (k === 'text' || k === 'key' || k === 'hazard_rating' ? undefined : x)));
  for (const inp of inputs || []) {
    if (typeof inp === 'string') { const v = get(inp); if (v !== undefined) out[inp] = clean(v); continue; }
    const list = get(inp.list);
    if (!Array.isArray(list)) continue;
    out[inp.list] = list.map(item => {
      const o = {};
      for (const f of inp.fields || []) if (f in item) o[f] = clean(item[f]);
      if (inp.region?.length && item.region) { o.region = {}; for (const f of inp.region) if (f in item.region) o.region[f] = clean(item.region[f]); }
      return (inp.fields || []).length || inp.region?.length ? o : clean(item);
    });
  }
  out.condition_pages = Object.entries(ctx.has?.condition || {}).filter(([, v]) => v)
    .map(([id]) => ({ condition: `${id} ${CONDITIONS[id]}`, page: `02-${id.slice(3)}` }));
  return out;
}

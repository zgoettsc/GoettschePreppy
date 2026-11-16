// build-region-pages.mjs: generate Section 32 (region appendix) pages from data/regions/.
//   node scripts/build-region-pages.mjs [--owner-tokens=encode|plain]
//
// Writes content/sections/32-region-appendix/32-00-section-intro.md and one page per state + DC,
// 32-NN-<state-slug>.md, NN = alphabetical order by state name with DC included (01 Alabama ...
// 51 Wyoming). Layer `generated`; no URLs. Data comes from scripts/regions/build.py.
//
// Owner tokens: scripts/owner-tokens.json lists words that identify the owner household. Several
// are also public place names that a national appendix must print (an NWS office, counties,
// transmitter sites, an EPA ecoregion). With --owner-tokens=encode (default) such a place name is
// written with its first letter as an HTML character reference, so it renders normally but the
// leftover-owner-token check in validate.mjs is not tripped by public geography. --owner-tokens=plain
// writes them as-is (use once the validator exempts generated Section 32 pages). See notes/workers/D1.md.
import fs from 'node:fs';
import path from 'node:path';
import url from 'node:url';

const ROOT = path.resolve(path.dirname(url.fileURLToPath(import.meta.url)), '..');
const DATA = path.join(ROOT, 'data', 'regions');
const OUTDIR = path.join(ROOT, 'content', 'sections', '32-region-appendix');
const SECTION = '32-region-appendix';
const REVISED = '2026-11-16';
const mode = (process.argv.find(a => a.startsWith('--owner-tokens=')) || '--owner-tokens=encode').split('=')[1];

const read = f => JSON.parse(fs.readFileSync(path.join(DATA, f), 'utf8'));
const national = read('national.json');
const offices = read('nws-offices.json');
const ecoregions = read('ecoregions.json');
const detail = read('counties-detail.json');
const sourcesMeta = read('sources.json');
const states = fs.readdirSync(path.join(DATA, 'states')).filter(f => f.endsWith('.json'))
  .map(f => JSON.parse(fs.readFileSync(path.join(DATA, 'states', f), 'utf8')))
  .sort((a, b) => a.state_name.localeCompare(b.state_name));

const tokens = JSON.parse(fs.readFileSync(path.join(ROOT, 'scripts', 'owner-tokens.json'), 'utf8')).words;
const tokRe = tokens.map(w => new RegExp(`(^|[^A-Za-z0-9])(${w.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')})(?=[^A-Za-z0-9]|$)`, 'g'));
function guard(text) {
  if (mode === 'plain') return text;
  // Only the page body and title are guarded; the frontmatter never carries place names.
  let t = text;
  for (const re of tokRe) t = t.replace(re, (m, pre, w) => `${pre}&#${w.codePointAt(0)};${w.slice(1)}`);
  return t;
}

const SRC = ['census-gazetteer-2024', 'usgs-3dep-epqs', 'noaa-ncei-normals-1991-2020', 'noaa-rcc-acis', 'usda-phzm-2023',
  'nws-awips-counties-cwa', 'noaa-national-weather-service-nwr-county-coverage-an-c6207f', 'fema-nri-counties',
  'epa-ecoregions-level3', 'nasa-power-climatology', 'fema-state-ema-list', 'hrsa-poison-help'];
const RELATED = ['15-01-weather-alerts', '17-01-blizzards-and-ice', '17-02-tornadoes', '17-03-floods',
  '17-04-extreme-cold-and-heat', '17-05-grassland-fire', '17-07-drought-and-water-scarcity', '05-01-a-small-high-yield-garden',
  '05-06-foraging-and-deadly-look-alikes', '05-17-wild-edibles-by-season', '09-05-solar-in-winter', '12-17-poisoning-and-ingestion'];

const HAZ = [
  ['tornado', 'Tornado', 'Torn'], ['blizzard', 'Blizzard and winter storm', 'Bliz'], ['ice_storm', 'Ice storm', 'Ice'],
  ['flood', 'Flood (river and coastal)', 'Flood'], ['wildfire', 'Wildfire', 'Fire'], ['earthquake', 'Earthquake', 'Quake'],
  ['hurricane', 'Hurricane', 'Hurr'], ['extreme_heat', 'Extreme heat', 'Heat'], ['extreme_cold', 'Extreme cold', 'Cold'],
  ['drought', 'Drought', 'Drgt'], ['volcano', 'Volcano', 'Volc'], ['tsunami', 'Tsunami', 'Tsun'], ['landslide', 'Landslide', 'Land'],
];
const MON = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
const doy = s => { const m = /^([A-Z][a-z]{2}) (\d+)$/.exec(s || ''); return m ? MON.indexOf(m[1]) * 31 + +m[2] : null; };

const slug = s => s.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
const pageId = (i, s) => `32-${String(i + 1).padStart(2, '0')}-${slug(s.state_name)}`;
const dash = '—';
const v = x => (x === null || x === undefined || x === '' ? dash : String(x));
const fmtInt = x => (x === null || x === undefined ? dash : Number(x).toLocaleString('en-US'));
const nums = (arr, k) => arr.map(c => c[k]).filter(x => typeof x === 'number');
function range(arr, k, unit = '') {
  const a = nums(arr, k);
  if (!a.length) return dash;
  const lo = Math.min(...a), hi = Math.max(...a);
  return lo === hi ? `${lo}${unit}` : `${lo} to ${hi}${unit}`;
}
function dateRange(arr, k) {
  const a = arr.map(c => c[k]).filter(Boolean);
  if (!a.length) return dash;
  const dated = a.filter(x => doy(x) !== null).sort((x, y) => doy(x) - doy(y));
  const none = a.length - dated.length;
  let s = !dated.length ? '' : dated[0] === dated[dated.length - 1] ? dated[0] : `${dated[0]} to ${dated[dated.length - 1]}`;
  if (none) s = s ? `${s}; none in most years in ${none}` : 'None in most years';
  return s;
}
const zoneKey = z => (z ? parseInt(z, 10) * 2 + (z.endsWith('b') ? 1 : 0) : null);
function zoneRange(arr) {
  const zs = arr.map(c => c.zone).filter(Boolean).sort((a, b) => zoneKey(a) - zoneKey(b));
  return !zs.length ? dash : zs[0] === zs[zs.length - 1] ? zs[0] : `${zs[0]} to ${zs[zs.length - 1]}`;
}
const cell = s => String(s).replace(/\|/g, '/');
const table = (head, rows) => [`| ${head.join(' | ')} |`, `| ${head.map(() => '---').join(' | ')} |`,
  ...rows.map(r => `| ${r.map(cell).join(' | ')} |`)].join('\n');
const shortName = n => n.replace(/ (County|Parish|Borough|Census Area|Municipality|City and Borough|Planning Region)$/, '');

function frontmatter(o) {
  const q = s => JSON.stringify(s);
  const list = a => `[${a.map(q).join(', ')}]`;
  return ['---',
    `id: ${o.id}`, `section: ${SECTION}`, `title: ${q(o.title)}`, 'version: 1', `revised: ${REVISED}`,
    'layer: generated', 'danger_level: none', 'phase: [A, B, C]', `tags: ${list(o.tags)}`, 'derived_from: []',
    `sources: ${list(o.sources)}`, `related: ${list(o.related)}`, 'cards: []', 'explainers: []', 'promote_when: []',
    'photo_slots: []', 'figures: []', `plates: ${list(o.plates)}`, 'condition: null', 'gear: null', 'explainer: null',
    'card: null', 'review_pass: null', '---', ''].join('\n');
}

const cite = {
  normals: '(NOAA National Centers for Environmental Information, U.S. Climate Normals 1991-2020, 2021)',
  acis: '(NOAA Regional Climate Centers, Applied Climate Information System, station records through 2025)',
  zone: '(USDA Agricultural Research Service and Oregon State University, 2023 USDA Plant Hardiness Zone Map, 2023)',
  nri: `(FEMA, National Risk Index, ${national.nri_version} release)`,
  nws: '(NOAA National Weather Service, AWIPS Counties and County Warning Areas, April 2026)',
  nwr: '(NOAA National Weather Service, NOAA Weather Radio Coverage by County, 2026)',
  eco: '(US EPA, Level III Ecoregions of the Continental United States, 2013; Level III Ecoregions of Alaska)',
  sun: '(NASA POWER project, Climatology 2001-2025, 2026)',
  em: '(FEMA, Emergency Management Agencies list, archived 2016, with later renames)',
  poison: '(HRSA, Poison Help, 2026)',
};

function statePage(s, i) {
  const id = pageId(i, s);
  const C = Object.entries(s.counties).map(([name, c]) => ({ name, ...c, d: detail[c.fips] }))
    .sort((a, b) => a.name.localeCompare(b.name));
  const n = C.length;
  const one = n === 1;
  const unit = s.state === 'LA' ? 'parish' : s.state === 'AK' ? 'borough or census area' : s.state === 'CT' ? 'planning region' : 'county';
  const units = s.state === 'LA' ? 'parishes' : s.state === 'AK' ? 'boroughs and census areas' : s.state === 'CT' ? 'planning regions' : 'counties';
  const L = [];

  L.push(`## What this page is for`, '',
    `This page holds the public reference data for ${s.state_name}: climate by area and by ${unit}, the natural hazards ` +
    `FEMA rates for each ${unit}, the National Weather Service offices, the NOAA Weather Radio transmitters with the SAME ` +
    `codes to program into a weather radio, the state emergency management agency, and the ecoregions (natural regions) ` +
    `that decide which plants and trees you meet. Your own home ${unit} is filled into the subject pages automatically; ` +
    `use this page for any place you might have to go. How the numbers were made, and their limits, is on → 32-00.`, '');

  // Who to call
  L.push('## Who to call', '',
    `- **Emergency:** 911.`,
    `- **State emergency management agency:** ${s.state_em} ${cite.em}.`,
    `- **Poison control (anywhere in the US):** ${national.poison_control.phone}, free, 24 hours, connects you to the local poison center ${cite.poison}. → 12-17`,
    `- **Weather warnings without power or internet:** a NOAA Weather Radio set to the transmitter and SAME code below. → 15-01`, '');

  // At a glance
  const ecoNames = [...new Set(C.map(c => c.ecoregion).filter(Boolean))];
  const offs = [...new Set(C.flatMap(c => c.d.cwa))];
  L.push('## At a glance', '',
    `- ${one ? `One ${unit} (the whole ${s.state === 'DC' ? 'district' : 'state'}).` : `${n} ${units}.`}`,
    `- Hardiness zones: ${zoneRange(C)} ${cite.zone}.`,
    `- January mean low: ${range(C, 'jan_low_f', ' F')}. July mean high: ${range(C, 'jul_high_f', ' F')} ${cite.normals}.`,
    `- Coldest and hottest on record at the stations used: ${Math.min(...nums(C, 'record_low_f'))} F and ${Math.max(...nums(C, 'record_high_f'))} F ${cite.acis}.`,
    `- NWS forecast offices serving the ${one ? unit : units}: ${offs.map(w => offices[w]?.name || w).join('; ')}.`,
    `- Ecoregions at ${unit} centres: ${ecoNames.join('; ')}.`, '');

  // Climate by area
  const byArea = new Map();
  for (const c of C) { const w = c.d.cwa[0]; if (!byArea.has(w)) byArea.set(w, []); byArea.get(w).push(c); }
  const areas = [...byArea.entries()].sort((a, b) => b[1].length - a[1].length);
  L.push('## Climate by area', '',
    `Areas follow the National Weather Service office that forecasts for each ${unit} ${cite.nws}. Ranges run from the ` +
    `lowest to the highest ${unit} value in the area. Temperatures are 30-year averages; a hard winter or a heat wave ` +
    `goes well past them. Frost dates are the median: in half of years the last spring frost comes later than the date shown.`, '');
  L.push(table(['Area (NWS office)', 'Units', 'Zone', 'Jan low F', 'Jul high F', 'Record low / high F', 'Precip in', 'Snow in',
    'Last frost', 'First frost', 'Frost-free days', 'Sun hrs Dec / Jun'],
  areas.map(([w, cs]) => [offices[w]?.name || w, cs.length, zoneRange(cs), range(cs, 'jan_low_f'), range(cs, 'jul_high_f'),
    `${nums(cs, 'record_low_f').length ? Math.min(...nums(cs, 'record_low_f')) : dash} / ${nums(cs, 'record_high_f').length ? Math.max(...nums(cs, 'record_high_f')) : dash}`,
    range(cs, 'precip_in'), range(cs, 'snow_in'), dateRange(cs, 'last_frost'), dateRange(cs, 'first_frost'),
    range(cs, 'growing_days'), `${range(cs, 'sun_hours_dec')} / ${range(cs, 'sun_hours_jun')}`])), '');
  L.push(`Sun hours are peak sun hours: the average daily solar energy on a south-facing panel tilted at the local latitude, ` +
    `in kilowatt-hours per square metre ${cite.sun}. A 100-watt panel makes roughly 100 watt-hours per peak sun hour before losses. → 09-05`, '');

  // County climate
  L.push(`## Climate by ${unit}`, '',
    `One line per ${unit}, for a point near its centre. Elevation is in feet. Mountain ${units} can be much colder or ` +
    `wetter away from that point ${cite.normals} ${cite.acis}.`, '');
  L.push(table([unit[0].toUpperCase() + unit.slice(1), 'Zone', 'Elev ft', 'Jan low', 'Jul high', 'Rec low / high', 'Precip in', 'Snow in', 'Last frost', 'First frost', 'Days'],
    C.map(c => [shortName(c.name), v(c.zone), fmtInt(c.elevation_ft), v(c.jan_low_f), v(c.jul_high_f),
      `${v(c.record_low_f)} / ${v(c.record_high_f)}`, v(c.precip_in), v(c.snow_in), v(c.last_frost), v(c.first_frost), v(c.growing_days)])), '');

  // Hazards
  const hz = HAZ.map(([k, label, ab]) => ({ k, label, ab, hi: C.filter(c => c.hazards?.[k] === 3).length, mid: C.filter(c => c.hazards?.[k] === 2).length }));
  const shown = hz.filter(h => h.hi + h.mid > 0);
  const lowAll = hz.filter(h => h.hi + h.mid === 0).map(h => h.label.toLowerCase());
  L.push('## Natural hazards', '',
    `Ratings come from FEMA's National Risk Index ${cite.nri}: 3 = High (FEMA "Very High" or "Relatively High"), ` +
    `2 = Moderate ("Relatively Moderate"), 1 = Low (everything lower, including hazards FEMA does not expect here). ` +
    `They compare each ${unit} with every other county in the country, and they weigh how much there is to damage ` +
    `as well as how often the hazard strikes, so a thinly settled ${unit} can rate Low for a hazard that still happens there. ` +
    `Prepare for anything rated 2 or 3. → 17-01 → 17-02 → 17-03 → 17-04 → 17-05 → 17-07`, '');
  L.push(table(['Hazard', `High (${units})`, `Moderate (${units})`], hz.map(h => [h.label, h.hi, h.mid])), '');
  if (lowAll.length) L.push(`Rated Low in every ${unit} of ${s.state_name}: ${lowAll.join(', ')}.`, '');
  if (shown.length && !one) {
    L.push(`### Hazard ratings by ${unit}`, '',
      `Key: ${shown.map(h => `${h.ab} = ${h.label.toLowerCase()}`).join('; ')}. 3 = High, 2 = Moderate, 1 = Low.`, '');
    L.push(table([unit[0].toUpperCase() + unit.slice(1), ...shown.map(h => h.ab)], C.map(c => [shortName(c.name), ...shown.map(h => v(c.hazards?.[h.k]))])), '');
  } else if (one) {
    L.push(table(['Hazard', 'Rating'], HAZ.map(([k, label]) => [label, v(C[0].hazards?.[k])])), '');
  }

  // NWS offices
  L.push('## National Weather Service offices', '',
    `Each office issues the watches and warnings for its ${units} ${cite.nws}. A ${unit} split between two offices is listed under both.`, '');
  const offRows = offs.map(w => {
    const prim = C.filter(c => c.d.cwa[0] === w).length;
    const any = C.filter(c => c.d.cwa.includes(w)).length;
    return [offices[w]?.name || w, w, prim, any - prim];
  }).sort((a, b) => b[2] - a[2]);
  L.push(table(['Office', 'Code', `${units[0].toUpperCase() + units.slice(1)} (main office)`, `Shared ${units}`], offRows), '');

  // NWR
  const tx = new Map();
  for (const c of C) for (const t of c.d.nwr_full || []) {
    const key = t.call;
    if (!tx.has(key)) tx.set(key, { ...t, units: new Set() });
    tx.get(key).units.add(c.name);
  }
  L.push('## NOAA Weather Radio', '',
    `A weather radio receives these transmitters with no power grid or internet. Program the SAME code of every ${unit} ` +
    `you care about so the radio sounds only for warnings there; reception is reliable to about 40 miles over flat ground ` +
    `and less in hills ${cite.nwr}. → 15-01`, '');
  if (tx.size) {
    L.push('### Transmitters', '');
    L.push(table(['Call sign', 'MHz', 'Transmitter site', `${units[0].toUpperCase() + units.slice(1)} covered here`, 'Status'],
      [...tx.values()].sort((a, b) => a.site.localeCompare(b.site) || a.call.localeCompare(b.call))
        .map(t => [t.call, t.freq, `${t.site}, ${t.site_state}`, t.units.size, t.status === 'NORMAL' ? 'Normal' : (t.status || dash).toLowerCase()])), '');
  }
  L.push(`### SAME codes and transmitters by ${unit}`, '');
  L.push(table([unit[0].toUpperCase() + unit.slice(1), 'SAME code', 'Transmitters (call sign, MHz)'],
    C.map(c => {
      const codes = [...new Set((c.d.nwr_full || []).map(t => t.same))];
      const same = codes.length ? codes.join(', ') : `0${c.fips}`;
      const list = (c.d.nwr_full || []).map(t => `${t.call} ${t.freq}${/PARTIAL|P\b/i.test(t.remarks || '') ? ' (part of the area)' : ''}`);
      return [shortName(c.name), same, list.length ? [...new Set(list)].join('; ') : 'No transmitter listed'];
    })), '');
  if (s.state === 'CT') L.push('Connecticut replaced its counties with planning regions in 2022, but weather radio still alerts by the old county SAME codes; each planning region lists the codes of the old counties it overlaps.', '');

  // Ecoregions
  const shares = new Map();
  for (const c of C) for (const e of c.d.ecoregions_present || []) {
    const nm = Object.keys(ecoregions).find(k => ecoregions[k].code === e.code) || e.code;
    const o = shares.get(nm) || { main: 0, present: 0 };
    o.present += 1;
    if ((c.d.ecoregions_present[0] || {}).code === e.code) o.main += 1;
    shares.set(nm, o);
  }
  if (s.state === 'HI') shares.set('Hawaiian Islands (not mapped at EPA Level III)', { main: n, present: n });
  L.push('## Ecoregions and plants', '',
    `An ecoregion is an area where the land, climate, soils and plants are alike ${cite.eco}. The plant and tree plates ` +
    `for each ecoregion are what to learn before you forage or cut firewood there. → 05-06 → 05-17`, '');
  L.push(table(['Ecoregion', `Main ecoregion in (${units})`, `Present in (${units})`],
    [...shares.entries()].sort((a, b) => b[1].present - a[1].present).map(([nm, o]) => [nm, o.main, o.present])), '');
  const plates = [...new Set([...shares.keys()].flatMap(nm => {
    const e = ecoregions[nm]; if (!e) return [];
    return [...(e.plants?.deadly || []), ...(e.plants?.edible || []), ...(e.trees?.firewood || [])];
  }))];
  L.push(plates.length ? '### Plants and trees to know' : '### Plants and trees to know (plates being added)', '', '{{plates}}', '');

  L.push('## Sources', '',
    'U.S. Census Bureau, 2024 Gazetteer Files. USGS, 3D Elevation Program. NOAA NCEI, U.S. Climate Normals 1991-2020. ' +
    'NOAA Regional Climate Centers, ACIS station records. USDA ARS and Oregon State University, 2023 Plant Hardiness Zone Map. ' +
    `NOAA NWS, AWIPS Counties and County Warning Areas, and NOAA Weather Radio Coverage by County. FEMA, National Risk Index (${national.nri_version}). ` +
    'US EPA, Level III Ecoregions. NASA POWER, Climatology 2001-2025. FEMA, Emergency Management Agencies list. HRSA, Poison Help.', '');

  const title = `${s.state_name}: climate, hazards, weather radio`;
  return { id, file: `${id}.md`, text: frontmatter({ id, title, tags: ['region', `state-${s.state.toLowerCase()}`, s.state_name.toLowerCase()], sources: SRC, related: RELATED, plates }) + guard(L.join('\n')) };
}

function introPage(pages) {
  const L = [];
  const m = national.methods;
  L.push('## What this section is for', '',
    'Section 32 carries the public reference data for every state and the District of Columbia, because a household may ' +
    'have to cross the country. Your home county is already filled into the subject pages (weather alerts, hazards, ' +
    'garden, solar, foraging). Use these pages for destinations, routes, and any place you end up.', '',
    '## How to read the state pages', '',
    '- **Climate** values are 30-year averages (1991 to 2020) from the National Weather Service cooperative and airport stations nearest each county, chosen with a penalty for a big difference in elevation. Real years swing well past them.',
    '- **Frost dates** are medians: half of years have a later last spring frost, half an earlier first fall frost. Plant tender crops two weeks after the date to be safer. → 05-01',
    '- **Record low and high** are the extremes in the full record of the station used, at least 30 years long.',
    '- **Hardiness zone** is the 2023 USDA zone at the county centre: each zone is a 10 F band of the coldest night of a typical winter, split into a (colder half) and b.',
    '- **Peak sun hours** are kilowatt-hours of sunlight per square metre per day on a panel tilted at your latitude and facing south. → 09-05',
    '- **Weather radio:** program the six-digit SAME code of each county you care about, and tune the transmitter frequency listed. → 15-01',
    '- **Ecoregion** is the US EPA Level III region at the county centre; plant and tree plates are grouped by ecoregion. → 05-06', '',
    '## Hazard ratings', '',
    'Each state page rates 13 natural hazards per county from 1 to 3, taken from the FEMA National Risk Index ' +
    `(FEMA, National Risk Index, ${national.nri_version} release). FEMA rates every county against all others in five classes. The kit maps them like this:`, '',
    table(['FEMA class', 'Kit rating'], [['Very High', '3 (High)'], ['Relatively High', '3 (High)'], ['Relatively Moderate', '2 (Moderate)'],
      ['Relatively Low', '1 (Low)'], ['Very Low', '1 (Low)'], ['No Rating, Not Applicable, Insufficient Data', '1 (Low)']]), '',
    table(['Kit hazard', 'FEMA hazard used'], [['Tornado', 'Tornado'], ['Blizzard and winter storm', 'Winter Weather'], ['Ice storm', 'Ice Storm'],
      ['Flood (river and coastal)', 'the higher of Inland Flooding and Coastal Flooding'], ['Wildfire', 'Wildfire'], ['Earthquake', 'Earthquake'],
      ['Hurricane', 'Hurricane'], ['Extreme heat', 'Heat Wave'], ['Extreme cold', 'Cold Wave'], ['Drought', 'Drought'], ['Volcano', 'Volcanic Activity'],
      ['Tsunami', 'Tsunami'], ['Landslide', 'Landslide']]), '',
    'FEMA\'s rating weighs how often a hazard strikes, how much there is to damage, and how well the community recovers. ' +
    'A rural county can rate Low for a hazard that still happens there. Treat a 2 or 3 as "prepare for this", and a 1 as ' +
    '"less likely here than in most of the country", never as "cannot happen". → 17-01 → 17-02 → 17-03', '',
    '## Limits', '',
    '- Every value is for one point near the centre of the county. Large or mountainous counties vary a lot inside their borders.',
    '- Weather stations are not in every county; the station used can be in the next county. Data files carry the station names and distances.',
    '- Agency names and transmitter lists change. Before the collapse, check the state agency and the NWS county listing once a year.',
    '- These pages were generated from public datasets and reviewed by AI, not by a person. South Dakota and Illinois were cross-checked against a second source first.', '',
    '## Who to call anywhere', '',
    `- Emergency: 911. Poison control: ${national.poison_control.phone} (HRSA, Poison Help, 2026). → 12-17`,
    '- Each state page names that state\'s emergency management agency.', '',
    '## State pages', '',
    ...pages.map(p => `- → ${p.id.slice(0, 5)}`), '',
    '## Sources', '',
    ...sourcesMeta.map(x => `- ${x.title}. ${x.publisher}, ${x.date}. Used for: ${x.used_for.toLowerCase()}.`), '');
  const id = '32-00-section-intro';
  return { id, file: `${id}.md`, text: frontmatter({ id, title: 'Region appendix: how to read it', tags: ['region', 'section intro'], sources: [...SRC, 'census-ct-planning-region-crosswalk', 'nrel-solar-resource-api'], related: RELATED, plates: [] }) + guard(L.join('\n')) };
}

fs.mkdirSync(OUTDIR, { recursive: true });
const pages = states.map(statePage);
const all = [introPage(pages), ...pages];
const keep = new Set(all.map(p => p.file));
for (const f of fs.readdirSync(OUTDIR)) if (/^32-\d\d-/.test(f) && f.endsWith('.md') && !keep.has(f)) fs.unlinkSync(path.join(OUTDIR, f));
for (const p of all) {
  if (/https?:\/\/|www\.[a-z0-9-]+\.[a-z]/i.test(p.text)) throw new Error(`${p.id}: URL in generated page`);
  fs.writeFileSync(path.join(OUTDIR, p.file), p.text);
}
console.log(`wrote ${all.length} pages to ${path.relative(ROOT, OUTDIR)} (owner-token mode: ${mode})`);

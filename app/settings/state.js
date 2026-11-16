// The household's answers, held in memory only, and conversion to and from profile.json.
//
// `draft` mirrors schema/profile.schema.json but may be incomplete or hold raw text the person is
// still typing. `toProfile()` turns it into a clean profile (empty answers dropped, hidden
// follow-up answers dropped, every card given a value). Nothing here touches storage.

import validateProfile from './profile-validate.js';
import { CARD_IDS } from './data.js';

export const draft = blankDraft();
// UI-only answers that are not part of the profile (never saved, never sent).
export const ui = { hasGenerator: false };

export function blankDraft() {
  return {
    schema_version: 1,
    access: { save_profile_locally: false },
    home: {},
    dwelling: {},
    members: [newMember()],
    pets: [], livestock: [], destinations: [],
    contacts: {}, gear: {},
    decision_cards: {},
  };
}
export function newMember() { return { label: '', age: { unit: 'years' } }; }

// ---- path access -------------------------------------------------------------------------
export const ptr = (path) => '/' + path.join('/');
export function getAt(path, root = draft) {
  let o = root;
  for (const k of path) { if (o == null) return undefined; o = o[k]; }
  return o;
}
export function setAt(path, value, root = draft) {
  let o = root;
  for (let i = 0; i < path.length - 1; i++) {
    const k = path[i];
    if (o[k] == null || typeof o[k] !== 'object') o[k] = typeof path[i + 1] === 'number' ? [] : {};
    o = o[k];
  }
  const last = path[path.length - 1];
  if (value === undefined) { if (Array.isArray(o)) o[last] = undefined; else delete o[last]; }
  else o[last] = value;
}
export function replaceDraft(next) {
  for (const k of Object.keys(draft)) delete draft[k];
  Object.assign(draft, next);
}

// ---- clean profile -----------------------------------------------------------------------
const isEmpty = (v) => v === undefined || v === null || v === '' ||
  (Array.isArray(v) && v.length === 0) ||
  (typeof v === 'object' && !Array.isArray(v) && Object.keys(v).length === 0);

function clean(v) {
  if (Array.isArray(v)) {
    // list items are kept even when blank so validation can point at them
    const out = v.filter(x => x !== undefined && x !== null).map(x => (typeof x === 'object' ? (clean(x) ?? {}) : x));
    return out.length ? out : undefined;
  }
  if (v && typeof v === 'object') {
    const out = {};
    for (const [k, x] of Object.entries(v)) {
      const c = clean(x);
      if (!isEmpty(c)) out[k] = c;
    }
    return Object.keys(out).length ? out : undefined;
  }
  if (typeof v === 'string') { const t = v.trim(); return t === '' ? undefined : t; }
  return v;
}

const TANK_HEATERS = ['tank-gas', 'tank-electric'];

export function showsPregnancy(m) {
  return m && m.sex !== 'male' && !['child', 'infant-toddler'].includes(m.role);
}

/** The profile as it would be saved or sent. `opts.includeKey` false leaves the access key out. */
export function toProfile(opts = {}) {
  const d = structuredClone(draft);
  const dw = d.dwelling || {};
  if (dw.gas_service && dw.gas_service.kind !== 'propane-tank') delete dw.gas_service.tank_gallons;
  if (dw.water_heater && !TANK_HEATERS.includes(dw.water_heater.kind)) delete dw.water_heater.gallons;
  if (dw.pool_or_hot_tub && (!dw.pool_or_hot_tub.kind || dw.pool_or_hot_tub.kind === 'none')) delete dw.pool_or_hot_tub.gallons;
  if (dw.windowless_interior_room && dw.windowless_interior_room.present !== true) delete dw.windowless_interior_room.which;
  for (const m of d.members || []) {
    if (!m) continue;
    if (m.weight && (m.weight.value === undefined || m.weight.value === '')) delete m.weight;
    else if (m.weight && !m.weight.unit) m.weight.unit = 'lb'; // the unit menu shows lb until changed
    if (m.age && m.age.value !== undefined && !m.age.unit) m.age.unit = 'years';
    if (m.age && (m.age.value === undefined || m.age.value === '') && Object.keys(m.age).length <= 1) {
      // only a unit: the age is unanswered; leave `age` out so "required" is reported once
      delete m.age;
    }
    if (!showsPregnancy(m)) delete m.pregnant_or_nursing;
    if (!(m.skills || []).includes('ham-licence')) delete m.ham_callsign;
    if ((m.mobility_or_sensory || []).includes('none') && m.mobility_or_sensory.length > 1)
      m.mobility_or_sensory = m.mobility_or_sensory.filter(x => x !== 'none');
    if ((m.skills || []).includes('none') && m.skills.length > 1) m.skills = m.skills.filter(x => x !== 'none');
  }
  const g = d.gear || {};
  if (!ui.hasGenerator) delete g.generator;
  if (g.firearms && g.firearms.owned !== true) {
    delete g.firearms.platforms_and_calibers; delete g.firearms.safe; delete g.firearms.suppressors;
  }
  if (g.water && Array.isArray(g.water.filters)) g.water.filters = g.water.filters.filter(f => f && String(f).trim());

  const cards = {};
  for (const id of CARD_IDS) {
    let v = d.decision_cards?.[id];
    if (id === 'DC-05' && dw.attached_garage !== true) v = 'undecided';
    cards[id] = v || 'undecided';
  }
  d.decision_cards = cards;

  const out = clean(d) || {};
  out.schema_version = 1;
  // keep the required objects even when empty, so validation names each missing answer
  out.home ??= {};
  out.dwelling ??= {};
  out.decision_cards = cards; // always present, even if every card is undecided
  if (out.access) {
    if (opts.includeKey === false) delete out.access.access_key;
    if (out.access.save_profile_locally === undefined) out.access.save_profile_locally = false;
  } else out.access = { save_profile_locally: false };
  // keep a stable key order (schema order) so saved files are easy to read
  const order = ['schema_version', 'access', 'home', 'dwelling', 'members', 'pets', 'livestock', 'destinations', 'contacts', 'gear', 'experience', 'decision_cards', 'notes_for_the_binder'];
  const sorted = {};
  for (const k of order) if (out[k] !== undefined) sorted[k] = out[k];
  return sorted;
}

// ---- load a profile.json -----------------------------------------------------------------
const LIST_PATHS = [['members'], ['pets'], ['livestock'], ['destinations'], ['dwelling', 'vehicles'], ['contacts', 'local_contacts'],
  ['gear', 'power_stations'], ['gear', 'solar_panels'], ['gear', 'heaters']];

/** Turn parsed JSON into a draft, tolerating gaps; never throws on odd shapes. */
export function draftFromProfile(p) {
  if (!p || typeof p !== 'object' || Array.isArray(p)) throw new Error('not-an-object');
  const d = blankDraft();
  for (const [k, v] of Object.entries(p)) d[k] = structuredClone(v);
  d.schema_version = 1;
  for (const k of ['access', 'home', 'dwelling', 'contacts', 'gear', 'decision_cards'])
    if (!d[k] || typeof d[k] !== 'object' || Array.isArray(d[k])) d[k] = {};
  for (const path of LIST_PATHS) {
    const v = getAt(path, d);
    if (v !== undefined && !Array.isArray(v)) setAt(path, [], d);
    const arr = getAt(path, d);
    if (Array.isArray(arr)) setAt(path, arr.map(x => (x && typeof x === 'object' && !Array.isArray(x) ? x : {})), d);
  }
  if (!d.members.length) d.members = [newMember()];
  for (const m of d.members) {
    if (!m.age || typeof m.age !== 'object') m.age = { unit: 'years' };
    for (const k of ['medications', 'allergies']) if (m[k] !== undefined && !Array.isArray(m[k])) m[k] = [];
  }
  if (d.access.save_profile_locally === undefined) d.access.save_profile_locally = false;
  return d;
}
export function loadProfile(p) {
  const d = draftFromProfile(p);
  replaceDraft(d);
  ui.hasGenerator = !!(d.gear && d.gear.generator && Object.keys(d.gear.generator).length);
}

// ---- validation --------------------------------------------------------------------------
export const STEP_OF = {
  access: 0, home: 1, dwelling: 2, members: 3, pets: 4, livestock: 4, destinations: 5,
  contacts: 6, gear: 7, experience: 8, decision_cards: 8, notes_for_the_binder: 8, schema_version: 0,
};

function plain(e) {
  const p = e.params || {};
  switch (e.keyword) {
    case 'required': return 'Please answer this one.';
    case 'const': return e.instancePath === '/access/acknowledged_notice' ? 'Please tick the box to say you have read the notice.' : 'This answer is not one we can use.';
    case 'enum': return 'Please pick one of the choices.';
    case 'type': return p.type === 'integer' ? 'Please type a whole number, digits only.' : p.type === 'number' ? 'Please type a number, digits only.' : 'This answer is not in a form we can use.';
    case 'minLength': return p.limit === 1 ? 'Please answer this one.' : `Please type at least ${p.limit} characters.`;
    case 'maxLength': return `That is too long: ${p.limit} characters at most.`;
    case 'minimum': return `The smallest number allowed here is ${p.limit}.`;
    case 'maximum': return `The largest number allowed here is ${p.limit}.`;
    case 'minItems': return p.limit === 1 ? 'Please add at least one.' : `Please add at least ${p.limit}.`;
    case 'maxItems': return `At most ${p.limit} here.`;
    case 'uniqueItems': return 'The same choice appears twice.';
    case 'pattern':
      if (/ham_callsign$/.test(e.instancePath)) return 'That does not look like a callsign (for example KD0ABC).';
      if (/^\/access\/access_key/.test(e.instancePath)) return 'That does not look like an access key.';
      return 'This answer is not in a form we can use.';
    case 'additionalProperties': return `The file has an answer we do not recognise (${p.additionalProperty}).`;
    default: return 'This answer needs another look.';
  }
}

/**
 * Validate a profile. Returns { ok, errors: [{ pointer, step, message }] }.
 * `extra` adds checks the schema cannot express (county against the state's list).
 */
export function validate(profile, extra = []) {
  const ok = validateProfile(profile);
  const errors = [];
  const seen = new Set();
  for (const e of ok ? [] : validateProfile.errors || []) {
    let pointer = e.instancePath || '';
    if (e.keyword === 'required') pointer += '/' + e.params.missingProperty;
    if (e.keyword === 'additionalProperties') pointer += '/' + e.params.additionalProperty;
    if (e.keyword === 'if' || e.keyword === 'anyOf' || e.keyword === 'oneOf') continue;
    const key = pointer + '|' + e.keyword;
    if (seen.has(key)) continue;
    seen.add(key);
    const top = pointer.split('/')[1] || 'access';
    errors.push({ pointer, step: STEP_OF[top] ?? 0, message: plain(e) });
  }
  // a member with no answered age: point at the number box
  for (const er of errors) if (/^\/members\/\d+\/age$/.test(er.pointer)) er.pointer += '/value';
  errors.push(...extra);
  return { ok: ok && extra.length === 0, errors };
}

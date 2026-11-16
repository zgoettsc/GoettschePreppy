// derive.js — the derived values of schema/context.json (`derived.*`), as pure functions.
//
// Every formula below is the one written in schema/context.json; nothing is added. Inputs are the
// raw profile (schema/profile.schema.json). Where an input is missing the result is null, which the
// template prints as a fill-in blank, never a guess.
//
// Published tables implemented here:
//   * Water: 1 gallon per person per day, at least 3 days, 2 weeks if possible.
//     CDC, "Creating and Storing an Emergency Water Supply" (2024); FEMA/Ready.gov, "Water" (2023).
//     The +0.5 gal (pregnant or nursing; infant) and +0.25 gal (pet) allowances and the 1.3 planning
//     margin are the kit's own rules as written in schema/context.json.
//   * Calories: U.S. Department of Agriculture and U.S. Department of Health and Human Services,
//     Dietary Guidelines for Americans, 2020-2025, 9th edition, Appendix 2 "Estimated Calorie Needs
//     per Day, by Age, Sex, and Physical Activity Level", MODERATELY ACTIVE column, ages 2 and over. Ages 12 to 23 months: the Guidelines' Chapter 2
//     ("Infants and Toddlers") states toddler needs of roughly 700 to 1,000 calories a day; the kit
//     takes the upper figure (1,000) so a store is not planned short. Under 12 months: the
//     Guidelines give no calorie figure (breast milk or infant formula), so infants are left out of
//     the food sum and covered by the infant-feeding module (→ 02-13). Pregnant +340 (second
//     trimester figure) and nursing +450 are printed as written in schema/context.json.
//   * Power station fridge estimate: 1.2 kWh/day typical full-size refrigerator and 85 % usable
//     inverter output, as written in schema/context.json. Printed as an estimate.

// [sedentary, moderately active, active] — DGA 2020-2025 Appendix 2. Keys are the age row's lower bound.
export const DGA_CALORIES = {
  male: [
    [2, 1000, 1000, 1000], [3, 1000, 1400, 1400], [4, 1200, 1400, 1600], [5, 1200, 1400, 1600],
    [6, 1400, 1600, 1800], [7, 1400, 1600, 1800], [8, 1400, 1600, 2000], [9, 1600, 1800, 2000],
    [10, 1600, 1800, 2200], [11, 1800, 2000, 2200], [12, 1800, 2200, 2400], [13, 2000, 2200, 2600],
    [14, 2000, 2400, 2800], [15, 2200, 2600, 3000], [16, 2400, 2800, 3200], [17, 2400, 2800, 3200],
    [18, 2400, 2800, 3200], [19, 2600, 2800, 3000], [21, 2400, 2800, 3000], [26, 2400, 2600, 3000],
    [31, 2400, 2600, 3000], [36, 2400, 2600, 2800], [41, 2200, 2600, 2800], [46, 2200, 2400, 2800],
    [51, 2200, 2400, 2800], [56, 2200, 2400, 2600], [61, 2000, 2400, 2600], [66, 2000, 2200, 2600],
    [71, 2000, 2200, 2600], [76, 2000, 2200, 2400],
  ],
  female: [
    [2, 1000, 1000, 1000], [3, 1000, 1200, 1400], [4, 1200, 1400, 1400], [5, 1200, 1400, 1600],
    [6, 1200, 1400, 1600], [7, 1200, 1600, 1800], [8, 1400, 1600, 1800], [9, 1400, 1600, 1800],
    [10, 1400, 1800, 2000], [11, 1600, 1800, 2000], [12, 1600, 2000, 2200], [13, 1600, 2000, 2200],
    [14, 1800, 2000, 2400], [15, 1800, 2000, 2400], [16, 1800, 2000, 2400], [17, 1800, 2000, 2400],
    [18, 1800, 2000, 2400], [19, 2000, 2200, 2400], [21, 2000, 2200, 2400], [26, 1800, 2000, 2400],
    [31, 1800, 2000, 2200], [36, 1800, 2000, 2200], [41, 1800, 2000, 2200], [46, 1800, 2000, 2200],
    [51, 1600, 1800, 2200], [56, 1600, 1800, 2200], [61, 1600, 1800, 2000], [66, 1600, 1800, 2000],
    [71, 1600, 1800, 2000], [76, 1600, 1800, 2000],
  ],
};
export const TODDLER_12_23_MONTHS = 1000; // DGA 2020-2025 ch. 2, upper end of "700 to 1,000"
export const PREGNANT_EXTRA = 340;
export const NURSING_EXTRA = 450;

export function ageMonths(member) {
  const a = member && member.age;
  if (!a || typeof a.value !== 'number') return null;
  return a.unit === 'months' ? a.value : a.value * 12;
}

const isPregnant = m => m.pregnant_or_nursing === 'pregnant' || m.pregnant_or_nursing === 'both';
const isNursing = m => m.pregnant_or_nursing === 'nursing' || m.pregnant_or_nursing === 'both';
const isInfant = m => { const mo = ageMonths(m); return mo !== null ? mo < 24 : m.role === 'infant-toddler'; };

// Moderately active row for one member. Sex not given → the higher of the two rows (a store is
// not planned short). Returns null for under 12 months (no published figure).
export function dgaModerate(member) {
  const mo = ageMonths(member);
  if (mo === null) return null;
  if (mo < 12) return null;
  if (mo < 24) return TODDLER_12_23_MONTHS;
  const years = Math.floor(mo / 12);
  const row = sex => { let r = null; for (const x of DGA_CALORIES[sex]) if (years >= x[0]) r = x; return r[2]; };
  if (member.sex === 'male') return row('male');
  if (member.sex === 'female') return row('female');
  return Math.max(row('male'), row('female'));
}

export const round1 = x => Math.round(x * 10) / 10;
export const roundQuarter = x => Math.round(x * 4) / 4;
export const roundUpTo = (x, step) => Math.ceil(x / step - 1e-9) * step;

export function petCount(profile) {
  return (profile.pets || []).reduce((n, p) => n + (Number(p.count) || 0), 0);
}

export function water(profile) {
  const members = profile.members || [];
  if (!members.length) return { floor_gal_day: null, plan_gal_day: null, two_weeks_gal: null, stored_days: null };
  let floor = members.length * 1;
  floor += members.filter(m => isPregnant(m) || isNursing(m)).length * 0.5;
  floor += members.filter(isInfant).length * 0.5;
  floor += petCount(profile) * 0.25;
  const plan = roundQuarter(floor * 1.3);
  const stored = profile.gear?.water?.stored_gal;
  return {
    floor_gal_day: floor,
    plan_gal_day: plan,
    two_weeks_gal: roundUpTo(plan * 14, 5),
    stored_days: typeof stored === 'number' ? round1(stored / floor) : null,
  };
}

export function calories(profile) {
  const members = profile.members || [];
  let day = 0, counted = 0;
  const left_out = [];
  for (const m of members) {
    const base = dgaModerate(m);
    if (base === null) { left_out.push(m.label); continue; }
    let c = base;
    if (isPregnant(m)) c += PREGNANT_EXTRA;
    if (isNursing(m)) c += NURSING_EXTRA;
    day += c; counted++;
  }
  // A nursing or pregnant member under 12 months is impossible; extras only ride on a counted row.
  return counted ? { day, two_weeks: day * 14, left_out } : { day: null, two_weeks: null, left_out };
}

export function stationWhTotal(profile) {
  const st = profile.gear?.power_stations || [];
  const wh = st.reduce((n, s) => n + (Number(s.wh) || 0), 0);
  return st.length && wh > 0 ? wh : null;
}

export function stationFridgeDays(profile) {
  const wh = stationWhTotal(profile);
  return wh ? round1(wh * 0.85 / 1200) : null;
}

export function supplyClocks(profile) {
  const rows = [];
  for (const m of profile.members || []) for (const med of m.medications || [])
    rows.push({ member: m.label, name: med.name, days_on_hand: null, text: med.name });
  return rows;
}

export function deriveAll(profile) {
  const c = calories(profile);
  return {
    water: water(profile),
    calories: { day: c.day, two_weeks: c.two_weeks },
    calories_left_out: c.left_out,
    station_fridge_days: stationFridgeDays(profile),
    supply_clocks: supplyClocks(profile),
  };
}

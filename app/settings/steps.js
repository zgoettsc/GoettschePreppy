// Steps 0 to 8 of docs/02-profile-schema.md. Each step returns DOM nodes; app.js wraps them
// with the notice, the navigation and the Save / Load bar.

import { h, q, list, group, idOf } from './ui.js';
import { draft, ui, getAt, setAt, newMember, showsPregnancy } from './state.js';
import { STATES, CONDITIONS, E } from './data.js';
import { NOTICE } from './notice.js';

// Filled in by app.js: { regions, kitState, keyCheck(), keepToggle() }
export const env = { regions: { available: false, counties: {} }, kitState: { loading: true, cards: [] } };

const P = (...p) => p; // readability: P('home','state')

// ---- county picker ---------------------------------------------------------------------------
function countyPicker(statePath, countyPath, { required = true, label = 'County', why } = {}) {
  const st = getAt(statePath);
  const list = env.regions.available && st ? env.regions.counties[st] : null;
  if (list && list.length) {
    const cur = getAt(countyPath);
    const options = list.map(c => [c, c]);
    if (cur && !list.includes(cur)) options.unshift([cur, `${cur} (not in our list)`]);
    return q({ kind: 'select', path: countyPath, label, why, required, options, emptyLabel: 'Choose your county…' });
  }
  const warn = !st
    ? 'Choose the state first and the county list appears here.'
    : env.regions.available
      ? 'We have no county list for this state yet, so please type the county name exactly as it is spelled, for example "Minnehaha County".'
      : 'The county list could not be loaded, so please type the county name exactly as it is spelled, for example "Minnehaha County". The binder checks it later.';
  const node = q({ kind: 'text', path: countyPath, label, why, required, maxlength: 64, autocomplete: 'off', placeholder: 'County name' });
  node.insertBefore(h('p', { class: 'warn' }, warn), node.querySelector('.err'));
  return node;
}
function clearCountyIfStale(countyPath) {
  return (st) => {
    const list = env.regions.available && st ? env.regions.counties[st] : null;
    const cur = getAt(countyPath);
    if (list && cur && !list.includes(cur)) setAt(countyPath, undefined);
  };
}
const stateOptions = STATES.map(([v, n]) => [v, n]);

/** Checks for an object of booleans (gear.comms): ticked = true, unticked = left out. */
function boolChecks(basePath, title, why, options) {
  const box = h('div', { class: 'choices cols' }, options.map(([key, label]) => {
    const path = [...basePath, key];
    const id = idOf(path);
    return h('label', { class: 'choice', for: id },
      h('input', { type: 'checkbox', id, checked: getAt(path) === true || undefined,
        onchange: (e) => { setAt(path, e.target.checked ? true : undefined); } }),
      h('span', { class: 'choice-text' }, label));
  }));
  return h('fieldset', { class: 'q', dataset: { paths: '/' + basePath.join('/') } },
    h('legend', { class: 'q-label' }, title),
    why ? h('p', { class: 'why' }, h('span', { class: 'why-tag' }, 'Why we ask: '), why) : null, box,
    h('p', { class: 'err', hidden: true }));
}

/** A list of plain strings (water filters). */
function stringList(path, title, why, itemName, placeholder) {
  return list({
    path, title, why, itemName, make: () => '', max: 20,
    item: (ip) => [q({ kind: 'text', path: ip, label: `${itemName} (brand or type)`, maxlength: 60, placeholder })],
  });
}

// ---- the steps -------------------------------------------------------------------------------
export const STEPS = [
  {
    id: 'access', title: 'Access and privacy', short: 'Access',
    intro: 'This page asks about your household so it can make your binder: one file you keep on your phone and laptop. There are nine short steps. Skip anything you do not know; the binder then prints a blank line to fill in by hand, never a guess.',
    render: () => [
      noticeFull(NOTICE.privateCopy, 'private-copy'),
      noticeFull(NOTICE.whatItIs, 'what-it-is'),
      q({ kind: 'password', path: P('access', 'access_key'), label: 'Your access key', required: true, maxlength: 128,
        why: 'The key shows the relay that the owner invited you. It is checked, then forgotten. This page never stores it.',
        autocomplete: 'off', reveal: env.revealKey,
        after: [
          h('button', { type: 'button', class: 'btn small ghost', 'aria-pressed': env.revealKey ? 'true' : 'false',
            onclick: () => { env.revealKey = !env.revealKey; env.rerender({ focus: idOf(['access', 'access_key']) }); } }, env.revealKey ? 'Hide' : 'Show'),
        ] }),
      env.keyCheckUI(),
      q({ kind: 'check', path: P('access', 'acknowledged_notice'), label: 'The notice', required: true,
        text: 'I have read the notice: my answers are never stored, and the finished file is for my household only.',
        why: 'So you know, before you type anything, where your answers go and that your finished file is for your household only.' }),
      q({ kind: 'check', path: P('access', 'save_profile_locally'), label: 'A file of your answers', falseWhenOff: true,
        text: 'At the end, offer me a file of my answers (profile.json) to keep on this device.',
        why: 'With that file you can come back to change answers, rebuild your binder, or upgrade from Small to Large, without typing it all again. The file stays with you.' }),
      env.keepToggleUI(),
    ],
  },
  {
    id: 'home', title: 'Home base', short: 'Home',
    intro: 'Where you live decides your weather, your hazards, your plants, your radio frequencies and your state\'s emergency contacts. We ask for the county, not your street.',
    render: () => [
      q({ kind: 'select', path: P('home', 'state'), label: 'State', required: true, options: stateOptions, rerender: true,
        then: clearCountyIfStale(P('home', 'county')), emptyLabel: 'Choose your state…',
        why: 'Your state\'s weather, hazards, plants and emergency contacts go to the front. Every state stays in the back of the binder in case you have to travel.' }),
      countyPicker(P('home', 'state'), P('home', 'county'), {
        why: 'Your county sets your weather-radio code, your weather office, your growing zone and your climate. We never ask for your street.' }),
      q({ kind: 'text', path: P('home', 'nearest_town'), label: 'Nearest town', maxlength: 64,
        why: 'Used only in sentences such as "the drive from your town to the cabin". Leave it blank if you prefer.' }),
      q({ kind: 'radio', path: P('home', 'setting'), label: 'What kind of place is it?', required: true, options: E.setting,
        why: 'City, suburb or countryside changes the advice on water, security, light at night, scavenging and neighbours.' }),
      q({ kind: 'select', path: P('home', 'elevation_band'), label: 'Height above sea level', options: E.elevation, emptyLabel: 'Not sure (work it out from my county)',
        why: 'Height changes boiling and cooking times, how cold it gets and how well solar panels work.' }),
    ],
  },
  {
    id: 'dwelling', title: 'The dwelling', short: 'Home type',
    intro: 'Your house decides how you heat one room, where you shelter from a tornado, where fuel can live, and how you get water when the taps stop.',
    render: () => {
      const d = draft.dwelling || {};
      return [
        q({ kind: 'radio', path: P('dwelling', 'dwelling_type'), label: 'What do you live in?', required: true, options: E.dwelling,
          why: 'Apartments, mobile homes and houses get different advice on generators, fuel storage and shelter.' }),
        q({ kind: 'int', path: P('dwelling', 'stories'), label: 'Floors above ground (1 to 4)',
          why: 'Stairs and upper floors change where the warm room and the tornado shelter go.' }),
        q({ kind: 'select', path: P('dwelling', 'basement'), label: 'Basement', options: E.basement,
          why: 'A basement is often the best tornado and fallout shelter; a walkout basement (one wall at ground level) changes that advice.' }),
        q({ kind: 'yesno', path: P('dwelling', 'windowless_interior_room', 'present'), label: 'Is there an inside room with no windows?', rerender: true,
          why: 'An inside room with no windows, on the lowest floor, is where you shelter from a tornado.' }),
        d.windowless_interior_room?.present === true ? q({ kind: 'text', path: P('dwelling', 'windowless_interior_room', 'which'), label: 'Which room?', maxlength: 80,
          placeholder: 'For example: downstairs bathroom', why: 'So your family plan can name the room.' }) : null,
        q({ kind: 'radio', path: P('dwelling', 'water_supply'), label: 'Where does your water come from?', required: true, options: E.water,
          why: 'How you get water when the taps stop depends on where it comes from now. A well adds the well-pump pages.' }),
        q({ kind: 'radio', path: P('dwelling', 'sewer'), label: 'Where does your toilet drain?', required: true, options: E.sewer,
          why: 'A septic tank needs different care from a city sewer when power or water is out.' }),
        q({ kind: 'select', path: P('dwelling', 'primary_heat'), label: 'Main heat', required: true, options: E.heat,
          why: 'Your heat source decides which fuel explainers and heater pages come first.' }),
        q({ kind: 'select', path: P('dwelling', 'gas_service', 'kind'), label: 'Gas at the house', options: E.gas, rerender: true,
          why: 'The page on shutting off gas is put up front only if you have gas.' }),
        d.gas_service?.kind === 'propane-tank' ? q({ kind: 'int', path: P('dwelling', 'gas_service', 'tank_gallons'), label: 'Propane tank size', unit: 'gallons',
          why: 'Tank size tells the binder roughly how long your propane lasts. It is printed on the tank\'s plate.' }) : null,
        q({ kind: 'select', path: P('dwelling', 'cooking_fuel'), label: 'What your stove runs on', options: E.cooking,
          why: 'Tells the binder whether your stove still works in a power cut.' }),
        q({ kind: 'select', path: P('dwelling', 'water_heater', 'kind'), label: 'Water heater', options: E.waterHeater, rerender: true,
          why: 'A tank water heater holds 40 to 50 gallons of drinkable water; the binder shows how to get it out.' }),
        ['tank-gas', 'tank-electric'].includes(d.water_heater?.kind) ? q({ kind: 'int', path: P('dwelling', 'water_heater', 'gallons'), label: 'Tank size', unit: 'gallons',
          why: 'Printed on the label on the tank. It goes into your water math.' }) : null,
        q({ kind: 'multi', path: P('dwelling', 'fire_features'), label: 'Fireplaces and fire pits (tick any)', options: E.fire,
          why: 'Changes the pages on cooking and keeping warm with fire.' }),
        q({ kind: 'select', path: P('dwelling', 'pool_or_hot_tub', 'kind'), label: 'Pool or hot tub', options: E.pool, rerender: true,
          why: 'A pool or hot tub is a large store of water for washing and, with treatment, drinking.' }),
        d.pool_or_hot_tub?.kind && d.pool_or_hot_tub.kind !== 'none' ? q({ kind: 'int', path: P('dwelling', 'pool_or_hot_tub', 'gallons'), label: 'About how many gallons?', unit: 'gallons',
          why: 'Goes into your water math. A guess is fine.' }) : null,
        q({ kind: 'select', path: P('dwelling', 'garden_space'), label: 'Space to grow food', options: E.garden,
          why: 'Decides how much of the food-growing section applies to you.' }),
        q({ kind: 'yesno', path: P('dwelling', 'attached_garage'), label: 'Is there a garage attached to the house?',
          why: 'Fuel kept in an attached garage is a fire risk next to where you sleep. The fuel-storage decision card appears only if you have one.' }),
        list({ path: P('dwelling', 'vehicles'), title: 'Vehicles', itemName: 'Vehicle', max: 6,
          why: 'Your vehicles decide the fuel, route and leaving-home pages; an electric car changes the power pages.',
          make: () => ({}),
          item: (ip) => [
            q({ kind: 'select', path: [...ip, 'type'], label: 'Type', required: true, options: E.vehicleType, why: 'Size and type decide what you can carry.' }),
            q({ kind: 'select', path: [...ip, 'fuel'], label: 'Fuel', required: true, options: E.vehicleFuel, why: 'Decides the fuel pages and how far you can go without a filling station.' }),
            q({ kind: 'check', path: [...ip, 'four_wheel_drive'], label: 'Four-wheel drive', text: 'It has four-wheel or all-wheel drive', why: 'Snow, mud and back roads.' }),
            q({ kind: 'check', path: [...ip, 'can_tow'], label: 'Towing', text: 'It can tow a trailer', why: 'Towing changes how much you can take if you leave.' }),
          ] }),
        q({ kind: 'select', path: P('dwelling', 'trailer'), label: 'Trailer', options: E.trailer,
          why: 'A trailer changes how much you can carry if you leave.' }),
      ];
    },
  },
  {
    id: 'members', title: 'Household members', short: 'People',
    intro: 'Ages and weights decide water and calorie math, children\'s warmth and clothing, infant feeding, and which published medical tables apply. Weights are used only to pick a row in a published table; the binder never works out a dose.',
    render: () => [
      list({ path: P('members'), title: 'Who lives here', itemName: 'Person', min: 1, max: 12, required: true,
        why: 'Everyone counted here is counted in the water, food and warmth plans.', addLabel: 'Add a person',
        make: newMember, itemTitle: (m) => (m.label ? ` · ${m.label}` : ''),
        item: (ip) => memberFields(ip) }),
    ],
  },
  {
    id: 'animals', title: 'Pets and livestock', short: 'Animals',
    intro: 'Animals need water, food and medicine in the plan too. Leave these empty if you have none.',
    render: () => [
      list({ path: P('pets'), title: 'Pets', itemName: 'Pet', max: 10, addLabel: 'Add pets',
        why: 'Pets need water, food and medicine in the plan, and a decision ahead of time about hard choices (card DC-10).',
        make: () => ({ count: 1 }),
        item: (ip) => [
          q({ kind: 'select', path: [...ip, 'type'], label: 'Kind', required: true, options: E.petType, why: 'Dogs and cats get their own care notes.' }),
          q({ kind: 'int', path: [...ip, 'count'], label: 'How many', required: true, why: 'Multiplies food and water.' }),
          q({ kind: 'text', path: [...ip, 'medications'], label: 'Their medicines', maxlength: 200, why: 'Printed on the pet page so they are not forgotten when you pack.' }),
          q({ kind: 'text', path: [...ip, 'food_per_day'], label: 'Food per day', maxlength: 80, placeholder: 'For example: 2 cups dry food', why: 'Used for the food you need to store for them.' }),
        ] }),
      list({ path: P('livestock'), title: 'Livestock', itemName: 'Animal group', max: 10, addLabel: 'Add livestock',
        why: 'Farm animals move the animal-care pages forward and add feed and water to the math.',
        make: () => ({ count: 1 }),
        item: (ip) => [
          q({ kind: 'select', path: [...ip, 'type'], label: 'Kind', required: true, options: E.livestock, why: 'Each kind has its own feed, water and shelter needs.' }),
          q({ kind: 'int', path: [...ip, 'count'], label: 'How many', required: true, why: 'Multiplies feed and water.' }),
        ] }),
    ],
  },
  {
    id: 'destinations', title: 'Destinations and routes', short: 'Places to go',
    intro: 'If you ever have to leave, the binder should already know where you would go, how far it is, and whether anyone is expecting you. Up to three places. Leave this empty if you have none yet.',
    render: () => [
      list({ path: P('destinations'), title: 'Places you would go', itemName: 'Destination', max: 3, addLabel: 'Add a place',
        why: 'Each place gets its own page with that area\'s plants, hazards and climate.',
        make: () => ({}), itemTitle: (d) => (d.name ? ` · ${d.name}` : ''),
        item: (ip) => {
          return [
            q({ kind: 'text', path: [...ip, 'name'], label: 'What you call it', required: true, maxlength: 60, placeholder: 'For example: Dad\'s farm, the cabin',
              why: 'The name your family uses, so the page reads naturally.' }),
            q({ kind: 'select', path: [...ip, 'state'], label: 'State', required: true, options: stateOptions, rerender: true,
              then: clearCountyIfStale([...ip, 'county']), why: 'Brings that state\'s region pages into a destination appendix.' }),
            countyPicker([...ip, 'state'], [...ip, 'county'], { why: 'Brings that county\'s plants, hazards and climate into the destination page. No street address.' }),
            q({ kind: 'radio', path: [...ip, 'status'], label: 'Do they know you might come?', required: true, options: E.destStatus,
              why: 'Printed plainly on the page, so nobody is surprised on the day.' }),
            q({ kind: 'textarea', path: [...ip, 'who_is_there'], label: 'Who is there', maxlength: 300, why: 'So the page says who to expect.' }),
            q({ kind: 'textarea', path: [...ip, 'how_to_reach_them'], label: 'How to reach them', maxlength: 300, placeholder: 'Phone, radio, letter',
              why: 'Printed as you type it. We do not look up or check any number.' }),
            q({ kind: 'textarea', path: [...ip, 'route_notes'], label: 'Route notes', maxlength: 1000, rows: 4, placeholder: 'Roads you prefer, bridges to avoid, fuel stops',
              why: 'Printed on the route page. The binder adds the hazards for each county on the way; it does not plan a driving route.' }),
            q({ kind: 'int', path: [...ip, 'approximate_miles'], label: 'About how far', unit: 'miles',
              why: 'Your own estimate. Used for fuel and travel-days math.' }),
          ];
        } }),
    ],
  },
  {
    id: 'contacts', title: 'Contacts and meeting places', short: 'Contacts',
    intro: 'Phones may not work. Writing these down now means everyone knows who to call and where to meet.',
    render: () => [
      group('Out-of-area contact', 'Long-distance calls and texts often get through when local ones do not. Everyone in the family calls this one person to report in.',
        contactFields(P('contacts', 'out_of_area_contact'))),
      q({ kind: 'textarea', path: P('contacts', 'meeting_place_near_home'), label: 'Meeting place near home', maxlength: 200, rows: 2,
        placeholder: 'For example: the big oak at the end of the street', why: 'Where everyone goes if you cannot get into the house, for example after a fire.' }),
      q({ kind: 'textarea', path: P('contacts', 'meeting_place_in_town'), label: 'Meeting place in town', maxlength: 200, rows: 2,
        why: 'Where everyone goes if you cannot get home.' }),
      q({ kind: 'textarea', path: P('contacts', 'meeting_place_out_of_town'), label: 'Meeting place out of town', maxlength: 200, rows: 2,
        why: 'Where everyone goes if the whole area has to leave. Often your first destination.' }),
      group('Utilities', 'Copy these from your own bills. We do not look them up, because a looked-up number can be wrong for your address.',
        ['electric', 'gas', 'water'].map(u => h('div', { class: 'subgroup' },
          h('h4', {}, { electric: 'Electric', gas: 'Gas', water: 'Water' }[u]),
          q({ kind: 'text', path: P('contacts', 'utilities', u, 'provider'), label: 'Company name', maxlength: 80, why: 'Printed on your outage page.' }),
          q({ kind: 'tel', path: P('contacts', 'utilities', u, 'outage_phone'), label: 'Outage phone number', maxlength: 30, why: 'The number to report an outage or a leak.' })))),
      list({ path: P('contacts', 'local_contacts'), title: 'Local contacts', itemName: 'Contact', max: 20, addLabel: 'Add a contact',
        why: 'Doctor, vet, pharmacy, neighbours: the people you would call first. Printed on the family plan.',
        make: () => ({}), itemTitle: (c) => (c.name ? ` · ${c.name}` : ''),
        item: (ip) => contactFields(ip) }),
    ],
  },
  {
    id: 'gear', title: 'Gear you own', short: 'Gear',
    intro: 'Tick what you already have. For each item the binder adds the matching pages, written for that kind of gear, with a spec row for your model if we know it and a blank row to fill in from the label if we do not. Skip anything you do not have.',
    render: () => gearFields(),
  },
  {
    id: 'decisions', title: 'Experience and decision cards', short: 'Decisions',
    intro: 'Last questions. Some choices carry real risk and only you can make them. Each card explains the danger and the choices in plain words. You can leave any card undecided and decide on paper later.',
    render: () => [
      q({ kind: 'radio', path: P('experience'), label: 'How much of this have you done before?', required: true, options: E.experience,
        why: 'New households get every explainer at the front of the binder; experienced ones get them at the back.' }),
      decisionCards(),
      q({ kind: 'textarea', path: P('notes_for_the_binder'), label: 'Anything else for your family plan page', maxlength: 2000, rows: 4,
        why: 'Printed on your family plan page as you write it. Do not type passwords, account numbers or where valuables are.' }),
    ],
  },
];

function noticeFull(n, cls) {
  return h('section', { class: 'notice ' + cls, 'aria-label': n.title },
    h('h2', { class: 'notice-title' }, n.title), n.paragraphs.map(p => h('p', { html: p })));
}
export { noticeFull };

function contactFields(base) {
  return [
    q({ kind: 'text', path: [...base, 'name'], label: 'Name', maxlength: 80, why: 'Printed on the family plan page.' }),
    q({ kind: 'text', path: [...base, 'relationship'], label: 'Who they are to you', maxlength: 60, placeholder: 'For example: sister, family doctor', why: 'So anyone reading the page knows who this is.' }),
    q({ kind: 'tel', path: [...base, 'phone'], label: 'Phone', maxlength: 30, why: 'Printed as you type it; we do not check it.' }),
    q({ kind: 'text', path: [...base, 'notes'], label: 'Notes', maxlength: 200, why: 'Anything that helps, such as the best time to call.' }),
  ];
}

function memberFields(ip) {
  const m = getAt(ip) || {};
  const conds = Array.isArray(m.conditions) ? m.conditions : [];
  const unitSel = h('select', { 'aria-label': 'Age in', id: idOf([...ip, 'age', 'unit']),
    onchange: (e) => setAt([...ip, 'age', 'unit'], e.target.value) },
  E.ageUnit.map(([v, l]) => h('option', { value: v, selected: (m.age?.unit || 'years') === v || undefined }, l)));
  const wUnitSel = h('select', { 'aria-label': 'Weight in', id: idOf([...ip, 'weight', 'unit']),
    onchange: (e) => setAt([...ip, 'weight', 'unit'], e.target.value) },
  E.weightUnit.map(([v, l]) => h('option', { value: v, selected: (m.weight?.unit || 'lb') === v || undefined }, l)));
  const ageQ = q({ kind: 'int', path: [...ip, 'age', 'value'], alsoPaths: [[...ip, 'age']], label: 'Age', required: true,
    why: 'Ages pick the right row in published water, food and medical tables. Use months for a child under 2.' });
  wrapRow(ageQ.querySelector('input'), unitSel);
  const wQ = q({ kind: 'number', path: [...ip, 'weight', 'value'], alsoPaths: [[...ip, 'weight']], label: 'Weight',
    why: 'Used only to pick a row in a published table, such as the epinephrine or potassium iodide table. The binder never works out a dose. Optional for adults; please give it for children.' });
  wrapRow(wQ.querySelector('input'), wUnitSel);
  return [
    q({ kind: 'text', path: [...ip, 'label'], label: 'First name or nickname', required: true, maxlength: 40,
      why: 'Names appear in the binder so pages can say who needs what. A nickname is fine.' }),
    q({ kind: 'radio', path: [...ip, 'role'], label: 'Age group', required: true, options: E.role, rerender: true,
      then: (role) => { if (role === 'infant-toddler' && m.age && m.age.value === undefined) m.age.unit = 'months'; },
      why: 'Adults, children, infants and elders need different water, food, warmth and care.' }),
    ageQ, wQ,
    q({ kind: 'select', path: [...ip, 'sex'], label: 'Sex', options: E.sex, rerender: true,
      why: 'Only used to put the pregnancy and menstrual pages near the front.' }),
    showsPregnancy(m) ? q({ kind: 'select', path: [...ip, 'pregnant_or_nursing'], label: 'Pregnant or nursing?', options: E.pregnant,
      why: 'Adds water and food allowances and the infant-feeding pages.' }) : null,
    h('details', { class: 'more', open: (conds.length || m.conditions_other) ? true : undefined },
      h('summary', {}, `Medical conditions${conds.length ? ` (${conds.length} ticked)` : ''}`),
      q({ kind: 'multi', path: [...ip, 'conditions'], label: 'Tick any that apply', options: CONDITIONS.map(([id, n]) => ({ value: id, label: n })),
        why: 'Each condition you tick moves its pages to the front of the medical section. Every condition stays in the binder either way.' }),
      q({ kind: 'text', path: [...ip, 'conditions_other'], label: 'Something not in the list', maxlength: 200,
        why: 'The binder adds a page on managing a condition that is not in its library.' })),
    list({ path: [...ip, 'medications'], title: 'Medicines', itemName: 'Medicine', max: 30, addLabel: 'Add a medicine',
      why: 'Fills the "my meds" table. We print what you type. Nothing is interpreted, except whether it needs a fridge.',
      make: () => ({}), itemTitle: (x) => (x.name ? ` · ${x.name}` : ''),
      item: (mp) => [
        q({ kind: 'text', path: [...mp, 'name'], label: 'Name', required: true, maxlength: 80, why: 'As it is written on the bottle or box.' }),
        q({ kind: 'text', path: [...mp, 'strength'], label: 'Strength', maxlength: 40, placeholder: 'For example: 10 mg', why: 'From the label, so the right box is packed.' }),
        q({ kind: 'text', path: [...mp, 'schedule'], label: 'How often', maxlength: 80, placeholder: 'For example: once a day', why: 'From the label. Printed as written.' }),
        q({ kind: 'yesno', path: [...mp, 'refrigerated'], label: 'Kept in the fridge?', why: 'Fridge medicines get the cooling and power pages.' }),
        q({ kind: 'textarea', path: [...mp, 'if_missed'], label: 'What happens if doses are missed', maxlength: 300,
          why: 'In your own words, from your prescriber or the label. Printed exactly as written.' }),
      ] }),
    list({ path: [...ip, 'allergies'], title: 'Allergies', itemName: 'Allergy', max: 20, addLabel: 'Add an allergy',
      why: 'Drives the allergy and anaphylaxis pages and the food plan.',
      make: () => ({}), itemTitle: (x) => (x.allergen ? ` · ${x.allergen}` : ''),
      item: (ap) => [
        q({ kind: 'text', path: [...ap, 'allergen'], label: 'Allergic to', required: true, maxlength: 60, why: 'Printed on the allergy page and the food plan.' }),
        q({ kind: 'radio', path: [...ap, 'severity'], label: 'How bad is the reaction?', required: true, options: E.severity,
          why: 'Anaphylaxis (throat or breathing trouble) brings the emergency pages forward.' }),
        q({ kind: 'yesno', path: [...ap, 'carries_epinephrine'], label: 'Carries an epinephrine auto-injector?', why: 'Adds the storage and expiry pages for it.' }),
      ] }),
    q({ kind: 'multi', path: [...ip, 'mobility_or_sensory'], label: 'Aids and devices (tick any)', options: E.mobility, exclusive: 'none',
      why: 'Changes the power, device and leaving-home pages, for example power for oxygen or a CPAP.' }),
    q({ kind: 'multi', path: [...ip, 'skills'], label: 'Skills (tick any)', options: E.skills, exclusive: 'none', rerender: true,
      why: 'Fills the household roles table and decides how much the explanations assume.' }),
    (m.skills || []).includes('ham-licence') ? q({ kind: 'text', path: [...ip, 'ham_callsign'], label: 'Ham callsign', maxlength: 8, autocapitalize: 'characters',
      placeholder: 'For example: KD0ABC', why: 'Printed on the radio pages so it is at hand.' }) : null,
  ];
}
function wrapRow(input, extra) {
  if (input.parentNode && input.parentNode.classList && input.parentNode.classList.contains('row')) { input.parentNode.append(extra); return; }
  const row = h('div', { class: 'row' });
  input.replaceWith(row);
  row.append(input, extra);
}

function gearFields() {
  const g = draft.gear || {};
  return [
    group('Power', 'Your power gear decides which power pages you get and fills your power budget.',
      list({ path: P('gear', 'power_stations'), title: 'Power stations (big rechargeable batteries)', itemName: 'Power station', max: 10,
        why: 'Battery size (Wh) sets how long you can run a fridge, a CPAP or lights.', make: () => ({}),
        item: (ip) => [
          q({ kind: 'text', path: [...ip, 'model'], label: 'Model', maxlength: 60, why: 'If we know the model, the binder prints its specs.' }),
          q({ kind: 'number', path: [...ip, 'wh'], label: 'Capacity', unit: 'Wh', why: 'On the label. Leave blank if unsure; the binder prints a blank row.' }),
        ] }),
      list({ path: P('gear', 'solar_panels'), title: 'Solar panels', itemName: 'Panel type', max: 10, make: () => ({ count: 1 }),
        why: 'Panel watts and count set how much you can recharge each day.',
        item: (ip) => [
          q({ kind: 'text', path: [...ip, 'model'], label: 'Model', maxlength: 60, why: 'If we know the model, the binder prints its specs.' }),
          q({ kind: 'number', path: [...ip, 'watts'], label: 'Watts each', unit: 'W', why: 'On the label on the back of the panel.' }),
          q({ kind: 'int', path: [...ip, 'count'], label: 'How many', why: 'Multiplies the watts.' }),
        ] }),
      generatorToggle(),
      ui.hasGenerator ? h('div', { class: 'subgroup' },
        q({ kind: 'select', path: P('gear', 'generator', 'fuel'), label: 'Generator fuel', options: E.genFuel, why: 'Decides the fuel storage and run-time pages.' }),
        q({ kind: 'yesno', path: P('gear', 'generator', 'inverter'), label: 'Is it an inverter generator?', why: 'Inverter generators are quieter and safe for electronics.' }),
        q({ kind: 'number', path: P('gear', 'generator', 'watts'), label: 'Running watts', unit: 'W', why: 'On the label. Sets what it can power at once.' }),
        q({ kind: 'text', path: P('gear', 'generator', 'model'), label: 'Model', maxlength: 60, why: 'If we know the model, the binder prints its specs.' })) : null,
      q({ kind: 'select', path: P('gear', 'house_connection'), label: 'How a generator connects to the house', options: E.houseConn,
        why: 'Connecting a generator to house wiring the wrong way can kill a line worker. The binder explains the safe ways.' }),
      q({ kind: 'check', path: P('gear', 'car_inverter'), label: 'Car inverter', text: 'We have an inverter that plugs into a car', why: 'A car can charge phones and small devices in an outage.' })),
    group('Heat', 'Each heater has its own safety rules; the binder includes the pages for yours.',
      list({ path: P('gear', 'heaters'), title: 'Heaters you own', itemName: 'Heater', max: 10, make: () => ({}),
        why: 'Unvented heaters bring the carbon-monoxide pages and a decision card forward.',
        item: (ip) => [
          q({ kind: 'select', path: [...ip, 'kind'], label: 'Kind', required: true, options: E.heaterKind, why: 'Each kind has its own safety pages.' }),
          q({ kind: 'text', path: [...ip, 'model'], label: 'Model', maxlength: 60, why: 'If we know the model, the binder prints its specs.' }),
        ] })),
    group('Fuel on hand', 'Fuel amounts set how many days of heat, cooking and power you have. Rough numbers are fine; leave blank for none.',
      h('div', { class: 'grid2' },
        q({ kind: 'number', path: P('gear', 'fuel_on_hand', 'gasoline_gal'), label: 'Gasoline', unit: 'gal', why: 'Generator and vehicle days.' }),
        q({ kind: 'number', path: P('gear', 'fuel_on_hand', 'diesel_gal'), label: 'Diesel', unit: 'gal', why: 'Vehicle and heater days.' }),
        q({ kind: 'number', path: P('gear', 'fuel_on_hand', 'kerosene_gal'), label: 'Kerosene', unit: 'gal', why: 'Heater days.' }),
        q({ kind: 'int', path: P('gear', 'fuel_on_hand', 'propane_1lb'), label: 'Propane, 1-lb cylinders', unit: 'count', why: 'Camp stove and heater hours.' }),
        q({ kind: 'int', path: P('gear', 'fuel_on_hand', 'propane_20lb'), label: 'Propane, 20-lb tanks', unit: 'count', why: 'Grill-size tanks: cooking and heat days.' }),
        q({ kind: 'number', path: P('gear', 'fuel_on_hand', 'propane_bulk_gal'), label: 'Propane, big tank', unit: 'gal', why: 'How full your house tank usually is.' }),
        q({ kind: 'number', path: P('gear', 'fuel_on_hand', 'firewood_cords'), label: 'Firewood', unit: 'cords', why: 'Wood heat days.' }),
        q({ kind: 'number', path: P('gear', 'fuel_on_hand', 'charcoal_lb'), label: 'Charcoal', unit: 'lb', why: 'Outdoor cooking days.' }),
        q({ kind: 'number', path: P('gear', 'fuel_on_hand', 'lamp_oil_gal'), label: 'Lamp oil', unit: 'gal', why: 'Lamp hours.' }))),
    group('Water', 'Stored water and ways to clean it decide your water plan.',
      q({ kind: 'number', path: P('gear', 'water', 'stored_gal'), label: 'Stored water', unit: 'gal', why: 'Days of drinking water for your household.' }),
      stringList(P('gear', 'water', 'filters'), 'Water filters', 'The binder prints the care and limits for each kind.', 'Filter', 'For example: gravity filter, straw filter'),
      q({ kind: 'check', path: P('gear', 'water', 'bleach_or_shock'), label: 'Bleach or pool shock', text: 'We have unscented bleach or pool shock', why: 'Both can make water safe to drink when used as the page says.' }),
      q({ kind: 'int', path: P('gear', 'water', 'barrels'), label: 'Water barrels', unit: 'count', why: 'Storage you can refill.' })),
    group('Cooking', null,
      q({ kind: 'multi', path: P('gear', 'cooking'), label: 'Ways to cook without the kitchen stove', options: E.cookGear, columns: true,
        why: 'Each gets its own safe-use page; some must never be used indoors.' })),
    boolChecks(P('gear', 'comms'), 'Radios and messaging', 'When phones go down these are how you hear warnings and reach family. The radio pages are written for what you own.', E.comms),
    group('Safety', 'Alarms and extinguishers are the first line against fire and carbon monoxide, which rise in every outage.',
      q({ kind: 'select', path: P('gear', 'safety', 'first_aid_tier'), label: 'First-aid kit', options: E.firstAid, why: 'Sets which first-aid pages assume you have supplies.' }),
      h('div', { class: 'grid2' },
        q({ kind: 'int', path: P('gear', 'safety', 'co_alarms'), label: 'Carbon monoxide alarms', unit: 'count', why: 'One per sleeping area is the usual advice.' }),
        q({ kind: 'int', path: P('gear', 'safety', 'smoke_alarms'), label: 'Smoke alarms', unit: 'count', why: 'Checked against your floors.' }),
        q({ kind: 'int', path: P('gear', 'safety', 'extinguishers'), label: 'Fire extinguishers', unit: 'count', why: 'Where they are goes on your family plan.' }),
        q({ kind: 'int', path: P('gear', 'safety', 'fire_blankets'), label: 'Fire blankets', unit: 'count', why: 'For kitchen and clothing fires.' }))),
    group('Security', 'The firearms pages are in every binder. Only the inventory and care pages depend on this. We never ask for serial numbers or where anything is kept.',
      q({ kind: 'yesno', path: P('gear', 'firearms', 'owned'), label: 'Does the household own firearms?', rerender: true,
        why: 'Adds the inventory and care pages, and the safe-storage rules around children.' }),
      g.firearms?.owned === true ? h('div', { class: 'subgroup' },
        q({ kind: 'textarea', path: P('gear', 'firearms', 'platforms_and_calibers'), label: 'Types and calibers', maxlength: 300, rows: 2,
          placeholder: 'For example: 12-gauge shotgun, .22 rifle', why: 'Fills the inventory and ammunition pages. No serial numbers.' }),
        q({ kind: 'yesno', path: P('gear', 'firearms', 'safe'), label: 'A gun safe?', why: 'Changes the storage advice.' }),
        q({ kind: 'yesno', path: P('gear', 'firearms', 'suppressors'), label: 'Suppressors?', why: 'Adds their care page.' })) : null),
    group('Food', 'Your food on hand sets how many days you can eat without a store.',
      h('div', { class: 'grid2' },
        q({ kind: 'int', path: P('gear', 'food', 'pantry_days'), label: 'Pantry food', unit: 'days', why: 'Rough days of shelf-stable food for everyone.' }),
        q({ kind: 'number', path: P('gear', 'food', 'bulk_staples_lb'), label: 'Bulk staples (rice, beans, flour)', unit: 'lb', why: 'Long-term calories.' }),
        q({ kind: 'int', path: P('gear', 'food', 'freeze_dried_servings'), label: 'Freeze-dried food', unit: 'servings', why: 'Adds the water you need to make it.' })),
      q({ kind: 'multi', path: P('gear', 'food', 'canning'), label: 'Canning equipment', options: E.canning,
        why: 'Pressure canners are the only safe way to can low-acid food; the gauge type changes the steps.' }),
      q({ kind: 'check', path: P('gear', 'food', 'dehydrator'), label: 'Dehydrator', text: 'We have a food dehydrator', why: 'Adds the drying pages.' }),
      q({ kind: 'check', path: P('gear', 'food', 'seeds'), label: 'Seeds', text: 'We have garden seeds stored', why: 'Adds the seed-saving and planting pages.' })),
    group('Getting around', null,
      q({ kind: 'multi', path: P('gear', 'transport'), label: 'Ways to move without fuel', options: E.transport,
        why: 'Changes the travel and carrying pages if vehicles cannot be used.' })),
  ];
}

/** UI-only answer (not in the profile): whether the generator questions apply. */
function generatorToggle() {
  const id = 'f-has-generator';
  return h('fieldset', { class: 'q', dataset: { paths: '/gear/generator' } },
    h('legend', { class: 'q-label' }, 'Generator'),
    h('p', { class: 'why', id: id + '-why' }, h('span', { class: 'why-tag' }, 'Why we ask: '), 'Adds the generator pages, including the rules that keep its exhaust from killing anyone.'),
    h('label', { class: 'choice single', for: id },
      h('input', { type: 'checkbox', id, checked: ui.hasGenerator || undefined, 'aria-describedby': id + '-why',
        onchange: (e) => { ui.hasGenerator = e.target.checked; env.rerender({ focus: id }); } }),
      h('span', { class: 'choice-text' }, 'We have a generator')),
    h('p', { class: 'err', hidden: true }));
}

// ---- decision cards --------------------------------------------------------------------------
function decisionCards() {
  const ks = env.kitState;
  const garage = draft.dwelling?.attached_garage === true;
  const intro = h('div', { class: 'q' },
    h('h3', { class: 'q-label', id: 'cards-title' }, 'Decision cards'),
    h('p', { class: 'why' }, h('span', { class: 'why-tag' }, 'Why we ask: '),
      'Each card is a trade-off between safety and getting by. We print your choice on the card, and every other page that touches it points to it. "Undecided" prints the card open with a box to decide on paper.'));
  if (ks.loading) return [intro, h('p', { class: 'muted', role: 'status' }, 'Loading the decision cards…')];
  if (!ks.cards.length) return [intro, h('p', { class: 'warn' }, 'The decision cards could not be loaded. Every card will be printed open, so you can decide on paper.')];
  const shown = ks.cards.filter(c => c.card !== 'DC-05' || garage);
  return [intro,
    ks.source === 'fixture' ? h('p', { class: 'muted small' }, 'These are short summaries of the cards. The full card, with the reasons and the safer steps, is printed in your binder.') : null,
    shown.map(c => {
      const path = ['decision_cards', c.card];
      const titleId = idOf(path, 'title');
      if (!c.options.length) {
        return h('section', { class: 'card worksheet', 'aria-labelledby': titleId },
          h('h4', { id: titleId }, h('span', { class: 'card-id' }, c.card), ' ', c.title),
          h('p', {}, c.settings_summary));
      }
      const node = q({ kind: 'radio', path, label: '', options: [
        ...c.options.map(o => ({ value: o.id, label: o.label, hint: o.summary })),
        { value: 'undecided', label: 'Undecided', hint: 'Print the card open so we can decide on paper.' }] });
      // the default answer is "undecided"
      if (!getAt(path)) node.querySelector(`input[value="undecided"]`).checked = true;
      const legend = node.querySelector('legend');
      legend.textContent = '';
      legend.append(h('span', { class: 'card-id' }, c.card), ' ', c.title);
      legend.after(h('p', { class: 'card-summary' }, c.settings_summary));
      node.classList.add('card');
      return node;
    }),
    garage ? null : h('p', { class: 'muted small' }, 'Card DC-05 (fuel in an attached garage) is not shown because you said there is no attached garage. It will be printed open in your binder.'),
  ];
}

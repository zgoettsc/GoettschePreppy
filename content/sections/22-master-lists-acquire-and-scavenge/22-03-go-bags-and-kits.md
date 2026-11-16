---
id: 22-03-go-bags-and-kits
section: 22-master-lists-acquire-and-scavenge
title: "Go-bags and kits, one per person"
version: 1
revised: 2026-11-16
layer: household
danger_level: critical
phase: [A, B, C]
tags: [go-bag, evacuation, kits, per person, children, infants, elders, medical, EDC]
derived_from: [22-03-go-bags-and-kits]
sources:
  - us-fda-information-regarding-insulin-storage-and-swi-6448d3
  - cdc-how-to-create-and-store-an-emergency-water-suppl-f0c412
  - cdc-recognizing-and-responding-to-anaphylaxis-645825
  - american-red-cross-winter-storm-preparedness-and-bli-4bb6c0
  - us-epa-emergency-disinfection-of-drinking-water-6aa91f
  - usa-gov-replace-your-vital-documents-cde79b
  - ready-gov-build-a-kit
  - cdc-infant-formula-preparation-and-storage-29a24f
  - ready-gov-fema-pets-and-animals
related: [22-06-kit-medical, 22-05-kit-vehicle, 22-01-master-acquisition-list, 01-02-go-no-go-decision, 01-03-phase-b-movement, 01-06-phase-transition-checklists, 01-07-evacuating-with-medical-needs, 19-01-document-grab-kit, 25-08-quick-reference-cards, 24-02-drills, 20-09-pets, 20-05-infant-feeding]
cards: [DC-04, DC-08, DC-09, DC-10, DC-18]
explainers: [EX-07, EX-06]
promote_when: []
photo_slots:
  - { id: go-bags-spot, caption: "Where the go-bags live: by the exit we would actually use" }
figures: []
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: null
---

# Go-bags and kits, one per person

**What this page is for.** A go-bag is a packed bag, one per person, that lets you leave home in
minutes and get through about three days on what you carry (Ready.gov, Build A Kit). This page
builds one bag for each person in this household, from your settings, plus one shared bag for
the vehicle. The medical part of each bag comes from → 22-06 and is packed first.

> **SAFETY — CRITICAL.**
> - **Rescue medicines and daily medicines are packed first and checked most often.**
>   Everything else in a bag is negotiable; those are not. **Quantities come from your
>   prescriptions and your condition pages in Section 02, never from a list.**
> - **A frozen-then-thawed insulin vial or pen is discarded.** In cold weather, insulin and
>   other medicines that must not freeze ride inside the coat, against the body, not in the
>   pack (FDA, Insulin Storage in an Emergency; → 29-07).
> - **Children do not have access to firearms, fuel, medications or chlorine products.** A
>   child's bag holds no medicine; an adult carries it.

## Do this now

1. **Build the medical kit first** (→ 22-06). If the rest of the bag is perfect and the
   medicine is short, the bag has failed.
2. **Pack one bag per person** below ({{ household.size }} people), sized to who carries it,
   plus the shared household bag for the vehicle (→ 22-05).
{{#if has.epinephrine}}3. **Put an epinephrine pair in the allergic person's bag, in each adult's bag and in the
   house kit**, and check every expiry on the same day. The pair that counts travels **on a
   person**, not in a parked vehicle (→ 02-03).
{{else}}3. **Put every rescue medicine where the person who needs it will be**, not only in one bag
   (→ 22-06).
{{/if}}4. **Pick two check dates, six months apart** (for example when the clocks change), and
   write them here: ____________ and ____________. Rotate food and water, check batteries and
   expiry dates{{#if has.child}}, **re-size the children's clothing**{{/if}}, and walk the plan
   (→ 24-02).
5. **Store the bags where you can grab them in 60 seconds in the dark**, by the exit you
   would actually use.

{{photo go-bags-spot}}

## The four levels of kit

| Level | Covers | Where it lives | The question it answers |
|---|---|---|---|
| **1. Every day ("EDC", everyday carry)** | Right now | On your body | "It happened while I was out" |
| **2. Go-bag** | About 72 hours, on foot | By the door | "We have minutes to leave" |
| **3. Vehicle kit** | Days, with the car | In the vehicle, always | "We are stuck, or driving out" (→ 22-05) |
| **4. Household stores** | Weeks to months | The house | Sheltering in place (→ 01-01) |

**They nest.** Leaving with the go-bag means the vehicle kit is a bonus and the house is gone.
Never plan to fill Level 2 from Level 4 on the way out: under stress you will forget, and
there may be no light.

## Level 1: what is on each body, every day

For most households Level 1 is a small light, a way to make fire, a whistle (→ 15-07) and the
wallet card set from → 25-08. **For anyone with a medical clock, Level 1 is medical:**

| Person | Conditions (from settings) | Allergies | On the body, always |
|---|---|---|---|
{{#each members as m}}| {{m.label}} | {{m.conditions}} | {{m.allergies}} | Rescue medicine if any · medical ID · ____________ |
{{/each}}

{{#if has.anaphylaxis}}**Allergy rule:** whichever adult is with the allergic person carries an **epinephrine pair**
on their body (not in the car, not in a bag on a hook), the person's allergen card, and the
plan from their prescriber (→ 02-03). A second dose is often needed (CDC, Recognizing and
Responding to Anaphylaxis).
{{/if}}{{#if has.condition.CL-01}}**Diabetes rule:** the person with diabetes carries fast sugar, their meter or sensor reader,
and medical ID (→ 02-01, → 02-02).
{{/if}}**The test:** if it is not on a body when the siren goes or the reaction starts in a parking
lot, it is not Level 1. Pockets and a belt pouch beat everything else.

## The one rule that decides everything else

**A go-bag you cannot carry is not a go-bag.**
{{#if has.child}}This household has {{ household.children }} children. Every small child who cannot walk far is
carried, and that uses most of an adult's carrying capacity before a single item goes in.
{{/if}}{{#if has.mobility_aid}}Someone here uses a wheelchair or walker: decide now who pushes, who carries their bag, and how
the chair travels (→ 02-22).
{{/if}}

- **Weigh each loaded bag and write the weight on its tag.**
- **Walk a mile with the loaded bags** before you believe any of this (→ 24-02). Then take
  things out.
- **Children carry a small bag of their own** (comfort item, a snack, a whistle) because
  carrying something helps a child in a crisis, not because it helps the load.

## One bag per person

Each table is the core bag. The add-ons for each age band follow; pack them into the same bag.

{{#each members as m}}

### Bag: {{m.label}} ({{m.role}}, {{m.age_text}})

| ✔ | Category | Contents |
|---|---|---|
| [ ] | **Medical (first)** | Conditions: {{m.conditions}}. Allergies: {{m.allergies}}. Medicines: {{m.meds}}. The matching modules from → 22-06, as one pouch (for anyone under 13, an adult carries it). Printed medicine list and the family medical summary (→ 25-09) |
| [ ] | **Water** | A bottle + a small filter + chemical treatment as a backup (→ 03-04). Planning figure is 1 gallon per person per day (CDC); the bag carries a day's drinking, the vehicle the rest |
| [ ] | **Food** | Three days of high-calorie food this person will actually eat, sealed, in original labelled packaging |
| [ ] | **Warmth** | Base layer, hat, gloves or mittens, spare socks, rain shell, emergency blanket or bivvy |
| [ ] | **Light and tools** | Headlamp + spare batteries, knife or multi-tool (adults), lighter + ferro rod, cordage, duct tape |
| [ ] | **Documents** | Copies of ID, insurance cards, prescription list (→ 19-01) |
| [ ] | **Comms** | Printed contacts and meeting places (→ 15-03), whistle, a charged phone and cable |
| [ ] | **Hygiene** | Toothbrush, small soap, hand sanitiser, toilet paper, any menstrual supplies (→ 13-08) |
| [ ] | **Personal** | Spare glasses, hearing-aid batteries, comfort item, ____________ |

Bag weight: ______ lb · Checked on: ____________
{{/each}}

### Add-on: every adult and elder

For: {{#each adults as a}}{{a.label}} · {{else}}no one listed{{/each}}

Between the adults, divide the **shared** load so the person with the heaviest medical load
carries mainly medical: the main water filter and a collapsible container, the bulk of the
shared food, **the trauma kit** (tourniquet, pressure dressings, wound-packing gauze; → 12-02),
a tarp and emergency blankets, a small stove, fuel and pot, a repair kit, **a second set of any
rescue medicine**, cash (→ 19-02), the document kit or drive (→ 19-03), and this binder on a
charged device or a printed set of the core pages (→ 00-02, → 01-03, → 25-08).

{{#if has.pregnant}}**Pregnancy (in this household):** prenatal vitamins, extra water and food, the prenatal
records, and the hospital-bag items from → 02-12.
{{/if}}{{#if has.nursing}}**Nursing (in this household):** extra water and food for the nursing parent; their supply is
the baby's supply (→ 02-13).
{{/if}}

### Add-on: teenagers (13 to 17)

For: {{#each teens as t}}{{t.label}} ({{t.age_text}}) · {{else}}no one in this age band right now{{/each}}

A teen carries close to an adult load and a real share of the shared kit: their own water
filter or tablets, a headlamp, a knife if the household allows it, and one shared item they are
responsible for. Give them their own copy of the contact card and the meeting places, and walk
them through the plan as an adult would be (→ 20-04).

### Add-on: children under 13

For: {{#each children as c}}{{c.label}} ({{c.age_text}}) · {{else}}no one in this age band right now{{/each}}

| ✔ | Category | Contents |
|---|---|---|
| [ ] | **Their own small bag** | The comfort item, a snack, a whistle on a cord. **No medicine in the child's bag**: an adult carries it |
| [ ] | **ID card** | A card with the family's names, a photo of the family, the out-of-area contact's number and the meeting place (→ 15-03) |
| [ ] | **Warmth** | A full change of clothes, hat, mittens (warmer than gloves for small hands), two pairs of socks{{#if is.cold_winters}}, snow gear in season{{/if}} |
| [ ] | **Comfort** | **The specific comfort item.** It is what keeps a small child moving (→ 20-08) |
| [ ] | **Occupation** | A small book, cards, crayons |
| [ ] | **Safe food** | Snacks they reliably eat{{#if has.anaphylaxis}}; for a child with a food allergy, only food in original labelled packaging (→ 02-04){{/if}} |

{{#if has.anaphylaxis}}**For a child with anaphylaxis:** the epinephrine pair rides with the adult who is with the
child, in an outside pocket, marked, never buried; the written plan from the prescriber,
laminated, so anyone (a stranger included) can act (→ 02-03). Antihistamine only as the plan
says: never instead of epinephrine, never first. Feeding unlabelled or traded food:
{{choice DC-18}} → 30-19.
{{/if}}

### Add-on: babies and toddlers under 2

For: {{#each infants as i}}{{i.label}} ({{i.age_text}}) · {{else}}no one in this age band right now{{/each}}

| ✔ | Category | Contents |
|---|---|---|
| [ ] | **Feeding** | Formula if used, **plus safe water and the means to prepare it cleanly** (CDC, Infant Formula Preparation and Storage); bottles; the foods they take (→ 02-13, → 20-05) |
| [ ] | **Diapers** | Three days at the **current size**, wipes, cream, bags, and cloth as the backup (→ 20-06) |
| [ ] | **Carrier** | **A carrier or child-carrier pack is a survival item.** They cannot walk out of anything |
| [ ] | **Warmth** | Snowsuit or bunting in season, hat, mittens, blanket, two spares of everything (small children get wet) |
| [ ] | **Medical** | Their own medicines and an infant fever reducer as their provider directed, carried by an adult; a thermometer |
| [ ] | **Comfort** | Pacifiers, the specific blanket or toy, a familiar cup |
| [ ] | **Sleep** | Something they will actually sleep on (→ 21-07). Bed-sharing for warmth: {{choice DC-09}} → 30-10 |

### Add-on: elders (over 70)

For: {{#each elders as e}}{{e.label}} ({{e.age_text}}) · {{else}}no one in this age band right now{{/each}}

Lighter bag, more medical. Spare glasses and hearing-aid batteries (→ 02-23), a written list of
every medicine with the prescriber's words, a pill organiser for three days, compression or
mobility aids, an extra warm layer (older bodies cool faster; → 08-05), and a folding seat if
long waits are likely. If memory is a concern, an ID bracelet and one named adult who stays
with them at every stop (→ 02-21).

{{#if has.pets}}
### Pets

{{#each pets as p}}- {{p.count}} {{p.type}}: food for three days ({{p.food_per_day}} a day), water, bowls, medicines ({{p.medications}}), leash or carrier, litter or waste bags, vaccination records and a photo (Ready.gov, Pets and Animals; → 20-09).
{{/each}}

Decide the pet plan **now**, not at the door. If it ever becomes impossible to keep them:
{{choice DC-10}} → 30-11.
{{/if}}

## The household bag (rides in the vehicle)

- Larger water containers and the second filter (→ 03-04)
- Extra food for several days, a stove and fuel
- The full first-aid kit (→ 12-01) beyond the trauma kit
- Tent or heavy tarp, sleeping bags rated for the season, ground pads
{{#if has.pets}}- Pet carriers, food, water bowls, litter (→ 20-09)
{{/if}}- Tools, cordage, tape, work gloves
- Paper maps and a compass (→ 25-04)
- **Cash**, documents, backup drive (→ 19-01)
- This binder on a second charged device (→ 00-10)

## The 60-second, 10-minute and 30-minute lists

Post these on the inside of a cupboard door (→ 01-06):

| You have | You take |
|---|---|
| **60 seconds** | People{{#if has.pets}}, pets{{/if}}, **medical kit**, go-bags, phones, keys, wallets |
| **10 minutes** | + document kit, water, food bin, sleeping bags, coats and boots for everyone, the binder device |
| **30 minutes** | + tools, stove and fuel, extra water, extra clothing, whatever else the vehicle holds (→ 22-05) |

**Practise the 60-second list with the family, timed, at least twice a year** (→ 24-02).

## Your climate changes the bag

Home county: {{ home.county }}, {{ home.state_name }} · January mean low {{ region.home.jan_low_f }} °F
· July mean high {{ region.home.jul_high_f }} °F.

{{#if is.cold_winters}}- **Winter matters here.** Boots, snow gear and hats live with the bags, not in a closet
  upstairs. Medicines that must not freeze ride inside a coat. Batteries lose capacity in cold:
  carry spares warm (→ 09-05). On foot in a blizzard with small children is rarely survivable;
  in winter the honest plan is often "get to the vehicle, or stay put" (American Red Cross,
  Winter Storm Safety; → 17-01, → 01-02).
{{else}}- **Cold snaps still happen.** Keep a warm layer and a hat in every bag all year.
{{/if}}{{#if is.hot_summers}}- **Heat matters here.** More water than you think, sun hat, light long sleeves, and
  medicines kept out of direct sun and parked cars (→ 29-07, → 17-04).
{{/if}}{{#if is.hurricane_region}}- **Hurricane country:** waterproof everything; dry bags for documents and medicine (→ 17-13).
{{/if}}{{#if is.wildfire_region}}- **Wildfire country:** N95 masks for every person, goggles, and a bag that is ready all
  season, because warnings can be short (→ 17-14).
{{/if}}{{#if is.flood_region}}- **Flood risk:** waterproof bags, and the bag goes up high with you (→ 17-03).
{{/if}}

## Maintenance: the part everyone skips

A go-bag is not a purchase; it is a **rotation**. On the two check dates:

1. **Every expiry date**: medicines, rescue devices, food, water treatment.
2. **Every battery**, including the ones inside devices.
3. **Children's clothing sizes**, the fastest-expiring item in the house.
4. **Weigh the bags.** They gain weight every year.
5. **Reprint the paper pages** (→ 19-01, → 25-09): phone numbers and prescriptions change.
6. Log it in → 22-04 and write the date on each bag's tag.

Medicine that was too hot in a parked car or a summer bag: {{choice DC-08}} → 30-09. Using
expired rescue medicine when nothing in date exists: {{choice DC-04}} → 30-05.

## Gear for the bags

| Item | Why |
|---|---|
| One pack per person, sized to the person carrying it | Fit matters more than brand |
{{#if has.young_child}}| **A child-carrier pack** | A small child is cargo |
{{/if}}| Insulated medicine pouch | Keeps medicine in range in both directions (→ 29-07) |
| Dry bags or heavy zip bags | Everything gets wet eventually |
| Water bottles, a small filter, treatment tablets | Two ways to make water safe (→ 03-04) |
| Emergency bivvies and wool layers | Cold is what kills people outdoors |
| A headlamp per person + batteries | Hands free |
| Laminated plans and contact cards | Anyone must be able to act |
| A luggage scale | Keeps the bags honest |

**If you do not have it:** any backpack works; fit and weight matter more. A wagon{{#if is.snow_region}}
or a sled{{/if}} beats a pack for hauling children and gear. Bedsheets make carriers and
bundles. **There is no substitute for insulin, epinephrine or any other daily or rescue
medicine.** Do not plan around finding them (→ 23-03).

## When it runs out

A go-bag lasts about three days by design. **After that, everything in it is spent**, which is
the whole point of → 01-02: leaving is only a plan if it ends somewhere.

- **How long:** three days of water and food. The medical module's clock is the real number,
  and it comes from your condition pages, not this one.
- **Ration:** water and warmth first. Anyone whose eating is medical (diabetes, a nursing
  parent, a small child) eats to their need, not to a share (→ 23-01).
- **Resupply:** the vehicle kit (→ 22-05), then a destination (→ 01-05).
- **The strategic point:** a go-bag buys **the time to reach somewhere**. If there is no
  somewhere, better bags do not help; a destination does (→ 01-05).

## Phase notes

- **A (shelter in place):** the bags sit ready and get maintained. Most emergencies are handled
  at home.
- **B (moving):** this page is the plan. Grab, load, go; the 60-second list runs the door. The
  medical load-out follows → 01-07.
- **C (establish):** the bags become the starting kit at the new place and then get **rebuilt
  at once**: a spent bag left empty is the most common failure after any move.

Related: → 22-06 medical kit (build it first) · → 22-05 vehicle kit · → 22-01 where the gear
comes from · → 01-02 when to go · → 01-03 moving · → 01-06 transition checklists ·
→ 19-01 documents · → 25-08 quick-reference cards · → 24-02 practising the grab.

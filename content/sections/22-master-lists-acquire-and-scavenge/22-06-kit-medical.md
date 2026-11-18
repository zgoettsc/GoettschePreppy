---
id: 22-06-kit-medical
section: 22-master-lists-acquire-and-scavenge
title: "Medical go-kit"
version: 5
revised: 2026-11-18
layer: core
danger_level: critical
phase: [A, B, C]
tags: [medical kit, go-kit, medicines, rescue medicine, epinephrine, insulin, cold chain, conditions]
derived_from: [22-06-kit-medical]
sources:
  - us-fda-information-regarding-insulin-storage-and-swi-6448d3
  - cdc-recognizing-and-responding-to-anaphylaxis-645825
  - cdc-diabetic-ketoacidosis-55a7c2
  - cdc-managing-sick-days-18c7c8
  - american-academy-of-allergy-asthma-and-immunology-aa-7f3939
  - american-diabetes-association-insulin-storage-and-sy-6f1f94
  - american-college-of-surgeons-stop-the-bleed-stop-the-8d1b5b
  - usuhs-ncdmph-stop-the-bleed-apply-a-tourniquet-r7
  - american-academy-of-pediatrics-aap-allergy-and-anaph-3e6f49
related: [22-03-go-bags-and-kits, 22-05-kit-vehicle, 01-07-evacuating-with-medical-needs, 12-01-first-aid-kit, 12-07-meds-stockpile, 12-08-medical-kit-tiers, 12-11-chronic-conditions, 12-16-triage-and-hard-calls, 12-21-evaporative-cooling-pouches, 25-09-family-medical-summary, 23-02-master-consumables-table, 29-07-ex07-refrigerated-medicines, 02-01-cl01-type-1-diabetes-injections, 02-03-cl03-anaphylaxis]
cards: [DC-04, DC-08, DC-15, DC-16, DC-25]
explainers: [EX-07, EX-14]
promote_when: [has.refrigerated_meds, has.anaphylaxis, has.epinephrine, has.oxygen, has.cpap]
photo_slots:
  - { id: med-kit-packed, caption: "Our medical go-kit packed: each module's pouch, labelled, and where the kit lives" }
figures: []
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: { date: "2026-11-18", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "Tourniquet floor reworded per docs/05 (DC-25); second dose re-cited to AAP; belt-as-tourniquet line aligned with 12-02; dehydration claim softened. Wave 2 (R18): tourniquet floor bolded as one sentence pair, verbatim 30-01. K1 (G34): no-prescriber pointers added for sick days (CDC steps on 02-01), insulin switching (FDA text on 02-01) and daily medicines running short (labels, 12-11)." }
---

# Medical go-kit

**What this page is for.** One bag that holds everything this household's medical conditions
need for the first days away from home, packed so that someone who did not pack it can find
each part by feel, in the dark. It is built from the conditions, allergies and medicines in
your settings: each condition adds its module (its own pouch) from the condition library in
Section 02. Build this kit before any other kit in the binder.

> **SAFETY — CRITICAL.**
> - **This page contains no dosing.** Quantities and doses come from your prescriptions and
>   your prescribers. The binder never works out, adjusts or suggests a dose.
> - **Rescue medicine is never rationed and never delayed.** In anaphylaxis, epinephrine comes
>   first; antihistamines do not treat it (CDC, Recognizing and Responding to Anaphylaxis;
>   AAAAI, Anaphylaxis Emergency Action Plan).
> - **A frozen-then-thawed insulin vial or pen is discarded.**
> - **Children do not have access to firearms, fuel, medications or chlorine products.** The kit
>   is closed and rides with an adult.
> - **Never loosen a tourniquet once placed while help can still come; mark the time. If no
>   help will ever come, the conversion decision is DC-25 (→ 30-26).**

## Do this now

1. **Build this kit first.** → 22-03 waits; this does not.
2. **Ask every prescriber, at the next appointment, for the most on-hand supply your
   prescriptions and insurance allow**, and about 90-day fills and early-refill ("vacation")
   overrides (→ 12-07). This is the single highest-value medical preparation there is.
3. **Count what you have today** and write the number of days on the front of the kit and in
   the table below (→ 22-04).
{{#if has.epinephrine}}4. **Put an epinephrine pair everywhere the allergic person spends time**: their own bag, each
   adult's bag, the house kit, school or daycare. A vehicle pair is a marked backup only.
{{else}}4. **Put each rescue medicine where the person who needs it will be** (inhaler, glucagon,
   seizure rescue medicine, epinephrine), not only in this bag.
{{/if}}5. **Get each condition's emergency plan from the prescriber, in writing**, laminate it, and put
   one copy in the kit and one on the fridge. A plan a stranger can follow is worth more than
   a plan only you understand.
6. **Check every expiry date on the two kit-check dates** (→ 22-03).

{{photo med-kit-packed}}

## How the kit is organised

| Pouch | For | What it prevents |
|---|---|---|
| **One pouch per condition module** | Each person with a condition (below) | The condition's own emergency (each Section 02 page names it) |
| **Rescue pouch** | Anyone with a rescue medicine | A life-threatening event in minutes: anaphylaxis, a severe low, an asthma attack, a seizure |
| **General pouch** | Everyone | Bleeding, infection, dehydration, fever, wounds |

**Different coloured pouches, labelled on the outside, with that condition's printed plan
inside each.**

## What this household needs

**People and conditions:**

| Person | Age | Conditions | Allergies |
|---|---|---|---|
{{#each members as m}}| {{m.label}} | {{m.age_text}} | {{m.conditions}} | {{m.allergies}} |
{{/each}}

**Medicines, exactly as typed from the bottles** (the binder never changes these):

| Person | Medicine | Strength | Schedule | Refrigerated | If doses are missed (prescriber's words) | Where kept | Expiry | Days on hand |
|---|---|---|---|---|---|---|---|---|
{{#each meds as x}}| {{x.member}} | {{x.name}} | {{x.strength}} | {{x.schedule}} | {{x.refrigerated}} | {{x.if_missed}} | {{x.where_kept}} | {{x.expiry}} | {{x.days_on_hand}} |
{{else}}| none entered | | | | | | | | |
{{/each}}

**Allergies:**

| Person | Allergen | Severity | Carries epinephrine |
|---|---|---|---|
{{#each allergies as a}}| {{a.member}} | {{a.allergen}} | {{a.severity}} | {{a.carries_epinephrine}} |
{{else}}| none entered | | | |
{{/each}}

**Shortest medical clock in the household:** ______________ = ______ days. This number sits on
the front of the kit and drives → 01-02.

## The condition modules

Each row is the go-kit part of that condition's page. Rows marked **(in this household)** are
the ones your settings selected; the rest stay here so a condition can be added later.

| Condition | What goes in its pouch | Page |
|---|---|---|
| Type 1 diabetes, injections{{#if has.condition.CL-01}} **(in this household)**{{/if}} | Every vial or pen, syringes or pen needles, meter + strips + lancets, **ketone strips**, fast sugar, glucagon, the sick-day plan, cooling | → 02-01 |
| Type 1 diabetes, pump and sensor{{#if has.condition.CL-02}} **(in this household)**{{/if}} | All of the above **plus** pump supplies, sensors, chargers, the printed pump-failure plan from the prescriber. **The syringe is the survival path** | → 02-02 |
| Anaphylaxis{{#if has.condition.CL-03}} **(in this household)**{{/if}} | **Epinephrine pair**, the written plan, medical ID, antihistamine only as the plan says | → 02-03 |
| Food allergy{{#if has.condition.CL-04}} **(in this household)**{{/if}} | Safe food in original labelled packaging, dedicated utensils, the allergen list | → 02-04 |
| Type 2 diabetes{{#if has.condition.CL-05}} **(in this household)**{{/if}} | Tablets or injectables, meter + strips, fast sugar if the medicine can cause lows | → 02-05 |
| Type 2 diabetes on insulin{{#if has.condition.CL-06}} **(in this household)**{{/if}} | Insulin and supplies as for type 1, cooling, meter + strips, fast sugar | → 02-06 |
| Asthma{{#if has.condition.CL-07}} **(in this household)**{{/if}} | Rescue inhaler (two), spacer, controller inhaler, the written action plan, N95 masks for smoke | → 02-07 |
| COPD and oxygen{{#if has.condition.CL-08}} **(in this household)**{{/if}} | Inhalers, oxygen hours counted, tubing, concentrator power plan; **no flame near oxygen** | → 02-08 |
| High blood pressure and heart disease{{#if has.condition.CL-09}} **(in this household)**{{/if}} | Every daily tablet; a home blood-pressure cuff; any chest-pain medicine the prescriber gave | → 02-09 |
| Blood thinners{{#if has.condition.CL-10}} **(in this household)**{{/if}} | The tablets, extra pressure dressings and wound-packing gauze, a card saying which thinner | → 02-10 |
| Epilepsy and seizures{{#if has.condition.CL-11}} **(in this household)**{{/if}} | Every daily medicine, any rescue medicine, the seizure plan, a seizure log | → 02-11 |
| Pregnancy, birth and postpartum{{#if has.condition.CL-12}} **(in this household)**{{/if}} | Prenatal vitamins, records, the birth supplies list | → 02-12 |
| Infant feeding{{#if has.condition.CL-13}} **(in this household)**{{/if}} | Formula and safe water, or the nursing parent's extra food and water; bottles and cleaning | → 02-13 |
| Thyroid disease{{#if has.condition.CL-14}} **(in this household)**{{/if}} | The tablets, in original bottles | → 02-14 |
| Kidney disease and dialysis{{#if has.condition.CL-15}} **(in this household)**{{/if}} | Medicines, the fluid and potassium plan, the dialysis centre's emergency plan | → 02-15 |
| Mental-health medicines{{#if has.condition.CL-16}} **(in this household)**{{/if}} | Every daily medicine (some are dangerous to stop suddenly), the crisis plan | → 02-16 |
| Opioid dependence and chronic pain{{#if has.condition.CL-17}} **(in this household)**{{/if}} | Medicines as prescribed, **naloxone**, non-drug pain aids | → 02-17 |
| Immunosuppression and transplant{{#if has.condition.CL-18}} **(in this household)**{{/if}} | Every anti-rejection medicine, masks, hand sanitiser, a thermometer | → 02-18 |
| Celiac and severe gut disease{{#if has.condition.CL-19}} **(in this household)**{{/if}} | Safe food, oral rehydration salts, any prescribed medicine | → 02-19 |
| Adrenal insufficiency{{#if has.condition.CL-20}} **(in this household)**{{/if}} | Daily steroid (extra for sick-day doubling), the emergency hydrocortisone injection kit with syringes, and the published stress-dose tables on 02-20 printed and in the kit (no prescriber may be reachable) | → 02-20 |
| Dementia and elderly care{{#if has.condition.CL-21}} **(in this household)**{{/if}} | Medicines in a pill organiser, ID bracelet, a recent photo, a comfort item | → 02-21 |
| Mobility impairment{{#if has.condition.CL-22}} **(in this household)**{{/if}} | Pressure-injury supplies, toileting supplies, aid repair kit | → 02-22 |
| Hearing and vision aids{{#if has.condition.CL-23}} **(in this household)**{{/if}} | Spare glasses, the written glasses prescription, hearing-aid batteries | → 02-23 |
| Sleep apnoea (CPAP){{#if has.condition.CL-24}} **(in this household)**{{/if}} | Mask, tubing, filters, the 12 V cord or battery tested at home | → 02-24 |
| Contraception and menstrual health{{#if has.condition.CL-25}} **(in this household)**{{/if}} | The supply, plus reusable menstrual supplies | → 02-25 |
| Severe obesity and bariatric surgery{{#if has.condition.CL-26}} **(in this household)**{{/if}} | Vitamins and supplements as prescribed, larger-size first-aid and mobility items | → 02-26 |
| A condition not in the library | The twelve headings of → 02-27, filled in from the prescriber | → 02-27 |

## Rescue medicines: the rules that do not change

{{#if has.anaphylaxis}}**Anaphylaxis is in this household.**{{else}}No anaphylaxis is entered; read this anyway.{{/if}}

- **Epinephrine in pairs, in date.** A second dose may be needed if symptoms get worse,
  continue or do not get better in 5 minutes (AAP, Allergy and Anaphylaxis Emergency Plan).
  One device is not a kit.
- **The written, signed plan from the prescriber**, laminated, in the pouch. Anyone must be
  able to follow it, including someone who has never met the person (→ 02-03).
- **Medical ID on the person** listing the allergens.
- **Antihistamine only as the plan says: never first, never instead of epinephrine.**
- **Safe food** in original sealed packaging (→ 02-04), and dedicated utensils: cross-contact is
  the usual exposure in an improvised kitchen.
- **After epinephrine, the plan is normally emergency care.** Write down now what you do when
  that is not available (→ 12-16): a second dose may be needed, and a reaction can come back
  hours later. Watch the person.
- **Expired devices when nothing in date exists** is a household choice: {{choice DC-04}} → 30-05.

{{#if has.condition.CL-01}}**Insulin-dependent diabetes is in this household.**{{else}}No insulin-dependent diabetes is entered; read this anyway.{{/if}}

- **Every vial or pen you legitimately have**, plus the injection fallback (syringes or pens)
  **even if a pump works**: pumps fail, batteries die (→ 02-02).
- **Meter, strips and lancets.** A sensor is not the fallback; the meter is.
- **Ketone strips**: the most-forgotten life-saving item in the kit. They catch diabetic
  ketoacidosis (DKA) early (CDC, Diabetic Ketoacidosis).
- **Fast sugar** in several places: kit, pocket, car, bedside.
- **Glucagon**, and **a second adult who knows how to use it.**
- **The sick-day plan** from the prescriber, or with no prescriber CDC's published steps,
  printed on → 02-01 part 6 (CDC, Managing Sick Days).
- **Rationing insulin is not a household decision.** If supply is short, that is a reason to
  move toward resupply (→ 01-02), not to under-dose (→ 12-11). Switching to whatever insulin can
  be found, with no prescriber, follows FDA's published text on → 02-01 part 8.

## The cold chain

{{#if has.refrigerated_meds}}This household keeps refrigerated medicine:
{{#each refrigerated_meds as r}}{{r.member}}: {{r.name}} ({{r.where_kept}}) · {{/each}}
{{else}}No refrigerated medicine is entered. Read this anyway: a new prescription can change that.
{{/if}}

- **Insulin's fridge range is 36 to 46 °F.** Many insulins can be kept unrefrigerated between
  59 and 86 °F for up to 28 days, depending on the product; read your product's label (FDA,
  Insulin Storage in an Emergency; ADA, Insulin Storage and Syringe Safety). Other medicines:
  read each label (→ 29-14).
- **Freezing is a cliff; heat is a slope** (→ 29-07). **A frozen-then-thawed insulin vial or pen
  is discarded.** In winter, carry it against the body. Heat-exposed medicine:
  {{choice DC-08}} → 30-09.
- **A thermometer decides, not a hand.** Put one in whatever keeps the medicine cold.
- **Layers:** a 12 V fridge or cooler on a power station (tested at home for a day; → 09-10), an
  insulated pouch with cold packs that cannot touch the medicine, and an evaporative cooling
  pouch as the fallback (→ 12-21).

## General pouch (the carry version of → 12-01)

| Category | Items |
|---|---|
| **Bleeding** | Tourniquet (and the training), pressure dressing, wound-packing gauze, gauze rolls, tape (Stop the Bleed, USUHS; → 12-02) |
| **Wounds** | Irrigation syringe, antiseptic, non-stick pads, closure strips; sutures or stapler **only if trained** (→ 12-14) |
| **Infection** | Antibiotic ointment. Prescribed antibiotics only; using them without a prescription is a household choice: {{choice DC-16}} → 30-17 |
| **Burns** | Non-stick dressings, cling film, clean water (→ 12-03) |
| **Fluids** | **Oral rehydration salts**: diarrhoea and dehydration are common when water and sanitation fail (→ 12-05) |
| **Fever and pain** | Adult and **child** forms, each with the dosing tool from its package; a thermometer (→ 12-13) |
| **Splints** | Padded aluminium splint, wrap, triangular bandages (→ 12-09) |
| **Barrier** | Nitrile gloves (several pairs), N95 masks, eye protection, CPR face shield |
| **Dental** | Temporary filling material, clove oil, dental wax (→ 12-06) |
| **Tools** | Trauma shears, tweezers, safety pins, headlamp and spare batteries, permanent marker (write the time on a tourniquet and on dressings) |
| **Personal** | Everyone's prescriptions, spare glasses, sunscreen, insect repellent |
| **Paper** | → 12-01, → 12-02, → 12-16, every condition plan, and the family medical summary (→ 25-09) |

Giving one person's prescription medicine to another: {{choice DC-15}} → 30-16.

## Storage, rotation and where it lives

- **One grab bag, carried in the cabin**, never in the trunk in extreme weather (→ 01-07).
- **Insulated in both directions**: a cold-pack pocket for summer, body-carry for winter.
- **Waterproof**: a dry bag or heavy zip bags inside.
- **Labelled outside** with the household's name, the conditions, and "MEDICAL".
- **A copy of each plan on the fridge**, where responders look.
- **On each kit-check date:** every expiry, every battery, refresh the food, **replace anything
  within six months of expiry**, and read every plan aloud with another adult.

## The honest limits of this kit

It handles **hours to days**, not months. It cannot:

- **Make insulin, epinephrine or any other medicine.** No skill substitutes (→ 23-04).
- **Replace a hospital** for airway management, surgery, imaging or blood (→ 12-16).
- **Solve a supply shortage.** Only resupply does, which is why the count in → 22-04 is the
  number that drives the household's decisions, and why → 01-02 exists.

## If you do not have it

- **The general pouch substitutes broadly:** clean cloth for gauze, boiled water for
  irrigation, improvised splints (→ 12-09). **A tourniquet is the exception:** improvised ones
  often fail (→ 12-02), so firm direct pressure and wound packing come first.
- **Medicines do not substitute.** Found medicine of unknown storage history cannot be trusted
  as the primary: heat and freezing damage are invisible (→ 22-02).
- **The one thing you can always improvise is the written plan.** Copy the essentials onto
  paper and put it where responders look.

## When it runs out

| Item | How long | Ration? | Resupply | Substitute |
|---|---|---|---|---|
| **Daily medicines** | Count ÷ daily use, from the prescription | **Not a household decision**: ask the prescriber now what to do if it runs short. With no prescriber, the label's own lines and the condition page's "When there is no prescriber" part (→ 12-11) | Pharmacy, clinic, hospital, mutual aid (→ 12-07) | **None** for most |
| **Rescue medicines** | Devices or doses on hand | **Never** | Prescription | **None** |
| **Device supplies** (sensors, pump parts, CPAP filters) | Count | Only as the condition page says | As above | The condition page's fallback |
| **Test and ketone strips** | Count | **Do not skimp on ketone strips** | As above | None reliable |
| General pouch | Weeks | Yes, most items | Trade (→ 18-02), scavenge (→ 22-02) | Widely (→ 23-03) |

**Everything in this binder can be rationed, substituted, improvised or produced except the top
rows of this table.** They are the reason the household has a phase plan at all.

## Phase notes

- **A (shelter in place):** the kit sits packed; the house holds the bulk supply (→ 12-07). Work
  the resupply relationships now, while pharmacies and clinics function.
- **B (moving):** this kit **rides in the cabin with a person**, never left in a parked vehicle
  in heat or cold. First loaded, first checked at every stop (→ 01-07).
- **C (establish):** the supply count becomes the countdown. **Finding a medical supply line
  is a first task at the new place**, not a background chore (→ 01-04, → 18-01).

Related: → 22-03 go-bags · → 22-05 vehicle · → 01-07 the medical load-out · → 12-01 household
first-aid kit · → 12-08 kit tiers · → 12-11 chronic conditions · → 12-16 hard calls ·
→ 25-09 medical summary · → 23-02 the runway table · → 29-07 refrigerated medicines.

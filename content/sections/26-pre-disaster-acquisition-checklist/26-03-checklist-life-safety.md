---
id: 26-03-checklist-life-safety
section: 26-pre-disaster-acquisition-checklist
title: "Checklist 1: life safety and medical"
version: 1
revised: 2026-11-16
layer: core
danger_level: critical
phase: [A]
tags: [checklist, CO alarm, smoke alarm, medicines, rescue medicine, epinephrine, trauma kit, first aid]
derived_from: [26-03-checklist-life-safety]
sources:
  - cdc-carbon-monoxide-poisoning-basics-772153
  - us-fda-information-regarding-insulin-storage-and-swi-6448d3
  - cdc-recognizing-and-responding-to-anaphylaxis-645825
  - cdc-diabetic-ketoacidosis-55a7c2
  - usfa-smoke-alarms
  - american-college-of-surgeons-stop-the-bleed-stop-the-8d1b5b
related: [22-06-kit-medical, 12-07-meds-stockpile, 08-02-carbon-monoxide-safety, 12-01-first-aid-kit, 12-02-bleeding-and-wounds, 26-08-expiry-and-rotation-tracker, 26-09-shopping-list-and-budget, 25-09-family-medical-summary, 02-03-cl03-anaphylaxis, 29-07-ex07-refrigerated-medicines]
cards: [DC-04, DC-08]
explainers: [EX-03, EX-07, EX-12, EX-14]
promote_when: []
photo_slots: []
figures: []
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: null
---

# Checklist 1: life safety and medical

**What this page is for.** The first sheet of the walk (→ 26-01), and the one to do properly
even if you do no other. It covers the alarms that warn you of fire and carbon monoxide, every
medicine and device someone in the household depends on, and the first-aid kit. **No quantity on
this page is a recommendation**: amounts come from your prescriptions and your prescribers.

> **SAFETY — CRITICAL.**
> - **Never run a generator, charcoal, or any engine indoors, in a garage, or near an open
>   window.** A battery CO alarm is the cheapest life-saving item in the house (CDC, Carbon
>   Monoxide Poisoning: Basics; → 29-03).
> - **A frozen-then-thawed insulin vial or pen is discarded.**
> - **Children do not have access to firearms, fuel, medications or chlorine products.**

**Marks:** ✔ have it, it works, I know where it is · ~ partly, or needs a spare · ✗ do not have ·
n/a

## A. Alarms and fixed safety (check these where they are)

| ✔ ~ ✗ | Item | Where / notes | Page |
|---|---|---|---|
| [ ] | **CO alarm, battery or battery-backup type, on every level and outside every sleeping area** (we have {{ gear.co_alarms }}) | | → 08-02 |
| [ ] | A CO alarm in any room where anything burns{{#if has.unvented_heater}} (**you own an unvented heater**){{/if}}, installed and tested **before** it is lit | | → 08-02 |
| [ ] | Spare batteries for every alarm | | |
| [ ] | **Smoke alarm in every sleeping area, outside each one, and on every level**, tested (we have {{ gear.smoke_alarms }}) (USFA, Smoke Alarms) | | → 29-12 |
| [ ] | Fire extinguishers, in date, reachable (we have {{ gear.extinguishers }}) | | → 29-12 |
| [ ] | Every adult has operated the **gas shutoff**{{#if !has.gas_any}} (none per settings){{/if}} and knows where the tool is | | → 00-04 |
| [ ] | Every adult has operated the **water main** | | → 03-02 |
| [ ] | Escape ladder for any upstairs bedroom | | → 24-02 |

> **The CO alarm is the best value per dollar in this binder.** Bringing anything that burns
> indoors in an outage is the most likely way a household dies, and it is cheap to detect.

## B. Every medicine someone depends on

Printed from settings, exactly as typed. Count against the bottles.

| ✔ ~ ✗ | Person | Medicine | Strength | Refrigerated | On hand | Earliest expiry | Days on hand |
|---|---|---|---|---|---|---|---|
{{#each meds as x}}| [ ] | {{x.member}} | {{x.name}} | {{x.strength}} | {{x.refrigerated}} | ______ | {{x.expiry}} | {{x.days_on_hand}} |
{{else}}| [ ] | none entered | | | | | | |
{{/each}}| [ ] | Any medicine not yet in settings: ______________ | | | | ______ | ______ | ______ |

| ✔ ~ ✗ | Item | Page |
|---|---|---|
| [ ] | **A written list of every prescription**, and the family medical summary filled in | → 25-09 |
| [ ] | Asked each prescriber this year about emergency supply, 90-day fills and early-refill overrides: Y / N | → 12-07 |
| [ ] | Each condition's written plan from the prescriber, laminated | Section 02 |
{{#if has.refrigerated_meds}}| [ ] | **Cold chain (this household):** a thermometer in the fridge or cooler that holds the medicine; an insulated pouch and cold packs; an evaporative cooling pouch; a way to run a 12 V cooler in an outage | → 29-07, → 12-21 |
{{/if}}| [ ] | Medicine stored out of children's reach, locked if there are children | → 20-02 |
| [ ] | Spare glasses or the written glasses prescription; hearing-aid batteries | → 02-23 |

> **Medicine that must not freeze or overheat** (insulin and many others): if you have no way to
> keep it in range in a winter power cut or a summer car, that is a "~", not a "✔" (FDA, Insulin
> Storage in an Emergency). Heat-exposed medicine: {{choice DC-08}} → 30-09.

## C. Rescue medicines

{{#if has.epinephrine}}**Epinephrine (this household):**

| ✔ ~ ✗ | Location | Count | Expiry |
|---|---|---|---|
| [ ] | The allergic person's own bag | ______ | ______ |
| [ ] | Each adult's bag | ______ | ______ |
| [ ] | House medical kit | ______ | ______ |
| [ ] | School, daycare or work, on file | ______ | ______ |
| [ ] | Each vehicle: a **backup only**, in a pouch that comes inside in extreme heat or cold | ______ | ______ |
| [ ] | The written action plan, laminated, with every caregiver | | |
| [ ] | Medical ID worn | | |
| [ ] | Antihistamine as the plan says (**never instead of epinephrine**) | ______ | ______ |
| [ ] | A trainer device for practice | | |

> **A pair, not one.** A second dose is often needed (CDC, Recognizing and Responding to
> Anaphylaxis). Any location holding a single device is a "~". Expired devices when nothing in
> date exists: {{choice DC-04}} → 30-05.
{{/if}}

| ✔ ~ ✗ | Rescue item | Count | Expiry | Page |
|---|---|---|---|---|
| [ ] | Glucagon and fast sugar{{#if has.condition.CL-01}} **(this household)**{{/if}}{{#if has.condition.CL-06}} **(this household)**{{/if}} | ______ | ______ | → 02-01 |
| [ ] | Rescue inhaler and spacer{{#if has.condition.CL-07}} **(this household)**{{/if}} | ______ | ______ | → 02-07 |
| [ ] | Seizure rescue medicine{{#if has.condition.CL-11}} **(this household)**{{/if}} | ______ | ______ | → 02-11 |
| [ ] | Naloxone{{#if has.condition.CL-17}} **(this household)**{{/if}} | ______ | ______ | → 02-17 |
| [ ] | Emergency steroid kit{{#if has.condition.CL-20}} **(this household)**{{/if}} | ______ | ______ | → 02-20 |
| [ ] | Other: ______________ | ______ | ______ | |

## D. Devices and their supplies

| ✔ ~ ✗ | Item | Count / runtime | Page |
|---|---|---|---|
| [ ] | Diabetes: meter + strips, **ketone strips**, syringes or pens as the fallback, sensors, pump supplies{{#if has.condition.CL-02}} **(this household: pump and sensor)**{{/if}} | ______ | → 02-01, → 02-02 |
| [ ] | Oxygen: cylinders (hours), concentrator power plan, tubing{{#if has.oxygen}} **(this household)**{{/if}} | ______ h | → 02-08 |
| [ ] | CPAP: mask, tubing, filters, 12 V cord or battery tested for a night{{#if has.cpap}} **(this household)**{{/if}} | ______ | → 02-24 |
| [ ] | Wheelchair or walker: repair kit, spare tyre or tips{{#if has.mobility_aid}} **(this household)**{{/if}} | ______ | → 02-22 |
| [ ] | Power for every medical device, measured in watt-hours a day | ______ Wh | → 09-10 |
| [ ] | Sharps container (or a hard-sided substitute) | | → 13-03 |

> **Ketone strips are the most-forgotten item on this page** for anyone with diabetes, and they
> catch DKA early (CDC, Diabetic Ketoacidosis).

## E. Trauma and first aid

| ✔ ~ ✗ | Item | Count | Page |
|---|---|---|---|
| [ ] | Tourniquets, and the training (Stop the Bleed) | ______ | → 12-02 |
| [ ] | Pressure dressings; wound-packing gauze | ______ | → 12-02 |
| [ ] | Trauma shears | ______ | → 12-02 |
| [ ] | Gauze, tape, non-stick pads | ______ | → 12-01 |
| [ ] | Wound irrigation syringe | ______ | → 12-14 |
| [ ] | Closure strips (stapler or sutures only if trained) | ______ | → 12-14 |
| [ ] | Nitrile gloves, several pairs | ______ | → 12-01 |
| [ ] | Burn dressings | ______ | → 12-03 |
| [ ] | Padded splint, wrap, triangular bandages | ______ | → 12-09 |
| [ ] | **Oral rehydration salts** | ______ | → 12-05 |
| [ ] | Pain and fever medicine, **adult and child** forms, each with its dosing tool{{#if has.child}} **(this household has children)**{{/if}} | ______ | → 12-13 |
| [ ] | A working thermometer | ______ | → 12-05 |
| [ ] | Dental first aid (temporary filling, clove oil) | ______ | → 12-06 |
| [ ] | CPR face shield, N95 masks, eye protection | ______ | → 12-01 |
| [ ] | A second full kit for the house | | → 12-01 |
| [ ] | Stop the Bleed course taken by every adult | | → 12-02 |
| [ ] | First aid and CPR course{{#if has.infant}}, **including infant CPR**{{/if}}, every adult | | → 12-18 |

> **Dehydration and infection kill more people in long events than trauma does.** Oral
> rehydration salts and infection care are not glamorous, and they matter more than the
> tourniquet you will probably never use (→ 12-04, → 12-05).

## The lines that decide the rest

```
SHORTEST MEDICAL CLOCK:     ________ = ______ days  <- the household's governing number (23-01)
RESCUE MEDICINE IN DATE, IN EVERY LOCATION:  Y / N
CO ALARMS WORKING:          ________   <- should equal levels + sleeping areas + burning points
SMOKE ALARMS WORKING:       ________

BIGGEST GAP ON THIS PAGE: ______________________________________________
FIRST THING TO BUY:       ______________________________________________
```

**Copy these to → 26-09.** Anything on this page marked ✗ goes to the top of the shopping list,
ahead of everything on the other checklists, whatever it costs.

Related: → 22-06 the medical go-kit this stocks · → 12-07 medicine supply · → 08-02 carbon
monoxide · → 12-01 the household kit · → 26-08 where the expiry dates go · → 26-09 the shopping
list · → 25-09 medical summary.

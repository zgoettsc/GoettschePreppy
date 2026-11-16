---
id: 01-07-evacuating-with-medical-needs
section: 01-phase-playbooks
title: "Leaving home with medical needs: medicines, devices and the cold chain on the road"
version: 2
revised: 2026-11-16
layer: core
danger_level: critical
phase: [B]
tags: [evacuation, medical, cold chain, insulin, epinephrine, refrigerated medicine, oxygen, CPAP, devices, supply clock, med bag, destination medical card]
derived_from: [02-12-evacuation-medical-logistics]
sources:
  - us-fda-information-regarding-insulin-storage-and-swi-6448d3
  - american-diabetes-association-switching-between-insu-9c5595
  - american-diabetes-association-insulin-storage-and-sy-6f1f94
  - us-fda-epipen-epinephrine-injection-usp-auto-injecto-a9f17f
  - american-academy-of-pediatrics-aap-allergy-and-anaph-3e6f49
  - ecfr-47-cfr-part-9-911-requirements
related: [01-03-phase-b-movement, 01-05-choosing-a-destination, 01-06-phase-transition-checklists, 01-02-go-no-go-decision, 29-07-ex07-refrigerated-medicines, 12-21-evaporative-cooling-pouches, 09-10-power-for-medical, 09-06-charging-medical-devices, 22-05-kit-vehicle, 22-06-kit-medical, 25-09-family-medical-summary, 15-09-corridor-comms, 30-09-dc08-heat-exposed-medication]
cards: [DC-04, DC-08, DC-18]
explainers: [EX-07, EX-14, EX-02]
promote_when: [has.refrigerated_meds, has.oxygen, has.cpap, has.mobility_aid, has.anaphylaxis]
photo_slots:
  - { id: med-bag, caption: "Our cabin med bag, packed: everything in one grab" }
figures: []
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: { date: "2026-11-16", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "Days on hand from meds; refrigerated_meds listed; condition flags mark dialysis, dementia, pregnancy, diabetes; AAP second dose; 911 to 47 CFR 9.10." }
---

# Leaving home with medical needs: medicines, devices and the cold chain on the road

**What this page is for.** If anyone in the household depends on a medicine, a refrigerated drug,
a rescue medicine or a powered device, the trip is the most dangerous day for them: a summer
vehicle cooks medicine, a winter cargo area freezes it, a dead battery stops a device, and a
roadside meal can trigger an allergy. This page decides all of that now, so that loading day is
doing, not thinking. It works for any condition; your condition pages in Section 02 hold the
details for each one.

> **SAFETY — CRITICAL.**
> - **A frozen-then-thawed insulin vial or pen is discarded.** It loses strength with no way to
>   tell; the published guidance is unanimous (FDA, Insulin Storage in an Emergency). Many other
>   refrigerated medicines must not freeze either: follow each label (→ 29-14).
> - **Children do not have access to firearms, fuel, medications or chlorine products.** On the
>   road, the med bag rides with an adult, closed.
> - **Never run a generator, charcoal, or any engine indoors, in a garage, or near an open
>   window**, including to power a cooler or charge a device.
> - **Medicine never stays in a parked vehicle.** It leaves the vehicle with a person at every
>   stop.

## Do this now

1. **List who has a medical clock** (the table below is filled from your answers; add anything
   missing by hand).
2. **Pack the cabin med bag** from the load-out list below, into the medical kit (→ 22-06), so
   "grab the med bag" grabs all of it.
3. **Fill in a destination medical card** for each destination (below).
4. **Check every expiry, refill and device date against the trip**: prescriptions, devices,
   sensors, batteries, and any phone app a device depends on. Renew what would run out on the
   road **before** you leave.
5. **Write the household's departure rule:** we do not set out with fewer than ______ days of
   every clocked supply (below).

## Who in this household has a clock

| Person | Conditions | Condition pages |
|---|---|---|
{{#each members as m}}| {{m.label}} | {{m.conditions}} | Section 02 |
{{/each}}

**Medicines, exactly as typed from the bottles:**

| Person | Medicine | Strength | Schedule | Refrigerated | If doses are missed (prescriber's words) | Days on hand |
|---|---|---|---|---|---|---|
{{#each meds as x}}| {{x.member}} | {{x.name}} | {{x.strength}} | {{x.schedule}} | {{x.refrigerated}} | {{x.if_missed}} | {{x.days_on_hand}} |
{{else}}| none entered | | | | | | |
{{/each}}

**Devices:**{{#if has.oxygen}} oxygen (→ 02-08) ·{{/if}}{{#if has.cpap}} CPAP (→ 02-24) ·{{/if}}{{#if has.mobility_aid}} wheelchair or walker (→ 02-22) ·{{/if}} others: ______________________

The binder never works out or changes a dose. What to do if a medicine runs out or a device fails
comes from the prescriber, written on that condition's page in Section 02. **Ask now, while you
can.**

## Why / how it works

### The cold chain rides in the cabin, powered

{{#if has.refrigerated_meds}}This household has refrigerated medicine. This section is your plan for:

{{#each refrigerated_meds as x}}- **{{x.name}}** ({{x.member}})
{{/each}}
{{else}}No refrigerated medicine is entered. Read this anyway: a new prescription can change
that.{{/if}}

- **Primary layer: a powered cooler in the cabin.** A 12-volt compressor cooler or small fridge,
  run from a power station or the vehicle's socket, holds refrigerated medicine at fridge
  temperature. For insulin, refrigerated storage is **36 to 46 °F** (FDA, Insulin Storage in an
  Emergency); for other medicines, read the label (→ 29-14).
- **Set it up at home first.** Run it for a day from the battery you will use, and write down how
  much battery it used: ______ % per day. That number, not the brochure, tells you how long it
  lasts on the road (→ 09-10, → 29-02).{{#if has.power_station}} Our power stations hold about
  {{ gear.station_wh_total }} watt-hours in total.{{/if}}
- **On loading day: cooler running, thermometer reads in range, THEN the medicine goes in.** A
  separate thermometer you trust, not only the cooler's display.
- **Backup layer: an evaporative cooling pouch** in the med bag, with the medicine in current use
  and one spare, so a cooler or battery failure on the road is a setback, not a loss (→ 12-21).
- **In winter the danger flips from heat to freezing.** Refrigerated medicine never rides in the
  cargo area, a trailer or a roof box: cabin, in the cooler or against a person. **The same goes
  for every temperature-sensitive supply** (pump parts, sensors, test strips, rescue medicines):
  check each label's storage range (→ 29-14).
- **If the cooler fails in summer:** many insulins can be kept unrefrigerated between 59 and 86 °F
  for up to 28 days, depending on the product (FDA, Insulin Storage in an Emergency; ADA,
  Switching Between Insulin Products in Disaster Response Situations). Protect the stock first,
  check your product's label, and use the cooling pouch.
- **Medicine that got hotter than its label allows** is a household decision: discard it, or use
  it with closer watching when nothing else exists. **Our choice:** {{choice DC-08}} (→ 30-09)
- **At fuel and rest stops** the cooler keeps running on its battery, but the med bag **steps out
  with a person**. A parked vehicle in the sun gets hotter than any label allows.

### Rescue medicines on the road

- **Rescue medicines (epinephrine, glucagon, rescue inhalers, seizure rescue medicine) ride in the
  cabin, on or beside an adult.** Never the trailer, never a door pocket in the sun, never left in
  the parked vehicle. Keep them within the storage range on their label (FDA, EpiPen prescribing
  information; → 02-03).{{#if has.anaphylaxis}}
- **Epinephrine travels in pairs**: a second dose is given if symptoms get worse, continue, or
  are not better in 5 minutes (AAP, Allergy and Anaphylaxis Emergency Plan). Whether expired devices count when no in-date ones exist is a
  household choice. **Our choice:** {{choice DC-04}} (→ 30-05){{/if}}
- **Fast sugar** within the driver's reach and in the back seat, for anyone with diabetes{{#if has.diabetes}}
  *(applies to us)*{{/if}} (→ 02-01, → 02-05).

{{#if has.anaphylaxis}}### Food stops and allergies

**Food stops are the moment of greatest allergy risk.** The person with the allergy eats from the
packed safe-food bin: pack the whole trip's food for them plus a margin for delays (→ 02-04).
How strictly to hold that line when safe food runs out is a household choice. **Our choice:**
{{choice DC-18}} (→ 30-19)
{{else}}### Food stops and special diets

Anyone on a special diet (an allergy, celiac disease, infant formula) eats from a packed bin, with
the whole trip's food plus a margin for delays (→ 02-04, → 02-19, → 02-13).
{{/if}}

### Powered devices and mobility on the road

- **Oxygen**{{#if has.oxygen}} *(applies to us)*{{/if}}: a concentrator needs power for the whole trip;
  cylinders run out. Count hours of supply against the trip plus a delay, keep cylinders secured so
  they cannot roll or fall, and keep oxygen away from any flame or smoking (→ 02-08, → 09-10).
- **CPAP**{{#if has.cpap}} *(applies to us)*{{/if}}: a 12-volt adapter or a battery made for the machine,
  tested at home for one night (→ 02-24, → 09-06).
- **Wheelchair or walker**{{#if has.mobility_aid}} *(applies to us)*{{/if}}: does it fit with the
  load? Who lifts it? How does the person get to a toilet at stops (→ 02-22)?
- **Dialysis**{{#if has.condition.CL-15}} *(applies to us)*{{/if}}: treatment cannot travel with you. Ask the dialysis centre now what its emergency
  plan is and where you would be treated near each destination (→ 02-15).
- **Dementia**{{#if has.condition.CL-21}} *(applies to us)*{{/if}}: unfamiliar stops are where people wander off. One named adult stays with them
  every minute out of the vehicle (→ 02-21).
- **Late pregnancy or a newborn**{{#if has.pregnant}} *(applies to us)*{{else}}{{#if has.infant}} *(applies to us)*{{/if}}{{/if}}: know where the hospitals with a maternity unit are along the
  route (→ 02-12, → 02-13).

### The cabin med load-out (this list is the packing list)

{{photo med-bag}}

| Item | Check | Page |
|---|---|---|
| Refrigerated medicine in the running cooler, thermometer reading in range | [ ] | → 29-07 |
| Cooling pouch with the medicine in current use and one spare | [ ] | → 12-21 |
| Every other prescription, in original labelled containers | [ ] | → 25-09 |
| Rescue medicines (in date), on a person | [ ] | Section 02 |
| Devices, their spare batteries, chargers and 12-volt adapters | [ ] | → 09-06 |
| Device supplies: sensors, pump parts, tubing, masks, needles or syringes, test strips | [ ] | Section 02 |
| Any phone a device depends on, charged, with its charger | [ ] | → 00-10 |
| The printed backup plan for each device failure, from the prescriber | [ ] | Section 02 |
| Fast sugar within the driver's reach and in the back | [ ] | → 02-01 |
| Thermometer for medicine; a thermometer for people | [ ] | → 22-06 |
| Children's medicines and fever medicine | [ ] | → 22-06, → 12-13 |
| Printed prescriptions, the "my meds" table, insurance and ID copies | [ ] | → 19-01, → 25-09 |
| Safe food for anyone with an allergy or special diet | [ ] | → 02-04 |

**The only purchase this implies** beyond the gear you own: a rigid, labelled med bag big enough to
hold all of it as **one grab**.

### Destination medical card

Write one for each destination and keep it with the route notes (→ 25-04). Drive past the
emergency room once on your first visit.

{{#each destinations as d}}
**{{d.name}}** ({{d.county}}, {{d.state_name}})

| Need | Place | Drive time | Hours, phone |
|---|---|---|---|
| Emergency room (adults) | ______________ | ______ | ______________ |
| Emergency care for children | ______________ | ______ | ______________ |
| Pharmacy, and the nearest 24-hour pharmacy | ______________ | ______ | ______________ |
| A prescriber or telehealth path for refills | ______________ | | ______________ |
| Dialysis, oxygen or device supplier, if needed | ______________ | ______ | ______________ |
{{else}}
No destination entered. Fill a card for wherever you would go: the nearest town with a hospital is
usually the realistic answer (→ 01-05).

| Need | Place | Drive time | Hours, phone |
|---|---|---|---|
| Emergency room | ______________ | ______ | ______________ |
| Pharmacy | ______________ | ______ | ______________ |
{{/each}}

**Until you have checked it, treat any destination as far from emergency care**, and avoid
elective risks there: new foods for anyone with a history of allergy, risky jobs, anything that
could need a hospital.

### The departure rule

**Do not set out with fewer than ______ days of every clocked supply** (each medicine, each device
supply, in-date rescue medicines, safe food). Choose a number that covers the trip, a breakdown or
a weather hold, and the time to find resupply at the destination. A closed road must never turn
the drive itself into the emergency. Count against your Section 02 pages and → 23-02 at the
loading step (→ 01-06).

### Getting medical help from the road

- **911 first.** Mobile carriers must pass on every 911 call made on their network, whether or
  not the phone has a working plan (47 CFR 9.10(b), FCC 911 rules), so any mobile phone with a
  signal can try 911.
- **Then:** the destination's facility numbers above; the hub contact (→ 00-04); the prescriber.
- **No signal:** the other adult's phone on a different network; then a radio call to someone who
  can phone for you (→ 15-09).{{#if has.satellite}} The satellite messenger, if it is activated and
  charged (→ 15-02).{{/if}}

## Gear / items

The load-out table above is the list. **Have now:** the med bag; a 12-volt cooler or cooling
pouches if anyone has refrigerated medicine; a medicine thermometer; 12-volt adapters for every
device. **Scavenge / substitute:** a hard-sided lunch cooler with a frozen bottle wrapped in a towel
(never touching the medicine) buys hours, not days; a cooling pouch buys days in heat (→ 12-21).

## When it runs out

- **Resupply on the way is a bonus, never a plan.** Pharmacies along the route may be open, closed
  or empty.
- **If the cold chain fails mid-route:** follow the unrefrigerated window on each label (→ 29-07);
  protect the stock first; **only frozen insulin is automatically discarded** (above).
- **If a device's power runs out:** the backup plan from its condition page; then toward the
  nearest working power and medical help (→ 01-02).

## Phase notes

- **A (at home):** the standing arrangements: → 29-07 for refrigerated medicine, → 09-10 for
  powered devices, Section 02 for each condition.
- **B (moving):** this page. It exists so the medical layer of → 01-03's load-out is one decision,
  not forty.
- **C (arriving):** put medicines back into safe storage first (→ 01-04), then find the pharmacy
  and the emergency room on the card above.

## Cross-references

- → 01-03 the movement playbook · → 01-06 loading checklists · → 01-05 destinations
- → 29-07 refrigerated medicines · → 12-21 cooling pouches · → 09-10 power for medical devices
- → 22-05 vehicle kit · → 22-06 medical kit · → 19-01 documents · → 25-09 family medical summary

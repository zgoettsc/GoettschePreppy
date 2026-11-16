---
id: 02-27-a-condition-not-in-the-library
section: 02-medical-conditions
title: "A condition that is not in the library"
version: 1
revised: 2026-11-16
layer: condition
danger_level: caution
phase: [A, B, C]
tags: [condition library, blank module, worksheet, prescriber questions, my meds]
derived_from: [12-11-chronic-conditions]
sources: []
related:
  - 12-11-chronic-conditions
  - 12-07-meds-stockpile
  - 22-06-kit-medical
  - 09-06-charging-medical-devices
  - 09-10-power-for-medical
  - 27-03-protecting-electronics
  - 01-07-evacuating-with-medical-needs
  - 23-02-master-consumables-table
  - 25-09-family-medical-summary
  - 29-07-ex07-refrigerated-medicines
  - 29-14-ex14-reading-a-label
  - 29-15-ex15-how-this-binder-was-made
  - 30-05-dc04-expired-medication
  - 30-09-dc08-heat-exposed-medication
  - 30-16-dc15-someone-elses-prescription
  - 30-17-dc16-antibiotics-without-a-prescription
  - 30-01-the-floors
cards: [DC-04, DC-08, DC-15, DC-16]
explainers: [EX-07, EX-14, EX-15]
promote_when: []
photo_slots:
  - { id: pharmacy-leaflet, caption: "The pharmacy's printed information sheet for each medicine" }
figures: []
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: null
---

# A condition that is not in the library

**This condition is not in the library yet. Fill these headings from your prescriber and your
pharmacy's printed information while you still can.**

**What this page is for.** The condition library has 26 modules (→ 12-11). A household may live
with something else. This page gives that condition the same twelve headings every module uses,
so the person who reads it in an emergency finds the answers in the same places. Fill it in by
hand, in pencil, from the prescriber's answers and the leaflet the pharmacy prints with each
medicine (→ 29-14). Take this page to the next appointment and ask the questions under each
heading. Print one copy per condition. A condition can also be added to the library later
(→ 29-15).

> **SAFETY**
> - **Write only what the prescriber or the printed information says.** Do not fill a heading
>   with a guess; leave it blank and ask.
> - **Ask the prescriber which medicines must never be stopped suddenly**, and write it in part 4.
> - **Children do not have access to firearms, fuel, medications or chlorine products.** (floor,
>   → 30-01).

**Condition:** __________________________________________ **Who:** ____________________

**Prescriber or clinic, and phone:** __________________________________________________

**Filled in by:** ____________________ **Date:** __________

## 1. What it is

In two sentences a stranger would understand:

______________________________________________________________________________________

______________________________________________________________________________________

## 2. What runs out, and how fast

Each medicine, supply and device the condition depends on, and the clock on each (days of
medicine, device life, battery life, refrigeration):

______________________________________________________________________________________

______________________________________________________________________________________

______________________________________________________________________________________

## 3. Storing the medication without power

Heat, cold, freezing, light and moisture rules from each label (→ 29-07, → 29-14). What to do if
it freezes or gets hot:

______________________________________________________________________________________

______________________________________________________________________________________

## 4. Day by day without it

What happens over hours, days and weeks if the medicine or device is lost. **Which medicines must
never be stopped suddenly, and the prescriber's step-down plan if supply runs out:**

______________________________________________________________________________________

______________________________________________________________________________________

______________________________________________________________________________________

## 5. Warning signs that mean an emergency

The signs, and the first aid anyone in the house can give:

______________________________________________________________________________________

______________________________________________________________________________________

______________________________________________________________________________________

## 6. Sick-day basics

What changes with fever, vomiting, diarrhoea, not eating or dehydration. Which medicines to pause
or keep:

______________________________________________________________________________________

______________________________________________________________________________________

## 7. What to stock, and how much

**Days on hand = on hand ÷ used per day.** Every household medicine row is printed; use the ones
for this condition and add the supplies.

| Medicine or supply | On hand | Used per day | Days on hand | Days you want | Still to get |
|---|---|---|---|---|---|
{{#each meds as m}}| {{m.name}} {{m.strength}} ({{m.member}}) | ____ | ____ | ____ | ____ | ____ |
{{/each}}| ____ | ____ | ____ | ____ | ____ | ____ |
| ____ | ____ | ____ | ____ | ____ | ____ |
| ____ | ____ | ____ | ____ | ____ | ____ |

## 8. Sourcing when the pharmacy is closed

Over-the-counter equivalents the pharmacist says are safe, what other households might hold, what
is dangerous to substitute:

______________________________________________________________________________________

______________________________________________________________________________________

## 9. Power and devices

What needs charging or a fridge, how much power it draws (from its label), what breaks in heat or
cold, what to protect from EMP (→ 09-06, → 09-10, → 27-03):

______________________________________________________________________________________

______________________________________________________________________________________

## 10. Travel and evacuation

The supply clock on the road, keeping it cold or warm in a vehicle, what goes in the go-bag
(→ 01-07, → 22-06):

______________________________________________________________________________________

______________________________________________________________________________________

## 11. Decision cards that apply

These four cards touch most medicines; tick the ones that apply to this condition.

- ☐ **Expired medicine:** {{choice DC-04}} (→ 30-05).
- ☐ **Heat-exposed refrigerated medicine:** {{choice DC-08}} (→ 30-09).
- ☐ **Someone else's prescription:** {{choice DC-15}} (→ 30-16).
- ☐ **Antibiotics without a prescription:** {{choice DC-16}} (→ 30-17).

Other cards that apply: ________________________________________________________________

{{photo pharmacy-leaflet}}

## 12. My meds

Every medicine row your household entered is printed. **Tick the rows for this condition**, cross
out the rest, and fill any blank columns by hand.

| For this? | Who | Medicine | Strength | Schedule | Fridge? | If doses are missed (prescriber's words) | Where kept | Days on hand | Expires |
|---|---|---|---|---|---|---|---|---|---|
{{#each meds as m}}| ☐ | {{m.member}} | {{m.name}} | {{m.strength}} | {{m.schedule}} | {{m.refrigerated}} | {{m.if_missed}} | {{m.where_kept}} | {{m.days_on_hand}} | {{m.expiry}} |
{{else}}| ☐ | (no medicines entered yet) | | | | | | ____ | ____ | ____ |
{{/each}}| ☐ | ____ | ____ | ____ | ____ | ____ | ____ | ____ | ____ | ____ |
| ☐ | ____ | ____ | ____ | ____ | ____ | ____ | ____ | ____ | ____ |
| ☐ | ____ | ____ | ____ | ____ | ____ | ____ | ____ | ____ | ____ |

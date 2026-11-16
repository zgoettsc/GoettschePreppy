---
id: 29-07-ex07-refrigerated-medicines
section: 29-explainers
title: "Refrigerated medicines: the cold chain without power"
version: 2
revised: 2026-11-16
layer: explainer
danger_level: critical
phase: [A, B, C]
tags: [medication, insulin, epinephrine, cold chain, refrigerated, storage label, evaporative cooling, thermometer, explainer]
derived_from: [02-02-insulin-without-the-grid, 02-07-epinephrine-storage-and-supply, 02-10-evaporative-cooling-pouches]
sources: [us-fda-information-regarding-insulin-storage-and-swi-6448d3, american-diabetes-association-insulin-storage-and-sy-6f1f94, us-fda-epipen-epinephrine-injection-usp-auto-injecto-a9f17f]
related: [02-01-cl01-type-1-diabetes-injections, 02-02-cl02-type-1-diabetes-pump-and-cgm, 02-03-cl03-anaphylaxis, 02-06-cl06-type-2-diabetes-on-insulin, 12-21-evaporative-cooling-pouches, 12-07-meds-stockpile, 09-10-power-for-medical, 29-14-ex14-reading-a-label, 30-01-the-floors, 30-05-dc04-expired-medication, 30-09-dc08-heat-exposed-medication]
cards: [DC-04, DC-08]
explainers: [EX-02, EX-14]
promote_when: [has.refrigerated_meds, experience.new]
photo_slots:
  - { id: med-cooler, caption: "Our cooler or medical fridge, with the thermometer inside" }
figures: []
plates: []
condition: null
gear: null
explainer: EX-07
card: null
review_pass: { date: "2026-11-16", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "FDA insulin 36-46 F and 59-86 F for up to 28 days re-read, matches 02-01 and 30-09; EpiPen storage re-read (label says nothing about freezing; that claim removed); floor 7 as on 30-01." }
---

# Refrigerated medicines, explained from the beginning

**What this page is for.** Some medicines, insulin above all, lose strength if they get too warm
and are ruined if they freeze. When the power goes, the kitchen fridge stops protecting them.
This page explains the "cold chain", how to read a storage label, and the order of things to try
when there is no working fridge. It gives no doses.

> **SAFETY — the floor that applies (→ 30-01).** **A frozen-then-thawed insulin vial or pen is
> discarded.** Loss of potency with no way to tell; the published guidance is unanimous.
>
> **No derived dosing.** Never change a dose because a medicine got warm. Your prescriber's plan
> and the condition page govern (→ 02-01, → 02-03).

## What "cold chain" means

The **cold chain** is the unbroken run of correct temperatures from the factory to the moment of
use. Every link counts: pharmacy, car, home fridge, cooler, pocket. A break is called an
**excursion**. **Heat is a slope**: the warmer and longer, the more strength is lost, usually
without any visible change. **Freezing is a cliff**: one freeze can ruin the medicine.

## Reading a storage label

The box and the package insert say how to store the product. The words mean:

| Label says | Means |
|---|---|
| "Store refrigerated, 36°F to 46°F (2°C to 8°C)" | Fridge temperature, never the freezer, never against the cooling plate |
| "Do not freeze" / "Discard if frozen" | One freeze ends it, even if it thaws and looks normal |
| "Store at room temperature, 68°F to 77°F (20°C to 25°C); excursions permitted 59°F to 86°F (15°C to 30°C)" | The usual range, and the short swings the maker tested and allows |
| "Once opened (in use), may be kept at room temperature up to N days" | A countdown starts when the vial or pen is first used or taken out of the fridge. Write the date on it |
| "Protect from light" | Keep it in its box |
| "Inspect before use; do not use if cloudy, discoloured or contains particles" | The look-test the maker allows. A normal look does not prove full strength |

Two examples, as published:
- **Insulin:** unopened, in the fridge at 36°F to 46°F. In an emergency, insulin can be kept
  unrefrigerated at 59°F to 86°F for up to 28 days (FDA, Insulin Storage in an Emergency;
  American Diabetes Association). Never frozen. Each product's own label gives its in-use days.
- **Epinephrine auto-injector:** room temperature, 68°F to 77°F, with excursions to 59°F to 86°F
  allowed; **do not refrigerate**; keep it in its carrier tube to protect it from light; replace
  it if the liquid is discoloured, cloudy or has particles (FDA, EpiPen prescribing information).

Expiry dates and lot numbers: → 29-14.

## The fridge-without-power ladder

Try these in order. **At every step, a thermometer decides, not a guess.** A min/max thermometer
(it records the highest and lowest temperature since you last reset it) in each place medicine is
kept, read and written down morning and evening.

1. **A powered fridge kept running.** A small 12-volt medical or travel fridge on a power station
   or generator-charged battery is the most reliable cold chain (→ 09-10, → 29-02). Some go cold
   enough to freeze: set it and check it with the thermometer, not the display.
2. **A cooler with ice or cold packs**, with a towel or box between the ice and the medicine so
   it **cannot freeze**. Keep it shut; add ice before it is gone.
3. **The coolest stable place in the house**: a basement, an interior closet, a cooler set on a
   concrete floor. More stable than living space, but measure it.
4. **An evaporative cooling pouch or clay-pot cooler** for warm weather: water evaporating from
   its surface cools what is inside below the air temperature, but not to fridge cold. The
   pouch maker's instructions set how to soak it and how long it lasts (→ 12-21).
5. **Winter cold, carefully.** An unheated room or porch may sit at fridge temperature, but it
   swings below freezing. Only inside an insulated cooler as a buffer, with the min/max
   thermometer, never below 36°F.

## Decisions on this page

- Using insulin or other refrigerated medicine after a heat excursion: {{choice DC-08}} → 30-09
- Using expired or heat-exposed epinephrine or other expired medicine: {{choice DC-04}} → 30-05

## This household

{{#if has.refrigerated_meds}}Medicines in your profile, with whether each is marked refrigerated:

| Person | Medicine | Refrigerated |
|---|---|---|
{{#each meds as m}}| {{m.member}} | {{m.name}} | {{m.refrigerated}} |
{{/each}}

Put a thermometer with each refrigerated one today.{{else}}No refrigerated medicine is listed in
your profile. If that changes, add it in settings and regenerate.{{/if}}

{{photo med-cooler}}

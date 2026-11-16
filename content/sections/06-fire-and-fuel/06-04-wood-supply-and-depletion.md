---
id: 06-04-wood-supply-and-depletion
section: 06-fire-and-fuel
title: "When the wood runs out (burn rate and sourcing)"
version: 2
revised: 2026-11-16
layer: core
danger_level: critical
phase: [A, B, C]
tags: [firewood, runway, burn rate, cord, scavenging, rocket stove, depletion, carbon monoxide]
derived_from: [06-04-wood-supply-and-depletion]
sources:
  - university-of-missouri-extension-wood-fuel-for-heati-b63761
  - us-epa-burn-wise-heating-with-wood-safe-operation-se-ba0e76
  - cdc-carbon-monoxide-poisoning-basics-772153
  - epa-burn-wise-best-wood-burning-practices-0c1680
related:
  - 06-02-sustaining-fire
  - 06-03-firewood-basics
  - 06-05-alternative-fuels
  - 06-06-fuel-storage-safety
  - 06-09-chimney-and-creosote
  - 07-01-cooking-on-an-open-fire
  - 07-02-rocket-stove
  - 07-05-propane-and-camp-stoves
  - 08-01-heating-one-room
  - 08-02-carbon-monoxide-safety
  - 08-04-emergency-heat-options
  - 23-01-depletion-framework
  - 23-02-master-consumables-table
  - 29-03-ex03-carbon-monoxide
  - 30-01-the-floors
cards: []
explainers: [EX-01, EX-03, EX-12]
promote_when: [has.wood_stove, has.fireplace, has.outdoor_fire]
photo_slots: []
figures: []
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: { date: "2026-11-16", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "Seasoning re-sourced (EPA under 20 percent, at least six months; MU dense hardwoods a year); pine reclassed per species.json (white pine low); unsourced 'twice the heat' and rocket-stove percentages removed; face cord per MU." }
---

# When the wood runs out (burn rate and sourcing)

**What this page is for.** A woodpile that lasts a whole winter of evening fires can be gone in
weeks once it is the only way to cook and boil water every day. This page shows how to work out
how long your wood will last, how to make it last longer, where more comes from, and what not to
burn when you get desperate.

> **SAFETY.** Two ways this kills.
> 1. **Desperation fuel.** Burning treated lumber, plywood, painted, stained or
>    pressure-treated wood, or trash releases poisons (EPA, Best Wood-Burning Practices; MU
>    Extension, Wood Fuel for Heating). Never burn them,
>    especially where anyone breathes the smoke.
> 2. **Carbon monoxide (CO).** Every fire makes CO, a gas you cannot see or smell (CDC; → 29-03).
>    **Never run a generator, charcoal, or any engine indoors, in a garage, or near an open
>    window.** Carbon monoxide kills in minutes with no warning; alarms fail; there is no
>    mitigation that works every time. An outdoor fire, fire pit, rocket stove or grill is
>    outdoor equipment: it never comes inside, not even "for a while" (→ 08-02, → 30-01).

## Do this now

1. **Assume your woodpile is smaller than you think.** Count it in cords (→ 06-03). This
   household's count: **{{ gear.fuel.firewood_cords }} cords**.
2. **Know your cooking fires.** Have at least two ways to cook outdoors in case one fails: an
   outdoor fireplace or fire-pit ring (buildable from blocks or scrap steel), a rocket stove
   (→ 07-02, the most wood-efficient), or a camp stove on propane (→ 07-05).{{#if has.outdoor_fire}}
   Your outdoor fireplace or fire pit is one of them.{{/if}}
3. **Separate the two jobs.** Cooking needs **small, hot, short** fires. Heating needs **large,
   long** fires. Doing both on one outdoor fire burns wood fast. **Cooking and boiling water
   come first** (survival); get heat by the methods in Section 08 (→ 08-04).
4. **Cut use now.** Cook on a rocket stove or small contained fire. Cook in batches and boil
   water in bulk while a fire is going.
5. **Start finding more wood before you are low**, not after.

## How long will it last? Do the arithmetic

1. **Count cords on hand.** A cord is 128 cubic feet (4 × 4 × 8 ft). A face cord or "rick" is
   the same height and length but only one row deep, usually 16 to 24 inches, so it is a third to
   a half of a cord (MU Extension, G5450). Be honest.
2. **Estimate daily use** for how you actually burn: cooking only, or cooking and heating. Weigh
   or count what you burn in a normal day for a few days, and use the average.
3. **Divide** cords on hand by cords per day. That is your **runway**, in days.

Write it here and on the master consumables table (→ 23-02):

| Cords on hand | Cords burned per day | Days of wood |
|---|---|---|
| ______ | ______ | ______ |

A household heating with wood through a cold winter burns **several cords a season**, far more
than a small backyard stack holds.{{#if is.cold_winters}} Your home has cold winters: expect
the high end.{{/if}} If your arithmetic says "weeks", believe it and start finding wood now.

## Three things that change the arithmetic

**Moisture.** Wet ("green") wood wastes much of its energy boiling off its own water, makes
little heat, and coats the chimney with **creosote**, a tar that can catch fire (→ 06-09).
Firewood should be **seasoned to below 20 percent moisture** (EPA, Best Wood-Burning Practices).
That takes **at least six months** split, stacked and covered on top (EPA), and **most dense
hardwoods need at least a year** (MU Extension, Wood Fuel for Heating, G5450). Green wood in a
crisis barely works. A cheap moisture meter tells you what will actually burn.

**Species.** Dense hardwoods such as oak and hickory hold far more heat per cord than light
woods such as cottonwood, willow, boxelder or white pine: MU Extension rates the first "high"
and the second "low" (MU Extension, G5450; → 06-03). A "cord" is not a fixed amount of survival:
if your wood is light, plan on considerably more volume for the same heat.

**Drying time.** Dense woods dry slowly: oak and hickory often need a year or more (MU
Extension). Light woods often dry in one summer. Wood cut this year from the best trees may not burn well until next
winter. Cut standing dead wood first for wood you can burn now.

## Somewhere else may be a different wood world

The trees, and so the firewood, change across the country. Plan each place on its own trees,
not on a generic "cord".

- **Home ({{ region.home.ecoregion }}):** see your region page and its firewood trees (→ 32-00).
{{#each destinations as d}}- **{{d.name}}, {{d.county}}, {{d.state_name}} ({{d.region.ecoregion}}):** see the region page for that state (→ 32-00). If it is open prairie or desert, expect little wood and plan cooking on other fuels (→ 06-05) and heat by other means (→ 08-04).
{{/each}}

Two traps: **in places with little wood**, a cord of light wood gives much less heat than a cord
of oak, so cord arithmetic silently shrinks. **In places with the best wood**, none of it burns well
for about a year after you cut it, so start cutting and stacking on the first visit.

## Gear

**Have now:**

| Item | Why | Notes |
|---|---|---|
| Rocket stove or efficient wood cookstove | Cooks on much less wood than an open fire, and less again with a lid, windscreen and haybox | The biggest single wood saver (→ 07-02) |
| Axe, maul, splitting wedges | Turn rounds into splits that burn | Keep sharp (→ 16-02) |
| Bow saw, spare blades, hand saw | Cut with no power or fuel | Quiet and reliable |
| Chainsaw with fuel, bar oil, files (optional) | Fast while fuel lasts | Runs out; back up with hand tools |
| Moisture meter | Know what will burn | Prevents creosote trouble |
| Tarps, a woodshed, pallets | Season and keep wood dry off the ground | Wet wood is nearly no wood |
| Work gloves, eye protection, first-aid kit | Cutting injuries are common | → 12-01 |
| Fire extinguisher and water | Chimney fires and stray embers | → 29-12; CO alarms → 08-02 |

**If you do not have it, scavenge:**

- **Standing dead trees and fallen limbs**: already partly seasoned, the best crisis wood.
- **Storm debris, downed branches, untreated pallets, untreated scrap lumber, fruit-tree and
  hedge prunings.** In town, wind-downed limbs are plentiful after storms.
- **Bundle small stuff.** Twigs and yard waste burn better tied in bundles or fed to a rocket
  stove.
- **Never burn:** pressure-treated, painted or stained wood; plywood, OSB or particleboard (the
  glues); driftwood (salt); trash; plastics. All release toxic smoke (EPA).

## When it runs out

- **Recount weekly** as the pile shrinks, and update the runway (→ 23-01).
- **Warm the people, not the space:** clothing (→ 11-01), one small heated room (→ 08-01),
  sleeping close together, insulation. Cook in batches so one fire does many meals. Bank coals
  so you relight without wasting kindling (→ 06-02).
- **Other fuels:** propane for cooking is compact and clean (stored as → 06-06); charcoal
  (outdoors only), compressed fire logs and dense biomass (→ 06-05).
- **Always be drying next season's wood.**
- **The trap to avoid:** running the pile to zero, then burning wet, green or toxic wood in
  desperation. Stay a month ahead, and keep a **reserve** you do not touch until you are truly
  cornered.

## Phase notes

- **A (sheltering at home):** the backyard stack plus storm debris; propane as the compact
  backup for cooking. Outdoor fires are for cooking and boiling, not whole-house heat.
  {{#if has.wood_stove}}The wood stove is your heat; guard its wood for that job.{{/if}}
- **B (on the move):** do not haul wood. Carry a compact stove and a little fuel; gather on the
  way.
- **C (settled somewhere new):** more wood, but you must **cut and season ahead**; a winter's
  heat is several cords. Thin windbreaks gently: they protect the house from wind first and are
  fuel second. Keep the chimney clean (→ 06-09). Build a woodshed and stay a season ahead.

---
id: 30-18-dc17-old-fuel
section: 30-decisions-and-floors
title: "DC-17. Old kerosene, diesel or gasoline in a heater or engine"
version: 2
revised: 2026-11-16
layer: card
danger_level: critical
phase: [A, B, C]
tags: [decision card, fuel, kerosene, diesel, gasoline, shelf life, jar test, heater, generator]
derived_from: [06-05-alternative-fuels, 06-06-fuel-storage-safety, 08-10-dyna-glo-kerosene-heater, 09-04-generators, 09-15-generator-maintenance]
sources:
  - ghp-group-inc-dyna-glo-manufacturer-portable-kerosen-477cfd
  - cdc-carbon-monoxide-poisoning-basics-772153
  - cpsc-464-carbon-monoxide-invisible-killer
related: [06-05-alternative-fuels, 06-06-fuel-storage-safety, 08-10-wick-kerosene-heaters, 08-07-ducted-heater-operation, 09-04-generators, 09-15-generator-maintenance, 26-08-expiry-and-rotation-tracker, 29-01-ex01-fuels, 29-03-ex03-carbon-monoxide, 30-06-dc05-fuel-in-attached-garage, 30-02-dc01-unvented-heater-overnight]
cards: [DC-17, DC-05, DC-01]
explainers: [EX-01, EX-03]
promote_when: [has.kerosene_heater, has.diesel_heater, has.generator]
card: DC-17
options:
  - id: fresh-only
    label: "Fresh fuel only, on a rotation schedule"
    summary: "Every can is dated. Gasoline is stabilised when bought and rotated into vehicles on a schedule; kerosene and diesel are used and replaced on a schedule. Fuel past the household's age limit is not burned in heaters or the generator."
  - id: jar-test-and-use
    label: "Jar-test old fuel and use it if it passes"
    summary: "Old fuel may be used if a sample in a clear jar, left to stand, is clear and bright with no water layer, cloudiness, sludge or colour change, and it smells like the right fuel. Any doubt, or an unlabelled can, and it is not used."
settings_summary: "Fuel ages. Gasoline loses the parts that help it start, can absorb water and leaves gum that blocks small-engine carburettors. Kerosene and diesel take up water from the air in part-full cans and can grow sludge. One common wick-heater maker says never use kerosene stored from one season to the next. The real danger is in heaters: the heater maker says old kerosene will not burn properly: smoke, odour, a low flame and deposits on the wick, and a heater burning badly indoors adds carbon monoxide (CO) to the room. Old gasoline in a generator mostly means it will not start when needed. What helps most: date, stabilise and rotate (removes most of it); store full, sealed, cool and dark, and jar-test before every fill (reduces it a lot). An unlabelled or unknown can is never poured."
review_pass: { date: "2026-11-16", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "MU G1999 (404, unread) dropped; Dyna-Glo manual quoted for 1-K and season-to-season rule; CPSC fact sheet (403) swapped for CPSC 464." }
---

# DC-17. Old kerosene, diesel or gasoline in a heater or engine

**What this page is for.** Stored fuel gets old. Throwing it out when no more is coming costs
heat and power; burning it can foul a heater indoors or leave a generator dead. This card
explains what ageing does to each fuel, what the makers say, and what the household decides.

> **SAFETY.** Fuel is never stored or transferred near an open flame or a running appliance
> (floor, → 30-01). **Gasoline is never put in a kerosene heater**: that causes a fire or
> explosion (heater maker's manual). A can with a missing or unreadable label is not poured
> into anything. If a heater smokes, smells strongly or a CO alarm sounds: off, everyone out,
> → 08-02.

## 1. The thing, in plain words

Read → 29-01 for what each fuel is.
- **Gasoline** is a blend that evaporates easily. With age the lightest parts evaporate (it gets
  harder to start an engine), it can take up water (especially blends with ethanol), and it
  leaves gum and varnish in small engines.
- **Kerosene** is a heavier fuel for wick heaters and lamps. **1-K** (also written K-1) is the
  grade refined "to virtually eliminate contaminants such as sulphur" and the only grade a wick
  heater maker allows (heater maker's manual). Kerosene does not "go off"
  quickly, but part-full cans breathe in damp air, collect water at the bottom, and can grow
  sludge.
- **Diesel** behaves like kerosene: water and sludge are the enemies, and they plug filters.
- **Stabiliser** is an additive put in fresh gasoline to slow ageing.
- The **jar test**: pour a sample into a clean clear glass jar and let it stand. Good fuel is
  clear and bright. Water sits as a separate layer or droplets at the bottom; contamination shows
  as cloudiness, sludge, specks or a darker colour.

{{#if has.kerosene_heater}}Your household has a wick kerosene heater. Kerosene on hand: {{ gear.fuel.kerosene_gal }} gal.{{/if}} {{#if has.generator}}Generator fuel: {{ gear.generator_fuel }}. Gasoline on hand: {{ gear.fuel.gasoline_gal }} gal.{{/if}}

## 2. The rule, and why it was set

- A common wick kerosene heater maker says use only **water-clear 1-K kerosene**, and **"NEVER use
  kerosene that has been stored from one season to the next. Kerosene deteriorates over time.
  'OLD KEROSENE' WILL NOT BURN PROPERLY."** It lists what poor kerosene causes: smoke, odour, low
  flame, difficult lighting and excessive deposits on the wick (GHP Group/Dyna-Glo, kerosene
  heater owner's manual).
- Generator and small-engine makers call for clean, fresh gasoline and give storage steps for
  long idle periods.

**Why:** a wick heater works only when the wick soaks up clean fuel evenly. Water and sludge
clog the wick, and the flame burns low, smoky and uneven (heater maker's manual). Fuel that burns
badly burns incompletely, and in an unvented heater everything it makes, carbon monoxide
included, goes into the room (→ 29-03). For engines, stale gasoline is the most common reason
a stored generator will not start.

## 3. How it actually hurts people

- **Kerosene heater indoors:** wet or dirty fuel fouls the wick. The flame burns low and
  smoky; the household turns the wick down to stop the smell, which makes more CO. The family is
  sleeping in a closed room (→ 30-02). CO poisons quietly, and people who are asleep can die
  before they feel ill (CDC, Carbon Monoxide Poisoning: Basics; CPSC, The "Invisible" Killer).
- **Wrong fuel in an old, faded can:** gasoline poured into a kerosene heater makes the flame run
  away: flare-up, fire, explosion.
- **Generator:** stale gasoline gums the carburettor. It will not start on the night it is
  needed, or it surges and stalls, and the insulin fridge or furnace goes without power.
- **Diesel:** water and sludge plug the fuel filter and stop the engine, often at the worst
  moment on the road.

## 4. What makes it safer

**Removes most of the risk**
- **Date every can** on a label, and keep a log (→ 26-08).
- **Rotate**: stabilise gasoline when you buy it and pour each can into a vehicle on a schedule,
  refilling fresh; burn the oldest kerosene first each winter and replace it.
- **Propane** does not go stale; where it fits, it avoids this problem for generators (→ 09-04).

**Reduces it a lot**
- **Store full, sealed, cool and dark.** A full can has little air to breathe and little room for
  water to condense.
- **Jar-test before every fill** of a heater, and before using any can older than your rotation
  limit.
- **Read the label aloud, smell, then pour.** Gasoline smells sharp and stings the eyes;
  kerosene smells oily. The usual can colours (red gasoline, yellow diesel, blue kerosene) are a
  convention, not a guarantee.

**Reduces it a little**
- Run a generator for a short time every month and drain or run it dry for long storage, as its
  manual says (→ 09-15).
- Keep spare wicks and fuel filters; a fouled wick is replaced, not turned down.

## 5. The options

**`fresh-only`: Fresh fuel only, on a rotation schedule.**
You give up: old fuel that might still have burned; you must buy, rotate and dispose of fuel
regularly. You accept: less fuel in a long emergency once fresh supply ends.

**`jar-test-and-use`: Jar-test old fuel and use it if it passes.**
You give up: the heater maker's season-to-season rule. You accept: that the jar test catches
water and sludge but not every problem, so the heater's flame and the CO alarm must be watched
more closely, and any smoky, smelly burn means off and out.

Write your household's age limit for each fuel here: gasoline ______ · kerosene ______ ·
diesel ______.

## 6. Our choice

{{card DC-17}}

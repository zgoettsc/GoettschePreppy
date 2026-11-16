---
id: 30-06-dc05-fuel-in-attached-garage
section: 30-decisions-and-floors
title: "DC-05. Storing gasoline, kerosene or propane in an attached garage"
version: 1
revised: 2026-11-16
layer: card
danger_level: critical
phase: [A]
tags: [decision card, fuel storage, gasoline, kerosene, propane, garage, vapour, fire]
derived_from: [06-06-fuel-storage-safety, 06-07-moving-and-transferring-fuel, 09-04-generators]
sources:
  - us-consumer-product-safety-commission-cpsc-promotes-994cab
  - ghp-group-inc-dyna-glo-manufacturer-portable-kerosen-477cfd
  - cpsc-safety-alert-portable-generator-hazards-r8
  - minnesota-sfm-lp-gas-inside-buildings-r3
  - maryland-mde-gasoline-safety-r3
  - niosh-npg-gasoline-r3
related: [06-06-fuel-storage-safety, 06-07-moving-and-transferring-fuel, 06-05-alternative-fuels, 09-04-generators, 20-02-child-safety-offgrid, 29-01-ex01-fuels, 29-12-ex12-extinguishers-blankets-and-alarms, 30-01-the-floors, 30-18-dc17-old-fuel]
cards: [DC-05, DC-17]
explainers: [EX-01, EX-12]
promote_when: [has.garage, has.generator]
card: DC-05
photo_slots:
  - { id: fuel-storage-spot, caption: "Where our fuel cans and cylinders are kept, with labels visible" }
options:
  - id: outbuilding-only
    label: "Outbuilding or outdoor locker only"
    summary: "Gasoline and kerosene live in a detached shed or ventilated outdoor locker; propane cylinders outdoors, upright. Nothing in the attached garage or the house."
  - id: garage-with-rules
    label: "Attached garage with rules"
    summary: "Approved, labelled cans, caps tight, as far from any heater, water heater or spark as the garage allows; never poured or transferred inside; propane cylinders never in the garage; a written quantity cap."
settings_summary: "Many households keep gas cans in the attached garage, next to the car, the lawn mower and often a water heater or furnace. The danger is not the liquid but its vapour. Gasoline vapour can burn even in deep cold, is heavier than air, travels along the floor and catches fire from a pilot light, igniter, spark or hot engine. CPSC says store fuel outside living areas and away from fuel-burning appliances. A garage fire spreads into the house. Propane cylinders in a garage can vent gas when they warm. What helps most: fuel in a detached shed or outdoor locker (removes most of it); approved sealed cans, far from ignition sources, never opened inside, small quantity (reduces it a lot)."
review_pass: null
---

# DC-05. Storing gasoline, kerosene or propane in an attached garage

**What this page is for.** Stored fuel is one of the most dangerous things in a prepared house.
The garage is the convenient spot. This card explains what the risk is, why codes limit it,
and what the household decides.

> **SAFETY.** Fuel is never stored or transferred near an open flame or a running appliance.
> Children do not have access to firearms, fuel, medications or chlorine products. (Both are
> floors, → 30-01.) If you smell strong fuel vapour in the garage: no switches, no engines,
> open the big door from outside if you can, keep everyone away until it clears.

## 1. The thing, in plain words

- **Gasoline** is car fuel: thin, sharp-smelling, and it evaporates fast (→ 29-01).
- **Kerosene** is a heavier, oily fuel for wick heaters and lamps. It gives off much less
  vapour than gasoline.
- **Propane** is a gas stored as a liquid in steel cylinders.
- An **attached garage** shares a wall, a door and often air with the house. Many hold a
  water heater, furnace or garage heater with a **pilot light** (a small flame that is always
  lit) or an **electronic igniter** (a spark when it starts).

{{#if !has.garage}}Your household has not listed an attached garage. The same physics applies to
fuel kept in a basement, a carport against the house or any room that shares air with it.{{/if}}{{#if has.garage}}Your home has an attached garage. Fuel on hand from your settings: gasoline
{{ gear.fuel.gasoline_gal }} gal, kerosene {{ gear.fuel.kerosene_gal }} gal, 20-lb propane
cylinders {{ gear.fuel.propane_20lb }}.{{/if}}

## 2. The rule, and why it was set

- CPSC says never store generator fuel in the home; store gasoline, propane and kerosene
  outside living areas in properly labelled, non-glass safety containers, and not near a
  fuel-burning appliance such as a gas water heater in a garage (CPSC, Safety Alert: Portable
  Generator Hazards).
- NFPA 58, the propane code, does not allow cylinders larger than 1 lb to be stored or used
  inside a home, attached and detached garages included (Minnesota State Fire Marshal, LP Gas
  Inside Buildings, summarising NFPA 58).
- A common kerosene heater maker says store kerosene only in a container made for kerosene,
  not red, and clearly marked "kerosene", in a well-ventilated place outside the living area
  (GHP Group/Dyna-Glo, kerosene heater manual).

**Why:** gasoline vapour is heavier than air and can travel along the floor to an ignition
source (Maryland Department of the Environment, Gasoline Safety), and it can burn even in deep
cold (flash point −45 °F; NIOSH Pocket Guide, Gasoline). It ignites from tiny sources. A garage gathers exactly those sources: pilot lights, igniters, light switches, a car
or generator engine, tools that spark. A fire there reaches the house through the shared wall
and door.

> **Before the collapse:** your local fire code sets a number for how much gasoline may sit in
> an attached garage. Check it while your fire department can answer. It is a legal limit; the
> physics below is the same with or without it.

## 3. How it actually hurts people

A can's cap is loose, a can cracks in a freeze, or someone tops up the mower inside on a cold
day. Vapour spreads across the floor. The water heater's burner lights on its own, or a car
starts. The vapour cloud flashes back to the can: CPSC warns this can cause an explosion that
can severely burn those nearby (CPSC, Fuel Container Safety, 2023). The fire spreads into the
house through the door. If the fire reaches a propane cylinder, its relief valve vents and
feeds the fire.

A second path: a child finds a can, or fuel ends up in a drink bottle (→ 30-01, floor 9).

## 4. What makes it safer

**Removes most of the risk**
- **Fuel out of the house and garage**: a detached shed or a ventilated, lockable outdoor
  steel locker, shaded. Propane cylinders outdoors, upright, valves closed, away from anything
  that sparks.

**Reduces it a lot** (if fuel stays in the garage)
- **Approved fuel cans only**, caps tight, labelled by fuel, kerosene and gasoline on separate
  shelves. Since July 2023 CPSC has required flame mitigation devices on new fuel containers;
  older cans may not have one (CPSC, Fuel Container Safety, 2023).
- **As far from any pilot light, igniter, heater or engine as the garage allows**, on the
  floor rather than above anything hot.
- **Never pour or transfer fuel inside the garage**, in any season. Carry the can out, pour
  outside, cap it, bring it back (→ 06-07).
- **A small, written quantity cap**: only what you rotate through vehicles and the generator.
- **Propane cylinders never in the garage**, whatever the liquids rule.

**Reduces it a little**
- A listed flammables cabinet.
- An ABC fire extinguisher mounted **outside** the storage spot, so you never reach through a
  fire for it (→ 29-12).
- Spill absorbent (cat litter or sand) and a locked door against children.

{{photo fuel-storage-spot}}

## 5. The options

**`outbuilding-only`: Outbuilding or outdoor locker only.**
You give up: convenience, and the cost of a shed or locker. Fuel kept outdoors can be harder
to reach in a storm and easier to steal. You accept: a short walk.

**`garage-with-rules`: Attached garage with rules.**
You give up: CPSC's advice (fuel outside living areas, away from fuel-burning appliances) and
the safest location. You accept: a store of vapour-producing
fuel sharing a wall with the house, controlled by caps, distance, the never-pour-inside rule
and a quantity cap. Write the cap here: ______ gal gasoline · ______ gal kerosene.

## 6. Our choice

{{card DC-05}}

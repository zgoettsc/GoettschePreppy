---
id: 01-01-phase-a-shelter-in-place
section: 01-phase-playbooks
title: "Phase A: shelter in place"
version: 2
revised: 2026-11-16
layer: core
danger_level: caution
phase: [A]
tags: [phase A, shelter in place, priorities, warm room, water, medicines, timeline, routine]
derived_from: [01-01-phase-a-shelter-in-place]
sources:
  - american-red-cross-power-outage-safety-6d07a8
  - cdc-winter-weather-before-during-and-after-13bbd5
  - cdc-carbon-monoxide-poisoning-basics-772153
related: [01-02-go-no-go-decision, 01-03-phase-b-movement, 01-06-phase-transition-checklists, 08-01-heating-one-room, 03-01-daily-water-needs, 09-16-outage-day-one, 08-02-carbon-monoxide-safety, 23-02-master-consumables-table, 29-07-ex07-refrigerated-medicines]
cards: [DC-01, DC-02, DC-19]
explainers: [EX-03, EX-07]
promote_when: []
photo_slots:
  - { id: warm-room, caption: "Our warm room: heater spot, CO alarm at pillow height, the vents, the barrier" }
figures: []
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: { date: "2026-11-16", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "CO alarm at pillow height (matches 08-02)." }
---

# Phase A: shelter in place

**What this page is for.** How to stay at home and make it work when the power, water, phones or
shops fail. Home is almost always the right answer at first: it is where your supplies, your heat,
your medicine and your beds are.

> **CAUTION.** **Staying is the default, but it is not automatic.** Phase A ends when home stops
> working, and knowing in advance what that looks like is the job of → 01-02. Carbon monoxide
> from heaters, stoves and generators is the way people actually die sheltering at home: **never
> run a generator, charcoal, or any engine indoors, in a garage, or near an open window**, and
> put up a tested CO alarm before any fuel-burning heater is lit (CDC, Carbon Monoxide Poisoning:
> Basics; → 08-02).

## Do this now

1. **Default to staying.** You are better supplied at home than anywhere you can reach.
2. **Work the priority order below. Do not skip ahead.** People die of the boring items.
3. **Get medicines stable first**: the temperature of anything refrigerated (→ 29-07), rescue
   medicines where everyone can reach them (→ 22-06). Those clocks start immediately.
4. **Power, first 24 hours: run → 09-16.** Charge everything to full while the grid flickers:
   phones, power banks, medical devices{{#if has.power_station}}, the power stations{{/if}}
   (→ 00-10, → 09-06).{{#if has.solar}} Put the solar panels out (→ 09-02).{{/if}}
5. **Fill every water container** before the pressure goes (→ 03-02).
6. **Set up one warm room before the house cools**, not after (→ 08-01). Pick an inside room with
   few outside walls and a door that closes, where people can sleep{{#if has.basement}}; a
   basement room stays nearer ground temperature{{/if}}. Never a room with a fuel-burning
   appliance and no window.
7. **Heat, first 24 hours (cold weather), in this order:**
   - {{#if has.gas_any}}If the furnace still has fuel but no power, it needs electricity for its
     blower and controls; running it from a generator or power station needs a safe connection
     (→ 09-04, → 30-08).{{else}}Close the house down to the warm room (→ 08-01).{{/if}}
   - **CO alarms installed and tested BEFORE any fuel-burning heater is lit.** No alarm, no
     heater. One in the warm room at pillow height (→ 08-02).
   - **Only heaters rated for indoor use**, set up as their manual says (→ 08-04, → 08-09,
     → 08-10). Each one burning in a closed room adds carbon monoxide and uses oxygen.
   - Running a fuel-burning heater while people sleep is a trade-off the manuals forbid and some
     households accept with strict rules. **Our choice:** {{choice DC-01}} (→ 30-02)
   - A propane cylinder larger than 1 lb inside the house is another. **Our choice:**
     {{choice DC-02}} (→ 30-03)
8. **Write down the date and time it started.** Everything else is measured from there.

{{photo warm-room}}

## Why / how it works

### The priority order (do not reorder this under stress)
1. **Immediate life safety**: fire, carbon monoxide (→ 08-02), injury, everyone accounted for.
2. **Medical continuity**: refrigerated medicines, rescue medicines, powered devices, counting
   days on hand (Section 02, → 01-07).
3. **Water**: fill everything now; the tap may stop or become unsafe (→ 03-01).
4. **Warmth**: one room, before the house cools (→ 08-01); in summer, shade and moving air
   (→ 17-04).
5. **Information**: NOAA Weather Radio, what happened, for how long (→ 15-01).
6. **Food**: eat what will spoil first (→ 04-17); you have days of slack here.
7. **Sanitation**: decide where waste goes before the toilet stops (→ 13-01).
8. **Security and discretion**: lights, noise, cooking smells, and what neighbours can see (→ 14-03).
9. **Everything else.**

**Water and warmth beat food by a wide margin.** People reliably store too much food and too
little water, sanitation and heat.

### This house, in one table

| | What we have | Page |
|---|---|---|
| Water supply | {{ dwelling.water_supply }} | {{#if has.well}}→ 03-10{{else}}→ 03-02{{/if}} |
| Sewer | {{ dwelling.sewer }} | {{#if has.septic}}→ 13-12{{else}}→ 13-01{{/if}} |
| Main heat | {{ dwelling.primary_heat }} | → 08-04 |
| Basement | {{ dwelling.basement }} | → 08-01 |
| Shelter room | {{ dwelling.shelter_room }} | → 17-06 |
| Stored water | {{ gear.water.stored_gal }} gallons, about {{ derived.water.stored_days }} days at the floor of {{ derived.water.floor_gal_day }} gal/day | → 03-01 |
| Pantry | about {{ gear.food.pantry_days }} days (our estimate) | → 04-01 |
{{#if has.pool}}| Pool or hot tub | about {{ dwelling.pool_gallons }} gallons of non-drinking water until treated | → 03-03, → 30-14 |
{{/if}}{{#if has.water_heater_tank}}| Water heater | about {{ dwelling.water_heater_gallons }} gallons | → 03-02 |
{{/if}}

### The timeline

| Window | The job |
|---|---|
| **First hour** | → 00-06: safety, everyone accounted for, medicines secured, water filling |
| **First 24 hours** | Warm room set up, **CO alarm up, then any heater**, everything charged, information gathered, sanitation plan, eat the fridge first (→ 09-16) |
| **First week** | Routine set, everything counted, runways worked out (→ 23-02), neighbours contacted (→ 18-01) |
| **First month** | Food production started where possible, resupply plans, serious rationing decisions (→ 23-01) |
| **Beyond** | The long game: food production (Section 05), community (Section 18), and the honest question of whether staying still works (→ 01-02) |

### Why staying is usually right
- **Everything is here**: supplies, tools, fuel, water, medicine, and a house you know how to heat.
- **Medical help is usually nearer home** than at a rural destination. For a household whose
  binding limit is a medicine, being near pharmacies and hospitals is a serious argument for
  staying, possibly the strongest one.{{#if is.urban}} In a town or city, that infrastructure is
  likely to come back sooner than in the countryside.{{/if}}
- **Moving is dangerous**, especially in winter{{#if has.child}}, and especially with
  children{{/if}}{{#if has.elder}}, elders{{/if}}{{#if has.mobility_aid}}, or anyone who cannot
  walk far{{/if}} (→ 01-03).
- **You know your neighbours and your streets.** That is real security (→ 18-01).

### What makes Phase A fail
Know these in advance; they are the triggers on → 01-02:
- **A medicine or medical supply runs short** (Section 02, → 01-07).
- **Heat becomes impossible**: fuel gone in deep winter (→ 06-04), house unheatable (→ 08-01).
- **Water becomes unavailable or unsafe** beyond what storage, rain and treatment can cover.
- **The house becomes unsafe**: fire, structural damage, flooding (→ 17-03), or a threat you
  cannot manage (→ 14-01).
- **The neighbourhood changes**: an organised threat, fire spreading, or everyone else leaving.

When to leave is a decision your household writes down in advance, with its own thresholds.
**Our triggers:** {{choice DC-19}} (→ 30-20, → 01-02)

### Living it: the part nobody plans for
Weeks in one warm room is a **social** problem as much as a practical one. Build a **routine**
early: fixed mealtimes, a fixed bedtime, chores, {{#if has.child}}school-ish time (→ 20-03), {{/if}}and
an hour alone for each adult if you can manage it. Morale is a survival system (→ 21-02), and
{{#if has.child}}children take their cues almost entirely from the adults' calm{{else}}people take
their cues from each other's calm{{/if}}.

**Assign roles** (→ 00-07). Who hauls wood while someone else cooks? Who does the daily water and
fuel count? Decide it once rather than every day when you are cold and tired.

## Gear / items

**Have now (buy toward this):**

| Item | Why | Notes |
|---|---|---|
| NOAA Weather Radio (hand-crank or battery) | Information is a Phase A priority | → 15-01 |
| The one-room kit: blankets, plastic sheeting, tape, hooks | Warm room, fast | → 08-01 |
| CO alarms, battery-powered, tested | No alarm, no heater | → 08-02 |
| Water containers, ready to fill | Fill before pressure is lost | → 03-02 |
| Printed inventory sheets | Count what you have, early | → 22-04 |
| A headlamp per person, plus lanterns | Long dark evenings | → 10-01 |
| Power banks and a way to recharge them | Phones, lights, medical devices | → 00-10 |
| This binder, on two devices and printed | The plan when screens are dead | → 00-10 |
| Paper, pencils, a wall calendar | Log days, track runways, keep a routine | Pencil works in the cold |

**Scavenge / substitute:**
- Most of Phase A is arrangement, not equipment: moving what you already own into the right
  configuration.
- Your neighbours' skills and supplies are the largest untapped resource around you (→ 18-01).

## When it runs out

- **Runway:** Phase A lasts as long as your **shortest critical runway**: often a medicine, then
  heating fuel in winter (→ 06-04), then safe water, then food for anyone on a special diet.
  Work out each one (→ 23-02).
- **Ration:** the whole binder is the rationing plan. Recount weekly and write the numbers on
  → 23-02.
- **Resupply / substitute:** local resupply (pharmacies, mutual aid, trade) extends Phase A and is
  nearly always better than moving.
- **The decision:** when a critical runway gets short, that is → 01-02, and it should be a
  **threshold decided in advance**, not a moment of panic.

## Phase notes

- **A (at home):** this page.
- **B (moving):** → 01-03. Only when staying has stopped working.
- **C (establishing elsewhere):** → 01-04. Where you are going, if you go.

## Cross-references

- → 01-02 the go/no-go decision · → 01-06 phase-transition checklists
- → 09-16 outage day one (power and heat sequence) · → 08-01 heating one room · → 08-02 CO
- → 03-01 water needs · → 23-02 the consumables table · → 21-02 morale

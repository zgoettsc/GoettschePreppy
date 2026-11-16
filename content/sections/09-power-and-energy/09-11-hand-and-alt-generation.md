---
id: 09-11-hand-and-alt-generation
section: 09-power-and-energy
title: "Hand-crank, vehicle, wind and other backup generation"
version: 2
revised: 2026-11-16
layer: core
danger_level: caution
phase: [A, B, C]
tags: [power, hand-crank, vehicle, alternator, hybrid, wind, thermoelectric, micro-hydro, backup, carbon monoxide]
derived_from: [09-11-hand-and-alt-generation]
sources:
  - us-department-of-energy-consumer-guide-to-residentia-1d87da
  - us-department-of-energy-solar-energy-technologies-of-2a534a
  - cdc-carbon-monoxide-poisoning-basics-772153
  - us-consumer-product-safety-commission-cpsc-what-to-k-3390a4
  - victron-wiring-unlimited-r14
related:
  - 09-01-power-priorities
  - 09-02-solar-basics
  - 09-04-generators
  - 09-05-solar-in-winter
  - 09-06-charging-medical-devices
  - 09-08-wiring-and-safety
  - 09-14-car-batteries-in-practice
  - 08-02-carbon-monoxide-safety
  - 15-02-radio-options
  - 01-05-choosing-a-destination
  - 22-05-kit-vehicle
  - 29-03-ex03-carbon-monoxide
  - 30-01-the-floors
cards: []
explainers: [EX-02, EX-03]
promote_when: [has.vehicle]
photo_slots: []
figures: []
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: { date: "2026-11-16", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "Unsourced output ranges replaced by rough relative sizes and label/manual methods; socket limit from Victron; wind siting from DOE consumer guide; CO floor wording checked" }
---

# Hand-crank, vehicle, wind and other backup generation

**What this page is for.** Everything here is a backup to solar and batteries, not a plan: what you
use when the panels are buried, the controller has failed, or you are on the move. It ranks the
options by what they actually deliver, and covers the one that is dangerous, a running vehicle.

> **CAUTION: the vehicle is the dangerous one.** A car used as a generator is a fuel-burning engine
> and makes **carbon monoxide**, which you cannot see or smell and which can kill within minutes
> (CDC, Carbon Monoxide Poisoning: Basics). **Never run a generator, charcoal, or any engine indoors,
> in a garage, or near an open window** (→ 30-01): not in an attached garage, not even with the door
> open. Outdoors, exhaust away from the house, carbon monoxide alarms on every level (→ 08-02). In
> snow, **check the tailpipe is not buried**: a drifted exhaust pushes carbon monoxide straight into
> the cabin, and it kills people in vehicles in snowstorms.

## Do this now
- **Buy a hand-crank weather radio with a USB output.** It needs nothing and covers information
  (→ 15-02) and a trickle of emergency phone charge.
- **Learn how to charge from your vehicles**, and keep the cables that do it in the vehicle kit
  (→ 22-05): a high-wattage USB-C car charger for phones and power banks, and the station
  maker's car-charging cable if your station has one.
- **Keep vehicle fuel tanks above half, always.** Half a tank is a real power reserve and a head
  start if you have to leave.

## Why it works this way

**Sort the options by what they deliver:**

These are rough sizes, from largest to smallest; the device's own label or manual gives the real
figure, and a watt meter tells you what you actually get.

| Method | Rough output | Honest verdict |
|---|---|---|
| **Hybrid vehicle in "ready" mode** | Whatever the 12 V socket or inverter allows, engine starting and stopping only as needed | The best vehicle option, far more fuel-efficient than idling a conventional engine |
| Conventional vehicle alternator, engine idling | Hundreds of watts and more through an inverter on the battery | Good, but fuel-hungry at idle. Limited by fuel |
| Vehicle 12 V socket, engine off | Limited by the socket's fuse (Victron: these plugs are not made for more than about 10 A, roughly 120 W) | Small loads only; do not flatten a battery you need to start the vehicle (→ 09-14) |
| Small wind turbine | Far below its rating except in strong, steady wind | Worth it only with open exposure and a tall tower |
| Hand crank (radio, charger) | A few watts while cranking hard | Real but tiny: slow, tiring work for a small charge |
| Bicycle generator | More than a hand crank, for as long as the rider lasts | Exercise, not a power supply |
| Thermoelectric (TEG) stove generator | A few watts while a fire burns | Free power from a fire you were burning anyway |
| Micro-hydro | Continuous, day and night, with real drop and flow | The best of all, **if** you have year-round moving water |

### The vehicle as a generator
**The vehicle is a generator, not a battery.** The engine and alternator make the power; the 12 V
battery only buffers it.

**Our vehicles:**
{{#each vehicles as v}}- {{v.type_text}} ({{v.fuel_text}})
{{else}}- None recorded.
{{/each}}

**Conventional vehicles.** An idling conventional engine burns a lot of fuel to make a trickle of
electricity: very inefficient. Run it in **batches** at a meaningful load, as with a generator
(→ 09-04): charge hard, then shut down. Its fuel is also your evacuation range.

**Hybrids.** A hybrid in "ready" mode, with everything else off, starts and stops its engine by
itself to keep the large traction battery charged. It does not idle continuously: it runs the engine
a few minutes at a time at an efficient load and is silent in between. **That makes charging devices
in ready mode extremely fuel-efficient.** The carbon monoxide rules do not change: **the engine will
start on its own; never ready mode in a garage, and never with a snow-drifted tailpipe.**

**Hybrid cautions:**
- A hybrid's **12 V battery is a small auxiliary battery**, often an AGM type, whose job is to boot
  the computers. It is smaller than a normal starting battery. **Do not deep-cycle it with the
  vehicle off**: take it low and the vehicle may not enter ready mode, the hybrid version of "will
  not start". In ready mode the vehicle maintains it.
- **Jump rules differ** (→ 09-14). Check the owner's manual for the jump point and rules.
- **The high-voltage traction battery is not user-accessible. Never tap, probe or wire to it.**
  Orange cables mean hundreds of volts.

{{#if has.ev}}**Electric vehicles.** An EV is a very large battery. Read its owner's manual for an
accessory or "camp" mode that keeps the 12 V system powered, and for any built-in AC outlet or
vehicle-to-load adapter. The traction-battery rule above applies.{{/if}}

**What each vehicle path charges:**

| Load | Path | Notes |
|---|---|---|
| Phones, power banks, small DC stations | High-wattage USB-C car charger in the 12 V socket | The main use: refills the pocket tier |
| A 12 V medicine cooler | 12 V socket, directly | Native 12 V; no adapter needed (→ 09-10) |
| A larger power station | The station maker's 12 V car-charging cable | **Slow** (the manual gives its car-charging watts, → 28-01): an all-day trickle, not a bulk refill |
| AC loads | An inverter on the 12 V system, fused (→ 09-08) | Small inverters only through the socket (about 10 A at most; → 09-14) |

### Wind: worth it only in the right place
Wind can produce at night, in overcast, and in the middle of a dark winter that has flattened your
solar, and in many open places the windiest months are the least sunny. The caveats are real:
- **Small turbines routinely make far less than their rating**, because the rating assumes a wind
  speed you rarely get.
- **Height is everything.** A turbine on a short pole between houses and trees is close to useless.
  DOE's guidance for a home wind system is at least one acre and an average wind speed of at least
  10 mph, with the tower chosen to clear nearby obstructions and typically 60 to 140 feet tall (US
  Department of Energy, Consumer Guide to Residential Renewable Energy): impractical and
  conspicuous on a town lot, and often against local rules.
- **Moving parts fail:** ice, hail, bearings, gusts.
- **It is noisy and visible** (→ 14-03).

**Verdict: not in town; worth evaluating at a rural site** with open exposure and room for a tower.
A supplement to solar, never a replacement.

### Thermoelectric: small, free, and it fits a wood plan
A TEG (thermoelectric generator) makes a few watts from the temperature difference across a burning
stove. Little, but **you are already burning that fire** to cook or heat, so it is free, it works at
night and in a blizzard, and a few watts charges a phone over a few hours. A good winter backup.

### Hand crank and pedal: the honest floor
Hand-crank output is **a few watts of hard, continuous cranking**: a full phone charge is long,
steady work. Do not build a plan on it. **Do** own a hand-crank radio: the radio
itself uses almost nothing, and information with **no** power dependency is worth a lot (→ 15-02).
A bicycle generator does better but needs a stand, a generator head, a controller and a willing
rider: a settled-site project, not a preparation.

### Micro-hydro: the one that would change everything
Year-round moving water with real drop produces **continuously, day and night, in winter**: the best
off-grid power there is. Put it on the criteria list when choosing a rural site (→ 01-05). Many
streams freeze or dry up.

> **Before the collapse:** water rights and permits apply to diverting a stream.

## Gear and items

**Have it now (buy toward this):**

| Item | Why | Notes |
|---|---|---|
| Hand-crank weather radio with USB out | Information with no power dependency | Also a light and a tiny charger |
| High-wattage USB-C car charger | The right way to charge the pocket tier from a vehicle | One per vehicle |
| Station's 12 V car-charging cable | Trickle-charges a station while driving | Check it is in the kit |
| DC-DC charger | Charges a separate battery bank from an alternator properly | Settled-site or scavenged-vehicle tool |
| 1,000 W inverter with battery clamps and an inline fuse | Turns any vehicle into AC power | Fuse it (→ 09-08) |
| Heavy jumper cables | Charging, jump-starting, salvage cable | |
| TEG stove generator | A few watts from a fire you are burning anyway | Best when solar fails |
| Spare vehicle battery, maintained | Portable storage and a starting reserve | Rotate it |
| **Carbon monoxide alarms** | Any engine anywhere near the house | The recurring answer in this section |

**Scavenge or substitute:**
- **Alternators** from any scrapped vehicle can be belt- or hand-driven into a crude generator.
  Needs a regulator and real speed: a genuine project.
- **Permanent-magnet motors** from treadmills, scooters, power tools and washing machines run
  backwards as generators; treadmill motors are the classic home-built turbine head.
- **Bicycle dynamos and hub generators:** small, but made for this.
- **Every abandoned vehicle** is a lead-acid battery, a 12 V socket and potentially an alternator
  (→ 09-13).
- **What you cannot improvise well:** a charge controller and a good charger. Buy spares.

## When it runs out
- **Vehicle generation ends when the fuel ends**, and that fuel is also your evacuation range.
  Budget it on → 23-02 as **both** miles and watt-hours, and decide in advance which use wins.
- **Hand crank and TEG never run out:** the only truly renewable generation you can carry. That is
  why they are the floor, small as they are.
- **Wind and hydro run as long as you can maintain them;** bearings, blades and controllers are the
  consumables.
- **The order of fallback as things degrade:** solar → generator → vehicle → wind or hydro if built →
  TEG on the cooking fire → hand crank → **nothing, and each medical device falls back to the
  non-electric method in its condition module** (→ 09-06). Every rung buys time; none is permanent.

## Phase notes
- **A (at home):** the vehicles are the big backup (hybrids in ready mode where you have them) and
  the hand-crank radio is the floor. Tanks above half. **No engine running in the garage, ever.**
- **B (moving):** the vehicle *is* the power system while you drive: the USB-C charger keeps phones
  and small medical devices alive, and a 12 V cooler runs from the socket. On foot: a folding panel
  and power banks, with the hand crank as reserve.
- **C (settled somewhere new):** where wind and micro-hydro become worth building. Evaluate the wind
  and water **before** choosing the site (→ 01-05).

## Cross-references
→ 09-04 generators and carbon monoxide · → 09-14 car batteries and hybrid 12 V rules · → 09-06
charging medical devices · → 09-08 wiring and fusing · → 08-02 carbon monoxide safety · → 22-05 the
vehicle kit · → 15-02 radios

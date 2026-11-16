---
id: 30-07-dc06-fuel-in-passenger-vehicle
section: 30-decisions-and-floors
title: "DC-06. Carrying fuel inside a passenger vehicle"
version: 1
revised: 2026-11-16
layer: card
danger_level: critical
phase: [B]
tags: [decision card, fuel, gasoline, propane, vehicle, evacuation, jerrican, vapour]
derived_from: [06-08-fuel-transport, 06-07-moving-and-transferring-fuel, 22-05-kit-vehicle]
sources:
  - us-consumer-product-safety-commission-cpsc-promotes-994cab
  - propane-education-and-research-council-perc-safety-g-40ea6b
  - ecfr-49-cfr-173-6-materials-of-trade-r3
  - maryland-mde-gasoline-safety-r3
  - niosh-npg-gasoline-r3
  - ysn-flame-king-manufacturer-training-program-1a-fill-a69318
related: [06-08-fuel-transport, 06-07-moving-and-transferring-fuel, 22-05-kit-vehicle, 01-03-phase-b-movement, 01-02-go-no-go-decision, 29-01-ex01-fuels, 30-06-dc05-fuel-in-attached-garage, 30-01-the-floors]
cards: [DC-06]
explainers: [EX-01]
promote_when: [has.vehicle, has.destinations]
card: DC-06
options:
  - id: never-inside
    label: "Never inside: roof, hitch carrier or trailer only"
    summary: "Fuel rides outside the passenger space: a roof rack, a hitch-mounted carrier, a pickup bed or an open trailer. If none is available, fuel stays behind and the route is planned on the tank."
  - id: cargo-area-shortest-time
    label: "Cargo area, sealed cans, shortest time"
    summary: "Only when no outside carry exists: approved sealed cans, filled no more than 95 percent, caps tight, upright and strapped in the rear cargo area, windows cracked, emptied into the tank at the first chance. Propane cylinders upright, valves closed."
settings_summary: "When a family has to drive a long way with no fuel stations working, extra gasoline in cans can be the difference between arriving and being stranded. There is no simple agency rule for gasoline cans in a family car; the guidance is to fill cans on the ground, never inside a vehicle, keep them sealed and secured, and never leave propane cylinders in a closed vehicle. Inside a closed car, vapour from a can collects in the cabin and can ignite from a spark. In a rear-end crash, a can behind the back seat can split and burn next to the passengers. Propane in a closed car can leak and pool on the floor. What helps most: carry fuel outside the cabin on a rack, hitch carrier or trailer (removes most of it); approved sealed cans, strapped upright, windows cracked, shortest possible time (reduces it a lot)."
review_pass: null
---

# DC-06. Carrying fuel inside a passenger vehicle

**What this page is for.** If the household ever has to drive somewhere far away with no
working fuel stations, it may want to carry extra fuel. This card explains what the guidance
does and does not say, what actually goes wrong, and what the household decides.

> **SAFETY.** Fuel is never stored or transferred near an open flame or a running appliance
> (floor, → 30-01). Refuel the vehicle from a can with the engine off, outdoors, nobody
> smoking, children kept away.

## 1. The thing, in plain words

A **jerrican** or **fuel can** is a container made and approved for gasoline or diesel
(→ 29-01). **Passenger space** means anywhere people sit and the cargo area of an SUV, van or
hatchback that shares their air. **Outside carry** means a roof rack, a hitch-mounted cargo
carrier, a pickup bed or a trailer.

{{#if has.vehicle}}Your vehicles: {{#each vehicles as v}}{{v.type_text}} ({{v.fuel_text}}); {{/each}}{{#if has.trailer}}You have a trailer.{{/if}}{{/if}}

## 2. The rule, and why it was set

- There is no simple agency rule for a gasoline can inside a family car. What the guidance
  does say: never fill a can inside a vehicle, a trunk or a pickup bed; put it on the ground to
  fill; fill it no more than 95 percent full to allow for expansion; and make sure spilled fuel
  on the can has evaporated before the can goes in the vehicle (Maryland Department of the
  Environment, Gasoline Safety).
- The propane industry says do not leave cylinders inside a vehicle or trunk: the relief valve
  (if the parked vehicle gets too hot) or a leak may release propane, filling the enclosed space
  with flammable gas (PERC, Safety Guide for Portable Propane Cylinders).
- CPSC requires flame mitigation devices on new fuel containers because vapour that escapes a
  can and meets a spark or flame can flash back into it and explode (CPSC, Fuel Container
  Safety, 2023).
- US transport rules for fuel on work vehicles allow no more than 8 gallons per container, in
  packaging that is leak-tight, closed and secured against shifting (49 CFR 173.6, Materials of
  Trade). They were written for businesses, but they show what regulators consider manageable.

**Why:** a closed cabin is a small box. Gasoline gives off vapour that can burn even in deep
cold (NIOSH Pocket Guide, Gasoline), more as it warms in the sun, and the vapour is heavier
than air (Maryland Department of the Environment). It reaches people's lungs and any spark
inside the car. A crash turns a can into a fire next to
the passengers.

## 3. How it actually hurts people

**Vapour.** Cans breathe as they warm. On a warm day the cabin soon smells of fuel.
People get headaches and nausea; a static spark, a phone charger or a cigarette lighter socket
can ignite it.

**Crash.** The rear cargo area is where a rear-end collision lands. A can splits, fuel sprays
over hot metal and the back seat, and the people nearest are children in car seats who cannot
get out by themselves.

**Propane.** A cylinder's relief valve is built to sit in the gas space when the cylinder stands
upright (YSN/Flame King, Training Program 1A); lying on its side, the valve can sit in liquid. A
small leak in a closed car pools on the floor until it finds a spark (PERC).

## 4. What makes it safer

**Removes most of the risk**
- **Carry fuel outside the passenger space**: roof rack, hitch carrier, pickup bed or an open
  trailer (→ 06-08). An enclosed trailer is better than the cabin but still traps vapour in hot
  weather; vent it.
- **Plan the route on the tank** with fewer cans: fill at every chance, carry only what the
  route arithmetic needs (→ 01-03).

**Reduces it a lot** (if fuel must ride inside)
- **Approved cans only, filled no more than 95 percent** (room for expansion; Maryland
  Department of the Environment), caps tight, spouts stowed.
- **Upright and strapped** so cans cannot tip, slide or rub.
- **Windows cracked** the whole time it rides inside.
- **Shortest possible time**: empty the cans into the tank at the first safe stop.
- **Propane upright, valve closed and capped, secured**, never lying down, out of the car as
  soon as you arrive.

**Reduces it a little**
- Fuel as far from the children's seats as the vehicle allows; a barrier between cans and
  bags of food, water and clothing (vapour soaks into fabric, and fuel ruins water).
- No charging devices or loose batteries near the cans.
- Air the vehicle out before anyone climbs in after a stop.

## 5. The options

**`never-inside`: Never inside; roof, hitch carrier or trailer only.**
You give up: extra range if you have no outside carry; you may need more stops, a shorter
route or a different destination. You accept: the risk of running out of fuel.

**`cargo-area-shortest-time`: Cargo area, sealed cans, shortest time.**
You give up: the safest place for fuel. You accept: fuel vapour in the cabin and a fire risk in a
rear-end crash, controlled by sealed full cans, straps, open windows and emptying them early.

## 6. Our choice

{{card DC-06}}

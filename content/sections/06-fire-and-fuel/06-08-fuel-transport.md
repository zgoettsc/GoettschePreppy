---
id: 06-08-fuel-transport
section: 06-fire-and-fuel
title: "Carrying fuel on the road (cans, propane, trailers)"
version: 2
revised: 2026-11-16
layer: core
danger_level: critical
phase: [B]
tags: [fuel, transport, jerrican, propane, trailer, vehicle, vapour, stop discipline, children]
derived_from: [06-08-fuel-transport]
sources:
  - propane-education-and-research-council-perc-safety-g-40ea6b
  - us-dot-phmsa-materials-of-trade-exceptions-49-cfr-17-a40f21
  - nfpa-nfpa-58-liquefied-petroleum-gas-code-storage-of-13af35
  - us-consumer-product-safety-commission-cpsc-promotes-994cab
  - cdc-atsdr-toxfaqs-for-automotive-gasoline-1cb179
  - cdc-how-to-make-water-safe-in-an-emergency-5d78b5
  - maryland-mde-gasoline-safety-r3
  - niosh-fire-hazard-filling-gas-cans-in-pickups-1998-r3
  - ecfr-49-cfr-173-6-materials-of-trade-r3
related:
  - 01-02-go-no-go-decision
  - 01-03-phase-b-movement
  - 03-04-purifying-water
  - 06-06-fuel-storage-safety
  - 06-07-moving-and-transferring-fuel
  - 09-04-generators
  - 16-11-trailer-maintenance-and-repair
  - 17-11-corridor-hazards
  - 19-02-cash-and-value
  - 22-05-kit-vehicle
  - 29-01-ex01-fuels
  - 29-12-ex12-extinguishers-blankets-and-alarms
  - 30-01-the-floors
  - 30-07-dc06-fuel-in-passenger-vehicle
cards: [DC-06]
explainers: [EX-01, EX-12, EX-14]
promote_when: [has.trailer, has.agreed_destination]
photo_slots:
  - { id: fuel-load, caption: "How our fuel rides: cans strapped, propane upright and outside, the barrier" }
figures: [fig-trailer-fuel-load]
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: { date: "2026-11-16", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "Can-filling rule re-sourced (MDE/API, NIOSH); 8 gal / 440 lb verified against 49 CFR 173.6 text; 95 percent fill; PERC page blocked, its rules consistent with DC-06 card." }
---

# Carrying fuel on the road (cans, propane, trailers)

**What this page is for.** If the household has to drive somewhere far away with no working fuel
stations, it may carry extra fuel. This page covers where fuel rides, how to load cans and propane
so they cannot leak, tip or light, how much to carry, and what to check at every stop.

**New to fuels?** → 29-01 explains gasoline, diesel, kerosene and propane.

> **SAFETY.**
> - **Fuel is never stored or transferred near an open flame or a running appliance.** Vapour
>   ignition. Engine off, nobody smoking, when you pour.
> - **Children do not have access to firearms, fuel, medications or chlorine products.** Fixed
>   in every source. Children stay belted in the vehicle at fuel stops.
> - **Never fill a can inside a vehicle, a trunk, a pickup bed or on a trailer floor.** Put it on
>   the ground (CPSC; Maryland Department of the Environment, Gasoline Safety; NIOSH; → 06-07).
> - **Nobody ever rides in a trailer.**
>
> **A closed box in summer sun concentrates vapour.** Cans breathe as they warm, and in a closed
> cabin, trunk or trailer the vapour has nowhere to go. Propane is worse: heavier than air, it
> pools on the floor. Everything below reduces a hazard that cannot be removed.

## Where fuel rides: a decision

Carrying fuel inside the passenger space (the cabin, or an SUV's or van's cargo area that shares
the cabin's air) is a trade-off the household decides: {{choice DC-06}} → 30-07.

The order that keeps it away from people, best first:

1. **Outside the vehicle**: roof rack, hitch-mounted cargo carrier, pickup bed, or an open
   trailer.
2. **An enclosed trailer, vented**, with the steps below.
3. **Inside the passenger space** only if the household's card allows it, with the card's rules.

{{#if has.vehicle}}Your vehicles: {{#each vehicles as v}}{{v.type_text}} ({{v.fuel_text}}){{#if has.trailer}}, can tow: {{v.can_tow}}{{/if}}; {{/each}}{{/if}}
{{#if has.trailer}}**You have a trailer**, so outside carry is possible. The trailer steps below
apply to you.{{else}}**You have no trailer in your settings.** Outside carry means a roof rack,
a hitch-mounted carrier or a pickup bed. If none of those exist, the passenger-space card
applies (→ 30-07).{{/if}}

## Do this now

1. **Write the load plan on the trip card** (→ 01-03): which cans, where each rides, who checks
   them at stops.
2. **Mount propane outside** on a rack or carrier: open-air carriage is far better than inside
   any box.
3. **Check every can**: approved, made after July 2023 (has a flame mitigation device, → 06-07),
   sealed, and labelled with its fuel. Replace any that are not before the first loaded trip.
4. **If you carry fuel in a closed trailer:** check that its roof vent works, or decide which
   door can be safely cracked open while driving. A closed trailer with no vent should not carry
   gasoline in summer.
5. **Practise the load once in the driveway** (cans, straps, barrier, vent) so the first real
   load is not also the first attempt.

{{photo fuel-load}}

## Labels and colours on the road

The usual US colours are **red for gasoline, yellow for diesel, blue for kerosene** (→ 29-01).
A helper or a tired adult at a dark rest stop will trust the colour, so **the label is what
matters**:

- **Every can is labelled** with its fuel in large letters: "GASOLINE — NOT FOR HEATERS",
  "KEROSENE — HEATER ONLY", "DIESEL".
- **If two fuels ride in the same load, they ride apart** (separate tubs, or opposite sides of
  the barrier), every can labelled first.
- **At loading and again at the pour: read the label aloud, smell, then pour.** A can with a
  missing or unreadable label is not poured into anything.
- **Trip fuel is the vehicle's fuel.** Other fuels ride only if the destination plan needs them.
  Write it on the trip card: kerosene riding? yes / no.

## Can to tank: the transfer pump

A hand transfer pump moves fuel from a can into the tank at a stop without lifting a full can to
the filler, and spills less (→ 06-07, method 2).

- **One pump, one fluid. Label each pump with its fluid.** A gasoline pump never moves kerosene;
  a pump used for water never touches fuel, and a fuel pump never touches water.
- The → 06-07 rules apply: outdoors, engine off, no flames or smoking, children belted in the
  vehicle.
- **The pump rides with the fuel**, in a lidded fuel tub. A wet pump gives off vapour and never
  rides in the cabin.
- **Never transfer fuel in a garage** before you leave, even "a quick top-up": roll the vehicle
  out and pour outside (→ 06-06).

## Gasoline in an enclosed trailer: the honest version

{{#if !has.trailer}}(This applies to any closed space fuel rides in: a trunk, a closed
cargo carrier, a cargo van.){{/if}} No arrangement of a closed box makes gasoline in summer sun
safe. What you can do is stack every step:

1. **Approved fuel cans only**, sealed, caps tight, spouts stowed. Never improvised containers
   (→ 06-07).
2. **Upright and strapped.** Cans cannot tip, slide or rub. A can rubbing a strap for hundreds of
   miles wears through.
3. **Full cans**, filled to about 95 percent so the fuel has room to expand (Maryland Department
   of the Environment). A nearly full can has little vapour space; a half-empty can is mostly
   vapour. Fill before you leave.
4. **At the back, by the door**: last in, first out, shortest reach, first to air out when the
   doors open.
5. **Vent the box**: roof vent open, or a door cracked. Moving air is the single best step.
6. **Nothing shares the box with fuel** except behind a barrier: fuel in its own lidded tubs, a
   tarp or plastic-sheet wall between fuel and food, water and clothing. Vapour soaks into
   cardboard and fabric, and water that fuel gets into cannot be made safe (CDC, How to Make
   Water Safe in an Emergency; → 03-04).
7. **Nothing that sparks in the box**: no powered devices, no loose battery packs against metal,
   no lantern "just stored" with the fuel.
8. **Air it out before unloading**: doors open, walk away, let it breathe several minutes before
   anyone works inside. Longer on a hot day.

{{figure fig-trailer-fuel-load}}

**A yardstick from the US Department of Transportation.** DOT's "materials of trade" rules were
written for work vehicles, not family cars, so they are a guide here, not a law: no more than **8
gallons per container**, packaging that is leak-tight, closed, secured against shifting and
protected from damage, and no more than **440 lb** in all (49 CFR 173.6; US DOT/PHMSA, Materials
of Trade Exceptions). Ordinary 5-gallon cans sit inside it. Many small containers are better than
one large one.

## Propane: worse than gasoline in a closed box

Gasoline vapour needs a leak or a breathing cap. **Propane in a closed box needs only a weeping
valve, or the relief valve opening on a hot day**, and then it pools on the floor, heavier than
air, until it finds a spark. The propane industry's rules for cylinders on the road (PERC, Safety
Guide for Portable Propane Cylinders):

- **Upright, always.** A cylinder on its side can put liquid propane at the relief valve. Never
  carry one lying down.
- **Valve closed, plugged or capped**, held against tipping (a rack, a crate-style holder, or a
  ratchet strap to an anchor).
- **A ventilated space only.** The propane code also limits how much propane may ride in a closed
  vehicle; whatever your local figure, treat it as a ceiling, not a plan (NFPA 58).
- **Where it rides, best first:** (1) an open rack or exterior mount; (2) inside a closed trailer
  only with the vent open and the cylinders by the door; (3) never in the passenger space for
  longer than the card allows (→ 30-07).
- **Unload cylinders as soon as you arrive.** Do not leave them in a parked, sun-heated trailer or
  car.

## How much: carry what the arithmetic needs, not what fits

The trip fuel table on → 01-03 is the authority. Work it out there for each destination:

1. Distance to the destination, including a detour.
2. The vehicle's range on a full tank, **towing if you will tow** (towing uses more fuel; measure
   it on a loaded practice drive).
3. The gap between them, with a margin. That gap, in gallons, is what the cans must hold.

{{#each destinations as d}}- **{{d.name}}** (about {{d.approximate_miles}} miles): cans needed ______ ; cans owned ______ .
{{else}}- Destination: ______ (about ______ miles): cans needed ______ ; cans owned ______ .
{{/each}}

**Propane** travels for the stay at the destination: take what the stay needs, mounted outside
first.

Every extra can adds weight{{#if has.trailer}} against the trailer's cargo limit (on its data
plate; → 16-11){{/if}}, more vapour, and more value visible at stops (→ 17-11).

## Stop discipline

- **Park in shade** if there is any. Sun on a dark box drives vapour.
- **At every stop, walk round the load.** Check straps; smell at the door seam or around the cans.
  **A gasoline or propane smell at a closed door stops everything**: doors open, everyone away,
  find the source before driving on.
- **Children stay in the vehicle, belted, engine off, at every fuel stop.** Nobody is near a
  trailer while its doors are open and it airs out.
- **No smoking, no flames, no refuelling while trailer doors are open** downwind.
- Fuel stops are also when you are most exposed on the road. Keep them short (→ 17-11).

## Gear

**Have now:**

| Item | Why | Notes |
|---|---|---|
| Approved 5-gallon fuel cans, enough for the trip arithmetic | The range margin | Made after July 2023, child-resistant (→ 06-07) |
| Labels for every can | Colour alone fails | Large, readable by headlamp |
| Hand fuel transfer pump | Can to tank without lifting | One fluid only, labelled |
| Exterior propane rack or mount | Gets propane out of any box | Roof, hitch, trailer tongue or rear |
| Cylinder holders or ratchet straps and anchors | Upright and immovable | One per cylinder |
| Lidded fuel tubs and a tarp or plastic sheeting | The barrier from food and water | Fuel tubs carry nothing else |
| Ratchet straps and anchor points | Cans that cannot move | Check at every stop |
| ABC fire extinguisher, reachable from outside the load | Fire at a stop | A second one in the vehicle (→ 22-05, → 29-12) |
| Spill absorbent and nitrile gloves with the fuel | A leaking can at a stop | → 06-07 |

**If you do not have it:** straps and tubs can be improvised. **Fuel containers and propane
mounts cannot**: an unsecured cylinder or an unapproved can is the one corner never to cut.

## When it runs out

- **The cans are the range margin** (→ 01-03). A can spent on the way is range spent: recompute
  the gap at every fuel stop against the trip card's turn-back points.
- **Trip fuel feeds the vehicle only.** Do not let a cold night talk anyone into burning trip fuel
  in other equipment.
- **Resupply:** in a partial disruption, cash and small-town pumps on the way (→ 01-03, → 19-02).
  Every gallon bought is a can kept full.
- **Nothing replaces range.** If the fuel aboard plus the tank cannot close the distance, the
  answer is the go/no-go decision (→ 01-02), not hope.

## Phase notes

- **A (sheltering at home):** this page waits. Storage is → 06-06. Keep cans full and rotated so
  leaving is a loading job, not a shopping trip.
- **B (on the move):** this page is for now. Load plan on the trip card; checks at every stop.
- **C (settled somewhere new):** {{#if has.trailer}}the trailer becomes local hauling: same rules,
  shorter runs, same habit of airing it out before unloading.{{else}}local hauling follows the
  same rules, with shorter runs.{{/if}}

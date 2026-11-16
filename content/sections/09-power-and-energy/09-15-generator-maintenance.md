---
id: 09-15-generator-maintenance
section: 09-power-and-energy
title: "Generator maintenance, storage and fuel rotation"
version: 1
revised: 2026-11-16
layer: core
danger_level: caution
phase: [A, C]
tags: [generator, maintenance, oil, fuel, storage, ethanol, propane, stabiliser, troubleshooting, log]
derived_from: [09-15-generator-maintenance]
sources:
  - us-consumer-product-safety-commission-cpsc-what-to-k-3390a4
  - us-consumer-product-safety-commission-cpsc-promotes-994cab
  - cdc-carbon-monoxide-poisoning-basics-772153
  - osha-hand-and-power-tools-safe-use-maintenance-and-h-77254c
related:
  - 09-04-generators
  - 09-14-car-batteries-in-practice
  - 06-05-alternative-fuels
  - 06-06-fuel-storage-safety
  - 06-07-moving-and-transferring-fuel
  - 13-03-greywater-and-trash
  - 22-02-scavenging-field-guide
  - 24-03-seasonal-practice-plan
  - 26-08-expiry-and-rotation-tracker
  - 28-03-generators
  - 29-01-ex01-fuels
  - 30-01-the-floors
  - 30-06-dc05-fuel-in-attached-garage
  - 30-18-dc17-old-fuel
cards: [DC-05, DC-17]
explainers: [EX-01, EX-03]
promote_when: [has.generator]
photo_slots:
  - { id: generator-label, caption: "The label on the generator: run hours, last oil change, oil grade, fuel state" }
figures: [fig-generator-siting]
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: null
---

# Generator maintenance, storage and fuel rotation

**What this page is for.** A generator almost never dies from running. **It dies from sitting**, and
it fails on the one night you need it. This page is the routine that prevents that: a fuel-storage
strategy, exercise runs, oil, the service list, the no-start sequence and the log. Safety, siting and
the first start are on → 09-04.

> **CAUTION. The safety rules do not change because you are only doing maintenance.** **Never run a
> generator, charcoal, or any engine indoors, in a garage, or near an open window**: carbon monoxide
> kills in minutes with no warning (→ 30-01). Run it outdoors, 20 feet or more from the house,
> exhaust pointed away (CPSC, Portable Generator Safety). {{figure fig-generator-siting}}
> **Fuel is never stored or transferred near an open flame or a running appliance** (vapour ignition,
> → 30-01). Never refuel it hot or running. Store fuel in approved, closed containers, cool,
> ventilated, away from ignition and out of children's reach (CPSC, Fuel Container Safety; → 06-06).
> **Your engine's manual governs every interval and specification on this page.**

## Do this now
- **Choose an exercise cadence and put it on the calendar:** at least a few times a year, under load,
  logged. Ours: every ______ , on ______ (fuel). Tie two of the runs to the spring and autumn kit-check
  weekends (→ 24-03).
- **Keep the starting battery charged** the way the manual says (some manuals want a regular charge in
  months it has not run; if the charger is not a maintainer, unplug it after the manual's maximum
  time). A flat starting battery is the likeliest no-start after missing oil.
- **Print your model's manual and keep it with the machine.** Oil type, capacity and intervals are
  model-specific, and you will not have the internet. Copy the key numbers onto → 09-04.
- **Buy the maintenance kit now** (oil, oil filter if fitted, air filter, spark plug) and store it
  **with** the generator.
- **Write the run hours, last oil change, oil grade and fuel state on a label on the machine.** Nobody
  remembers. {{photo generator-label}}

## Why it works this way

### The three things that kill generators
1. **Stale fuel in the carburettor.** Ethanol gasoline absorbs water, separates, and leaves varnish in
   passages narrower than a pin. **The most common cause of a no-start.**
2. **No oil, or oil never changed.** Small engines hold very little oil and forgive nothing.
3. **Rodents.** Nests in the shroud and air box; chewed wiring. Stored equipment is where mice live.

**All three are prevented by one habit: run it under load a few times a year, and look at it while you
do.**

### Fuel: pick a storage state and stick to it
There are three defensible strategies. **The failure is having none.**

| Strategy | How | Best for |
|---|---|---|
| **Run it dry** | Shut the fuel valve and let the engine stall, so the carburettor empties | Gasoline machines used now and then |
| **Store it wet, stabilised** | Fill with stabilised, ideally ethanol-free fuel; run it long enough to draw stabilised fuel through the carburettor | Machines that must start instantly |
| **Never wet it: run on propane** | Dual- and tri-fuel machines | **The strongest option for long storage** |

> **On a multi-fuel generator, running on propane and never putting gasoline in it removes the most
> common failure entirely.** Propane does not go stale, does not absorb water, and leaves nothing in
> the carburettor to varnish (→ 06-05). Once gasoline has been used, **follow the manual's storage
> table** for draining the fuel tank and carburettor bowl by how long it will sit. Copy it here:
>
> | Will sit for | What the manual says to do |
> |---|---|
> | ______ | ______ |
> | ______ | ______ |
> | ______ | ______ |

{{#if has.generator}}Our generator runs on: **{{ gear.generator_fuel }}**.{{/if}} **Whichever
strategy you choose, write it on the label**, so the next person to touch it (including you in three
years) knows what state the machine is in. A generator stored with gasoline in it in an attached
garage is fuel storage in the garage: a decision card, {{choice DC-05}} (→ 30-06).

### The exercise run: what "running it" actually means
A thirty-second idle proves almost nothing.
```
[ ] OUTDOORS, 20+ ft from the house, exhaust pointed away. CO alarms working.  (09-04)
[ ] Check the oil BEFORE starting. Every time. Ten seconds.
[ ] Start it. Note how easily it started, and on which attempt.
[ ] LOAD IT: a space heater, kettle, battery charger, power station on charge.
    A generator run with no load does not clear its carburettor or warm properly.
    (A new machine: stay within the manual's break-in limit.)
[ ] Run 20-30 minutes under that load.
[ ] Listen and look: surging, misfiring, smoke colour, fuel or oil leaks, hot smells.
[ ] Shut down per the manual. If storing dry, shut the fuel valve and let it stall.
[ ] Log the date, run hours, and anything you noticed.
```
**If it runs on more than one fuel:** run it on propane most times, and on gasoline only as often as
your storage strategy needs.

### Oil: the ten-second check that saves the machine
- **Check the level before every run.** Small engines use and lose oil.
- **Change it on the manual's schedule**, and early on a new machine (break-in). If oil has sat unused
  for years, **change it anyway**: it absorbs moisture.
- **Use the grade the manual gives for the temperatures you will run in.** Cold starting is a real
  load on thick oil; manuals usually list a lower-viscosity grade for cold weather. Ours: ________ ,
  capacity ________. Keep two changes' worth with the machine and write the grade on the label.
- **A low-oil shutdown is a protection, not a gauge:** a machine that stops on low oil was already
  running low.
- **Store used oil in a sealed container** and dispose of it properly; never pour it out (→ 13-03).

### The rest of the service list

| Item | When | Notes |
|---|---|---|
| **Air filter** | Check every run; clean or replace per the manual | Also where rodents nest |
| **Spark plug** | Inspect yearly; replace per the manual | Its colour tells you how the engine is running |
| **Fuel filter** | Per the manual | Cheap; replace rather than clean |
| **Fuel lines and primer bulb** | Inspect yearly | Rubber ages even unused. Cracked = replace |
| **Propane hose and regulator** | Inspect yearly | Same ageing. Leak-check with soapy water, never a flame |
| **Starting battery** | Keep charged per the manual; expect to replace | Left unmaintained it sulfates (→ 09-14) |
| **Valve clearance, carburettor rebuild** | Long interval, per the manual | A real job: learn it now or plan to live without it |
| **Cooling fins and air intake** | Every run | Debris and nests cause overheating |

### Fuel rotation: the part that quietly expires
Stored fuel that is never rotated becomes the thing that ruins the engine you were saving it for
(→ 06-06, → 29-01).
```
[ ] LABEL every can with contents and FILL DATE.                       (06-07)
[ ] Rotate stored gasoline through the VEHICLES on a schedule, and refill
    the cans with fresh. Vehicles tolerate older fuel far better than small engines.
[ ] Buy ethanol-free fuel for small engines if you can get it. It stores better.
[ ] Use stabiliser per ITS instructions, added when the fuel is FRESH:
    stabiliser does not repair fuel that has already gone off.
[ ] Putting old or questionable fuel in the generator is a decision: DC-17.
[ ] Propane needs no rotation at all. That is the reason to prefer it. (06-05)
[ ] Record fill dates on 26-08 with everything else that expires.
```
Old fuel: {{choice DC-17}} (→ 30-18).

### When it will not start: work in this order
Do not skip to the carburettor; most no-starts are the first four lines.
```
1. FUEL     Is there fuel? Is the valve OPEN? Is the fuel FRESH?
2. SWITCH   Ignition or battery switch on? Choke set right for a cold engine?
3. OIL      Low-oil shutdown stops many machines from starting. Check the level.
4. LOAD     Anything plugged in? Some machines will not start under load.
            Unplug everything, start, then add load.
5. SPARK    Plug fouled, wet, or wrong gap? A spare plug is the cheapest test there is.
6. AIR      Filter blocked, or a nest in the intake?
7. FUEL DELIVERY  Old fuel or a gummed carburettor. On a dual- or tri-fuel
            machine, TRY IT ON PROPANE: if it runs on propane, the problem
            is the gasoline side. A diagnosis and a workaround in one.
8. BEYOND THAT  Carburettor cleaning or rebuild. Learn it now, or accept the limit.
```
> **The propane test on line 7 is the most useful diagnostic a multi-fuel owner has**, and it keeps
> you running while you deal with the fuel side.

### The maintenance log
```
DATE       RUN HRS   WHAT WAS DONE                      FUEL STATE   NEXT DUE
________   _______   ________________________________   __________   ________
________   _______   ________________________________   __________   ________
________   _______   ________________________________   __________   ________
________   _______   ________________________________   __________   ________
FUEL STATE: DRY (carburettor empty) · WET-STAB (stabilised fuel) · LP (propane only)
```

## Gear and items

**Have it now (buy toward this):** engine oil of the manual's grade (several changes' worth), oil
filter if fitted, **two air filters**, **two spark plugs** and the right plug wrench, fuel filter, spare
fuel line, **fuel stabiliser**, a funnel with a screen, an oil drain pan and a sealable container, a
bottle of soapy water for gas leak checks, **the printed manual**, and a label and marker for the
machine. Store it all **with the generator**. Specs by generator class: → 28-03.

**Scavenge or substitute:** oil in the right grade from vehicle stocks; plugs and filters from other
small engines are sometimes interchangeable, **so check the part numbers; do not guess**; fuel line
from other equipment. **What you cannot substitute is the manual's specifications:** print it while you
can.

## When it runs out
- **Runway:** maintenance parts are consumables. **Count oil changes, not hours:** a generator with fuel
  and no oil is finished.
- **Ration:** stretch intervals only if you must, and never the oil.
- **Resupply:** other small engines (mowers, snowblowers, chainsaws) are the parts bin (→ 22-02).
- **Substitute:** none for oil. **Plan for the generator to be a memory by month two and be fine
  anyway**: solar and batteries are the long-term answer (→ 09-02).

## Phase notes
- **A (at home):** exercise runs on your cadence, the starting battery kept charged, fuel rotated,
  parts stocked, log kept.
- **B (moving):** it travels only outside the passenger cabin, or stays behind (→ 09-04).
- **C (settled somewhere new):** use it hard for setting up (pumping, building), then keep the
  remaining fuel and parts for real emergencies.

## Cross-references
→ 09-04 generators: safety, siting, first start and house connections · → 06-06 storing fuel · → 06-07
moving fuel and judging old fuel · → 06-05 propane · → 09-14 the starting battery · → 26-08 expiry
tracking · → 24-03 the seasonal practice weekends · → 28-03 generators by class

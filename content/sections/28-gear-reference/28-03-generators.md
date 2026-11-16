---
id: 28-03-generators
section: 28-gear-reference
title: "Portable generators: the specs that keep you safe, and common models"
version: 2
revised: 2026-11-16
layer: gear
danger_level: critical
phase: [A, B, C]
tags: [generator, inverter generator, dual fuel, propane, running watts, starting watts, 120/240 V, CO shutoff, run time, altitude, spec table]
derived_from: [28-12-generator-and-fuel, 09-04-generators, 09-15-generator-maintenance]
sources:
  - cdc-carbon-monoxide-poisoning-basics-772153
  - us-consumer-product-safety-commission-cpsc-what-to-k-3390a4
  - honda-eu2200i-owners-manual
  - honda-eu7000is-owners-manual
  - champion-201297-product-page
  - predator-59137-owners-manual
  - generac-gp3500io-owners-manual
  - westinghouse-igen2200-product-page
  - westinghouse-wgen9500dfc-product-page
related: [09-04-generators, 09-15-generator-maintenance, 08-02-carbon-monoxide-safety, 06-06-fuel-storage-safety, 06-05-alternative-fuels, 28-01-power-stations, 28-07-reading-your-own-gear, 29-01-ex01-fuels, 29-03-ex03-carbon-monoxide, 29-04-ex04-electricity-in-the-house, 30-01-the-floors, 30-08-dc07-diy-cord-and-plug-conversion]
cards: [DC-07]
explainers: [EX-01, EX-03, EX-04, EX-14]
promote_when: [has.generator]
photo_slots:
  - { id: generator-plate, caption: "Our generator's data plate and its outlet panel" }
figures: []
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: { date: "2026-11-16", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "All 7 generator rows re-read against the manuals and maker pages (all match); 3.5 %/1,000 ft and 8-104 F (Generac), 3 ft (Honda), floors as on 30-01; generator volts line labelled so a blank reads right." }
---

# Portable generators: the specs that keep you safe, and common models

**What this page is for.** A portable generator is a small engine that turns a generator head and
gives you household power wherever you park it. This page lists the numbers on a generator that
decide what it can run, how long, on what fuel, and how it may be connected, then gives those
numbers for common models from the makers' own manuals and spec pages. How to run, refuel and
connect one safely is on → 09-04; upkeep on → 09-15.

> **SAFETY.** Two floors apply to every generator (→ 30-01).
> **Never run a generator, charcoal, or any engine indoors, in a garage, or near an open window.**
> Carbon monoxide kills in minutes with no warning; alarms fail; there is no mitigation that works
> every time. Run it outdoors, at least 20 feet from any window, door or vent, exhaust pointed
> away (CDC, Carbon Monoxide Poisoning: Basics; CPSC, Portable Generator Safety).
> **Never connect a generator to house wiring except through a transfer switch, or an interlock kit with the main breaker off. Never backfeed through an outlet with a double-male ("suicide") cord.**
> Backfeeding electrocutes line workers and neighbours and starts fires (→ 29-04).

## What matters and why

1. **Running (rated) watts and starting (surge, peak, maximum) watts.** Running watts is what it
   gives all day. Starting watts is a brief burst for motors. A fridge, well pump or furnace
   blower needs several times its running watts for a moment when it starts (→ 09-04). Add the
   running watts of everything on at once and keep a margin; check the biggest motor against the
   starting figure. Some makers print kVA (kilovolt-amps) instead: for planning, 1.8 kVA reads as
   1,800 W.
2. **Fuel.** Gasoline, propane, or both ("dual fuel"); some also natural gas ("tri-fuel").
   **Output is lower on propane**: about 10 % less in the table. Gasoline goes stale in months;
   propane keeps (→ 29-01, → 06-05). Whether stale fuel may be used is a decision card
   (→ 30-18).
3. **Tank and run time, with the load it was measured at.** Makers quote run time at 25 % or 50 %
   of rated load. At full load it is much shorter. Compare like with like.
4. **Inverter or not.** An **inverter generator** makes steady, clean power, throttles down at
   light load and is quieter. A **conventional** ("open frame") generator is cheaper per watt and
   often bigger. Sensitive electronics and some battery chargers are fussy about rougher power:
   test your own charger on your own generator before you need it.
5. **120 V only, or 120/240 V.** Many well pumps run on **240 V**, and a standard residential
   inlet and interlock are 240 V, usually fed from a four-prong twist-lock outlet (L14-30R) or a
   50 A outlet (14-50R). A 120 V-only generator cannot properly drive them. If the manual says it
   is not transfer-switch ready, it is not for one (→ 09-04, → 29-04).
6. **CO shutoff.** Newer models carry a carbon-monoxide sensor that stops the engine when CO
   builds up around it. Makers name it differently: CO-MINDER (Honda), CO Shield (Champion),
   CO SECURE (Predator), CO sensor (Westinghouse). **It protects people near the generator; it
   is not a CO alarm for the house** (Champion says so on its page). Keep battery CO alarms on
   every level and by the beds (→ 08-02).
7. **Altitude and temperature.** Engines lose power in thin air: Honda and Generac both give
   **about 3.5 % less per 1,000 feet** of elevation, and some carburettors need a high-altitude
   kit (Predator: above 3,280 ft). Generac also gives an operating range of 8 to 104 °F and less
   power when hot. {{#if is.high_altitude}}At about {{ region.home.elevation_ft }} ft, plan on
   your generator giving noticeably less than its plate says.{{/if}}
8. **Outlets.** 5-20R is the ordinary household duplex (20 A); TT-30R is the RV outlet (120 V,
   30 A); L5-30R is a 120 V twist-lock; L14-30R and 14-50R are 120/240 V. The outlet decides
   which cord and which connection are possible (→ 09-12).
9. **Distance from the house for fire, too.** Honda's manuals also say to keep the generator at
   least 3 feet from buildings for cooling and fire. That is **in addition to** the 20 feet from
   windows, doors and vents for carbon monoxide, not instead of it.

## Common models, from the makers' own documents

"See label" means the maker's document read for this kit did not give it. Run times say the load
they were measured at.

| Model | Fuel | Running / starting W | Volts | Inverter | Tank | Run time | CO shutoff | Source |
|---|---|---|---|---|---|---|---|---|
| Honda EU2200i | Gasoline | 1,800 / 2,200 (1.8 / 2.2 kVA) | 120 V | Yes | 0.95 gal | See label | Not in the manual edition read; CO-MINDER units: see label | Honda, EU2200i owner's manual |
| Honda EU7000iS | Gasoline | 5,500 / 7,000 (5.5 / 7.0 kVA) | 120/240 V | Yes | 5.07 gal | See label | Yes (CO-MINDER) | Honda, EU7000is owner's manual |
| Westinghouse iGen2200 | Gasoline | 1,800 / 2,200 | 120 V | Yes | 1.14 gal | 12 h at 25 % | No | Westinghouse, iGen2200 product page |
| Predator 3500 inverter (item 59137) | Gasoline | 3,000 / 3,500 | 120 V | Yes | 2.64 gal | 11 h at 25 % | Yes | Harbor Freight (Predator), owner's manual |
| Generac GP3500iO | Gasoline | 3,000 / 3,500 | 120 V | Yes | 2.37 gal | 8.0 h at 50 % | Not in the manual edition read; see label | Generac, GP3500iO owner's manual |
| Champion 3500 W dual fuel (201297) | Gasoline / propane | 3,500 / 4,375 gas; 3,150 / 3,951 propane | 120 V | No | 4.7 gal; propane from a 20-lb cylinder | 14 h gas, 10.5 h propane, at 50 % | Yes (CO Shield) | Champion, model 201297 product page |
| Westinghouse WGen9500DFc | Gasoline / propane | 9,500 / 12,500 gas; 8,500 / 11,200 propane | 120/240 V (L14-30R and 14-50R) | No (conventional) | 6.6 gal | 8 h gas and 7 h propane at 50 %; 12 h gas at 25 % | Yes | Westinghouse, WGen9500DFc product page |

**Read the letters after the model number.** Westinghouse sells the WGen9500DF **without** a CO
sensor and the WGen9500DF**c** with one; the "c" is the only difference in the name. Honda's
manuals for the same model differ by edition. Your data plate and your own manual are the
authority (→ 28-07).

Models from DuroMax and others are left out because the kit could not read their specifications
on the maker's own pages; that is not a judgement of the product.

## Connecting a generator to the house

The floors above decide the first part: a **transfer switch** or an **interlock kit** (with the
main breaker off whenever the generator feeds the panel), or extension cords to single appliances.
Never backfeed. What each one is: → 29-04. How to do it: → 09-04.

A **cord-and-plug conversion** gives one appliance, such as a furnace or well pump, its own plug so
it can be unplugged from the house outlet and plugged into the generator cord. That is not a
connection to house wiring, but whether to do that conversion yourself or have an electrician do
it is a trade-off between cost and the risk of a wiring mistake: {{choice DC-07}} → 30-08.

{{#if has.house_connection}}Our connection: **{{ gear.house_connection }}**.{{/if}}

## Our generator

{{#if has.generator}}From settings: **{{ gear.generator_watts }} running watts**,
**{{ gear.generator_fuel }}**, output volts: **{{ gear.generator_volts }}**.
{{#if has.inverter_generator}}It is an inverter generator.{{else}}It is a conventional (not
inverter) generator: test your battery chargers and electronics on it before you rely on it.{{/if}}
{{else}}We have not entered a generator. If you get one, fill this in from its data plate.{{/if}}

| Item | From our data plate and manual |
|---|---|
| Model and serial number | ______________________ |
| Running / starting watts, gasoline | ______ / ______ W |
| Running / starting watts, propane (if dual fuel) | ______ / ______ W |
| Volts; 240 V outlet type | ______ ; ______ |
| Tank; run time and the load it was measured at | ______ gal; ______ h at ______ % |
| CO shutoff? | yes / no |
| Oil type and amount | ______ |
| Lowest temperature in the manual; altitude kit needed? | ______ °F; ______ |
| Where it runs (20 ft or more from every window, door and vent) | ______________________ |
| How it connects to the house | ______________________ |

{{photo generator-plate}}

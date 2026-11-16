---
id: 28-01-power-stations
section: 28-gear-reference
title: "Power stations: the specs that keep you safe, and common models"
version: 2
revised: 2026-11-16
layer: gear
danger_level: caution
phase: [A, B, C]
tags: [power station, battery, watt-hours, LiFePO4, solar input, Voc, inverter, surge, UPS, cold charging, spec table]
derived_from: [28-02-equipment-inventory, 28-03-solar-fundamentals, 28-06-cross-compatibility, 28-09-battery-care-and-storage, 09-03-batteries-and-storage, 09-07-battery-chemistry]
sources:
  - ecoflow-delta-2-user-manual
  - ecoflow-delta-2-max-user-manual
  - ecoflow-delta-3-max-plus-user-manual
  - ecoflow-river-2-pro-user-manual
  - jackery-explorer-300-plus-user-manual
  - jackery-explorer-1000-v2-user-manual
  - jackery-explorer-1000-v2-us-product-page-r8
  - jackery-explorer-2000-plus-user-manual
  - anker-solix-c1000-gen-2-user-guide
  - anker-solix-f3800-user-guide
  - anker-solix-f3800-plus-product-page
  - bluetti-ac70-user-manual
  - bluetti-ac180-user-manual
  - goal-zero-yeti-1500x-product-page
  - nfpa-national-fire-protection-association-lithium-io-0c7d64
related: [09-03-batteries-and-storage, 09-07-battery-chemistry, 09-02-solar-basics, 09-12-ac-dc-cables-and-connectors, 09-04-generators, 28-02-solar-panels-and-controllers, 28-07-reading-your-own-gear, 29-02-ex02-batteries-and-power-stations, 29-04-ex04-electricity-in-the-house, 30-01-the-floors]
cards: []
explainers: [EX-02, EX-04, EX-14]
promote_when: [has.power_station]
photo_slots:
  - { id: station-labels, caption: "The rating label of each of our power stations, with the solar (DC) input limits readable" }
figures: []
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: { date: "2026-11-16", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "All 13 station rows re-read against the maker documents; Jackery 1000 v2 moved to the US product page (120 V); Anker F3800 given US outlet figures and both firmware current limits from Anker US page (still 60 V); F3800 Plus switch-over filled; DELTA 2 US manual not reachable, AC cell marked." }
---

# Power stations: the specs that keep you safe, and common models

**What this page is for.** A power station is a big battery in a box with its own charger, its
own solar charge controller and its own inverter (the part that makes household-style 120 V AC
power). New to the words volts, amps, watts and watt-hours? Read → 29-02 first. This page lists
the handful of numbers on a power station that decide whether it powers what you need, survives
the cold, and survives the solar panels you plug into it. Then it gives those numbers, from the
makers' own manuals and spec pages, for common models. **The label on your own unit wins over
this table every time** (→ 28-07).

## What matters and why

1. **Capacity, in watt-hours (Wh).** How much energy it holds. A 1,000 Wh station runs a 100 W
   load for very roughly 10 hours, less after inverter losses (→ 29-02). Some makers print the
   cell rating (for example "51.2 V, 20 Ah"); volts × amp-hours = watt-hours.
2. **Chemistry.** "LiFePO4" or "LFP" (lithium iron phosphate) is the longer-lived, less
   fire-prone kind; "NMC" or plain "lithium-ion" packs more energy into less weight. Both are
   lithium and both need the care in → 09-07. The warning signs of a failing lithium battery are
   heat, an odd smell, swelling, leaking, smoke or unusual noise: get people out and do not try to
   carry it (NFPA, Lithium-Ion Batteries; → 09-07).
3. **AC continuous (rated) watts.** The most the inverter delivers all day. Add up what will be
   plugged in at once and stay under it.
4. **AC surge or peak watts.** A short burst for motors starting (fridge, pump, furnace blower).
   Motors can need several times their running watts for a moment (→ 09-04). Some makers also
   advertise a "boost" or "lifting" mode that runs **heating-type** loads (kettle, hair dryer)
   above the rated watts by lowering the voltage; the manuals say it is not for motors.
5. **Solar input: maximum voltage (V), current (A), watts (W) and the connector.** This is the
   number that destroys stations. The station's built-in controller has a voltage ceiling. The
   panels' **Voc** (open-circuit voltage, printed on every panel) added up for panels wired in a
   chain, **times 1.20 for cold mornings**, must stay under that ceiling (→ 09-02, → 28-02). Too
   much current or too many watts only wastes power; too many volts breaks the controller for
   good and the warranty does not cover it. There is also a minimum voltage below which charging
   will not start.
6. **Car-charging input.** Whether it charges from a vehicle's 12 V socket, and at what rate.
   Some share the solar port. Goal Zero, for one, says to use its own 12 V lithium charging cable
   because an ordinary cable can damage the unit (Goal Zero, Yeti 1500X).
7. **Pass-through and UPS.** Many stations pass wall power straight to their outlets while
   charging and switch to battery when the power fails. The makers state a switch-over time
   (10 to 30 milliseconds in the table) and **all of them say it is not a true 0 ms UPS**: test
   any medical or computer device on it before you rely on it (→ 09-06).
8. **Charging and operating temperature.** Lithium must not be **charged** below freezing; most
   stations refuse to charge below 32 °F (0 °C) and some stop discharging below 14 °F or −4 °F.
   A station in a cold garage or car may show full and still refuse to charge from the sun.
   Bring it into the warm room (→ 08-01, → 09-07).
9. **Expansion and the AC output.** Extra battery packs fit only the models the maker lists. The
   AC outlets are for plugging appliances in. **They are never connected to the house wiring**
   except through equipment made for it and installed for it, for the same reason a generator is
   not (→ 30-01, → 29-04, → 09-04).

## Common models, from the makers' own documents

Every number is copied from the document named in the last column. "See label" means the maker's
document read for this kit did not publish it. The EcoFlow DELTA 2 manual read is the European
edition (230 V outlets) and the Anker F3800 guide the British one. The F3800 row takes its US
outlet figures from Anker's US page; the DELTA 2 row is marked, and a US unit's AC outlet figures
may differ. Check those two rows against your own label, the solar input line first. Solar input is per port unless it says total.

| Model | Capacity, chemistry | AC continuous / surge | Solar (DC) input: volts, amps, watts, connector | Car charging | UPS switch-over | Charge / discharge temperature | Source |
|---|---|---|---|---|---|---|---|
| EcoFlow RIVER 2 Pro | 768 Wh, LFP | 800 W / 1,600 W surge, 120 V | 11–50 V, 13 A, 220 W max; XT60 | See label (shares the DC input) | See label | 32–113 °F / 14–113 °F | EcoFlow, RIVER 2 Pro user manual |
| EcoFlow DELTA 2 | 1,024 Wh, LFP | 1,800 W / 2,700 W surge in the EU edition (230 V); US outlets: see label | 11–60 V, 15 A, 500 W max; XT60 | 12 V or 24 V battery, default 8 A | Within 30 ms (EPS) | 32–113 °F / 14–113 °F | EcoFlow, DELTA 2 user manual |
| EcoFlow DELTA 2 Max | 2,048 Wh, LFP | 2,400 W / 4,800 W surge, 120 V | 2 ports, each 11–60 V, 15 A, 500 W; 1,000 W both; XT60 | 12 V or 24 V battery, default 8 A | Within 30 ms (EPS) | 32–113 °F / 14–113 °F | EcoFlow, DELTA 2 Max user manual |
| EcoFlow DELTA 3 Max Plus | 2,048 Wh, LFP | 3,000 W / 6,000 W surge, 120 V (US) | 2 ports, each 11–60 V, 18 A; watts: see label; XT60i | 12 V or 24 V at 8 A; 48 V at 10.4 A (same ports) | See label | 32–113 °F / 14–113 °F | EcoFlow, DELTA 3 Max Plus user manual |
| Jackery Explorer 300 Plus | 288 Wh, lithium-ion | 300 W / 600 W surge, 120 V | USB-C input, 12–27 V, 5 A, 100 W max | 12 V car charger; rate: see label | Within 20 ms | 32–113 °F / 14–113 °F | Jackery, Explorer 300 Plus user manual (JE-300B) |
| Jackery Explorer 1000 v2 | 1,070 Wh, LiFePO4 | 1,500 W / 3,000 W surge, 120 V | 2 × 8 mm (DC8020): 16–60 V at up to 10.5 A each, 400 W max both | Low-voltage range of the same ports: 12–16 V, up to 8 A | Within 20 ms (manual) | 32–113 °F / 14–113 °F | Jackery, Explorer 1000 v2 US product page; user manual (JE-1000D) for the switch-over time |
| Jackery Explorer 2000 Plus | 2,042.8 Wh, lithium-ion | 3,000 W / 6,000 W surge, 120 V | 2 × 8 mm (DC8020): 17.5–60 V at up to 12 A each, 1,400 W max both | Low-voltage range of the same ports: 11–17.5 V, up to 8 A | Within 20 ms | 32–113 °F / 14–113 °F | Jackery, Explorer 2000 Plus user manual (JE-2000C) |
| Anker SOLIX C1000 Gen 2 | 1,024 Wh, LFP | 2,000 W; heating loads up to 2,400 W ("SurgePad"); not for motors per Anker | See label | See label | Within 10 ms | 32–104 °F / −4–104 °F | Anker, C1000 Gen 2 user guide |
| Anker SOLIX F3800 | 3,840 Wh, LiFePO4 | 6,000 W max; 120 V and 120/240 V (US, from Anker's comparison table) | 2 ports, each 11–60 V, 1,200 W each; XT-60. Current limit depends on firmware: 10 A below 32 V and 25 A from 32 to 60 V (older), or 10 A below 15 V and 27 A from 15 to 60 V (newer). **Over 60 V damages it** | Shares the solar ports; see label | 20 ms | 32–104 °F / −4–104 °F (given in °C) | Anker, F3800 user guide (A1790, UK edition), and the F3800 vs F3800 Plus table on Anker's US F3800 Plus page |
| Anker SOLIX F3800 Plus | 3,840 Wh, LFP | 6,000 W max; 120 V and 120/240 V (L14-30R) | 2 ports, each 11–165 V, 17 A, 1,600 W | See label | 20 ms, on the UPS outlets, when plugged into a 120 V wall outlet | See label | Anker, F3800 Plus product page |
| BLUETTI AC70 | 768 Wh, LiFePO4 | 1,000 W; resistive loads to 2,000 W ("Power Lifting") | 12–58 V, 10 A, 500 W max; XT60. **Panels over 58 V Voc must not be used** | 12 V or 24 V socket, through the DC input | 20 ms or less | 32–104 °F / −4–104 °F | BLUETTI, AC70 user manual |
| BLUETTI AC180 | 1,152 Wh, LiFePO4 | 1,800 W; resistive loads to 2,700 W ("Power Lifting") | 12–60 V, 10 A, 500 W max; DC7909 (MC4 cable supplied). **Over 60 V Voc damages it** | 12 V socket, through the DC input | 20 ms or less | 32–104 °F / −4–104 °F (1,500 W max above 86 °F) | BLUETTI, AC180 user manual |
| Goal Zero Yeti 1500X | 1,516 Wh, lithium-ion NMC | 2,000 W / 3,500 W surge, 120 V | High-power port 14–50 V, up to 50 A, 600 W max; 8 mm ports 14–50 V, up to 10 A, 150 W max | Goal Zero 12 V lithium car cable only | See label | Operating 32–104 °F | Goal Zero, Yeti 1500X product page |

**Two lessons hide in this table.** First, the Anker F3800 and F3800 Plus look alike and their
solar ceilings differ by more than 100 volts: a string that suits one destroys the other. Second,
stations from the same maker take panels in different voltage windows (50 V, 58 V, 60 V). **Never
move a panel string from one station to another without redoing the cold check** (→ 28-02).

Models from these makers that the kit looked for but could not confirm from a maker's own
document are left out rather than guessed. Many brands share these designs; whatever you own,
the rating label next to the solar input is the authority (→ 28-07).

## Habits that protect a station

- **Connect panels in the order your manual gives.** Some makers say to connect the panels
  before switching the station on. Write your manual's order on the label photo.
- **Measure Voc with a multimeter** before the first connection of any new panel or string, on a
  cold sunny morning if you can (→ 09-12, → 28-02).
- **One connector fits many things.** An adapter that lets a panel plug in does not make it safe:
  check volts first.
- **Store at part charge in a cool, dry place**, check it monthly, and top it up as the manual
  says (→ 09-03, → 09-07).

## Our power stations

Fill this from the label on each unit (→ 28-07). Photograph each label into the app.

| Model | Wh | Max solar volts | Max solar watts | Solar amps | Connector | Car input | AC continuous / surge | Charge temp limit | UPS? |
|---|---|---|---|---|---|---|---|---|---|
{{#each stations as s}}| {{s.model}} | {{s.wh}} | {{s.pv_input_max_v}} V | {{s.pv_input_max_w}} W | ______ A | ______ | ______ | ______ / ______ W | ______ °F | ______ |
{{else}}| ______ | ______ | ______ V | ______ W | ______ A | ______ | ______ | ______ / ______ W | ______ °F | ______ |
{{/each}}

{{#if has.power_station}}Our stations hold **{{ gear.station_wh_total }} Wh** in all.{{else}}We
have not entered a power station yet. The table above is ready for one.{{/if}}

{{photo station-labels}}

---
id: 28-02-solar-panels-and-controllers
section: 28-gear-reference
title: "Solar panels and charge controllers: the label numbers and common models"
version: 2
revised: 2026-11-16
layer: gear
danger_level: caution
phase: [A, B, C]
tags: [solar panel, Voc, Isc, Vmp, Imp, series, parallel, cold weather, MPPT, charge controller, spec table]
derived_from: [28-03-solar-fundamentals, 28-04-series-vs-parallel, 28-06-cross-compatibility, 28-07-panel-failure, 09-02-solar-basics, 09-08-wiring-and-safety]
sources:
  - renogy-rsp200d-g3-datasheet
  - rich-solar-mega-100-product-page
  - ecoflow-220w-bifacial-panel-product-page
  - ecoflow-400w-lightweight-panel-user-manual
  - bluetti-pv200-user-manual
  - jackery-solarsaga-100-js-100c-user-guide
  - victron-smartsolar-mppt-100-30-100-50-datasheet
  - ecoflow-delta-3-max-plus-user-manual
related: [09-02-solar-basics, 09-05-solar-in-winter, 09-08-wiring-and-safety, 09-09-small-solar-build, 09-12-ac-dc-cables-and-connectors, 28-01-power-stations, 28-07-reading-your-own-gear, 29-02-ex02-batteries-and-power-stations]
cards: []
explainers: [EX-02, EX-14]
promote_when: [has.solar]
photo_slots:
  - { id: panel-labels, caption: "The back label of each of our panels, Voc and Isc readable" }
figures: []
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: { date: "2026-11-16", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "All 6 panel and 2 controller rows re-read against the maker documents (all match); worked example arithmetic checked; added why 1.20 covers the RSP200D to -40 F." }
---

# Solar panels and charge controllers: the label numbers and common models

**What this page is for.** Every solar panel carries a label with four electrical numbers, and
every charge controller (the box, separate or built into a power station, that turns panel power
into battery charge) carries its limits. Matching the two is the whole job. This page explains
the numbers in plain words, shows the cold-weather check with real published figures, and lists
common panels and controllers from the makers' own documents. How solar works and how much it
makes in your season: → 09-02 and → 09-05. Connectors and adapters: → 09-12.

## What matters on a panel, and why

| Label word | Plain meaning | Why it matters |
|---|---|---|
| **Pmax** (rated watts) | Power at the test lab's bright light, 77 °F (25 °C) | Real panels make less: haze, angle, heat. Plan on less |
| **Voc** (open-circuit voltage) | Volts with nothing connected. **The highest voltage the panel makes** | Decides whether you destroy a controller. Always check against Voc, never Vmp |
| **Isc** (short-circuit current) | The most current it can push | Some controllers print a maximum input Isc too. Exceed that and it may be damaged |
| **Vmp, Imp** | Volts and amps while working at its best point | Vmp × Imp ≈ rated watts. Useful for sizing cable, not for safety limits |
| **Temperature coefficient of Voc** | How much Voc rises per degree colder, in % per °C | Lets you work the cold check exactly (below) |
| **Maximum system voltage, maximum series fuse** | Limits for the panel itself in a big array | Matter for fused, multi-panel arrays (→ 09-08) |
| **Connector** | MC4, Anderson, 8 mm (DC8020), DC7909, XT60, USB | A panel that plugs in is not necessarily safe to plug in |

**Series and parallel.** Panels chained plus-to-minus (series) **add their volts**; current stays
that of one panel. Panels joined plus-to-plus and minus-to-minus (parallel) **add their amps**;
volts stay those of one panel. Mixing models in one series string drags every panel down to the
weakest one's current. More on wiring: → 09-02, → 09-08.

## The cold check, every time

Panels are rated at 77 °F. **Colder panels make higher voltage**, and the highest voltage of the
year comes at sunrise on a clear, frozen morning (→ 09-02). The rule this kit uses:

1. Add up the label **Voc** of every panel wired in series.
2. **Multiply by 1.20.**
3. That number must be **below** the controller's or station's maximum solar input voltage.

**A worked example with published numbers.** The Renogy RSP200D datasheet (third-generation
sheet) gives Voc 23.0 V and a Voc coefficient of −0.28 % per °C. At −40 °F (−40 °C, 65 °C below the
lab's 77 °F) that panel's Voc rises by 0.28 × 65 ≈ 18 %, so the 1.20 factor covers it. A panel
with a larger coefficient, or a place colder than that, needs its own factor (method: → 09-02).

- Two in series: 46.0 V × 1.20 = **55.2 V cold**. Under a 60 V station limit. **Over** a 50 V
  limit: on such a station, that string will damage it.
- Three in series: 69.0 V × 1.20 = **82.8 V cold**. Over any 60 V station; under a 100 V
  controller.
- Four Rich Solar MEGA 100 panels in series: 4 × 22.8 V = 91.2 V; × 1.20 = **109.4 V cold**. Over
  a 100 V controller even though the warm number looks fine.

**Same name, different numbers.** Makers revise panels and mark it only with a small revision
code (the sheet above is "G3"). **Use the label on your own panel, and a multimeter reading in
full sun, not the catalogue** (→ 28-07).

**The three controller limits are not equally dangerous.** Too many volts breaks the controller
input at once and for good. Too many watts or amps is usually clipped: the controller takes what
it can and wastes the rest. The exception is a **maximum PV short-circuit current**, where the
maker prints one: Victron says an array with a higher short-circuit current may damage the
controller, and EcoFlow tells you to keep total Isc within 18 A on the DELTA 3 Max Plus ports
(Victron, SmartSolar MPPT 100/30 and 100/50 datasheet; EcoFlow, DELTA 3 Max Plus user manual).
**When in doubt, choose the wiring that keeps volts lower.** Wasted watts are free; a dead
controller is not.

## Common panels, from the makers' own documents

STC means the lab's standard test: bright sun (1,000 W per square metre) and a 77 °F panel.
"See label" means the maker's document read for this kit did not give it.

| Panel | Rated W | Voc | Isc | Vmp | Imp | Connector, other limits | Source |
|---|---|---|---|---|---|---|---|
| Renogy RSP200D (rigid, glass) | 200 | 23.0 V | 11.05 A | 19.2 V | 10.42 A | MC4; Voc coefficient −0.28 %/°C; max series fuse 20 A; operating −40 to 185 °F | Renogy, RSP200D datasheet (G3) |
| Rich Solar MEGA 100 (rigid) | 100 | 22.8 V | 5.78 A | 18.6 V | 5.38 A | MC4; max series fuse 10 A; operating −40 to 185 °F | Rich Solar, MEGA 100 product page |
| EcoFlow NextGen 220 W bifacial portable | 220 front (175 rear) | 21.5 V | 12.4 A front | 18.4 V | 11.9 A front | "Photovoltaic connectors"; IP68 | EcoFlow, 220 W bifacial panel product page |
| EcoFlow 400 W lightweight portable | 400 | 39.3 V | 12.2 A | See label | See label | Cable to XT60/XT60i station input | EcoFlow, 400 W lightweight panel user manual |
| BLUETTI PV200 (folding) | 200 | 26.1 V | 10.3 A | 20.5 V | 9.7 A | MC4; operating 14 to 149 °F (given as −10 to +65 °C); IP65, not waterproof | BLUETTI, PV200 user guide |
| Jackery SolarSaga 100 (JS-100C) | 100 | 24.8 V | 5.6 A | 20 V | 5 A | DC7909 plug, DC7909–DC8020 adapter; USB-A and USB-C outputs; operating −4 to 149 °F | Jackery, SolarSaga 100 user guide |

Notice the folding panels: **two of the 26.1 V panels in series reach about 62.6 V cold**, already
over a 60 V station. Folding panels made for one brand's station are often meant to be used one
at a time or in parallel; their manual says which.

## Charge controllers

A separate controller sits between panels and a battery (a 12 V or 24 V battery bank, not a power
station, which has its own). The model name of many controllers is the limits: "100/30" means a
100 V solar input ceiling and 30 A of charging current.

| Controller | Battery | Charge current | Max solar Voc | Max solar Isc | Panel watts it uses at 12 V / 24 V | Notes | Source |
|---|---|---|---|---|---|---|---|
| Victron SmartSolar MPPT 100/30 | 12/24 V auto | 30 A | 100 V | 35 A | 440 W / 880 W | Solar volts must be at least battery volts + 5 V to start; full output to 104 °F, operating −22 to 140 °F | Victron, SmartSolar 100/30 and 100/50 datasheet |
| Victron SmartSolar MPPT 100/50 | 12/24 V auto | 50 A | 100 V | 60 A | 700 W / 1,400 W | As above | Victron, same datasheet |

More panel than the "watts it uses" figure is allowed by Victron: the controller limits what it
takes. More **volts** than 100 is never allowed. Other controllers (Renogy, Rich Solar, EPEver and
others) print the same three limits on their side label; the kit could not confirm a Renogy
controller sheet from Renogy's own site and left it out rather than guess.

## Our panels

From the back of each panel (→ 28-07). The cold column is your series string's total Voc × 1.20.

| Panel | Watts | How many | Voc | Isc | Vmp / Imp | Connector | Wired as | String Voc cold (× 1.20) |
|---|---|---|---|---|---|---|---|---|
{{#each panels as p}}| {{p.model}} | {{p.watts}} | {{p.count}} | {{p.voc}} V | {{p.isc}} A | ______ / ______ | ______ | series / parallel | ______ V |
{{else}}| ______ | ______ | ______ | ______ V | ______ A | ______ / ______ | ______ | series / parallel | ______ V |
{{/each}}

{{#if has.solar}}Our panels total **{{ gear.solar_w_total }} W**. A rough December day gives about
**{{ derived.solar_wh_dec }} Wh** and a June day about **{{ derived.solar_wh_jun }} Wh**
(estimates, → 09-05).{{/if}}

**Our controllers and what each panel string feeds:**

| Controller or station input | Max solar volts | Max Isc | Which string | Cold string Voc | Under the limit? |
|---|---|---|---|---|---|
| ______ | ______ V | ______ A | ______ | ______ V | yes / **no: rewire** |
| ______ | ______ V | ______ A | ______ | ______ V | yes / **no: rewire** |

{{photo panel-labels}}

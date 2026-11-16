---
id: 26-05-checklist-heat-power-light
section: 26-pre-disaster-acquisition-checklist
title: "Checklist 3: heat, power and light"
version: 2
revised: 2026-11-16
layer: core
danger_level: caution
phase: [A]
tags: [checklist, heat, cooling, firewood, fuel, heaters, generator, power station, solar, lighting, cooking]
derived_from: [26-05-checklist-heat-power-light]
sources:
  - cdc-carbon-monoxide-poisoning-basics-772153
  - american-red-cross-winter-storm-preparedness-and-bli-4bb6c0
  - us-consumer-product-safety-commission-cpsc-what-to-k-3390a4
  - cpsc-warns-of-dangers-after-a-hurricane-or-power-outage-2006-r7
  - university-of-missouri-extension-wood-fuel-for-heati-b63761
  - noaa-national-weather-service-heat-safety-66fd15
related: [08-01-heating-one-room, 08-02-carbon-monoxide-safety, 08-04-emergency-heat-options, 06-03-firewood-basics, 06-06-fuel-storage-safety, 09-01-power-priorities, 09-04-generators, 09-05-solar-in-winter, 09-10-power-for-medical, 10-01-lighting-options, 07-01-cooking-on-an-open-fire, 26-09-shopping-list-and-budget, 17-04-extreme-cold-and-heat]
cards: [DC-01, DC-02, DC-05, DC-07, DC-17, DC-20, DC-21]
explainers: [EX-01, EX-02, EX-03, EX-04]
promote_when: []
photo_slots: []
figures: []
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: { date: "2026-11-16", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "Generator 20 ft added (CPSC); 'hundreds of cars' re-cited to CPSC release; seasoning aligned with G5450." }
---

# Checklist 3: heat, power and light

**What this page is for.** The third sheet of the walk (→ 26-01): how you will stay warm (or
cool), make power, see after dark, and cook when the grid is down. {{#if is.cold_winters}}In your
winters (January mean low {{ region.home.jan_low_f }} °F) heat is a life-safety item, not a comfort
one.{{else}}{{#if is.hot_summers}}In your summers (July mean high {{ region.home.jul_high_f }} °F) cooling is a life-safety item,
not a comfort one.{{else}}A long outage in the worst week of your year is the case to plan for.{{/if}}{{/if}}

> **CAUTION: the safety rules on this page are not optional.**
> - **Never run a generator, charcoal, or any engine indoors, in a garage, or near an open
>   window.** CPSC: one generator makes as much carbon monoxide as hundreds of idling cars
>   (CPSC, news release, 2006). Run it outdoors, at least 20 feet from the house (CPSC, Portable
>   Generator Safety).
> - **Never connect a generator to house wiring except through a transfer switch, or an interlock
>   kit with the main breaker off. Never backfeed through an outlet with a double-male
>   ("suicide") cord.**
> - **Fuel is never stored or transferred near an open flame or a running appliance.**
> - **Anything that burns indoors needs a working battery CO alarm first** (CDC, Carbon Monoxide
>   Poisoning: Basics; → 08-02), and only heaters rated for indoor use belong inside.

**Marks:** ✔ have it, it works, I know where it is · ~ partly, or needs a spare · ✗ do not have

## A. Heat

Our main heat: {{ dwelling.primary_heat }}. Without power it {{#if has.gas_any}}may still need
electricity for its fan or ignition{{else}}stops{{/if}}: check (→ 08-04).

| ✔ ~ ✗ | Item | Amount | Notes | Page |
|---|---|---|---|---|
| [ ] | Firewood, **seasoned** (settings: {{ gear.fuel.firewood_cords }} cords) | ______ cords | Split and stacked since: ______ | → 06-03 |
| [ ] | Firewood, green (next year's) | ______ cords | | → 06-03 |
| [ ] | Wood covered on top, open at the sides | | | → 06-03 |
| [ ] | Axe, splitting maul, wedges | ______ | | → 16-06 |
| [ ] | Bow saw + **spare blades**; chainsaw + file + chaps | ______ | | → 16-06 |
| [ ] | Moisture meter (target under 20 %) | ______ | | → 08-08 |
| [ ] | Fireplace or wood stove{{#if has.fireplace}} **(this household)**{{/if}}{{#if has.wood_stove}} **(this household)**{{/if}} inspected and swept this year; chimney brush sized to the flue; chimney-fire suppressant | | Using an uninspected one: {{choice DC-21}} → 30-22 | → 06-09 |
| [ ] | Outdoor fire pit or fireplace{{#if has.outdoor_fire}} **(this household)**{{/if}} + grate and tools | | | → 07-01 |
| [ ] | An indoor-rated heater for one room{{#if has.unvented_heater}} **(this household owns one)**{{/if}} | ______ | Overnight use: {{choice DC-01}} → 30-02 | → 08-04 |
| [ ] | Its spares: wicks, filters, hoses, fuses | ______ | | → 08-09, → 08-10 |
| [ ] | Propane 20-lb cylinders (settings: {{ gear.fuel.propane_20lb }}), stored outdoors, upright, valves closed | ______ | Full / part: ______. Bigger than 1 lb indoors: {{choice DC-02}} → 30-03 | → 06-05 |
| [ ] | Propane 1-lb cylinders (settings: {{ gear.fuel.propane_1lb }}) + adapter | ______ | | → 07-05 |
| [ ] | Kerosene, **1-K grade** (settings: {{ gear.fuel.kerosene_gal }} gal), in labelled cans | ______ gal | Bought on: ______. Old fuel: {{choice DC-17}} → 30-18 | → 29-01 |
| [ ] | Fuel cans **labelled**, caps tight, away from ignition | ______ | Attached-garage storage: {{choice DC-05}} → 30-06 | → 06-06 |
| [ ] | One-room plan hardware: window film, weatherstripping, door sweeps, plastic sheeting, tape | | | → 08-01 |
| [ ] | Heavy blankets, sleeping bags rated for your coldest nights ({{ region.home.record_low_f }} °F on record) | ______ | Rated to: ______ | → 08-06 |
| [ ] | Ignition three ways: lighters, matches, ferro rod; tinder | ______ | | → 06-01 |
{{#if has.house_connection}}| [ ] | **Generator connection to the furnace or well (this household: {{ gear.house_connection }})** tested before it is needed | | Doing a cord-and-plug conversion yourself: {{choice DC-07}} → 30-08 | → 09-04 |
{{/if}}

```
DAYS OF HEATING + COOKING FUEL, HONESTLY: ________   (06-04)
```

> **Wood cut this year is next year's fuel**: seasoning takes months, and dense hardwoods at
> least a year (University of Missouri Extension, Wood Fuel for Heating; → 06-03). If your only stack is green, your real number is
> zero.

## B. Cooling{{#if is.hot_summers}} (this household: hot summers){{/if}}

| ✔ ~ ✗ | Item | Count | Page |
|---|---|---|---|
| [ ] | Battery or USB fans, with a way to charge them | ______ | → 17-04 |
| [ ] | Reflective window covering for the sunny side; shade cloth | ______ | → 17-04 |
| [ ] | Spray bottles, cooling towels | ______ | → 17-04 |
| [ ] | A cooler room chosen (lowest floor, shaded side) | | → 17-04 |
| [ ] | Extra water for heat (more than the plan figure) | ______ gal | → 03-01 |
| [ ] | Every adult knows heat exhaustion and heat stroke (NWS, Heat Safety) | | → 17-04 |

## C. Power

**Settings:** power stations {{ gear.station_wh_total }} Wh · solar {{ gear.solar_w_total }} W ·
generator {{ gear.generator_watts }} W ({{ gear.generator_fuel }}, {{ gear.generator_volts }}).

| ✔ ~ ✗ | Item | Spec / count | Notes | Page |
|---|---|---|---|---|
| [ ] | **Power for medical devices first**: power banks or a station, sized and **tested**{{#if has.cpap}} **(this household: CPAP)**{{/if}}{{#if has.oxygen}} **(this household: oxygen)**{{/if}}{{#if has.refrigerated_meds}} **(this household: medicine fridge)**{{/if}} | ______ Wh | Measured runtime: ______ h | → 09-10 |
| [ ] | Power stations, charged; their label limits for heat and cold read | ______ Wh | | → 09-03 |
| [ ] | Solar panels + charge controller, stored dry; cables fit the station | ______ W | | → 09-02 |
| [ ] | 12 V accessories: inverter, socket splitter, USB-C car charger | ______ | | → 09-11 |
| [ ] | Jump pack (also charges devices) | ______ | | → 22-05 |
| [ ] | Rechargeable AA/AAA + a charger that runs from 12 V or USB | ______ | | → 09-03 |
| [ ] | Alkaline batteries in the sizes your devices take | ______ | Expiry: ______ | → 09-03 |
| [ ] | Multimeter, fuses, wire, connectors | ______ | | → 09-08 |
| [ ] | Generator{{#if has.generator}} (owned){{/if}}: started under load this season; oil in | ______ W | | → 09-04, → 09-15 |
| [ ] | Generator's **outdoor run spot** chosen and marked: at least 20 feet from every window, door and vent, exhaust pointing away | | | → 09-04 |
| [ ] | Heavy-duty outdoor extension cords sized for the load | ______ | | → 29-04 |
| [ ] | Watt-meter or battery monitor | ______ | | → 25-02 |

```
MEDICAL DEVICE RUNTIME OFF-GRID, MEASURED: ________ hours   (09-10, 24-04)
SOLAR, DECEMBER (estimate): {{ derived.solar_wh_dec }} Wh/day   vs MEDICAL NEED: ________ Wh/day
```

> **Size the system for medical devices and phones first** (→ 09-01), and for **December, not
> June**: winter output is a fraction of summer's (→ 09-05).

## D. Light

| ✔ ~ ✗ | Item | Count | Page |
|---|---|---|---|
| [ ] | **LED headlamp, one per person** ({{ household.size }}) | ______ | → 10-01 |
| [ ] | Spare batteries for each | ______ | → 10-01 |
| [ ] | Lanterns | ______ | → 10-01 |
| [ ] | Candles (open flame indoors: {{choice DC-20}} → 30-21) | ______ | → 10-02 |
| [ ] | Oil lamps + lamp oil + **spare wicks** | ______ | → 10-02 |
| [ ] | Materials to make candles or lamps (fat, wick) | ______ | → 10-04 |
| [ ] | Blackout curtains or window covering | ______ | → 10-05 |
| [ ] | Solar garden lights (free light, brought in at night) | ______ | → 10-03 |

> **One headlamp per person, not per household.** Several people sharing two lights is a "~".

## E. Cooking without the grid

| ✔ ~ ✗ | Item | Count | Page |
|---|---|---|---|
| [ ] | Cast iron: Dutch oven, skillet, griddle | ______ | → 07-04 |
| [ ] | Grill grate, tripod, long tongs | ______ | → 07-01 |
| [ ] | Heavy heat-resistant gloves | ______ | → 07-01 |
| [ ] | Camp stove + fuel, **outdoor use** | ______ | → 07-05 |
| [ ] | Efficient or rocket stove | ______ | → 07-02 |
| [ ] | Solar oven, bought or built | ______ | → 07-03 |
| [ ] | Large pots with lids; vacuum flasks | ______ | → 07-02 |

## F. The safety gate (do not skip)

| ✔ | Check | Page |
|---|---|---|
| [ ] | A battery CO alarm on every level, outside every sleeping area, and wherever **anything** burns | → 08-02 |
| [ ] | A CO detector **with a number (ppm) display** on every level: it shows a slow leak early | → 08-02 |
| [ ] | The generator's outdoor spot is known to every adult | → 09-04 |
| [ ] | **Nothing unvented that is not rated for indoor use** is stored where someone might use it indoors "just this once" | → 08-04 |
| [ ] | Fuel is away from the living space and ignition, in labelled containers | → 06-06 |
| [ ] | Chimney, stove or fireplace inspected this year | → 06-09 |

## The lines that matter

```
DAYS OF HEAT FUEL:   ________     DAYS OF COOKING FUEL:  ________
HEADLAMPS:           ________ of {{ household.size }}
CO ALARMS WORKING:   ________

BIGGEST GAP: ______________________________________________
```

Related: → 06-03 and → 06-04 firewood and running out · → 08-01 heating one room · → 08-02
carbon monoxide · → 09-01 power priorities · → 09-05 winter solar · → 09-10 medical power ·
→ 10-01 lighting · → 07-01 cooking outdoors · → 26-09 the shopping list.

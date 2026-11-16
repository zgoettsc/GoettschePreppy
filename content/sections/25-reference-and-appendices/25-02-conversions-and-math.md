---
id: 25-02-conversions-and-math
section: 25-reference-and-appendices
title: "Conversions, water and calorie math"
version: 3
revised: 2026-11-16
layer: core
danger_level: none
phase: [A, B, C]
tags: [conversions, units, water math, calories, fuel, BTU, electricity, travel rates]
derived_from: [25-02-conversions-and-math]
sources:
  - cdc-how-to-create-and-store-an-emergency-water-suppl-f0c412
  - us-epa-emergency-disinfection-of-drinking-water-6aa91f
  - cdc-how-to-make-water-safe-in-an-emergency-5d78b5
  - fema-477-food-and-water-in-an-emergency
  - foodsafety-gov-usda-hhs-cook-to-a-safe-minimum-inter-13daf3
  - foodsafety-gov-usda-hhs-food-safety-during-a-power-o-3894c1
  - noaa-national-weather-service-wind-chill-chart-frost-89f6d7
  - university-of-missouri-extension-wood-fuel-for-heati-b63761
  - us-doe-alternative-fuels-data-center-fuel-properties-84dd21
  - usda-hhs-dietary-guidelines-for-americans-2020-2025-4b2013
related: [03-01-daily-water-needs, 04-01-calorie-and-stockpile-math, 23-02-master-consumables-table, 06-03-firewood-basics, 09-03-batteries-and-storage, 09-05-solar-in-winter, 04-17-food-safety-power-outage, 03-04-purifying-water, 25-08-quick-reference-cards, 29-13-ex13-measuring-without-instruments, 29-02-ex02-batteries-and-power-stations]
cards: []
explainers: [EX-02, EX-13]
promote_when: []
photo_slots: []
figures: []
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: { date: "2026-11-16", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "Arithmetic verified; calorie rows aligned with 04-01; honey, canned goods, powdered milk, cord weight and seasoning corrected; kerosene AFDC mis-citation removed. Wave 2 (R18): unsourced propane 4.7 gal/430,000 BTU and 1-lb 21,500 BTU removed (no readable source for propane lb per gallon), runtime example now from AFDC BTU a gallon; toilet tank now last reserve, disinfect first (FEMA 477), unsourced 3 gal removed; boil line already EPA 5,000 / CDC 6,500 as 03-04." }
---

# Conversions, water and calorie math

**What this page is for.** The tables you will want at 2 a.m. with no phone. Everything here is
arithmetic or a planning estimate. **Where a number carries a safety consequence (how much
bleach to put in water, cooking temperatures, wind chill), this page points to the page that
owns it instead of repeating it.** That is deliberate: a mis-copied bleach amount is a real
hazard. Measuring without tools: → 29-13.

## Do this now

1. **Check this household's own numbers** in the worksheet at the bottom; the binder filled in
   what your settings allow. Write the rest in once, in pencil.
2. **Learn three numbers by heart:** water for this household,
   **{{ derived.water.plan_gal_day }} gallons a day** to plan with (→ 03-01); about
   **{{ derived.calories.day }} calories a day** for the household (→ 04-01); and **8.34 lb per
   gallon of water**.
3. **Do not use this page to dose bleach.** Go to → 03-04.

## Volume

| From | To | Multiply by |
|---|---|---|
| Gallons | Litres | 3.785 |
| Litres | Gallons | 0.264 |
| Gallons | Quarts | 4 |
| Quarts | Cups | 4 |
| Cups | Fluid ounces | 8 |
| Fluid ounces | Millilitres | 29.57 |
| Tablespoons | Teaspoons | 3 |
| Cups | Tablespoons | 16 |
| Cubic feet | Gallons | 7.48 |
| Gallons | Cubic feet | 0.134 |

## Weight

| From | To | Multiply by |
|---|---|---|
| Pounds | Kilograms | 0.454 |
| Kilograms | Pounds | 2.205 |
| Ounces | Grams | 28.35 |
| **Gallons of water** | **Pounds** | **8.34** |
| Cubic foot of water | Pounds | 62.4 |
| A 5-gallon bucket of water | Pounds | about 42, plus the bucket |
| A 55-gallon drum of water | Pounds | about 460: **it will not move once full** |

## Length, area, temperature

| Conversion | Formula |
|---|---|
| Inches to centimetres | × 2.54 |
| Feet to metres | × 0.305 |
| Miles to kilometres | × 1.609 |
| Acres to square feet | × 43,560 |
| **°F to °C** | **(°F − 32) × 5 ÷ 9** |
| **°C to °F** | **(°C × 9 ÷ 5) + 32** |

**Reference points:** 32 °F = 0 °C (freezing) · 40 °F = 4.4 °C (fridge) · 98.6 °F = 37 °C (body)
· 212 °F = 100 °C (boiling at sea level).

## Water math

| Question | Figure |
|---|---|
| **Minimum planning figure** | **1 gallon per person per day** for drinking and basic hygiene (CDC, How to Create and Store an Emergency Water Supply) |
| **This household, floor** | **{{ derived.water.floor_gal_day }} gal a day**: 1 gal per person, plus extra for nursing or pregnant members, infants and pets (→ 03-01) |
| **This household, plan** | **{{ derived.water.plan_gal_day }} gal a day**; two weeks = **{{ derived.water.two_weeks_gal }} gal** |
| **Stored now** | {{ gear.water.stored_gal }} gal = **{{ derived.water.stored_days }} days** at the floor rate |
| Realistic with cooking and washing | 2 to 3 gal per person per day |
| Absolute drinking minimum, short term | About 0.5 gal per person per day: **not sustainable, and worse when hot or working** |
| Toilet flush (conventional) | 1.6 to 3.5 gal, which is why the bucket toilet exists (→ 13-01) |
| Shower | 2 to 2.5 gal a minute |
| Sponge bath | About 1 gal |
| Hand-washing a load of laundry | 10 to 20 gal (→ 13-04) |
| Washing dishes carefully, two basins | 2 to 4 gal |

**Containers:** bathtub about 40 to 50 gal · this household's water heater
{{ dwelling.water_heater_gallons }} gal (a reserve: know the drain valve, → 03-02) · toilet
tanks (never the bowls), the last reserve: FEMA says not to drink tank water, so keep it for
flushing and washing, or disinfect it first if nothing else is left, and never if a cleaning
tablet or dye is in it (FEMA, Food and Water in an Emergency; → 03-04) · {{#if has.pool}}pool or hot tub {{ dwelling.pool_gallons }} gal, **none of
it drinkable without treatment** (→ 03-03){{else}}a 55-gal drum · a 5-gal bucket{{/if}}.

**Days of water = gallons on hand ÷ {{ derived.water.plan_gal_day }}** (the plan rate). Use the
floor rate, {{ derived.water.floor_gal_day }}, only when rationing. Do it on → 23-02.

## Calorie math

| Person or situation | Calories a day (planning) |
|---|---|
| Adult | About 1,600 to 3,000, by age, sex and activity (USDA/HHS, Dietary Guidelines for Americans, Appendix 2) |
| Adult, **hard physical work or cold** | The table's "active" column: for most adults **200 to 400 more** a day than the moderate one (→ 04-01) |
| Children and teenagers | By age and sex from the same table |
| **This household, normal** | **{{ derived.calories.day }}** (two weeks: {{ derived.calories.two_weeks }}) |
| **This household, working hard in the cold** | {{ derived.calories.day }} + 200 to 400 for each working adult = ______ |

**Two things people miss:** cold and hard work together can push the household's need far above
normal, and the eating of anyone with diabetes, a nursing parent or a small child is a
**medical** matter, not a rationing decision (→ 23-01).

**Rough calories per pound (dry):**

| Food | Calories per lb |
|---|---|
| **Oil and fat** | **About 4,000**: the densest thing you can store (→ 04-12) |
| Nuts and seeds | About 2,600 (an allergy constraint for some: → 02-04) |
| Powdered milk | About 1,650 (nonfat) to 2,250 (whole) |
| Sugar | About 1,750 |
| Honey | About 1,400 |
| Rolled oats | About 1,700 |
| **Rice, flour, pasta (dry)** | **About 1,600** |
| Dry beans | About 1,500 |
| Potatoes (fresh) | About 350 |
| **Canned goods**, mixed | About 400 to 600: you are carrying their water (→ 04-01) |

**Quick check:** 1 lb of mixed dry staples is about 1,500 to 1,800 calories, so an adult needs
roughly 1.5 lb a day. This household: {{ derived.calories.day }} ÷ about 1,600 = ______ lb a day,
× 30 = ______ lb a month, plus fat. A sanity check on → 04-01, not a substitute for counting.

## Fuel and heat

| Item | Figure |
|---|---|
| **A cord of wood** | 4 ft × 4 ft × 8 ft = **128 cubic feet stacked** |
| **A face cord (rick)** | 4 ft × 8 ft × the log length (often 16 in): about **1/3 of a cord** |
| Weight of a cord at 20 % moisture | About 2,700 lb (pine) to 3,700 lb (oak) (University of Missouri Extension, Wood Fuel for Heating) |
| Heat per cord | Dense hardwoods (oak, ash, hickory) give much more heat per cord than softwoods or cottonwood: **species matters** (University of Missouri Extension, Wood Fuel for Heating; → 06-03) |
| **Seasoning time** | **6 to 12 months, split and stacked; dense hardwoods a year or more** (→ 06-03) |
| Moisture target | **Under 20 %**: wet wood wastes heat boiling its own water and fouls the chimney |
| **Propane** | **91,420 BTU a gallon** (DOE AFDC). A refill receipt gives gallons; an exchange cylinder's label gives only the weight of propane, and the heater's manual often gives hours per cylinder |
| **Kerosene (1-K)** | **About 135,000 BTU a gallon** (typical figure; read your heater's label for its own rating) |
| Gasoline (pump gas with about 10 % ethanol) | **About 114,000 BTU a gallon** (DOE AFDC) ≈ 33 kWh of heat |
| **1 kWh of electricity** | **= 3,412 BTU.** A 1,500 W space heater gives about 5,100 BTU an hour and uses 1.5 kWh every hour |

A **BTU** (British thermal unit) is a unit of heat. Heaters are labelled in **BTU/h**: heat per
hour (→ 29-14).

**Heater runtime = fuel BTU ÷ the heater's BTU/h.** Example: 4 gallons of propane (from the
refill receipt) is 4 × 91,420 ≈ 366,000 BTU; in a heater burning 9,000 BTU/h it lasts about
366,000 ÷ 9,000 ≈ 40 hours, if nothing else uses that cylinder. Your heaters: {{#each heaters as h}}{{h.kind_text}} ({{h.model}}): ______ BTU/h → ______ hours per tank · {{else}}none entered{{/each}}.

**Cooking on an open fire uses far more wood** than an efficient stove for the same meal
(→ 07-02). **Measure yours during a blackout weekend** (→ 24-04).

## Electricity

| Term | Meaning |
|---|---|
| **Watts (W)** | Rate of use: volts × amps |
| **Watt-hours (Wh)** | Energy: watts × hours. **The unit that matters for batteries** |
| **Amp-hours (Ah)** | Battery capacity at a voltage. **Wh = Ah × volts** |
| 100 Ah at 12 V | 1,200 Wh on paper; **usable is less**, depending on chemistry (→ 09-07) |

**Typical loads (check your own labels; → 29-14):** LED bulb 5 to 10 W · headlamp 1 to 3 W ·
phone charge 10 to 20 Wh · laptop 30 to 60 W · CPAP 30 to 60 W · **fridge 100 to 200 W running,
about 1,000 to 2,000 Wh a day** · microwave 1,000 to 1,500 W · well pump 500 to 1,500 W, with a
higher start-up surge.

**This household:** power stations {{ gear.station_wh_total }} Wh · solar {{ gear.solar_w_total }} W ·
estimated solar harvest **{{ derived.solar_wh_jun }} Wh a day in June** and
**{{ derived.solar_wh_dec }} Wh a day in December** (your panels × your county's sun hours ×
0.75 for losses; an estimate). **Size for December, not June**, if the load is medical
(→ 09-05, → 09-10). A full-size fridge on the stations: about {{ derived.station_fridge_days }}
days (estimate).

## Temperature, weather and the body

- **Wind chill:** use the NWS chart (NWS, Wind Chill Chart; → 29-10). At extreme wind chill,
  exposed skin can freeze in minutes (→ 08-05).
- **Hypothermia** can happen well above freezing when wet and windy (→ 08-05).
- **Fridge 40 °F or colder; freezer 0 °F or colder.** After the power goes out: about **4
  hours** for refrigerated food, **48 hours** for a full freezer (24 if half full)
  (USDA/HHS, Food Safety During a Power Outage; → 04-17).
- **Safe cooking temperatures** for meat, poultry and leftovers, with rest times: **use the
  FoodSafety.gov chart** (Cook to a Safe Minimum Internal Temperature) and → 07-04. Do not
  estimate.
- **Boiling to make water safe:** a **rolling boil for 1 minute**; above about 5,000 ft,
  **3 minutes** (EPA says above 5,000 ft; CDC says above 6,500 ft; use the lower, safer figure)
  (EPA, Emergency Disinfection of Drinking Water; → 03-04). Your elevation: about {{ region.home.elevation_ft }} ft{{#if is.high_altitude}},
  **so boil for 3 minutes**{{/if}}.

## Time and distance (planning a move)

| How | Rate |
|---|---|
| Adult walking, unloaded, good ground | About 3 mph |
| **Adults walking loaded, with a small child** | **1 to 1.5 mph, with frequent stops** |
| Walking in snow or at night | **Half that or worse** |
| Bicycle, loaded | 8 to 12 mph |
| **A realistic day on foot with small children** | **5 to 8 miles** |

Take the last row seriously on → 01-03: it decides whether leaving on foot is a plan or a hope.

## This household's numbers

```
PEOPLE: {{ household.size }} ({{ household.adults }} adults, {{ household.children }} children)
WATER   floor/day: {{ derived.water.floor_gal_day }} gal   plan/day: {{ derived.water.plan_gal_day }} gal   realistic/day: ______ gal
CALORIES/day, normal: {{ derived.calories.day }}   cold + hard work: ______
DRY STAPLES/day: ______ lb        per month: ______ lb
WOOD per day (measured in a blackout weekend): ______
MEDICAL power use/day: ______ Wh
SOLAR, June: {{ derived.solar_wh_jun }} Wh/day (est.)   December: {{ derived.solar_wh_dec }} Wh/day (est.)
VEHICLE range on a full tank: ______ mi   + fuel cans: ______ mi
```

## Gear

**Buy toward:** a kitchen scale, a measuring jug, a fridge thermometer and a body thermometer, a
moisture meter for firewood, a watt-meter or battery monitor, a tape measure, and a calculator
with a solar cell. **And pencil and paper**: the actual instrument for all of this.

**If you do not have it:** a marked bucket measures water; a known weight checks a guess; **a cord
of wood is a fixed size**, so a tape measure is a scale; counting steps measures distance
(→ 29-13). **The most useful substitute of all is a written record of what you actually used
last time** (→ 24-04).

## When it goes stale

- These tables do not change; **the household's numbers change as children grow.** Redo the
  worksheet each year (→ 25-10).
- **Measure during every blackout weekend** and replace estimates with your real figures.
- **A measured number beats a table every time**, including the tables on this page.

## Phase notes

- **A (shelter in place):** measure everything now, while meters, scales and the internet work.
- **B (moving):** the travel table and the water figure matter most; carry them on a card
  (→ 25-08).
- **C (establish):** wood, calories and solar output are all different at a new place.
  **Re-measure in the first month.**

Related: → 03-01 water needs · → 04-01 calorie and stockpile math · → 23-02 runway table ·
→ 06-03 firewood · → 09-03 batteries · → 09-05 winter solar · → 04-17 food after an outage ·
→ 03-04 water treatment (**dosing lives there**) · → 25-08 the card version.

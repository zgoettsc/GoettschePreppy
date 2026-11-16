---
id: 23-02-master-consumables-table
section: 23-depletion-and-substitution
title: "Master consumables table"
version: 1
revised: 2026-11-16
layer: household
danger_level: critical
phase: [A, B, C]
tags: [depletion, runway, worksheet, consumables, water, food, fuel, medication, weekly check]
derived_from: [23-02-master-consumables-table]
sources:
  - us-fda-information-regarding-insulin-storage-and-swi-6448d3
  - cdc-how-to-create-and-store-an-emergency-water-suppl-f0c412
  - us-fda-epipen-epinephrine-injection-usp-auto-injecto-a9f17f
  - university-of-missouri-extension-wood-fuel-for-heati-b63761
related: [23-01-depletion-framework, 23-03-substitution-catalog, 23-04-resource-lifecycles, 23-05-skills-that-replace-supplies, 22-04-household-inventory, 22-07-priority-purchase-order, 12-07-meds-stockpile, 01-02-go-no-go-decision, 21-04-routine-and-structure, 25-05-blank-logs, 03-01-daily-water-needs, 04-01-calorie-and-stockpile-math, 06-04-wood-supply-and-depletion, 09-01-power-priorities, 30-18-dc17-old-fuel, 30-20-dc19-when-to-leave]
cards: [DC-17, DC-19, DC-13]
explainers: [EX-01, EX-02, EX-07, EX-13]
promote_when: [has.refrigerated_meds]
photo_slots: []
figures: []
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: null
---

# Master consumables table

**What this page is for.** Every section of this binder works out how long one kind of supply
lasts. This page puts all of them on one sheet so you can see **which clock is shortest**
(→ 23-01). Numbers from your settings are printed. Everything else you fill in with a pencil
and update at the weekly check (→ 21-04). **If you fill in only one thing, fill in the summary
line at the bottom.**

> **SAFETY.** The medicine rows are counts, not plans for stretching doses. **Never skip,
> split or space out a prescribed dose to make it last** without your prescriber's
> instructions; ask now what to do if supply is cut off and write the answer on → 12-07.
> **A frozen-then-thawed insulin vial or pen is discarded** (floor, → 30-01): freezing breaks
> it with no visible sign. Infant formula is never diluted to make it last (→ 20-05).

## Do this now

1. **Fill in the class C block first**: medicines and anything else nothing can replace. That
   is a today task.
2. **Measure the big four over a few real days**: water (→ 03-01), power (→ 09-01), wood or
   heating fuel (→ 06-04), food (→ 04-01). Measured, not guessed (→ 29-13).
3. **Write your own action point on each block.** The binder does not set them for you.
4. **Put the update on the weekly check** (→ 21-04) and the full review on the yearly calendar
   (→ 25-10). Blank copies: → 25-05.

**Household:** {{ household.size }} people ({{ household.adults }} adults, {{ household.children }}
children){{#if has.pets}}; pets: {{#each pets as p}}{{p.count}} {{p.type}}; {{/each}}{{/if}}.
Date of this update: ____________

## Class C: irreplaceable (the governing clocks)

No production, no substitute, no local resupply. **This block drives the leave-or-stay
decision** (→ 01-02).

| Item | Who | Days on hand (settings) | Recounted today | Date checked | Our action point | Ref |
|---|---|---|---|---|---|---|
{{#each meds as m}}| **{{m.name}}** {{m.strength}}{{#if has.refrigerated_meds}} (refrigerated: {{m.refrigerated}}){{/if}} | {{m.member}} | {{m.days_on_hand}} | ______ | ______ | ______ | → 12-07 |
{{else}}| Daily prescription medicine (none in settings) | ______ | ______ | ______ | ______ | ______ | → 12-07 |
{{/each}}| Device supplies (pump sets, sensors, test strips, ketone strips, CPAP parts, oxygen) | ______ | ______ | ______ | ______ | ______ | → 12-11 |
| Epinephrine auto-injectors (the clock is the **expiry date**, not use) | ______ | expires: ______ | ______ | ______ | ______ | → 02-03 |
| Other emergency medicines kept for a reaction (glucagon and similar): expiry, not use | ______ | expires: ______ | ______ | ______ | ______ | → 02-01 |
| Infant formula{{#if has.infant}} (a baby is in the household){{/if}} | ______ | ______ | ______ | ______ | ______ | → 20-05 |

How to fill a medicine row: count what is in the house (unopened plus open), divide by the
amount used per day **as prescribed**, and write the date. Insulin storage limits without a
fridge are on → 02-01 and → 29-07 (FDA, Information Regarding Insulin Storage and Switching
Between Products in an Emergency).

> **The shortest number in this block is the household's timeline.** When it reaches your
> action point, go to → 01-02. When to leave: {{choice DC-19}} → 30-20

## Water

| Item | On hand | Daily use | Days | Notes | Ref |
|---|---|---|---|---|---|
| Stored drinking water | {{ gear.water.stored_gal }} gal | floor {{ derived.water.floor_gal_day }} gal/day; plan {{ derived.water.plan_gal_day }} gal/day | about {{ derived.water.stored_days }} days at the floor | The floor is at least 1 gallon per person per day, more for nursing mothers, infants, pets, heat and illness (CDC, How to Create and Store an Emergency Water Supply). Two weeks at the planning figure: {{ derived.water.two_weeks_gal }} gal | → 03-01, → 03-02 |
| Filter life left, tablets, bleach | ______ | — | — | Spare filter cartridges? Bleach loses strength in storage (→ 29-05) | → 03-04, → 03-09 |
| Rain and snow catchment | ______ | — | — | Seasonal (→ 03-05, → 03-06) | → 03-05 |
{{#if has.pool}}| Pool or hot tub (not drinking water as it stands) | {{ dwelling.pool_gallons }} gal | — | — | Drinking it is a household choice: {{choice DC-13}} → 30-14 | → 03-03 |
{{/if}}{{#if has.water_heater_tank}}| Water-heater tank | {{ dwelling.water_heater_gallons }} gal | — | — | Drain from the bottom valve with the power or gas off (→ 03-02) | → 03-02 |
{{/if}}

**Our action point:** stored water below ______ days → harvest-and-treat mode (catchment out,
treatment running, → 03-05, → 03-04).

Use goes up with illness (→ 12-05), summer heat (→ 11-08), laundry (→ 13-04) and the garden
(→ 05-10).

## Food

| Item | On hand | Daily use | Days | Notes | Ref |
|---|---|---|---|---|---|
| Total stored calories | ______ kcal | {{ derived.calories.day }} kcal/day | ______ | Days = stored calories ÷ daily need. The daily figure is from the USDA Dietary Guidelines table for your members at a moderately active level; hard physical work in cold weather needs more. Two weeks: {{ derived.calories.two_weeks }} kcal. Your estimate in settings: {{ gear.food.pantry_days }} days | → 04-01 |
| Freeze-dried food | {{ gear.food.freeze_dried_servings }} servings | ______ | ______ | Add its calories to the line above. Needs hot water, little fuel (→ 04-19) | → 04-19 |
{{#if has.food_allergy}}| **Allergy-safe food, counted separately** | ______ | ______ | ______ | A narrower supply than the pantry; it runs out first (→ 02-04) | → 02-04 |
{{/if}}{{#if has.infant}}| Baby and toddler food | ______ | ______ | ______ | → 20-01 | → 20-05 |
{{/if}}| Fats and oils | ______ | ______ | ______ | Also soap and lamp fuel (→ 13-09, → 10-04) | → 04-12 |
| Salt | ______ | ______ | ______ | Preserving and trade | → 04-13 |
| Cooking fuel (propane, white gas, butane) | ______ | ______ | ______ | Count only the share set aside for cooking if the same fuel also heats or runs the generator | → 07-05, → 06-05 |
{{#each pets as p}}| Pet food: {{p.count}} {{p.type}} | ______ | {{p.food_per_day}} | ______ | | → 20-09 |
{{/each}}

**Our action point:** stored food below ______ days → → 04-18 (meal planning in scarcity).

## Heat and fuel

| Item | On hand | Daily use | Days | Notes | Ref |
|---|---|---|---|---|---|
| Firewood | {{ gear.fuel.firewood_cords }} cords | ______ | ______ | Work it out for a cold week, not an average one (MU Extension, Wood Fuel for Heating) | → 06-04 |
| Propane, 20-lb cylinders | {{ gear.fuel.propane_20lb }} | ______ | ______ | Propane does not go stale. If the same cylinders heat, cook and run the generator, split them on paper (→ 06-05) and track each share | → 06-05, → 06-06 |
| Propane, 1-lb cylinders | {{ gear.fuel.propane_1lb }} | ______ | ______ | | → 07-05 |
| Kerosene (K-1) | {{ gear.fuel.kerosene_gal }} gal | heater's gal per hour × hours run | ______ | The burn rate is on the heater's label or manual. Jar-test before filling (→ 30-18) | → 08-10, → 06-06 |
| Diesel | {{ gear.fuel.diesel_gal }} gal | ______ | ______ | | → 06-06 |
| Gasoline | {{ gear.fuel.gasoline_gal }} gal | ______ | ______ | Shared between generator and vehicles: every gallon burned at home is range lost on the road (→ 01-03). Untreated gasoline keeps for months, not years (→ 23-04) | → 09-04, → 06-06 |
| Generator fuel{{#if has.generator}} ({{ gear.generator_fuel }}){{/if}} | see above | measure gal per hour on first run | ______ | | → 09-04 |
| Lamp oil and candles | ______ | ______ | ______ | Count in hours of light | → 10-02 |

Old fuel: {{choice DC-17}} → 30-18

**Our action points:** heater fuel below ______ → heat only in waking hours, layers carry the
rest; below ______ → step down the heat chain (→ 23-03) and do the heat check on → 01-02.
Heater fuel below ______ before winter → buy now.

## Power

| Item | Capacity | Daily use | Days | Notes | Ref |
|---|---|---|---|---|---|
| Power stations | {{ gear.station_wh_total }} Wh | ______ Wh | ______ | A full-size fridge alone: about {{ derived.station_fridge_days }} days with no sun (an estimate; the battery's own percentage screen is the truth) | → 09-03 |
| Medicine fridge or cooler on battery | ______ Wh/day (measure) | — | ______ | Days = station Wh ÷ measured Wh per day, less if anything else is plugged in | → 09-10 |
| Power banks | ______ Wh each × ______ | — | ______ | | → 09-06 |
| AA and AAA cells (rechargeable / alkaline) | ______ / ______ | ______ per night | ______ | | → 09-07, → 10-06 |
| Solar | {{ gear.solar_w_total }} W | — | — | Rough clear-day harvest: about {{ derived.solar_wh_dec }} Wh in December, {{ derived.solar_wh_jun }} Wh in June (estimates). Overcast days give far less; snow-covered panels give none. **Size on December** | → 09-05 |

**Our action point:** cells below ______ → count, charge and restage the rotation (→ 10-06).

## Medical and sanitation

| Item | On hand | Use rate | Days | Notes | Ref |
|---|---|---|---|---|---|
| **Oral rehydration salts** | ______ | ______ | ______ | Count in litres and sick-days | → 12-05 |
| Gauze and dressings | ______ | ______ | ______ | Count in dressing changes | → 12-02 |
| Over-the-counter medicines | ______ | ______ | ______ | Check expiry dates | → 12-07, → 12-13 |
| **Soap** | ______ | ______ | ______ | The most valuable medical supply | → 13-02, → 13-09 |
| Bleach | ______ | ______ | ______ | Loses strength in storage (→ 29-05) | → 13-11 |
| Toilet paper and cover material | ______ | ______ | ______ | Measure a real week | → 13-01 |
| Waste bags | ______ | ______ | ______ | | → 13-01, → 13-03 |
| Diapers{{#if has.infant}} (a baby is in the household){{/if}} | ______ | count a real day | ______ | The child also outgrows the size | → 13-08 |
{{#if has.cats}}| Cat litter | ______ | ______ | ______ | Never compost it; bag it like human waste. Dirt, sand or ash substitute | → 13-03 |
{{/if}}| Menstrual supplies | ______ | ______ | ______ | Reusables end this line | → 13-08 |

**Our action point:** diapers below ______ days → start the cloth transition (→ 13-08); do
not wait for the last pack.

## Tools and materials

| Item | On hand | Notes | Ref |
|---|---|---|---|
| **Saw blades, chainsaw chains** | ______ | The firewood bottleneck | → 16-06, → 16-02 |
| Files and sharpening stones | ______ | Hard to improvise | → 16-02 |
| Hacksaw blades, drill bits | ______ | Hard to improvise | → 16-08 |
| **Thread and needles** | ______ | Cannot be made at home; stock far more than seems sensible | → 16-04 |
| Screws, nails, wire, tape | ______ | Plentiful to salvage | → 16-07, → 16-05 |
| Glues | ______ | Expire; rotate | → 16-05 |
| Radio cable and connectors | ______ | Fail without visible signs | → 15-06 |
| Bicycle tubes and tires | ______ | | → 16-09 |
| Heater wicks and fuel filters | ______ | A worn wick burns smoky and makes more carbon monoxide; replace, never turn down | → 08-10, → 08-09 |
| Igniter batteries for heaters and stoves | ______ | | → 28-04 |
| **CO and smoke alarm batteries** | ______ | For {{ gear.co_alarms }} CO and {{ gear.smoke_alarms }} smoke alarms. Replace at the chirp and by the date on the unit; test before any fuel-burning heater is lit (→ 08-02) | → 08-02 |
| Fire extinguishers | {{ gear.extinguishers }} | Check the gauge (→ 29-12) | → 29-12 |
| Seeds | ______ | Germination falls each year | → 05-03 |
| Potting mix, fertiliser | ______ | Slow to scavenge | → 05-10, → 05-11 |

## The summary line: fill this in every week

| | Value | Date |
|---|---|---|
| **Shortest class C clock (days)** | ______ | ______ |
| **What it is** | ______ | ______ |
| **Our action point** (→ 01-02) | ______ | ______ |
| **Shortest non-medical clock (days)** | ______ | ______ |
| **Did anything cross an action point this week?** | ______ | ______ |

## How to use it

- **Pencil.** It changes all the time.
- **Update at the weekly check** (→ 21-04): about fifteen minutes with every adult.
- **Measure the big ones over real days** (→ 23-01) and work them out for the hard case: a
  cold week, a hot week, a sick week.
- **Every block has an action point line.** Write your own and change it whenever you have a
  better number.

What the table is for:
1. Seeing which clock is shortest. In most households with a daily prescription, it is a
   medicine.
2. Making the leave-or-stay decision on numbers rather than feelings (→ 01-02).
3. Knowing what to buy next (→ 22-07): whatever has the shortest runway for how much it
   matters.
4. Knowing what to ration, and when (→ 23-01).
5. Catching a problem while it can still be fixed.

**What most households find when they fill it in honestly:** the medical clock is far shorter
than everything else and cannot be stretched by effort, only by supply (→ 12-07) and by acting
early (→ 01-02). And the renewable lines (water, wood, food) look worse on paper than they
are, because a runway leaves out what you can produce (→ 23-04).

## When it runs out

- **This table is the tool for that question.** When the summary line crosses an action
  point, go to → 01-02 and carry out the decision you already wrote down.
- **Failure one:** filling it in once, feeling prepared, and never updating it. The weekly
  check is the fix.
- **Failure two:** filling it in with hopeful numbers. Measure.
- **The reassurance:** most lines are class A or B (→ 23-01), renewable or substitutable. The
  table looks alarming, and most of it is not. The class C block is the real content, and it
  is short enough to check in two minutes.

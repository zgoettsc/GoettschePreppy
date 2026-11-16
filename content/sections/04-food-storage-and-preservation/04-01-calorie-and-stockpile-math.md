---
id: 04-01-calorie-and-stockpile-math
section: 04-food-storage-and-preservation
title: "Calorie planning and stockpile math"
version: 1
revised: 2026-11-16
layer: core
danger_level: caution
phase: [A, B, C]
tags: [food, calories, planning, math, stockpile, allergens, runway]
derived_from: [04-01-calorie-and-stockpile-math]
sources:
  - usda-hhs-dietary-guidelines-for-americans-2020-2025-4b2013
  - usda-agricultural-research-service-fooddata-central-9412f9
  - usda-fooddata-central-sr-legacy-staples-r12
  - foodsafety-gov-usda-hhs-cook-to-a-safe-minimum-inter-13daf3
  - us-fda-food-allergies-627fb6
related: [04-02-building-a-pantry, 04-03-bulk-staples-storage, 04-12-fats-and-oils, 04-13-salt-sugar-vinegar, 04-16-sprouting, 04-19-freeze-dried-stockpile, 03-01-daily-water-needs, 07-07-freeze-dried-rehydration, 02-04-cl04-food-allergy, 02-01-cl01-type-1-diabetes-injections, 02-05-cl05-type-2-diabetes, 02-13-cl13-infant-feeding, 20-05-infant-feeding, 23-02-master-consumables-table, 22-04-household-inventory, 30-19-dc18-unlabeled-food-and-allergies, 30-27-dc26-allergy-safe-food-reserve]
cards: [DC-18, DC-26]
explainers: [EX-13]
promote_when: []
photo_slots: []
figures: []
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: null
---

# Calorie planning and stockpile math

**What this page is for.** How much food your household needs each day, how to turn that into
pounds of food on a shelf, and how to work out how many days the food you already have will
last (your **runway**). Every other food page uses the numbers printed here.

> **CAUTION.** Calories are only half of a food plan. If anyone in the house has a food
> allergy, diabetes, celiac disease or another condition that limits what they can eat, their
> safe food is a second, separate number, and it is usually the one that runs out first. Plan
> both numbers together, or you will find the problem when it is too late to fix (→ 02-04).

## Do this now

1. **Know your daily number.** Your household needs about **{{ derived.calories.day }}
   calories a day** at an ordinary, moderately active level. Two weeks is about
   **{{ derived.calories.two_weeks }} calories**.
2. **Plan more in winter and for hard work.** Cold, hauling wood and water, and washing by
   hand all burn more. For most adults the "active" column of the same government table is
   200 to 400 calories a day higher than the moderate one (USDA/HHS, Dietary Guidelines
   2020-2025, Appendix 2).
3. **Count, do not estimate.** Your current estimate is **{{ gear.food.pantry_days }} days**
   of pantry food and **{{ gear.food.freeze_dried_servings }} freeze-dried servings**. Most
   households are wrong about this number. Count the shelf once, with the method below.
4. **Track any restricted diet separately.** If one person can eat only some of the food,
   work out their runway from their safe food only.
5. **Build in stages:** two weeks, then one month, then three months. Depth of food you
   already eat beats variety.
6. **Write the runway down** where everyone can see it (→ 23-02, → 22-04).

## How your number is worked out

The binder adds up one line per person from the published USDA/HHS table of estimated
calorie needs, using the **moderately active** column (USDA/HHS, Dietary Guidelines for
Americans 2020-2025, Appendix 2).

{{#each members as m}}
- **{{m.label}}**: {{m.age_text}}, {{m.sex}}. Daily need from the table below: ________ calories.
{{else}}
- No household members are entered yet. Add them in settings and this list fills in.
{{/each}}

**Household total: {{ derived.calories.day }} calories a day.** If the total shows a blank,
someone's age is missing in settings.

| Age | Male, moderately active | Female, moderately active |
|---|---|---|
| 12 to 23 months | about 1,000 (kit uses the top of the published 700 to 1,000) | about 1,000 |
| 2 | 1,000 | 1,000 |
| 3 | 1,400 | 1,200 |
| 4 to 5 | 1,400 | 1,400 |
| 6 | 1,600 | 1,400 |
| 7 to 8 | 1,600 | 1,600 |
| 9 | 1,800 | 1,600 |
| 10 | 1,800 | 1,800 |
| 11 | 2,000 | 1,800 |
| 12 to 13 | 2,200 | 2,000 |
| 14 | 2,400 | 2,000 |
| 15 | 2,600 | 2,000 |
| 16 to 18 | 2,800 | 2,000 |
| 19 to 25 | 2,800 | 2,200 |
| 26 to 45 | 2,600 | 2,000 |
| 46 to 50 | 2,400 | 2,000 |
| 51 to 65 | 2,400 | 1,800 |
| 66 and over | 2,200 | 1,800 |

Source: USDA/HHS, Dietary Guidelines for Americans 2020-2025, Appendix 2, printed as
published. Where sex is not entered the binder uses the higher figure, so the store is not
planned short.

- **Pregnant:** the binder adds **340 calories a day** (the published second-trimester
  figure; the Guidelines give nothing extra in the first trimester and 452 in the third).
  **Nursing:** it adds **330** (the published figure for the first 6 months of nursing; the
  Guidelines give 400 for months 7 to 12). All come from the same Guidelines and are printed as
  published. Plan the larger figure by hand for a pregnancy in its last three months or a baby
  over 6 months.
- **Babies under 12 months are not in the food total.** The Guidelines give no calorie figure
  for them: they live on breast milk or infant formula. Their plan is on → 02-13 and → 20-05.
  **Powdered or canned milk is not infant formula** (→ 04-14).
- **Toddlers 12 to 23 months need whole-fat food.** The dairy rule for them is on → 04-14 and
  the feeding plan on → 20-05.

## Turning calories into pounds

Rules of thumb that make this workable (worked from USDA FoodData Central values per 100 g;
your own labels govern):

- **1 lb of dry staples (rice, beans, flour, oats) is about 1,500 to 1,750 calories.** Dry
  white rice is about 1,650, dry white beans about 1,520, all-purpose flour about 1,650, oats
  about 1,760.
- **Pounds of dry staples per day, if you ate staples alone:** {{ derived.calories.day }} ÷
  1,600. Multiply by 30 for a month and by 90 for three months.
- **Fats and oils are about 4,000 calories per pound** (cooking oil is about 4,010), more than
  double any grain. They are the easiest way to close a calorie gap in a small space (→ 04-12).

### The runway is a sum

Count every layer: staples, canned goods, fats, and freeze-dried food. The number that goes on
the consumables table (→ 23-02) is:

> **(calories of staples on hand + calories of canned and other food on hand + calories of
> freeze-dried food on hand, from → 04-19) ÷ {{ derived.calories.day }} = days of runway**

No single layer is the number. If one person eats a restricted diet, work out their runway
the same way **from their safe food only**, using their own line from the table above.

How to count calories on hand: read the label (calories per serving × servings per package;
→ 29-14). For bulk buckets, weigh them and use the per-pound figures above. A kitchen scale
helps; → 29-13 has ways to estimate without one.

### The water cost: when water is short, eat the food that brings its own

Freeze-dried food is the best food when water is plentiful and the worst when it is not,
because you must add your stored water to eat it (→ 07-07, → 03-01). When the water runway is
the shorter one, turn the menu around:

| Food | Water it costs you to eat | Eat it when water is |
|---|---|---|
| **Canned goods** | **Lowest**: packed in their own liquid; drink it | **Short: eat these first** |
| Dry staples (rice, beans, oats) | Middle: real cooking water, some absorbed | Adequate |
| **Freeze-dried meals** | **Highest**: about 2 cups per pouch (the label governs) | **Plentiful: eat these last** |

## Medical diets change the plan

- **Food allergy.** One allergic person can remove a large share of the usual preparedness
  pantry. Build the family's staples from **single-ingredient foods** everyone can eat, keep any
  separate supply physically apart and labelled, and track the allergic person's safe-food
  runway as its own number: everyone else can eat almost anything; they cannot. Whether the
  rest of the household also eats that safe food, or keeps it as the allergic person's reserve,
  is a decision card: sharing shortens their runway, reserving means everyone else eats other
  food first. {{choice DC-26}} → 30-27. → 02-04. {{#if has.anaphylaxis}}**Someone in your household has an allergy marked
  severe enough for anaphylaxis.** Their safe-food runway is the number that binds.{{/if}}
- **Diabetes.** Carbohydrate is dosing information, not just calories. Write the carbohydrate
  content on each container of staples; repeat known meals with known carbohydrate; keep fast
  sugar for treating lows separate and protected (→ 02-01, → 02-05, → 04-18).
- **Celiac disease and other gut conditions:** → 02-19.
- **Unlabelled, traded or scavenged food for someone with a food allergy** is a decision card:
  {{choice DC-18}} → 30-19.

## What to store, by role

| Role | Foods | Why |
|---|---|---|
| **Calorie base** | Rice, wheat, oats, corn, beans, potatoes | Cheap, dense, long-storing (→ 04-03) |
| **Fat** | Oil, lard, tallow, shortening | Calorie density; cooking (→ 04-12) |
| **Protein** | Dried beans, canned meat and fish, jerky | Beans and grain eaten together give complete protein |
| **Vitamins** | Canned and dried vegetables and fruit, sprouts (→ 04-16) | Scurvy (vitamin C lack) is a real risk over months |
| **Morale** | Sugar, coffee, tea, spices, cocoa | Not optional over months (→ 21-02) |
| **Medical** | Fast sugar for diabetics, oral rehydration salts | → 02-01, → 12-05 |

**Do not overlook vitamins.** A family living on rice and beans for six months develops real
deficiencies. Sprouting (→ 04-16), preserved vegetables and a garden (→ 05-01) are the
practical answers. A multivitamin is cheap insurance; check its label for allergens.

## Building it in stages

1. **Two weeks** of normal food you already eat.
2. **One month,** adding bulk staples and fats (→ 04-02, → 04-03).
3. **Three months,** adding the ability to preserve food (→ 04-04 to → 04-08).
4. **Beyond that** needs **production**: garden, animals, hunting, trade (Section 05, → 18-02).

**Storage alone does not carry a household through a long grid-down.** Every stored pound is
eaten once. Storage buys time to start producing.

## Leaving home: calories per pound decide what rides

When you leave home (Phase B) the limit is weight and space in the vehicle, not shelf space
(→ 01-03). Load by calories per pound, with one exception that comes first.

| Food | About calories per lb | Note |
|---|---|---|
| Rendered fat, lard, shortening | **4,000** | Densest food in the house (→ 04-12) |
| Cooking oil | **4,000** | Jugs pack tight |
| Sugar | 1,750 | Dense and keeps for ever (→ 04-13) |
| Jerky | **1,800** | Ready-to-eat protein (USDA FoodData Central: about 410 calories per 100 g) |
| Freeze-dried pouches | Read the label: calories per serving × servings, ÷ the pouch weight in lb | Ready to eat; needs your water (→ 04-19) |
| Dry staples | 1,500 to 1,750 | Needs cooking fuel and water |
| Canned goods | **About 100 to 700** (vegetables low, meat and fish high) | You are hauling its water: cheap water, expensive weight |

(Figures worked from USDA FoodData Central per 100 g: oil 884, sugar 387; canned salmon 153,
canned capers 23. Labels govern.)

**One 50-lb bin, worked out** (use your own labels' figures; these are examples):

- of **dry staples** at about 1,600 per lb = about **80,000 calories**
- of **canned goods** at an assumed 500 per lb = about **25,000 calories**
- of **freeze-dried** pouches: work out calories per lb from the label, × 50

Divide each by {{ derived.calories.day }} to get household-days per bin. Same bin, same weight,
about three times the difference between staples and cans. Load dense.

**Grab order (write it on the bin lids):**

1. **Any allergy-safe or medical-diet bin, first, always.** It is the one kind of food that
   scavenging and charity cannot replace (→ 02-04). Density does not apply to it.
2. **Fats and oils:** the most calories per pound.
3. **Freeze-dried pouches:** dense and no cooking, but check the water plan (→ 03-01).
4. **Sugar, jerky, dry staples:** dense, but staples need fuel and water to become food.
5. **Canned goods last,** and only if weight remains; or on purpose, as food-plus-water for
   the first day on the road.

## Gear and supplies

| Item | Why | Notes |
|---|---|---|
| Bulk staples: rice, beans, oats, flour, sugar, salt | The calorie base | Storage method → 04-03 |
| Cooking oil, shortening, lard | Calorie density | Check labels for allergens (→ 04-12) |
| Plain canned vegetables, fruit, meat | Vitamins and protein | Single-ingredient, readable labels |
| Separate stock for any restricted diet | Usually the binding number | Track its own runway; who eats it is DC-26 (→ 30-27) |
| Kitchen scale and measuring cups | Real numbers; carbohydrate counting | Also for canning and curing |
| Written inventory and calorie sheet | Planning needs numbers | → 22-04, → 23-02 |
| Multivitamins | Cheap insurance against deficiency | Check allergens on the label |

**If you don't have it:**

- **Single-ingredient staples in sealed original packaging** are the safest food to scavenge
  or trade for, and the easiest to check for allergens.
- Garden produce (→ 05-01) is fully traceable.
- Fats are the hardest food to find later and the most valuable per pound. Get them early.

## When it runs out

- **Runway:** total calories on hand (every layer, summed) ÷ {{ derived.calories.day }}. Write
  it on → 23-02. Then work out each restricted diet's separate runway from that person's safe
  food only; it is usually shorter.
- **Ration:** many households cut adult portions before children's. Keep a diabetic's
  carbohydrate steady rather than cut. Never ration an allergic person into eating unchecked
  food.
- **Resupply:** production (Section 05), preserving gluts (→ 04-04 to → 04-08), trade (→ 18-02).
- **The honest limit:** storage buys months. Only production buys years.

## Phase notes

- **A (sheltering at home):** build the stockpile now; it is the cheapest phase to do it in.
- **B (moving):** you carry days, not months: dense, ready to eat, and safe for everyone who
  travels (→ 01-03). Use the grab order above.
- **C (rural or at a destination):** storage plus growing; the planting calendar becomes the
  plan (→ 25-01).

## Cross-references

→ 04-02 building a pantry · → 04-03 bulk staples · → 04-12 fats · → 04-19 freeze-dried food ·
→ 03-01 water · → 02-04 food allergy · → 02-01 diabetes · → 02-13 infant feeding ·
→ 23-02 consumables table

---
id: 26-04-checklist-water-food
section: 26-pre-disaster-acquisition-checklist
title: "Checklist 2: water and food"
version: 1
revised: 2026-11-16
layer: core
danger_level: caution
phase: [A]
tags: [checklist, water storage, water treatment, food storage, canning, garden, allergen-safe food]
derived_from: [26-04-checklist-water-food]
sources:
  - cdc-how-to-create-and-store-an-emergency-water-suppl-f0c412
  - us-epa-emergency-disinfection-of-drinking-water-6aa91f
  - foodsafety-gov-usda-hhs-food-safety-during-a-power-o-3894c1
  - national-center-for-home-food-preservation-nchfp-gen-c43991
related: [03-01-daily-water-needs, 03-02-storing-water, 03-03-pool-water-desalination, 03-04-purifying-water, 03-05-rain-and-snow-water, 04-01-calorie-and-stockpile-math, 04-03-bulk-staples-storage, 04-05-canning-pressure, 02-04-cl04-food-allergy, 05-03-seed-saving, 26-08-expiry-and-rotation-tracker, 26-09-shopping-list-and-budget]
cards: [DC-13]
explainers: [EX-05, EX-06, EX-08]
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

# Checklist 2: water and food

**What this page is for.** The second sheet of the walk (→ 26-01). Water first, because it is
the shortage that arrives first in almost every emergency and the one most households are
least ready for (CDC, How to Create and Store an Emergency Water Supply). Then food, food
storage and growing.

> **CAUTION.** **This household's water floor is {{ derived.water.floor_gal_day }} gallons a
> day; plan on {{ derived.water.plan_gal_day }} gallons a day, so two weeks is
> {{ derived.water.two_weeks_gal }} gallons** (→ 03-01). Cooking and washing come on top, from
> water you treat. **No bleach amounts or canning times on this page**: read → 03-04 and → 04-05.
> **Bleach or pool shock is never mixed with ammonia, acids or other cleaners.**

**Marks:** ✔ have it, it works, I know where it is · ~ partly, or needs a spare · ✗ do not have

## A. Water storage

| ✔ ~ ✗ | Item | Gallons / count | Notes | Page |
|---|---|---|---|---|
| [ ] | Stored drinking water (settings: {{ gear.water.stored_gal }} gal) | ______ | Filled on: ______ | → 03-02 |
| [ ] | Food-grade containers (jugs, drums) | ______ | | → 03-02 |
| [ ] | Food-grade 5-gal buckets + lids | ______ | | → 03-02 |
| [ ] | Separate **non-drinking** buckets, labelled | ______ | | → 13-03 |
| [ ] | Water heater{{#if has.water_heater_tank}} ({{ dwelling.water_heater_gallons }} gal){{/if}}: drain valve found + a hose that fits | | Power or gas off first; let it cool; close the cold inlet | → 03-02 |
| [ ] | Bathtub liner (a water bladder for the tub) | ______ | | → 03-02 |
| [ ] | Rain barrels + diverter + **screen** | ______ | {{#if is.cold_winters}}Drained before the hard freeze{{else}}Mosquito screen on{{/if}} | → 03-05 |
| [ ] | Rainwater treatment supplies located (rain is not drinking water until treated) | | | → 03-04 |
| [ ] | Siphon pump, hose, funnel, **marked for water only** | | | → 03-02 |
| [ ] | {{#if has.pool}}**Pool or hot tub ({{ dwelling.pool_gallons }} gal): raw water**, plan for treating it{{else}}Nearby raw water (pond, creek, a neighbour's pool) and a plan for treating it{{/if}} | | Drinking it is a household choice: {{choice DC-13}} → 30-14 | → 03-03 |
{{#if has.well}}| [ ] | **Well: a way to get water with no power** (bailer + rope, hand pump, or generator wiring) **(this household)** | | | → 03-10 |
{{/if}}

## B. Water treatment

| ✔ ~ ✗ | Item | Count | Expiry or life | Page |
|---|---|---|---|---|
| [ ] | Gravity or pump filter | ______ | | → 03-04 |
| [ ] | **Spare filter elements** (at least two) | ______ | Element life: ______ | → 03-09 |
| [ ] | Unscented household bleach | ______ | **Bought on:** ______ | → 03-04 |
| [ ] | Pool shock (calcium hypochlorite), stored sealed, dry, away from fuel and other chemicals | ______ | | → 29-05 |
| [ ] | Purification tablets | ______ | ______ | → 03-04 |
| [ ] | Dropper or measuring syringe, marked for bleach only | ______ | | → 03-04 |
| [ ] | Large pot with a lid for boiling | ______ | | → 07-01 |
| [ ] | Distillation setup (removes salt) | ______ | | → 03-03 |
| [ ] | Cloth or coffee filters for pre-filtering cloudy water | ______ | | → 03-04 |
| [ ] | Mosquito larvicide (Bti) for standing water | ______ | ______ | → 03-08 |

> **A filter with no spare element is a "~", not a "✔".** The element is the consumable, and it
> sets how long the filter works.

## C. Food staples

**This household needs about {{ derived.calories.day }} calories a day** (→ 04-01). Pantry by
your estimate: {{ gear.food.pantry_days }} days. Freeze-dried: {{ gear.food.freeze_dried_servings }}
servings.

| ✔ ~ ✗ | Item | Amount (lb or cans) | Earliest expiry | Page |
|---|---|---|---|---|
| [ ] | Rice and grains | ______ | ______ | → 04-03 |
| [ ] | Beans and lentils | ______ | ______ | → 04-03 |
| [ ] | Flour, oats, pasta | ______ | ______ | → 04-03 |
| [ ] | Canned meat and fish | ______ | ______ | → 04-02 |
| [ ] | Canned vegetables and fruit | ______ | ______ | → 04-02 |
| [ ] | **Fats and oils** | ______ | ______ | → 04-12 |
| [ ] | Sugar and honey | ______ | ______ | → 04-13 |
| [ ] | **Salt** (canning or pickling, not only iodised table salt) | ______ | | → 04-13 |
| [ ] | Powdered or canned milk | ______ | ______ | → 04-14 |
{{#if has.child}}| [ ] | Shelf-stable milk and foods the children reliably eat | ______ | ______ | → 20-05 |
{{/if}}{{#if has.infant}}| [ ] | **Infant formula** (if used), unopened, in date, and safe water to mix it | ______ | ______ | → 02-13 |
{{/if}}| [ ] | Spices, vinegar, baking supplies | ______ | ______ | → 04-13 |
| [ ] | Coffee, tea, comfort food | ______ | ______ | → 21-02 |
| [ ] | Manual can opener (two) | ______ | | → 04-02 |

```
TOTAL ESTIMATED CALORIES: __________ ÷ {{ derived.calories.day }} a day = ________ DAYS
```

> **Fats are the hardest food to store and the easiest to run short of** (→ 04-12). Households
> almost always have more grain and less fat than they think.

## D. Special-diet food{{#if has.anaphylaxis}} (this household: food allergy){{/if}}

| ✔ ~ ✗ | Item | Amount | Expiry | Page |
|---|---|---|---|---|
| [ ] | A **dedicated bin**, kept apart from shared food | ______ | | → 02-04 |
| [ ] | Safe staples the person reliably eats | ______ | ______ | → 02-04 |
| [ ] | Safe shelf-stable snacks for bags and vehicles | ______ | ______ | → 22-03 |
| [ ] | Dedicated utensils, cutting board, pans | ______ | | → 02-04 |
| [ ] | A written list of safe brands (makers change recipes; re-read labels) | ______ | | → 29-14 |
| [ ] | Freeze-dried or bulk food **checked against the allergen list before buying** | ______ | ______ | → 04-19 |

{{#if has.anaphylaxis}}Allergens in this household: {{#each allergies as a}}{{a.member}}: {{a.allergen}} ({{a.severity}}) · {{/each}}
{{/if}}A shared scoop in a shared bin is a "~" at best. Celiac disease and other medical diets follow
the same rules (→ 02-19).

## E. Food storage and preserving gear

| ✔ ~ ✗ | Item | Count | Notes | Page |
|---|---|---|---|---|
| [ ] | Mylar bags + **oxygen absorbers** | ______ | | → 04-03 |
| [ ] | Food-grade buckets + gamma (screw-top) lids | ______ | | → 04-03 |
| [ ] | Rodent-proof bins | ______ | | → 04-11 |
| [ ] | Pressure canner{{#if has.pressure_canner}} (owned){{/if}} + **spare gasket** | ______ | Dial gauge tested this year? | → 04-05 |
| [ ] | Boiling-water canner | ______ | | → 04-04 |
| [ ] | Jars | ______ | | → 04-04 |
| [ ] | **Lids** (single use: count them) | ______ | | → 04-04 |
| [ ] | Dehydrator and/or drying screens | ______ | | → 04-06 |
| [ ] | Fermenting crocks or jars with airlocks | ______ | | → 04-08 |
| [ ] | Vacuum sealer + bags | ______ | | → 04-03 |
| [ ] | Labels + permanent marker | ______ | | → 04-10 |
| [ ] | **A current tested-recipe book** (USDA, NCHFP or Extension) | ______ | | → 04-05 |

> **Canning lids are single use.** A canner with no lids is a "✗" dressed as a "✔" (NCHFP,
> General Canning Information). **Low-acid foods are pressure-canned to the published time and
> pressure, or not canned.**

## F. Growing food

| ✔ ~ ✗ | Item | Count | Notes | Page |
|---|---|---|---|---|
| [ ] | **Open-pollinated seed** (not hybrid) | ______ | Packet year: ______ | → 05-03 |
| [ ] | Seed-starting trays, mix, grow light | ______ | | → 05-14 |
| [ ] | Garden hand tools | ______ | | → 05-01 |
| [ ] | Row cover, hoops, cold frame | ______ | | → 05-02 |
| [ ] | Containers + potting mix{{#if has.apartment}} (balcony or windowsill){{/if}} | ______ | | → 05-10 |
| [ ] | Compost bin or pile started | ______ | | → 05-11 |
| [ ] | Watering cans, soaker hose | ______ | | → 05-01 |
| [ ] | Fruit trees or bushes **planted** | ______ | Planted on: ______ | → 05-13 |
| [ ] | Sprouting jars + sprouting seed | ______ | ______ | → 04-16 |
| [ ] | Fishing tackle | ______ | | → 05-08 |
| [ ] | Traps and snare wire | ______ | | → 05-15 |
| [ ] | Game-processing knives, saw, gambrel | ______ | | → 05-09 |
| [ ] | Two regional field guides **with photographs** | ______ | | → 05-06 |

> **Seed and soil are the two things money cannot buy in a hurry.** Seed needs a season; soil
> takes years. Both are cheap now and unobtainable later (→ 23-04). Your frost dates: → 25-01.

## The lines that matter

```
DAYS OF WATER STORED:     ________  (gallons ÷ {{ derived.water.plan_gal_day }} a day, the plan rate;
                                      ÷ {{ derived.water.floor_gal_day }} is the rationing floor)
   TARGET: two weeks = {{ derived.water.two_weeks_gal }} gal.
   Under a week of water is a TODAY problem, not a someday problem.
DAYS OF FOOD:             ________  (calories ÷ {{ derived.calories.day }})
SPARE FILTER ELEMENTS:    ________  (zero = the filter has a deadline)
BLEACH PURCHASE DATE:     ________  (it weakens on the shelf)
CANNING LIDS ON HAND:     ________

BIGGEST GAP: ______________________________________________
```

Food from a fridge or freezer after a power cut: about 4 hours for the fridge, 48 for a full
freezer (USDA/HHS, Food Safety During a Power Outage; → 04-17).

Related: → 03-02 storage · → 03-04 treatment (**amounts live there**) · → 03-03 pool and salt
water · → 04-01 pantry math · → 04-03 bulk staples · → 04-05 pressure canning · → 02-04 food
allergy · → 05-03 seed saving · → 26-08 expiry tracker · → 26-09 the shopping list.

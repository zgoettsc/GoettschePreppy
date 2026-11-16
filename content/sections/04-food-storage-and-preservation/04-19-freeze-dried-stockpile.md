---
id: 04-19-freeze-dried-stockpile
section: 04-food-storage-and-preservation
title: "Freeze-dried meals: buying, checking and storing a stockpile"
version: 1
revised: 2026-11-16
layer: core
danger_level: critical
phase: [A, B, C]
tags: [food, freeze-dried, dehydrated, stockpile, allergens, labels, water, storage, inventory]
derived_from: [04-19-freeze-dried-stockpile]
sources:
  - utah-state-university-extension-oxygen-absorbers-dry-d72137
  - usda-food-safety-and-inspection-service-fsis-shelf-s-942af8
  - us-fda-food-allergies-627fb6
  - usda-hhs-dietary-guidelines-for-americans-2020-2025-4b2013
related: [04-01-calorie-and-stockpile-math, 04-02-building-a-pantry, 04-03-bulk-staples-storage, 04-06-dehydrating, 04-09-winter-cold-storage, 04-10-rotation-and-inventory, 04-11-pests-and-rodents, 03-01-daily-water-needs, 07-01-cooking-on-an-open-fire, 07-05-propane-and-camp-stoves, 07-06-electric-kettle-cooking, 07-07-freeze-dried-rehydration, 01-03-phase-b-movement, 23-02-master-consumables-table, 22-04-household-inventory, 02-04-cl04-food-allergy, 02-03-cl03-anaphylaxis, 29-14-ex14-reading-a-label, 30-19-dc18-unlabeled-food-and-allergies]
cards: [DC-18]
explainers: [EX-14]
promote_when: []
photo_slots:
  - { id: freeze-dried-shelf, caption: "Our freeze-dried shelf: where it is, how the allergy-safe stock is kept apart" }
figures: []
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: null
---

# Freeze-dried meals: buying, checking and storing a stockpile

**What this page is for.** How freeze-dried meals fit into a food store, how much to buy for your
household, how to check every product for allergens, how much water they need, and how to store
them so the long shelf life on the label is true.

> **SAFETY.** **Commercial freeze-dried and "emergency food" products very often contain soy, egg,
> milk or wheat, and recipes change without notice** (→ 04-02). If anyone in the house has a food
> allergy, every pouch must be **checked against their allergy list before purchase, checked again
> at purchase, and kept apart** (protocol below). A stockpile that skips that check can be a
> stockpile of allergy triggers with a 25-year shelf life (→ 02-04, → 02-03).

## Do this now

1. **Read the directions on every product and write down its TYPE:**
   - **"Add boiling water, wait"** = **true freeze-dried.** It is already cooked; cold-water
     soaking works too (slowly).
   - **"Boil" or "simmer X minutes"** = **dehydrated or blended "emergency food"** (most bucket
     systems, many "just add water" pasta and rice blends). Its pasta, beans and textured soy are
     **not precooked;** it needs **a real boil on a stove** (→ 07-05, → 07-01) and is **NOT a
     cold-water meal.**
   - **Water per pouch is the label's figure.** About 2 cups is only a planning average.
2. **Run the allergen protocol below on every product before buying** if anyone in the house has
   a food allergy. No exceptions, no "same brand, probably fine".
3. **Fill in the inventory table** as you buy. An uncounted stockpile cannot be planned with.
4. **Mark every container** safe or not safe for each allergic person, in bold marker, and shelve
   the safe stock separately.
5. **Store cool, dry and sealed:** not the garage, not the attic. Heat is what breaks the
   "25-year" claim.
6. **Count the water these meals need** into your water plan (→ 03-01).

## Where freeze-dried food fits

| Property | Why it matters |
|---|---|
| **Long dating** ("25 years" is a manufacturer claim, for cool storage) | Buy once; less rotation work (see the rotation note below) |
| **No cooking: only hot water** (true freeze-dried) | About 2 cups of boiling water per pouch (the label governs); about 55 Wh at an electric kettle, more from a battery after inverter losses (→ 07-06). No fire, no pot to wash. **Dehydrated "simmer" products do not qualify:** they need a stove |
| **Cold-water fallback** (true freeze-dried only) | Softens in cold water in **1 to 2 hours:** a zero-energy meal when power is rationed (→ 07-07). **Never for a "boil/simmer" product** |
| **Weight** | The most calories per pound of any ready-to-eat food (→ 04-01); good for leaving home |

**Staples are cheaper per calorie** (→ 04-03), and freeze-dried food does not replace them. It is
the **ready-to-eat, no-fuel, travels-well layer** on top. Both count toward the runway (→ 04-01,
→ 23-02).

## How much to buy

Your household needs about **{{ derived.calories.day }} calories a day** (→ 04-01 shows how
that is worked out from the published USDA/HHS table for your {{ household.size }} people).

> **target days × {{ derived.calories.day }} ÷ calories per serving (from the label) = servings
> to stock**

| Target | Calories needed | Servings to stock |
|---|---|---|
| 2 weeks | {{ derived.calories.two_weeks }} | {{ derived.calories.two_weeks }} ÷ ______ calories per serving = ______ |
| 1 month | {{ derived.calories.day }} × 30 = ______ | ÷ ______ = ______ |
| 3 months | {{ derived.calories.day }} × 90 = ______ | ÷ ______ = ______ |

**Check it a second way.** Count meals, not just calories: {{ household.size }} people × 3 meals
a day × the number of days, and compare that with the label's servings. Plan from the calories,
not the serving count: a label's serving size may not match what your household eats. You have **{{ gear.food.freeze_dried_servings }}
servings** logged now.

**Run the same line for any restricted diet alone,** using that person's own figure from
→ 04-01 and only the products marked safe for them. That runway is computed separately and is
usually the one that matters most.

**Babies under 12 months** are not in these numbers: they need breast milk or infant formula
(→ 02-13, → 20-05). Freeze-dried meals are not baby food.

## The allergen protocol

Most commercial freeze-dried meals contain **soy** (soy protein, soy lecithin, "vegetable oil"),
many contain **egg, milk or wheat,** and **sesame** turns up in seasoning blends. US labels must
name the nine major allergens: milk, egg, fish, shellfish, tree nuts, peanuts, wheat, soybeans and
sesame (FDA, Food Allergies). How to read a label: → 29-14.

{{#each allergies as a}}
- **{{a.member}}:** {{a.allergen}} ({{a.severity}})
{{else}}
- No allergies are entered for your household. If none applies, skip to the inventory table.
{{/each}}

1. **BEFORE purchase:** get the full ingredient list and "Contains" line for the exact product and
   size, and check it against every allergy above. **An allergen outside the nine never appears in
   a "Contains" line:** read the full list. Check the maker's "made in a facility with" statements
   and follow the allergist's advice on traces.
2. **AT purchase:** read the physical label on the units in your hand again. **Recipes change;** a
   product checked last year is not checked today. Write the date you checked it.
3. **AFTER purchase:** mark every container safe or not safe, log it in the table below, and shelve
   the safe products **physically apart:** their own bin, their own shelf, above the others.
4. **A product that fails any step is not for that person,** and is marked and stored that way.

**Where this fits with → 04-02:** that page warns against buying a year of unchecked bucket food,
and the warning stands. This protocol is the discipline that makes the category usable: checked
single products, not blind buckets. Feeding an allergic person food you could not check:
{{choice DC-18}} → 30-19.

{{photo freeze-dried-shelf}}

## Inventory table

The products on your shelf are a fact you record here. Keep it current: it feeds every runway
number on → 04-01 and → 23-02.

| Product (maker and exact name) | **Type: FD (add water, wait) or DEHYD (boil X min)** | Water per pouch (label) | Servings | Calories per serving | **Safe for each allergy? (date checked)** | Bought | Lot number, best-by |
|---|---|---|---|---|---|---|---|
| ______ | ______ | ______ | ______ | ______ | ______ | ______ | ______ |
| ______ | ______ | ______ | ______ | ______ | ______ | ______ | ______ |
| ______ | ______ | ______ | ______ | ______ | ______ | ______ | ______ |
| ______ | ______ | ______ | ______ | ______ | ______ | ______ | ______ |
| ______ | ______ | ______ | ______ | ______ | ______ | ______ | ______ |
| ______ | ______ | ______ | ______ | ______ | ______ | ______ | ______ |

**Totals:** calories on hand ______ · **allergy-safe calories on hand ______** (track separately).

## The water these meals need

Freeze-dried food **uses your water;** that is the price of the convenience.

- **Your plan figure is {{ derived.water.plan_gal_day }} gallons a day** for the household
  (→ 03-01). Treat it as the least you need if you will eat mostly freeze-dried food.
- **About 2 cups of boiling water per pouch** (the label governs): small boils, about 55 Wh each
  at an electric kettle (→ 07-06).
- **Cold water works for TRUE freeze-dried pouches:** 1 to 2 hours instead of about 10 minutes,
  worse texture, no energy (→ 07-07). A "boil/simmer" product needs the stove.
- **When water is short, eat this food LAST.** Canned food brings its own water; freeze-dried
  food takes yours (→ 04-01 has the table).

## Storage: heat is the enemy of the 25-year claim

The long shelf-life figures assume **cool storage.** Utah State University Extension's research
summary is blunt: the ideal is **40 to 70 °F**, and the same stored wheat that kept about 25 years
in a cool basement kept **about 5 years in a hot garage or attic** (Utah State University
Extension). Treat every "25-year" label as conditional on:

- **Cool:** a basement or interior closet. **Never** the garage, the attic, or a vehicle or
  trailer parked in the sun.
- **Dry:** dried food that picks up moisture grows mould and bacteria. Off the concrete floor,
  low humidity. {{#if is.hot_summers}}Your summers are hot: find the coolest place in the house
  for this.{{/if}} In humid places this matters twice as much (→ 04-09).
- **Sealed:** unopened original packaging (cans, pouches with oxygen absorbers). **An opened
  container is ordinary food:** reseal it and use it within weeks, faster in humid weather
  (USDA FSIS, Shelf-Stable Food Safety).
- **Dark, and off concrete.**

## Rotation: 25-year food does not rotate like a pantry

"First in, first out" (→ 04-02, → 04-10) does not fit food you may not outlive. Instead:

- **Check seals once a year:** walk the shelf and look at every can and pouch for swelling,
  punctures, crushed seams and rodent damage (→ 04-11). Throw out swollen or punctured ones.
  Log the check on → 23-02.
- **Eat one pouch of each product each year.** It confirms people will eat it, teaches the
  preparation, and catches a bad batch. Replace what you eat.
- **Re-check the allergy marks** at the same yearly walk: anything opened, water-damaged or
  unlabelled loses its "safe" mark until checked again.

## Gear and supplies

| Item | Why | Notes |
|---|---|---|
| Checked freeze-dried products, logged above | The stockpile | Check BEFORE buying; mark at purchase |
| A separate bin or shelf for allergy-safe stock | Physical separation | Above other food (→ 02-04) |
| Bold markers and labels | Safe or not safe | Re-mark at every yearly check |
| Printed ingredient labels or photos, filed | Re-checking without internet | Tape inside the bin lid |
| Water storage sized to your plan figure | The paired consumable | → 03-01 |
| Kettle or small pot, measuring cup | About 2 cups boiling per pouch | An insulated bottle saves energy |
| This page's inventory table, kept current | Runway input | Feeds → 04-01 and → 23-02 |

**If you don't have it:**

- Scavenged freeze-dried food is **not for an allergic person unless the label is intact and
  passes the full protocol.** For them, sealed single-ingredient staples are the safest find.
- Home-dried food (→ 04-06) is the home-made cousin: heavier and shorter-lived, but fully
  traceable.

## When it runs out

- **Runway:** total logged calories ÷ {{ derived.calories.day }}, **plus** the staples runway
  (→ 04-01). The figure on → 23-02 is the SUM. Work out each restricted diet's runway separately.
- **Ration:** it is the best travel and no-fuel food. Many households save it for moving days and
  days when power or fuel is rationed, and eat staples on ordinary days when the stove works.
  Where one person eats a restricted diet, agree in advance whether their safe pouches are held as
  their reserve while everyone else eats the general stock (→ 02-04).
- **Resupply:** most households cannot make freeze-dried food; the substitutes are drying
  (→ 04-06), canning (→ 04-04, → 04-05) and production (Section 05).
- **The honest limit:** this layer is bought, not renewable. It buys months of certainty;
  Section 05 buys years.

## Phase notes

- **A (sheltering at home):** buy and check now; store cool; do the yearly seal walk.
- **B (moving):** the densest ready-to-eat calories you own; first into the vehicle after any
  allergy-safe or medical-diet bin (→ 04-01 grab order, → 01-03).
- **C (rural or at a destination):** bridge food while production starts. In humid places the
  sealed-container and reseal rules get stricter (→ 04-09).

## Cross-references

→ 04-01 runway and grab-load math · → 04-02 the unchecked-bucket warning (stands) · → 04-03
staples · → 03-01 water · → 07-07 rehydrating · → 02-04 food allergy · → 04-10 inventory ·
→ 04-11 pests

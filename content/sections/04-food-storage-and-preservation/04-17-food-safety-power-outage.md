---
id: 04-17-food-safety-power-outage
section: 04-food-storage-and-preservation
title: "Food safety when the power fails"
version: 1
revised: 2026-11-16
layer: core
danger_level: critical
phase: [A]
tags: [food, power outage, refrigerator, freezer, food safety, 40 F, dry ice, triage]
derived_from: [04-17-food-safety-power-outage]
sources:
  - foodsafety-gov-usda-hhs-food-safety-during-a-power-o-3894c1
  - foodsafety-gov-usda-hhs-cook-to-a-safe-minimum-inter-13daf3
  - cdc-keep-food-safe-after-disaster-2025
  - cdc-carbon-monoxide-poisoning-basics-772153
  - us-fda-information-regarding-insulin-storage-and-swi-6448d3
related: [04-01-calorie-and-stockpile-math, 04-02-building-a-pantry, 04-03-bulk-staples-storage, 04-05-canning-pressure, 04-09-winter-cold-storage, 04-14-powdered-and-canned-dairy, 01-01-phase-a-shelter-in-place, 03-02-storing-water, 07-01-cooking-on-an-open-fire, 09-01-power-priorities, 09-03-batteries-and-storage, 09-04-generators, 09-05-solar-in-winter, 09-16-outage-day-one, 12-05-common-illness-and-dehydration, 02-01-cl01-type-1-diabetes-injections, 02-04-cl04-food-allergy, 29-02-ex02-batteries-and-power-stations, 29-07-ex07-refrigerated-medicines, 29-14-ex14-reading-a-label, 30-01-the-floors, 30-15-dc14-questionable-food]
cards: [DC-14]
explainers: [EX-02, EX-07, EX-14]
promote_when: []
photo_slots:
  - { id: freezer-inventory-card, caption: "Our freezer inventory card, taped to the lid" }
figures: []
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: null
---

# Food safety when the power fails

**What this page is for.** What to do with the food in your fridge and freezer from the moment
the power goes out: how long it stays safe, what to eat first, what to throw out, and how to
stretch the cold.

> **SAFETY.** **Never taste food to find out whether it is safe** (FoodSafety.gov). Food
> poisoning without a working hospital is not an inconvenience: vomiting and diarrhoea mean
> dehydration, which is dangerous for babies, small children, elders and anyone with diabetes
> (→ 12-05). **When in doubt, throw it out.**
>
> **Floor:** **Never run a generator, charcoal, or any engine indoors, in a garage, or near an
> open window.** Carbon monoxide kills in minutes with no warning (→ 30-01).
>
> **Floor:** **A frozen-then-thawed insulin vial or pen is discarded.** Loss of potency with no
> way to tell (→ 30-01). Medicines follow different rules from food (→ 29-07).

## Do this now: the first hour

1. **Keep the fridge and freezer doors shut.** Every opening costs hours of safe storage.
2. **A closed fridge keeps food safe for up to 4 hours.**
3. **A full freezer keeps food safe for about 48 hours; a half-full one about 24 hours,** with
   the door kept shut.
4. **Throw out perishable food** (meat, poultry, fish, eggs, milk, leftovers) that has been
   **above 40 °F for 2 hours or more.**
5. **Move insulin and other refrigerated medicines to their own managed cold,** with its own
   thermometer (→ 02-01, → 29-07). {{#if has.refrigerated_meds}}**Someone in your household
   takes a refrigerated medicine: do this first.**{{/if}}
6. **In cold weather, use the outdoors, but measure it** (→ 04-09).
7. **Put a thermometer in the fridge and the freezer** if they are not already there.

(All times and temperatures: FoodSafety.gov, Food Safety During a Power Outage; CDC gives the
same 4, 48 and 24 hours in Keep Food Safe After a Disaster or Emergency.)

## The clock

| Appliance | Safe holding time, door kept shut |
|---|---|
| **Refrigerator** | **Up to 4 hours;** after that, perishables (meat, poultry, fish, eggs, leftovers) are thrown out |
| **Freezer, full** | **About 48 hours** |
| **Freezer, half full** | **About 24 hours** |

**Every door opening sets you back.** Decide what you need *before* you open it, take it all at
once, and close it.

## The danger zone

Bacteria multiply fast between **40 °F and 140 °F**. The rule that follows: **perishable food
above 40 °F for 2 hours or more is thrown out.**

**Put an appliance thermometer in the fridge and the freezer now,** so that when the power comes
back (or when you check) you know what actually happened instead of guessing. It costs a few
dollars and it is the difference between a decision and a coin toss.

## The eating order

1. **Fridge perishables first:** meat, dairy, leftovers, opened items. Cook them now, to safe
   inside temperatures (→ 07-01).
2. **Freezer contents next,** as they thaw. **Cook thawed meat while it is still cold,** or
   preserve it (→ 04-05).
3. **Then the pantry** (→ 04-02).
4. **Then bulk staples** (→ 04-03).

**Cook a large batch early.** Cooking **resets** the clock; it does not stop it. Cooked food and
leftovers follow the **same 40 °F and 2-hour rule** as raw food (FoodSafety.gov). The gain is
that it feeds people now and turns a spoilage problem into meals. **Eat it or chill it;** in cold
weather that can mean outside in measured cold (→ 04-09), never "it's cooked, it'll keep on the
counter."

## Stretching the freezer with the power you have

The 48-hour and 24-hour times above are for a freezer with **no power.** If you have stored
power, it can buy more time, but it competes with medical needs and other loads for the same
energy (→ 09-01).

{{#if has.power_station}}- **Your power stations** total **{{ gear.station_wh_total }} Wh.** The
  binder's rough estimate is that this runs a typical full-size fridge (about 1.2 kWh a day) for
  **about {{ derived.station_fridge_days }} days** per full charge. It is an estimate; your own
  appliance may use more or less (→ 09-03, → 29-02).{{else}}- **A power station** (a large
  rechargeable battery with outlets, → 29-02) can run a fridge or freezer for a day or more,
  depending on its size and the appliance (→ 09-03).{{/if}}
- **Find your own appliance's daily use** on its yellow EnergyGuide label: kilowatt-hours per
  year ÷ 365 = kilowatt-hours per day (→ 29-14). Compare it with your stored watt-hours
  (1 kWh = 1,000 Wh).
{{#if has.generator}}- **Your generator** can recharge batteries or run the freezer directly in
  short runs, as long as fuel lasts (→ 09-04). Outdoors only, as the floor above says.{{else}}- A
  **generator** can run the freezer in short runs while fuel lasts (→ 09-04). Outdoors only, as
  the floor above says.{{/if}}
{{#if has.solar}}- **Solar** gives partial refills. In winter, short days and snow cut output
  hard; a December day may not carry a freezer (→ 09-05).{{/if}}

**The moment the outage looks longer than your fuel, stop bridging and start triage:**

1. **Any frozen food that someone on a restricted diet depends on, first.** Allergy-safe or
   medical-diet food is the one category that scavenging, charity and barter **cannot replace**
   (→ 02-04). Cook it, or move it to your coldest backup.
2. **Raw meat second:** the biggest loss and the best to convert. Cook it or pressure-can it
   (→ 04-05) while it is still at 40 °F or below.
3. **Cooked food and leftovers:** eat these in the first day's big meals.
4. **Bread and frozen fruit last:** FoodSafety.gov lets these be kept or refrozen even after
   2 hours above 40 °F, unless mouldy, slimy or yeasty-smelling. **Frozen vegetables are
   thrown out after 6 hours above 40 °F.**

**Keep a freezer inventory card.** Tape a card to the freezer lid and update it whenever the
contents change: what is inside, where (top or bottom), and which items are allergy-safe or
medical-diet food. Then triage decisions get made **without opening the door,** and the card
answers "is it worth running the generator?" with a list instead of a guess.

{{photo freezer-inventory-card}}

## Making the cold last

- **Dry ice or block ice:** CDC advises buying it to keep food cold if the power could be out for
  a long time (CDC, Keep Food Safe After a Disaster or Emergency). Handle dry ice with gloves,
  never bare hands, and **never in a closed space with people** (it turns to carbon dioxide gas,
  which pushes out the air).
- **Block ice** lasts longer than cubes.
- **Fill empty freezer space** with jugs of water. A full freezer stays cold much longer, and the
  frozen jugs become drinking water later (→ 03-02).
- **Blankets over the freezer** (not covering any vents) help hold the cold.
- **In cold weather, the outdoors is a freezer,** with the cautions on → 04-09.

## What to keep and what to throw out

| Food | If above 40 °F for 2 hours or more |
|---|---|
| Meat, poultry, fish, eggs | **Throw out** |
| Leftovers, casseroles, cooked dishes | **Throw out** |
| Soft cheeses, milk, cream, yogurt, reconstituted powdered milk | **Throw out** |
| Hard cheeses (cheddar, Swiss, parmesan), processed cheese | Keep |
| Shredded and low-fat cheeses | **Throw out** |
| Butter, margarine | Keep |
| Opened creamy dressings | **Throw out** |
| Opened mayonnaise, tartar sauce, horseradish | **Throw out** if above 50 °F for 8 hours or more |
| Opened vinegar-based dressings, peanut butter, jelly, mustard, ketchup, pickles | Keep |
| Fresh fruit and vegetables, **uncut** | Keep |
| Fresh fruit and vegetables, **cut**; cooked vegetables, cooked pasta, rice and potatoes | **Throw out** |
| Bread, rolls, cakes without custard fillings | Keep |
| Unopened shelf-stable items | Keep |

(FoodSafety.gov's full chart lists more foods. In the Large and Everything downloads it is bound
in this binder: the "Sources for this page" list below links to it.)

**Thawed food that still has ice crystals and is at 40 °F or below** can generally be refrozen,
with some loss of quality (FoodSafety.gov). Fully thawed and warm is thrown out.

**Infant formula** that has been mixed follows its own, shorter rules (→ 02-13, → 20-05).

## The judgment rule

**No smell test. No taste test.** The germs that cause food poisoning do not reliably announce
themselves. How strictly your household follows these published lines when food is truly short
is a decision card: {{choice DC-14}} → 30-15. Bulging, leaking or spurting cans are not part of
that choice: they are thrown away.

## Medicine is not food

This page is about food. **Insulin and other refrigerated medicines follow different numbers and
fail the opposite way:** they must stay cool but **must never freeze** (FDA, Information Regarding
Insulin Storage). Do not let "keeping things cold" become one shared job. Give medicine its own
container and its own thermometer (→ 02-01, → 29-07).

## Gear and supplies

| Item | Why | Notes |
|---|---|---|
| **Appliance thermometers** (fridge and freezer) | Know what actually happened | A few dollars each |
| **Instant-read food thermometer** | Cooking safely (→ 07-01) | And a spare |
| Water jugs to fill freezer space | Holds cold longer; becomes drinking water | Free |
| Coolers | Gather together what you are keeping | Also → 04-09 |
| Blankets for the freezer | Buys hours | Do not cover vents |
| A known dry-ice source | Extends a freezer by days | Find it before you need it |
| **Freezer inventory card,** taped to the lid | Triage without opening the door | Mark allergy-safe and medical-diet items |
| Charged power station, or generator fuel | The powered bridge | → 09-03, → 09-04 |

**If you don't have it:**

- **Snow and ice** in winter (→ 04-09).
- Coolers packed with snow; an unheated garage or the north side of the house.
- **Cooking and eating** is always a valid way to "preserve" food.

## When it runs out

- **Runway:** refrigerated food is measured in **hours,** not days. Plan to turn it into meals or
  preserved food at once.
- **Ration:** eat the most perishable first; do not "save" meat that is on the clock.
- **Resupply:** pressure canning (→ 04-05) turns thawing meat into shelf-stable food, the best
  answer to a freezer full of meat in a long outage, if you have jars, lids and fuel.
- **The season matters:** a summer outage is a food emergency within hours; a winter outage in a
  cold place is an opportunity (→ 04-09). Know which one you are in.

## Phase notes

- **A (sheltering at home):** this page is the first-day food plan (→ 01-01, → 09-16).
- **B (moving):** take shelf-stable food only; leave the fridge behind.
- **C (rural or at a destination):** the same rules; less resupply, so making food shelf-stable
  matters more.

## Cross-references

→ 04-09 winter cold storage · → 04-05 pressure canning thawing meat · → 04-01 calorie math ·
→ 09-01 power priorities · → 09-03 batteries · → 09-04 generators · → 02-01 insulin ·
→ 02-04 food allergy · → 07-01 safe cooking temperatures · → 12-05 illness

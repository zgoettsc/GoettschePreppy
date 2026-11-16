---
id: 25-01-planting-calendar
section: 25-reference-and-appendices
title: "Planting and harvest calendar for your frost dates"
version: 2
revised: 2026-11-16
layer: region
danger_level: none
phase: [A, C]
tags: [garden, planting calendar, frost dates, hardiness zone, seed starting, season extension, storage crops]
derived_from: [25-01-planting-calendar]
sources:
  - usda-phzm-2023
  - university-of-minnesota-extension-planting-the-veget-acacfa
  - university-of-minnesota-extension-starting-seeds-ind-2449d5
related: [05-01-a-small-high-yield-garden, 05-02-season-extension, 05-03-seed-saving, 05-11-soil-and-compost, 05-13-perennials-and-fruit, 05-14-indoor-growing, 05-18-destination-garden-calendar, 04-09-winter-cold-storage, 25-05-blank-logs, 24-03-seasonal-practice-plan]
cards: []
explainers: [EX-13]
promote_when: [has.garden]
photo_slots: []
figures: [fig-planting-timeline]
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: { date: "2026-11-16", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "SDSU (owner-state) citation dropped; hardening-off period aligned with UMN Extension." }
---

# Planting and harvest calendar for your frost dates

**What this page is for.** Almost every garden date hangs off two dates: the **last spring
frost** and the **first fall frost**. A frost is a night cold enough (32 °F or below) to kill
tender plants. This page prints your county's median dates from the region data and then gives
a method that works in any climate: count weeks backwards and forwards from those dates. It
never needs a month-by-month calendar for one place.

## Your numbers

| | Home: {{ home.county }}, {{ home.state_name }} |
|---|---|
| **Last spring frost (median)** | {{ region.home.last_frost }} |
| **First fall frost (median)** | {{ region.home.first_frost }} |
| **Frost-free days (median)** | {{ region.home.growing_days }} |
| **USDA hardiness zone** | {{ region.home.zone }} |
| **July mean high** | {{ region.home.jul_high_f }} °F |
| **Elevation** | {{ region.home.elevation_ft }} ft |

{{#if has.destinations}}| Destination | Last frost | First frost | Frost-free days | Zone |
|---|---|---|---|---|
{{#each destinations as d}}| {{d.name}} ({{d.county}}, {{d.state_name}}) | {{d.region.last_frost}} | {{d.region.first_frost}} | {{d.region.growing_days}} | {{d.region.zone}} |
{{/each}}

The destination garden plan is → 05-18.
{{/if}}

**Median means half of years are worse.** A median last frost is the date after which a frost
happens in about half of years, so a late frost after it is normal, and low spots in a yard
frost earlier than the street. Plan to cover tender plants for two or three weeks either side,
and keep your own record (→ 25-05): two years of your own dates beat any published table.

**The hardiness zone is about winter, not summer.** It is the coldest winter night on average,
and it tells you which **perennials** (fruit trees, bushes, asparagus, rhubarb) survive the
winter (USDA, Plant Hardiness Zone Map). It does not tell you when to plant vegetables; the
frost dates do.

## Do this now

1. **Copy the two frost dates onto a wall calendar** and mark the weeks before and after each
   (the timeline below).
2. **Order seed in mid-winter.** Popular open-pollinated varieties sell out, and seed is the
   cheapest, lightest, most time-sensitive purchase in the binder (→ 05-03, → 22-07).
3. **Count backwards from the last frost** to get every indoor sowing date (table below), and
   write them on the calendar.
4. **Start a garden log** (→ 25-05).

## Read your season length first

{{figure fig-planting-timeline}}

| Your season | What it means | What to do |
|---|---|---|
| **Short**: frost-free days not much more than the "days to maturity" of tomatoes or winter squash on their packets | Warm-season crops barely finish. Cool-season crops do well | Start tomatoes, peppers and squash indoors; choose short-season ("days to maturity" well under your frost-free days) varieties; season extension matters most (→ 05-02) |
| **Middle**: room for slow crops with weeks to spare | A full spring-summer-fall garden | Use the tables as written; cool crops in spring and again for fall |
| **Long**: frost comes late or rarely, and summers are hot | Summer heat, not frost, is the limit. Lettuce and peas bolt (go to seed) in heat | Plant cool-season crops in late summer to grow through fall and winter; warm crops in spring; shade cloth and mulch in midsummer |
| **No regular frost** | Frost dates are blank or rare | Plant by season and soil temperature: cool crops in the cool months, warm crops in the warm months; watch for the hottest, driest weeks instead |

{{#if is.hot_summers}}**Your summers are hot** (July mean high {{ region.home.jul_high_f }} °F): expect the long-season pattern.
Spring cool crops must be in early; plan a second, larger cool-season planting in late summer.
{{/if}}{{#if is.cold_winters}}**Your winters are cold** (January mean low {{ region.home.jan_low_f }} °F): perennials must be
hardy to your zone, and root crops can stay in the ground under heavy mulch into early winter.
{{/if}}{{#if is.high_altitude}}**You are above 5,000 ft:** nights are colder than the frost dates suggest, sun is strong, and the
season is often shorter than the county median. Use frost cover generously.
{{/if}}

**Check every seed packet's "days to maturity"** against your frost-free days. A crop needing
more days than your season gives must be started indoors or swapped for a faster variety.

## Indoor sowing: count backwards from the last frost

Seedlings started indoors need a sunny window or a grow light, and warmth to sprout
(University of Minnesota Extension, Starting Seeds Indoors).

| Crop | Start indoors | Plant out | Notes |
|---|---|---|---|
| **Onions, leeks** | **10 to 12 weeks before** last frost | About 4 weeks **before** last frost | Very cold-tolerant |
| **Celery** | 10 to 12 weeks before | After last frost | Slow |
| **Peppers, eggplant** | **8 to 10 weeks before** | About **2 weeks after** last frost, in warm soil | Dislike cold soil |
| **Tomatoes** | **6 to 8 weeks before** | After last frost | Do not start too early: leggy plants transplant badly |
| **Broccoli, cabbage, cauliflower** | 6 to 8 weeks before | 2 to 4 weeks **before** last frost | Hardy |
| **Lettuce, greens** | 4 to 6 weeks before | 3 to 4 weeks before | Or sow directly |
| **Cucumbers, melons, squash** | **3 to 4 weeks only** | After last frost | Dislike transplanting: sow in pots that go into the ground whole |
| **Basil and tender herbs** | 6 to 8 weeks before | After last frost, warm | Frost-tender |

**Harden off everything over one to two weeks** before it goes out: set seedlings outside for a few
hours, then longer each day, so sun and wind do not kill them in an afternoon (University of
Minnesota Extension, Planting the Vegetable Garden; → 05-14).

My dates this year: onions ______ · peppers ______ · tomatoes ______ · brassicas ______ ·
squash ______ · plant out ______.

## Direct sowing, relative to the frost dates

| When | Crops |
|---|---|
| **4 to 6 weeks before last frost** (as soon as the soil can be worked) | Peas, spinach, radish, turnip, mustard |
| **2 to 4 weeks before** | Carrots, beets, chard, lettuce, kale, potatoes, onion sets |
| **At or after last frost** | Beans, corn, squash, cucumber, melon, sunflower |
| **2 weeks after** | Anything that wants truly warm soil |
| **For a fall crop** | Beets, carrots, kale, lettuce, spinach, radish, turnip: count back from the **first fall frost** by the packet's days to maturity, plus a couple of weeks for slower autumn growth |
| **Fall** | **Garlic** (a few weeks before the ground freezes, or in the cool season where it does not) and cover crops |

A soil thermometer is the honest test: it tells you when the ground is ready better than any
date (→ 29-13).

## The year as weeks around your frost dates

| When | Garden work |
|---|---|
| **12 weeks before last frost** | Order seed. Test saved seed for germination. Plan beds and rotation |
| **10 to 12 weeks before** | Start onions and leeks. Prune fruit trees while dormant (→ 05-13). Set up lights |
| **6 to 10 weeks before** | Start peppers, eggplant, brassicas, then tomatoes. Build and repair beds. Turn compost (→ 05-11) |
| **2 to 6 weeks before** | Sow peas, spinach, radish as the soil works. Potatoes and onion sets. Row cover on |
| **Last frost to 2 weeks after** | Harden off, then transplant. Sow beans, corn, squash. **Be ready to cover for a late frost** |
| **Early summer** | Succession-sow lettuce, beans, carrots every 2 to 3 weeks. Mulch heavily. Watch pests (→ 05-12) |
| **Midsummer** | Water deeply. **Sow the fall crops.** Harvest and preserve as things come in (→ 04-04, → 04-06) |
| **Late summer** | Peak harvest and preservation. Save seed from the best plants (→ 05-03) |
| **Around the first frost** | Harvest tender crops ahead of it. **Cover for early frosts**: warm weeks often follow. Plant garlic and cover crops |
| **After the first frost** | Root crops into cold storage (→ 04-09). Clean up, mulch, compost. **Write down what worked** |
| **Winter** | Clean, oil and sharpen tools (→ 16-02). Plan. Check stored crops for spoilage |

## What actually feeds a family

Ranked by calories per square foot, with storage in mind:

| Rank | Crop | Why |
|---|---|---|
| **1** | **Potatoes** (or **sweet potatoes** in long, hot seasons) | Most calories per square foot; store well (→ 04-09) |
| **2** | **Winter squash** | Dense calories; keeps for months at room temperature |
| **3** | **Dry beans** | Protein, stores dry, no processing |
| **4** | **Corn (flour or flint types)** | Calories and long storage; needs space |
| **5** | **Beets, carrots, turnips, rutabaga** | Store in damp sand, or in the ground under mulch where winters allow |
| **6** | **Onions, garlic** | Keep long; flavour matters for morale |
| **7** | **Cabbage** | Stores, and ferments into sauerkraut (→ 04-08) |
| **8** | **Kale, chard, spinach** | Vitamins and cold tolerance, few calories |
| **9** | Tomatoes, cucumbers, peppers | Vitamins, preserving and morale, **not calories** |

**The honest note:** a good home garden is a **meaningful supplement and a large morale and
vitamin asset.** It will not feed a family for a year. Grain and fat are the gaps (→ 23-04).

## Frost protection: what buys how much

| Method | Buys | Notes |
|---|---|---|
| Floating row cover | 2 to 4 °F | Cheap; also keeps insects off |
| Doubled row cover or a low tunnel | 4 to 8 °F | The workhorse |
| Cold frame | Several weeks at each end of the season | → 05-02 |
| Water jugs among the plants | A few degrees overnight | Free |
| Mulch | Protects roots and moisture | Also stops weeds |
| Sheets and blankets, for one night | A few degrees | The emergency answer to a late frost |

## How long the harvest keeps (approximate, in a cold room)

| Crop | Keeps | Conditions |
|---|---|---|
| Potatoes | 4 to 6 months | Dark, about 40 °F, humid; **never with apples or onions** |
| Winter squash | 3 to 6 months | Cool and **dry**, about 50 °F |
| Onions, garlic | 4 to 8 months | Cool, dry, airy |
| Carrots, beets, turnips | 4 to 6 months | Cold and damp: sand or damp sawdust |
| Cabbage | 2 to 4 months | Cold and damp |
| Apples | 2 to 5 months | Cold; **away from potatoes** |

Full detail: → 04-09. In warm climates without a cold room, the storage crops are squash, sweet
potatoes, dry beans and grain, and the rest is preserved (→ 04-04 to → 04-08).

## Blanks to fill in (once, then every year)

```
MY LAST SPRING FROST: ____________   EARLIEST I HAVE SEEN: ____________
MY FIRST FALL FROST:  ____________   LATEST I HAVE SEEN:   ____________
FROST-FREE DAYS: ______

LAST YEAR: last frost ________  first frost ________  first hard freeze ________
BEST PERFORMERS: __________________________________________
FAILURES (and why): _______________________________________
CHANGE NEXT YEAR: _________________________________________
```

## Gear

**Buy toward:** **open-pollinated seed** (bought in mid-winter), a soil thermometer, row cover
and hoops, a grow light and heat mat, seed trays and mix, plant labels and a pencil, a garden
notebook.

**If you do not have it:** milk jugs make cloches; old windows make cold frames; bedsheets cover
a frost night; yogurt pots and newspaper pots start seed; a sunny window substitutes, poorly,
for a grow light. **Seed saved from open-pollinated plants is free forever** (→ 05-03).

## When it runs out

Seasons, not supplies.

- **Each planting window is one to three weeks wide. Miss it and you wait a year.**
- **If you can only do part of a garden**, plant **potatoes, squash and beans** (the calorie
  crops) plus greens for vitamins.
- **Save your own seed** (→ 05-03): the only way this calendar keeps working when seed cannot
  be bought.
- Indoor growing and sprouting stretch the season at the edges (→ 05-14, → 04-16), and cold
  storage stretches the harvest into spring (→ 04-09).

## Phase notes

- **A (shelter in place):** garden the yard, containers and any balcony (→ 05-01, → 05-10).
  Learn the calendar in your own soil while mistakes are cheap.
- **B (moving):** carry seed. **It weighs nothing and is the most valuable thing you can bring
  to a new place.**
- **C (establish):** this calendar is the year's work, recalculated for the new place's frost
  dates (→ 05-18). Scale up and add grain and storage crops.

Related: → 05-01 the garden · → 05-02 season extension · → 05-03 seed saving · → 05-11 soil ·
→ 04-09 cold storage · → 04-04 and → 04-06 preserving · → 24-03 the practice calendar ·
→ 25-05 the garden log · → 05-13 fruit (plant now, harvest in years).

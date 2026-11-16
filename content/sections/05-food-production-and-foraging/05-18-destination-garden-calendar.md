---
id: 05-18-destination-garden-calendar
section: 05-food-production-and-foraging
title: "Garden calendar for each destination"
version: 2
revised: 2026-11-16
layer: household
danger_level: none
phase: [A, C]
tags: [garden, destination, frost dates, hardiness zone, growing season, fall garden, seed cache, planting calendar]
derived_from: [05-18-goshen-ozark-garden-calendar, 05-01-small-urban-garden]
sources:
  - university-of-minnesota-extension-planting-the-veget-acacfa
  - university-of-minnesota-extension-starting-seeds-ind-2449d5
  - noaa-ncei-normals-1991-2020
  - usda-phzm-2023
related: [05-01-a-small-high-yield-garden, 05-02-season-extension, 05-03-seed-saving, 05-11-soil-and-compost, 05-12-pollination-and-pests, 05-13-perennials-and-fruit, 05-19-destination-foraging-and-hazards, 01-05-choosing-a-destination, 01-04-phase-c-establish, 25-01-planting-calendar, 19-01-document-grab-kit]
cards: []
explainers: []
promote_when: [has.destinations]
photo_slots: []
figures: []
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: { date: "2026-11-16", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "State-specific Extension citations replaced; calendar row timings aligned with 05-01 (UMN); unsourced 'double the seed' figure made qualitative" }
---

# Garden calendar for each destination

**What this page is for.** A destination can sit in a different climate from home, and then the
home calendar (→ 05-01) is wrong there. This page sets out each destination's season next to
home's, what changes, and what to do before you ever need it. The crop rankings and methods on
→ 05-01 still apply everywhere.

## Do this now

1. **Compare each destination's season with home's** (table below). A difference of more than a
   few weeks changes what you plant and when.
2. **Get the destination state's Extension planting chart, print it, and keep it with the
   destination's papers** (→ 19-01). It is the local authority.
3. **Place a duplicate seed stock at each agreed destination** (→ 05-03), sealed with
   desiccant, with the owner's permission. Seed already there is a garden that starts the day
   you arrive.
4. **Buy varieties suited to each destination's band** and store them with that cache.
5. **Get a soil test at the destination** on an ordinary visit (→ 05-11).

## Why / how it works

### Home and each destination, side by side

| Place | Zone | Last spring frost | First fall frost | Frost-free days | Precipitation | January low | July high |
|---|---|---|---|---|---|---|---|
| **Home** ({{ region.home.county }}, {{ region.home.state_name }}) | {{ region.home.zone }} | {{ region.home.last_frost }} | {{ region.home.first_frost }} | {{ region.home.growing_days }} | {{ region.home.precip_in }} in | {{ region.home.jan_low_f }} °F | {{ region.home.jul_high_f }} °F |
{{#each destinations as x}}| **{{x.name}}** ({{x.county}}, {{x.state_name}}) | {{x.region.zone}} | {{x.region.last_frost}} | {{x.region.first_frost}} | {{x.region.growing_days}} | {{x.region.precip_in}} in | {{x.region.jan_low_f}} °F | {{x.region.jul_high_f}} °F |
{{else}}| **No destinations entered** | | | | | | | |
{{/each}}

Find each destination's zone in the bands on → 05-01. A longer season usually means a **second
full planting** (a fall garden), earlier potatoes, and crops that do not ripen at home. A wetter
place swaps drought for **fungal disease and waterlogged ground**. A colder or higher place
shortens everything and makes season extension (→ 05-02) essential.

### Each destination's calendar

Fill this in from the destination state's Extension chart on an ordinary visit, then trust a soil
thermometer over the calendar. The anchor dates are printed for you.

{{#each destinations as x}}
#### {{x.name}} ({{x.status_text}})

Zone **{{x.region.zone}}**. Median last spring frost **{{x.region.last_frost}}**; median first
fall frost **{{x.region.first_frost}}**; about **{{x.region.growing_days}} frost-free days**;
about **{{x.region.precip_in}} inches** of precipitation a year.

| When | What to plant there |
|---|---|
| 5 to 15 weeks before transplanting (→ 05-01) | Start onions, cabbage family, peppers, tomatoes indoors: ______________________ |
| Before {{x.region.last_frost}}, soil 40 to 50 °F | Cool-season crops outside (potatoes, peas, onions, greens, roots): ______________________ |
| After {{x.region.last_frost}}, nights warm | Warm-season crops (beans, corn, squash, tomatoes, peppers; sweet potatoes in long seasons): ______________________ |
| Midsummer | Second warm-season planting, if the season allows: ______________________ |
| Late summer, counting back from {{x.region.first_frost}} | **The fall garden:** cabbage family, greens, roots, fall potatoes in long seasons: ______________________ |
| Around {{x.region.first_frost}} | Garlic; hardy greens under row cover to overwinter (→ 05-02): ______________________ |
| Winter | Harvest stored roots and covered greens: ______________________ |

Verified against the Extension chart on (date): __________ by: __________

Seed cache placed there? ____ (date: ______) Where exactly: ______________________
Soil test done? ____ pH: ______ Lime or other amendment needed: ______________________

{{else}}
No destinations are entered. Add them in settings, or plan from the home calendar (→ 05-01,
→ 25-01).
{{/each}}

### What usually changes in a longer, warmer season

- **Plantings per year:** two full gardens, spring and fall, instead of one. Potatoes twice: an
  early spring planting dug before summer heat, a midsummer planting dug in fall. The
  destination state's Extension chart gives the dates.
- **The fall planting is often the better one:** fewer insects, milder finish, greens sweetened
  by light frost.
- **Overwintering:** spinach, kale, collards and garlic planted in fall feed you through a mild
  winter under cover.
- **Variety choice:** the short-season problem becomes a **heat and disease** problem. Choose
  heat-setting, disease-resistant tomatoes; early northern types stop setting fruit in a hot
  summer.
- **Crops worth adding:** sweet potatoes (a top survival calorie crop where the season allows),
  okra, southern peas (cowpeas).
- **Plan seed for two plantings**, not one: more of the succession crops in that cache.

### What usually changes in a wetter climate

- **Watering mostly disappears** as a chore; watering new transplants and trees still matters.
- **Fungal disease replaces drought as the main plant killer:** blights, mildews and rots thrive
  in humidity. The answers: **wide spacing, morning sun, water the soil not the leaves, mulch to
  stop soil splashing onto leaves, resistant varieties, and prompt removal of diseased leaves**
  (→ 05-12's no-chemical ladder).
- **Raised beds** on wet clay ground: waterlogged roots rot.
- **Soil is often acidic** in wet, wooded regions: test before adding lime or wood ash; over-liming
  locks up nutrients as surely as acid does (→ 05-11).

### What usually changes in a shorter, colder season

- One planting, short-season varieties, transplants started indoors (→ 05-14).
- Season extension at both ends (→ 05-02) and storage crops that keep through winter.
- Perennials rated for that destination's zone or colder (→ 05-13).

### Fruit at a destination

If a destination is agreed and the owner welcomes it, **plant fruit trees there now**: a tree
planted this year bears before you might need it. Choose for that destination's zone (→ 05-13).
If anyone in the household is allergic to tree nuts, plant fruit, not nut trees.

## Gear / items

| Item | Why | Notes |
|---|---|---|
| **Duplicate seed cache at each agreed destination** | The garden starts on arrival | Sealed, with desiccant (→ 05-03) |
| Varieties suited to that destination's band | The home list may be wrong there | Open-pollinated where possible |
| **The destination state's printed Extension chart** | The local calendar | → 19-01 |
| Raised-bed materials or a plan | Drainage on wet ground | Untreated wood for food beds |
| Row cover | Frost edges and overwintering | Same stock as → 05-02 |
| Soil test | Know the starting point | First visit |

**Scavenge or substitute:** the host's existing tools, hoses and outbuildings: inventory before
buying duplicates. Leaves and wood chips on wooded land are endless mulch and compost carbon.

## When it runs out

- **Runway:** a garden is a seasonal flow wherever it is. A longer season shortens the gap stored
  food must bridge; a shorter one lengthens it.
- **Resupply:** seed saving (→ 05-03) often works better in a longer season, where biennials and
  late crops ripen seed reliably.

## Phase notes

- **A (at home):** buy the destination-band seed, place the caches, and verify frost dates and
  soil while travel is easy.
- **B (moving):** with caches in place, you carry nothing extra for the garden.
- **C (at a destination):** run that destination's calendar, not home's. First season: beds near
  the house, potatoes and beans first, and a fall garden the same year if the season allows.

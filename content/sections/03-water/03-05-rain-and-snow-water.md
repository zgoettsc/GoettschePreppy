---
id: 03-05-rain-and-snow-water
section: 03-water
title: "Rain catchment and melting snow and ice"
version: 2
revised: 2026-11-16
layer: core
danger_level: caution
phase: [A, B, C]
tags: [water, rain, rain barrel, catchment, snow, ice, cistern, first flush]
derived_from: [03-05-rain-and-snow-water]
sources: [cdc-collecting-rainwater-and-your-health-an-overview-05b0d7, cdc-cistern-safety-and-disasters-before-during-and-a-a1228c, cdc-how-to-make-water-safe-in-an-emergency-5d78b5]
related: [03-02-storing-water, 03-03-pool-water-desalination, 03-04-purifying-water, 03-06-winter-water, 03-08-keeping-water-from-going-bad, 03-10-well-water-without-power, 06-04-wood-supply-and-depletion, 16-12-grid-down-house-repairs, 17-07-drought-and-water-scarcity, 22-04-household-inventory, 23-02-master-consumables-table, 01-05-choosing-a-destination]
cards: []
explainers: [EX-06]
promote_when: []
photo_slots:
  - { id: rain-barrel-setup, caption: "Our rain barrel: where it stands, the downspout or funnel, the screen, the WATER ONLY pump" }
figures: [fig-first-flush-diverter]
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: { date: "2026-11-16", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "CDC mosquito rule corrected to screen or empty every 10 days; roof yield uses dwelling.roof_area_sqft and derived.rain_gal_per_inch (0.623); unsourced snow ratio removed." }
---

# Rain catchment and melting snow and ice

**What this page is for.** Rain and snow are the cheapest water you can get in fuel terms:
they need disinfecting, not distilling. This page covers catching rain, melting snow and
ice, and keeping both safe.

> **CAUTION.** Rain is clean when it leaves the sky and dirty by the time it leaves your roof:
> bird droppings, grit, roofing residue and whatever blew onto it. **Treat harvested rain
> before drinking it** (CDC, Collecting Rainwater and Your Health). Snow is the same, plus
> whatever it landed on.

## Do this now

1. **Put barrels or any clean containers under downspouts.** A modest rain fills them.
2. **Always treat before drinking:** filter out the grit, then boil or disinfect (→ 03-04).
   Rain needs **disinfecting only**, not distilling.
3. **Skip the first flush.** The first rain off the roof in a storm carries the most dirt,
   germs and chemicals (CDC). Send it away from the barrel and collect what comes after.
4. **Melt snow with a little water already in the pot.** Never eat snow to stay hydrated: it
   costs body heat you cannot spare (→ 03-06).
5. **Screen where the water comes into every barrel, or empty the barrel at least every 10
   days.** That is the CDC's rule for stopping mosquitoes breeding in it (CDC, Collecting
   Rainwater and Your Health; → 03-08).

## Setting up a barrel

- **Stand it on level, solid ground or a sturdy platform.** A full 55-gallon barrel holds
  about **460 lb of water** (55 gal x 8.34 lb). On a slope or soft ground it can tip over or
  split; a falling barrel can crush a child.
- **Lid and screen on**, against mosquitoes and debris (→ 03-08).
- **Draw from a spigot or a pump**, never by dipping.
- **A pump or hose used for drinking water is "WATER ONLY" for ever.** Anything that has
  touched fuel, diesel exhaust fluid or chemicals never touches drinking water again. Mark the
  pump "WATER ONLY" in marker and keep it in a separate bag from any fuel pump. Before first
  use, rinse barrel and pump with the container-cleaning solution on → 03-02 (1 teaspoon
  bleach per quart of water, 30 seconds), then with clean water.
- **No roof? Make a funnel.** A tarp strung as a funnel, or an upside-down ceiling-leak
  diverter hung from posts or a line with a hose to the barrel, collects rain without the
  roof's grit. (If your roof is leaking, that job comes first: → 16-12.)
- **Freeze rule: drain the barrel and bring it in before a hard freeze.** Water expands as it
  freezes and splits barrels and pumps. In winter, snowmelt replaces it.

Write where your barrel, pump and treatment supplies are kept: __________ (→ 22-04).

{{photo rain-barrel-setup}}

## How much water a roof gives

**One inch of rain on 1,000 square feet of roof is about 623 gallons** (arithmetic: one inch
of water over one square foot is 144 cubic inches, which is 0.623 gallon). Some of it is lost
to the first flush, splash and overflow; measure what your barrels actually catch in one
storm and compare.

The roof footprint (length x width of the house from outside, not the sloped surface):
{{ dwelling.roof_area_sqft }} sq ft. Then:

- **Gallons per inch of rain, before losses** = roof square feet x 0.623 =
  {{ derived.rain_gal_per_inch }}
- Your area gets about **{{ region.home.precip_in }} inches of rain a year** and
  **{{ region.home.snow_in }} inches of snow**.

Even one downspout on a modest roof section fills a 55-gallon barrel in an ordinary rain. For
most houses, **storage barrels and treatment are the limit, not the rain.**

> **Before the collapse:** a few states limit how much rainwater a household may collect or
> how it may be used. Your state's water-rights agency can tell you. This never decides
> whether you collect water to survive.

## What is actually in it

The CDC says rain picks up germs and chemicals from the air, the roof, gutters, pipes and
storage: bird droppings, dust, smoke, and metals such as lead or copper from roofing
materials. Dirt and germs wash off the roof most after several dry days. The CDC prefers tap or
bottled water to rainwater for drinking, cooking and brushing teeth. When rain is what you
have, treat everything anyone drinks.

**Never mix rainwater into treated water.** The CDC warns that adding rain to treated water
(bottled or tap) can contaminate it. Keep "TREATED" and "RAW" containers strictly apart, and
never connect a catchment line to house plumbing.

**Roofing matters.** Asphalt shingles shed grit and some chemicals; metal roofs are the
cleanest common surface. Do not collect from anything with lead flashing, treated wood or moss
killer. If the roof is doubtful, use the water for flushing, washing and the garden, and drink
from a cleaner source.

**Treatment chain:** screen out leaves at the gutter → let it settle in the barrel → draw from
a spigot above the sediment → **filter** → **boil or disinfect** (→ 03-04) → store clean
(→ 03-02).

{{figure fig-first-flush-diverter}}

## Snow and ice

- **Melt, don't eat.** Eating snow lowers your core temperature and costs more energy than it
  gives back. Melt it and drink it warm.
- **Prime the pot.** Put an inch of water in the pot first, then add snow a little at a time.
  Snow packed into a dry hot pot scorches and can ruin the pot.
- **Volume is disappointing.** Fresh fluffy snow is mostly air: a full pot melts down to a
  small puddle. Wet, dense snow and ice give far more.
- **Ice beats snow** for yield and fuel. Take icicles or hard-packed snow over powder.
- **Take clean snow.** Not near roads (salt, exhaust), not near the driveway, not discolored,
  not where pets or wildlife have been. The middle of an untouched yard, or a clean tarp, is
  best.
- **Still treat it.** Snow is not sterile. Clean fresh snowmelt is usually low-risk and has
  little sediment, but it gets the same treatment as rain.

{{#if is.snow_region}}**Where you live, snow is a real reserve.** A snowbank is a large store
of water sitting in the yard for months. In deep winter, snowmelt often beats every other
source on effort, but it costs **fuel**, so it competes with cooking and heat (→ 06-04).{{/if}}

## Gear and supplies

| Item | Why | Notes |
|---|---|---|
| Rain barrels, food-grade, with spigot (two or more) | The catchment | Link in a row; raise them for gravity flow |
| Drum pump or siphon, marked WATER ONLY | Empties the barrel into jugs without dipping | Never used for fuel |
| Downspout diverter and first-flush device | Skips the dirtiest runoff | Can be built from pipe |
| Fine screen, gutter guards, barrel screens | Blocks leaves and mosquitoes | Mosquito control is not optional (→ 03-08) |
| Clean tarp and cord | Catch rain or clean snow away from the roof | The cleanest catchment surface you can own |
| Large melting pot | Snow to water in volume | A dark pot melts faster in sun |
| Filter and treatment supplies | Rain and snow both need them | → 03-04 |
| Food-grade containers | Move it to storage | → 03-02 |

**If you don't have it:**

- **Any clean container under a downspout:** trash cans, storage totes, buckets. Volume beats
  neatness.
- A **tarp strung as a funnel** into a barrel.
- Kiddie pools, coolers and totes all hold water; cover them against mosquitoes and debris.
- A **sled** is the best tool for hauling snow to the pot.

## When it runs out

- **Runway:** rain and snow are seasonal and you cannot schedule them. Collect hard whenever
  they come, not when you need them.
- **Ration:** use rain and snowmelt for drinking and cooking *first*, because they are cheap
  in fuel.{{#if has.pool}} Save the pool for washing and flushing.{{/if}}
- **Resupply:**{{#if has.pool}} the pool (→ 03-03) is the constant backstop: huge volume,
  high fuel cost. Rain is the opposite: free but irregular. Run both.{{else}} keep stored water
  (→ 03-02) for dry spells and look for other sources (→ 17-07).{{/if}}
- **The fuel trade:** melting snow and boiling rain both burn fuel. In a hard winter, water and
  heat compete for the same woodpile. Put both in the consumables table (→ 23-02).

## Phase notes

- **A (sheltering at home):** barrels on downspouts and snow from the yard are quiet water
  sources that nobody sees you collect, unlike hauling from a public source.
- **B (moving):** a tarp and a pot make rain and snow your water anywhere. This is the most
  portable water skill in the binder.
- **C (rural or at a destination):** scale it up: a cistern, more roof, more barrels. Clean
  and disinfect a new or unused cistern before trusting it (CDC, Cistern Safety and
  Disasters). Where a destination is on town or district water with no well, pressure dies
  with the grid, and **roof catchment becomes the water plan**, not a supplement: fill every
  container on arrival (→ 03-01), then live on the roof. Do the roof sum for each place you
  might go, and send barrels ahead if you can.
{{#if has.destinations}}
{{#each destinations as d}}  - **{{ d.name }}** gets about {{ d.region.precip_in }} inches of rain a year. Roof size: ______ sq ft; gallons per inch: ______; barrels there: ______
{{/each}}
{{/if}}

## Cross-references

→ 03-02 storing water · → 03-04 purifying water · → 03-06 winter water ·
→ 03-08 mosquitoes in barrels · → 06-04 fuel for melting · → 17-07 drought ·
→ 03-10 well water · → 01-05 destination water

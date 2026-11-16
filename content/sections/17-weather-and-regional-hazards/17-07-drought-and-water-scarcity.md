---
id: 17-07-drought-and-water-scarcity
section: 17-weather-and-regional-hazards
title: "Drought and water scarcity"
version: 1
revised: 2026-11-16
layer: region
danger_level: caution
phase: [A, B, C]
tags: [drought, water, rationing, greywater, rain barrels, well, garden, mulch, pool, fire risk]
derived_from: [17-07-drought-and-water-scarcity]
sources:
  - cdc-how-to-create-and-store-an-emergency-water-suppl-f0c412
  - cdc-private-drinking-water-and-public-health-dc08f9
  - noaa-national-weather-service-heat-safety-66fd15
  - noaa-national-weather-service-wildfire-safety-b17a66
related: [03-01-daily-water-needs, 03-02-storing-water, 03-03-pool-water-desalination, 03-04-purifying-water, 03-05-rain-and-snow-water, 03-06-winter-water, 03-08-keeping-water-from-going-bad, 03-10-well-water-without-power, 05-10-container-and-vertical, 05-11-soil-and-compost, 05-13-perennials-and-fruit, 13-02-hygiene-and-handwashing, 13-03-greywater-and-trash, 13-04-laundry-by-hand, 13-11-disease-outbreak, 17-04-extreme-cold-and-heat, 17-05-grassland-fire, 17-14-wildfire-smoke-and-evacuation, 01-02-go-no-go-decision, 01-05-choosing-a-destination, 23-02-master-consumables-table, 30-14-dc13-drinking-pool-or-surface-water]
cards: [DC-13]
explainers: [EX-06]
promote_when: [is.drought_region]
photo_slots: []
figures: [fig-water-cascade]
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: null
---

# Drought and water scarcity

**What this page is for.** Drought is the slow hazard. It arrives over a season, and by the time it
is obvious the choices are fewer. Three things fail together: **the water supply** (wells drop,
creeks shrink, rain barrels stay empty), **the garden**, and **fire safety**, because everything
dries out (→ 17-05). This page is about doing the water math honestly, cutting use in a planned
order, and knowing when storage is no longer enough.
{{#if is.drought_region}}**Your home county is rated 2 or 3 for drought in the region data.**{{/if}}
Your area gets about **{{ region.home.precip_in }} inches** of rain and melted snow in a normal
year.

> **CAUTION.** **Never cut drinking water, cooking water or hand washing.** An illness outbreak
> costs far more water than hand washing ever saves (→ 13-11). In heat, people need more water,
> not less (→ 17-04).

## Do this now

1. **Do the water math for a hot, dry month, not an average one** (→ 03-01). Your household's
   minimum is about **{{ derived.water.floor_gal_day }} gallons a day** for drinking and basic
   hygiene; the planning figure is **{{ derived.water.plan_gal_day }} gallons a day**. Laundry,
   dishes, bathing and the garden come on top.
2. **Put a barrel on every downspout you can** (→ 03-05).
3. **Set up the greywater cascade** (→ 13-03) so each gallon does two or three jobs. It is the
   biggest saving available.
4. **Mulch the garden deeply.** It is the cheapest water saving there is (→ 05-11).
5. **Write the cutting order below on → 23-02** so it is decided before anyone is thirsty.

> **Before the collapse:** some states limit rainwater collection or set rules for water rights,
> wells and diverting streams. Check your state's rules before building a large system while that
> system still works.

## What drought does to each source

| Source | In a drought |
|---|---|
| **Town water** | Restrictions first, then possibly rationing. Usually the last to fail |
| **Rain barrels** (→ 03-05) | **Empty exactly when you need them** |
| **Wells** | The water table drops; yield falls; shallow wells can go dry. Deeper wells hold up better (CDC, Private Drinking Water) |
| **Creeks, ponds, sloughs** | Shrink, then stop. What is left is warm, concentrated and dirtier (→ 03-04) |
| **Rivers** | Low, warm and poorer in quality; treatable with work |
| **Snowpack** | A dry winter means a dry spring. **Drought often starts the winter before** |
{{#if has.pool}}| **Your pool or hot tub** (about {{ dwelling.pool_gallons }} gallons) | The largest single reserve on the property, but not drought-proof: uncovered, it loses water to evaporation every hot, windy day, and with no pump or chlorine it turns green. **Keep it covered** (→ 03-03) |
{{/if}}{{#if has.well}}| **Your well** | Note its depth and normal yield now: ______ ft, ______ gal/min. Watch for sputtering, air or sediment as the level drops (→ 03-10) |
{{/if}}

## Storage math

**In a drought, storage is the buffer.**
- **Stored drinking water:** {{ gear.water.stored_gal }} gallons, which lasts about
  **{{ derived.water.stored_days }} days** at the floor rate.
- **Two weeks at the planning rate** is about {{ derived.water.two_weeks_gal }} gallons (CDC, Emergency
  Water Supply; → 03-01).
- Add hygiene (→ 13-02), dishes, laundry (→ 13-04), toilet flushing (→ 13-01) and the garden, and the
  real household figure is several times the drinking figure. Most households find their runway
  is days, not weeks. Write it on → 23-02 and recompute weekly in a dry spell.

## The cutting order: decide it in advance

When water is short, cut in this order:
1. **Garden watering.** Painful, and the right first cut. Mulch, shade and save the most valuable
   beds; let the rest go.
2. **Laundry.** Wash less, air more (→ 13-04).
3. **Bathing.** Basin washes instead of full baths.
4. **Dishes.** One-pot meals, scrape well, wash once (→ 13-10).
5. **Flushing.** Greywater only (→ 13-03), or a bucket toilet (→ 13-01).
6. **Never cut: drinking, cooking and hand washing.** Hand washing is the last thing to go.

## Savings that actually move the number

- **Cascade every gallon** (→ 13-03): rinse water becomes wash water becomes flush water or water
  for non-food plants.
- **Deep mulch** cuts evaporation from the soil (→ 05-11).
- **Water the soil, not the leaves**, early in the morning or in the evening.
- **Drip or soaker lines** instead of sprinklers.
- **Shade cloth** over the garden in extreme heat cuts water need.
- **Containers dry fastest:** group them, shade them, mulch them (→ 05-10).
- **Fix every leak.** A dripping tap is a real loss over a month.
- **Cover stored water** against evaporation and dirt (→ 03-02).
- **Grow what survives.** Deep-rooted, drought-tolerant crops and established perennials
  (→ 05-13); give up the thirsty ones.

{{figure fig-water-cascade}}

## Drought and fire are the same event

Dry fuel everywhere, low humidity, and **firefighting water is scarce exactly when fire risk is
highest** (→ 17-05). Cooking fires, ash, generator exhaust and saws all become more dangerous. Read
burn conditions off the sky and the radio. Long droughts also bring smoke from distant fires
(→ 17-14).

## Food

- **A drought year is a poor harvest year.** If the garden is part of the food plan, the stored
  food is the drought plan (→ 04-01).
- **Established plants survive; new plantings do not.** Water what is already invested.
- **Wild food fails too**: fewer berries, nuts and game.

## The multi-year drought

- **Storage buys a season, not a drought.** For years of drought you need a **source**, not a
  buffer.
- **A reliable water source is the first test of any long-term site** (→ 01-05): a deep well, a
  spring or dependable surface water outranks almost everything else.
- **A town lot with barrels and stored water has a fixed, finite reserve.** Long-term water is a
  question of where you live (→ 01-02).
- **People downstream share the water.** Expect disputes and plan to be a good neighbour
  (→ 18-01).

## Gear

| Item | Why | Notes |
|---|---|---|
| **As much stored water as you can keep** | Storage is the buffer | → 03-02 |
| Rain barrels on every downspout | Free when it rains | → 03-05 |
| Water treatment and spare filters | Shrinking sources are dirtier | → 03-04 |
| **Mulch, lots of it** | The cheapest saving in the garden | Straw, leaves, chips |
| Drip or soaker hose | Targeted watering | |
| Shade cloth | Cuts water need | |
| Greywater basins and buckets | The cascade | → 13-03 |
| Covered containers | Evaporation and dirt | |
| Rain gauge and a water-use log | You cannot manage what you do not measure | → 25-05 |
| Drought-tolerant seed | Grow what survives | |
{{#if has.pool}}| Pool cover; pump and hose | Slows evaporation; makes the pool usable for washing, garden and fire water | A cover is a drowning hazard for small children: → 20-02 |{{/if}}

**If you do not have it:** tarps funnelled into barrels catch a surprising amount from a modest
rain; the bathtub is storage (fill it at the first sign of restrictions); leaves, grass clippings,
cardboard and straw are free mulch; snow in winter is free water (→ 03-06). **What you cannot
substitute is a source.**

**Pool and surface water for drinking:** pool water and untreated surface water need treatment, and
salt-water pools need distilling, which costs fuel (→ 03-03). Drinking them is a trade-off with a
decision card: {{choice DC-13}} → 30-14

## When it runs out

- **This whole page is about running out.** Compute the runway at the rationed rate and recompute
  weekly.
- **Substitute in order:** rain (→ 03-05), then stored (→ 03-02), then pool or other non-drinking
  reserves treated or distilled (→ 03-03), then surface water treated (→ 03-04), then hauling from
  a distant source. Each step costs more fuel, work or risk.
- **The trigger to move:** when the runway at rationed use drops below the time it would take to
  relocate, that is a go/no-go decision (→ 01-02). Water has no substitute and cannot be made
  locally.

## Phase notes

- **A (at home):** town water usually holds longest. **While it works, fill every container you
  own.** Expect restrictions before failure.
- **B (moving):** in summer, water is the limit on travel: heavy, used fast in heat, and sources on
  the route may be dry or fouled. Plan the route around water and carry more than feels necessary
  (→ 01-03).
- **C (rural or new site):** water is the site. Plan for well yield to drop in drought, build
  storage, and place the garden and animals around the water, not the other way round.

---
id: 22-07-priority-purchase-order
section: 22-master-lists-acquire-and-scavenge
title: "What to buy first: the spending order"
version: 2
revised: 2026-11-16
layer: household
danger_level: none
phase: [A]
tags: [buying, priorities, budget, tiers, spending order]
derived_from: [22-07-priority-purchase-order]
sources:
  - cdc-how-to-create-and-store-an-emergency-water-suppl-f0c412
  - us-epa-emergency-disinfection-of-drinking-water-6aa91f
  - american-red-cross-power-outage-safety-6d07a8
  - cdc-carbon-monoxide-poisoning-basics-772153
  - us-fda-information-regarding-insulin-storage-and-swi-6448d3
  - ready-gov-build-a-kit
related: [22-01-master-acquisition-list, 22-04-household-inventory, 22-02-scavenging-field-guide, 23-04-resource-lifecycles, 23-05-skills-that-replace-supplies, 26-09-shopping-list-and-budget, 01-05-choosing-a-destination, 25-10-annual-review, 12-07-meds-stockpile]
cards: []
explainers: [EX-03]
promote_when: []
photo_slots: []
figures: []
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: { date: "2026-11-16", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "Unsupported 'near-certain over a decade' power-cut claim reworded to what Red Cross says." }
---

# What to buy first: the spending order

**What this page is for.** → 22-01 is what to buy; this page is the order. The rule is not about
comfort: **buy against what hurts people soonest, then against what cannot be bought later.**
Tier 0 and Tier 1 below are cheap and cover most realistic risk. Rows that your settings make
urgent for this household are marked **(this household)**.

## Do this now

1. **Do Tier 0 this week.** It is cheap and small, and several of its items prevent deaths in
   the next month, not the next decade.
2. **Do not skip ahead to solar panels and rifles.** Both are on this list; neither is near the
   top, and buying them first is the most common preparedness mistake.
3. **Fill in the → 22-04 inventory first** if you have not: you may already own half of what you
   are about to buy.
4. **Set a monthly amount you can actually sustain** and work down the tiers. Steady beats a
   spree, because the ⌛ items (seed, wood, soil, skill) need years, not money.

## The ordering rule

Rank every purchase by three questions, in this order:

1. **How fast does its absence hurt someone here?** Minutes, hours, days, weeks, months.
2. **Can it still be bought later?** ⌛ items (seed, seasoned wood, soil, skill, children's next
   sizes) **cannot**. They move up.
3. **How likely is the event it covers?** A power cut lasting days is common enough
   that the American Red Cross tells every household to plan two weeks of food and water for
   one (American Red Cross, Power Outage Safety); a years-long collapse is not. **Buy against the
   likely first**, then the severe.

**For most households that produces:** carbon monoxide → medical dependency →
{{#if is.cold_winters}}cold{{else}}{{#if is.hot_summers}}heat{{else}}cold or heat{{/if}}{{/if}} → water →
injury and infection → food → everything else. **Food is sixth**, and it is where most people
start.

## Tier 0: this week (small money, largest risk reduction)

| # | Item | Why it is first | Page |
|---|---|---|---|
| 1 | **Battery CO alarms**, one on every level and outside every sleeping area, plus batteries. You have {{ gear.co_alarms }} | Bringing any burning heat source indoors in an outage is how households die; detecting it is cheap (CDC, Carbon Monoxide Poisoning: Basics; → 29-03){{#if has.unvented_heater}}. **(this household): you own an unvented heater**{{/if}}{{#if has.generator}}. **(this household): you own a generator**{{/if}} | → 08-02 |
| 2 | **The fullest legitimate supply of every daily and rescue medicine**: start the conversation with each prescriber now{{#if has.refrigerated_meds}} **(this household: refrigerated medicine)**{{/if}} | Nothing else you buy changes this clock | → 12-07, → 22-06 |
{{#if has.epinephrine}}| 3 | **Epinephrine pairs for every location** the allergic person spends time **(this household)** | Minutes matter and there is no substitute | → 02-03 |
{{/if}}| 3a | **Trauma and family first-aid core**: tourniquets, wound-packing gauze, pressure bandages, oral rehydration salts, adult and child fever medicine with dosing tools, a CPR face shield | A bleed, a dehydrated child or a fever with no emergency room is the realistic medical emergency. Count what you have first (→ 22-04) | → 12-01, → 12-02, → 12-05, → 12-13 |
| 4 | **Water: bleach + a filter + containers** toward {{ derived.water.two_weeks_gal }} gallons | Days, not weeks (CDC, How to Create and Store an Emergency Water Supply) | → 03-02, → 03-04 |
| 5 | **A headlamp per person** ({{ household.size }}) + batteries | Everything else is harder in the dark | → 10-01 |
| 5a | **Smoke alarms and an ABC fire extinguisher** on every level. You have {{ gear.smoke_alarms }} smoke alarms and {{ gear.extinguishers }} extinguishers | Fire with no fire department | → 29-12 |
| 5b | **Labels on every fuel can** | One wrong pour puts gasoline in a heater (→ 29-01) | → 06-06 |
{{#if has.refrigerated_meds}}| 5c | **A thermometer for the medicine fridge or cooler** **(this household)** | The storage range is unverifiable without one (→ 29-07) | → 22-06 |
{{/if}}{{#if has.child}}| 5d | **A lockable box for medicines** **(this household: children)** | **Children do not have access to firearms, fuel, medications or chlorine products.** | → 20-02 |
{{/if}}

## Tier 1: this month

| # | Item | Why | Page |
|---|---|---|---|
| 6 | **Base layers, insulated boots, hats and mittens for everyone**{{#if has.child}}, children included{{/if}} | {{#if is.cold_winters}}Cold is a local killer here (January mean low {{ region.home.jan_low_f }} °F){{else}}Cold snaps and wet weather still kill{{/if}}; children's sizes ⌛ expire | → 11-01, → 11-02 |
| 7 | **Trauma kit (row 3a) + a Stop the Bleed class** | The class is what makes the tourniquet work | → 12-02 |
| 8 | **Two weeks of shelf-stable food you actually eat**{{#if has.anaphylaxis}}, **including allergen-safe food (this household)**{{/if}} | Cheap, useful at once, rotates naturally | → 04-02 |
| 9 | **NOAA Weather Radio** (battery or crank, SAME){{#if has.noaa_radio}}: owned{{/if}} | The best early warning there is | → 15-01 |
| 10 | **A vehicle kit for each vehicle**{{#if is.cold_winters}}, winter add-on included{{/if}} | Blankets, shovel, traction, children's gear in current sizes | → 22-05 |
| 11 | **Ignition three ways + a way to cook without the grid** | Boiling water is the base skill | → 06-01, → 07-01 |
| 12 | **Document kit + cash in small bills** | Costs almost nothing; cannot be replaced if lost | → 19-01, → 19-02 |
| 13 | **Bucket toilet + cover material** | Sanitation failure causes outbreaks fast (→ 13-11) | → 13-01 |
| 14 | **Power for medical devices**: power banks or a station sized to them{{#if has.cpap}} **(this household: CPAP)**{{/if}}{{#if has.oxygen}} **(this household: oxygen)**{{/if}} | Devices through a multi-day outage | → 09-10 |
| 14a | **A CO detector with a number (ppm) display** on each level | Catches a slow leak before the alarm threshold | → 08-02 |
| 14b | **Fuel-transport hardware**: approved cans, straps, an exterior rack{{#if has.destinations}} **(this household: you have destinations)**{{/if}} | Fuel that cannot ride safely is range you do not have | → 06-08 |
| 14c | **Spares for any heater you own**: wicks, filters, hoses{{#if has.unvented_heater}} **(this household)**{{/if}} | A heater you cannot fix mid-winter is not a heater | → 08-09, → 08-10 |
{{#if has.trailer}}| 14d | **Trailer spare wheel + bearing kit + coupler lock** **(this household)** | One bearing or one tyre is the whole move | → 16-11 |
{{/if}}{{#if has.vehicle}}| 14e | **Tyre plug kit + 12 V compressor**, and a real spare if the vehicle has none | A flat you cannot fix is a stranding | → 16-10, → 22-05 |
{{/if}}

## Tier 2: this season (and the ⌛ items: do not defer these)

| # | Item | Why | Page |
|---|---|---|---|
| 15 | **⌛ Open-pollinated seed, in quantity** | Cheap, light, and **unbuyable later** | → 05-03 |
| 16 | **⌛ Firewood, far more than feels sensible, seasoning now**{{#if has.fireplace}} **(this household: fireplace)**{{/if}}{{#if has.wood_stove}} **(this household: wood stove)**{{/if}} | Wood bought today is next winter's fuel | → 06-03, → 06-04 |
| 17 | **⌛ A compost pile started; soil begun**{{#if has.garden}} **(this household: garden space)**{{/if}} | Years to build; free to start | → 05-11 |
| 18 | **⌛ The next two sizes of children's clothing and boots**{{#if has.child}} **(this household)**{{/if}} | The expiry nobody plans for | → 11-02, → 11-09 |
| 19 | **A good axe, saw + file, and a good knife** | Best lifetime value of any tool | → 16-01, → 16-06 |
| 20 | **Bulk staples + mylar + oxygen absorbers + buckets** | Turns cheap food into long-keeping food | → 04-03 |
| 21 | **Ammunition for the calibres you already own**, cleaning kit, spare parts{{#if !has.firearms}} (none owned per settings){{/if}} | Feed and maintain what you have; buy nothing new first | → 14-07, → 14-05 |
| 21a | **Locked storage for every firearm**{{#if has.firearms}}{{#if has.child}} **(this household: firearms and children)**{{/if}}{{/if}} | Child-access prevention, in calm times and crisis | → 14-14 |
| 22 | **Home hardening**: locks, door reinforcement, window film, lighting | The cheapest security spend | → 14-02 |
| 23 | **Go-bags built out** | Most of the contents come from Tiers 0 to 2 | → 22-03 |
| 24 | **Sanitation bulk**: soap, bleach, liners, gloves{{#if has.infant}}, diapers and wipes{{/if}} | Boring; runs out fastest | → 13-01 |
| 25 | **First-aid depth**: oral rehydration salts, dental, splints | | → 12-01, → 12-05, → 12-06 |
| 25a | **Chimney brush sized to your flue + suppressant**{{#if has.fireplace}} **(this household)**{{/if}} | Wood heat means creosote on a schedule | → 06-09 |
| 25b | **Chainsaw chaps + eye and ear protection** | A saw injury with no emergency room | → 11-05 |
| 25c | **Large vacuum flasks** | Saves cooking fuel | → 07-02 |
| 25d | **Push-fit pipe couplings + a tube cutter** | A burst pipe becomes a short repair | → 16-12 |
{{#if has.young_child}}| 25e | **Car-seat ponchos or over-harness blankets** **(this household)** | No bulky coat under the harness (→ 11-02) | → 22-05 |
{{/if}}{{#if has.well}}| 25f | **Well bailer + rope** **(this household: well)** | The no-power fallback; cheap, and unbuyable once needed | → 03-10 |
{{/if}}{{#if has.pets}}| 25g | **Pet food, carriers and medicines for two weeks** **(this household)** | | → 20-09 |
{{/if}}

## Tier 3: this year

| # | Item | Why here and not earlier | Page |
|---|---|---|---|
| 26 | **Solar + a battery or power station**: you have {{ gear.solar_w_total }} W and {{ gear.station_wh_total }} Wh | Size it to medical loads and December sun; insulation, layers and a CO alarm come first | → 09-02, → 09-03 |
| 27 | **Pressure canner + jars + lids** | Pays off only with a harvest and the skill (→ 24-01) | → 04-05 |
| 28 | **Rocket or efficient stove, Dutch oven, cast iron** | Cuts wood use sharply | → 07-02, → 07-04 |
| 29 | **Rain barrels + gutters + screens** | Turns weather into a supply (→ 23-04) | → 03-05 |
| 30 | **Water distillation setup**{{#if has.pool}} **(this household: pool or hot tub)**{{/if}} | The only home method that removes salt | → 03-03 |
| 31 | **Garden built out**: beds, tools, row cover, ⌛ fruit trees | | → 05-01, → 05-02, → 05-13 |
| 32 | **Two-way radios + a ham licence** | The licence takes time | → 15-02, → 15-05 |
| 33 | **Chickens or rabbits** (check local rules) | Ongoing protein and fat | → 05-04, → 05-05 |
| 34 | **Bicycles + trailer + spares** | Transport after fuel | → 16-09 |
| 35 | **Generator**{{#if has.generator}} (owned: {{ gear.generator_watts }} W){{/if}}: outdoor-rated cords, oil and filters, a marked outdoor spot, a first start | Useful, loud, thirsty, and **CO-lethal indoors**. **Never run a generator, charcoal, or any engine indoors, in a garage, or near an open window.** | → 09-04 |
| 35a | **Analog barometer** | Hours of warning with no forecast | → 17-10 |
| 35b | **Moisture meter for firewood** | The difference between heat and creosote | → 08-08 |

## Tier 4: the things money cannot shortcut

These outrank most of Tier 3 and cost little or nothing:

- **Skills** (→ 23-05, → 24-01): the only asset that never runs out.
- **Practice** (→ 24-02, → 24-04): a blackout weekend finds more gaps than a large purchase.
- **A destination** (→ 01-05): {{#if has.agreed_destination}}you have an agreed destination. What
  money cannot buy is the remaining work with the people there: agreed terms (→ 18-04) and a tote
  of supplies left there on each visit.{{else}}no destination is agreed yet. A conversation, a
  visit or an agreement is worth more than another year of gear.{{/if}}
- **Neighbours** (→ 18-01): mutual aid is the highest-return preparation there is.
- **A medical supply relationship** (→ 12-07): the only thing that moves the medical clock.

## Budget shapes

An illustrative split, not prices. Replace with real local numbers as you fill → 22-04.

| If you have | Spend it on |
|---|---|
| **$100** | Tier 0 items 1, 4, 5: CO alarms, bleach + containers, headlamps |
| **$500** | Tier 0 complete + food, base layers, NOAA radio |
| **$1,500** | + vehicle kits, trauma kit, bucket toilet, go-bags, bulk staples, seed |
| **$5,000** | + wood, tools, canning setup, rain barrels, home hardening |
| **$15,000+** | + solar and batteries, distillation, garden build-out, livestock, transport |
| **$0** | **Tier 4.** Inventory, practise, teach the children, meet the neighbours, walk the routes |

## The five most common ways to waste money

1. **Buying the tool without the consumable**: a filter with no element, a canner with no lids,
   an optic with no batteries, a saw with no file.
2. **Buying gear for a skill never practised.** An unused pressure canner is furniture.
3. **Buying one of something everyone needs.**
4. **Buying solar before insulation, layers and a CO alarm.** A warm, safe household uses far
   less power.
5. **Putting off the ⌛ items** because they feel unhurried. Seed, wood, soil, children's sizes
   and skill are the only things here money cannot fix later.

## When the shops close

This page becomes read-only.

- **Every ⌛ item becomes unobtainable at that moment.**
- **Tier 0 and Tier 1 are the items you will most regret skipping**: cheapest and most
  consequential.
- **Almost everything in Tiers 2 and 3 has a scavenged or traded equivalent** (→ 22-02).
  **Nothing in Tier 0 does**: CO alarms and medicines are bought, not found.
- After that, → 22-02 (scavenge), → 18-02 (trade) and → 23-05 (skills) are the only ways left
  to acquire anything, and only the last one grows.

## Phase notes

- **A (shelter in place):** work down the tiers on a monthly budget; re-rank at every recount
  (→ 22-04). The worksheet version is → 26-09.
- **B (moving):** nothing here can be bought once you are moving.
- **C (establish):** seed, tools and skill make a place viable (→ 23-04), so buy in Phase A with
  Phase C in mind.

Related: → 22-01 the full list by subject · → 22-04 what you already have · → 22-02 what to
look for later · → 23-04 which purchases last · → 23-05 the free ones · → 26-09 the shopping
worksheet · → 25-10 annual review. A national starting list: Ready.gov, Build A Kit.

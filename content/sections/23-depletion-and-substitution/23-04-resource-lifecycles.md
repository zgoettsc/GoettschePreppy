---
id: 23-04-resource-lifecycles
section: 23-depletion-and-substitution
title: "Lifecycles of every major consumable"
version: 2
revised: 2026-11-16
layer: core
danger_level: caution
phase: [A, B, C]
tags: [lifecycle, depletion, production, stock, substitute, fuel shelf life, seed, soil, soap]
derived_from: [23-04-resource-lifecycles]
sources:
  - university-of-missouri-extension-wood-fuel-for-heati-b63761
  - us-epa-emergency-disinfection-of-drinking-water-6aa91f
  - cdc-how-to-create-and-store-an-emergency-water-suppl-f0c412
  - university-of-minnesota-extension-composting-in-home-01e436
  - us-fda-information-regarding-insulin-storage-and-swi-6448d3
  - ghp-group-inc-dyna-glo-manufacturer-portable-kerosen-477cfd
related: [23-01-depletion-framework, 23-02-master-consumables-table, 23-03-substitution-catalog, 23-05-skills-that-replace-supplies, 06-04-wood-supply-and-depletion, 06-06-fuel-storage-safety, 03-04-purifying-water, 05-03-seed-saving, 05-11-soil-and-compost, 13-09-soap-making, 01-02-go-no-go-decision, 01-05-choosing-a-destination, 22-07-priority-purchase-order, 30-18-dc17-old-fuel, 30-14-dc13-drinking-pool-or-surface-water]
cards: [DC-17, DC-13]
explainers: [EX-01, EX-02, EX-06]
promote_when: []
photo_slots: []
figures: [fig-four-stages-of-a-resource]
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: { date: "2026-11-16", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "No fuel shelf-life figure stated; Dyna-Glo 'one season' line verified in the manual; traps claim softened." }
---

# Lifecycles of every major consumable

**What this page is for.** Every supply in the house moves through the same four stages, from
a pile that only shrinks to something you can make for yourself. This page shows the **shape**
of each problem and where your household stands. It holds no burn rates, doses or mixing
ratios: each row points to the page that has the real numbers, limits and method.

> **Caution.** Do not plan a fuel burn rate, a medicine dose or a chlorine dilution from this
> page. Follow the cross-reference.

## Do this now

1. **Read the four stages once.** They are the same for every supply, and knowing them turns
   "we are running out of X" into a decision.
2. **For each row below, mark the stage you are really at today.** For most things in most
   houses the honest answer is **stage 1: stock only**. That is the finding.
3. **Pick the three rows where stage 2 or 3 is cheapest to reach** and buy or learn toward them
   this year (→ 22-07). For most households: water treatment, fuel or firewood, and garden seed.
4. **Accept the class C rows.** Prescription medicines the body depends on, epinephrine and
   infant formula have **no stage 2, 3 or 4**. They only have stock. That is why the
   leave-or-stay plan exists (→ 01-02).

## The four stages every supply passes through

{{figure fig-four-stages-of-a-resource}}

| Stage | What it means | What it costs you |
|---|---|---|
| **1. Stock** | You have a pile. It only shrinks | Nothing now; it ends on a fixed date |
| **2. Extend** | Ration, recover, reuse, repair. The pile shrinks more slowly | Discipline and work |
| **3. Substitute** | Something else does the job, usually worse (→ 23-03) | Some quality, comfort or safety |
| **4. Produce** | You make or gather it, on and on | Land, tools, skill and a lot of time |

**A supply is only really solved at stage 4.** Stages 2 and 3 buy time to get there. A supply
with **no stage 4** has a deadline, and the deadline sets the plan.

**The most useful question on this page:** for this supply, what does stage 4 actually
need, and do we have it here, on this property, in this {{ home.setting }} setting? Many stage 4
answers need land, wood, water and space that a town lot does not have. If that is true for
you, it is the case for a destination (→ 01-05), stated as an inventory rather than a fear.

Each row below gives: **Stock**, **Runway** (how long the stock alone lasts at normal use),
**Extend**, **Substitute**, **Produce**, **Stage 4 needs**, a **Verdict**, and where the real
numbers are.

## Water

| | |
|---|---|
| **Stock** | Stored containers, the water-heater tank{{#if has.water_heater_tank}} ({{ dwelling.water_heater_gallons }} gal){{/if}}, the pipes{{#if has.pool}}, the pool or hot tub ({{ dwelling.pool_gallons }} gal, not drinkable as it stands){{/if}} |
| **Runway** | Days on stored water (yours: about {{ derived.water.stored_days }} days at the floor, → 23-02) |
| **Extend** | Stop flushing with drinking water; catch every drop; reuse wash water (→ 13-03) |
| **Substitute** | Snow and ice melt (→ 03-06), rain (→ 03-05), surface water as a last resort, treated (→ 03-04). Drinking pool or surface water: {{choice DC-13}} → 30-14 |
| **Produce** | Rain catchment plus a treatment chain you can run indefinitely: filter, then boil or disinfect (EPA, Emergency Disinfection of Drinking Water; → 03-04) |
| **Stage 4 needs** | A roof, gutters, barrels, and either fuel for boiling or a lasting filter with spare elements{{#if has.well}}. Your well also needs a way to draw water without power (→ 03-10){{/if}} |
| **Verdict** | **Reachable almost anywhere it rains or snows.** Water is the supply most households can solve where they are |
| **Where the numbers are** | → 03-01 needs · → 03-04 treatment · → 03-03 pool · → 03-06 winter · → 03-08 keeping it good · → 03-10 a well without power |

## Heat and cooking fuel: wood

| | |
|---|---|
| **Stock** | The woodpile ({{ gear.fuel.firewood_cords }} cords in settings) |
| **Runway** | **Short.** A stack sized for occasional fires disappears fast once it is your only heat and cooking fuel (MU Extension, Wood Fuel for Heating) |
| **Extend** | Burn for work, not looks: contained fire, cook and heat with the same burn, heat one room (→ 08-01), bank the coals, cook in bulk (→ 07-01) |
| **Substitute** | Fallen wood, scrap lumber, pallets, paper logs. **Never burn painted or pressure-treated wood indoors** (→ 06-04) |
| **Produce** | Cut, split and **season** wood. Seasoning takes months, so wood cut today is next winter's fuel, not tonight's |
| **Stage 4 needs** | **Standing timber you have the right to cut**, an axe and saw and the skill to use them (→ 16-06), and a dry stack with a year of lead time |
| **Verdict** | {{#if has.acreage}}**Possibly reachable** if your land carries enough timber. Work it out on → 06-04.{{else}}**Usually not reachable in a town or suburb.** There is rarely a lasting in-town firewood supply. For many households this is the strongest depletion argument for a rural destination (→ 01-05).{{/if}} |
| **Where the numbers are** | → 06-01 fire · → 06-04 wood supply · → 07-01 cooking fire · → 16-06 axes and saws · → 08-08 wood heat |

## Liquid fuels and propane

| | |
|---|---|
| **Stock** | Gasoline {{ gear.fuel.gasoline_gal }} gal, diesel {{ gear.fuel.diesel_gal }} gal, kerosene {{ gear.fuel.kerosene_gal }} gal, propane {{ gear.fuel.propane_20lb }} × 20-lb and {{ gear.fuel.propane_1lb }} × 1-lb (from settings) |
| **Runway** | Hours of running time per gallon or cylinder, from each appliance's label or manual. **And a shelf life** (below) |
| **Extend** | Run engines and heaters only for a purpose, at the setting the manual gives; share one burn for several jobs |
| **Substitute** | Wood, solar, doing without (→ 23-03). Never a different fuel in an appliance not built for it |
| **Produce** | **Not possible at household scale** |
| **Stage 4 needs** | A working fuel supply chain |
| **Verdict** | **Stock only, and some of it ages.** See below |
| **Where the numbers are** | → 06-06 storage · → 09-04 generators · → 08-10, → 08-09 heaters · → 29-01 what each fuel is |

**How long stored fuel lasts.** There is no federal or manufacturer shelf-life number for
stored gasoline, kerosene or diesel that you can plan on. What can be said:
- **Untreated gasoline keeps for months, not years.** It loses the parts that help an engine
  start, can take up water, and leaves gum in small engines. Stabiliser added when it is fresh
  slows this.
- **Kerosene and diesel** age more slowly but take up water and grow sludge in part-full cans.
  One common wick-heater maker says never use kerosene stored from one season to the next
  (GHP Group/Dyna-Glo, kerosene heater owner's manual).
- **Propane does not go stale.**

Whether your household burns old fuel, and how old, is a decision card: {{choice DC-17}}
→ 30-18. Date every can when you fill it (→ 26-08).

## Food

| | |
|---|---|
| **Stock** | The pantry, plus the freezer (which is on a clock the moment the power goes) |
| **Runway** | Whatever your counted calories say (→ 04-01; your daily need is about {{ derived.calories.day }} kcal). Count it, do not estimate it |
| **Extend** | Eat the freezer first, keep portions steady, **never ration children's food** (→ 23-01), preserve freezer food before it spoils (→ 04-17) |
| **Substitute** | Sprouts for fresh food in winter (→ 04-16); wild greens as an extra only, identified with certainty (→ 05-06) |
| **Produce** | Garden, chickens or rabbits, hunting, fishing, trapping, each with its own season and lead time |
| **Stage 4 needs** | Garden space and **soil built over years** (→ 05-11), **seed you can save** (→ 05-03), water for the garden, animal protein, and a way to preserve the harvest (→ 04-04) |
| **Verdict** | {{#if has.acreage}}**Partly to largely reachable** on acreage, with years of work.{{else}}**Partial.** A yard can grow real vegetables and eggs; it cannot grow a year of calories for {{ household.size }} people. Grain and fat are the gaps.{{/if}} |
| **Where the numbers are** | → 04-01 pantry math · → 04-19 freeze-dried food · → 05-01 garden · → 05-03 seed saving · → 05-07 hunting |

## Light

| | |
|---|---|
| **Stock** | Flashlights, headlamps, batteries, candles, lamp oil |
| **Runway** | Longer than people expect if you use LEDs first and stop lighting empty rooms (→ 10-01) |
| **Extend** | One light per task, not per person; rechargeables plus a small panel; go to bed with the dark |
| **Substitute** | Fat and oil lamps, homemade candles, firelight (→ 10-03, → 10-04) |
| **Produce** | Rendered fat into candles and lamp oil; cotton wicks. Lasting, and dim |
| **Stage 4 needs** | A fat supply (which means animals, which means stage 4 food) and wick material |
| **Verdict** | **Reachable, at a quality cost.** Light fades gradually rather than ending |
| **Where the numbers are** | → 10-01 · → 10-03 · → 10-04 |

## Electricity

| | |
|---|---|
| **Stock** | Power stations ({{ gear.station_wh_total }} Wh in settings), power banks, vehicle batteries |
| **Runway** | Days, and less in cold (→ 09-07). A full-size fridge alone: about {{ derived.station_fridge_days }} days with no sun (estimate; the battery's own screen is the truth) |
| **Extend** | Triage the loads: **medical devices first, everything else negotiable** (→ 09-01) |
| **Substitute** | Vehicle charging (engine outdoors only), hand crank, doing without |
| **Produce** | Solar panels, a charge controller and a battery bank (→ 09-02, → 09-09). Yours: {{ gear.solar_w_total }} W of panels |
| **Stage 4 needs** | Panels, a controller, a battery you can replace, and **winter reality**: December output is a fraction of June's (→ 09-05). Your rough clear-day estimate: {{ derived.solar_wh_dec }} Wh in December, {{ derived.solar_wh_jun }} Wh in June |
| **Verdict** | **Reachable now, fading later.** Panels last decades; **the batteries are the consumable**, and they are stage 1 with no stage 4 |
| **Where the numbers are** | → 09-01 load triage · → 09-02 solar · → 09-03 batteries · → 09-05 winter · → 09-10 medical power |

## Sanitation and hygiene

| | |
|---|---|
| **Stock** | Soap, bleach, toilet paper, wipes, bin bags{{#if has.cats}}, cat litter{{/if}} |
| **Runway** | Weeks. **Bin bags and bleach run out sooner than you expect**, and both carry a lot of weight in the plan |
| **Extend** | Wash hands with less water, not less often. **Hygiene is never the thing you ration** (→ 13-02) |
| **Substitute** | Boiled cloth wipes, wood ash for scouring, ash or lime in the latrine (→ 13-07) |
| **Produce** | **Soap from fat and lye** (→ 13-09): a real stage 4 and one of the most valuable skills in the binder |
| **Stage 4 needs** | Fat, hardwood ash for lye, a container, and the method done carefully: **lye burns skin and eyes** |
| **Verdict** | **Reachable.** Soap-making is where a skill truly replaces a supply chain |
| **Where the numbers are** | → 13-02 · → 13-09 · → 13-01 · → 13-11 |

## Clothing, bedding, footwear

| | |
|---|---|
| **Stock** | What is in the closets{{#if has.child}}, and **the children grow out of theirs on a schedule**{{/if}} |
| **Runway** | Months to a year before wear matters{{#if has.child}}; **the children's sizes are the real clock**{{/if}} |
| **Extend** | Repair before replacing (→ 16-04), rotate to dry (→ 11-03), keep feet dry (→ 11-04) |
| **Substitute** | Layers, quilts, a blanket made into a garment, adult wool cut down for a child |
| **Produce** | Sew and patch from salvaged cloth. **Making new cloth is not realistic** |
| **Stage 4 needs** | Needles, thread and salvage. Plan on salvage for good |
| **Verdict** | **Salvage-dependent, permanently.**{{#if has.child}} Buying the next two sizes up of children's clothing and boots now is one of the cheapest hedges in this binder (→ 11-09).{{/if}} |
| **Where the numbers are** | → 11-01 · → 11-02 · → 11-07 · → 16-04 |

## Tools, blades, fasteners

| | |
|---|---|
| **Stock** | The tools in the house and garage |
| **Runway** | Years for good steel; **the consumables around them go first**: files, saw blades, fuel, screws, tape |
| **Extend** | Sharpen and maintain (→ 16-02), use the right tool, store dry |
| **Substitute** | Hand tools for power tools (→ 16-01), cord for hardware (→ 16-03) |
| **Produce** | Basic forge and repair work (→ 16-08). Realistically you reuse rather than make |
| **Stage 4 needs** | Fire, an anvil surface and skill: a long apprenticeship for modest results |
| **Verdict** | **Buy quality once.** A good axe, a good file and a good knife outlast almost everything else here |
| **Where the numbers are** | → 16-01 · → 16-02 · → 16-06 · → 16-08 |

## Medical: class C

| | |
|---|---|
| **Stock** | Prescription medicines, device supplies, epinephrine, formula, first-aid supplies |
| **Runway** | **For most households with a daily prescription, the governing clock.** Yours: {{#each meds as m}}{{m.name}} ({{m.member}}) about {{m.days_on_hand}} days; {{else}}none entered in settings; {{/each}}see → 23-02 |
| **Extend** | Correct storage (→ 29-07, → 12-21) and building supply legitimately while pharmacies work (→ 12-07). **Stretching doses is not a household decision**: ask the prescriber now |
| **Substitute** | **None for insulin, epinephrine or most daily prescriptions. None for a skilled birth attendant or surgery** (→ 23-03) |
| **Produce** | **Impossible**, at any scale, by any skill |
| **Stage 4 needs** | A working pharmaceutical industry |
| **Verdict** | **No lifecycle: only a stock and a date.** That is why the leave-or-stay decision exists (→ 01-02), why the medical go-kit is packed first (→ 22-06), and why getting supply back is a goal, not a chore |
| **Where the numbers are** | → 12-07 · → 12-11 · → 02-01 · → 02-03 · → 12-01 · → 12-16 · → 23-02 |

## Ammunition

| | |
|---|---|
| **Stock** | What is on the shelf, by calibre{{#if !has.firearms}} (none, per settings){{/if}} |
| **Runway** | Long for defence, **short for hunting** if hunting becomes a food plan |
| **Extend** | Practise with the cheapest calibre; confirm your sights once rather than re-adjusting again and again (→ 14-09) |
| **Substitute** | Traps and snares, which keep working while you do other jobs and use no ammunition (→ 05-15) |
| **Produce** | Reloading only moves the problem: its parts are a stock too. **No load data appears in this binder** |
| **Stage 4 needs** | Press, dies, primers, powder, bullets; primers are the hard stop |
| **Verdict** | **Finite. Treat every round as irreplaceable**, and let traps feed you |
| **Where the numbers are** | → 14-07 · → 14-08 · → 14-09 · → 05-15 |

## Seed, soil and fertility

| | |
|---|---|
| **Stock** | The seed packets in the drawer and what the soil holds now |
| **Runway** | Seed germination drops each year; **soil fertility drops with every harvest** |
| **Extend** | Store seed cool, dark and dry; compost everything (University of Minnesota Extension, Composting in Home Gardens; → 05-11); rotate beds |
| **Substitute** | Buy open-pollinated varieties now: **hybrid seed does not come true from saved seed** (→ 05-03) |
| **Produce** | **Save seed** and **build soil**: compost, ash, mulch; human waste only within → 13-06's limits |
| **Stage 4 needs** | Open-pollinated varieties, distance between some crops so they do not cross, drying and storage, years of compost |
| **Verdict** | **Reachable, but only with a head start of several years.** Seed and soil cannot be bought in a hurry, which makes them the best thing to spend this year on |
| **Where the numbers are** | → 05-03 · → 05-11 · → 05-02 · → 25-01 |

## Money and records

| | |
|---|---|
| **Stock** | Cash on hand and the document kit (→ 19-01) |
| **Runway** | Cash is useful early and worthless late; documents stay useful |
| **Extend** | Small bills; spend cash while it is still accepted |
| **Substitute** | Trade goods and, better, **trade skills** (→ 18-02, → 18-03) |
| **Produce** | **Skills are the only thing you can produce indefinitely** (→ 23-05) |
| **Stage 4 needs** | Something people want that you can do again and again |
| **Verdict** | **The move from stock to skill happens here first** |
| **Where the numbers are** | → 19-01 · → 19-02 · → 18-02 · → 18-03 |

## The pattern, stated plainly

Read the verdict rows in order. Three things stand out:
1. **Water, light, soap and part of food can be solved where most people live.** Build those
   now.
2. **Fuel is stock-only, and firewood is hard to produce on a town lot.** For many
   households this row is the honest core of the case for a destination (→ 01-02, → 01-05).
3. **The class C medical rows have no stage 4 at all.** Nothing changes that. Preparation
   changes **how much time the stock buys** and **what you do with that time**.

## What to buy, in the order it pays off

| Item | What it moves forward | Notes |
|---|---|---|
| Rain barrels and a downspout diverter | Water → stage 4 | The cheapest stage 4 step on this page |
| Spare filter elements | Water → stage 4 | A filter is useless once its element is |
| A good axe, saw, file and splitting maul | Fuel → stages 2 and 4 | → 16-06; only pays off with wood to cut |
| **Open-pollinated seed**, plenty | Food → stage 4 | → 05-03. Cheap, light and time-sensitive |
| A compost bin (or just a pile) | Soil → stage 4 | → 05-11 |
| Soap-making supplies | Hygiene → stage 4 | → 13-09 |
| Sewing kit, heavy needles, thread | Clothing → stage 2 | → 16-04 |
| **Next two sizes of children's clothing and boots**{{#if !has.child}} (if children may join you){{/if}} | Clothing → stage 2 | The clock nobody plans for |
| Traps and snare wire | Food → stage 3 | → 05-15 |
| Extra battery capacity | Power → stage 2 | → 09-05; the panel outlives the battery |

No money? Salvage. Every food-grade bucket, jug and barrel moves water forward. Scrap wood and
fallen wood are the only in-town fuel resupply (never treated wood indoors). Cloth in the
children's future sizes, files, blades, needles, thread and screws are small, light, and the
real limiting supply around every tool you own.

## When it runs out

This page is the "when it runs out" page for the whole binder.
- Work down the table and mark each row 1, 2, 3 or 4.
- **Any row still at stage 1 with a runway shorter than your plan is an unfunded debt.**
- **Fuel stays at stage 1 for almost every household.** That shapes the decision about where
  to be.
- **The class C rows never leave stage 1.** That sets the timeline.

## By phase

- **A, at home:** water, light, hygiene and part of food can reach stage 4 on most
  properties. Push everything reachable to stage 4 while the shops still work.
- **B, moving:** you carry stage 1 stock and stage 2 skills; **almost nothing produces while
  you travel.** Everything on this page is being used up during phase B, which is why phase B
  should be short (→ 01-03).
- **C, establishing:** the only phase where fuel, food and fat can reach stage 4 together, and
  only somewhere with land, timber and water. {{#if has.destinations}}Run every row of this
  table against each destination: {{#each destinations as x}}{{x.name}} ({{x.status_text}}; water: {{x.water_source_text}}); {{/each}}see → 01-05.{{else}}No destination is entered in settings; → 01-05 shows how to judge one against this table.{{/if}} A
  place where no one expects you is a possibility, not a plan: arrive self-sufficient.

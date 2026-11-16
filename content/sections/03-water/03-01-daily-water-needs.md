---
id: 03-01-daily-water-needs
section: 03-water
title: "How much water we need (household math)"
version: 2
revised: 2026-11-16
layer: core
danger_level: caution
phase: [A, B, C]
tags: [water, planning, math, storage, household, runway]
derived_from: [03-01-daily-water-needs]
sources: [cdc-how-to-create-and-store-an-emergency-water-suppl-f0c412, cdc-how-to-make-water-safe-in-an-emergency-5d78b5, fema-ready-gov-water, fema-477-food-and-water-in-an-emergency]
related: [03-02-storing-water, 03-03-pool-water-desalination, 03-04-purifying-water, 03-05-rain-and-snow-water, 03-06-winter-water, 03-10-well-water-without-power, 23-02-master-consumables-table, 07-07-freeze-dried-rehydration, 20-05-infant-feeding, 20-09-pets, 22-05-kit-vehicle, 02-01-cl01-type-1-diabetes-injections]
cards: []
explainers: [EX-06]
promote_when: []
photo_slots: []
figures: []
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: { date: "2026-11-16", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "Needs-go-up and 3/4-gal drinking figures re-attributed to FEMA/Ready.gov; kit allowances labelled; toilet-tank water flagged as last reserve, disinfect first (FEMA); destination water source slot." }
---

# How much water we need (household math)

**What this page is for.** Water is the fastest survival clock in the house: you can go weeks
without food but only days without water. This page turns the CDC planning figure into your
household's numbers: how much to store, and how many days the water you already have will
last. Every other water page uses the numbers printed here.

> **CAUTION.** The numbers below are planning minimums built on the CDC figure, not comfort
> levels. Heat, hard work, illness, pregnancy and nursing all push real need higher. Plan above the
> minimum, never below it.

## Do this now

1. **Know your two numbers.**
   - **Floor:** {{ derived.water.floor_gal_day }} gallons a day for the whole household. This
     is the bare minimum. It is the number you fall back to in a crisis, never the plan.
   - **Plan:** {{ derived.water.plan_gal_day }} gallons a day. Store to this number.
2. **Three days is the minimum store. Two weeks is the goal.** For your household, two weeks
   at the plan rate is **{{ derived.water.two_weeks_gal }} gallons**.
3. **Know your runway.** You have {{ gear.water.stored_gal }} gallons stored. At the floor
   rate that is about **{{ derived.water.stored_days }} days**. At the plan rate it is
   shorter. Recount every week during an emergency.
4. **Store more if** anyone is sick, pregnant or nursing, if it is hot, or if people are
   doing hard physical work.
5. **Never ration drinking water to the point of thirst.** FEMA's advice: drink the amount you
   need today and try to find more for tomorrow (→ 03-05 rain and snow{{#if has.pool}}, → 03-03 your pool{{/if}}{{#if has.well}}, → 03-10 your well{{/if}}).

## Why these numbers

The CDC planning figure is **1 gallon per person per day**, with **at least a 3-day supply**
at home and a **2-week supply** if you can manage it (CDC, How to Create and Store an
Emergency Water Supply). That gallon is not all for drinking. FEMA says a normally active
person needs about three quarters of a gallon of fluid a day from water and other drinks; the
rest covers cooking, dishes, brushing teeth and basic washing (FEMA, Ready.gov Water).

**Needs go up.** The CDC says to store more for pregnant women, sick people, pets and hot
climates. FEMA adds that children, nursing mothers and sick people may need more, that a
medical emergency may need extra water, and that **in very hot weather water needs can
double** (FEMA, Ready.gov Water). Hard physical work raises it too. A grid-down summer with laundry by
hand and wood to haul is not a quiet day on the couch.

### How your numbers are worked out

The binder builds your **floor** from your household profile. The 1 gallon per person is the
CDC figure. The CDC and FEMA say to store more for pregnancy, nursing, infants and pets but
publish no exact amount, so the extra amounts below are this binder's planning allowances, not
published figures:

| Who | Added to the daily floor |
|---|---|
| Each person | 1 gallon |
| Each pregnant or nursing member | 0.5 gallon more |
| Each infant (formula mixing and washing) | 0.5 gallon more |
| Each pet | 0.25 gallon (a cat drinks far less, a big dog may drink more; check yours) |

Your household: **{{ household.size }} people**, floor **{{ derived.water.floor_gal_day }}
gallons a day**.

The **plan** figure is the floor plus a 30 percent margin ({{ derived.water.plan_gal_day }}
gallons a day). The margin is also this binder's planning allowance, not a published figure.
It covers heat, sickness, spills and the water that cooking eats.
If your food store leans on freeze-dried or dehydrated meals, those meals are rehydrated with
water that counts against the day, so treat the plan number as the least you need
(→ 07-07).

| | Per day | Two weeks |
|---|---|---|
| Floor (crisis ration) | {{ derived.water.floor_gal_day }} gal | floor x 14 |
| Plan (store to this) | {{ derived.water.plan_gal_day }} gal | {{ derived.water.two_weeks_gal }} gal |

### People who need extra care

{{#if has.infant}}- **Your infant.** Any water used for bottles, formula, cups or feeding must
  be safe water: boiled or treated, never raw pool or surface water. Infants are the least
  able to survive a stomach illness from bad water (→ 20-05).
{{else}}- **Infants.** Any water used for bottles, formula, cups or feeding must be safe water:
  boiled or treated, never raw pool or surface water. Infants are the least able to survive a
  stomach illness from bad water (→ 20-05).
{{/if}}
{{#if has.nursing}}- **The nursing member.** FEMA says needs rise while nursing. The margin
  in your plan number exists for her. Hers is never the line to ration.
{{else}}- **Anyone nursing** may need more water, says FEMA. Never ration a nursing mother's
  share.
{{/if}}
- **Diabetes.** Dehydration and high blood sugar feed each other: high sugar makes the body
  pass more urine, which concentrates the sugar further. Keep drinking water within reach of
  a person with diabetes, day and night, and give them a larger share
  {{#if has.condition.CL-01}}(→ 02-01){{else}}(→ 02-05){{/if}}. Some households agree in
  advance that this person gets water first if supply runs short. That is a conversation to
  have now, not during the shortage.
- **Children** get a full share. Do not shortchange them.
{{#if has.pets}}- **Your pets drink treated water too.** Raw pool or pond water can make an
  animal sick, and there may be no vet. Keep pets away from the pool and pour their water from
  the treated supply (→ 20-09).
{{else}}- **Pets** drink treated water, the same as people (→ 20-09).
{{/if}}

### Water that is not drinking water

Flushing a toilet uses gallons each time. Laundry and bathing use more. **Do not spend stored
drinking water on these.**
{{#if has.pool}}Your pool is for that: raw pool water flushes toilets, washes floors and
fights fires perfectly well (→ 03-03).{{else}}Use rain barrels, a pool or pond, or other
untreated water for flushing and washing floors (→ 03-05, → 13-01).{{/if}}

### The runway

**Runway = stored gallons ÷ gallons used per day.** That is how many days you have before you
*must* be producing water. Divide by the plan figure while things are normal; divide by the
floor only after you have already cut back to the floor. Write the number on the consumables
table (→ 23-02). For most households the honest answer is under two weeks, which is why rain,
snow{{#if has.pool}}, the pool{{/if}}{{#if has.well}}, the well{{/if}} and a way to treat
water matter so much.

## Gear and supplies

**Have it now (buy toward this):**

| Item | Why | Notes |
|---|---|---|
| Food-grade water containers (5 to 7 gal jugs, or a 55-gal drum) | The bulk of the store | Jugs can be moved. A full 55-gal drum weighs about 460 lb and never moves again |
| Bottled water by the case | Safest water with no preparation | The CDC calls it the safest reliable emergency source |
| Bathtub water bladder | Fills a tub cleanly before the water stops | Read the capacity on the package; only useful if filled *before* pressure is lost (→ 03-02) |
| Labels and a marker | Track what is left | Date each container; mark drums in gallons |
| A runway card | Know the number without doing maths under stress | Write "stored gallons ÷ {{ derived.water.plan_gal_day }}" on the container |

**If you don't have it, use what is in the house:**

{{#if has.water_heater_tank}}- **Your water heater** holds about {{ dwelling.water_heater_gallons }} gallons. It can be
  scalding hot, and gas heaters keep heating while gas flows. Never drain it from memory: use
  the step-by-step procedure on → 03-02.
{{else}}- **A tank water heater**, if you have one or find one, holds tens of gallons (the size
  is on its label). FEMA lists it as a safe water source in the home. It can be scalding hot;
  use the step-by-step procedure on → 03-02.
{{/if}}
- The water in your **pipes** and **ice** in the freezer, which FEMA lists as safe sources.
- Toilet **tanks** (the box behind the seat, never the bowl), only if no cleaning tablet or dye
  is in them. They are the last of the in-house reserves: FEMA's guide says not to drink tank
  water, so disinfect it before drinking (→ 03-04), or keep it for washing and flushing.
- Any clean food-grade container: soda bottles, juice jugs. **Not** milk jugs (milk protein
  is hard to clean out and the water spoils), and never containers that held chemicals.

## When it runs out

- **Runway:** stored gallons ÷ {{ derived.water.plan_gal_day }} a day (÷ {{ derived.water.floor_gal_day }}
  only once you have already cut back to the floor). Recount weekly.
- **Ration:** cut washing and cooking water first, never drinking water. Move washing and
  flushing to untreated water at once; that alone can halve how fast stored water goes.
- **Resupply:** rain and snowmelt first, because they cost the least fuel to make safe
  (→ 03-05). In winter, snow is often the easiest large source (→ 03-06).{{#if has.pool}}
  Distilling pool water works but burns a lot of fuel (→ 03-03).{{/if}}{{#if has.well}} Your
  well can still give water without power (→ 03-10).{{/if}}

## Phase notes

- **A (sheltering at home):** build the two-week store now, while it is a shopping trip.
- **B (moving):** water weighs 8.34 lb per gallon, so you can carry very little. Carry one
  to two days per person and a way to treat more (→ 03-04), and plan the route around water.
  For {{ household.size }} people that is roughly {{ derived.water.plan_gal_day }} to twice
  that in gallons. Load it low in the vehicle, over the rear axle, strapped down; never in a
  roof box and never loose in the passenger area (→ 22-05). Fill containers from the tap on
  the way out if there is time.
- **C (rural or at a destination):** find out before you go where the water comes from.
  On **town or district water**, pressure dies when the grid's pumps stop, so the first job
  on arrival is to **fill every container and tub at once**, then set up rain catchment
  (→ 03-05). On a **private well**, the pump needs power; → 03-10 explains how to get water out
  without it. Either way the daily maths becomes a hauling and treating problem, not a storage
  problem.
{{#if has.destinations}}
  Your destinations:
{{#each destinations as d}}  - **{{ d.name }}** ({{ d.county }}, {{ d.state_name }}). Water source: {{ d.water_source_text }}
{{/each}}
{{/if}}

## Cross-references

→ 03-02 storing water · → 03-03 pool water · → 03-04 purifying water · → 03-05 rain and snow ·
→ 03-06 winter water · → 03-10 well water without power · → 23-02 consumables table ·
→ 22-05 vehicle loading

---
id: 09-01-power-priorities
section: 09-power-and-energy
title: "What actually needs power (load triage)"
version: 2
revised: 2026-11-16
layer: core
danger_level: caution
phase: [A, B, C]
tags: [power, electricity, triage, planning, watt-hours, medical]
derived_from: [09-01-power-priorities]
sources:
  - american-red-cross-power-outage-safety-6d07a8
  - generac-gp3500io-owners-manual
  - resmed-airsense-11-user-guide-r14
  - caire-airsep-newlife-technical-manual-r14
  - dometic-cfx3-35-product-page-r14
related:
  - 09-02-solar-basics
  - 09-03-batteries-and-storage
  - 09-05-solar-in-winter
  - 09-06-charging-medical-devices
  - 09-10-power-for-medical
  - 09-16-outage-day-one
  - 07-06-electric-kettle-cooking
  - 08-04-emergency-heat-options
  - 23-01-depletion-framework
  - 23-02-master-consumables-table
  - 29-02-ex02-batteries-and-power-stations
  - 28-07-reading-your-own-gear
cards: [DC-07, DC-20]
explainers: [EX-02, EX-04, EX-14]
promote_when: []
photo_slots: []
figures: []
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: { date: "2026-11-16", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "Kettle 135 Wh/litre-boil to match 07-06/09-03; fridge row arithmetic fixed to EX-02's 1,000-2,000 Wh; CPAP (ResMed), concentrator (AirSep) and cooler (Dometic) from maker specs; motor start 3x (Generac); remaining rows labelled placeholders as on EX-02" }
---

# What actually needs power (load triage)

**What this page is for.** Before you buy a single panel, battery or generator, decide what *must*
run when the grid is down, add up how much energy that takes in a day, and size everything else to
that number. Most households do it backwards: they buy a generator or a "solar generator" first and
then find out what it can run. This page is the list and the arithmetic. If watts and watt-hours
are new to you, read → 29-02 first; this page uses them without re-explaining.

## Do this now
- **Buy a plug-in watt meter (the kind a lamp plugs into) and measure your real devices.** The
  label on an appliance gives its *maximum* draw, not what it uses over a day. A refrigerator
  draws its full running watts only while the compressor runs; a typical full-size one uses about
  1,000 to 2,000 Wh across a day, an average of roughly 40 to 85 W (→ 29-02). Its yellow
  EnergyGuide label gives kilowatt-hours per year: ÷ 365 for a day (→ 04-17). Guessing here is the
  single biggest cause of systems that turn out too small.
- **Fill in the table at the bottom of this page** with measured numbers. It is the input to
  → 09-02, → 09-09 and → 09-10. Nothing downstream works without it.
- **Sort every load into the four tiers below and put the tier on a label on the device.** You
  make these decisions once, calmly, now, not at 2 a.m. in a cold house.
- **Know your Tier 0 loads by name.**
  {{#if has.refrigerated_meds}}This household has a refrigerated medicine: keeping it cold is a
  Tier 0 load and usually the biggest one (→ 09-10).{{/if}}
  {{#if has.cpap}}A CPAP machine is on the Tier 0 list (→ 02-24, → 09-06).{{/if}}
  {{#if has.oxygen}}An oxygen concentrator is on the Tier 0 list, and it is a large load:
  one common 5-litre home concentrator is rated at 350 W (AirSep NewLife technical manual), about
  8,400 Wh a day if it runs around the clock (→ 02-08, → 09-06).{{/if}}
  Everything else on this page is comfort by comparison.

## Why it works this way

**The number that matters is the watt-hour (Wh).** Watts are how fast a device uses energy;
watt-hours are how much it used. Watts × hours = watt-hours: a 10 W LED bulb for 5 hours is
50 Wh. A battery is rated in watt-hours, or in amp-hours at a voltage (amp-hours × volts =
watt-hours; a 100 Ah 12 V battery is roughly 1,200 Wh counted at 12.0 V, or 1,280 Wh for a
lithium iron phosphate battery counted at its 12.8 V nominal). Every sizing decision in this section is that one piece of arithmetic
(→ 29-02).

**Two numbers describe every load, and you need both:**
- **Power (W)** decides whether a battery and its inverter can run the device *at all*. A
  1,500 W microwave trips a 300 W power station instantly, however large its battery is.
- **Energy (Wh per day)** decides how long you can keep doing it.

**Heat and motors are the two budget-killers.** Anything that makes heat (kettle, toaster, hair
dryer, space heater, coffee maker) or drives a compressor or motor (refrigerator, freezer, well
pump, furnace blower) draws ten to a thousand times what electronics draw. **A survival power
system does not make heat.** Heat comes from fire and fuel (Sections 06, 07 and 08). Electricity
is for information, medicine and light.

**Two deliberate exceptions** (→ 07-06):
- **Boiling small amounts of water.** An electric kettle is efficient, silent and makes no carbon
  monoxide. Budget about **135 Wh from the battery per one-litre boil**, kettle and inverter losses
  included; a freeze-dried pouch that takes about half a litre is about half that (→ 07-06). A
  vacuum flask filled from one boil saves boiling again later.
- **Heated blankets (50 to 100 W)** warm the person, not the room: the best heat per watt you
  can get from a battery.

### The four tiers

**Tier 0: life-critical. This is the reason the system exists.**

| Load | Why | Typical draw |
|---|---|---|
| Phone(s) used for medical devices, alerts and contact | Information; for some households the phone runs a medical device (→ 09-06) | About 10 to 20 Wh a day with the screen mostly off |
| Cooling for refrigerated medicine | Some medicines lose strength when warm (→ 29-07, → 09-10) | **200 to 1,500 Wh a day, depending on what does the cooling** |
| Medical devices that plug in or charge (CPAP, oxygen concentrator, pump accessories, nebuliser) | Breathing and medicine delivery (→ 09-06) | From a few Wh to thousands; read the manual's power figures and measure (→ 09-06) |
| One reliable light source at night | Falls, stairs, children, injuries | 10 to 50 Wh a day |

**Tier 1: high value, low cost.** Radio and scanner (→ 15-02, → 15-04), headlamps and
rechargeable AA and AAA cells (→ 10-01), a small fan to move warm air in one room (→ 08-01), a
tablet or laptop holding this binder, rechargeable tool batteries, a water filter pump.

**Tier 2: quality of life, when there is a surplus.** A refrigerator or freezer for food (as
opposed to medicine), laundry, children's devices for morale (→ 21-02), power tools, a sewing
machine.

**Tier 3: do not run these on batteries.** Electric space heat, electric cooking, electric water
heating, air conditioning, a well pump on a small system, a clothes dryer. **These are fuel jobs,
not electricity jobs.** Each one empties a battery bank in well under a day and buys almost
nothing.

### Typical draws (planning placeholders; measure your own)

Rows marked with a maker's name are that maker's published figure for one common model; the rest
are rough placeholders, the same ones used on → 29-02, to be replaced by your own measurements.

| Device | Typical W | Typical Wh per day | Tier |
|---|---|---|---|
| Phone charge | 5 to 20 W | 10 to 20 Wh | 0 |
| LED bulb or lantern | 3 to 10 W | 15 to 50 Wh | 0 or 1 |
| Headlamp recharge | 2 to 5 W | 5 to 10 Wh | 1 |
| Handheld radio charge | 5 W | 10 to 20 Wh | 1 |
| Laptop | 30 to 65 W | 100 to 300 Wh | 1 or 2 |
| CPAP (ResMed AirSense 11: typical 56 W, peak 73 W) | about 56 W | about 450 Wh for an 8-hour night at the typical figure; less with humidifier and heated tube off (measure) | 0 if you use one |
| Oxygen concentrator, 5-litre home unit (AirSep NewLife: 350 W) | 350 W | about 8,400 Wh if run 24 hours | 0 if you use one |
| 12 V compressor cooler (medicine) (Dometic CFX3 35: 0.98 Ah an hour at 12 V in a 90 °F room) | up to 90 W while running (7.5 A rated) | about 280 Wh in a hot room | 0 |
| **The power station's own draw** (its idle use while it runs a load) | commonly 3 to 10 W, more with the AC inverter on | 70 to 240 Wh | 0: unavoidable; keep it small by using the 12 V port and switching the AC inverter off (→ 09-10) |
| Full-size refrigerator | 100 to 200 W while the compressor runs | 1,000 to 2,000 Wh (EnergyGuide label ÷ 365 for yours) | 0 or 2 |
| Chest freezer | Running watts on its label | EnergyGuide label ÷ 365 | 2 |
| Box fan | 50 to 100 W | 400 to 800 Wh | 1 or 2 |
| Microwave | 1,000 to 1,500 W | | 3 |
| Electric kettle | 1,200 to 1,800 W | | 3, except the small-boil exception above (→ 07-06): tea and meals yes, bulk heating never |
| Space heater | 1,500 W | 36,000 Wh per day if run continuously | 3, never |
| Well pump | 1,000 to 2,500 W, much more at start | | 3 on small systems (→ 03-10) |

Look hard at the space heater row. One space heater running all day uses about 36,000 Wh. Compare
that with what your panels make on a clear December day (→ 09-05): for most households it is a
few hundred to a couple of thousand watt-hours. That is why heat comes from combustion, clothing
and one warm room (→ 08-04), not from batteries.

{{#if has.house_connection}}A furnace blower is a motor load (its running watts are on the motor
plate; allow about 3 times that for starting, as Generac's manual does for motor loads). It can run
from a generator or a large station only through a safe connection: this household's is
"{{ gear.house_connection }}" (→ 09-04).
{{else}}A gas furnace needs electricity for its blower and controls. It can run from a generator
or a large station only through a safe connection: a transfer switch or interlock fitted by an
electrician, or a cord-and-plug conversion, which is a decision card (→ 09-04, {{choice DC-07}},
→ 30-08). Never by plugging a generator into an outlet (→ 30-01).{{/if}}

### Doing the triage
1. List every device you would want. Measure or estimate its watts and hours per day.
2. Multiply for watt-hours per day. Add up each tier.
3. **The Tier 0 total is your must-have design number.** Add about 30% for inverter and charging
   losses (this binder's planning margin; your inverter's efficiency is on its label, and
   batteries lose a little too).
4. **Tier 0 plus Tier 1 is the realistic target.** If that is affordable, build to it.
5. **Everything above Tier 1 is a fair-weather bonus** you run only on a sunny surplus day.
6. **Check the plan against December, not June** (→ 09-05). A system sized in summer
   disappoints in the month you need it most.

## Gear and items

**Have it now (buy toward this):**

| Item | Why | Notes |
|---|---|---|
| Plug-in watt meter | Turns guesses into a real design | The highest-value purchase in this section |
| DC watt meter (inline 12 V or USB) | Measures the DC side: 12 V loads, USB loads, panel output | For → 09-09 |
| This page's table, filled in | The design document for everything downstream | Copy the totals to → 23-02 |
| Label maker or masking tape and marker | Tier label on every device | Removes decisions from a crisis |
| Power strips with switches | Kills standby draw at once | Standby draw adds up over weeks |
| USB power banks, 20,000 mAh or larger | About 70 Wh each (20 Ah × the cell's 3.6 to 3.7 V); covers phone loads for days (→ 09-06) | The cheapest useful battery there is |

**Scavenge or substitute:**
- **Measuring without a meter:** appliance labels give maximum watts (a ceiling, not a daily
  figure, → 29-14); a car's 12 V socket fuse rating bounds what you can pull from it; the
  percentage drop on a power station over a known time is a crude but usable meter.
- **Storage:** laptop batteries, tool batteries with USB adapters, car batteries (with the
  cautions in → 09-14), any power bank in a drawer.
- **Cutting the load beats making power.** A headlamp instead of a room light, a hand-crank radio,
  cooking on fire, hanging laundry: every watt you do not need is a watt you do not have to make,
  store and maintain.

## When it runs out
- **Batteries are the consumable, not panels.** Panels degrade slowly over decades; batteries wear
  out in years and faster if abused (→ 09-03, → 09-07). Your power runway is a battery question.
- **Ration by tier, in order.** Tier 3 is already off; drop Tier 2, then Tier 1. **Tier 0 is
  defended to the end**, and if Tier 0 cannot be met, that is not a power problem, it is a medical
  emergency and an input to the go/no-go decision (→ 01-02).
- **Substitutes for each tier:** light → lamps and flashlights first, candles only with care
  (→ 10-02; candles indoors are a decision, {{choice DC-20}}, → 30-21); refrigeration → cold
  storage and evaporative cooling (→ 04-09, → 12-21); information → this binder and a hand-crank
  radio; tools → hand tools (→ 16-01).
- **Write the Tier 0 number on the consumables table (→ 23-02)** and track how many days of it
  your storage holds, the same way you track food and water.

## Our loads

{{#if has.power_station}}Our power stations total **{{ gear.station_wh_total }} Wh**.{{/if}}
{{#if has.solar}}Our panels total **{{ gear.solar_w_total }} W**. On a clear December day at
home ({{ region.home.sun_hours_dec }} peak sun hours) that is roughly
{{ gear.solar_w_total }} × {{ region.home.sun_hours_dec }} × 0.75 = ________ Wh; in June
({{ region.home.sun_hours_jun }} sun hours), ________ Wh (method on → 09-02).{{/if}}
{{#if has.generator}}Our generator is rated **{{ gear.generator_watts }} W** running on
{{ gear.generator_fuel }} (→ 09-04).{{/if}}

Measure each device, then write it in. Correct in pencil as you learn.

| Device | Measured W | Hours per day | Wh per day | Tier |
|---|---|---|---|---|
{{#if has.refrigerated_meds}}| Medicine cooler (→ 09-10) | | 24 (cycling) | | 0 |
{{/if}}{{#if has.cpap}}| CPAP (→ 09-06) | | | | 0 |
{{/if}}{{#if has.oxygen}}| Oxygen concentrator (→ 09-06) | | | | 0 |
{{/if}}| Phones and medical charging | | | | 0 |
| Night light or headlamp recharge | | | | 0 |
| Power station idle draw | | 24 | | 0 |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| **Tier 0 subtotal** | | | | |
| **Tier 0 × 1.3 = design target** | | | | |
| **Tier 0 + Tier 1 subtotal** | | | | |

## Phase notes
- **A (at home):** the whole system lives here: panels in the yard, batteries indoors where they
  stay warm (→ 09-07), Tier 0 and Tier 1 running.
- **B (moving):** you carry a fraction: a folding panel, one power station or battery, power
  banks and the medical loads. **Tier 0 only.**
- **C (settled somewhere new):** rebuild bigger. This is also where fuel generation (→ 09-04) is
  least sustainable and solar matters most, because there is no fuel resupply.

## Cross-references
→ 09-02 solar basics and sizing · → 09-03 batteries and power stations · → 09-05 solar in winter ·
→ 09-09 a small solar build · → 09-10 power for refrigerated medicine · → 09-16 outage day one ·
→ 29-02 batteries and power stations explained · → 28-07 reading your own gear

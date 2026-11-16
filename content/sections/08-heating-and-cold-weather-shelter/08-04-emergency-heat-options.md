---
id: 08-04-emergency-heat-options
section: 08-heating-and-cold-weather-shelter
title: "Emergency heat options and their risks"
version: 1
revised: 2026-11-16
layer: core
danger_level: critical
phase: [A, C]
tags: [heating, heaters, furnace, propane, kerosene, wood stove, heated blanket, power station, carbon monoxide, fire, children]
derived_from: [08-04-emergency-heat-options]
sources:
  - cdc-carbon-monoxide-poisoning-basics-772153
  - cdc-winter-weather-before-during-and-after-13bbd5
  - noaa-national-weather-service-during-extremely-cold-9c1973
  - american-academy-of-pediatrics-healthychildren-org-h-7bd7d0
  - enerco-group-mr-heater-manufacturer-portable-buddy-r-759ce5
  - ghp-group-inc-dyna-glo-manufacturer-portable-kerosen-477cfd
  - university-of-missouri-extension-unvented-portable-k-e850fe
  - nfpa-heating-fire-safety-5cb9e6
  - us-fire-administration-fema-candle-fire-safety-use-f-6eeda1
related:
  - 08-01-heating-one-room
  - 08-02-carbon-monoxide-safety
  - 08-06-improvised-shelter-warmth
  - 08-07-ducted-heater-operation
  - 08-08-wood-heat-operation
  - 08-09-portable-propane-heaters
  - 08-10-wick-kerosene-heaters
  - 06-05-alternative-fuels
  - 06-06-fuel-storage-safety
  - 09-01-power-priorities
  - 09-03-batteries-and-storage
  - 09-04-generators
  - 09-05-solar-in-winter
  - 09-16-outage-day-one
  - 11-02-keeping-kids-warm
  - 20-02-child-safety-offgrid
  - 22-05-kit-vehicle
  - 23-02-master-consumables-table
  - 28-04-portable-heaters
  - 29-01-ex01-fuels
  - 29-02-ex02-batteries-and-power-stations
  - 29-03-ex03-carbon-monoxide
  - 29-04-ex04-electricity-in-the-house
  - 29-12-ex12-extinguishers-blankets-and-alarms
  - 29-14-ex14-reading-a-label
  - 30-01-the-floors
  - 30-02-dc01-unvented-heater-overnight
  - 30-03-dc02-propane-cylinder-indoors
  - 30-08-dc07-diy-cord-and-plug-conversion
  - 30-10-dc09-infant-bed-sharing
  - 30-21-dc20-open-flame-indoors
  - 30-22-dc21-uninspected-fireplace-or-stove
  - 06-04-wood-supply-and-depletion
  - 07-01-cooking-on-an-open-fire
  - 08-05-hypothermia-frostbite
  - 11-01-cold-weather-layering
cards: [DC-01, DC-02, DC-07, DC-09, DC-20, DC-21]
explainers: [EX-01, EX-02, EX-03, EX-04, EX-12, EX-14]
promote_when: [is.cold_winters]
photo_slots:
  - { id: heater-barrier, caption: "Our heater in the warm room with its barrier and clearances marked" }
  - { id: furnace-data-plate, caption: "Our furnace data plate (blower watts or amps)" }
figures: []
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: null
---

# Emergency heat options and their risks

**What this page is for.** A plain comparison of every way to stay warm when the power or fuel
fails, from the furnace you already own to a candle, with what each one can do to you. Each
option is ranked by risk, and the heater pages hold the procedures. Fuels are explained on
→ 29-01, carbon monoxide (CO) on → 29-03, power stations on → 29-02.

> **SAFETY.** Every option here can hurt you in a different way: **carbon monoxide**, **house
> fire**, or **burns to a child**. Only a device's own label and manual decide whether it may be
> used indoors; follow the manual over anything written here. **Never run a generator, charcoal,
> or any engine indoors, in a garage, or near an open window.** Carbon monoxide kills in minutes
> with no warning; alarms fail; there is no mitigation that works every time (→ 30-01). **Never
> use a gas oven or range to heat the house** (CDC). Battery CO **and** smoke alarms in the heated
> room before anything is lit (→ 08-02).

## Do this now

1. **Rank your own options** with the table below and write your order here:
   1 ________ 2 ________ 3 ________ 4 ________.
2. **Insulation, layers and body heat are always on** and cost no fuel (→ 08-01, → 08-06).
3. **Before you light any heater:** CO alarm and smoke alarm up and tested; extinguisher within
   reach (→ 29-12); the manual's air openings open; a barrier if there are children or pets.
4. **One fuel-burning heater at a time.** Never two unvented heaters together.
5. **Overnight heat is a decision card,** not a default: {{choice DC-01}} (→ 30-02).

## Your home on file

Main heat: **{{ dwelling.primary_heat }}**.
{{#if has.unvented_heater}}Heaters you listed: {{#each heaters as h}}{{h.kind_text}} {{h.model}};
{{/each}}{{else}}You have not listed a portable heater.{{/if}}
{{#if has.power_station}}Power stations on file: {{ gear.station_wh_total }} watt-hours in
total.{{/if}}{{#if has.generator}} Generator: {{ gear.generator_watts }} running watts,
{{ gear.generator_fuel }}.{{/if}}

## The options, honestly assessed

| Option | Heat | Indoors? | Main risks | Notes |
|---|---|---|---|---|
| **Insulation, layers, body heat** | Passive | Yes | None | Always on (→ 08-06, → 11-01) |
| **Your gas furnace on battery or generator power** | Whole house | Yes, it is the furnace | None new, **if** it can be safely connected (below) | Often the best heater you already own |
| **Heated blanket on a power station** | Person-level | Yes | Burns and overheating for babies | Warm the bed, not the room (below) |
| **Portable propane heater sold for indoor use** (Buddy family) | Good | Yes, by its manual | CO, low oxygen, fire, propane leak | Oxygen-depletion and tip-over shutoffs; tank outdoors (→ 08-09) |
| **Wick kerosene heater sold for indoor use** | High | Yes, by its manual | CO, fumes, fire, **wrong fuel** | Usually no oxygen-depletion sensor (→ 08-10) |
| **Ducted diesel or kerosene heater** | High | Yes, if installed with intake and exhaust outside | CO if the install leaks | → 08-07 |
| **Wood stove or fireplace** (installed, vented) | High (stove); low (open fireplace) | Yes | Chimney fire; CO if the flue is blocked | Inspect first: {{choice DC-21}} (→ 30-22; → 08-08) |
| **Outdoor fire pit or outdoor fireplace** | High, outdoors | **No** | CO, fire | Cook and boil there; it is not house heat (→ 07-01) |
| **Generator running an electric heater** | Moderate | **Generator outdoors only** | CO; burns fuel fast | Usually a poor use of fuel (→ 09-01) |
| **Candles and tea-light "heaters"** | Negligible | A decision card | **Fire** | Not a heat source (below) |
| **Gas oven or range** | — | **Never** | CO | Not a heater. People die doing this (CDC) |
| **Charcoal, grill, camp stove** | — | **Never** | CO | Floor rule (→ 30-01) |

Spec tables for common heater models are on → 28-04.

## The gas furnace: the heater you may already have

{{#if has.gas_any}}Your home has gas service.{{/if}} **In many electrical outages the gas keeps
flowing.** The gas supply runs largely separately from the electric grid, so a gas furnace is
often fully fuelled and stopped only because its **blower and controls** have no power. Many
furnace blowers draw roughly 400 to 800 watts; **read your furnace's data plate** for the real
figure (→ 29-14).

- **Run it in bursts:** 15 to 20 minutes to lift the whole house a few degrees, then off, and let
  the house coast on its stored heat for an hour or more. Repeat. Warm the house before bed and
  at waking; hold the warm room with blankets and bodies between bursts (→ 08-01).
- **Power it from a power station or a generator outdoors.** Divide the station's usable
  watt-hours by the blower's watts for a rough runtime (→ 29-02); solar recharge stretches it
  (→ 09-05).

**The connection must be safe, and must be arranged in advance.** Most furnaces are wired
directly into the house, so nothing can plug into them. **Never connect a generator to house
wiring except through a transfer switch, or an interlock kit with the main breaker off. Never
backfeed through an outlet with a double-male ("suicide") cord.** Backfeed electrocutes line
workers and neighbours and starts fires (→ 30-01; → 29-04). A third route is converting the
furnace to a cord and plug, so that the furnace unplugs from its own wall outlet and plugs into
the generator or power-station cord; that is not a connection to house wiring. Whether your
household does that conversion itself or has an electrician do it is a decision card:
{{choice DC-07}} (→ 30-08). The write-up is on → 09-04.

{{photo furnace-data-plate}}

## Heated blankets: warm the bed, not the room

A heated blanket draws a small fraction of what a plug-in space heater does (a space heater is
typically 1,500 watts on high; read both labels). On a power station it can warm a bed all night
where a space heater would drain the same station in an hour or two. Work out your own runtime
from the labels (→ 29-02).

**No electric blanket on or around a baby or toddler.** The AAP keeps loose bedding out of a
young child's sleep space and warns against overheating (AAP, How to Keep Your Sleeping Baby
Safe). A small child can neither escape nor report a blanket that is too hot. Use it to pre-warm
a bed and switch it off before the child gets in, or to warm the adults, whose bodies then warm
the shared sleeping space (→ 11-02). {{#if has.young_child}}Your household has a young child:
this applies.{{/if}} Bed-sharing for warmth is its own card: {{choice DC-09}} (→ 30-10).

## Portable fuel heaters sold for indoor use

{{photo heater-barrier}}

These are **unvented**: no chimney, so their exhaust, including some CO, stays in the room, and
they use the room's oxygen and add water vapour (MU Extension, Unvented Portable Kerosene
Heaters).

- **Propane heaters of the Buddy family** carry an **oxygen depletion sensor (ODS)**, which shuts
  the heater off when room oxygen falls, and a **tip-over switch**. Neither measures CO. The
  manual requires air openings high and low, and allows a 20-lb tank only **outdoors**, on the
  maker's hose (Enerco/Mr. Heater, Buddy owner's manual). Bringing a larger tank inside is a
  decision card: {{choice DC-02}} (→ 30-03). Procedures: → 08-09.
- **Wick kerosene heaters** usually have a tip-over shutoff but no ODS. They burn steadily for
  many hours on a tank, need water-clear 1-K kerosene only, and are refuelled outdoors and cold
  (GHP Group/Dyna-Glo, Portable Kerosene Heater owner's manual). Procedures: → 08-10.

**The rules for either, from their manuals:**

- **Follow the manual** for room size, air openings, clearances and fuel.
- **CO alarm running** in the same room, at pillow height (→ 08-02).
- **An adult in the room** while it burns. Never left unattended.
- **No fuel stored in the living space** (→ 06-06). **Fuel is never stored or transferred near an
  open flame or a running appliance** (→ 30-01).
- **One at a time.** The propane class's manual forbids other fuel-burning appliances in the
  space.
- **Overnight:** both manuals say never while sleeping. Keeping one burning trades CO and fire
  risk against a dangerously cold night; the household decides on the card: {{choice DC-01}}
  (→ 30-02).
- **Moisture:** both add water vapour. In a closed room that means condensation, damp bedding
  and mould, and damp bedding is a cold-injury risk (→ 08-05). Vent briefly.

## Candles

Candles give almost no heat against a house's losses, and an open flame in a blanket-draped room
full of people is a fire risk bought for nothing. The US Fire Administration says use flashlights,
not candles, in a power outage (USFA, Candle Fire Safety). Whether your household uses any open
flame indoors is a decision card: {{choice DC-20}} (→ 30-21). A stranded car is the one place a
single candle's heat matters, with a window cracked and an adult awake beside it (→ 22-05).

## Fire risk with children

{{#if has.child}}Your household has children.{{/if}} A small child and any hot surface is a burn
waiting to happen.

- **A physical barrier** around any heater or stove: a hearth gate or a furniture perimeter.
- **Never leave a burning heater unattended,** and never with children in the room unsupervised.
- **Clearances:** keep bedding, door blankets, curtains and toys out of the manual's clearance.
  NFPA's rule is at least 3 feet from anything that can burn (NFPA, Heating Fire Safety). A
  blanket hung to trap heat is a fire hazard if it can swing into the heater.
- **Teach the rule** early and often (→ 20-02).

## Passive heat that costs nothing

- **South-facing windows:** curtains open in sun, closed at dusk.
- **Thermal mass:** jugs of water near (not on) a heat source soak up heat and give it back
  overnight.
- **Hot-water bottles or heated stones** wrapped thickly in cloth, in the bedding before you get
  in. **They pre-warm a child's bed and come out before the child gets in** (burns on skin that
  cannot report it). Never a hot stone straight against skin or bedding.
- **Cooking heat:** if you cook indoors on an appliance allowed indoors, that heat is already paid
  for.

## Gear

| Item | Why | Notes |
|---|---|---|
| Battery CO alarm **and** smoke alarm for the heated room | The two ways heaters kill | → 08-02 |
| Fire extinguisher (ABC), plus a second | Fire is the other killer | Within reach, not behind the heater (→ 29-12) |
| Hearth gate or barrier | Keeps children off hot surfaces | |
| Heater sold for indoor use, its manual, its fuel | Supplemental heat | → 08-09, → 08-10, → 28-04 |
| Safe furnace connection, arranged in advance | Unlocks the furnace option | → 09-04, → 30-08 |
| Heavy extension cord rated for the furnace load | Power station or generator to furnace | |
| Hot-water bottles | Heat the bed, not the room | |
| Wool blankets, cold-rated sleeping bags | Passive warmth | → 08-06 |
| Thermometer | Know if the room is improving | |

**No gear?** Heated stones from an outdoor fire, wrapped thickly in cloth. Water jugs as thermal
mass. Insulation from cardboard, foam, rugs, bubble wrap and newspaper.

## When it runs out

- **Count your fuel:** propane cylinders, kerosene gallons, cords of wood (you have listed
  {{ gear.fuel.propane_20lb }} 20-lb propane tanks, {{ gear.fuel.kerosene_gal }} gallons of
  kerosene, {{ gear.fuel.firewood_cords }} cords of wood). Write the hours each gives on → 23-02,
  using the runtimes on → 08-09 and → 08-10.
- **Ration:** heat the room while awake; shrink the space (→ 08-01, → 08-06) before burning more.
- **Resupply:** wood is the most findable fuel in a long outage (→ 06-04); propane and kerosene
  are not. Plan the move to wood and insulation.
- **The endpoint:** with no fuel, survival is insulation, layers, body heat and a very small
  shelter. That is why → 08-06 is not a curiosity.

## Phase notes

- **A (at home):** furnace bursts if it can be safely connected, heated-blanket nights,
  insulation always, a portable heater as backup, one at a time, alarm first.
- **B (moving):** **no unvented burner in a vehicle or tent while sleeping.** Warmth is layers and
  insulation (→ 11-01).
- **C (established somewhere else):** a properly installed, inspected wood stove is the goal
  (→ 08-08).

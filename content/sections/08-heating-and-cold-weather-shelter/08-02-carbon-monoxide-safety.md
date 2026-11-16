---
id: 08-02-carbon-monoxide-safety
section: 08-heating-and-cold-weather-shelter
title: "Carbon monoxide: the silent killer"
version: 2
revised: 2026-11-16
layer: core
danger_level: critical
phase: [A, B, C]
tags: [carbon monoxide, CO alarm, generator, heater, ventilation, poisoning, winter]
derived_from: [08-02-carbon-monoxide-safety]
sources:
  - cdc-carbon-monoxide-poisoning-basics-772153
  - cdc-winter-weather-before-during-and-after-13bbd5
  - cpsc-carbon-monoxide-fact-sheet-e97206
  - cpsc-carbon-monoxide-questions-and-answers-783766
  - epa-carbon-monoxide-s-impact-on-indoor-air-quality-a995e7
  - first-alert-co-alarm-users-manual-m08-0534-r8
  - medlineplus-carbon-monoxide-poisoning-r13
related:
  - 08-01-heating-one-room
  - 08-03-winterizing-the-home
  - 08-04-emergency-heat-options
  - 08-06-improvised-shelter-warmth
  - 08-07-ducted-heater-operation
  - 08-08-wood-heat-operation
  - 08-09-portable-propane-heaters
  - 08-10-wick-kerosene-heaters
  - 07-05-propane-and-camp-stoves
  - 09-04-generators
  - 06-09-chimney-and-creosote
  - 20-04-teaching-kids-the-plan
  - 22-05-kit-vehicle
  - 29-03-ex03-carbon-monoxide
  - 29-12-ex12-extinguishers-blankets-and-alarms
  - 30-01-the-floors
  - 30-02-dc01-unvented-heater-overnight
  - 30-21-dc20-open-flame-indoors
  - 30-22-dc21-uninspected-fireplace-or-stove
  - 08-05-hypothermia-frostbite
  - 11-01-cold-weather-layering
  - 29-14-ex14-reading-a-label
cards: [DC-01, DC-20, DC-21]
explainers: [EX-03, EX-12]
promote_when: [is.cold_winters, has.unvented_heater, has.generator, has.gas_any]
photo_slots:
  - { id: co-alarm-warm-room, caption: "The CO alarm in the warm room: opposite wall from the heater, at pillow height" }
  - { id: co-alarm-other, caption: "Our other CO alarms: one per level and outside each sleeping area" }
  - { id: exhaust-vents, caption: "Our furnace, water heater and dryer exhaust vents outside, to clear after snow" }
figures: [fig-co-alarm-placement]
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: { date: "2026-11-16", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "UL 2034 table now cites a maker manual (not CPSC); EPA 9 ppm (not on the EPA page) replaced by EPA home levels; CPSC symptom bands and placement re-read; placement details traced to the First Alert manual; delayed effects per MedlinePlus; matches 29-03." }
---

# Carbon monoxide: the silent killer

**What this page is for.** Carbon monoxide (CO) is the gas that kills families in cold
outages. This page explains it in a few lines (the full explainer is → 29-03), sets out the rules
for every kind of fuel-burning device, tells you where to put CO alarms and what their numbers
mean, and gives the step-by-step for a suspected poisoning, including what to do when no one
answers 911. It outranks every other heating page.

> **SAFETY.** **Never run a generator, charcoal, or any engine indoors, in a garage, or near an
> open window.** Carbon monoxide kills in minutes with no warning; alarms fail; there is no
> mitigation that works every time (→ 30-01). **Fuel is never stored or transferred near an
> open flame or a running appliance** (→ 30-01). CO cannot be seen, smelled or tasted. More
> than 400 Americans die from unintentional CO poisoning each year, and people who are asleep
> or drunk can die before they ever feel ill (CDC, Carbon Monoxide Poisoning: Basics).

## Do this now

1. **Put battery CO alarms on every level of the home and outside each sleeping area** (CPSC),
   and one in the warm room at pillow height (→ 30-02). Test each one. You have listed {{ gear.co_alarms }}.
2. **Never use a gas oven or range to heat the house.** It is not a heater (CDC).
3. **Never use a camp stove, grill or charcoal indoors** (CDC; → 07-05).
4. **Generators outdoors only, more than 20 feet from any window, door or vent** (CDC; → 09-04).
5. **Know the signs:** headache, dizziness, weakness, upset stomach, vomiting, chest pain,
   confusion. They feel like flu (CDC). **If several people, or the pets, feel ill at once and
   better outdoors, get everyone out into fresh air now.**

## What CO is, in brief

Anything that burns fuel makes CO: furnaces, water heaters, stoves, portable heaters,
fireplaces, generators, vehicles, charcoal (CDC). It takes the place of oxygen in your blood. The
first symptoms are the same as flu, so people lie down to rest and do not get up.

**Who is hurt first.** CDC names infants, older adults, and people with chronic heart disease,
anaemia or breathing problems as higher risk (CDC). One CO alarm maker's manual adds that young
children and pets may be the first affected (First Alert, CO alarm user's manual). {{#if has.young_child}}Your household has a child under 6: if a child
is unusually sleepy or sick while anything is burning indoors, treat it as CO until you know
otherwise.{{/if}}{{#if has.elder}} Your household has an older member, who may show it early
too.{{/if}}

**Why the alarm matters more than your senses.** A sleeping person cannot notice symptoms.
That is the reason for the alarm.

## The grid-down trap

Every winter outage produces the same deaths, in the same order:

1. The power fails and the house gets cold.
2. Someone puts the generator in the garage "out of the snow", or lights charcoal in the
   fireplace, or runs the camp stove indoors "just to take the chill off".
3. Everyone gets sleepy.
4. Nobody wakes up.

**Outdoor equipment stays outdoors.** An outdoor fire pit, a grill or a generator is exactly right
outside and deadly inside.

## Rules by device

| Device | Indoors? | Rule |
|---|---|---|
| Portable generator | **Never** | Outdoors, more than 20 ft from windows, doors and vents (CDC); floor rule (→ 30-01; → 09-04) |
| Charcoal or a charcoal grill | **Never** | Outdoors only; floor rule (→ 30-01) |
| Any engine, including a vehicle | **Never** in a garage, even with the door open | Floor rule (→ 30-01) |
| Gas camp stove | **Never** | Outdoors (→ 07-05) |
| Gas oven or range used as a heater | **Never** | It is not a heater (CDC) |
| Portable propane or kerosene heater **sold for indoor use** | Yes, by its manual | Its manual's air openings; CO alarm first; one at a time; an adult awake in the room. Overnight use is a decision card: {{choice DC-01}} (→ 30-02). → 08-09, → 08-10 |
| Ducted diesel or kerosene heater | Yes, if intake and exhaust are both sealed and outside | CO alarm in the room anyway (→ 08-07) |
| Installed fireplace or wood stove | Yes, if the chimney is sound and clear | Inspect before use: {{choice DC-21}} (→ 30-22; → 08-08) |
| Candles and oil lamps | A decision card | {{choice DC-20}} (→ 30-21) |

## The numbers: what a CO reading means

An alarm with a digital readout turns CO into a number, in **parts per million (ppm)**: how many
CO molecules there are in every million molecules of air (→ 29-03). Three published sets of
figures help you read it.

**What the home alarm standard requires.** UL 2034, as printed in a First Alert CO alarm manual
(CPSC says alarms are designed to sound before levels become life-threatening):

| CO level | What the alarm standard requires |
|---|---|
| 30 ppm, steady | No alarm, even after 30 days |
| 70 ppm | Alarm within 1 to 4 hours |
| 150 ppm | Alarm within 10 to 50 minutes |
| 400 ppm | Alarm within 4 to 15 minutes |

**What the levels do to people** (CPSC, Carbon Monoxide Questions and Answers): long exposure at
about 1 to 70 ppm usually causes no symptoms, though people with heart disease may get more chest
pain. Sustained above 70 ppm, symptoms become noticeable: headache, tiredness, nausea. Sustained
at 150 to 200 ppm, disorientation, unconsciousness and death are possible.

**What ordinary homes read** (EPA, Carbon Monoxide's Impact on Indoor Air Quality): 0.5 to 5 ppm
in homes without gas stoves; 5 to 15 ppm near a properly adjusted gas stove; 30 ppm or more near a
badly adjusted one.

**What to do with a reading.** This table is deliberately cautious:

| Reading | What to do |
|---|---|
| **Steady, above the ordinary-home levels, alarm silent** | Something is making CO. **A silent alarm is not proof of safety.** Ventilate, check every burning appliance and flue, and do not sleep with an unexplained steady reading |
| **30 to 70 ppm** | A source is running and winning, often with no symptoms yet, which is the trap. Ventilate now; find and shut off the source. Nobody sleeps until it reads low and the cause is known |
| **Alarm sounding, or above 70 ppm sustained** | **Everyone out to fresh air;** burning appliances off (one-adult re-entry rule below); air the house fully before anyone returns |
| **150 ppm and higher** | **Leave immediately. Carry the children, count heads, nobody goes back in** |

Two readings deserve special fear: **any reading while people were asleep**, and a **peak on the
alarm's memory you cannot explain**. Both mean you find the source before the next night.

## Where the alarms go

- **Minimum:** one on every level and one outside each sleeping area (CPSC). With only one
  alarm, it goes where people sleep, which in an outage is the warm room (→ 08-01).
- **Height and placement: follow your alarm's own manual.** Makers differ: one common manual
  allows a wall or a tabletop (First Alert); CPSC says a plug-in outlet or high on the wall, never
  in a kitchen or above a fuel-burning appliance (CPSC). **In the warm room, put it at pillow
  height**, the height of sleeping heads (→ 30-02).
- **Distance from the heater.** Many alarm manuals give a minimum distance from fuel-burning
  appliances; one common manual says 20 feet from a furnace or other fuel-burning heat source
  (First Alert). A small warm room often cannot meet it. Then put the alarm on the **wall opposite the heater, at pillow height, never directly
  above it**, and treat a short alarm at lighting as "ventilate and check", never as "pull the
  battery". An alarm pulled for being annoying is not there at 3 a.m.
- **Never in still-air or blowing-air spots:** not within 4 inches of the corner where wall meets
  ceiling, not where curtains or furniture can cover it, not near a fan, heat vent or open window,
  because blowing air can keep CO from reaching the sensor (First Alert; CPSC). A heater's cracked
  window or air openings count: keep the alarm away from them.
- **Not in bathrooms or above heat sources:** one common manual says at least 10 feet from a bath
  or shower, because constant high humidity or heat can shorten the sensor's life (First Alert).
- **Battery alarms only count in an outage.** A plug-in alarm with no battery backup is useless
  when the power is out.

{{figure fig-co-alarm-placement}}

{{photo co-alarm-warm-room}}

{{photo co-alarm-other}}

**Blocked vents are the quiet version of this.** Snow drifting over a furnace, water heater or
dryer vent, or a bird's nest in a chimney, sends exhaust back into the house. **After every heavy
snow, clear the outside exhaust vents.**{{#if has.gas_any}} Your home has gas service, so this
applies to your furnace and water heater vents.{{/if}}

{{photo exhaust-vents}}

## If you suspect CO

1. **Get everyone outside into fresh air immediately,** pets included.
2. **Do not go back in** to open windows or look for the source first. Out, then think.
3. **Call 911** if it works. CO poisoning needs medical care; some effects are delayed.
4. **Do not go back in** until the source is found and shut off and the house is aired out.
5. **Count heads.** Confusion is a symptom: someone affected may not follow instructions.

**If there is no 911:**

- **Fresh air is the field treatment** (MedlinePlus, Carbon monoxide poisoning). There is no home
  antidote. Hospitals give oxygen; the household version is time in clean air. Keep everyone outside, **resting** (exertion makes it
  worse), warm (→ 08-05), for hours, not minutes. A safely parked vehicle running outdoors with
  a clear tailpipe, or a neighbour's house, can be the warm spot.
- **Anyone who was confused, staggering, vomiting or unconscious** gets the longest rest and a
  watcher. Permanent brain damage can follow, and impaired thinking can come back after one to two
  weeks without symptoms (MedlinePlus). Write down
  who was exposed and how badly, in case care becomes reachable.
- **One clear-headed adult goes back in**, briefly, holding their breath, with doors open, to shut
  off the source and open windows. The house then airs out until the alarm is silent on fresh
  batteries before anyone sleeps in it.
- **Find the cause before the next night.** The stove, flue or heater that did it will do it
  again. The alarm going quiet is not a diagnosis.

## Gear

| Item | Why | Notes |
|---|---|---|
| **Battery CO alarms**: every level, outside sleeping areas, the warm room | The only thing that detects CO | Test as its manual says (one common manual: weekly); the test button checks the circuit, not the sensor (CPSC); replace at the end-of-life date printed on the unit, and at once on an end-of-life chirp |
| CO alarm with a **digital peak readout** | Shows what happened while you slept | CDC suggests considering one |
| A deep supply of the alarms' batteries | Alarms fail silent without them | Check twice a year (CDC) |
| Heavy outdoor extension cord, 25 ft or more | Lets the generator sit 20+ ft from the house | Rated for the load (→ 09-04) |
| Chimney inspection or brush | A blocked flue makes CO and fire | → 06-09 |
| A snow shovel by the vent side of the house | Clear vents after storms | |
| The manual for every fuel-burning heater | "Sold for indoor use" is on the label, not a guess | → 29-14 |

**There is no substitute for a CO alarm.** No sense, no plant, no rule of thumb detects CO. If you
have exactly one, it goes where people sleep. Ventilation helps, but a cracked window does not
make an unsuitable burner safe indoors.

## When it runs out

- **Alarms run out twice:** batteries, and the sensor itself, which expires at the date printed
  on the unit even if never used. Write that date here: ____________. Keep spares.
- **Never ration alarms away from sleepers.** One working alarm goes where people sleep.
- **The rule that never runs out:** nothing that burns fuel comes inside except heaters sold for
  indoor use, run by their manuals, and never those without a working alarm. Teach it to the whole
  family (→ 20-04).

## Phase notes

- **A (at home):** the highest-risk phase. There is a garage, a generator, a grill and a cold
  house. Most CO deaths happen here.
- **B (moving):** never run a vehicle in an enclosed space to keep warm, and never bring a stove
  into a tent or car to sleep. Warmth comes from insulation and layers (→ 11-01). A stranded car
  in snow: clear the tailpipe first (→ 22-05).
- **C (established somewhere else):** an unfamiliar stove or heater is an unknown. Inspect the
  flue before first use, and put an alarm in the sleeping room on day one.

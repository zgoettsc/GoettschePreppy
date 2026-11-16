---
id: 29-03-ex03-carbon-monoxide
section: 29-explainers
title: "Carbon monoxide: the gas you cannot see or smell"
version: 2
revised: 2026-11-16
layer: explainer
danger_level: critical
phase: [A, B, C]
tags: [carbon monoxide, CO, CO alarm, generator, heater, charcoal, explainer, safety]
derived_from: [08-02-carbon-monoxide-safety, 09-04-generators]
sources: [cdc-carbon-monoxide-poisoning-basics-772153, cpsc-carbon-monoxide-questions-and-answers-783766, cpsc-carbon-monoxide-fact-sheet-e97206, epa-carbon-monoxide-s-impact-on-indoor-air-quality-a995e7, us-consumer-product-safety-commission-cpsc-what-to-k-3390a4, cdc-winter-weather-before-during-and-after-13bbd5, first-alert-co-alarm-users-manual-m08-0534-r8]
related: [08-02-carbon-monoxide-safety, 08-01-heating-one-room, 08-04-emergency-heat-options, 09-04-generators, 07-05-propane-and-camp-stoves, 29-01-ex01-fuels, 30-01-the-floors, 30-02-dc01-unvented-heater-overnight, 30-03-dc02-propane-cylinder-indoors, 30-21-dc20-open-flame-indoors]
cards: [DC-01, DC-02, DC-20]
explainers: [EX-01]
promote_when: [experience.new]
photo_slots:
  - { id: co-alarm-spot, caption: "Where our CO alarms are mounted, and the date printed on each" }
figures: []
plates: []
condition: null
gear: null
explainer: EX-03
card: null
review_pass: { date: "2026-11-16", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "UL 2034 alarm points now cite a manufacturer manual that prints them (CPSC pages read do not); EPA 9 ppm (not on the EPA page cited) replaced by that page's own indoor figures; CDC 400 deaths/100,000 ED visits, CPSC placement and 20 ft re-read." }
---

# Carbon monoxide, explained from the beginning

**What this page is for.** Every winter power outage kills families who brought a generator,
grill or stove inside to stay warm. They die from carbon monoxide. This page says what it is,
where it comes from, why your senses will not warn you, what an alarm does and does not do, and
what to do if you suspect it.

> **SAFETY — the floor that applies (→ 30-01).** **Never run a generator, charcoal, or any
> engine indoors, in a garage, or near an open window.** Carbon monoxide kills in minutes with no
> warning; alarms fail; there is no mitigation that works every time.

## What it is

**Carbon monoxide (CO)** is a gas made whenever a fuel burns: gasoline, diesel, kerosene,
propane, natural gas, wood, charcoal (→ 29-01). It has **no colour, no smell and no taste**
(CDC). When you breathe it, it takes the place of oxygen in your blood, so the body slowly
starves of oxygen. More than 400 Americans die each year from CO poisoning that is not caused
by fire, and more than 100,000 go to an emergency room (CDC, Carbon Monoxide Poisoning: Basics).

## Where it comes from in a house

Furnaces, water heaters, gas ranges, fireplaces and wood stoves, portable generators, charcoal
grills, camp stoves, kerosene and propane heaters, and cars. A properly vented appliance sends
its CO up a flue or chimney. **Trouble starts when the exhaust stays in the room**: a generator
or grill brought inside, a camp stove used indoors, a blocked chimney, or a vent buried by snow.

## Why you will not notice it

The first symptoms feel like flu: **headache, dizziness, weakness, upset stomach, vomiting,
chest pain, confusion** (CDC). People feel tired, lie down, and do not wake up. **People who are
asleep or drunk can die from CO before they have any symptoms** (CDC). Infants, older adults, and
people with heart or lung disease or anaemia are hurt first and worst (CDC). A clue: several
people, or the pets, feel ill at the same time and feel better outdoors.

## What a CO alarm does and does not do

An alarm measures CO in **parts per million (ppm)**: how many CO molecules there are in every
million molecules of air. Alarms are designed to stay **silent at low levels** so they do not
go off constantly. The home CO alarm standard, UL 2034, sets these alarm points (as printed in
a First Alert CO alarm manual; CPSC says alarms are designed to sound before levels become
life-threatening):

| CO level | What the alarm standard requires |
|---|---|
| 30 ppm, steady | No alarm, even after 30 days |
| 70 ppm | Alarm within 1 to 4 hours |
| 150 ppm | Alarm within 10 to 50 minutes |
| 400 ppm | Alarm within 4 to 15 minutes |

For comparison, homes without gas stoves average 0.5 to 5 ppm, and the air near a properly
adjusted gas stove 5 to 15 ppm (EPA, Carbon Monoxide's Impact on Indoor Air Quality). So **a
quiet alarm is not proof the air is clean**, and a reading that stays above those levels means something
is making CO. An alarm with a number display tells you more than one that only beeps.

- **Where:** on every level of the home and outside each sleeping area (CPSC). In a room where
  people sleep near a heater, at the height of sleeping heads, on the wall away from the heater,
  not in a dead-air corner, not next to an open window. The alarm's own manual gives the height.
- **Power:** battery or battery backup (CDC). A plug-in alarm with no battery does nothing in an
  outage.
- **Replace** the alarm at the end-of-life date printed on it, and at once if it chirps that it
  has reached end of life.
- **An alarm is a backup, not permission.** It can fail, have a dead battery, or be in the wrong
  room. It does not make a generator in the garage safe.

## If you suspect CO

1. **Get everyone outside into fresh air now**, pets included. Do not stop to open windows or
   look for the cause.
2. **Call 911** if it works. CO poisoning needs medical care; some effects show up later.
3. **Count heads.** Confusion is a symptom; someone may not follow you out.
4. **Nobody goes back in** until the source is found and shut off and the house is aired out.
5. **No 911:** fresh air is the treatment. Keep everyone outside, warm and resting, for hours,
   with someone watching anyone who was confused, vomiting or passed out. The full offline
   procedure is on → 08-02.

## Rules that follow from this

- Generators run **outdoors only, at least 20 feet from the house**, exhaust pointed away
  (CPSC, Portable Generator Safety). Never in a garage, even with the door open.
- **Never** burn charcoal indoors. **Never** heat the house with a gas oven or range. **Never**
  use a portable camp stove indoors (CDC).
- **After heavy snow**, clear the snow from furnace, water-heater and dryer vents.

## Decisions on this page

- An unvented heater running while people sleep: {{choice DC-01}} → 30-02
- A propane cylinder larger than 1 lb inside: {{choice DC-02}} → 30-03
- Open-flame cooking or candles indoors: {{choice DC-20}} → 30-21

## This household

CO alarms on hand: {{ gear.co_alarms }}.
{{#if has.unvented_heater}}You have a portable heater that vents into the room. Install and test
the alarms before it is lit the first time. → 08-01{{/if}}
{{#if has.generator}}You have a generator. Mark its outdoor spot now, at least 20 feet out. → 09-04{{/if}}

{{photo co-alarm-spot}}

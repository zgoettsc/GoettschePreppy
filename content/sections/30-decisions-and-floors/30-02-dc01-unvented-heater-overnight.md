---
id: 30-02-dc01-unvented-heater-overnight
section: 30-decisions-and-floors
title: "DC-01. An unvented heater running while people sleep"
version: 1
revised: 2026-11-16
layer: card
danger_level: critical
phase: [A, C]
tags: [decision card, heater, unvented, propane, kerosene, carbon monoxide, sleep, overnight]
derived_from: [08-01-heating-one-room, 08-02-carbon-monoxide-safety, 08-09-mr-heater-buddy, 08-10-dyna-glo-kerosene-heater, 21-07-sleep, 11-02-keeping-kids-warm]
sources:
  - cdc-carbon-monoxide-poisoning-basics-772153
  - cpsc-carbon-monoxide-fact-sheet-e97206
  - cpsc-carbon-monoxide-questions-and-answers-783766
  - enerco-group-mr-heater-manufacturer-portable-buddy-r-759ce5
  - ghp-group-inc-dyna-glo-manufacturer-portable-kerosen-477cfd
  - university-of-missouri-extension-unvented-portable-k-e850fe
  - cdc-preventing-hypothermia-c53e0c
related: [08-01-heating-one-room, 08-02-carbon-monoxide-safety, 08-04-emergency-heat-options, 08-09-portable-propane-heaters, 08-10-wick-kerosene-heaters, 21-07-sleep, 11-02-keeping-kids-warm, 29-01-ex01-fuels, 29-03-ex03-carbon-monoxide, 30-01-the-floors]
cards: [DC-01]
explainers: [EX-01, EX-03]
promote_when: [has.unvented_heater, is.cold_winters]
card: DC-01
options:
  - id: never
    label: "Never while anyone sleeps"
    summary: "The heater is off and confirmed out before anyone sleeps. Warmth overnight comes from one small room, shared body heat, layers, sleeping bags and pre-warmed beds."
  - id: alarm-and-wake
    label: "Lowest setting, alarm, vents, barrier, 3-hour wake"
    summary: "Lowest safe setting; tested CO alarm at pillow height installed first; the manual's vents open; heater behind a barrier; one adult wakes every 3 hours to check flame and alarm; headache or nausea means everyone out."
  - id: run-it
    label: "Run it with alarms and vents"
    summary: "The heater runs overnight with a tested CO alarm in the room and the manual's vents open, but no one is set to wake and check it."
settings_summary: "Portable propane and kerosene heaters sold for indoor use are 'unvented': their exhaust, including carbon monoxide (CO), stays in the room. Both common types' manuals say never run them while you sleep. CO has no smell; CDC says sleeping people can die before they feel any symptom, and children are affected first. Fire from bedding or a tipped heater is the second risk. What helps most: heater off while people sleep (removes the risk); a tested CO alarm at pillow height, the manual's vent openings, the lowest correct flame, a barrier, and an adult who wakes every 3 hours to check (reduces it a lot). The cost of 'never' is a cold night, which matters most for babies and frail elders in deep cold."
review_pass: null
---

# DC-01. An unvented heater running while people sleep

**What this page is for.** In a winter outage the coldest hours are the sleeping hours. This
card explains what can go wrong when a portable fuel heater keeps burning while everyone is
asleep, why the makers say never do it, and what the household decides. The choice box at the
bottom is the household's answer; every heater page points here.

> **SAFETY.** Never run a generator, charcoal, or any engine indoors, in a garage, or near an
> open window. That is a floor (→ 30-01), not this card. This card is only about heaters sold
> for indoor use. If a CO alarm sounds, or anyone wakes with a headache, dizziness or nausea:
> heater off, everyone out into fresh air, → 08-02.

## 1. The thing, in plain words

A **portable fuel heater** burns propane (the gas in grill tanks) or kerosene (a clear liquid
fuel, → 29-01) to make heat. **Unvented** means it has no chimney or pipe to the outside. Its
exhaust stays in the room you are in. That exhaust includes **carbon monoxide (CO)**, a gas you
cannot see or smell that stops your blood from carrying oxygen (→ 29-03). The heater also uses
up the oxygen in the room and adds water vapour.

Some propane heaters have an **oxygen depletion sensor (ODS)**: it shuts the heater off when
the room's oxygen drops. It does **not** measure CO. Most wick kerosene heaters have no ODS at
all.

{{#if has.unvented_heater}}Your household listed these heaters: {{#each heaters as h}}{{h.kind_text}}; {{/each}}CO alarms on hand: {{ gear.co_alarms }}.{{else}}Your household has not listed a portable fuel heater. Read this card anyway: a borrowed or scavenged heater raises the same question.{{/if}}

## 2. The rule, and why the makers set it

- The owner's manual of one widely sold indoor-rated propane heater says, in capitals,
  **never operate the heater while sleeping**, and requires fresh-air openings high and low in
  the room while it burns (Enerco/Mr. Heater, portable propane heater owner's manual).
- A common wick kerosene heater's manual says never leave it unattended and turn it off and
  check that it is out **before going to bed** (GHP Group/Dyna-Glo, Portable Kerosene Heater
  owner's manual).
- University of Missouri Extension warns that unvented kerosene heaters raise indoor CO and
  other pollutants, more so in small closed rooms (MU Extension, Unvented Portable Kerosene
  Heaters, G1999).

**Why:** a sleeping person cannot notice a flame going wrong, a blanket falling on the heater,
or the first signs of CO. The makers cannot see your room, your fuel or your ventilation, so
they draw the line where a sleeping person is never the only safety system.

## 3. How it actually hurts people

The usual sequence: the house is cold, so the family closes the warm room tightly. The heater
is turned down to save fuel. On a wick heater a turned-down or tarred wick burns badly and
makes more CO (manufacturer's manual). Over several hours the CO level climbs. Children and
anyone with heart or lung disease feel it first (CDC). Everyone gets drowsy, which feels like
ordinary sleep. **CDC says people who are asleep can die from CO before having any
symptoms** (CDC, Carbon Monoxide Poisoning: Basics).

The second path is fire: bedding, clothes drying nearby, or a curtain within the heater's
clearance, or a heater knocked over in the dark.

The other side is real too. A very cold room can hurt a baby or a frail elder, and CDC lists
infants sleeping in cold bedrooms and older adults among the people most at risk of
hypothermia (CDC, Preventing Hypothermia). {{#if is.cold_winters}}Your home's January average
low is about {{ region.home.jan_low_f }} °F, so this is a real question for your household.{{/if}}

## 4. What makes it safer

**Removes the risk**
- Heater off and confirmed out before anyone sleeps. Keep warm by other means: everyone in
  one small room, shared body heat, dry layers and hats, sleeping bags, a warm drink and food
  before bed (→ 08-01, → 21-07). Hot-water bottles pre-warm a bed and come out before a child
  gets in; skin that is asleep burns without waking (→ 11-02).

**Reduces it a lot**
- A **tested, battery CO alarm in the room at the height of sleeping heads**, opposite the
  heater, installed before the heater is ever lit (→ 08-02). No alarm, no overnight heater.
- The **manual's ventilation**, open the whole time: for the propane heater above, an opening
  of 9 square inches high and another low; for the kerosene heater above, a window open at
  least 1 inch in a small room (each manufacturer's manual). Your heater's manual sets its own.
- A heater **with an ODS** rather than one without.
- The **lowest correct setting**: low on a propane heater; on a wick heater, the flame height
  the manual specifies, never turned down below it.
- **One adult wakes about every 3 hours** to look at the flame, the alarm and the openings.
- The heater **behind a barrier** on the far side of the room, with the manual's clearances.

**Reduces it a little**
- Fill the kerosene tank before bed so it does not run dry and smoke at 3 a.m.
- A second CO alarm elsewhere in the house.
- A standing rule: **anyone who wakes with a headache or nausea means everyone out.**

## 5. The options

**`never`: Never while anyone sleeps.**
You give up: overnight heat. On the coldest nights the room may fall well below comfortable,
and you must manage the cold with bodies, layers and bedding. You accept: a cold night.

**`alarm-and-wake`: Lowest setting, alarm, vents, barrier, 3-hour wake.**
You give up: the manuals' rule, and an adult's unbroken sleep every night it runs. You accept:
that the alarm and the wake checks are what stand between the family and CO, and that on a
heater without an ODS they are the only things watching.

**`run-it`: Run it with alarms and vents.**
You give up: the manuals' rule and the human check. You accept: that if the alarm fails, is
placed wrong or sleeps through a slow rise, nobody is awake to notice. This is the riskiest
option.

## 6. Our choice

{{card DC-01}}

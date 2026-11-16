---
id: 27-02-emp-and-geomagnetic-storm
section: 27-cbrn-and-emp
title: "EMP and geomagnetic storms: what actually happens"
version: 1
revised: 2026-11-16
layer: core
danger_level: caution
phase: [A, B, C]
tags: [EMP, geomagnetic storm, space weather, solar storm, grid failure, NOAA, early warning]
derived_from: [27-02-emp-and-geomagnetic-storm]
sources:
  - noaa-space-weather-prediction-center-noaa-space-weat-038109
  - noaa-space-weather-prediction-center-noaa-space-weat-10d973
  - noaa-national-weather-service-noaa-weather-radio-all-5f13d8
  - american-red-cross-power-outage-safety-6d07a8
related: [27-01-how-to-think-about-this, 27-03-protecting-electronics, 17-08-power-grid-failure, 09-01-power-priorities, 09-10-power-for-medical, 15-01-weather-alerts, 23-02-master-consumables-table, 00-06-first-60-minutes, 09-16-outage-day-one]
cards: []
explainers: [EX-02, EX-09]
promote_when: []
photo_slots: []
figures: []
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: null
---

# EMP and geomagnetic storms: what actually happens

**What this page is for.** Two very different things get called "EMP". This page explains both,
prints NOAA's storm scale, and says what to do with the one real early warning you can get. The
short version: **the reliable result of every scenario here is that the grid goes away and stays
away**, which the rest of this binder already plans for.

> **Caution.** What is **not** predictable is which individual devices survive. **Plan for the
> outage, not for a particular pattern of gadget failure**, and be sceptical of anyone who tells
> you exactly what will and will not work.

## Do this now

1. **Know that the likely version is watched and forecast.** NOAA's Space Weather Prediction
   Center issues public watches and warnings for geomagnetic storms. That is a real early-warning
   channel; there is none for a weapon (→ 15-01).
2. **Do the electronics protection on → 27-03** for the devices someone in your household
   depends on{{#if has.condition.CL-02}} (the pump, the sensor, a backup meter){{/if}}{{#if has.cpap}} (the CPAP){{/if}}{{#if has.oxygen}} (oxygen equipment){{/if}}.
3. {{#if has.condition.CL-02}}**Practise the injection backup** (→ 02-02). It answers every electronics-failure scenario
   and needs no power at all.{{else}}**Give every device you depend on a non-electronic backup** (→ 27-03), and practise using
   it.{{/if}}
4. **Treat the rest as a grid failure**, because that is what it is: → 17-08, → 09-01, → 23-02.

## Two different things get called "EMP"

| | **Geomagnetic storm (space weather)** | **High-altitude EMP** |
|---|---|---|
| **Cause** | The sun: a burst of charged particles (a coronal mass ejection) hitting Earth's magnetic field | A nuclear weapon set off high in the atmosphere |
| **How likely** | **Recurring.** NOAA expects about 4 G5 storms per 11-year solar cycle | Low, and needs a nuclear attack |
| **Warning** | **Yes: hours to days**, from NOAA | None |
| **Main way it does damage** | Currents pushed into **very long conductors**: power lines, pipelines, and the large transformers at their ends | A fast pulse into electronics and wiring, plus the same long-line effects |
| **Household electronics** | Mostly not affected directly; you lose power because the grid does | Unpredictable; published claims vary wildly |

**The practical point:** both end in the same place for you: **no grid, possibly for a long time,
possibly over a wide area.** This binder already treats that as its starting point.

## The NOAA scale, in NOAA's words

NOAA rates geomagnetic storms from **G1 (minor) to G5 (extreme)** (NOAA Space Weather Prediction
Center, NOAA Space Weather Scales):

| Scale | Effect on the power system | About how often, per 11-year cycle |
|---|---|---|
| **G1** minor | Weak power-grid fluctuations | about 1,700 |
| **G2** moderate | Voltage alarms in high-latitude power systems; long storms can damage transformers | about 600 |
| **G3** strong | Voltage corrections may be needed; false alarms on some protection devices | about 200 |
| **G4** severe | *"Possible widespread voltage control problems and some protective systems will mistakenly trip out key assets from the grid."* | about 100 |
| **G5** extreme | *"Widespread voltage control problems and protective system problems can occur, some grid systems may experience complete collapse or blackouts. Transformers may experience damage."* | **about 4** |

**Read the last row honestly, both ways.** A G5 is not science fiction: it happens several times
a solar cycle. And its stated effect is *blackouts and transformer damage*, not the end of
technology.

## Why "which devices survive" is the wrong question

You will find confident, contradictory lists. They disagree because the answer depends on the
event, the device, whether it is plugged into the mains or a long antenna, whether it is switched
on, and where it sits. **Nobody can give you a reliable list.**

So do not plan around one. Plan around the two things that are reliable:
1. **The grid is gone**, over a possibly large area, possibly for a long time. Repair is slow
   because everyone needs the same parts (→ 23-04).
2. **Anything you depend on needs a non-electronic backup**: {{#if has.condition.CL-02}}injections
   instead of the pump (→ 02-02), a simple glucose meter, {{/if}}paper copies of documents
   (→ 19-01), and this binder installed on more than one device (→ 00-10).

## What a long, wide-area outage changes

The honest difference between "the power is out" and these scenarios:
- **It is regional, not local.** No repair crews coming from the next state, because the next
  state has the same problem. Neighbours matter more, not less (→ 18-01).
- **Repair is slow.** Large transformers are built to order and take a long time to make.
- **Fuel stops moving** once pumps and card payments are down (→ 06-06, → 22-05).
- **Water and sewage run on electricity.** Town water may fail or lose pressure (→ 03-02)
  {{#if has.well}}, and your well pump stops (→ 03-10){{/if}}.
- **Nothing else about your day changes.** You still need water, heat, food, medicine and
  sanitation, in that order: the whole binder.

## The one early warning worth knowing

For **space weather only**, there is real forecasting:
- **NOAA's Space Weather Prediction Center** issues public watches, warnings and alerts. News and
  weather services usually pass on the big ones (→ 15-01).
- A **G4 or G5 watch** is the one realistic case in which you get hours to days of notice that a
  serious grid event may be coming.
- **What to do with that notice:** top up stored water (→ 03-02), fill the vehicles' tanks
  (→ 22-05), charge every power bank, power station and medical device (→ 09-10), and count the
  medicines (→ 23-02). It is the same two-hour routine as any storm warning (→ 00-06).
- **Unplugging is a household judgement, not an agency instruction.** NOAA's scale describes
  effects on the **grid**; no agency tells households to unplug anything for a geomagnetic storm.
  Some households choose to unplug fully charged power stations and non-essential electronics
  during a G4 or G5 watch, as a cheap hedge: a full battery gains nothing by staying plugged in.
  {{#if has.refrigerated_meds}}If you do, the medicine cooler then runs on the station's battery:
  know how many hours that gives you (→ 09-10) and plug back in when NOAA ends the watch.{{/if}}
  Near the peak of a solar cycle G4 watches come several times a year; if the hedge costs you,
  keep the top-up and drop the unplugging.

**There is no such warning for a weapon.** Which is another reason routine preparation matters
more than scenario gear.

## What you need

| Item | Why | Notes |
|---|---|---|
| **Battery or hand-crank NOAA Weather Radio** | Already needed (→ 15-01); also your news source here (NOAA, NOAA Weather Radio All Hazards) | Buy it for storms; it works for this too |
| **Simple backups for medical devices**{{#if has.diabetes}} (a basic glucose meter and strips){{/if}} | Not networked, battery-powered, cheap | → 22-06, → 27-03 |
| **A shielded container for backup electronics** | A cheap hedge for spares | → 27-03; read its honest limits |
| **Power banks and solar** | The medical loads are the ones that matter | → 09-10 |
| Paper copies of key documents and numbers | Paper does not care about any of this | → 19-01 |
| Hand tools, a manual can opener, matches | The general non-electronic backup | → 16-01 |

No money? Vehicles hold batteries and alternators (→ 09-11; engine running outdoors only). Older,
simpler equipment tends to be easier to repair.{{#if has.condition.CL-02}} **The injection backup
replaces the whole electronic diabetes setup** (→ 02-02): that is the substitution that matters
here.{{/if}}

## When it runs out

- **Runway:** in a long, wide-area outage every clock on → 23-02 starts at once, and the shortest
  one governs (→ 23-01).
- **Ration:** power goes first to medical devices, then light, then communications (→ 09-01).
- **Resupply:** none from the grid. Solar and vehicle charging are the only inputs (→ 09-02,
  → 09-11), and winter solar is thin (→ 09-05).
- **Substitute:** the non-electronic way of doing everything: paper, hand tools, manual methods,
  and the binder in front of you.

## By phase

- **A, at home:** shelter in place. This is a services problem, not a danger to the house.
- **B, moving:** a wide-area outage makes travel **harder**: no fuel pumps, no card payments, no
  traffic lights. It weakens the case for leaving (→ 01-02).
- **C, establishing:** a rural place with wood, water and its own power copes with this scenario
  much better than a town lot (→ 23-04).

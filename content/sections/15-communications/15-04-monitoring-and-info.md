---
id: 15-04-monitoring-and-info
section: 15-communications
title: "Monitoring the news, scanning, and judging what you hear"
version: 2
revised: 2026-11-16
layer: core
danger_level: none
phase: [A, B, C]
tags: [scanner, shortwave, AM radio, monitoring, rumours, information, encryption, amateur nets, listening, morale]
derived_from: [15-04-monitoring-and-info]
sources: [us-government-publishing-office-ecfr-47-cfr-part-95-c8b55a, noaa-national-weather-service-noaa-weather-radio-all-5f13d8, noaa-national-weather-service-weather-ready-nation-b0a52f, arrl-the-national-association-for-amateur-radio-what-5edded]
related: [29-09-ex09-radios, 15-01-weather-alerts, 15-02-radio-options, 15-05-ham-and-licensing, 15-06-antennas-and-range, 14-01-situational-awareness, 14-03-opsec, 01-02-go-no-go-decision, 21-01-stress-and-panic, 21-02-long-haul-morale, 21-07-sleep, 20-08-kids-and-fear, 09-01-power-priorities, 09-07-battery-chemistry, 09-11-hand-and-alt-generation, 10-05-light-discipline, 18-01-mutual-aid, 25-03-regional-contacts, 25-05-blank-logs, 25-08-quick-reference-cards, 15-03-family-comms-plan]
cards: []
explainers: [EX-09]
promote_when: []
photo_slots: []
figures: []
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: { date: "2026-11-16", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "Unsourced NWR backup-power claim softened; calling frequencies checked." }
---

# Monitoring the news, scanning, and judging what you hear

**What this page is for.** Listening is the most valuable and least risky thing a radio does. It
costs a little power, it is legal, and unlike transmitting, **it tells nobody you exist**
(→ 14-03). But in a crisis most of what circulates is wrong, exaggerated or out of date, and
constant bad news wears down a household's morale and judgement (→ 21-01, → 21-02). This page is
as much about **filtering and rationing** information as gathering it.

## Do this now

1. **Buy a scanner or a wideband receiver** and learn it before you need it (check first what is
   still listenable in your area; below).
2. **Buy a portable radio with shortwave.** When local sources go dark, shortwave still carries
   regional and world broadcasts, and it needs only batteries and a wire antenna.
3. **Fill in the frequency table below** while the internet still exists. **You will not be able
   to look these up later** (→ 25-03, → 25-08).
4. **Set an information routine now**: twice a day, at set times, for a fixed period. A habit set
   early is what keeps listening from becoming compulsive later.

## The layers, and how they fail

| Layer | What it gives you | How it fails |
|---|---|---|
| **NOAA Weather Radio** | Weather warnings, straight from the NWS (→ 15-01) | Usually among the last to go, but a transmitter can go off the air |
| **Local AM and FM** | Local conditions, official information | Stations run on generators for a while, then fade |
| **AM at night** | Distant stations: AM carries far after dark | Very durable; often the last broadcast standing |
| **Shortwave** | Regional and world broadcasts | **Least dependent on local infrastructure**; no licence to listen |
| **Scanner (public services)** | What is happening locally, right now | Many systems are digital, some encrypted; may go quiet |
| **Amateur bands** | **People on the ground, talking**: often the best real information (→ 15-05) | You need to know where to listen |
| **Internet and cell** | Everything, while it lasts | **Fails first, and early** |

**What to expect:** internet and cell go first; local broadcast lasts a while; **the weather
radio, AM at night, shortwave and amateur radio are what remain**, roughly in that order.

## What a scanner is really for

A scanner tells you what is happening **near you, now**: emergency responses, road closures,
where the problems are. That matters for the decision to stay or go (→ 01-02) and for awareness
(→ 14-01).

**Know before you buy:**

- **Many public-safety systems are digital and "trunked"** (shared among many users by computer).
  Hearing them needs a scanner made for that; an old analogue scanner may hear nothing useful.
- **Many police agencies now encrypt their radio traffic.** Encrypted traffic cannot be heard, and
  trying to decrypt it is unlawful. **No scanner hears it, and no plan should depend on it.** Fire,
  ambulance and state agencies vary: some talk groups stay open.
- **Amateur, marine and aviation bands are open** and are often more informative in a wide-area
  event.
- **The decision:** buy a digital scanner **only if** you have confirmed that local fire, EMS or
  state talk groups are still unencrypted. Otherwise a cheap analogue or wideband receiver covers
  everything else on this page. Our decision and date: ______________________

## The monitoring table (fill it in while the internet exists)

| What | Frequency or channel | Notes |
|---|---|---|
| NOAA Weather Radio, home transmitter | {{#each region.home.nwr as t}}{{t.call}} {{t.freq}} MHz; {{/each}} | → 15-01 |
| Local police and sheriff | ____________ | Encrypted? ☐ yes ☐ no |
| Fire and EMS dispatch | ____________ | Digital? Encrypted? Check |
| State police and state agencies | ____________ | Some talk groups may be open |
| Amateur 2-metre: main local repeater | ____________ | → 15-05 |
| Amateur simplex calling frequencies | **146.520 MHz** (2 m), **446.000 MHz** (70 cm) | National calling channels |
| AM stations that carry far at night | ____________ | Many keep newsrooms on generator power |
| FM local news | ____________ | |
| Aviation emergency frequency | **121.5 MHz** (AM mode) | Emergencies and distress beacons; listen only, never transmit |
| Family GMRS channel and repeater | ____________ | → 15-02, → 15-03 |

Scanner: ☐ owned, model ____________ ☐ not owned.

## Amateur radio as a news source, even unlicensed

**You do not need a licence to listen.** In regional emergencies, amateur operators run
**organised emergency nets**: scheduled, disciplined traffic about real conditions on the ground
(ARRL, What is Ham Radio?). That is often the best information available in a disaster, and
listening is free. Learn where the local repeaters and nets are **now** and write them in the
table (→ 15-05).

## Judging what you hear: the part that matters most

In a crisis, information quality collapses. Ask:

- **Who is saying it, and how do they know?** "I can see the bridge is out" beats "someone said
  the bridge is out" by a huge margin.
- **When did it happen?** Crisis information goes stale in hours.
- **Is it specific?** "The road is flooded at the river crossing this morning" is usable; "the
  roads are bad" is not.
- **Do independent sources repeat it**, or is it one rumour going in circles?
- **Rumours travel faster and farther than facts**, and grow as they travel.
- **Be wary of news that is exactly what you feared, or exactly what you hoped.** Those are the
  stories people pass on without checking.
- **Write down what you hear, with the time and the source** (→ 25-05). Over days, patterns
  appear and rumours fall apart on their own.

## Rationing information

This is not a soft point. In a long crisis:

- **Constant bad news raises anxiety, spoils sleep and worsens decisions** (→ 21-01, → 21-07). It
  also drains batteries.
- **Set fixed listening times**, twice a day, for a set period. **Then turn it off and do the
  day's work.**
- **One adult listens and briefs the others**, rather than everyone soaking in it.
- **Children should not listen to disaster coverage.** {{#if has.young_child}}Young children
  absorb far more than adults think and have no way to make sense of it (→ 20-08).{{else}}Young
  children absorb far more than adults think (→ 20-08).{{/if}}
- **The information you need is usually small:** is the weather dangerous, are the roads passable,
  is help coming, has anything changed near us? A five-minute question, not an all-day one.

## Security

- **Listening is invisible.** Nobody can tell you are listening. That is the whole advantage
  (→ 14-03).
- **Do not repeat on the air what you hear**, and do not confirm details about your own situation.
- **A scanner heard from outside** at night breaks noise discipline (→ 10-05). Use an earpiece.

## Gear

| Item | Why | Notes |
|---|---|---|
| **Scanner** (digital only if it helps where you live) | Local awareness, invisibly | Check what your area's systems need |
| **Portable radio with shortwave** | Survives when local infrastructure does not | Battery or crank; a wire antenna helps a lot |
| AM/FM portable radio | Local official news; AM carries far at night | Cheap, durable |
| NOAA Weather Radio | The alert layer | → 15-01 |
| Earpiece or headphones | Quiet; saves battery | → 10-05 |
| **A written frequency list for your area** | You cannot look it up later | → 25-03, → 25-08 |
| Wire, cable and connectors for receiving antennas | A long wire greatly improves shortwave | → 15-06 |
| Notebook and pencil for an information log | Patterns appear; rumours collapse | → 25-05 |
| Rechargeable AA and AAA cells and a charger | Listening is a small, steady load | → 09-07 |
| Hand-crank radio | Works with no power | → 09-11 |

**If you do not have it:**

- **A vehicle radio** gets AM and FM, and many get the weather band. A car is a listening post
  that runs a long time on its own battery.
- **Old scanners, marine radios, aviation receivers, amateur handhelds**: many receive far more
  than they transmit.
- **A long wire strung outside** is the biggest single improvement to any shortwave receiver
  (→ 15-06). Free.
- **Neighbours** (→ 18-01): someone on the block has a scanner, a licence or a working radio.
  Sharing information is one of the easiest kinds of mutual aid.
- **Your own eyes:** smoke, traffic, aircraft, whether streetlights are on, whether anyone is
  ploughing. What you see yourself is the best information there is (→ 14-01).

## When it runs out

- **Batteries are the only real consumable**, and listening is a small load (→ 09-01). Set
  listening times cut it to almost nothing.
- **What fades is the information itself**, in roughly this order: internet, cell, local
  broadcast, scanner traffic, weather radio, then shortwave and amateur radio. **Plan for the last
  two to be what you have**, and set up to receive them (→ 15-06).
- **In a long event the most reliable information becomes local and first-hand**: what you see,
  and what someone who was there tells you face to face (→ 18-01).
- **The failure to avoid is acting on a rumour**: leaving, trading away supplies, confronting a
  neighbour. **Write it down, wait for confirmation where you can, and prefer what you have seen
  yourself** (→ 01-02, → 14-01).

## By phase

- **A (at home):** the full set works. **Set the routine and the discipline now.** This is also
  when information most affects the stay-or-go decision (→ 01-02).
- **B (on the move):** the vehicle radio, a handheld scanner, and CB for road information
  (→ 15-02). **Route information is what you need**: closures, conditions, where people are
  gathering.
- **C (rural or a new place):** farther from local broadcast, but **far better for receiving**:
  space and height for real antennas (→ 15-06), less electrical noise. A rural site with a good
  wire antenna is a better listening post than a house in town.

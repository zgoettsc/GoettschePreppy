---
id: 15-02-radio-options
section: 15-communications
title: "Radio options: FRS, GMRS, MURS, CB, ham, scanners and satellite"
version: 2
revised: 2026-11-16
layer: core
danger_level: caution
phase: [A, B, C]
tags: [radio, FRS, GMRS, MURS, CB, ham, amateur radio, scanner, repeater, channels, CTCSS, Starlink, satellite, batteries, opsec]
derived_from: [15-02-radio-options]
sources: [us-government-publishing-office-ecfr-47-cfr-part-95-c8b55a, us-government-publishing-office-ecfr-47-cfr-part-97-17b11d, arrl-the-national-association-for-amateur-radio-gett-5839f6, noaa-national-weather-service-noaa-weather-radio-all-5f13d8, starlink-help-center-spacex-how-does-pausing-service-9e1a3f, starlink-spacex-critical-information-summary-starlin-459c04, mobile-internet-resource-center-starlink-changes-in-6d5f78, 5gstore-starlink-kills-in-motion-use-on-5-standby-pl-9c94e5]
related: [29-09-ex09-radios, 15-01-weather-alerts, 15-03-family-comms-plan, 15-04-monitoring-and-info, 15-05-ham-and-licensing, 15-06-antennas-and-range, 15-07-signals-and-codes, 15-08-destination-comms, 15-09-corridor-comms, 28-05-radios, 28-07-reading-your-own-gear, 09-01-power-priorities, 09-03-batteries-and-storage, 09-07-battery-chemistry, 09-08-wiring-and-safety, 09-11-hand-and-alt-generation, 14-03-opsec, 01-03-phase-b-movement, 18-01-mutual-aid, 25-08-quick-reference-cards, 25-10-annual-review]
cards: []
explainers: [EX-09, EX-02]
promote_when: [has.gmrs, has.ham]
photo_slots:
  - { id: radios-and-chargers, caption: "Our radios, their chargers and battery trays, and where they live" }
figures: [fig-line-of-sight-and-repeater]
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: { date: "2026-11-16", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "FRS/GMRS/MURS/CB power and channels checked against 47 CFR 95; GMRS licence terms (10 yr, 18+, family) added; ranges labelled typical." }
---

# Radio options: FRS, GMRS, MURS, CB, ham, scanners and satellite

**What this page is for.** Choosing radios that will actually work for your household when the
phones do not: which "service" does what, the FRS and GMRS channel table, how repeaters work,
buying advice, power, and the security cost of transmitting. Start with the plain-words
explainer on → 29-09 if any of these names are new.

> **CAUTION.** **The biggest mistake is buying handhelds and expecting the range on the
> package.** "35-mile" radios do not do 35 miles; typical numbers are on → 15-06, so read it
> before spending money. **Transmitting is announcing**: anyone listening learns that you
> exist, roughly where you are and what you are doing (→ 14-03). That is a trade-off to make on
> purpose.

> **Before the collapse:** power limits, frequencies and licences are federal rules (47 CFR
> Part 95 for FRS, GMRS, MURS and CB; Part 97 for amateur radio), and they change. Check the
> current rule, not this page. Transmitting outside a service's rules or your licence class is a
> federal violation while the FCC operates. A GMRS licence needs no exam, is issued to an adult
> (18 or older) for a ten-year term, carries an FCC fee, and lets the holder's immediate family
> (spouse, children, grandchildren, parents, grandparents, brothers and sisters, aunts, uncles,
> nieces, nephews, in-laws and step-relations) use the station (47 CFR 95.1705). An amateur
> licence needs an exam (→ 15-05). **Listening needs no licence.** A
> radio you are licensed and practised on now is worth far more than one you are guessing at
> later.

## Do this now

1. **Decide what you need radios for**, because it changes the answer:
   (a) **family coordination around the house and neighbourhood**; (b) **staying in touch while
   moving**; (c) **hearing what is happening in the region**; (d) **reaching real distance**. Most
   households need (a) and (c); (d) is amateur radio.
2. **For (a) and (b), buy GMRS radios** and get the GMRS licence: no exam, covers the family, more
   capable than FRS.
3. **For (d), start on the amateur (ham) Technician licence now** (→ 15-05). You cannot sit the
   exam after the grid goes down.
4. **For (c), buy a scanner or wideband receiver.** Listening is legal, useful, and does not
   broadcast your existence (→ 15-04).
5. **Write down what you own** (below) so the family plan on → 15-03 matches reality.

## The services compared

Orientation only; the explainer (→ 29-09) and the current federal rule give the details.

| Service | Licence | Typical range (terrain decides; → 15-06) | Notes |
|---|---|---|---|
| **FRS** (Family Radio Service) | **None** | A few hundred yards to about a mile in town | Fixed antennas; **2 W (0.5 W on channels 8 to 14)**. Fine for the yard and the block |
| **GMRS** (General Mobile Radio Service) | **Licence, no exam, covers the family** | 1 to 5 miles typical; more with repeaters and better antennas | **The sweet spot for family use.** More power, removable antennas, repeaters allowed |
| **MURS** | **None** | About 1 to 3 miles | **5 channels** (151.820, 151.880, 151.940, 154.570, 154.600 MHz), **2 W**; fewer users; **outside antennas allowed** (top no higher than 60 ft above ground or 20 ft above the structure) |
| **CB** (Citizens Band) | **None** | 1 to 5 miles typical; sometimes very far | 40 channels near 27 MHz; **4 W AM, 12 W single-sideband**; still used by truckers; long antennas; **road information on the move** |
| **Amateur (ham)** | **Licence, exam** | Across town to across the world, by band, power and antenna | **The only option with real reach.** Repeaters, emergency nets |
| **Scanner or receiver** | **None** | Listening only | **Legal, useful, invisible.** Start here |

## What each is good for

**FRS and GMRS: family coordination.** One adult at the water source, one at the house; keeping
track of {{#if has.child}}children{{else}}people{{/if}} in a crowd; coordinating a move. **GMRS is
the better buy**: more power, better antennas, repeaters, and one licence covers the household.

**MURS:** a quieter alternative to FRS with the big advantage that you may fit a better antenna.

**CB: road information.** On the move by vehicle, CB is where road conditions circulate. Cheap,
no licence, and the antenna is the whole game.

**Amateur radio: real reach.** The only service that reliably gets beyond line of sight. In a
regional emergency, amateur operators run organised emergency nets and are often the last working
communications network (ARRL). It is also where the knowledge is: antennas, propagation, power,
repair (→ 15-05, → 15-06).

**Scanner or receiver: awareness without exposure.** Listening tells you what is happening
without telling anyone you are there (→ 14-03, → 15-04). For a household that values discretion,
this is the most valuable radio capability.

## What we own (fill in)

{{#if has.gmrs}}Your profile lists FRS or GMRS radios.{{else}}Your profile lists no FRS or GMRS
radios. If you buy some, they are the first hardware purchase in this section: matched pairs or
fours, same model.{{/if}}{{#if has.ham}} Your profile lists a ham radio or a licensed member
(→ 15-05).{{/if}}{{#if has.satellite}} Your profile lists a satellite messenger or satellite
internet (below).{{/if}}

- FRS or GMRS handhelds: model ____________ count ____ AA trays? ☐ programming cable? ☐
- GMRS licence: filed ☐ (date ______) granted ☐ call sign ______________
- Amateur licence holders and class: ___________________________________________
- Scanner or receiver: ____________ CB: ____________ Satellite: ____________

{{photo radios-and-chargers}}

## The FRS and GMRS channel table

All 22 shared channels, from 47 CFR Part 95 (§§ 95.563, 95.567, 95.1763, 95.1767). Print it;
it is public and rarely changes. Power figures are the legal maximums: the FRS limits and the
GMRS 5 W and 0.5 W limits are radiated power; the GMRS 50 W limit is for mobile, base and
repeater radios (fixed stations 15 W). Your family channel is chosen on → 15-03.

| Ch | MHz | Power | Ch | MHz | Power |
|---|---|---|---|---|---|
| 1 | 462.5625 | FRS 2 W / GMRS 5 W | 12 | 467.6625 | 0.5 W only |
| 2 | 462.5875 | FRS 2 W / GMRS 5 W | 13 | 467.6875 | 0.5 W only |
| 3 | 462.6125 | FRS 2 W / GMRS 5 W | 14 | 467.7125 | 0.5 W only |
| 4 | 462.6375 | FRS 2 W / GMRS 5 W | 15 | 462.5500 | FRS 2 W / GMRS 50 W |
| 5 | 462.6625 | FRS 2 W / GMRS 5 W | 16 | 462.5750 | FRS 2 W / GMRS 50 W |
| 6 | 462.6875 | FRS 2 W / GMRS 5 W | 17 | 462.6000 | FRS 2 W / GMRS 50 W |
| 7 | 462.7125 | FRS 2 W / GMRS 5 W | 18 | 462.6250 | FRS 2 W / GMRS 50 W |
| 8 | 467.5625 | 0.5 W only | 19 | 462.6500 | FRS 2 W / GMRS 50 W |
| 9 | 467.5875 | 0.5 W only | 20 | 462.6750 | FRS 2 W / GMRS 50 W |
| 10 | 467.6125 | 0.5 W only | 21 | 462.7000 | FRS 2 W / GMRS 50 W |
| 11 | 467.6375 | 0.5 W only | 22 | 462.7250 | FRS 2 W / GMRS 50 W |

**"Privacy codes"** on these radios are tones (CTCSS or DCS) that only filter what **you** hear.
They hide nothing from anyone else (→ 15-03). **GMRS repeaters transmit on 462.550 to 462.725 MHz
(channels 15 to 22) and listen 5 MHz higher (467.550 to 467.725 MHz).** FRS radios can hear a
repeater's output but cannot talk through it; a repeater-capable GMRS radio can.

## Programming a repeater

A **repeater** is a radio on a tall tower that receives you and re-transmits at once, so radios
that cannot reach each other can both reach it (→ 29-09).

{{figure fig-line-of-sight-and-repeater}}

Any repeater needs three settings in your radio:

1. **The offset:** transmit 5 MHz above the frequency you listen on (GMRS repeaters are always
   +5 MHz; a radio's "repeater channel" mode usually does this for you).
2. **The transmit tone** (CTCSS or DCS): a tone the repeater needs before it will repeat you.
   **It is a key, not privacy**: everyone can still hear you.
3. **The test:** press to talk, give your call sign, and listen for the repeater's short "tail"
   after you let go. If nothing comes back, the tone or offset is wrong.

Our local repeater (if any): output ______ MHz, input ______ MHz, tone ______, open to the
public? ☐ Programmed ☐ (date ______) memory slot ______ tested on the air ☐ (date ______).
**Check it is still on the air twice a year**: repeaters are volunteer machines and come and go
(→ 15-05).

## Buying advice that matters

- **The antenna matters more than the radio.** A modest radio with a good antenna beats an
  expensive one with a stubby antenna, every time (→ 15-06).
- **Range claims are marketing.** Expect a small fraction of the number on the box in real
  terrain, and much less indoors or in town.
- **Buy radios that take common batteries (AA trays) or charge from 12 V** (→ 09-08). A radio with
  a battery pack you cannot replace is a temporary radio.
- **Buy in pairs or fours, all the same model**, so batteries, chargers and accessories swap and
  everyone knows how to use them.
- **Get spare batteries, spare antennas and a programming cable** while you can.
- **Practise now.** A radio nobody has used is not a capability.
- Spec tables for common radios: → 28-05.

## The security side

Every transmission is an announcement (→ 14-03):

- **Anyone with a scanner can hear you**, including on FRS, GMRS and CB, which are unencrypted by
  rule.
- **Finding a transmitter by direction is not exotic.** A transmitter used often can be located.
- **What you say matters.** What you have, where you are going and when the house is empty do not
  belong on an open channel.
- **What helps:** listen far more than you transmit; keep transmissions short and bland; use
  simple pre-agreed family codes (→ 15-07); and ask whether the coordination is worth the
  exposure.
- **In an ordinary emergency** (a blizzard, an outage, a tornado) the balance favours talking. In a
  long breakdown it shifts (→ 14-03).

## Power

Radios are a small load but a steady one if you listen all day (→ 09-01).

- **Handhelds:** rechargeable packs plus **AA battery trays** as backup, so they can be charged or
  fed from almost anything (→ 09-07).
- **Base and vehicle radios** run on **12 V DC directly** from a battery bank: efficient, no
  inverter (→ 09-08).
- **A scanner listening all day** is a real draw over 24 hours. Budget it.
- **Hand-crank radios** for when there is no power at all (→ 09-11).
- {{#if has.power_station}}**Your power station** (→ 09-03) can charge handhelds from its USB ports
  and run a scanner or base radio from its 12 V port. Keep any station reserved for medical or food
  loads for that job; radios charge from the others.{{else}}A power station or 12 V battery bank
  (→ 09-03) charges handhelds by USB and runs a base radio from 12 V.{{/if}}
- **In the vehicle:** a USB charger in the 12 V socket keeps handhelds topped up while driving.

## Satellite: messengers and satellite internet

Satellite devices reach past dead cell towers, but they depend on companies, networks and
accounts outside your control. **They are a layer in the plan, never the plan.**

- **Satellite messengers and phones with satellite texting** send short messages and SOS calls
  where there is no cell signal (→ 15-03).
- **Satellite internet dishes** (for example Starlink) give real internet, and with phone Wi-Fi
  calling turned on, a phone beside a working dish can make ordinary calls and texts.

**If you have satellite internet (or are thinking about it):**

- **It must be activated, with a paid account, before the emergency.** Activation runs through an
  app and the internet. Starlink's low-cost Standby Mode (low-speed messaging, weather and email,
  not video) is only available to customers who already have the kit on another plan, and since
  March 2026 it is for stationary use only: it switches off when the dish senses motion
  (Starlink, How does pausing service work; Starlink, Critical Information Summary; Mobile
  Internet Resource Center, 2026). Full-speed in-motion use needs a mobile plan. Check current
  plans and prices in the app while you still can.
- **It depends on things you do not control**: satellites, ground stations, billing and policy.
  It shines in a local or regional outage; a wider collapse, an account problem or a policy change
  can switch it off.
- **Power:** read the label for its voltage and watts (→ 28-07); smaller dishes run from a 12 V
  vehicle socket with an adapter, or from a power station. Run it in scheduled windows to stretch
  the battery.
- **Security:** a dish in the yard is visible and it transmits (→ 14-03).
- **The day it is activated:** turn on **Wi-Fi Calling** on every phone, join the dish's Wi-Fi,
  and test a voice call and a text **with cellular switched off**. That test is what proves it
  is a channel.

Ours: ☐ none ☐ messenger ☐ satellite internet. Plan ______ activated ______ Wi-Fi calling on
every phone ☐ tested ☐

## Gear

| Item | Why | Notes |
|---|---|---|
| **GMRS handhelds and a GMRS licence** | Family coordination; no exam; covers the household | Removable antennas; spare batteries |
| **Amateur Technician licence and a dual-band handheld** | The path to real capability | → 15-05 |
| **Scanner or wideband receiver** | Listen without transmitting | Legal, invisible, high value |
| Better antennas for everything | The antenna matters more than the radio | → 15-06 |
| AA battery trays for handhelds | Charge or feed them from anything | Often sold separately |
| Spare batteries, chargers, programming cable | The parts that fail or get lost | Buy while available |
| 12 V leads and fuses for base radios | Run straight off a battery bank | → 09-08 |
| CB (mobile or handheld) and a real antenna | Road information on the move | The antenna is the whole game |
| Hand-crank radio | Works with no power | → 09-11, → 15-01 |
| **A written family channel plan** | Everyone knows where to meet on the air | → 15-03, → 25-08 |
| Printed operating notes and licence details | Paper survives dead batteries | This binder |

**If you do not have it:**

- **Radios** turn up in vehicles, boats, businesses, marine sets and old scanners. **Vehicle radios
  receive AM and FM, and many receive the weather band.**
- **Antennas** are the best improvisation: wire, coaxial cable and a little knowledge make good
  ones (→ 15-06).
- **Power:** a battery bank, AA trays, a vehicle battery.
- **What you cannot scavenge is a licence and the skill.** Both take time and can only be got now
  (→ 15-05).

## When it runs out

- **Batteries are the consumable** (→ 09-07). Radios are a small load, so with solar and
  rechargeables this lasts a long time.
- **Hardware is what fails:** antennas break, connectors corrode, handhelds get dropped, battery
  packs die. **Stock spare antennas, cable, connectors and battery trays.**
- **Think about which capability you lose first.** Handhelds with proprietary packs go first;
  radios that take AA cells and run on 12 V last much longer. Buy accordingly.
- **Step down in order:** amateur, GMRS, FRS, then **signals without radio** (→ 15-07): whistles,
  mirrors, lights, flags, pre-agreed signals, and walking over to a neighbour (→ 18-01).
- **Knowledge does not run out.** Someone who understands antennas, propagation and 12 V power can
  keep communications going from salvage for a very long time (→ 15-05, → 15-06).

## By phase

- **A (at home):** GMRS for the household and the block, a scanner for awareness, the weather
  radio (→ 15-01), and amateur radio for regional news if someone is licensed. **Listen more than
  you transmit** (→ 14-03).
- **B (on the move):** GMRS handhelds keep the group together (this is where they earn their
  keep), CB for road information if driving, and great care about what you say on the air
  (→ 01-03, → 15-09).
- **C (rural or a new place):** distance becomes the problem and **amateur radio becomes the
  answer** (→ 15-05). At a rural site you can put up real antennas, so this is one capability that
  gets better (→ 15-06).

---
id: 15-06-antennas-and-range
section: 15-communications
title: "Antennas, range and realistic expectations"
version: 2
revised: 2026-11-16
layer: core
danger_level: caution
phase: [A, B, C]
tags: [antenna, range, line of sight, height, repeater, dipole, J-pole, coax, connectors, SWR, lightning, power lines, RF exposure]
derived_from: [15-06-antennas-and-range]
sources: [us-government-publishing-office-ecfr-47-cfr-part-97-17b11d, arrl-single-band-dipoles, arrl-the-national-association-for-amateur-radio-what-5edded, us-government-publishing-office-ecfr-47-cfr-part-95-c8b55a, noaa-national-weather-service-weather-ready-nation-b0a52f]
related: [29-09-ex09-radios, 15-01-weather-alerts, 15-02-radio-options, 15-04-monitoring-and-info, 15-05-ham-and-licensing, 15-09-corridor-comms, 09-02-solar-basics, 09-08-wiring-and-safety, 12-09-splints-and-fractures, 14-03-opsec, 16-01-essential-hand-tools, 16-03-knots-and-cordage, 17-01-blizzards-and-ice, 17-18-hail-and-damaging-wind, 22-02-scavenging-field-guide, 23-05-skills-that-replace-supplies]
cards: []
explainers: [EX-09]
promote_when: [is.rural]
photo_slots: []
figures: [fig-line-of-sight-and-repeater, fig-wire-dipole]
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: { date: "2026-11-16", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "Range table labelled typical; dipole formula sourced to ARRL; owner GMRS channel residue replaced; arithmetic rechecked." }
---

# Antennas, range and realistic expectations

**What this page is for.** How far radios really reach, why the antenna matters more than the
radio, how to build a working antenna from wire, and how to put one up without being killed by a
power line, a fall or lightning. Radio words are explained on → 29-09.

> **CAUTION. Three ways antenna work hurts people.**
> **(1) Power lines.** **Never put up an antenna, mast or wire where it could touch or fall onto a
> power line.** This kills people every year. Treat every line as live, keep the full length of
> the mast plus a wide margin away, and have a second person present.
> **(2) Falls.** Roof and ladder work, especially in ice or wind, is one of the likeliest serious
> injuries in this binder (→ 12-09). **Do antenna work in good weather, with help.**
> **(3) Lightning.** An outdoor antenna is a path for lightning into the house. **Ground the
> system and disconnect the cable when storms threaten.** A strike can destroy every radio you own
> and start a fire.

## Do this now

1. **Reset your expectations before spending money.** Range numbers on packaging are
   mountaintop figures. Typical numbers are in the table below.
2. **Buy a better antenna for every handheld.** The cheapest, biggest single improvement.
3. **Buy coaxial cable ("coax"), connectors and wire now.** Cheap, they do not expire, and they
   are the raw material for every antenna you will ever improvise.
4. **Put up one antenna and use it**, so you learn while it is a hobby and not an emergency.
5. **Test your own range** (below) and write it down.

## The one thing to understand: height beats power

For VHF and UHF radios (handhelds, FRS, GMRS, repeaters), **communication is essentially line of
sight**:

- **Doubling the power buys very little range.**
- **Raising the antenna buys a great deal.**
- **Hills, buildings and trees block signals**; height gets over them.

**A 5-watt handheld with a good antenna up high beats a 50-watt radio with a stubby antenna at
ground level.** That is why money and effort belong in the antenna.

{{figure fig-line-of-sight-and-repeater}}

## Typical ranges

These are typical figures for planning, not measurements or promises: terrain, buildings, trees,
weather and the antenna decide the real number, which is why you test your own (below).

| Setup | Typical range |
|---|---|
| **FRS handheld, in town, at ground level** | **A few hundred yards to about a mile** |
| FRS or GMRS handheld, open flat country | 1 to 3 miles |
| **GMRS handheld with a good antenna** | 2 to 5 miles |
| GMRS mobile with a roof antenna | 5 to 15 miles |
| **GMRS or amateur through a repeater** | **20 to 50 miles or more**: the repeater's height does the work |
| Amateur VHF/UHF radio to radio, good antennas, both raised | 10 to 30 miles |
| **CB with a proper (long) antenna** | 1 to 5 miles typical; sometimes very far when conditions allow |
| **Amateur HF with a wire dipole** | **Hundreds to thousands of miles**, varying with band, time of day and conditions |

**What the table shows:** handhelds are a **household and neighbourhood** tool. **Real distance
comes from repeaters (someone else's height) or from HF, which does not depend on line of
sight.**

**Flat country helps; buildings, trees and being indoors cut range hard.** Test your real range:
one person walks or drives away calling every block until contact is lost, from inside the house
and from outside. Write it down:

| Radio and antenna | From | Range reached |
|---|---|---|
| ______________ | inside the house | ______ |
| ______________ | outside | ______ |
| ______________ | through the repeater | ______ |

## Antennas, worst to best

1. **The stubby "rubber duck"** supplied on a handheld: a poor compromise.
2. **A longer whip**: a real improvement for a few dollars.
3. **A roll-up J-pole or slim-jim** (a flexible wire antenna) hung in a tree or from a curtain
   rod: cheap, packable, dramatically better. **For a handheld, the best value in this section.**
4. **A magnetic-mount antenna on a vehicle roof**: the metal roof and the height help a lot.
5. **A permanent outdoor vertical**, as high as can be safely put up.
6. **For HF: a wire dipole**: two lengths of wire and a centre feed point. Cheap, effective, and
   buildable from salvage (→ 15-05).

## Coax and connectors: the quiet failure

- **Coax loses signal**, more with length and frequency. A long run of cheap coax to a UHF antenna
  can throw away most of your signal.
- **Keep runs short**, use decent coax, and **do not coil the spare tightly.**
- **Water is the enemy.** Water in coax ruins it. **Seal every outdoor connector** with
  self-amalgamating tape, then electrical tape over it.
- **Sunlight destroys cheap coax jackets** within a few years. Check them.
- **Corroded connectors are a common, invisible cause of "my radio stopped working".** Inspect
  them every season, and **stock spare connectors and a crimper.**

## Building an antenna from wire

This works, and it is satisfying.

- **A dipole is two pieces of wire**, each a quarter of a wavelength long, fed in the middle by the
  coax. **The formula is one line:**
  **each leg (feet) = 234 ÷ frequency (MHz); whole dipole (feet) = 468 ÷ frequency (MHz)**
  (ARRL, Single Band Dipoles). Cut each leg a little long, hang it, and trim both ends equally
  until an SWR meter (which measures how well the antenna matches the radio) reads lowest. If the
  SWR falls as you tune lower in frequency, the antenna is still too long; if it rises, it is too
  short and needs wire added to both ends (ARRL). Worked out for common
  frequencies:

  | Use | Frequency | Each leg | Whole dipole |
  |---|---|---|---|
  | Amateur 2-metre calling | 146.520 MHz | **19.2 in** | 38.3 in |
  | NOAA Weather Radio (receive) | 162.400 MHz | **17.3 in** | 34.6 in |
  | GMRS channel 15 | 462.550 MHz | **6.1 in** | 12.1 in |
  | CB channel 19 | 27.185 MHz | **8.6 ft** | 17.2 ft |
  | Amateur 40 metres (General licence) | 7.200 MHz | **32.5 ft** | 65.0 ft |

  For your own family channel or repeater: 234 ÷ ______ MHz = ______ ft each leg.

{{figure fig-wire-dipole}}

- **A ground-plane vertical** is one quarter-wave wire pointing up, over **several
  quarter-wave "radial" wires** (four is common) laid flat or drooping. **A replacement for a broken GMRS handheld
  antenna is the 6-inch quarter wave above, not "longer is better".** A random long wire is fine
  for *receiving* shortwave and broadcast; for *transmitting*, cut it to length and check the SWR.
- **Wire:** speaker wire, house wiring, fence wire, salvaged electrical cable (→ 09-08).
- **Insulators:** pieces of plastic bottle, wooden dowels, ceramic, plastic sheet.
- **Supports:** trees, a fence post, a pole, the house, a line thrown over a branch.
- **An SWR meter or antenna analyser** tells you whether it is right. **Without one you are
  guessing, and a badly mismatched antenna can damage the transmitter.** Buy one now.

## Keep people away from transmitting antennas

A transmitting antenna heats what is right next to it. **Any base or vehicle antenna, a 50-watt
GMRS mobile especially, goes where nobody, least of all a child, can touch it or stand within
arm's reach while it transmits**: roof peak or mast, not a deck rail or window ledge. With a 5-watt
handheld, keep the antenna a hand's width from your face and eyes, and never transmit with the tip
against anyone. Before the collapse, the FCC's radio-frequency exposure rules govern this;
afterwards it is still physics.

## Ice, wind and lightning

- **Ice storms bring antennas down.** Build for ice, use good supports, expect repairs after a
  storm (→ 17-01).
- **Wind:** guy (brace with ropes or wires) anything tall, properly (→ 17-18).
- **Lightning:** **ground the antenna system, and disconnect the cable when storms threaten.** A
  disconnected coax lying on the floor is a safe coax.
- **Snow on horizontal wires** makes them sag; leave slack and check after storms.

## Security

**A visible antenna is a visible capability** (→ 14-03). A big mast on a town lot says this house
has communications. **Wire antennas in trees are nearly invisible**, attic and indoor antennas
work (less well), and **a magnetic-mount antenna that comes off the vehicle leaves no trace.**
Weigh discretion against performance on purpose.

## Gear

| Item | Why | Notes |
|---|---|---|
| **A better antenna for every handheld** | Cheapest, biggest improvement | Longer whip; roll-up J-pole |
| Roll-up J-pole or slim-jim | Hang it in a tree; packable | Best value in this section |
| Magnetic-mount vehicle antenna | Roof height; removable | On the move; discretion |
| **Good coax, connectors, crimper** | The failure point nobody stocks | Buy extra; it does not expire |
| Self-amalgamating tape and electrical tape | **Sealing outdoor connectors** | Cheap; essential |
| Antenna wire, several hundred feet | Dipoles, radials, repairs | Stranded copper |
| Insulators, rope, pulleys | Getting wire up and keeping it there | → 16-03 for knots |
| **SWR meter or antenna analyser** | Stops guessing; protects the radio | Worth it |
| Grounding rod, ground wire, clamps | Lightning protection | Plus the disconnect habit |
| Lightning arrestor or coax switch | Fast disconnection | → 17-01 |
| Mast sections, guy line, stakes | Height is the whole game | Guy it properly |
| An amateur antenna book on paper | Designs beyond the dipole table | → 15-05 |

**If you do not have it:**

- **Wire:** speaker wire, electrical cable, fence wire, the centre conductor of salvaged coax.
- **Insulators:** plastic bottles, plastic pipe scraps, wooden dowels, ceramic pieces.
- **Supports:** trees (**the best mast you will ever have, and free**), fence posts, a fibreglass
  pole, a ladder, the house.
- **Mast:** conduit, a fence post, pipe, a cut sapling.
- **Ground plane:** wires laid on the ground, a vehicle roof, metal roofing.
- **Coax:** salvaged TV coax works for receiving and for some transmitting at lower frequencies.
  Not ideal; better than nothing.
- **Rope over a branch:** a weight on a line thrown over a high limb is the classic way to get wire
  into a tree (→ 16-03).

## When it runs out

- **Coax and connectors are the consumables**, and they fail invisibly from water, sunlight and
  corrosion. **Stock spares now**; they are the most under-stocked item in this section.
- **Antenna wire is nearly unlimited** from salvage (→ 22-02).
- **Sealing is the maintenance that matters.** A sealed system with good supports lasts years; a
  poorly sealed one fails in one wet season.
- **A ten-minute seasonal check** (connectors, cable jacket, supports, and everything after every
  ice storm and windstorm) prevents most failures.
- **Knowledge substitutes directly for money here** (→ 23-05): understanding wavelength, height
  and matching lets you build a working antenna from a fence and a spool of wire, indefinitely.

## By phase

- **A (at home):** modest and discreet: a wire in a tree, an attic antenna, or a magnetic mount on
  the vehicle. **Ground it and disconnect it in storms.** Test and write down your real range.
- **B (on the move):** a magnetic mount on the vehicle and a roll-up J-pole in a pack. A roll-up
  hung from a branch at a stop turns a handheld into something truly useful (→ 15-09).
- **C (rural or a new place):** **where antennas finally get to be good**: space, height, trees,
  no neighbours, little electrical noise. **A full-size HF dipole between two trees and a 12 V
  solar bank is a real long-distance station** (→ 15-05, → 09-02). Build it early, guy it for
  wind, and ground it for lightning.

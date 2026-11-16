---
id: 09-13-scavenging-electrical-power
section: 09-power-and-energy
title: "Scavenging electrical power: what to harvest"
version: 1
revised: 2026-11-16
layer: core
danger_level: critical
phase: [A, B, C]
tags: [power, scavenging, salvage, batteries, solar, lithium, ups, alternator, safety]
derived_from: [09-13-scavenging-electrical-power]
sources:
  - nfpa-national-fire-protection-association-lithium-io-0c7d64
  - osha-electrical-safety-and-health-topics-a7a68f
  - us-department-of-energy-solar-energy-technologies-of-2a534a
  - us-consumer-product-safety-commission-cpsc-what-to-k-3390a4
related:
  - 09-03-batteries-and-storage
  - 09-04-generators
  - 09-07-battery-chemistry
  - 09-08-wiring-and-safety
  - 09-09-small-solar-build
  - 09-11-hand-and-alt-generation
  - 09-12-ac-dc-cables-and-connectors
  - 09-14-car-batteries-in-practice
  - 06-06-fuel-storage-safety
  - 10-03-diy-and-conservation
  - 18-02-barter-and-trade-goods
  - 22-02-scavenging-field-guide
  - 23-04-resource-lifecycles
  - 30-01-the-floors
cards: []
explainers: [EX-02, EX-12]
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

# Scavenging electrical power: what to harvest

**What this page is for.** What is worth taking from vehicles, buildings and abandoned equipment to
keep your power going in a long event, what is not worth the risk, and how to tell a useful battery
from scrap. Read → 09-12 first: without a multimeter and an adapter kit, most of what you could
harvest is unusable.

> **SAFETY. Four things on this page can kill or burn you, and they are not the obvious ones.**
> **(1) Stored charge.** Capacitors inside inverters, power supplies, microwave ovens and old CRT
> televisions hold a **lethal charge long after unplugging.** **Do not open them.**
> **(2) Lithium packs.** Damaged or mishandled cells go into thermal runaway, an intense,
> self-sustaining fire (NFPA, Lithium-Ion Batteries). **Do not take packs apart for cells.**
> **(3) Solar panels are live in daylight.** They make voltage whenever light falls on them; there is
> no off switch (US Department of Energy, Solar Photovoltaic System Design Basics).
> **(4) Anything connected to house wiring or a running generator.** That is electrician territory
> (OSHA, Electrical) and the backfeed floor: **never connect a generator to house wiring without a
> transfer switch, interlock, or a cord-and-plug conversion with the main breaker locked off; never
> backfeed through an outlet** (→ 09-04, → 30-01).

## Do this now
- **Read → 09-12 first.**
- **Learn the resting voltages for lead-acid** (→ 09-07): they tell a useful battery from scrap with
  no special equipment.
- **Decide the lithium rule now, calmly: take whole packs with their matching chargers, never loose
  cells.** That rule is the whole safety margin.
- **Scavenging is no substitute for owning a system** (→ 09-09). It extends what you have; it does not
  produce anything (→ 23-04).

## Why it works this way

### What is actually worth taking
Ranked by usefulness for the risk and effort:

| Rank | Item | Why | Risk |
|---|---|---|---|
| **1** | **Lead-acid batteries:** car, truck, marine, RV, golf cart, floor scrubber, mobility scooter | Everywhere, testable with a meter, no fire risk in normal use | Acid, weight, hydrogen when charging: **ventilate** |
| **2** | **Wire, terminals, fuses, fuse blocks, 12 V sockets** | The consumable every repair uses (→ 09-12) | Low |
| **3** | **Vehicle 12 V accessories:** chargers, inverters, socket splitters | Built for exactly this voltage | Low |
| **4** | **UPS units** (office and computer battery backups) | **Underrated.** A sealed lead-acid battery, a charger and an inverter in one box | Stored charge in the inverter: **do not open it** |
| **5** | **Solar:** garden and path lights, sign and construction panels, RV panels | Free DC, no fuel, silent | Live in daylight; theft risk on the last two |
| **6** | **Alternators, small motors** | Generation potential (→ 09-11) | Needs a mechanical drive you probably do not have |
| **7** | **Whole cordless tool, e-bike or laptop packs, with their charger** | Usable **as a pack**, on its own charger | **High: see the lithium section** |
| **(none)** | **Loose lithium cells, opened packs** | | **Do not** |

### Lead-acid: the one you can judge
In depth on → 09-03 and → 09-07; the field version:
- **Resting voltage tells you most of what you need.** A 12 V lead-acid battery at rest reads about
  **12.6 to 12.7 V full**, about **12.0 to 12.1 V at 50%** (as low as you should take it), and below
  about **11.8 V you are damaging it.**
- **A battery at 0 V, or with a cracked case, bulging sides or leaking acid, is scrap.** Leave it.
  Batteries that have sat flat for months are usually beyond recovery.
- **Deep-cycle beats starting.** Marine, RV, golf-cart and floor-scrubber batteries are built to be
  drained; car starting batteries die fast if cycled (→ 09-14).
- **Carry them upright, wear eye protection and gloves,** and never let a metal tool bridge the
  terminals: that is an instant, violent short (→ 09-08).
- **Charge in a ventilated space.** Charging lead-acid makes hydrogen.

### UPS units: the best-value scavenge nobody thinks of
Every office, server closet and home desk has one. A UPS is effectively a **pre-built 12 V system in
a box**: a sealed lead-acid battery, a charger and an inverter.
- **The battery is the useful part:** usually a standard 12 V sealed lead-acid, easy to remove from
  its own compartment.
- **The inverter section holds stored charge. Do not open the electronics.** Take the battery from its
  compartment; leave the rest sealed.
- **The whole unit is useful as-is** if you have any AC to charge it from, as a small buffer for a
  critical load.

### Solar you can actually find
- **Garden and path lights:** a tiny panel, a small cell and an LED each. Trivial one by one; **in
  quantity a useful trickle**, and free indoor light as they are (→ 10-03).
- **Sign, construction, RV and boat panels:** real panels, usually with **MC4 connectors** and often
  a controller and battery attached.
- **Treat every panel as live.** **Cover it with something opaque before handling the connectors,**
  and never bridge the leads.
- **Read the label** for the open-circuit voltage before connecting anything. A panel meant for a 24 or
  48 V system will not behave the way you want on a 12 V controller, and may exceed your station's
  input limit (→ 09-02, → 09-03).
- **A panel is useless without a charge controller.** Connecting a panel straight to a battery can
  destroy the battery. Take the controller if there is one (→ 09-09).

### Vehicles: a rolling parts bin
Beyond the battery (→ 09-11 covers running a vehicle as a generator, and the carbon monoxide rule):
- **Alternator:** real generation potential, but it needs to be spun fast by something.
- **Inverters, 12 V sockets, fuse blocks, relays and the wiring harness:** all reusable in a 12 V
  system (→ 09-12).
- **Heavy cable:** battery and starter cables are excellent conductors.
- **Fuses:** every vehicle carries an assortment, and fuses are consumed by every mistake.

### Lithium: the honest and unpopular position
Tool packs, laptop batteries, e-bike and scooter packs and power station cells are everywhere and hold
real energy. **They are also the most dangerous thing in this section.**

**The rule: use whole packs with their own chargers, or leave them.** Why:
- **Damaged or mishandled lithium cells can go into thermal runaway**, an intense, self-sustaining
  fire that is very hard to extinguish and gives off toxic smoke (NFPA, → 09-07).
- **Cells in a pack are spot-welded, not screwed.** Getting them apart is exactly the handling that
  punctures or shorts them.
- **The pack's battery management system is the safety device.** Remove it and you have removed the
  protection against overcharge, over-discharge and imbalance.
- **You cannot tell a good salvaged cell from a bad one by looking.**

**The warning signs, worth memorising:** **heat, an odd smell, swelling or a change of shape.** Any of
those: get it away from people and buildings, outdoors, on a non-combustible surface, and do not try
to charge it.

**What is reasonable:**
- Take a tool pack **and its charger together**, and use it with the tool it belongs to.
- Take a power station or e-bike battery **whole and undamaged**, and use it as designed.
- **Store salvaged lithium outside the living space**, away from anything that would burn (→ 06-06),
  not in the basement beside the medical supplies.
- **Never charge salvaged lithium unattended, overnight or indoors.**

### What is NOT worth taking
- **Microwave ovens and CRT televisions** for parts: the stored charge is lethal.
- **Anything with a cut or damaged mains cord.**
- **Sealed inverter or electronics housings:** you cannot repair them and they hold charge.
- **Batteries that are swollen, leaking, cracked or read 0 V.**
- **Solar panels with shattered glass or peeling backing:** degraded, and a shock hazard when wet.
- **Anything still connected to a building's wiring.** That is not scavenging; it is working on live
  wiring (OSHA, → 09-08).

### The legal and ethical line
**Taking property that is not yours is theft**, and while the law works, the law applies. Sign and
construction solar arrays belong to someone. **Ask, trade or leave it** (→ 18-02, → 22-02): the
relationships outlast the panel.

## Gear and items

**Have it now (buy toward this):**

| Item | Why | Notes |
|---|---|---|
| **Multimeter** | Nothing on this page works without one | → 09-12 |
| **Insulated gloves and eye protection** | Acid, sparks, shorts | → 16-01 |
| Battery terminal cleaner and puller | Corroded terminals are the usual failure | |
| **Insulated wrenches**, or tape over the metal | Bridging terminals is the classic injury | → 09-08 |
| Battery carry strap | They are heavier than they look | |
| **Spare charge controller** | A salvaged panel is useless without one | → 09-09 |
| MC4 and Anderson connector kit | Connect what you find | → 09-12 |
| Assorted fuses and holders | Consumed by every mistake | → 09-08 |
| Hydrometer or battery tester | Judging lead-acid properly | → 09-07 |
| **Fire extinguisher of the right class** | Especially with any lithium around | → 29-12 |

**Scavenge or substitute:** a cheap 12 V bulb makes a crude load tester; jumper cables move charge
between batteries; a vehicle's own charging system will charge a salvaged lead-acid battery (→ 09-11).

## When it runs out
Scavenged electricity is **substitution, never production** (→ 23-04).
- **Runway:** salvageable batteries degrade whether used or not. Most abandoned lead-acid is scrap
  within a couple of years; lithium packs age out too.
- **Ration:** treat every working battery as a consumable; do not deep-cycle a starting battery for
  convenience.
- **Resupply:** vehicles are the deepest reservoir, and they are finite.
- **Substitute:** **solar is the only electricity that keeps coming** (→ 09-02): panels last decades,
  and the batteries are the consumable.

## Phase notes
- **A (at home):** buy the multimeter and the adapter kit, and note what exists nearby. Take nothing
  that is not yours.
- **B (moving):** almost nothing here is worth the weight while moving: cables, adapters and a
  multimeter, not batteries.
- **C (settled somewhere new):** farms and outbuildings hold batteries, wire, panels and controllers,
  with less competition than town. Bring the connectors.

## Cross-references
→ 09-12 connectors and testing, read first · → 09-03 and → 09-07 judging lead-acid · → 09-08 fusing
and shorts · → 09-09 building with what you have · → 09-11 vehicle generation · → 09-14 car batteries
· → 22-02 scavenging guide and its ethics · → 23-04 resource lifecycles

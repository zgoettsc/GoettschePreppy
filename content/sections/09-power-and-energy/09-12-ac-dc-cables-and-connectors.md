---
id: 09-12-ac-dc-cables-and-connectors
section: 09-power-and-energy
title: "AC versus DC, cables, connectors and adapters"
version: 1
revised: 2026-11-16
layer: core
danger_level: caution
phase: [A, B, C]
tags: [power, ac, dc, cables, connectors, usb-c, mc4, anderson, adapters, inverter, polarity, scavenging]
derived_from: [09-12-ac-dc-cables-and-connectors]
sources:
  - osha-electrical-safety-and-health-topics-a7a68f
  - us-department-of-energy-solar-energy-technologies-of-2a534a
  - nfpa-national-fire-protection-association-lithium-io-0c7d64
  - osha-hand-and-power-tools-safe-use-maintenance-and-h-77254c
related:
  - 09-03-batteries-and-storage
  - 09-06-charging-medical-devices
  - 09-08-wiring-and-safety
  - 09-09-small-solar-build
  - 09-13-scavenging-electrical-power
  - 22-02-scavenging-field-guide
  - 22-03-go-bags-and-kits
  - 22-05-kit-vehicle
  - 25-02-conversions-and-math
  - 29-02-ex02-batteries-and-power-stations
  - 29-04-ex04-electricity-in-the-house
cards: []
explainers: [EX-02, EX-04]
promote_when: []
photo_slots:
  - { id: adapter-kit, caption: "Our adapter kit laid out and labelled" }
figures: [fig-mc4-polarity-check]
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: null
---

# AC versus DC, cables, connectors and adapters

**What this page is for.** Making mismatched equipment work together: which connectors you will
meet, how to charge things efficiently, and how to test a scavenged power source before it destroys
something. Volts, amps and watts: → 29-02. House wiring: → 29-04.

> **CAUTION.** Mismatched equipment is exactly when people connect something backwards and destroy
> it, or start a fire. **Three rules prevent almost every disaster here: check polarity before
> connecting, check voltage before connecting, and fuse the battery side** (→ 09-08). **Anything
> touching house wiring is an electrician's job** (OSHA, Electrical).

## Do this now
- **Buy a cheap multimeter and learn three measurements:** DC volts, AC volts, continuity. It costs
  less than a tank of fuel and is the difference between "I found a power supply" and "I destroyed my
  battery bank".
- **Build the adapter kit** listed below. It is small and cheap and it turns salvaged parts into
  working power (→ 09-13). {{photo adapter-kit}}
- **Label every cable you own:** voltage, polarity, what it belongs to.
- **Put a known-good charging set in the go-bag** (→ 22-03): the cable and charger that definitely
  work, not the drawer of maybes.

## Why it works this way

### AC and DC: the practical difference

| | **DC (direct current)** | **AC (alternating current)** |
|---|---|---|
| **What it is** | Current flows one way, steadily | Current reverses direction many times a second |
| **Where you meet it** | Batteries, solar panels, USB, vehicles, 12 V gear | Wall outlets, generators, inverter outputs |
| **Typical voltages** | 3.7, 5, 12, 20, 24, 48 V | 120 V (240 V for big appliances) |
| **Polarity** | **Matters. Backwards can destroy things instantly** | No polarity in the same sense |
| **Danger** | Low shock risk at 12 V; **high fire risk**: huge current into a short | **High shock risk.** 120 V can kill |

Almost everything you store energy in is **DC** (batteries, panels), and almost everything made for a
wall outlet is **AC**. Converting between them costs energy.

### The rule that saves the most power: run DC loads on DC
An **inverter** turns battery DC into household AC. That costs energy as heat, and the inverter draws
power just by being switched on, even with nothing plugged in.

```
BATTERY (12 V DC) --> 12 V DC device                  best: no conversion
BATTERY (12 V DC) --> USB adapter --> phone           very good: one small conversion
BATTERY (12 V DC) --> INVERTER --> wall charger --> phone
                                                      worst: two conversions,
                                                      and the inverter idles all day
```
**Charging a phone through an inverter and a wall charger is the most wasteful way.** Use a **12 V
to USB adapter.** {{#if has.condition.CL-02}}Where a phone runs a medical device, as in this household
(→ 09-06), that habit meaningfully extends the battery bank.{{/if}}

**When you do need the inverter:** for anything that only exists as AC (most kitchen appliances, power
tools, some medical equipment). **Switch it off when not in use**, and use a **pure sine** inverter
for anything sensitive (→ 09-08).

### The voltage ladder

| Voltage | What lives there |
|---|---|
| **3.6 to 3.7 V** | A single lithium cell |
| **5 V** | USB-A, basic USB-C charging, most small electronics |
| **12 V nominal** | Vehicles, most portable solar setups, RV and marine gear. **Real range about 11.8 to 14.6 V** depending on charge and charging |
| **9, 15, 20 V** | USB-C Power Delivery levels; laptops typically 20 V |
| **18 to 24 V** | Cordless tool packs |
| **24 and 48 V** | Larger off-grid systems: fewer amps, thinner wire |
| **120 V AC** | Wall outlets, inverter output |

**Watts = volts × amps** (→ 25-02). A 60 W load is 5 A at 12 V or 0.5 A at 120 V, which is why 12 V
needs much thicker wire for the same job (→ 09-08).

### The connectors you will actually meet
Salvaged power fails at the connector far more often than at the battery.

| Connector | Where it lives | Notes |
|---|---|---|
| **MC4** | Solar panels, almost universally | Weatherproof, locking. **Panels are live in daylight; treat them as live.** The + side has the male pin. {{figure fig-mc4-polarity-check}} |
| **12 V socket** ("cigarette lighter") | Vehicles, power stations, RVs | Convenient, **loose-fitting, limited current**: typically fused around 10 to 15 A |
| **Anderson Powerpole** | Ham radio, RV, home-built systems | **Excellent**: genderless, high current, hard to connect wrong. Worth standardising on |
| **XT60 / XT90** | Hobby gear, e-bikes, many power station solar inputs | High current, polarised |
| **Barrel jack** (commonly 5.5 × 2.1 mm) | Small electronics, routers, LED strips, some panels and stations | **Polarity varies by device**: centre-positive is common, not universal. **Check first** |
| **Ring and spade terminals** | Battery posts, fuse blocks | The workhorse of permanent 12 V wiring |
| **Alligator clips** | Testing and temporary connections | **Never for anything permanent or unattended** |
| **USB-A** | Older everything | About 5 V, low power |
| **USB-C** | Phones, laptops, modern power banks and panels | See below |

### USB-C Power Delivery
- **USB-C can carry far more than 5 V.** With **Power Delivery (PD)** the device and charger agree on a
  higher voltage (commonly 9, 15 or 20 V), so one connector charges a phone or a laptop.
- **Not every USB-C cable carries full power.** Some are data-only or low-power; cables rated for the
  highest power are electronically marked. **A phone that charges slowly may just have the wrong
  cable.**
- **Buy a couple of known-good, high-rated USB-C cables and label them.** Test them. One in the
  go-bag and one in each vehicle (→ 22-05).
- **A 12 V to USB-C PD adapter** charges phones and laptops straight from a battery, a station's 12 V
  port or a vehicle with one conversion. One of the highest-value small purchases in this section.

### Polarity: the mistake that destroys things
**Reversed polarity on DC can kill a device instantly, and on a battery it can start a fire.**
- **Red, a marked stripe or a ridged conductor = positive** by convention. **Convention is not a
  guarantee** on salvaged gear.
- **Check with the multimeter before connecting.** Every time, on anything salvaged. A **minus sign**
  on the meter's reading means your probes are on the opposite conductors: the red probe is on
  negative.
- **Barrel jacks:** look for the polarity symbol printed near the socket.
- **Fuse the positive lead close to the battery** (→ 09-08). A fuse turns a polarity mistake into a
  blown fuse instead of a fire.

### Wire: what to keep and what to salvage
- **Thicker is safer.** Undersized wire heats up (→ 09-08).
- **Stranded flexes, solid does not.** Use stranded anywhere that moves or vibrates.
- **Extension cords are AC wire.** In a pinch they work as heavy DC wire, but keep them fully unrolled
  under load: a coiled cord heats (OSHA).
- **Worth salvaging:** jumper cables (very heavy), speaker wire, thermostat wire (light duty only),
  vehicle harnesses, welding cable.
- **Never assume a salvaged cable's rating.** If you cannot read a gauge marking, size
  conservatively.

### Testing before you connect anything salvaged
```
1. LOOK      Damage, corrosion, melted insulation, swelling, burnt smell?  -> reject
2. MEASURE   DC volts across the output. Note the POLARITY the meter shows.
3. COMPARE   Does that voltage match what the load expects? Within its range?
4. FUSE      Put a suitably rated fuse in the positive lead first.
5. CONNECT   Smallest, least valuable load first. Never a medical device first.
6. WATCH     Heat, smell, buzzing. Check it again after 10 minutes.
```
> **Never test a new supply on a phone or device that someone's health depends on.** Prove it on a
> headlamp or a cheap USB light first (→ 09-06).

## Gear and items

**Have it now (buy toward this):**

| Item | Why | Notes |
|---|---|---|
| **Multimeter** and a spare battery for it | The most useful electrical tool you can own | DC volts, AC volts, continuity |
| **12 V to USB-C PD adapter** | Charges phones with one conversion | High value |
| **Known-good, high-rated USB-C cables** | Cables fail more than batteries | Label and test |
| **12 V socket splitter with inline fuses** | One outlet into several, safely | → 09-08 |
| **Anderson Powerpole set and crimper** | Standardise DC connections | Hard to get wrong |
| **MC4 connectors, Y-branch pair and spanner** | Solar side, including salvaged panels | → 09-03 |
| **Assorted barrel-jack adapters** | Salvaged small electronics | Check polarity every time |
| **Ring and spade terminals, heat-shrink, crimper** | Proper battery connections | Not twisted wire and tape |
| **Inline fuse holders and assorted fuses** | Stops a mistake becoming a fire | → 09-08 |
| **Alligator test leads** | Testing only | Never permanent |
| **10 to 12 AWG stranded wire, red and black** | Fixing and extending | Buy more than you think |
| Electrical tape, heat-shrink, cable ties, marker | Labelling and insulation | |

**Scavenge or substitute:** jumper cables are excellent heavy DC conductors; vehicle 12 V sockets,
fuse blocks and harnesses are reusable (→ 09-13); computer power supplies, wall chargers and car
chargers are everywhere and each is a labelled DC source: **read the label, check with the meter,
then use it**.

## When it runs out
- **Runway:** connectors and wire do not wear out fast, but **every repair uses some**, and crimp
  terminals and fuses go fastest.
- **Ration:** reuse terminals where safe; **never reuse a fuse by bridging it. A bridged fuse is the
  most dangerous "repair" in this section.**
- **Resupply:** vehicles, appliances and abandoned electronics are full of wire, terminals and fuses
  (→ 09-13, → 22-02).
- **Substitute:** proper crimps > soldered joints > twisted and taped. All three beat nothing, but only
  the first two belong in anything left unattended.

## Phase notes
- **A (at home):** standardise now: one DC connector family, labelled cables, a stocked adapter kit.
- **B (moving):** the 12 V socket adapters, the USB-C PD adapter and known-good cables travel
  (→ 22-05).
- **C (settled somewhere new):** the adapter kit and multimeter let you use whatever you find. **Bring
  the connectors; you will not find the right ones when you need them.**

## Cross-references
→ 09-08 fusing and wire sizing, read before wiring anything · → 09-03 batteries and the MC4 polarity
check · → 09-06 charging medical devices · → 09-13 what to scavenge · → 09-09 the small build ·
→ 25-02 conversions and math · → 22-02 scavenging field guide

---
id: 09-08-wiring-and-safety
section: 09-power-and-energy
title: "12 V wiring, fusing and electrical safety"
version: 1
revised: 2026-11-16
layer: core
danger_level: critical
phase: [A, C]
tags: [power, wiring, fuses, 12v, dc, wire gauge, extension cords, safety, fire, electrical]
derived_from: [09-08-wiring-and-safety]
sources:
  - us-department-of-energy-solar-energy-technologies-of-2a534a
  - us-department-of-energy-consumer-guide-to-residentia-1d87da
  - nfpa-national-fire-protection-association-lithium-io-0c7d64
  - us-consumer-product-safety-commission-cpsc-what-to-k-3390a4
  - osha-electrical-safety-and-health-topics-a7a68f
related:
  - 09-02-solar-basics
  - 09-03-batteries-and-storage
  - 09-04-generators
  - 09-07-battery-chemistry
  - 09-09-small-solar-build
  - 09-12-ac-dc-cables-and-connectors
  - 12-03-burns
  - 16-01-essential-hand-tools
  - 24-01-skills-checklist
  - 29-04-ex04-electricity-in-the-house
  - 30-01-the-floors
  - 30-08-dc07-diy-cord-and-plug-conversion
cards: [DC-07]
explainers: [EX-02, EX-04, EX-12]
promote_when: []
photo_slots:
  - { id: wiring-diagram, caption: "Our 12 V system's wiring diagram with every fuse rating written on it" }
figures: []
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: null
---

# 12 V wiring, fusing and electrical safety

**What this page is for.** The rules that keep a battery system, a solar setup or a car-battery
inverter from starting a fire: wire sizes, fuses, working habits, and the AC side (inverters and
extension cords). Read it before you cut a single wire. Volts and amps are explained on → 29-02;
the house panel and breakers on → 29-04.

> **SAFETY. Low voltage is not low danger.** A 12 V battery bank will not shock you through dry
> skin, which is exactly why people get careless with it. What it *will* do is push **hundreds of
> amps** into a short circuit: enough to melt a wrench instantly, ignite wire insulation inside a
> wall or a joist, and start a fire behind something you cannot see. **Undersized wire and missing
> fuses are the most common causes of home-built off-grid fires.** The rules on this page are not
> optional: **fuse every conductor at the battery, size wire for current AND length, no bare
> terminals, and take off rings and watches before you touch a battery bank.**
> **Never connect a battery system, an inverter or a power station to house wiring.** Generators
> and house wiring are on → 09-04: **never connect a generator to house wiring without a transfer
> switch, interlock, or a cord-and-plug conversion with the main breaker locked off; never backfeed
> through an outlet** (it electrocutes line workers and neighbours and causes fires, → 30-01). Doing
> a cord-and-plug conversion yourself is a decision card: {{choice DC-07}} (→ 30-08). Anything else
> in a wall belongs to a qualified electrician (OSHA, Electrical).

## Do this now
- **Buy a fuse block, an assortment of fuses, and more wire than you think you need, heavier than
  you think you need.** Cheap now, unobtainable later.
- **Put a main fuse or breaker on the battery positive terminal, within inches of it.** If you do
  exactly one thing from this page, do that.
- **Get a proper crimping tool and heat-shrink terminals.** Twisted-and-taped joints are a common
  source of DC fires: a bad connection makes heat.
- **Fire extinguisher and smoke alarm in the room where the batteries live** (→ 09-03).
- **Cover the battery terminals** with boots or caps. {{#if has.young_child}}A young child with a
  spoon and an uncovered battery bank is a serious hazard.{{/if}}
- **Draw the wiring diagram on paper, with every fuse rating, and keep it in this binder.**
  {{photo wiring-diagram}}

## Why it works this way

### Why 12 V systems bite
Power is volts × amps. To deliver **600 W**:
- at **120 V AC** you need **5 amps**: thin lamp cord handles it.
- at **12 V DC** you need **50 amps**: cable about the size of jumper leads.

**Same power, ten times the current.** Every problem in DC wiring comes from that:
- **Voltage drop.** Resistance in a long, thin wire eats voltage. Lose 1 V out of 12 and you have
  lost over 8% of your power as heat in the wire. Aim to keep drop under **3%** on important runs.
  **Length matters as much as thickness**, and you must count **both** conductors (out and back).
- **Heat.** An undersized wire carrying 50 A gets hot along its whole length. Inside a wall, under
  insulation, or bundled, it can reach ignition temperature without tripping anything, because
  **there is nothing to trip if you did not fuse it.**
- **Connections.** A loose or corroded joint has resistance; resistance makes heat; heat raises
  resistance. That runaway is why crimped and sealed connections matter more in DC than people
  expect.

### Wire sizing (conservative planning guidance; check against a real ampacity table)
Lower gauge number = thicker wire. For a **12 V** system, keeping voltage drop reasonable, counting
the **round-trip** length:

| Current | ≤10 ft round trip | ≤20 ft | ≤30 ft |
|---|---|---|---|
| 5 A | 16 AWG | 14 AWG | 12 AWG |
| 10 A | 14 AWG | 12 AWG | 10 AWG |
| 20 A | 12 AWG | 10 AWG | 8 AWG |
| 30 A | 10 AWG | 8 AWG | 6 AWG |
| 50 A | 8 AWG | 6 AWG | 4 AWG |
| 100 A | 4 AWG | 2 AWG | 1/0 AWG |
| 200 A (inverter cables) | 1/0 to 2/0 AWG | 2/0 to 4/0 AWG | keep it short |

**Rules of thumb:** keep battery-to-inverter cables **as short as possible**; between two sizes,
**take the thicker**; prefer **fine-stranded copper** (marine or welding cable) over solid or
aluminium. **Never use aluminium wire on battery terminals.**

### Fusing: the rule set
**The fuse protects the WIRE, not the device.** Size it to the wire's capacity, not to what you wish
the device could draw.

1. **Main fuse or breaker at the battery positive, within about 7 inches of the terminal**, rated at
   or below the capacity of the cable it protects. This is the fuse that prevents the catastrophic
   fault.
2. **A fuse on every branch circuit**, at the source end, sized to that branch's wire.
3. **A fuse between the solar panels and the charge controller, and between the controller and the
   battery**, as the controller's manual says. **Three or more panel strings in parallel need a fuse
   on each string**; two do not.
4. **The inverter gets its own heavy fuse** (class T or similar): inverters pull very large currents.
5. **Use DC-rated fuses and breakers.** An AC-rated switch or breaker on DC can fail to break the arc:
   **DC does not pass through zero volts the way AC does, so a DC arc keeps burning.** That is why
   "it's just a light switch" is wrong on a 12 V system.
6. **Never replace a fuse with a bigger one to stop it blowing.** The fuse is telling the truth.
   Find the fault.

### Working habits
- **Take off rings, watches and metal bracelets.** A ring bridging a battery terminal heats red-hot
  and cannot be pulled off in time.
- **Insulate the wrench.** Tape all but the working end, or use insulated tools.
- **Disconnect negative first, reconnect negative last.** Then a slipped wrench touching the frame is
  harmless.
- **Cover every terminal:** boots, caps or heat-shrink.
- **Do not work on a live system tired, cold or rushed.** Most of these accidents happen at the end
  of a long day.
- **Reversed polarity kills electronics.** Reversing the leads on a charge controller or inverter
  usually destroys it instantly. **Check twice with the meter.** Red and black consistently; label
  both ends of every cable.
- **Strain relief and abrasion protection.** Wire rubbing on a metal edge eventually wears through and
  shorts. Use grommets, loom and clamps.
- **Keep DC wiring physically separate from house AC wiring**, and never run it into house circuits.

### The AC side
- **Pure sine inverters** for anything sensitive: medical gear, laptops, chargers. Modified sine can
  damage some devices and makes others buzz and run hot.
- **Ground the system as the inverter's manufacturer says.** Grounding on a portable system is
  subtle; follow the manual, do not improvise.
- **GFCI protection** (the outlets with test and reset buttons) on any outlet near water: kitchen,
  bathroom, outdoors.
- **Extension cords: heavier than you think, fully unrolled.** A coiled cord under load heats up; a
  16 AWG cord running a heater is a fire. Generator cords: → 09-04.
- **Never chain extension cords or power strips.**
- **Anything permanent, anything in a wall, anything touching house circuits: a qualified
  electrician**, except the cord-and-plug conversion if your household has chosen to do it
  ({{choice DC-07}}, → 30-08).

## Gear and items

**Have it now (buy toward this):**

| Item | Why | Notes |
|---|---|---|
| DC fuse block and assorted blade fuses | Branch protection | A wide spread of ratings |
| Main fuse and holder (ANL, MRBF or class T) | The battery-terminal fuse | The most important single part here |
| DC-rated breakers, a few sizes | Resettable; also a disconnect switch | **Must be DC-rated** |
| Battery cable: 4, 6, 8, 10, 12, 14, 16 AWG | You will always want more | Fine-stranded, marine or welding grade |
| Ratcheting crimper, lugs, heat-shrink | Good connections do not make heat | Cheap tool, prevents the common fire |
| Heat gun or lighter for heat-shrink | Sealed, waterproof joints | |
| Digital multimeter | Polarity, voltage, continuity, current | Learn it before you need it |
| DC clamp meter | Measures current without breaking the circuit | Diagnosis without disassembly |
| Terminal boots, wire loom, grommets, clamps | Prevent shorts and abrasion | |
| Insulated wrenches or tape | Prevents the dropped-wrench short | |
| Labels or tape and marker | Label both ends of every cable | |
| Fire extinguisher and smoke alarm | This page is about fire | In the battery room |

**Scavenge or substitute:**
- **Wire:** vehicle wiring harnesses, jumper cables (excellent heavy cable), welding leads, battery
  cables from scrapped vehicles, speaker wire (light duty only), house cable from construction (solid
  core: acceptable for fixed runs, poor where it flexes).
- **Fuses:** every vehicle has blade fuses in a labelled box, in exactly the ratings you want. **One
  of the best things to salvage from a vehicle.** Also fusible links and midi and maxi fuses.
- **Fuse blocks, switches, sockets and USB outlets** from vehicles, boats and RVs.
- **Connectors:** vehicle harness connectors, Anderson-style plugs from equipment (→ 09-12).
- **What you must not substitute: a fuse.** **Never use a nail, a bolt, foil or a coin in a fuse
  holder.** That is how a fault becomes a house fire. With no fuse of the right rating, use a smaller
  one and accept the nuisance trips.

## When it runs out
- **Wire, fuses and connectors are consumables** in an active system: corrosion, vibration, rodents
  and repairs eat them. Stock generously now; they do not expire.
- **Corrosion is the slow failure.** In an unheated or humid space, terminals corrode, resistance
  rises and things quietly get hot. Inspect each season: green or white powder, discolouration,
  melted insulation, anything warm to the touch under load. **A warm connector is a warning.**
- **Rodents chew wire** (→ 04-11). Run cable in conduit or loom and check after any rodent sign.
- **Substitute:** heavier salvaged cable can always replace lighter; a DC-rated breaker can replace a
  fuse; a switch plus a fuse can replace a breaker. **Nothing replaces the fuse itself.**
- **The skill is the real asset:** sizing wire, crimping a lug, reading a meter, finding a short.
  Practise it now on a bench in daylight (→ 24-01). Burns first aid: → 12-03.

## Phase notes
- **A (at home):** build it properly the first time, with real fuses and real crimps, where children
  cannot reach it. Label everything. Keep the diagram on paper.
- **B (moving):** a portable system is short runs and plug connections. Secure against vibration,
  protect against abrasion, fuse it anyway, keep cables out from underfoot.
- **C (settled somewhere new):** longer runs mean thicker wire and more voltage drop. This is where
  **24 V or 48 V** systems make sense: they cut current, and so wire size, proportionally.

## Cross-references
→ 09-03 batteries · → 09-04 generators, backfeed and house connections · → 09-07 battery chemistry
· → 09-09 small solar build (this page in practice) · → 09-12 connectors and testing · → 29-04
electricity in the house · → 30-01 the floors

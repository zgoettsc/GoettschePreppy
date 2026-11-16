---
id: 09-08-wiring-and-safety
section: 09-power-and-energy
title: "12 V wiring, fusing and electrical safety"
version: 2
revised: 2026-11-16
layer: core
danger_level: critical
phase: [A, C]
tags: [power, wiring, fuses, 12v, dc, wire gauge, extension cords, safety, fire, electrical]
derived_from: [09-08-wiring-and-safety]
sources:
  - victron-wiring-unlimited-r14
  - victron-awg-metric-chart-r14
  - trojan-users-guide-r14
  - renogy-rsp200d-g3-datasheet
  - cpsc-safety-alert-portable-generator-hazards-r8
  - osha-quickcard-portable-generator-safety
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
review_pass: { date: "2026-11-16", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "Backfeed floor as 30-01; wire table recomputed for 2.5% drop (Victron) within NEC copper ampacity (Trojan); fusing rules re-sourced to Victron and panel datasheet; unsourced 7-inch rule and 'most common cause' removed" }
---

# 12 V wiring, fusing and electrical safety

**What this page is for.** The rules that keep a battery system, a solar setup or a car-battery
inverter from starting a fire: wire sizes, fuses, working habits, and the AC side (inverters and
extension cords). Read it before you cut a single wire. Volts and amps are explained on → 29-02;
the house panel and breakers on → 29-04.

> **SAFETY. Low voltage is not low danger.** A 12 V battery bank will not shock you through dry
> skin, which is exactly why people get careless with it. What it *will* do is push a very large
> current into a short circuit: enough to melt a wrench, ignite wire insulation inside a wall or a
> joist, and start a fire behind something you cannot see. A short-circuited battery can cause a
> fire or an explosion, and undersized wiring or a bad connection can cause a fire (Victron Energy,
> Wiring Unlimited). The rules on this page are not optional: **fuse every conductor at the
> battery, size wire for current AND length, no bare terminals, and take off rings and watches
> before you touch a battery bank.**
> **Never connect a battery system, an inverter or a power station to house wiring.** Generators
> and house wiring are on → 09-04: **Never connect a generator to house wiring except through a
> transfer switch, or an interlock kit with the main breaker off. Never backfeed through an outlet
> with a double-male ("suicide") cord.** Backfeed electrocutes line workers and neighbours (→ 30-01;
> CPSC, Portable Generator Hazards). A cord-and-plug conversion is not a connection to house wiring:
> the appliance is unplugged from the house outlet and plugged into the generator cord, so nothing
> reaches the panel; doing that conversion yourself is a decision card: {{choice DC-07}} (→ 30-08).
> Anything else in a wall belongs to a qualified electrician (Victron Energy, Wiring Unlimited).

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
  lost over 8% of your power as heat in the wire. Victron advises aiming for a drop no bigger than
  **2.5%**: 0.3 V on a 12 V system (Victron Energy, Wiring Unlimited). **Length matters as much as
  thickness**, and you must count **both** conductors (out and back).
- **Heat.** An undersized wire carrying 50 A gets hot along its whole length. Inside a wall, under
  insulation, or bundled, it can reach ignition temperature without tripping anything, because
  **there is nothing to trip if you did not fuse it.**
- **Connections.** A loose or corroded joint has resistance; resistance makes heat; heat raises
  resistance. That runaway is why crimped and sealed connections matter more in DC than people
  expect.

### Wire sizing for a 12 V system
Lower gauge number = thicker wire. The table gives the **thinnest copper wire** that keeps the drop
at or under 2.5% (0.3 V) for the **round-trip** length (out and back added together), and that is
also within the wire's current rating. It is worked out from the copper resistance per metre in
Victron's AWG chart, and never goes below the current ratings Trojan prints for copper cable from
the National Electrical Code (75 °C insulation, air no warmer than 86 °F; Trojan, User's Guide).
In a hotter space, in a bundle, or under insulation, go one size thicker.

| Current | ≤10 ft round trip | ≤20 ft | ≤30 ft |
|---|---|---|---|
| 5 A | 14 AWG | 14 AWG | 12 AWG |
| 10 A | 14 AWG | 10 AWG | 10 AWG |
| 20 A | 10 AWG | 8 AWG | 6 AWG |
| 30 A | 10 AWG | 6 AWG | 4 AWG |
| 50 A | 6 AWG | 4 AWG | 2 AWG |
| 100 A | 2 AWG | 1 AWG | 1/0 AWG |
| 200 A (inverter cables) | 4/0 AWG | 4/0 AWG | 4/0 AWG; shorter is better |

To check another case: drop (V) = amps × round-trip metres × the ohms per metre for that gauge in
the chart (Victron Energy, AWG to Metric Conversion Chart); keep it at or under 0.3 V.

**Rules of thumb:** keep battery-to-inverter cables **as short as possible**; between two sizes,
**take the thicker**; prefer **fine-stranded copper** (marine or welding cable) over solid wire.
Aluminium has much higher resistance than copper for the same size (Victron's resistance table):
**do not use aluminium wire on battery terminals.**

### Fusing: the rule set
**The fuse protects the WIRE.** A fuse exists to stop too much current in a wire, which causes
overheating or fire. With one device on a circuit, the fuse matches the device's current rating or
the cable's, whichever is lower; with several devices, it matches the cable (Victron Energy, Wiring
Unlimited). Never size it to what you wish the device could draw.

1. **Main fuse or breaker on the battery positive, as close to the terminal as the holder allows**,
   rated at or below the capacity of the cable it protects. Every device on a battery is fused in
   its positive cable, after this main fuse (Victron). This is the fuse that prevents the
   catastrophic fault.
2. **A fuse on every branch circuit**, at the source end, sized to that branch's wire.
3. **A fuse between the solar panels and the charge controller** (Victron), **and between the
   controller and the battery**, as the controller's manual says. **Panel strings in parallel:**
   each panel's label gives a **maximum series fuse rating**. If the other strings together can
   push more current than that into a faulty string, every string needs its own fuse of no more
   than that rating. With two strings this usually cannot happen; with three or more it can.
   Example: two other panels of 11.05 A each can push about 22 A into a panel rated for a 20 A
   fuse (Renogy, RSP200D datasheet), so three in parallel need a fuse on each string.
4. **The inverter gets its own heavy fuse.** With lithium batteries, at least one fuse in the line
   must be able to break the very large short-circuit current a lithium bank can deliver (its
   "interrupt rating"); Victron names the class T fuse as one well suited to lithium systems.
5. **Use DC-rated fuses and breakers.** Not every fuse or breaker works on both AC and DC, and some
   DC breakers must be wired the right way round (Victron). **DC does not pass through zero volts
   the way AC does, so a DC arc keeps burning** where an AC switch would break it. That is why
   "it's just a light switch" is wrong on a 12 V system.
6. **Never replace a fuse with a bigger one to stop it blowing.** The fuse is telling the truth.
   Find the fault.

### Working habits
- **Take off rings, watches and metal bracelets** (Trojan, User's Guide: never wear jewellery or
  other metal objects when working on batteries). A ring bridging a battery terminal heats red-hot
  and cannot be pulled off in time.
- **Insulate the wrench.** Use insulated tools (Trojan; Victron), or tape all but the working end.
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
- **Extension cords: rated above the load, fully unrolled.** A cord's amps are on its jacket or
  tag; its watt rating must exceed everything plugged into it (CPSC, Portable Generator Hazards),
  and a light cord under a heating load (a heater, a kettle) overheats. Grounded three-prong cords
  only, undamaged (OSHA, Portable Generator Safety). Generator cords: → 09-04.
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
  **24 V or 48 V** systems make sense: the same power at 48 V is a quarter of the current at 12 V,
  and the voltage drop falls with it (Victron, Wiring Unlimited).

## Cross-references
→ 09-03 batteries · → 09-04 generators, backfeed and house connections · → 09-07 battery chemistry
· → 09-09 small solar build (this page in practice) · → 09-12 connectors and testing · → 29-04
electricity in the house · → 30-01 the floors

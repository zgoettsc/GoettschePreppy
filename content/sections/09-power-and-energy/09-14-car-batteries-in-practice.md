---
id: 09-14-car-batteries-in-practice
section: 09-power-and-energy
title: "Car batteries in practice: getting energy out and back in"
version: 2
revised: 2026-11-16
layer: core
danger_level: critical
phase: [A, B, C]
tags: [power, batteries, lead-acid, vehicle, hybrid, inverter, charging, jump-start, scavenging]
derived_from: [09-14-car-batteries-in-practice]
sources:
  - osha-batteries-and-battery-charging-29-cfr-1926-441-9def7d
  - cdc-carbon-monoxide-poisoning-basics-772153
  - us-consumer-product-safety-commission-cpsc-what-to-k-3390a4
  - stryten-battery-metrics-r14
  - optima-rc-vs-ah-r14
  - trojan-users-guide-r14
  - trojan-faqs-r14
  - victron-wiring-unlimited-r14
  - battle-born-bb10012i-manual-r14
  - resmed-airsense-11-user-guide-r14
related:
  - 09-03-batteries-and-storage
  - 09-04-generators
  - 09-06-charging-medical-devices
  - 09-07-battery-chemistry
  - 09-08-wiring-and-safety
  - 09-10-power-for-medical
  - 09-11-hand-and-alt-generation
  - 09-12-ac-dc-cables-and-connectors
  - 09-13-scavenging-electrical-power
  - 01-03-phase-b-movement
  - 08-02-carbon-monoxide-safety
  - 22-05-kit-vehicle
  - 30-01-the-floors
cards: []
explainers: [EX-02, EX-03, EX-14]
promote_when: [has.vehicle]
photo_slots:
  - { id: vehicle-battery-labels, caption: "The label on each vehicle's 12 V battery (Ah or RC) and where the jump point is" }
figures: []
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: { date: "2026-11-16", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "CCA/RC definitions (Stryten), Ah basis (OPTIMA); worked example at 12 V; voltages, cold capacity and starting-battery deep-discharge from Trojan; socket limit from Victron; unsourced 'dozen cycles' and fuse ranges removed" }
---

# Car batteries in practice: getting energy out and back in

**What this page is for.** How much energy is really in a car battery, the three ways to get it out,
the four ways to put it back, how to take one out of a vehicle safely, and the rules for hybrids,
whose 12 V battery is a different animal. Chemistry and resting voltages: → 09-07.

> **SAFETY. A car battery is the most dangerous-feeling-harmless object in the garage.** It will not
> shock you through dry skin, which is why people get careless with it.
> **(1) Explosive gas.** Charging batteries give off hydrogen; ventilation must prevent "the
> accumulation of an explosive mixture" (OSHA, 29 CFR 1926.441). **No sparks, flames or smoking near
> a charging battery. Never charge one in a sealed space.**
> **(2) Short-circuit current.** A wrench dropped across the terminals is a short circuit, and a
> short-circuited battery can cause a fire or an explosion (Victron Energy, Wiring Unlimited).
> Insulated tools, no rings or watches (Trojan, User's Guide).
> **(3) Acid.** OSHA requires face shields, aprons and rubber gloves for handling batteries, with
> drenching facilities nearby. **Eye protection, always.**
> **(4) Never charge a frozen battery** (Trojan), and never charge or jump one that is cracked,
> bulging or leaking.
> **(5) Engines.** Charging from a running vehicle: **never run a generator, charcoal, or any engine
> indoors, in a garage, or near an open window.** Carbon monoxide kills in minutes with no warning
> (→ 30-01; CDC, Carbon Monoxide Poisoning: Basics).

## Do this now
- **Read the label on each battery you own** and write down the **RC** (reserve capacity) or **Ah**,
  not just the CCA. CCA tells you nothing about how much energy is stored. {{photo vehicle-battery-labels}}
- **Buy a cheap voltmeter or multimeter** (→ 09-12). Resting voltage is your fuel gauge.
- **Buy one small inverter (150 to 300 W) with a 12 V plug, and one larger one (1,000 W or more) with
  battery clamps and an inline fuse.** Together they cover almost everything (→ 09-08).
- **Set the household rule now: the batteries in the vehicles you drive are not a power bank.** They
  are your ability to start and leave (→ 01-03). Hybrids are stricter still: read the box below.

## Why it works this way

### Hybrids are different
Everything below about worked examples, big inverters clamped to posts and harvesting energy assumes
a **conventional vehicle with a conventional starting battery.** A hybrid is a different machine:
- **Its 12 V battery is a small auxiliary battery**, not a starting battery. It boots the computers
  and closes the high-voltage contactors; the traction battery starts the engine. It is smaller than
  a normal starting battery, so **the arithmetic below does not apply to it. Do not deep-cycle it
  with the vehicle off:** take it low and the vehicle will not enter ready mode, the hybrid version of
  "will not start".
- **Draw power in ready mode** (→ 09-11): the vehicle maintains its own 12 V system and runs the
  engine only as needed. With ready mode on, the auxiliary-battery problem disappears. Same carbon
  monoxide rules: the engine starts by itself.
- **Jump rules differ.** Read the owner's manual for where the 12 V jump point is (the battery may
  not be under the hood) and what a jump does: on a hybrid it boots the computers. **Do not use a
  hybrid to jump-start another vehicle unless its owner's manual says you may:** its small 12 V
  battery and wiring are not a starting system. A dead **traction** battery is not a jumper-cable
  problem.
- **The high-voltage traction battery is not user-accessible. Never tap, probe or wire to it.**
  Orange cables mean hundreds of volts.
- **What still applies to hybrids:** the voltmeter habit, terminal care, the freeze and
  deep-discharge cautions, and the rule that the vehicle battery's job is mobility.

**Our vehicles:**
{{#each vehicles as v}}- {{v.type_text}} ({{v.fuel_text}}): battery Ah or RC ______ · conventional
  or hybrid ______ · jump point ______
{{else}}- None recorded.
{{/each}}

The rest of this page is for **conventional vehicles and the spare and scavenged batteries**
(→ 09-13).

### How much energy is in there
**The label usually shows CCA: ignore it for this.** Cold cranking amps measures a short, violent
burst to turn a starter. It says nothing about stored energy.

**What you want is Ah (amp-hours) or RC (reserve capacity, in minutes).** CCA (cold cranking
amps) is the current a battery can deliver for 30 seconds at 0 °F while staying at or above 7.2 V;
RC is how many minutes a new, fully charged battery can supply 25 A at 80 °F before falling below
10.5 V (Stryten Energy, Key Metrics of Battery Performance). Ah is usually measured over a 20-hour
discharge (OPTIMA, Reserve Capacity vs Amp Hour Ratings). If you only have RC:
```
Ah  ~=  RC (minutes) x 25 / 60   the amp-hours delivered in the RC test
                                 (25 A for RC minutes); the 20-hour Ah
                                 rating is usually somewhat higher
Wh  ~=  Ah x 12 V                (nominal)
```
**Worked example, a car battery with RC 100:**
```
RC 100 minutes  ->  100 x 25 / 60  ~=  42 Ah
42 Ah x 12 V                       ~=  500 Wh  ALL OF IT, on paper
Lead-acid: take only 50%           ~=  250 Wh
STARTING battery: less again; it is not built for deep discharges
Through an inverter: less again (its efficiency is on its label)
```

**What one car battery actually runs:**

| Load | Roughly |
|---|---|
| **Phone (10 to 20 Wh a day)** (→ 09-06) | **A week or more.** The best use of it |
| LED lantern or headlamps | Many nights |
| Laptop (50 to 60 Wh a charge, typical) | A few charges |
| CPAP (ResMed AirSense 11: typical 56 W) | About four hours: part of a night |
| **Refrigerator (1,000 to 2,000 Wh a day)** (→ 09-10) | **A few hours at most. Do not plan on it** |
| Anything with a heating element | **Minutes. Never** |

> **The lesson:** a car battery is a useful reservoir for **small DC loads and charging**, and
> nowhere near enough for refrigeration or heat. That is why medicine cooling has its own page
> (→ 09-10).

### Starting versus deep-cycle

| | **Starting battery** (cars, trucks) | **Deep-cycle** (marine, RV, golf cart, floor scrubber) |
|---|---|---|
| Built for | Short high-current bursts | Being drained and refilled again and again |
| Deep discharge | **Kills it quickly**: a starting battery "cannot withstand more than a few deep discharges before failure" (Trojan, FAQs) | Designed for it (still best kept to 50% or less; Trojan) |
| Use as storage? | Gently, in an emergency | **Yes: this is the one you want** |

Every abandoned RV, boat, golf cart and floor scrubber holds the better battery (→ 09-13).

### Getting energy out: three paths, best first
**1. Straight 12 V DC: the efficient path.** A socket adapter or clamps to a **12 V to USB-C PD
adapter** (→ 09-12). One conversion, no inverter idling. **For phones and medical devices this is the
right way** (→ 09-06).

**2. Small inverter (150 to 300 W) in the 12 V socket.** For small AC things. Limited by the socket
and its fuse: Victron warns that these plugs are not made for currents beyond about 10 A, and the
car's circuit may be fused lower (Victron Energy, Wiring Unlimited). Read the socket's fuse in the
owner's manual: watts ≈ fuse amps × 12. **Do not exceed it.**

**3. Large inverter (1,000 W or more) clamped to the terminals.** For real AC loads. Rules (→ 09-08):
- **Fuse the positive lead close to the battery**, sized to the cable.
- **Heavy, short cable:** a 1,000 W inverter at 12 V pulls 1,000 ÷ 12 ≈ 83 A before its own losses,
  more after them (cable sizes: → 09-08).
- **Connect the inverter's negative last; disconnect it first.**
- **Engine running for anything substantial** (outdoors, never in a garage), or you flatten the
  battery fast.

**Watch the voltage, not the clock** (resting, nothing connected for at least an hour; Trojan):
about **12.7 V full** for a flooded battery (12.8 V for AGM), **12.1 V at 50%** (12.2 V for AGM:
stop there), and about **11.8 V means only about 30% left** (Trojan, User's Guide). On a battery in
a vehicle you want to drive, **stop well above 50%.**

### Putting energy back: four ways, best first
**1. Alternator, through a proper charger or DC-DC charger** (→ 09-11). Controlled and fast. Run the
engine at a meaningful load **in batches**, not idling for hours: idling burns a lot of fuel for very
little power, and that fuel is also your range (→ 01-03). **Never in an attached garage** (CDC; CPSC,
Portable Generator Safety; → 08-02).

**2. Solar through a charge controller** (→ 09-02, → 09-09). The only renewable path: slow, silent,
every sunny day. **A panel connected straight to a battery with no controller will damage it.**

**3. Mains or generator AC through a proper battery charger** (→ 09-04). A smart charger with a
lead-acid profile; batch-charge while the generator is running for other loads anyway.

**4. Another vehicle, by jumper cables.** Emergency only. It moves charge crudely and does not fill a
bank.

**While charging (OSHA 1926.441):** ventilate; keep vent caps in place on flooded batteries to avoid
electrolyte spray; eye protection; no sparks or flames.

### Taking a battery out of a vehicle
```
[ ] Engine off, key out. Eye protection and gloves on.
[ ] DISCONNECT NEGATIVE (-) FIRST, then positive (+).
    Negative first means a slipped wrench touching the body cannot short anything.
[ ] Tape over the wrench, or use insulated tools. NEVER let a tool bridge the posts.
[ ] Release the hold-down clamp. Lift with your legs: they are heavy.
[ ] Carry and store UPRIGHT. Flooded batteries spill acid.
[ ] REINSTALLING: positive (+) FIRST, negative (-) LAST.
[ ] Store CHARGED, cool, and never fully flat.
```

### Building a small bank from several batteries
Worth doing at a settled site; not in a hurry.
- **Parallel for more capacity at 12 V** (all positives together, all negatives together).
- **Only parallel batteries of the same type, capacity and age, at the same state of charge**
  (Battle Born says the same for its lithium batteries: same state of charge before connecting).
  Otherwise the good one endlessly drains into the bad one.
- **Never mix lead-acid with lithium** in one bank (→ 09-07).
- **Fuse each battery's positive lead individually** (→ 09-08).
- **Ventilate**, and keep flooded batteries out of the living space (OSHA).
- **Use equal-length cables** to each battery (Trojan), or the nearest one does all the work.

### Keeping them alive
Lead-acid dies from neglect far more often than from use (→ 09-07):
- **Never leave one flat.** A flat battery sulfates and may not recover. A flat battery is also the
  one that **freezes** in winter, and **a frozen battery must never be charged or jumped.**
- **Top up flooded cells with distilled water only**, plates covered (Trojan).
- **Clean corroded terminals:** corrosion looks minor and destroys capacity.
- **Cold cuts capacity a lot.** Trojan's figures: at 0 °F a battery delivers about 50% of its
  rated capacity (→ 09-05).
- **Recharge promptly after every use.** That one habit is most of a battery's life.

### The rule that outranks all of this
**Do not flatten the battery in a vehicle you may need to drive.** The vehicle is your way out
(→ 01-03), it can be shelter, and it is your fastest charging source (→ 09-11). **Harvest from spare
and scavenged batteries first;** take an in-service vehicle battery down only for a phone, and only
when it will be recharged soon.

## Gear and items

**Have it now (buy toward this):**

| Item | Why | Notes |
|---|---|---|
| **Multimeter or voltmeter** | Your only fuel gauge | → 09-12 |
| **12 V to USB-C PD adapter** | The efficient path for phones and medical devices | → 09-06 |
| Small inverter (150 to 300 W, 12 V plug) | Small AC loads, no wiring | |
| **Large inverter (1,000 W or more) with clamps** | Real AC loads | **Fuse it** (→ 09-08) |
| **Inline fuse holders and fuses (100 A class and up)** | The difference between a mistake and a fire | → 09-08 |
| Heavy short cables, ring terminals, crimper | 12 V means big amps | → 09-12 |
| **Smart lead-acid battery charger** | Charging properly from AC | → 09-04 |
| **DC-DC charger** | The right way to charge from an alternator | → 09-11 |
| Charge controller | The only safe way to charge from a panel | → 09-09 |
| Heavy jumper cables | Emergency transfer; excellent salvage wire | → 09-13 |
| **Eye protection, rubber gloves** | OSHA requires them for a reason | |
| Terminal cleaner, distilled water, battery strap | Maintenance and carrying | |
| Vented battery box | Contains a flooded battery indoors | |

**Scavenge or substitute:** every vehicle, RV, boat, tractor, golf cart and mobility scooter holds a
battery, and **the deep-cycle ones are the prize** (→ 09-13). A 12 V bulb makes a crude load tester.
**A vehicle's own charging system will recharge a salvaged battery**: often the fastest route back to
usable power (→ 09-11).

## When it runs out
- **Runway:** a car battery is **hundreds of watt-hours per cycle**, not thousands: days of phone and
  light, **not refrigeration.**
- **Ration:** stop at 50% resting voltage, and much sooner on a battery you need for starting.
- **Resupply:** recharging is the resupply: alternator, solar or generator. **The battery is storage,
  never a source.**
- **Substitute:** solar with a controller is the only renewable input (→ 09-02). Salvaged lead-acid
  extends storage but generates nothing (→ 09-13).
- **The long view:** salvageable lead-acid degrades whether used or not: years, not decades.

## Phase notes
- **A (at home):** keep the vehicle batteries healthy and charged; harvest from spares, not from the
  vehicles you drive.
- **B (moving):** the vehicle battery's job is **starting the vehicle**. Charge phones and run a
  cooler only with the engine running or a hybrid in ready mode, and stop there (→ 22-05).
- **C (settled somewhere new):** the vehicle becomes a real power asset: alternator charging plus a
  salvaged deep-cycle bank, with solar as the daily input (→ 09-11, → 09-02).

## Cross-references
→ 09-07 chemistry, voltages and the 50% rule · → 09-13 finding more batteries · → 09-08 fusing, read
before clamping any inverter · → 09-12 connectors and testing · → 09-11 alternator charging and the
carbon monoxide rule · → 09-06 medical devices · → 22-05 the vehicle kit

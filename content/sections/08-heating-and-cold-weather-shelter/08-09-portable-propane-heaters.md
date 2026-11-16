---
id: 08-09-portable-propane-heaters
section: 08-heating-and-cold-weather-shelter
title: "Portable propane heaters (Buddy family): setup, safe use and troubleshooting"
version: 1
revised: 2026-11-16
layer: gear
danger_level: critical
phase: [A, C]
tags: [propane, portable heater, Buddy, unvented, oxygen depletion sensor, tip-over switch, 1-lb cylinder, 20-lb tank, hose, carbon monoxide, altitude]
derived_from: [08-09-mr-heater-buddy]
sources:
  - enerco-group-mr-heater-manufacturer-portable-buddy-r-759ce5
  - enerco-group-mr-heater-manufacturer-mh9bx-buddy-powe-d748af
  - nfpa-nfpa-58-liquefied-petroleum-gas-code-storage-of-13af35
  - ysn-flame-king-manufacturer-training-program-1a-fill-a69318
  - flame-king-manufacturer-1lb-refillable-lp-cylinder-1-4bb08a
  - cdc-carbon-monoxide-poisoning-basics-772153
  - cpsc-carbon-monoxide-fact-sheet-e97206
related:
  - 08-01-heating-one-room
  - 08-02-carbon-monoxide-safety
  - 08-04-emergency-heat-options
  - 08-06-improvised-shelter-warmth
  - 08-10-wick-kerosene-heaters
  - 06-05-alternative-fuels
  - 06-06-fuel-storage-safety
  - 07-05-propane-and-camp-stoves
  - 20-02-child-safety-offgrid
  - 23-02-master-consumables-table
  - 28-04-portable-heaters
  - 28-07-reading-your-own-gear
  - 29-01-ex01-fuels
  - 29-03-ex03-carbon-monoxide
  - 29-12-ex12-extinguishers-blankets-and-alarms
  - 29-14-ex14-reading-a-label
  - 30-01-the-floors
  - 30-02-dc01-unvented-heater-overnight
  - 30-03-dc02-propane-cylinder-indoors
  - 30-04-dc03-refilling-1-lb-cylinders
  - 08-05-hypothermia-frostbite
cards: [DC-01, DC-02, DC-03]
explainers: [EX-01, EX-03, EX-12, EX-14]
promote_when: [has.propane_heater]
photo_slots:
  - { id: propane-heater-setup, caption: "Our propane heater in the warm room: clearances, barrier, high and low openings" }
  - { id: propane-tank-outside, caption: "The 20-lb tank outdoors, upright, and the window or door the hose passes through" }
  - { id: propane-heater-plate, caption: "Our heater's data plate: model, BTU/h, certification, altitude and temperature limits" }
figures: [fig-propane-heater-hose-route]
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: null
---

# Portable propane heaters (Buddy family): setup, safe use and troubleshooting

**What this page is for.** How to set up, light, run, shut down and troubleshoot the small
portable propane heaters sold for indoor emergency use: the "Buddy" family (small, mid and large
sizes from one maker) and similar radiant heaters from other makers. The figures on this page come
from the owner's manual of one widely sold model, the Portable Buddy MH9BX (Enerco/Mr. Heater,
Portable Buddy Radiant Heater operating instructions and owner's manual). **Other sizes and makers
differ:** their spec tables are on → 28-04, and **your own heater's manual and data plate govern.**
Propane is explained on → 29-01, carbon monoxide (CO) on → 29-03.

> **SAFETY.** This is an **unvented** heater: it burns the room's oxygen and its exhaust stays in
> the room. "Approved for indoor use" means it has safety shutoffs; **it does not mean it cannot
> poison you.** Four rules from its manual and this binder: **(1)** a tested battery CO alarm is up
> **before** it is lit (→ 08-02); **(2)** the manual's fresh-air openings are open the whole time it
> burns; **(3)** never unattended; **(4)** a cylinder larger than 1 lb stays **outdoors**. **Fuel is
> never stored or transferred near an open flame or a running appliance** (→ 30-01). If the CO
> alarm sounds or anyone gets a headache, dizziness or nausea: heater off, everyone out, → 08-02.

{{#if has.propane_heater}}**Your household listed:** {{#each heaters as h}}{{h.kind_text}} {{h.model}}; {{/each}}Propane on hand: {{ gear.fuel.propane_1lb }} 1-lb cylinders, {{ gear.fuel.propane_20lb }} 20-lb tanks.{{/if}}

{{photo propane-heater-plate}}

## Do this now: the sequence, every time

1. **CO alarm first.** Battery in, hold TEST until it sounds. In the warm room at pillow height, on
   the wall opposite the heater, not above it, not in a still-air corner, not by an air opening
   (→ 08-02).
2. **Fresh air:** open the manual's openings (below) before lighting.
3. **Clearances:** 30 in above, 24 in in front, 6 in each side; on a level, hard surface out of foot
   traffic; children and pets kept back by a barrier (→ 20-02).
4. **Fuel:** a 1-lb cylinder attached outdoors, or a 20-lb tank **outdoors** on the maker's hose
   through a cracked window or door, with the fuel filter fitted. Soapy-water leak test on every
   connection.
5. **Light** by the steps below. **An adult stays in the room while it burns.**
6. **Shut down** before leaving the room: tank valve closed, let the line burn empty, knob to OFF.
7. **One fuel-burning heater at a time.** The manual says do not use other fuel-burning appliances
   inside.

## What "indoor-approved" means, and what it does not

The manual certifies the heater to **ANSI Z21.103, unvented portable gas camp heaters for indoor
and outdoor use,** and calls it a heater for **recreational and emergency indoor use**. Check the
data plate on yours for the certification mark (→ 29-14). Two built-in protections earn that:

- **Oxygen depletion sensor (ODS).** The pilot flame is set so that when the room's oxygen falls,
  the flame lifts off its sensor and the gas valve closes. **An ODS shutoff means the room ran short
  of air. It is a warning, not a nuisance.**
- **Tip-over switch.** Shuts the heater off if it tips or is knocked hard.

**Neither one measures CO.** A dirty burner, a blocked pilot, or a knob left between settings makes
CO while the oxygen is still fine. The manual itself warns that without enough air for burning and
ventilation the heater may give off excessive carbon monoxide. The alarm is your only CO detector
(CDC; → 08-02).

## The manufacturer's numbers (one model; check yours)

| Item | Portable Buddy MH9BX manual |
|---|---|
| Heat input | **4,000 BTU/h on LO, 9,000 BTU/h on HI** |
| Fuel use, shown as runtime | **3 to 6 hours per 1-lb cylinder; 48 to 110 hours per 20-lb tank,** shorter below 20 °F |
| Required fresh air | **9 square inches (a 3 × 3 in opening) at ceiling level and at floor level** |
| Other fuel appliances in the space | Not allowed |
| Permitted settings by room | Bathroom: LO only. Bedroom: HI or LO |
| Sleeping | "Never operate the heater while sleeping" |
| Clearances to anything that burns | Top 30 in, front 24 in, sides 6 in, rear 0 in |
| Safety devices | ODS and tip-over switch |
| Altitude | Weak burning and **possible shutoff above 7,000 ft** |
| Lowest room temperature on the spec plate | **0 °F** |
| Larger cylinder | Up to 20 lb, **only when the cylinder is outdoors**, on the maker's hose |
| Cylinders indoors | "Never bring a refillable propane cylinder indoors"; cylinders not connected for use are stored outdoors, not in a building or garage |

Source: Enerco/Mr. Heater, Portable Buddy owner's manual. Larger "Big Buddy" class heaters burn more
fuel per hour and smaller ones less; read yours (→ 28-04).

## Fresh air

- **Two openings of at least 9 square inches each: one high, one low.** In practice: a window or
  door cracked to give at least a 3 × 3 in opening near the ceiling, and another near the floor,
  for example an upper window sash dropped an inch across its width plus a door to the rest of the
  house open at the floor.
- A towel stuffed around a hose gap is a draught seal, **not** one of these openings.
- The heater also makes **water vapour**: condensation and damp bedding follow in a closed room, and
  damp bedding is a cold-injury risk (→ 08-05).
{{#if is.high_altitude}}- **Your home is above 5,000 ft.** The manual warns of possible shutoff
  above 7,000 ft. If it shuts off at altitude: fresh air, wait 5 minutes, relight.
{{/if}}
## Heat while people sleep

The manual says **never operate the heater while sleeping**. Running it overnight keeps the room
warm but leaves CO and fire with no one awake to catch them; turning it off means a cold night,
which matters most for babies and frail elders. The household decides on the card:
{{choice DC-01}} (→ 30-02). If the household's answer allows overnight use, on this class "lowest
setting" means **LO**, both openings open, the heater behind its barrier on the far side of the room
from the sleepers, and whoever checks looks at the burner tile, the alarm and the openings. **If you
wake to a cold heater, the ODS may have shut it off because the room was short of air: ventilate
before relighting.**

## Placement

| Direction | Minimum clearance to anything that burns |
|---|---|
| Top | 30 in |
| Front | 24 in |
| Sides | 6 in |
| Rear | 0 in |

Level, hard ground, out of traffic. Never on a bed, couch or rug edge (some carpet or vinyl may
discolour under it). **Never warm or cook food on it**: the manual says that can defeat the safety
systems. **Never move it while lit**: a bump trips the tip-over switch, and the grille is hot. Keep
door blankets, curtains and toys out of the clearances.

{{photo propane-heater-setup}}

## Cold-weather limits

The spec plate lists a **0 °F** minimum room temperature, and the manual says runtimes drop **below
20 °F**. With the tank outdoors on a very cold night, the propane itself is the limit: **a heater
that sputters or dies with the tank outside in deep cold has a cold-fuel (low-pressure) problem,
not an air problem.** Shelter the tank from wind, switch to a fuller tank, or use another heat
source. **Never warm a tank with a flame, a heater or anything but air.**

## Lighting, step by step (manual)

**With a hose to a 20-lb tank:**

1. Control knob at **OFF**. Swing the regulator outward.
2. Screw the **fuel filter** onto the heater's regulator, then the hose onto the filter; screw the
   hose's other end into the tank valve. Hand-tight; **no thread sealant**; do not overtighten.
3. **Open the tank valve.** Soapy-water test **both ends.** Bubbles mean a leak: stop.
4. Turn the knob to **PILOT** and press it in to spark. **With a hose, the first light takes
   longer**, because air in the hose has to clear. If it does not light, hold the knob down about
   **30 seconds**, release, and press again; repeat until the pilot lights.
5. Once the pilot lights, **keep holding the knob down 30 to 60 seconds** (this heats the pilot's
   sensor), then release. The pilot must stay lit.
6. Press slightly and turn to lock on **HI**; leave it on HI until the burner tile glows **bright
   orange** (a few minutes from cold). Then choose LO or HI. **Never leave the knob between the
   locked positions**: poor burning and more CO.

**With a 1-lb cylinder:** attach and remove it **outdoors only, with the heater cool and no flame
nearby**. Screw it in clockwise, hand-tight; soapy-water test; then steps 4 to 6. Only 1-lb
(16.4 oz) cylinders made for this purpose.

**Normal at first use:** smoke and smell from the grille paint (once), the reflector discolouring, a
narrow unlit border around the tile, condensation on the cylinder. **Not normal:** visible flames on
the tile; turn it off.

## Shutting down

- **Hose:** close the **tank valve first**, let the heater burn the gas left in the hose until it
  goes out, then press and turn the knob to OFF. If it was set up but never lit, the manual says
  purge the line **outdoors** by holding the control down.
- **1-lb cylinder:** knob to OFF; remove the cylinder **outdoors, once cool**. The manual says
  cylinders must be disconnected from the heater when not in use.
- The wire guard stays hot for a long time; let it cool before storing.

## The heat-powered fan (accessory)

The maker's add-on fan is **thermoelectric**: it runs on the heater's own heat, with no batteries or
electricity. Install it only with the heater **off and cool**, seated tight against the heater with
no gap. Light on **HI**; it takes **3 to 5 minutes** to start spinning, then LO is fine. **Never put
anything in front of or on the fan.** If it has not started after 15 minutes, shut down, cool, reseat
it and retry (Enerco/Mr. Heater, Buddy power fan installation instructions).

## The propane source

**Why a 20-lb tank lives outdoors:**

1. **Size.** A 20-lb grill tank holds about twenty times the propane of a 1-lb cylinder. A leak
   indoors is not a whiff; there is enough gas to make the air of a whole room explosive.
2. **It sinks and pools.** Propane is heavier than air (manual). It flows along floors, down stairs
   and into **basements**, below your nose, toward the furnace and water-heater flames.
3. **Warmth makes it vent.** A cold tank brought into a warm house builds pressure, and its relief
   valve can open and release gas indoors, by design.
4. **The rule says so.** The manual allows a cylinder of up to 20 lb **only when the cylinder is
   outdoors**, and says **never bring a refillable propane cylinder indoors**. The national
   propane code limits cylinders kept inside a home, attached garages included, to the 1-lb class
   (NFPA 58).

**The normal method:**

- **Tank outdoors,** upright, on a board off snow and ice, out of the wind if possible, valve closed
  until you are ready to light.
- **The maker's hose** through a cracked window or door at ground level; a towel around the gap so
  the hose is not pinched. The heater sits within the hose's reach of that window, which is why the
  warm room has to be chosen with this in mind (→ 08-01). **Never a fully below-ground room with
  propane.**
- **Fuel filter on.** The manual strongly recommends the maker's fuel filter with any remote tank,
  and requires it with some of its hoses: hoses shed an oily residue that clogs the regulator and
  pilot, and the manual's remedy for that is a new control valve and regulator. Check your hose's
  tag against the manual's accessory list. Replace the filter yearly; write the date on it.
- **Only the maker's hoses.** The manual forbids hand-made or third-party accessories.
- **Inspect the hose every use:** cracks, cuts, wear mean replace it first.
- **No second regulator.** The heater's own regulator must always be in place.

{{figure fig-propane-heater-hose-route}}

{{photo propane-tank-outside}}

**Bringing a tank larger than 1 lb inside** (for example when the window route is frozen shut) is a
trade-off between a cold room and a propane leak that pools at floor level until it finds a flame;
the manual and the propane code both say no. The household decides on the card, which lists the
conditions for each option: {{choice DC-02}} (→ 30-03).

## Refilling 1-lb cylinders

The green 1-lb cylinders are made to be filled once at the factory. Adapters sold for refilling them
from a 20-lb tank exist. The heater's maker allows only disposable 1-lb cylinders on the heater and
says never bring a refillable cylinder indoors; the refillable-cylinder maker says a disposable
single-trip cylinder must never be refilled. The risks are overfilling (a 1-lb cylinder has no
overfill stop, so an overfilled one vents gas when it warms indoors) and a worn valve leaking in the
room. Whether your household refills at all is a decision card: {{choice DC-03}} (→ 30-04).

**If the card's answer is to refill by weight, this is the cylinder maker's method** (YSN/Flame King,
Training Program 1A; Flame King, 1-lb refillable cylinder product information):

- **Only cylinders built and stamped as refillable.** The foot ring carries the specification, the
  **tare weight (TW, the empty weight)**, the date made, and a 12-year requalification requirement.
  **Never refill a disposable (single-trip) cylinder.**
- **Outdoors, away from any flame or spark,** gloves and long sleeves: liquid propane causes
  frostbite burns.
- Supply valve **closed** before connecting. **Turn the 20-lb tank upside down** in a stable stand
  so liquid flows, and **never leave it inverted longer than 10 minutes.**
- **Never put a refillable 1-lb cylinder in a fridge or freezer,** and never use one that has been
  in one.
- **Fill limit:** the rated content is **16.4 oz (about 1 lb) of propane**, which leaves room for
  the liquid to expand. **Full weight is the stamped TW plus 1 lb, never more.** Example from the
  training sheet: TW 1.5 lb + 1 lb = 2.5 lb full. Weigh every filled cylinder on a kitchen scale.
  Cylinders with a bleed valve show **white fog at the bleed vent when 80% full: stop at once.**
- **Overfilled:** bleed it down outdoors until the weight is right. **Leaking:** set it outdoors away
  from everything; do not use it.
- **Soapy-water test** the filled cylinder's valve. **Retire any cylinder that hisses or whose valve
  is bent or stiff.**
- Put the 20-lb tank back **upright**, valve closed.

## Troubleshooting (manual)

| Symptom | Likely cause | Fix |
|---|---|---|
| **No spark** when the knob is pressed | Broken electrode, loose igniter wire, bad igniter | Parts replacement, not a field fix. Use other heat (→ 08-04) |
| **Spark but no pilot** | No gas: tank valve closed, tank empty, 1-lb not fully seated | Open the valve; change cylinder outdoors; check the filter is fitted where required |
| | Air in the hose (first light) | Hold the knob in at PILOT about 30 s, release, repeat |
| | Knob not exactly at PILOT; pilot blocked | Reseat at PILOT; clean the pilot with air (never a needle or wire) |
| **Pilot goes out when the knob is released** | Not held long enough | Hold 30 to 60 s after it lights |
| | Pilot flame not reaching its sensor; tip-switch wires loose | Clean the pilot; reconnect tip-switch wires |
| **Burner tile will not light** | Burner orifice blocked; knob not locked on HI | Lock on HI; clean per manual |
| **Shuts off after running** | **ODS tripped: the room is short of air** | **Stop. Do not just relight.** Open both openings, wait 5 minutes, relight. If it keeps happening, stop using it |
| | Bumped or tipped | Set it level, out of traffic; relight |
| | Oily contamination from a hose without a filter | New control valve and regulator; this is why the filter is on |
| **Weak flame, short runtime in deep cold** | Cold tank, low pressure | Use a 20-lb tank; shelter it from wind; never heat it |
| **Flames on the tile, yellow pilot, flame rolling over the top** | Dust, lint or spider webs inside | Off; cool; clean per manual. Persistent: service |
| **Smell of gas** | Leak at a connection, hose or cylinder | **Light nothing. Put out flames. Close the tank valve. Leave, and air the space at least 5 minutes.** Soapy-water test every joint. Propane sinks: smell low. **Persistent smell: everyone out; call the gas supplier or fire department from outside** |
| **Fan not spinning** | Takes 3 to 5 min on HI; not seated; blocked | Wait on HI; after 15 min shut down, cool, reseat |
| **CO alarm sounds, or headache, dizziness, nausea** | CO | **Heater off, everyone out to fresh air**, → 08-02 |

## Gear

| Item | Why | Notes |
|---|---|---|
| The heater, its manual, its data plate photographed | Your model's numbers | Keep the manual in its bag |
| **Battery CO alarm** | No alarm, no heater | → 08-02 |
| The maker's hose and fuel filter | 20-lb tank stays outdoors | Spare filter; replace yearly |
| 1-lb cylinders and/or 20-lb tanks | Fuel | Stored outdoors (→ 06-06) |
| Soapy-water spray bottle | Leak test every connection, every time | Dish soap and water |
| Barrier | Children and pets | → 20-02 |
| Extinguisher | The fire that gets past the heater | → 29-12 |
| Refillable cylinders, adapter, kitchen scale | Only if the card says refill | → 30-04 |

**There is no substitute for the CO alarm.** Neighbours' grill tanks fit the maker's hose.

## When it runs out

- **Runtime:** use the manual's figures above: 3 to 6 hours per 1-lb, 48 to 110 hours per 20-lb, less
  in deep cold. Log cylinders on → 23-02. Propane is often shared with cooking and the generator
  (→ 06-05): decide how it is split before the outage.
- **Ration:** burst-heat the warm room, then off; bedding and bodies carry most nights (→ 08-06).
- **Substitute:** a wick kerosene heater (→ 08-10), then insulation and layers (→ 08-06).

## Phase notes

- **A (at home):** the warm-room heater with the tank outdoors and the hose through a window, alarm
  first, never unattended.
- **B (moving):** the manual forbids use in a moving vehicle. Never as a sleeping heater in a tent or
  car (→ 08-02).
- **C (established somewhere else):** the same rules. The manual allows a cabin with a window or roof
  vent that gives the required openings.

---
id: 09-03-batteries-and-storage
section: 09-power-and-energy
title: "Batteries and power stations"
version: 3
revised: 2026-11-16
layer: core
danger_level: critical
phase: [A, B, C]
tags: [power, batteries, storage, power station, lifepo4, lead-acid, solar input, series, parallel, fire, safety]
derived_from: [09-03-batteries-and-storage]
sources:
  - usfa-battery-fire-safety-r14
  - usfa-blog-lithium-ion-batteries-2026-r8
  - osha-batteries-and-battery-charging-29-cfr-1926-441-9def7d
  - victron-wiring-unlimited-r14
  - trojan-users-guide-r14
  - trojan-battery-maintenance-r14
  - trojan-faqs-r14
  - battle-born-bb10012-data-sheet-r14
  - battle-born-temperature-limits-r14
  - battle-born-bb10012i-manual-r14
  - bluetti-ac180-user-manual
  - anker-solix-c1000-gen-2-user-guide
  - ecoflow-river-2-pro-user-manual
  - ecoflow-delta-2-max-user-manual
  - jackery-explorer-2000-plus-user-manual
  - generac-gp3500io-owners-manual
  - renogy-rsp200d-g3-datasheet
  - dometic-cfx3-35-product-page-r14
related:
  - 09-01-power-priorities
  - 09-02-solar-basics
  - 09-04-generators
  - 09-05-solar-in-winter
  - 09-07-battery-chemistry
  - 09-08-wiring-and-safety
  - 09-10-power-for-medical
  - 09-16-outage-day-one
  - 28-01-power-stations
  - 28-02-solar-panels-and-controllers
  - 28-07-reading-your-own-gear
  - 29-02-ex02-batteries-and-power-stations
  - 29-12-ex12-extinguishers-blankets-and-alarms
  - 30-01-the-floors
  - 30-08-dc07-diy-cord-and-plug-conversion
cards: [DC-07]
explainers: [EX-02, EX-04, EX-12, EX-14]
promote_when: [has.power_station]
photo_slots:
  - { id: station-ports, caption: "The back and front of each power station: solar input socket, 12 V port, AC outlets, the label with the input limits" }
  - { id: panel-labels, caption: "The label on the back of each solar panel (Voc, Vmp, Imp, Isc)" }
figures: [fig-series-vs-parallel, fig-mc4-polarity-check]
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: { date: "2026-11-16", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "Lithium safety re-cited to USFA (NFPA archive empty); storage charge per maker manuals (they differ); lead-acid voltages/DoD from Trojan; LiFePO4 cycles/cold limits from Battle Born and station manuals; cooler from Dometic; motor start 3x (Generac) R19: fridge Wh/day stated as 09-01's 1,000 to 2,000 Wh (estimate uses 1,200)." }
---

# Batteries and power stations

**What this page is for.** Storage, not generation, is what keeps a phone and a medicine cooler
alive through a night and a cloudy day. This page covers the two kinds of battery you will meet
(lithium iron phosphate and lead-acid), power stations versus home-built systems, how to look after
them, and how to connect solar panels to your stations without destroying them. What a power
station is, and volts, amps and watt-hours, are on → 29-02. Model-by-model station specs are on
→ 28-01.

> **SAFETY. Three ways batteries hurt people.**
> **(1) Lithium fire.** A damaged, defective or wrongly charged lithium battery can bulge, leak or
> catch fire; the fire is fast, very hot, hard to put out, and gives off harmful chemicals (US Fire
> Administration). **Stop using a battery that shows an odd smell, a change in colour, too much
> heat, a change in shape, leaking or odd noises** (USFA, Battery Fire Safety, from NFPA), or that
> is smoking, hissing, punctured or swollen (USFA). If it smokes or burns, get people out and call
> for help. Charge on a solid, flat surface, not a bed or couch, out of direct sun; store it away
> from anything that burns and away from exits (USFA). **Never charge a battery that has been
> damaged, crushed, punctured or soaked.**
> **(2) Lead-acid gas and acid.** Charging lead-acid batteries gives off gas that can form an
> explosive mixture, and they hold **sulfuric acid**. Ventilate, no sparks or flames nearby, face
> and eye protection and rubber gloves (OSHA, 29 CFR 1926.441; Trojan, User's Guide).
> **(3) Short circuit.** A short-circuited battery can cause a fire or an explosion, and a lithium
> bank can deliver a very large short-circuit current (Victron Energy, Wiring Unlimited). A dropped
> wrench across the terminals sets the wire, the tool and the room on fire. **Fuse everything**
> (→ 09-08). Take off rings and watches before working on a battery (Trojan).
> {{#if has.child}}**Children live in this house: batteries live where they cannot reach them, on a
> hard surface, with a working smoke alarm in the room.**{{else}}Keep batteries where children
> cannot reach them, on a hard surface, with a working smoke alarm in the room.{{/if}}
> **Never connect a power station's AC output to house wiring or into a wall outlet.** That is
> backfeeding, the same floor as for generators (→ 09-04, → 30-01).

## Do this now
- **Own one good lithium iron phosphate battery or one quality power station before anything else
  electrical.**
- **Put a fire extinguisher and a smoke alarm where the batteries live** (→ 29-12). Not optional
  with lithium.
- **Store each station and battery at the charge level its manual gives.** Makers differ: BLUETTI
  says 40 to 60% for an AC180 left unused over three months; EcoFlow says recharge a RIVER 2 Pro
  to 60% every three months; Anker says recharge a C1000 Gen 2 to 100% every three months; Battle
  Born says charge its 12 V batteries to 100% and disconnect them for storage. Ours: ______.
  **Whatever the manual says, when a storm is forecast, charge everything to 100%.** An outage
  that arrives with the station half full costs you half your reserve.
- **Exercise them every three months**, as most station manuals ask: note the charge you find (a
  unit that lost a lot in 90 days has a drain or a fault), discharge and recharge it as the manual
  says, return it to its storage level, check every port works, and **write it in the log**
  (→ 25-05). The failure you are guarding against is finding a dead unit after years of neglect.
- **Heat is the enemy of stored lithium:** room temperature, never in direct sun or a hot car
  (USFA). And **lithium batteries are not charged below freezing.** Station manuals list 32 °F
  (0 °C) as the lowest charging temperature (EcoFlow, Jackery, Anker), and so does USFA;
  discharging is allowed colder. Battle Born's 12 V batteries block charging in the cold and warn
  that charging at low temperatures can damage the cells.
- **Turn off any power-saving ("ECO" or auto-off) setting on a port that runs a medicine cooler.**
  A compressor cooler resting between cycles draws almost nothing, and a station set to switch off
  an idle output can mistake that for nothing plugged in. Find the setting in your manual and
  check the screen before the cooler goes on.
- **Fill in the station and panel tables below from the labels** (how: → 28-07), and take the
  photos: {{photo station-ports}} {{photo panel-labels}}
- **Buy several 20,000 mAh USB power banks.** About 70 Wh each (20 Ah × the cell's 3.6 to 3.7 V),
  cheap, no wiring, no knowledge needed, and they cover phone loads for days (→ 09-06).

## Why it works this way

**Batteries are rated three ways and you need all three:**
- **Capacity:** watt-hours, or amp-hours at a voltage (Ah × V = Wh). A 100 Ah lithium iron
  phosphate battery (12.8 V nominal) is about 1,280 Wh; a 100 Ah lead-acid battery at 12 V, about
  1,200 Wh.
- **Usable capacity:** what you can take out without wrecking it. This is where chemistries
  differ enormously (→ 09-07).
- **Continuous and surge current:** how fast you can pull it out. A big battery with a small
  inverter still cannot start a compressor.

**The comparison that decides a purchase:**

| | **Lithium iron phosphate (LiFePO4)** | **Lead-acid (AGM, flooded, gel)** |
|---|---|---|
| Usable depth of discharge | Up to 100% (Battle Born BB10012) | **50% or less recommended; 80% at most** (Trojan) |
| Cycle life | Thousands: 3,000 to 5,000 for one maker's battery (Battle Born) | Fewer; shallow discharges give longer life (Trojan) |
| Weight | Lighter for the same usable energy (BB10012: 31 lb for 100 Ah, all of it usable) | Heavy |
| Tolerates sitting part-charged | Yes | **No**: it sulfates and loses capacity (Trojan) |
| **Charging below freezing** | **No.** Makers set the limit at 32 °F (stations) or 25 to 32 °F (Battle Born) and the battery management system blocks it; a heated battery can charge colder | With temperature-compensated charging; **never charge a frozen battery** (Trojan) |
| Fire risk | Can overheat and burn if damaged or abused (USFA) | Explosive gas while charging, and acid |
| Can you find more in a crisis? | Rarely | **Everywhere: every car, truck, boat, RV** |

**Read the cold-charging row twice.** {{#if is.cold_winters}}Your winters here are cold enough that
this decides where the bank lives: **inside the heated space** (→ 08-01), not in the garage, a
shed or on the porch.{{else}}Even where winters are mild, a cold snap, a garage or a car in January
can put a battery below freezing.{{/if}} Many quality batteries include internal heating or a
low-temperature charge cutoff; check the spec sheet for that feature specifically.

**Power station or component system?**

*Power station* (one box: battery, inverter, charge controller, outlets):
- **For:** works out of the box, no wiring knowledge, portable, protected by design, one thing to
  grab in Phase B. **The right first purchase for most households.**
- **Against:** expensive per Wh, cells usually not repairable, and when the electronics fail the
  whole unit is gone. Expansion only with the maker's add-ons.

*Component system* (separate battery, controller, inverter: → 09-09):
- **For:** cheaper per Wh, **repairable and expandable**, any part can be replaced or scavenged,
  runs 12 V loads directly with no conversion loss.
- **Against:** you must understand fusing and wire sizing (→ 09-08) or you will start a fire.

For many households the answer is both: a power station as the grab-and-go and the simple backup,
and a component 12 V system as the house bank that can be repaired and grown.

### Our stations

{{#if has.power_station}}Total: **{{ gear.station_wh_total }} Wh** across all stations.{{else}}No
power station is recorded in this household's settings. If you get one, add it in the app; until
then use this table on paper.{{/if}}

Fill the blank columns from each station's label or manual (→ 28-07). The solar input numbers are
the ones that protect the station.

| Station | Wh | AC output W (continuous / surge) | Solar input: max volts | Solar input: max amps | Solar input: max watts | Number of solar inputs, socket type | Charging temperature range | Where kept |
|---|---|---|---|---|---|---|---|---|
{{#each stations as s}}| {{s.model}} | {{s.wh}} | ______ / ______ | ______ V | ______ A | ______ W | ______ | ______ to ______ °F | ______ |
{{else}}| ______ | ______ | ______ / ______ | ______ V | ______ A | ______ W | ______ | ______ to ______ °F | ______ |
{{/each}}

**Operating rules for any station:**
- **AC output never into house wiring** (above).
- **Idle draw is real.** With the AC inverter on and nothing plugged in, a station uses its own
  battery. Run DC loads from the 12 V and USB ports and switch the AC inverter off when you do not
  need it (→ 09-10). Measure yours: fully charged, inverter on, nothing plugged in, note the
  percentage after 12 hours.
- **Motor starts.** A motor (a blower, a pump, a compressor) needs a burst of extra power for a
  moment at start; Generac's rule for generators is to allow about 3 times the running watts.
  Check that against the station's surge figure before you rely on it. Some stations have a high-power mode meant for heating elements; read the manual for
  whether it suits motors.
- **UPS or pass-through mode.** Some stations can sit plugged into the wall with a load attached
  and switch to battery in milliseconds when the grid drops. If yours can, it is a good everyday
  home for a medicine cooler (→ 09-10). Read the manual's switchover time and whether the maker
  approves it for continuous use.
- **Temperature.** Station manuals list a charging range that starts at 32 °F (0 °C) (EcoFlow,
  Jackery, Anker). A station does not live in a parked car in summer or winter.

### Connecting solar panels to a station without destroying it

{{figure fig-series-vs-parallel}}

The full explanation is on → 09-02. In one breath: **series adds voltage** (current stays at the
weakest panel's level); **parallel adds current** (voltage stays near the lower panel's). **Too
much voltage destroys a station's solar input instantly and permanently; too much current is
normally just clipped.** Cold raises voltage, never current, so series is what winter can push over
a station's ceiling.

**Our panels** (from each label; {{#if has.solar}}total {{ gear.solar_w_total }} W{{else}}none
recorded yet{{/if}}):

| Panel | Watts | How many | Voc | Vmp | Imp | Isc | Measured Voc (multimeter, in sun) |
|---|---|---|---|---|---|---|---|
{{#each panels as p}}| {{p.model}} | {{p.watts}} | {{p.count}} | ______ V | ______ V | ______ A | ______ A | ______ V |
{{else}}| ______ | ______ | ______ | ______ V | ______ V | ______ A | ______ A | ______ V |
{{/each}}

(Voc: voltage with nothing connected. Vmp and Imp: voltage and current at full working output.
Isc: current if the leads were shorted. All are printed on the label; → 28-07.)

**Work out every configuration before the first connection.** For each one:
- **Series:** voltage = sum of the Voc of every panel in the string; cold voltage = that × 1.20
  (→ 09-02 for where 1.20 comes from and when to use more); current = the **lowest** Imp in the
  string.
- **Parallel:** voltage = the **highest** single Voc; cold voltage = that × 1.20; current = the
  **sum** of the Isc of all panels.
- **Compare with each station's input window.** The cold voltage must be below the station's
  maximum input voltage, with real margin. Current over the station's limit is clipped (a little
  harvest wasted), unless the manual sets a maximum short-circuit current, which you then respect.

| Configuration | Warm V | Cold V (× 1.20) | Current | Into which station? (OK / NEVER) |
|---|---|---|---|---|
| All panels in series | | | | |
| Two in series | | | | |
| Two in parallel | | | | |
| One panel alone | | | | |
| | | | | |

**Read the pattern in your own table.** A station with a high voltage ceiling and a low current
limit is a *series* machine. A station with a low voltage ceiling and a high current limit is a
*parallel* machine: it takes parallel pairs or single panels, and **never a series string whose
cold voltage reaches its ceiling, in any season.** Write your standing configurations here, pick
one each time, and do not improvise at first light:

1. ________________________________________ → ________________
2. ________________________________________ → ________________
3. ________________________________________ → ________________

The same table, cut down to a card, is on → 09-16; keep a copy with the panels.

**Rules that go with every configuration:**
- **Three or more strings in parallel need a fuse on each string**, no larger than the panel's
  maximum series fuse rating; two usually do not (→ 09-08 has the check).
- **Mismatch:** series cares about matched *current* (the string runs at the lowest Imp);
  parallel cares about matched *voltage*. Pair the most alike panels in parallel.
- **Measure the string's Voc with a multimeter before any first-time connection.** Red probe to
  the + lead (as marked on the panel label or cable), black to the − lead. A
  **minus sign** on the meter means a connector is reversed: swap it before anything is plugged
  in. A station's input may survive reverse polarity, but a reversed panel *inside* a series chain
  silently subtracts its voltage. {{figure fig-mc4-polarity-check}}
- **Connect in the order the station's manual gives.** Where it gives none, the safe habit is:
  panels positioned and chained first, cable laid, then plugged into the station, then the station
  switched on.
- **Suitcase kits with a separate controller box.** Some folding panels come with a small charge
  controller and clips meant for a 12 V car battery. That box puts out *regulated battery-charging
  voltage*, not panel power. **The controller box, its clips and its adapter tips never go into a
  series string and never into a power station.** Use the panel's own bare MC4 leads, and store
  the controller box separately so nobody grabs it in the dark.
- **Small stations have small limits.** A small DC-only or USB-class station can have an input
  voltage and wattage limit that one large panel exceeds on its own, especially cold. Run the same
  check for it; it usually gets only its own small panel.

Full input specs for common stations and panels: → 28-01, → 28-02.

### What a station runs (estimates; the percentage on the screen is the truth)
- **A typical full-size refrigerator** (about 1,000 to 2,000 Wh a day, → 09-01; this estimate
  uses 1,200 Wh): our station bank,
  {{ gear.station_wh_total }} Wh, runs one for roughly **{{ derived.station_fridge_days }} days**.
  That is an estimate: it assumes about 85% of the rated Wh is usable and does not count the
  station's own idle draw or anything else plugged in. **Measure your own:** fully charge, plug in
  only the fridge, and note the percentage every few hours for a day.
- **A small 12 V compressor medicine cooler** (one common 36-litre model is rated at 0.98 amp-hours
  per hour at 12 V in a 90 °F room, about 280 Wh a day; Dometic, CFX3 35): days per charge =
  station Wh × 0.85 ÷ (cooler Wh per day + 24 × idle watts). Work it per station on → 09-10.
- **Kettle boils:** about 135 Wh per one-litre boil once kettle and inverter losses are counted
  (→ 07-06). Boils per charge ≈ station Wh × 0.85 ÷ 135.
- **Phones, lights, radios, laptops:** trivially.
- **A furnace blower** only through a safe connection: a transfer switch or interlock fitted by an
  electrician, or a cord-and-plug conversion ({{choice DC-07}}, → 30-08; write-up on → 09-04).
  Check the blower's running watts and start surge against the station's figures first.

### Lead-acid: the scavenger's chemistry
In a long event, every abandoned car, truck, tractor, boat, RV and mobility scooter holds a
lead-acid battery. They are heavy, inefficient and short-lived, and they may be the only batteries
you can find in year two (→ 09-13, → 09-14).
- A **starting battery** (from a car) is built for short bursts, not deep cycling. It works as
  storage but dies quickly if deeply discharged again and again.
- A **deep-cycle battery** (marine, RV, golf cart, floor scrubber) is the one you want.
- **Only discharge to about 50%** (Trojan recommends 50% or less): about **12.1 V at rest** for a
  flooded 12 V battery, about **12.2 V** for an AGM. **Full reads about 12.7 V (flooded) or 12.8 V
  (AGM)** after resting with nothing connected. About 11.8 V on a flooded battery is only about 30%
  left: well past the line (Trojan, User's Guide). A cheap voltmeter is your fuel gauge (→ 09-07
  has the full table).
- Never mix old and new, or different types, in one bank.

**Capacity reality check.** With Tier 0 and Tier 1 loads of roughly 500 to 800 Wh a day, two to
three days of autonomy needs about **1.5 to 2.5 kWh of usable storage**: one or two 100 Ah
lithium iron phosphate batteries, a large power station plus a spare, or roughly **three to five**
100 Ah lead-acid batteries (about 600 Wh usable each, because of the 50% rule).

## Gear and items

**Have it now (buy toward this):**

| Item | Why | Notes |
|---|---|---|
| Lithium iron phosphate 100 Ah battery (one or two) | The house bank | **Insist on low-temperature charge protection or internal heating** |
| Power station, 1 to 2 kWh, pure sine | Grab-and-go; runs AC out of the box | → 28-01 for how to compare them |
| 20,000 mAh USB power banks (three or four) | About 70 Wh each; phones and small medical devices | Cheapest useful storage |
| Charger with a **lithium iron phosphate profile**; a lead-acid smart charger | The wrong profile ruins a battery | The lead-acid one is for scavenged batteries |
| Multimeter and a 12 V battery monitor | Your fuel gauge | A shunt-based monitor beats voltage alone on lithium |
| Fuses, breakers, correct wire | Prevents the fire this page warns about | → 09-08 |
| Fire extinguisher near the batteries, smoke alarm in the room | Lithium and electrical fires | → 29-12 |
| Vented battery box | Contains acid, keeps children out | **Required** for lead-acid |
| Insulated battery blanket or a warm interior spot | Cold stops charging | Cheaper than a new battery |
| Safety glasses and baking soda | Acid neutraliser for lead-acid | Keep both with the batteries |
| MC4 Y-branch pair, spare MC4 connectors, the station's own solar cable | Parallel wiring and repairs | → 09-12 |

**Scavenge or substitute:**
- **Vehicle batteries:** the most abundant storage in a town. Vehicles also give you alternator
  charging (→ 09-11).
- **UPS units** (computer battery backups): sealed lead-acid, often nearly new (→ 09-13).
- **Mobility scooters, wheelchairs, floor scrubbers, golf carts:** real deep-cycle batteries.
- **Cordless tool batteries:** usable with USB adapters for small loads.
- **Laptop and e-bike packs:** high energy and **the most dangerous to repurpose.** Use whole
  packs with their own charger; never take them apart.
- **What you cannot scavenge:** a proper charge controller and a good charger. Buy spares.

## When it runs out
- **Batteries die of age, deep discharge, heat and cold, and the death is often sudden.** Track
  real capacity: note how long a known load runs, and watch that number shrink. A bank that held
  two days and now holds half a day is telling you it is ending.
- **Runway:** lithium iron phosphate gives **many years** of daily cycling (3,000 to 5,000 cycles
  for one maker's battery) if never charged below its cold limit and never left flat. Lead-acid
  gives far fewer, and less again if regularly run below 50% or kept warm (Trojan: life halves for
  every 18 °F above 77 °F).
- **Ration:** shed loads by tier (→ 09-01). Charge and run loads during the sunny hours: power used
  while the sun is up is capacity you do not have to store.
- **Resupply:** scavenged lead-acid, in quantity, accepting the weight.
- **Substitute:** move loads off electricity entirely: light to lamps (→ 10-02), refrigeration to
  cold storage (→ 04-09, → 09-10), information to this binder on paper. **The final fallback for a
  phone is a hand-crank or vehicle charge** (→ 09-11).
- **End of life:** a dead lead-acid battery is still lead and acid. Do not burn it, do not open it,
  and keep it from freezing and splitting near children or the garden (a discharged battery
  freezes far more easily than a charged one; Trojan).

## Phase notes
- **A (at home):** house bank indoors in a warm room, fused, boxed, out of children's reach, smoke
  alarm overhead. Stations charged to storage level and staged where you can reach them.
- **B (moving):** the power stations and power banks go; a lead-acid bank does not (weight).
  **Charge everything to 100% before you leave.**
- **C (settled somewhere new):** build a larger bank in a space that stays above freezing. Collect
  scavenged lead-acid into a big, ugly, serviceable bank and keep the lithium for what has to be
  portable and reliable.

## Cross-references
→ 09-01 load triage · → 09-02 solar basics and the cold-voltage check · → 09-05 winter ·
→ 09-07 battery chemistry · → 09-08 wiring and fusing, read before wiring anything ·
→ 09-10 power for refrigerated medicine · → 09-16 outage day one and the hard-limits card ·
→ 28-01 power stations · → 28-02 panels and controllers · → 28-07 reading your own gear ·
→ 29-02 batteries and power stations explained

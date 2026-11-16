---
id: 09-07-battery-chemistry
section: 09-power-and-energy
title: "Battery types and chemistry (LiFePO4 versus lead-acid)"
version: 2
revised: 2026-11-16
layer: core
danger_level: critical
phase: [A, C]
tags: [power, batteries, chemistry, lifepo4, lead-acid, agm, nimh, bms, safety, cold]
derived_from: [09-07-battery-chemistry]
sources:
  - usfa-battery-fire-safety-r14
  - usfa-blog-lithium-ion-batteries-2026-r8
  - osha-batteries-and-battery-charging-29-cfr-1926-441-9def7d
  - trojan-users-guide-r14
  - trojan-battery-maintenance-r14
  - trojan-faqs-r14
  - battle-born-bb10012-data-sheet-r14
  - battle-born-bb10012i-manual-r14
  - battle-born-temperature-limits-r14
  - ecoflow-river-2-pro-user-manual
  - bluetti-ac180-user-manual
  - anker-solix-c1000-gen-2-user-guide
  - victron-wiring-unlimited-r14
related:
  - 09-02-solar-basics
  - 09-03-batteries-and-storage
  - 09-05-solar-in-winter
  - 09-08-wiring-and-safety
  - 09-09-small-solar-build
  - 09-13-scavenging-electrical-power
  - 09-14-car-batteries-in-practice
  - 14-08-ammunition-sourcing
  - 29-02-ex02-batteries-and-power-stations
  - 29-12-ex12-extinguishers-blankets-and-alarms
cards: []
explainers: [EX-02, EX-12, EX-14]
promote_when: []
photo_slots: []
figures: []
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: { date: "2026-11-16", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "Chemistry table and resting-voltage table re-sourced to Trojan and Battle Born (unsourced LiFePO4 voltage column and NiMH cycle figures removed); lithium safety to USFA; storage charge per maker; desulfator advice per Trojan" }
---

# Battery types and chemistry (LiFePO4 versus lead-acid)

**What this page is for.** The batteries you will meet, how each one is charged, stored and killed,
and how to read a battery's charge with a cheap voltmeter. → 09-03 covers choosing and using
batteries and power stations; → 29-02 explains the basic words.

> **SAFETY. Every chemistry on this page can hurt you in a different way.** Lithium can catch
> fire: a fast, very hot fire that is hard to put out and gives off harmful chemicals (US Fire
> Administration). **Stop using a battery that shows an odd smell, a change in colour, too much
> heat, a change in shape, leaking or odd noises** (USFA, Battery Fire Safety, from NFPA), or that
> is smoking, hissing, punctured or swollen; if it smokes or burns, get people out and call for
> help; do not try to carry a burning battery. Lead-acid holds **sulfuric acid** and gives off gas
> that can form an **explosive mixture** while charging (OSHA, 29 CFR 1926.441). **Any** battery
> large enough to be useful can push enough current through a dropped tool to start a fire or an
> explosion (Victron Energy, Wiring Unlimited). **Fuse everything
> (→ 09-08), keep batteries out of children's reach, and put a smoke alarm and an extinguisher in the
> room where they live** (→ 29-12).

## Do this now
- **Find out whether your lithium batteries and stations have low-temperature charge protection.**
  If they do not, they must live and charge indoors, above freezing, always.
- **Write the correct charging voltages for each battery on a label stuck to it.** The wrong charge
  profile is the most common way people quietly destroy a battery bank.
- **Get a multimeter and learn the resting-voltage table below.** On lead-acid, voltage is your fuel
  gauge and it is nearly free.
- **Never mix chemistries, ages or capacities in one bank.** The weakest battery drags the whole bank
  down and then fails early.

## Why it works this way

### The chemistries you will actually meet

| | **LiFePO4** | **AGM / sealed lead-acid** | **Flooded lead-acid** | **NiMH (AA/AAA)** |
|---|---|---|---|---|
| Usable depth of discharge | Up to 100% (Battle Born) | **50% or less recommended, 80% at most** (Trojan) | Same as AGM | Used to empty in normal devices |
| Cycle life | **Thousands:** 3,000 to 5,000 for one maker's battery (Battle Born) | Fewer; shallow discharges give longer life (Trojan) | Same, with watering and equalizing | Printed on the pack |
| Self-discharge | 2 to 3% a month (Battle Born) | Check voltage every 2 to 3 months in storage (Trojan) | 5 to 15% a month for lead-acid (Trojan); check every 4 to 6 weeks in storage | Varies; "pre-charged" types hold charge longest |
| Maintenance | None | None; **never add water** (Trojan) | **Distilled water top-ups** (Trojan) | None |
| Venting | Sealed | Releases gas, at a much lower rate than flooded (Trojan) | **Releases gas, most while charging: ventilate** (Trojan; OSHA) | Minor |
| **Charging below freezing** | **No.** Station makers set 32 °F; Battle Born's battery management system blocks charging below about 25 °F; a heated battery can charge colder | With temperature-compensated charging; **never charge a frozen battery** (Trojan) | Same as AGM | Check the pack |
| Freeze risk | Not charged cold; discharging allowed to about −4 °F (Battle Born) | **Can freeze if discharged** (Trojan) | **Can freeze and split if discharged:** at 40% charge the electrolyte freezes at about 16 °F; fully charged, about −92 °F (Trojan) | Low |
| Weight | **Lightest for the energy** (BB10012: 31 lb for 100 Ah, all usable) | Heavy | Heavy | n/a |
| Easy to find in year two | Rare | Common (UPS units, some vehicles) | **Everywhere** | Common |

LiFePO4 is lithium iron phosphate, the chemistry in most current power stations and "lithium" 12 V
batteries. AGM (absorbed glass mat) and gel are sealed lead-acid; flooded lead-acid has removable
caps and liquid you can see.

**In practice:** LiFePO4 for the main bank (light, deep cycles, long life, no maintenance), with
its cold limit respected absolutely, and **lead-acid as the scavenger's chemistry** you add in a long
event because it is in every abandoned vehicle.

### Depth of discharge: the idea that saves your money
Trojan, a deep-cycle battery maker, puts it plainly: shallow discharges give longer battery life;
discharges of 50% or less are recommended; 80% is the maximum safe discharge, and fully
discharging a flooded battery damages or kills it (Trojan, Battery Maintenance). **You do not "get
more" from a lead-acid battery by draining it deeper; you trade part of its lifetime for a little
extra today.** LiFePO4 is far more tolerant: Battle Born rates its battery for 100% depth of
discharge and 3,000 to 5,000 cycles.

**Resting voltage as a fuel gauge for lead-acid** (12 V battery, nothing connected and no charging
for at least an hour, longer is more accurate; Trojan, FAQs and User's Guide):

| State of charge | Flooded (12 V) | AGM (12 V) |
|---|---|---|
| 100% | 12.73 V | 12.84 V |
| 75% | about 12.4 V (between Trojan's 80% and 70% rows) | 12.54 V |
| **50%: the line to stop at** | **12.10 V** | **12.24 V** |
| 25% | about 11.7 V (between Trojan's 30% and 20% rows) | 11.94 V |

Gel batteries read differently again (Trojan's gel table: 12.84 V full, 12.36 V at 50%). **On
lithium, voltage is a poor gauge:** it barely moves across most of the range, so use the battery's
own monitor or app, or a **shunt-based battery monitor** (which counts the amp-hours going in and
out). Battle Born recommends disconnecting loads at 10.5 V; its battery management system cuts off
at 10 V.

### Charging: the part people get wrong
- **Each chemistry wants a different charging profile.** Always set the charger for the battery
  type (Trojan). Battle Born, for example, gives its own absorption (14.2 to 14.6 V) and float
  (13.4 to 13.8 V) voltages and says to disable temperature compensation, a lead-acid setting.
  Copy your battery's voltages from its datasheet onto the label; do not assume the default is
  right.
- **Lead-acid must be charged fully after each use**; left in a partial or discharged state it
  sulfates and loses capacity (Trojan).
- **Lead-acid gives off gas while charging: ventilate.** Flooded batteries need **distilled or
  deionised water** top-ups, never tap water, never acid; **never add water to AGM or gel**
  (Trojan).
- **LiFePO4 is not charged below its cold limit.** Discharging cold is allowed; charging at low
  temperatures can damage the internal cells, and a good battery management system blocks it
  (Battle Born). **Confirm yours does.** {{#if is.cold_winters}}With winters as cold as yours, this
  one line is why the bank lives in the heated room (→ 09-05).{{else}}Even in a mild climate, a
  garage or a car in a cold snap can be below freezing.{{/if}}
- **Heat is the other killer.** Lead-acid life halves for every 18 °F (10 °C) above 77 °F (Trojan);
  lithium makers also warn that sustained heat wears batteries faster (Battle Born). Cool, dry,
  above freezing, out of the sun.

### The battery management system: what you are really buying
A LiFePO4 "battery" is a pack of cells plus a **battery management system (BMS)**, and the quality of
the BMS *is* the product. It balances the cells, cuts off on over- and under-voltage, limits current,
and should **block charging below freezing**. A cheap pack with a minimal BMS is the one that swells,
fails or burns. **Buy the BMS, not the sticker capacity.**

### Storage and end of life
- **Store lithium at the charge its maker gives, cool and dry**, if it will sit for months. Makers
  differ: BLUETTI says 40 to 60% for its stations, EcoFlow 60%, Anker recharge to 100% every three
  months, Battle Born 100% and disconnected (→ 09-03). Store lead-acid **fully charged** and
  recharge it every 3 to 6 months, or it sulfates and dies (Trojan).
- **A swollen, hot, hissing or deformed lithium pack is a hazard, not a battery** (USFA). If it can
  be moved safely, get it outside onto a non-combustible surface away from anything that burns, and
  keep people away. Do not puncture it and do not throw it in a fire.
- **A dead lead-acid battery still holds lead and acid.** Do not burn it, do not open it; keep it
  away from children{{#if has.pets}}, pets{{/if}} and the garden. In a long event it is also lead you
  may want for other uses, with the cautions about lead exposure on → 14-08.

## Gear and items

**Have it now (buy toward this):**

| Item | Why | Notes |
|---|---|---|
| LiFePO4 batteries **with a quality BMS and low-temperature cutoff** | The core bank | Read the datasheet for cold-charge behaviour |
| Multi-chemistry smart charger | The right profile for each battery; recovers scavenged ones | LiFePO4 **and** AGM/flooded modes |
| Digital multimeter | Fuel gauge and diagnostic tool | Learn DC volts and DC amps |
| Shunt-based battery monitor | Voltage tells you little on lithium | Counts what went in and out |
| Hydrometer (for flooded lead-acid) | True state of charge, cell by cell | Cheap and definitive |
| Distilled water | Flooded battery top-ups | Never tap water |
| Baking soda, safety glasses, gloves | Acid neutraliser and protection | Store with the batteries |
| Vented battery box; hard non-combustible surface | Contains acid, keeps children out, contains a lithium event | Ventilation required for lead-acid |
| Smoke alarm and extinguisher in the battery room | Lithium fire response | → 29-12 |
| Terminal grease or anti-corrosion pads | Corroded terminals cause heat and voltage loss | Cheap |

**Scavenge or substitute:**
- **Flooded and AGM lead-acid** from cars, trucks, tractors, boats, RVs, UPS units, golf carts, floor
  scrubbers, mobility scooters. **Deep-cycle sources (golf cart, scrubber, marine) beat car starting
  batteries** (→ 09-13, → 09-14).
- **NiMH AA and AAA** from anything; they make every AA device rechargeable.
- **Small sealed lead-acid bricks** from alarm panels, emergency lights and exit signs: small, but
  numerous and often barely used.
- **A sulfated flooded battery** can sometimes be partly recovered with the equalizing charge its
  maker describes; Trojan advises against add-on "desulfator" devices, and **AGM and gel batteries
  are never equalized** (Trojan). **Do not open, refill with acid or "rebuild" a battery** (Trojan:
  never add acid), least of all with children around.
- **Do not** take lithium packs apart (laptop, e-bike, tool) to harvest cells. It is a common way
  people start fires.

## When it runs out
- **Batteries are the section's true consumable.** Panels, wire and mounts outlive them. Plan to
  replace storage, more than once, over a long event.
- **Runway:** LiFePO4 cycled daily and treated well gives **many years** (3,000 to 5,000 cycles is
  about eight to thirteen years of daily cycles). Lead-acid gives far fewer, and fewer again if run
  deep or kept warm (Trojan). Cycled to empty, charged cold or left flat, either can be finished in
  **months**.
- **Watch the decline:** log how long a known load runs. When a bank that held two days holds half a
  day, start sourcing the replacement.
- **Resupply:** salvaged lead-acid in quantity. A bank of matched salvaged deep-cycle batteries is
  heavy and needs ventilation and water, and it works.
- **Substitute:** shrink the load (→ 09-01), use power at midday so you store less, move to
  non-electric methods, and keep the good lithium **for Tier 0**. **The last battery in the house
  should be running the medical load and nothing else.**

## Phase notes
- **A (at home):** lithium bank indoors, warm, fused, boxed, alarmed. Salvaged lead-acid in a
  **ventilated** space above freezing: not a bedroom, not sealed.
- **B (moving):** lithium only, because of weight. Charge to 100% before leaving; keep packs inside
  your coat or the vehicle cabin, not an unheated trunk, and remember that in real cold you may be
  able to discharge but not charge.
- **C (settled somewhere new):** a proper battery room above freezing, ventilated, off the floor, out
  of the sun, with lithium as the daily driver and salvaged lead-acid as the bulk reserve.

## Cross-references
→ 09-03 batteries and power stations · → 09-05 winter and cold-charge limits · → 09-08 wiring and
fusing · → 09-09 small solar build · → 09-13 scavenging · → 09-14 car batteries · → 29-02
batteries explained

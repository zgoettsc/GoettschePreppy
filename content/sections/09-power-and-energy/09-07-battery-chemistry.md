---
id: 09-07-battery-chemistry
section: 09-power-and-energy
title: "Battery types and chemistry (LiFePO4 versus lead-acid)"
version: 1
revised: 2026-11-16
layer: core
danger_level: critical
phase: [A, C]
tags: [power, batteries, chemistry, lifepo4, lead-acid, agm, nimh, bms, safety, cold]
derived_from: [09-07-battery-chemistry]
sources:
  - nfpa-national-fire-protection-association-lithium-io-0c7d64
  - us-department-of-energy-solar-energy-technologies-of-2a534a
  - us-department-of-energy-consumer-guide-to-residentia-1d87da
  - noaa-national-weather-service-during-extremely-cold-9c1973
  - osha-batteries-and-battery-charging-29-cfr-1926-441-9def7d
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
review_pass: null
---

# Battery types and chemistry (LiFePO4 versus lead-acid)

**What this page is for.** The batteries you will meet, how each one is charged, stored and killed,
and how to read a battery's charge with a cheap voltmeter. → 09-03 covers choosing and using
batteries and power stations; → 29-02 explains the basic words.

> **SAFETY. Every chemistry on this page can hurt you in a different way.** Lithium can go into
> **thermal runaway**: an intense, self-sustaining, hard-to-extinguish fire with toxic smoke. The
> warning signs are **heat, an odd smell, swelling or a change of shape, leaking, smoke or unusual
> noise**; if you see any of them, get people out and call for help; do not try to carry the
> battery (NFPA, Lithium-Ion Batteries). Lead-acid holds **sulfuric acid** and gives off **explosive
> hydrogen** while charging (OSHA, 29 CFR 1926.441). Nickel-metal hydride (NiMH) and nickel-cadmium
> cells are milder but can vent and get very hot if shorted. **Any** battery large enough to be
> useful can push enough current through a dropped tool to start a fire. **Fuse everything
> (→ 09-08), keep batteries out of children's reach, and put a smoke alarm and an extinguisher in the
> room where they live** (→ 29-12).

## Do this now
- **Find out whether your lithium batteries and stations have low-temperature charge protection.**
  If they do not, they must live and charge indoors, above freezing, always.
- **Write the correct charging voltages for each battery on a label stuck to it.** The wrong charge
  profile is the most common way people quietly destroy a battery bank.
- **Get a multimeter and learn the resting-voltage table below.** Voltage is your fuel gauge and it
  is nearly free.
- **Never mix chemistries, ages or capacities in one bank.** The weakest battery drags the whole bank
  down and then fails early.

## Why it works this way

### The chemistries you will actually meet

| | **LiFePO4** | **AGM / sealed lead-acid** | **Flooded lead-acid** | **NiMH (AA/AAA)** |
|---|---|---|---|---|
| Usable depth of discharge | 80 to 100% | About 50% | About 50% | About 100% |
| Typical cycle life | **2,000 to 5,000+** | 300 to 600 | 500 to 1,200 if maintained | 500 to 1,000 |
| Self-discharge | Very low | Low | Moderate | Moderate (low on "pre-charged" types) |
| Maintenance | None | None | **Water top-ups; check the electrolyte** | None |
| Venting | Sealed | Sealed, low-pressure vents | **Vents hydrogen: ventilate** | Minor |
| **Charging below 32 °F** | **No: permanent damage** | Yes, at a reduced rate | Yes, at a reduced rate | Reduced; check the spec |
| Freeze risk | Damaged if charged cold | Can freeze if discharged | **Can freeze and split if discharged** | Low |
| Weight per usable Wh | **Lightest by far** | Heavy | Heaviest | n/a |
| Cost per usable Wh over its life | **Lowest** | Middle | Middle | High for large loads |
| Easy to find in year two | Rare | Common (UPS units, some vehicles) | **Everywhere** | Common |

LiFePO4 is lithium iron phosphate, the chemistry in most current power stations and "lithium" 12 V
batteries. AGM (absorbed glass mat) and gel are sealed lead-acid; flooded lead-acid has removable
caps and liquid you can see.

**In practice:** LiFePO4 for the main bank (light, deep cycles, long life, no maintenance), with
its cold limit respected absolutely, and **lead-acid as the scavenger's chemistry** you add in a long
event because it is in every abandoned vehicle.

### Depth of discharge: the idea that saves your money
A lead-acid battery taken to 50% might give 500 cycles. Taken to 80% it might give a fraction of
that. **You do not "get more" from a lead-acid battery by draining it deeper; you trade a large part
of its lifetime energy for a little extra today.** LiFePO4 is far more tolerant, which is most of why
it is cheaper over its life despite costing more up front.

**Resting voltage as a fuel gauge** (12 V nominal; measure after an hour with no load and no
charging; these are typical values, check your datasheet):

| State | Lead-acid (12 V) | LiFePO4 (12.8 V nominal) |
|---|---|---|
| 100% | about 12.7 V | about 13.4 V |
| 75% | about 12.4 V | about 13.2 V |
| **50%: the lead-acid floor** | **about 12.1 V** | about 13.1 V |
| 25% | about 11.9 V | about 12.9 V |
| Empty, stop | about 11.8 V and below = damage | about 12.0 V and below |

Notice how **flat the LiFePO4 column is**: voltage barely moves across most of its range. That is
why a **shunt-based battery monitor** (which counts the amp-hours going in and out) is worth far more
than a voltmeter on a lithium bank. On lead-acid, voltage works fine.

### Charging: the part people get wrong
- **Each chemistry wants a different charging profile.** A charger or controller set for lead-acid
  typically **undercharges** LiFePO4; a lithium profile applied to lead-acid can **overcharge and
  cook it**. Set the profile deliberately; do not assume the default is right.
- **Lead-acid must be brought to 100% regularly** or it sulfates and permanently loses capacity.
  **LiFePO4 does not need that** and is happiest not sitting at 100% for long periods.
- **Lead-acid gives off gas at the end of charge: ventilate.** Flooded batteries need **distilled
  water** top-ups; never tap water, never acid.
- **LiFePO4 must not be charged below freezing.** Discharging cold is usually allowed at reduced
  capacity; charging cold plates lithium metal inside the cell and **permanently damages it**,
  sometimes creating a hazard. A good battery management system blocks this automatically. **Confirm
  yours does.** {{#if is.cold_winters}}With winters as cold as yours, this one line is why the bank
  lives in the heated room (→ 09-05).{{else}}Even in a mild climate, a garage or a car in a cold snap
  can be below freezing.{{/if}}
- **Heat is the other killer.** Lead-acid life falls steeply above about 77 °F; lithium dislikes
  heat too. Cool, dry, above freezing, out of the sun.

### The battery management system: what you are really buying
A LiFePO4 "battery" is a pack of cells plus a **battery management system (BMS)**, and the quality of
the BMS *is* the product. It balances the cells, cuts off on over- and under-voltage, limits current,
and should **block charging below freezing**. A cheap pack with a minimal BMS is the one that swells,
fails or burns. **Buy the BMS, not the sticker capacity.**

### Storage and end of life
- **Store lithium at about 40 to 60% charge, cool and dry**, if it will sit for months. Store
  lead-acid **fully charged** and top it up regularly, or it sulfates and dies.
- **A swollen, hot, hissing or deformed lithium pack is a hazard, not a battery.** If it can be moved
  safely, get it outside onto a non-combustible surface away from anything that burns, and keep
  people away. Do not puncture it, do not put it in water, do not throw it in a fire.
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
- **Recovering a sulfated lead-acid battery** sometimes works with a long, low, controlled charge: a
  skill worth practising before you need it. **Do not open, refill with acid or "rebuild" a
  battery**, least of all with children around.
- **Do not** take lithium packs apart (laptop, e-bike, tool) to harvest cells. It is a common way
  people start fires.

## When it runs out
- **Batteries are the section's true consumable.** Panels, wire and mounts outlive them. Plan to
  replace storage, more than once, over a long event.
- **Runway:** LiFePO4 cycled daily and treated well gives **many years**. Lead-acid cycled daily to
  50% gives **one to a few years**. Cycled to empty, charged cold or left flat, either gives
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

---
id: 29-02-ex02-batteries-and-power-stations
section: 29-explainers
title: "Batteries and power stations: volts, amps, watts and watt-hours"
version: 2
revised: 2026-11-16
layer: explainer
danger_level: caution
phase: [A, B, C]
tags: [power, battery, power station, watt-hours, inverter, lithium, LiFePO4, lead-acid, solar, explainer]
derived_from: [09-01-power-priorities, 09-03-batteries-and-storage, 09-07-battery-chemistry, 09-12-ac-dc-cables-and-connectors, 09-14-car-batteries-in-practice, 25-02-conversions-and-math]
sources: [us-department-of-energy-consumer-guide-to-residentia-1d87da, us-department-of-energy-solar-energy-technologies-of-2a534a, nfpa-national-fire-protection-association-lithium-io-0c7d64, usfa-blog-lithium-ion-batteries-2026-r8, osha-batteries-and-battery-charging-29-cfr-1926-441-9def7d, osha-electrical-safety-and-health-topics-a7a68f]
related: [09-01-power-priorities, 09-02-solar-basics, 09-03-batteries-and-storage, 09-05-solar-in-winter, 09-07-battery-chemistry, 09-08-wiring-and-safety, 09-12-ac-dc-cables-and-connectors, 09-14-car-batteries-in-practice, 28-01-power-stations, 28-07-reading-your-own-gear, 29-04-ex04-electricity-in-the-house, 29-14-ex14-reading-a-label]
cards: []
explainers: [EX-04, EX-14]
promote_when: [experience.new]
photo_slots: []
figures: [fig-watts-and-watt-hours]
plates: []
condition: null
gear: null
explainer: EX-02
card: null
review_pass: { date: "2026-11-16", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "Arithmetic checked (100 Ah x 12 V; 1,000 Wh / 100 W); NFPA warning signs and OSHA 1926.441 hydrogen line as on 09-07; appliance figures labelled typical (accepted); lead-acid half-charge rule matches 09-03/09-07 and now points there." }
---

# Batteries and power stations, explained from the beginning

**What this page is for.** When the power is out, stored electricity is counted in four words:
volts, amps, watts and watt-hours. With those, you can read any battery or appliance label and
work out how long something will run. This page also says what a power station is, which
battery types last, and why a car battery makes a poor house battery.

> **SAFETY.** A lithium battery that is **hot, swelling, leaking, smoking, smells odd or makes
> an unusual noise** is a fire about to happen: get people away from it and call for help; do not
> carry it (NFPA, Lithium-Ion Batteries; USFA, Lithium-Ion Batteries: Everyday Convenience,
> Hidden Fire Risks). Lead-acid batteries give off explosive hydrogen while
> charging and hold sulfuric acid: charge them only where the air moves, with eye protection
> (OSHA, 29 CFR 1926.441).

## The four words

Think of water in a hose.

| Word | Symbol | Water picture | In plain words |
|---|---|---|---|
| **Volts** | V | Pressure | How hard the electricity pushes. A car battery is 12 V; a wall outlet is 120 V |
| **Amps** | A | How much water flows | How much electricity is moving right now |
| **Watts** | W | Pressure × flow | **Watts = volts × amps.** How fast something uses power while it runs |
| **Watt-hours** | Wh | Water in the bucket | **Watt-hours = watts × hours.** How much energy a battery holds, or a device uses over time |

A battery label may give **amp-hours (Ah)** instead. Turn them into watt-hours by multiplying by
the volts: 100 Ah at 12 V is 1,200 Wh. That is the nominal figure; you can safely use only part
of it (below).

**Household examples** (typical planning ranges; read your own appliance's label, → 29-14):

| Thing | Watts while running | Energy |
|---|---|---|
| Phone, full charge | — | 10 to 20 Wh |
| Electric kettle | 1,200 to 1,800 W | A few minutes per boil |
| Full-size fridge | 100 to 200 W while the motor runs | 1,000 to 2,000 Wh a day |

**The one sum to remember:** a 1,000 Wh battery runs a 100 W load for roughly 10 hours, less the
losses below. Heat-making things (kettles, heaters, hair dryers) use the most; lights, radios and
phone charging use the least.

{{figure fig-watts-and-watt-hours}}

## What a power station is

A **power station** is a battery in a box with everything needed to use it: a **charge
controller** (lets solar panels, a wall outlet or a car charge the battery safely), an
**inverter** (turns the battery's direct current into household alternating current, → 29-04),
and outlets (wall-style AC, 12 V car-style, USB). The label shows three numbers that matter:
**Wh** (how much it holds), **output watts** (the biggest load it can run at once), and the
**input** limits (how fast it can be refilled). → 28-01

**Why "watts in" is limited.** Every station has a maximum charging rate, and for solar a
voltage and current window printed on it. Panels connected beyond that window can damage the
station; inside it, the station takes only what it can. Panels also make much less than their
rated watts on short, low-sun winter days (US DOE, Solar Photovoltaic System Design Basics). → 09-02, 09-05

**Inverter losses.** Turning DC into AC wastes some energy as heat, and an inverter left switched
on draws power even when nothing is plugged in. Run 12 V and USB devices from the 12 V and USB
ports where you can, and switch the AC side off when you are not using it. → 09-12

## Battery types

| Type | What it is like | Watch out for |
|---|---|---|
| **Lithium iron phosphate (LiFePO4, "LFP")** | The usual chemistry in newer power stations. Light, lasts thousands of charge cycles, needs no maintenance, most of its capacity is usable | **Must not be charged below freezing** unless its battery management system blocks cold charging. Read the datasheet |
| **Other lithium-ion** (phones, laptops, tools, many older stations) | Light and powerful | Shorter life; more prone to fire when damaged. Never take packs apart |
| **Lead-acid (car, marine, AGM)** | Heavy, cheap, found everywhere | Using more than about half its charge shortens its life sharply; flooded types vent hydrogen and need distilled-water top-ups (→ 09-03, → 09-07) |
| **NiMH rechargeable AA/AAA** | Small, safe, common | Lose charge sitting on a shelf unless "pre-charged" type |

**Cold and heat.** Cold reduces what any battery delivers; lithium cannot be charged when
frozen. Heat shortens every battery's life. Keep batteries indoors, above freezing, out of the
sun. → 09-07

**Why a car battery is a poor house battery.** A car's starting battery is built to give a big
burst for a few seconds and then be recharged at once by the engine. Drained deeply, again and
again, it wears out quickly. A deep-cycle battery (marine, golf cart) is better, and a car can
still charge phones and small devices from its 12 V socket. Never run the engine in an attached
garage (→ 29-03). → 09-14

## This household

{{#if has.power_station}}Your power stations hold about {{ gear.station_wh_total }} Wh in total.
As a rough estimate, that would run a typical full-size fridge for about
{{ derived.station_fridge_days }} days with no recharging. Your own fridge and your own
percentage screen are the truth.{{else}}No power station is listed in your profile. A phone power
bank is the smallest useful battery; → 09-03 explains the sizes.{{/if}}
{{#if has.solar}} Your solar panels total {{ gear.solar_w_total }} W on their labels.{{/if}}

What to power first: → 09-01. Wiring and fuses: → 09-08.

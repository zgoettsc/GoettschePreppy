---
id: 10-06-winter-light-budget
section: 10-lighting
title: "The winter light budget (watt-hours, cells and fuel)"
version: 1
revised: 2026-11-16
layer: core
danger_level: none
phase: [A, C]
tags: [lighting, budget, watt-hours, batteries, NiMH, AA, AAA, power station, kerosene, winter, inventory]
derived_from: [10-06-winter-light-budget]
sources:
  - us-department-of-energy-solar-energy-technologies-of-2a534a
  - american-red-cross-power-outage-safety-6d07a8
  - us-fire-administration-fema-candle-fire-safety-use-f-6eeda1
related:
  - 06-06-fuel-storage-safety
  - 08-10-wick-kerosene-heaters
  - 09-01-power-priorities
  - 09-03-batteries-and-storage
  - 09-05-solar-in-winter
  - 09-06-charging-medical-devices
  - 09-16-outage-day-one
  - 10-01-lighting-options
  - 10-02-fuel-lamps-and-candles
  - 10-03-diy-and-conservation
  - 10-05-light-discipline
  - 22-04-household-inventory
  - 23-02-master-consumables-table
  - 26-09-shopping-list-and-budget
  - 29-02-ex02-batteries-and-power-stations
  - 30-18-dc17-old-fuel
cards: [DC-17]
explainers: [EX-02, EX-13]
promote_when: [is.cold_winters]
photo_slots:
  - { id: light-bin, caption: "Our lights and cells: where the bin lives and what is in it" }
figures: []
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: { date: "2026-11-16", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "Spot-checked: arithmetic (Wh tiers, kerosene 280 and 1,400 lamp-hours, cell counts) consistent; planning figures labelled; 85 percent usable matches 09-03; no changes." }
---

# The winter light budget (watt-hours, cells and fuel)

**What this page is for.** → 10-01 says which lights to use. This page works out what they cost
each night in stored power, how many rechargeable cells that takes per winter, how much lamp fuel
a winter would use, and whether it fits the power plan on → 09-01. A **watt-hour** (Wh) is a
measure of stored energy: one watt for one hour (→ 29-02). Every figure here is a planning number
for the type of device. Measure your own gear and write over the numbers in pen.

## Do this now

1. **Fill in the lights inventory** at the bottom of this page. Cells, fuel and chargers all start
   from knowing what the house holds. Ten minutes with a box.
2. **Measure your real lanterns and night lights** with a plug-in watt meter if you have one
   (→ 09-01), and correct the budget table.
3. **Know your tier:** AUSTERE is the life-critical floor; COMFORT is what a working household
   wants. Know which one tonight calls for.

## How long is your dark season?

Write down sunset and sunrise at home in mid-December, and how many nights of the year you need
light for a long evening:

- Hours of darkness in mid-December: ______ h
- Nights in the long-dark season: ______

{{#if is.cold_winters}}Your home has cold winters, which in the US mostly means the northern states,
where mid-December darkness runs to roughly 15 hours or more. Budget for the long end.{{else}}Your
winters are milder, and your December nights are likely shorter than in the far north, but they are
still long. Use your own numbers.{{/if}}

## The nightly budget: two tiers

**COMFORT: the full plan, about 45 to 50 Wh a night (planning figures)**

| Load | Draw | Hours a night | Wh a night |
|---|---|---|---|
| 2 LED lanterns (gathered room and kitchen), low to medium | about 3 W each | about 5 | about 30 |
| 2 night lights (stair top and bottom, or stairs and a child's room) | about 0.5 W each | about 12 | about 12 |
| Headlamps in use (low mode, everyone) | about 1 W (real low modes draw 0.1 to 0.5 W; 1 W is the cautious figure) | 2 to 3 in all | 2 to 3 |
| Topping up the bedside care headlamp (→ 10-01), plus charging losses | — | — | about 2 |
| **COMFORT total** | | | **about 45 to 50** |

**AUSTERE: the floor, about 15 to 20 Wh a night**

| Load | Draw | Hours a night | Wh a night |
|---|---|---|---|
| 1 LED lantern, low, one gathered room only | about 2 W | about 5 | about 10 |
| 1 night light: the stairs are never dark (→ 10-03) | about 0.5 W | about 12 | about 6 |
| Headlamps, including any night-time care job (→ 10-01) | about 1 W | 1 to 2 in all | 1 to 2 |
| **AUSTERE total** | | | **about 15 to 20** |

**How this fits → 09-01.** The power-priorities page puts "one reliable light source at night" in the
life-critical tier at **10 to 50 Wh a day**.

- **AUSTERE (15 to 20 Wh)** buys one lit gathered room for the evening, stairs that are never dark,
  and the night-time care light. It sits inside the life-critical line, and power banks alone can
  carry it for days. **This is the number the system is designed to defend.**
- **COMFORT (about 50 Wh)** adds a second lit workspace, a night light in each child's room, and a
  longer evening for reading, school work and morale (→ 21-04). The extra comes **from surplus**,
  on whichever station is fullest (→ 09-16), and it is the first lighting load dropped when the sun
  does not come out.

### Your stored power, in nights of light

{{#if has.power_station}}Your power stations:

| Station | Capacity |
|---|---|
{{#each stations as s}}| {{s.model}} | {{s.wh}} Wh |
{{/each}}| **Total** | **{{ gear.station_wh_total }} Wh** |

{{/if}}**The method:** nights of light = usable watt-hours ÷ Wh per night. Count about 85 percent of a
station's rated capacity as usable (inverter and other losses; → 29-02).

| | Usable Wh | ÷ Wh per night | = Nights |
|---|---|---|---|
| COMFORT | ______ | 50 | ______ |
| AUSTERE | ______ | 20 | ______ |

{{#if has.refrigerated_meds}}**Not from the medicine's station.** Count only the stations and banks
that are not keeping refrigerated medicine cold (→ 09-16).{{/if}} Light is cheap next to
refrigeration; the point of two tiers is knowing which one you are running.

## Cells per winter: the worksheet

Planning values: a **NiMH AA** rechargeable cell holds about **2.4 Wh** usable; a **NiMH AAA** about
**1.0 Wh** (1.2 volts times typical capacity). Assume about **500 recharges** per cell, so a cell
recharged daily lasts **three winters or more**. Rechargeable cells are a durable asset, not a
consumable, as long as the USB charger and a charging source last (→ 09-06).

**Fill in from your measured gear:**

1. Cells used up per day in AA and AAA devices (headlamps, night lights, a meter): **___ AA and
   ___ AAA.** (USB-rechargeable lanterns draw from power banks instead and do not count here.)
2. Times 2 for rotation: one set in the device, one on the charger: **___**
3. Times 2 again for a run of sunless days. Winter solar is feast or famine (→ 09-05): **___**
4. **Rechargeable stock to own = line 1 × 4.**

**Example:** a household using about 6 AA and 4 AAA a day on COMFORT needs about **24 NiMH AA and
16 NiMH AAA**.

**Alkaline reserve.** Alkaline cells keep for years and are the buffer when charging fails. Divide
the reserve by cells used per day. For example, 24 alkaline AA at 6 a day is about 4 days, around 5
with alkaline's better performance at low draw; at AUSTERE (2 to 3 cells a day) the same reserve
lasts about a week and a half. With the recharge loop running, the NiMH stock covers the whole
season, winter after winter.

**Without rechargeables:** 6 to 10 throwaway cells a day across a long winter is **on the order of a
thousand cells.** That one line is the whole argument for rechargeables and a charger (→ 09-06).

**Recharging in winter.** Your home gets about **{{ region.home.sun_hours_dec }}** peak sun hours a
day in December, against **{{ region.home.sun_hours_jun }}** in June. Winter is when you need the
most light and harvest the least, so size the cell stock for December (→ 09-05).

## Kerosene: gallons per winter

Planning figure: **a flat-wick kerosene lamp burns very roughly 1 ounce of fuel per lamp-hour**. It
varies with wick width and height: measure yours once and write it here: ______ oz per hour.

- **Backup use**, one lamp about 2 hours a night: over 140 nights that is about 280 lamp-hours, or
  roughly **2 to 2.5 gallons**. Adjust for your season length above.
- **Everyday use**, two lamps 5 hours a night over 140 nights: about 1,400 lamp-hours, roughly **11
  gallons**, plus wicks, chimneys, soot and carbon monoxide (→ 10-02). This is why kerosene is the
  backup and LED on stored power is the plan.

This household's kerosene: **{{ gear.fuel.kerosene_gal }} gal.**{{#if has.kerosene_heater}} **Your
kerosene heater burns the same fuel.** Every gallon in a lamp is hours of heat gone; look up the
heater's burn rate in its manual (→ 08-10). In winter, light with LEDs and save the kerosene for
heat.{{/if}}

- **Labels:** kerosene usually lives in **blue** cans, gasoline in **red**. Trust the label, not the
  colour: read it aloud, smell, then pour (→ 06-06).
- **Rotation:** date every can, burn the oldest first, keep cans full, sealed and dark, and jar-test
  before every fill: clear, no water layer, no cloudiness, no sludge (→ 06-06). Cloudy or wet
  kerosene fouls wicks, smokes and makes more carbon monoxide. How old is too old is a household
  decision: {{choice DC-17}} → 30-18.

## The seasonal correction

The budget is sized for the December worst case. In midsummer the nights are short, the lit evening
nearly disappears, and the budget falls to little more than the night lights, just when solar
harvest peaks. **Size everything to December. Do not size anything to July.**

## Lights inventory: fill this in

The binder does not know how many lights the house holds or where they are. Count once and write it
here; update it when things move. This table feeds → 22-04 and the cell targets above.

| Item | Count | Cell type or fuel | Where it lives |
|---|---|---|---|
| LED headlamps (red mode) | ___ | ___ | ___ |
| — of which: the bedside care light (→ 10-01) | ___ | ___ | bedside |
| — of which: its twin in the medical kit (→ 22-06) | ___ | ___ | medical kit |
| LED flashlights | ___ | ___ | ___ |
| LED lanterns | ___ | ___ | ___ |
| Night lights (stairs, children's rooms) | ___ | ___ | ___ |
| Solar path lights | ___ | solar | ___ |
| Kerosene lamps (→ 10-02) | ___ | fuel: ___ | ___ |
| Candles (count as hours, not sticks) | ___ h | wax | ___ |
| NiMH AA / AAA cells | ___ / ___ | — | ___ |
| Alkaline AA / AAA reserve | ___ / ___ | — | ___ |
| USB chargers for AA and AAA (→ 09-06) | ___ | — | ___ |
| Power banks | ___ | ___ Wh each | ___ |

{{photo light-bin}}

**Buy toward the gaps only.** The inventory decides the shopping list, not the other way round
(→ 26-09).

## When it runs out

- **The budget does not run out; the inputs do.** Track cells, the alkaline reserve and kerosene
  hours on → 23-02. The recharge loop (panel or station, then bank, then charger, then cells) is the
  renewable core; everything else is buffer.
- **What to drop when power is short:** the COMFORT extras first (second lantern, children's-room
  night lights, the long evening), then shorten the lit block. **The stair night light and the
  bedside care light go last, after everything else in the house.**
- **If the arithmetic stops working** (dead stations, dead cells), the answer is the conservation
  ladder on → 10-03, not more flame: shift the day to daylight, one room, sleep the long nights.

## Phase notes

- **A (sheltering at home):** run AUSTERE by default in a real outage, COMFORT when the stations are
  full and the sun is out. Power banks and the smallest station carry it either way.
- **C (settled somewhere new):** rebuild this table for the new place: different house, different
  stairs, a different length of dark. The lighting bin travels with its own copy of the inventory
  (→ 10-01).

---
id: 07-06-electric-kettle-cooking
section: 07-cooking-off-grid
title: "Electric kettle cooking from stored power"
version: 1
revised: 2026-11-16
layer: core
danger_level: caution
phase: [A, B, C]
tags: [electric kettle, power station, induction, solar, watt-hours, indoor cooking, no carbon monoxide, freeze-dried food]
derived_from: [07-06-electric-kettle-cooking]
sources:
  - cdc-carbon-monoxide-poisoning-basics-772153
related: [07-07-freeze-dried-rehydration, 07-02-rocket-stove, 07-05-propane-and-camp-stoves, 07-01-cooking-on-an-open-fire, 04-19-freeze-dried-stockpile, 08-02-carbon-monoxide-safety, 09-01-power-priorities, 09-02-solar-basics, 09-03-batteries-and-storage, 09-04-generators, 09-05-solar-in-winter, 09-10-power-for-medical, 09-16-outage-day-one, 28-01-power-stations, 29-02-ex02-batteries-and-power-stations, 29-14-ex14-reading-a-label, 02-04-cl04-food-allergy]
cards: []
explainers: [EX-02, EX-14]
promote_when: [has.power_station]
photo_slots:
  - { id: kettle-station, caption: "Our kettle: its rating plate (watts) and the station it plugs into" }
figures: []
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: null
---

# Electric kettle cooking from stored power

**What this page is for.** Using an electric kettle (and, optionally, an induction plate) run from
a power station or solar as an everyday stove in an outage: what it can cook, how much power it
takes, and when to stop and move to another method.

> **CAUTION.** This is the one cooking method that is safe **indoors**: no flame, no fuel, no
> carbon monoxide (CO). Every fuel-burning cooker stays outdoors (CDC, Carbon Monoxide Poisoning;
> → 08-02). The cautions here are electrical and thermal: a kettle draws a lot of power and must
> be budgeted against the station like any big load (→ 09-16), and a just-boiled kettle is a scald
> hazard. Pour at the counter; never carry boiling water over children.

## Do this now

1. **Read your kettle's rating plate** for its watts (→ 29-14), and your power station's label for
   its maximum continuous output. The kettle's watts must be **below** the station's output.
   Most kettles draw 1,200 to 1,800 W.
2. **Medical loads come first.** If anyone depends on a refrigerated medicine, oxygen or CPAP,
   that device's power is never the one spent on the kettle (→ 09-10).
3. **Boil in full litres, not cupfuls.** One litre is about two freeze-dried pouches (→ 07-07).
   Batching is free efficiency.
4. **Boil in the afternoon, from the day's solar surplus**, not at night from stored charge
   (→ 09-16).
5. **Fill vacuum flasks with every surplus boil** (→ 07-02): hot water banked is a boil you do not
   pay for twice.
6. **When the stations are low and there is no sun, stop** and move to the next method (→ 07-05,
   → 07-01, → 07-02), outdoors.

## Why / how it works

### Why a kettle, of all things

The general rule for stored power is **never make heat with electricity**: heat is what drains a
battery fastest (→ 09-01). Boiling small amounts of water is the exception, because a kettle puts
nearly all its energy straight into the water, and because much emergency food needs **only hot
water**: freeze-dried pouches (→ 04-19), instant staples, hot drinks, washing-up water.

**And it works in the cold, indoors.** Every other method in this section means standing over a
flame outdoors or at a vented hearth. The kettle runs **indoors, silently, with no CO and no fuel**,
in a closed-up room with the family around it.

### The power arithmetic

Words first (→ 29-02): **watts (W)** are how fast something uses power; **watt-hours (Wh)** are how
much energy it uses in total, and how much a battery holds.

- **Heating water takes a fixed amount of energy.** Heating 1 litre from cold tap water to boiling
  takes roughly 100 Wh of heat (physics: about 1.16 Wh per litre per °C). Add kettle and inverter
  losses and **plan on about 135 Wh out of the battery per one-litre boil**, the figure used across
  Section 09 (→ 09-03).
- **A freeze-dried pouch** takes about 2 cups (half a litre) of boiling water: roughly half a
  litre-boil.
- **Boils per full charge ≈ station Wh × 0.85 ÷ 135** (the 0.85 allows for the part of the battery
  you cannot use and inverter losses; → 09-03).

**Your stations:**
{{#each stations as s}}- {{s.model}}: {{s.wh}} Wh → ______ litre-boils per full charge
{{else}}- No power station entered.
{{/each}}
Total: **{{ gear.station_wh_total }} Wh** × 0.85 ÷ 135 = ______ litre-boils per full charge, before
any other load.

**Solar refill** ({{#if has.solar}}your panels total {{ gear.solar_w_total }} W{{else}}no panels
entered{{/if}}; method on → 09-02): daily Wh ≈ panel watts × peak sun hours × 0.75. At home that is
{{ gear.solar_w_total }} × {{ region.home.sun_hours_jun }} × 0.75 = ______ Wh on a clear June day,
and {{ gear.solar_w_total }} × {{ region.home.sun_hours_dec }} × 0.75 = ______ Wh on a clear
December day. Overcast days give far less, and snow on the panels gives nothing (→ 09-05).

**Measure it once:** boil 1 litre from cold on your station and write the station's own Wh
drop here: ______ Wh (date ______). That number replaces every estimate above.

{{photo kettle-station}}

### What boiling water alone cooks

- **Freeze-dried pouches** (→ 07-07) and anything labelled "add boiling water".
- **Instant staples:** oatmeal, instant rice and potatoes, couscous, quick noodles.
- **Hot drinks:** a big morale item in a cold house.
- **Washing-up and wash water**, including any allergy-safe cookware (→ 02-04).
- **Hot-water bottles** for beds: the same boil, one more job.

It does **not** fry, sear, simmer a pot or bake. For that, see induction below, or the fuel
methods.

### An induction plate: real cooking on stored power

A portable **induction plate** heats the pan directly with a magnetic field. Like the kettle it is
efficient, flameless and safe indoors, and it turns "boiling water only" into eggs, pancakes,
soup from staples and skillet meals. It needs **iron or steel cookware** (a magnet sticks to the
bottom); cast iron works (→ 07-04). Check that its watts fit under your station's output, and count
it like the kettle. It is an optional buy, not a requirement.

### Limits: read these before relying on it

- **One big load at a time.** A kettle at full draw leaves little room on most stations. Kettle
  **or** a furnace blower **or** heavy charging: one after the other, not together.
- **Never on the station that carries a medical device or a medicine fridge** unless you decide
  so deliberately, against that device's needs (→ 09-10).{{#if has.refrigerated_meds}} This
  household has refrigerated medicine.{{/if}}{{#if has.cpap}} This household uses CPAP.{{/if}}{{#if has.oxygen}}
  This household uses oxygen.{{/if}}
- **The kettle dies with the stations.** No sun, empty batteries and no generator to recharge
  (→ 09-04) means this method is over until recharge. Keep a **stovetop kettle** that works on
  every fuel.
- **A 12-volt kettle** on a vehicle or station 12 V socket avoids inverter losses but takes far
  longer per litre: background flask-filling only, never dinner.

## Gear / items

**Have it now (buy toward this):**

| Item | Why | Notes |
|---|---|---|
| Electric kettle, stainless inside | The everyday indoor stove | Watts below your station's output |
| Power station(s) | Stored power | → 28-01 |
| Solar panels | Daily refill | → 09-02 |
| Stainless vacuum flasks | One boil serves the day | Routine on → 07-02 |
| Whistling stovetop kettle | Works on every fuel when power is gone | |
| Induction plate (optional) | Real cooking, indoors, no CO | Needs iron or steel pans |
| Measuring cup | Exact water per pouch, no waste | Lives with the pouches (→ 07-07) |

**Scavenge or substitute:**

- Any household kettle whose rating plate fits your station.
- A coffee maker or electric skillet works but wastes power; prefer the kettle for anything that
  is really a water job. Check the watts first.

## When it runs out

- **Runway:** the station charge. Track it in litre-boils (about 135 Wh each) against the day's
  solar; → 09-16 decides which station carries what.
- **Ration:** flask every surplus boil (→ 07-02); cold-water rehydration of true freeze-dried
  pouches uses no energy (→ 07-07); hot drinks are the first thing cut; medical loads are never
  the cut.
- **Resupply:** sun (→ 09-05), a generator run outdoors (→ 09-04), then the fuel methods: propane
  (→ 07-05), wood (→ 07-01, → 07-02), outdoors.
- **In a long event,** electricity from the sun renews daily; propane does not. Use this method as
  long as the sun allows before spending tanks.

## Phase notes

- **A (at home):** the everyday indoor method, all winter, with combustion cooking outdoors as the
  backup.
- **B (moving):** the kettle travels with a station; boil at stops from vehicle charging or sun,
  and cold-rehydrate on the road.
- **C (establishing):** at a destination with a working gas range or hearth, the kettle becomes the
  quiet, fuel-free option rather than the only indoor one.

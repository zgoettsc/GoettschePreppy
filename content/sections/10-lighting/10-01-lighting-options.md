---
id: 10-01-lighting-options
section: 10-lighting
title: "Lighting options ranked (safety and runtime)"
version: 1
revised: 2026-11-16
layer: core
danger_level: caution
phase: [A, B, C]
tags: [lighting, LED, headlamp, lantern, batteries, AA, red light, power outage, children, night care]
derived_from: [10-01-lighting-options]
sources:
  - us-fire-administration-fema-candle-fire-safety-use-f-6eeda1
  - american-red-cross-power-outage-safety-6d07a8
  - nfpa-national-fire-protection-association-lithium-io-0c7d64
  - cdc-carbon-monoxide-poisoning-basics-772153
related:
  - 08-01-heating-one-room
  - 08-02-carbon-monoxide-safety
  - 09-01-power-priorities
  - 09-03-batteries-and-storage
  - 09-07-battery-chemistry
  - 09-08-wiring-and-safety
  - 09-16-outage-day-one
  - 10-02-fuel-lamps-and-candles
  - 10-03-diy-and-conservation
  - 10-04-candles-and-oil
  - 10-05-light-discipline
  - 10-06-winter-light-budget
  - 20-02-child-safety-offgrid
  - 21-02-long-haul-morale
  - 22-03-go-bags-and-kits
  - 22-06-kit-medical
  - 23-02-master-consumables-table
  - 29-02-ex02-batteries-and-power-stations
  - 30-21-dc20-open-flame-indoors
cards: [DC-20]
explainers: [EX-02, EX-03]
promote_when: []
photo_slots:
  - { id: bedside-lights, caption: "Each bed's headlamp, where it lives and where it charges" }
figures: []
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: null
---

# Lighting options ranked (safety and runtime)

**What this page is for.** When the power goes out, the house goes dark for many hours every
day. This page ranks the ways to light it, by safety first and then by how long each runs on what
you have stored. It explains why battery LED lights win, how to choose a light for each job, and
why the batteries, not the lights, are what you run out of.

> **CAUTION. In a power outage, use flashlights, not candles** (US Fire Administration, Candle
> Fire Safety). Every light that burns something is a distant second choice to an LED, and has
> its own rules on → 10-02. Nothing that burns fuel goes in a bedroom, near bedding, or left
> alone, and anything burning indoors needs a working carbon monoxide (CO) alarm (→ 08-02,
> → 29-03). Whether to use candles and oil lamps indoors at all is a household decision:
> {{choice DC-20}} → 30-21. **Children do not have access to firearms, fuel, medications or
> chlorine products.** Fixed in every source. Lamp oil counts.

## Do this now

1. **A headlamp beside every bed, one in each coat pocket, one by the back door.** Headlamps
   beat flashlights for almost everything: both hands stay free, which matters when you carry a
   child, cook on a fire or work on batteries.
2. **Use as few battery sizes as possible.** AA is the most common and the easiest to find.
   Rechargeable AA cells and a USB charger turn every light into one your stored power can
   refill. Any new light you buy should take the same cells as the rest.
3. **Test everything today.** Dead cells, corroded contacts and lights "in a drawer somewhere"
   are the usual outage discovery.
4. **Count the dark hours.** Look up tonight's sunset and tomorrow's sunrise, and do it again in
   December. {{#if is.cold_winters}}In a northern winter the dark lasts most of the day, for
   months.{{else}}Even in the south, winter nights are long.{{/if}} Light is a daily consumable,
   and it drives both your power budget (→ 09-01) and morale (→ 21-02). The arithmetic is on
   → 10-06.

{{photo bedside-lights}}

## The night light that is never optional

Some households have a job that must happen in the dark: checking blood sugar and drawing up
insulin, a night feed, putting on a CPAP mask or checking an oxygen line, giving a medicine on a
schedule.{{#if has.condition.CL-01}} This household has a member with type 1 diabetes (→ 02-01).{{/if}}{{#if has.condition.CL-02}} This household has a member on an insulin pump or sensor (→ 02-02).{{/if}}{{#if has.condition.CL-06}} This household has a member with type 2 diabetes on insulin (→ 02-06).{{/if}}{{#if has.infant}} There is an infant in this household: night feeds and changes need light.{{/if}}{{#if has.cpap}} A member uses CPAP.{{/if}}{{#if has.oxygen}} A member uses oxygen.{{/if}}
That job gets its own light, not "whatever is around":

- **A headlamp reserved for it, kept on charge at the bedside.** It never leaves the bedside and
  is never borrowed for the yard, the car or a game. The predictable failure is that it gets
  borrowed "just once" and is somewhere else at 3 a.m.
- **Red light to move, white light to read.** Red keeps your night vision and does not wake the
  house. But check before trusting it: some meter screens fade under red light, and syringe and
  dose markings are fine lines that need enough light to read **correctly**. **A misread dose is
  worse than lost night vision.** Use red to get up; use a short burst of white, aimed down and
  shielded, for reading and measuring. Test both tonight with the real meter or device.
- **A second identical headlamp in the medical kit** (→ 22-06): same model, same buttons, so the
  habit carries over and the bedside light and the grab-and-go light are never the same missing
  light.
- **The rule:** the night-time care job never depends on finding a light.

## The ranking

Rank every option on four things: safety, how long it runs on stored energy, how you get more,
and the quality of the light. LEDs win the first three so clearly that everything else is a
fallback.

| Option | Safety | Efficiency | How you get more | Verdict |
|---|---|---|---|---|
| **LED headlamp** | Excellent | Excellent: 30 to 150 hours on low | Rechargeable or AA cells | **First choice for tasks and moving around** |
| **LED lantern** (AA or USB-rechargeable) | Excellent | Excellent | Rechargeable or AA cells | **First choice for a room** |
| **LED flashlight** | Excellent | Excellent | Rechargeable or AA cells | Good, but uses a hand |
| **USB light run from a power bank or power station** | Excellent | Excellent | Solar, if you have it (→ 09-03) | The house solution if you own stored power |
| 12-volt LED strip wired to a battery | Excellent | Best on paper: no conversion loss | Solar | A later project (→ 09-08) |
| Solar garden or path light | Excellent | Dim, but free | Sun | Bring them in at dusk |
| Chemical light stick | Excellent | Single use | None | Children, marking, one-time use |
| **Oil or kerosene lamp** | **Fire, CO, fumes** | Good run time, warm light | Needs fuel | Backup only (→ 10-02) |
| **Candle** | **Worst: open flame is a leading cause of home fires** | Poor | Can be made (→ 10-04) | Last resort, with rules |
| Propane or white-gas lantern | **Fire and serious CO** | Bright | Needs fuel | **Outdoors only** |
| Fireplace or stove glow | Already burning | Free | Wood | Background light only, not for tasks |

## Your stored power is your lighting grid

If you own power stations or power banks (→ 29-02), they already are the lighting system. Plan it
as an allocation, not a wish:

- **Small loads on small sources.** USB lanterns, headlamp charging and AA charging run off power
  banks and the smallest station first, so the big stations are kept for big jobs.
{{#if has.refrigerated_meds}}- **Never the station that keeps refrigerated medicine cold.** A
  lantern charging there is spending the medicine's watt-hours (→ 09-16).
{{/if}}- **Area lighting is cheap.** An LED string or a couple of plug-in LED lights drawing 5 to
  10 watts in all costs a large station very little per evening hour. Put it on whichever station
  is fullest.
- **A wired 12-volt LED circuit** (→ 09-08) is a reasonable later project. Nothing here waits for
  it.

{{#if has.power_station}}Your stations: {{#each stations as s}}{{s.model}} ({{s.wh}} Wh); {{/each}}total {{ gear.station_wh_total }} Wh. → 10-06 turns that into hours of light.{{/if}}

## The numbers that matter

- **A modern LED headlamp on low (10 to 50 lumens)** draws about 0.1 to 0.5 watts and runs about
  **30 to 150 hours** on one set of three AA or AAA cells. **On high (200 to 300 lumens)** it draws
  2 to 3 watts and lasts only **2 to 5 hours**. Three cells hold only about 3 to 7 watt-hours, so
  both numbers cannot be large. Some dim "moonlight" modes run for weeks. **Low is almost always
  enough**: your eyes adapt in a dark house. High is for going outside. Check your own lights'
  packaging for their ratings.
- **A 20,000 mAh power bank** (about 70 watt-hours) runs a 2-watt lamp for over 30 hours.
- **Lighting is a small load** next to refrigeration (→ 09-10), which is why it is affordable even
  on a small solar setup, and why it should be electric rather than flame.
- **A candle gives a small fraction of the useful light of an LED lantern**, and brings fire risk.

## Choosing light by job, not by device

- **Moving around and tasks:** headlamp on low; red at night to keep your night vision.
- **A room or gathering:** one lantern on a table, bounced off a white ceiling. Spread-out light
  feels far brighter than a point of light and is easier on the eyes over a long evening.
- **Children's rooms:** a dim, **flameless** night light. A small child in a dark house is a
  safety and morale problem (→ 20-02). Battery LED, always. **Never a candle or fuel lamp in a
  room where children sleep** (USFA).{{#if has.young_child}} This household has a child under 6:
  put a night light in every room they sleep in.{{/if}}
- **Outside:** a bright flashlight, used **sparingly** (→ 10-05).
- **Reading and long evenings:** a warm, dim, spread-out lamp. Here light becomes a morale
  question: long nights are hard on people, and good light matters more than you would guess.

## Red light, and why it is worth the habit

After a few minutes in the dark your eyes adapt, and a burst of white light undoes that for many
minutes. Red light does not. Red is also much harder to see from outside (→ 10-05) and disturbs
sleep less for everyone in the room. Buy headlamps with a red mode and make it the default indoors
at night.

## Batteries: the real bottleneck

**The lights are not what runs out; the cells are.**

- **Pick one main cell size**, usually AA, and buy new lights to match. If you already own lights
  that take another size (often AAA), stock that size too and stop there.
- **Rechargeable NiMH cells and a USB charger** let solar or stored power feed every light
  (→ 09-07).
- **Keep a reserve of alkaline cells** as well: they keep for years and need no charging. **Store
  them out of the devices**: alkaline cells leak and ruin the contacts. Check stored lights twice a
  year.
- **Lights with a built-in rechargeable cell** are efficient and handy, but when the cell dies the
  light is finished. **Prefer lights that take cells you can replace**; ideally own some of each.
  Charge lithium devices where you can see them, not on a bed or sofa (NFPA, Lithium-Ion
  Batteries).
- **Cold cuts run time.** In an unheated space expect much less from any battery. Keep spare cells
  warm (→ 09-07).

## Gear

**Have now:**

| Item | Why | Notes |
|---|---|---|
| LED headlamps: one per person ({{ household.size }} people) plus spares | Hands-free is the whole game | **Red mode**; same cells as your other lights |
| LED lanterns, AA or USB-rechargeable, three or four | Room light for long nights | Spread-out, warm, dimmable |
| Rechargeable NiMH cells (plenty) and a USB charger | Makes lighting solar- or station-powered | The core of the plan |
| Alkaline cell reserve | Keeps for years; no charging | Stored **outside** devices |
| Children's flameless night lights | Safety and sleep | Dim, warm, never a flame |
| Clip-on book light | Long-evening morale | Low draw |
| White paper, foil or a white sheet | Spreads light and roughly doubles how bright a room feels | Costs nothing |
| Chemical light sticks (a box) | Children, marking hazards, one-time use | No heat, no flame, no batteries |
| Spare lights and cells in each go-bag | Redundancy | → 22-03 |
| 12-volt LED strip, wire, fuses | Later efficiency project | → 09-08; low priority |

**If you do not have it, scavenge:**
- **Lights** from vehicles (dome, map and work lights), bike lights, emergency exit signs, solar
  path lights, phone flashlights, cordless-tool work lights.
- **Batteries** from remotes, toys, clocks, keyboards, cameras and every drawer in the house. If
  you take them from smoke alarms, **replace them**. **Count your batteries now.**
- **12-volt lighting** from RVs, campers and boats: built for exactly this.
- **Diffusers:** a plastic milk jug over a headlamp makes a lantern; a jar of water in front of a
  light spreads it.
- **Reflectors:** foil, white paint, a mirror, a pale wall. **Bouncing light off a white ceiling is
  the cheapest lighting upgrade there is.**

## When it runs out

- **Count cells, not lights.** Estimate hours per set (usually far more than you think on low) and
  write the total on → 23-02. Most households find they have **weeks to months** of LED light: rare
  good news.
- **Stretch it, in this order:** (1) low or moonlight mode, always; (2) **one light for the
  household, not one each**: gather in the heated room in the evening (→ 08-01), which saves fuel,
  light and morale at once; (3) **shift the day earlier**: get up with the sun, do everything in
  daylight, sleep through the long winter nights; (4) red or dim only; (5) flame as a last resort
  with the rules on → 10-02.
- **Resupply:** solar into rechargeable cells is the renewable loop, which is why one cell size
  matters. Scavenged alkalines stretch it. Beyond that, → 10-04: making candles and lamps from fat
  and wax.
- **Never swap an unattended candle in for a lamp.** That trade has killed more people than the
  dark ever will.
- **The real risk is morale.** Long dark days for months are hard on adults and harder on
  children. Budget light for **evening gathering, reading and children's routines** on purpose
  (→ 20-02, → 21-04).

## Phase notes

- **A (sheltering at home):** LEDs off power banks and the smallest station; area light in the one
  heated room when there is spare power; headlamps everywhere; children's night lights on; the
  bedside care light on charge. A lit house in a dark street is visible a long way (→ 10-05).
- **B (on the move):** headlamps, red mode, spare cells. **Light discipline is a safety rule on the
  move**: one dim red headlamp per adult, children kept close.
- **C (settled somewhere new):** the same LED plan, plus more freedom to use flame lamps in a
  building you control, and a real reason to make candles and lamp oil (→ 10-04). On arrival, walk
  the building and find out what actually lights, and whether any circuits run from a generator,
  before assuming any house lighting exists. **A bin of lanterns, headlamps, chargers and cells**
  travels with you, or is placed at the destination ahead of time.{{#if has.agreed_destination}}
  For your agreed destination, ask the people there about lights and generator circuits now, not
  on arrival.{{/if}}

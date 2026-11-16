---
id: 09-02-solar-basics
section: 09-power-and-energy
title: "Solar power basics and sizing"
version: 2
revised: 2026-11-16
layer: core
danger_level: caution
phase: [A, C]
tags: [power, solar, pv, sizing, charge-controller, inverter, series, parallel, off-grid]
derived_from: [09-02-solar-basics]
sources:
  - us-department-of-energy-solar-energy-technologies-of-2a534a
  - us-department-of-energy-solar-photovoltaic-technolog-ca10f6
  - doe-solar-and-resilience-basics-r14
  - mike-holt-nec-690-table-690-7-r14
  - renogy-rsp200d-g3-datasheet
  - ecoflow-400w-lightweight-panel-user-manual
  - rich-solar-mega-100-product-page
  - victron-wiring-unlimited-r14
  - battle-born-bb10012-data-sheet-r14
  - trojan-battery-maintenance-r14
  - generac-gp3500io-owners-manual
  - noaa-gml-solar-calculator-r14
related:
  - 09-01-power-priorities
  - 09-03-batteries-and-storage
  - 09-05-solar-in-winter
  - 09-08-wiring-and-safety
  - 09-09-small-solar-build
  - 09-10-power-for-medical
  - 09-16-outage-day-one
  - 28-02-solar-panels-and-controllers
  - 28-07-reading-your-own-gear
  - 29-02-ex02-batteries-and-power-stations
cards: []
explainers: [EX-02, EX-14]
promote_when: [has.solar]
photo_slots: []
figures: [fig-series-vs-parallel]
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: { date: "2026-11-16", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "Cold factor tied to maker coefficients and NEC Table 690.7 (1.20 to -13 F, 1.25 at -40 F); grid-tied shutdown to DOE; unsourced conversion-loss, MPPT-gain and surge ranges removed or re-sourced; figure text matches" }
---

# Solar power basics and sizing

**What this page is for.** How a solar setup is put together, how to work out how many panels and
how much battery you need, and the one wiring mistake that destroys equipment on the first cold
morning. Do the load list on → 09-01 first; you cannot size anything without its watt-hour number.
Volts, amps and watts are explained on → 29-02.

> **CAUTION.** A grid-tied rooftop solar array is **designed to switch off when grid power cuts
> out**, for safety. To make power on its own it needs a suitably configured inverter and a battery
> that can run the house "islanded" (US Department of Energy, Solar and Resilience Basics). If your
> house has rooftop solar with no battery and no inverter that can run on its own (often called
> "backup-capable"), **you will have no power in an outage despite the panels on the roof.** Find
> out which kind you have before you need it.
> Also: **a panel in daylight is live.** There is no off switch on a solar panel; you cover it or
> you disconnect it.

## Do this now
- **Finish → 09-01 first.**
- **If the house has rooftop solar, find out whether it is grid-tied, hybrid or off-grid.** Grid-tied
  without a battery is no help in an outage. This is a phone call to the installer today.
- **Size on the December number, not the June number** (→ 09-05). This is where most plans fail.
- **Start small and modular.** A few hundred watts of panels, a lithium iron phosphate battery or a
  power station, and a good charge controller cover Tier 0 and much of Tier 1. Buy parts you can
  add to, not a sealed box you cannot expand.
- **Read the label on every panel and station you own** and write the numbers in the tables on
  → 09-03 (how to read them: → 28-07).

## Why it works this way

**Four parts, four jobs.** Every solar setup, from a folding kit to a whole-house array, is the
same four blocks (US Department of Energy, Solar Photovoltaic System Design Basics):

| Part | Job | If it fails |
|---|---|---|
| **Panels** (PV modules) | Turn light into DC electricity | No generation. Very reliable; decades of life |
| **Charge controller** | Regulates panel output into the battery safely | Overcharges and destroys the battery, or will not charge |
| **Battery** | Stores energy for night and cloud | Power only while the sun shines |
| **Inverter** | Turns battery DC into 120 V AC for household plugs | Only DC devices work |

A **power station** is all of these except the panels, in one box (→ 09-03).

**Skip the inverter where you can.** Running 12 V DC loads directly (USB charging, LED lights, a
12 V compressor cooler) avoids the energy lost in each conversion (an inverter's efficiency is on
its label) and the inverter's own idle draw. Direct DC is the easiest
efficiency gain there is. Run the medicine cooler and the lights on DC; keep the inverter for the
few things that truly need AC.

**"Sun hours" is the sizing unit.** A panel rated 100 W makes 100 W only in full, square-on,
clear-sky noon sun at a mild temperature: a laboratory condition. A "peak sun hour" is one hour of
that full-strength sun; a December day gives far fewer of them than it has hours of daylight (your
home's figures are below). Real daily output is roughly:

**Daily Wh ≈ panel watts × peak sun hours × 0.75**

The 0.75 is this binder's planning allowance for wiring and controller losses, dust, heat and
imperfect aim (the same factor the app uses for your estimates). Be pessimistic.

**Your home's sun hours** (from the region data for {{ region.home.county }} County,
{{ region.home.state_name }}): June **{{ region.home.sun_hours_jun }}**, December
**{{ region.home.sun_hours_dec }}**. Use December for sizing. Overcast and snow cut December far
below even that (→ 09-05).

**Size the system with this arithmetic:**
1. **Daily need** (Wh per day) from → 09-01, including the 1.3 loss factor.
2. **Panel watts needed ≈ daily need ÷ (December sun hours × 0.75).**
   Example: 600 Wh per day ÷ (2.5 × 0.75) ≈ **320 W of panel** to break even on a clear December
   day. Yours: ________ Wh ÷ ({{ region.home.sun_hours_dec }} × 0.75) = ________ W.
3. **Battery ≈ daily need × days of autonomy** (days you can run with no sun at all). Two to three
   days is the practical minimum where overcast or snow can last several days. Then divide by the
   usable depth of discharge (→ 09-07): lithium iron phosphate up to 100% by its maker's rating
   (plan on about 90%); lead-acid 50% or less (Trojan), so a lead-acid bank must be about
   **twice** the size.
   Example: 600 Wh × 3 days = 1,800 Wh usable → about 2,000 Wh of lithium iron phosphate, or about
   4,000 Wh of lead-acid.
4. **Inverter size ≈ the largest set of AC loads that run at the same time**, plus headroom for
   motor start (allow about 3 times a motor's running watts for starting; Generac, GP3500iO
   Owner's Manual).
5. **Charge controller** must handle the panels' voltage and current with margin: the array's
   open-circuit voltage must not exceed the controller's rating (Victron Energy, Wiring
   Unlimited). **Buy MPPT.** (MPPT and PWM are the two kinds of controller; MPPT converts surplus
   panel voltage into extra charging current, PWM throws it away, which matters most with
   higher-voltage panels and in cold weather.)

### Series and parallel: the wiring choice that matters most

{{figure fig-series-vs-parallel}}

When you connect two or more panels you choose:
- **Series** (plus of one panel to minus of the next, in a chain): the **voltages add**; the
  current stays at the level of the weakest panel. Three panels of about 20 V each make a string of
  about 60 V.
- **Parallel** (all pluses together, all minuses together, usually with a Y-branch connector): the
  **currents add**; the voltage stays near the lower panel's voltage.

**The failure modes are not the same.** **Too much voltage kills a charge controller instantly
and permanently.** Too much current, at most station and controller inputs, is simply clipped:
the input takes what it can use and ignores the rest. (Check your manual: if it lists a maximum
short-circuit current, stay under that too.) So when in doubt, **choose the configuration with the
lower voltage.**

**Cold raises panel voltage.** A panel is rated at 77 °F (25 °C). For every degree colder, its
open-circuit voltage (Voc, the voltage with nothing connected, printed on the label) rises a
little: panel makers print this as the "temperature coefficient of Voc", for example −0.28% per °C
(Renogy, RSP200D datasheet) or −0.25% per °C (EcoFlow, 400W panel manual). A string that is safely under a controller's limit on a mild
afternoon can be over it at sunrise on a clear, frozen morning. Cold never raises current, so
**series is the configuration winter can push over the edge, and parallel is the one it cannot.**

**The cold-voltage check, every time you plan a series string:**
1. Add up the label **Voc** of every panel in the string (warm Voc).
2. **Multiply by 1.20.** With a coefficient of 0.3% per °C or less, as the panels above print,
   1.20 covers panel temperatures down to about −40 °F. If you do not know your panel's
   coefficient, the National Electrical Code's table uses 1.20 down to −13 °F (−25 °C) and rises to
   1.25 at −40 °F (NEC Table 690.7, as printed by Mike Holt Enterprises). Your home's record low is
   **{{ region.home.record_low_f }} °F**: if it is below −13 °F and you do not know the
   coefficient, use 1.25. With the coefficient, work it out: factor = 1 + (coefficient as a
   decimal, without its minus sign) × (25 − lowest temperature in °C). Example: 0.003 ×
   (25 − (−40)) = 0.195, so a factor of about 1.20.
3. **The result must be below the station's or controller's maximum PV input voltage**, with a
   margin. A few volts of margin is no margin.
4. Never drop the factor because "it is only 20 degrees this morning". Every winter morning is far
   below the 77 °F rating.

The worked tables for your own panels and stations, and which configuration goes into which
station, are on → 09-03. The short version that prevents almost every disaster: **a station with
a high input-voltage ceiling and a low current limit takes series strings that pass the cold check; a station with a low
voltage ceiling and a high current limit takes parallel pairs or single panels, never a series
string: its ceiling cannot hold one cold, and the over-voltage kills the input for good.**

### Mounting decisions that matter
- **Face true south** (US Department of Energy, Solar Photovoltaic System Design Basics). A compass
  points to magnetic north, which can be well off true north in much of the country. Set panels by
  the shadow at solar noon (when shadows are shortest, they point true north).
- **Tilt steep in winter.** DOE's year-round angle is your latitude. At noon on the shortest day the
  sun is 23.5° lower than at the equinox, so a panel tilted at your latitude plus 23.5° faces it
  square-on (NOAA Solar Calculator gives the sun's height for your place); roughly latitude plus
  15° is a common winter compromise that also catches morning and afternoon sun and sheds snow
  (→ 09-05). Adjustable tilt is worth the trouble twice a year.
- **Shade is disproportionately bad.** Shading part of one panel can cut the output of the whole
  series string, not just that panel. Trees, chimneys, a neighbour's roof and the low winter sun
  angle all matter.
- **Ground-mount or portable is better than roof for an emergency setup.** You can sweep snow off
  it, re-aim it, move it, and bring it inside at night. A roof array in a blizzard is
  unreachable, and a lit house in a dark neighbourhood is a signal (→ 14-03).
{{#if has.solar}}
**Our panels:**

| Panel | Watts each | How many | Voc (label) | Isc (label) |
|---|---|---|---|---|
{{#each panels as p}}| {{p.model}} | {{p.watts}} | {{p.count}} | ______ V | ______ A |
{{/each}}

Total: **{{ gear.solar_w_total }} W**. Model-by-model figures for common panels and controllers:
→ 28-02.
{{/if}}

## Gear and items

**Have it now (buy toward this):**

| Item | Why | Notes |
|---|---|---|
| Rigid panels, 100 to 200 W each, several | Modular, cheap per watt, decades of life | More smaller panels give more redundancy than one big one |
| One folding or portable 100 to 200 W panel | Phase B, and aiming at the low winter sun | The panel that leaves with you |
| **MPPT** charge controller with voltage headroom | More harvest than PWM; survives the cold-voltage rise | Check its maximum PV input voltage against the cold check above |
| Lithium iron phosphate battery, 100 Ah (about 1.28 kWh) or more, or a power station | Deep cycles, long life | Note the **cold-charging limit** (→ 09-07) |
| Pure sine inverter, 300 to 1,500 W | Medical gear and electronics want pure sine | Modified sine can damage or buzz some devices |
| 12 V DC distribution: sockets, USB, fuse block | Skips inverter losses | The efficient path for Tier 0 |
| Fuses, breakers, correctly sized wire | Not optional (→ 09-08) | Fire risk otherwise |
| Adjustable tilt mounts or a simple A-frame | Winter angle and snow shedding | Buildable from 2×4s |
| Soft broom or snow rake with a non-abrasive head | A snowed-over panel makes nothing | Never a metal scraper |
| Multimeter | Checks Voc and polarity before every first connection | → 09-12 |

**Scavenge or substitute:**
- **Panels** from RVs, campers, boats, construction signs, solar yard lights and derelict arrays.
  **Large grid-tie panels are higher-voltage** than the "12 V" panels (whose Voc is about 22 to
  23 V: Rich Solar MEGA 100, Renogy RSP200D); read the Voc on the label. They need an MPPT
  controller that accepts that input; they are not a direct 12 V battery charger.
- **Controllers and inverters** from RVs, boats and campers; car inverters for small AC loads.
- **Batteries** from vehicles, boats, RVs, UPS units, floor scrubbers, mobility scooters and golf
  carts (→ 09-13, → 09-14).
- **Mounts:** 2×4 A-frames, pallets, fence posts, a ladder, a leaned sheet of plywood: anything
  that holds a panel steep and facing south.
- **Wire:** automotive and battery cable, welding cable. **Do not undersize it** (→ 09-08).

## When it runs out
- **Panels are the durable part.** DOE describes a PV array's lifetime as 25 years (and expects
  the inverter to be replaced at least once in that time); panel makers give 25-year output
  warranties (for example Rich Solar). Hail is the real risk: store a spare panel flat and
  indoors.
- **The controller and inverter are the fragile electronics.** They fail from heat, water, surges
  and reversed polarity. **Buy a spare charge controller now**; without it the panels cannot
  safely charge anything. It is the highest-value spare in this section.
- **The battery is the true consumable** (→ 09-03, → 09-07).
- **When generation drops below Tier 0** (a snowed-in December week), fall back in order: stored
  battery, then a short generator run to bulk-charge the bank (→ 09-04), then vehicle and
  hand-crank charging (→ 09-11), then shedding to Tier 0 alone (→ 09-01).

## Phase notes
- **A (at home):** ground-mounted or yard-deployed panels you can sweep and re-aim, batteries
  **indoors** where they stay warm (→ 09-07).
- **B (moving):** one folding panel, one battery or station, power banks. Solar on foot or in a
  vehicle is a **trickle**: it keeps a phone and a small medical device alive, not a household.
- **C (settled somewhere new):** the permanent build. More panel than you think you need, real
  ground-mount racking, a battery room that stays above freezing. **Over-panel deliberately**:
  extra panels are cheap and they are what carry you through December.

## Cross-references
→ 09-01 load triage, do this first · → 09-03 batteries, stations and your wiring tables ·
→ 09-05 solar in winter, read before finalising any size · → 09-07 battery chemistry ·
→ 09-08 wiring and fusing · → 09-09 step-by-step build · → 28-02 panels and controllers ·
→ 29-02 batteries and power stations explained

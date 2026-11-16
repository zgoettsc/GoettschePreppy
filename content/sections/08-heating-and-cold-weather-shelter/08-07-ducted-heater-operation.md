---
id: 08-07-ducted-heater-operation
section: 08-heating-and-cold-weather-shelter
title: "Ducted diesel and kerosene heaters: install and operation"
version: 1
revised: 2026-11-16
layer: gear
danger_level: critical
phase: [A, C]
tags: [diesel heater, kerosene, parking heater, forced air, sealed combustion, exhaust, carbon monoxide, power draw, altitude]
derived_from: [08-07-ducted-heater-operation]
sources:
  - hcalory-manufacturer-hcalory-tb-max-diesel-air-parki-b67d4a
  - cdc-carbon-monoxide-poisoning-basics-772153
  - cpsc-carbon-monoxide-fact-sheet-e97206
  - eia-diesel-fuel-explained
  - eia-heating-oil-explained
related:
  - 08-01-heating-one-room
  - 08-02-carbon-monoxide-safety
  - 08-04-emergency-heat-options
  - 08-06-improvised-shelter-warmth
  - 08-08-wood-heat-operation
  - 06-05-alternative-fuels
  - 06-06-fuel-storage-safety
  - 09-03-batteries-and-storage
  - 22-05-kit-vehicle
  - 23-02-master-consumables-table
  - 28-04-portable-heaters
  - 29-01-ex01-fuels
  - 29-02-ex02-batteries-and-power-stations
  - 29-03-ex03-carbon-monoxide
  - 30-01-the-floors
  - 30-06-dc05-fuel-in-attached-garage
  - 30-18-dc17-old-fuel
cards: [DC-05, DC-17]
explainers: [EX-01, EX-02, EX-03]
promote_when: [has.diesel_heater]
photo_slots:
  - { id: ducted-window-board, caption: "Our window board: intake and exhaust pass-throughs, sealed, labelled" }
  - { id: ducted-exhaust-outside, caption: "The exhaust outlet outside: clear of windows, doors and snow" }
figures: [fig-ducted-heater-window-board]
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: null
---

# Ducted diesel and kerosene heaters: install and operation

**What this page is for.** How the class of small forced-air heaters often called "diesel heaters"
or "parking heaters" works, how to install one through a window so its fumes stay outside, how to
power and fuel it, and how it fails. These heaters were made for trucks and boats and are widely
sold for home and cabin use. Figures here come from one maker's manual for an all-in-one unit of
this class; **your own unit's manual governs.** Spec tables for common models are on → 28-04.
Diesel and kerosene are explained on → 29-01.

> **SAFETY.** This class is the safest serious fuel heat in this section **only if it is installed
> right:** combustion air comes from **outside**, exhaust goes **outside**, and only clean heated
> air enters the room. Installed wrong (exhaust inside, intake inside, a leaking joint) it is just
> another carbon monoxide (CO) source. **Sealed combustion is a design goal, not a guarantee: a
> battery CO alarm runs in the heated room every time** (CDC; → 08-02). **Fuel is never stored or
> transferred near an open flame or a running appliance** (→ 30-01): fill it with the heater off
> and cool, outdoors.

{{#if has.diesel_heater}}**Your household listed a ducted heater:** {{#each heaters as h}}{{h.kind_text}} {{h.model}}; {{/each}}{{/if}}

## Do this now (the week you get one)

1. **Do the window-board install as a dry run** in daylight and above freezing, not for the first
   time in an outage by headlamp.
2. **Make the window board:** plywood or rigid foam cut to one warm-room window opening, with two
   sealed pass-throughs for the **combustion intake** and the **exhaust**, both ending outdoors.
   Label it and store it with the heater.
3. **Stage the fuel** your manual names (diesel or kerosene), in approved, labelled cans
   (→ 06-06). **Winter diesel gels**: use winter-blend fuel or an anti-gel additive.
4. **Battery CO alarm in the room it heats,** every run (→ 08-02).
5. **Test-run it monthly in season** through the window board, so the pump, glow plug and
   controller are known to work before you need them.

## How this class works

Portable propane and kerosene heaters burn the room's air and leave their exhaust in the room
(→ 08-09, → 08-10). A ducted heater is different in kind. Its burner is a **sealed loop**: outside
air in, burn, exhaust out. A separate fan blows room air across a hot metal box (the heat
exchanger) and back out of a duct as clean hot air. Nothing the flame touches should mix with the
air you breathe. That is why the makers allow it to run for hours, **provided the install is tight
and the alarm is watching for the day it is not.**

It needs electricity: a **glow plug** (a small electric heater element) lights the fuel, then a fan
and a small dosing pump run all the time. Some units carry their fuel tank inside the unit itself,
which puts fuel inside the warm room; fill such a tank outdoors with the heater cold, and keep all
other fuel out of the living space (→ 06-06). Where fuel is stored is a decision card if the place
is an attached garage: {{choice DC-05}} (→ 30-06).

## The window-board install

{{figure fig-ducted-heater-window-board}}

1. Cut plywood or rigid foam to fill the chosen window opening snugly; foam-tape or weatherstrip
   the edges.
2. Make two holes through the board: **combustion intake** and **exhaust**, spaced apart as the
   manual says, both opening outdoors. The warm-air duct stays entirely indoors.
3. **Seal every joint on the exhaust run** with the supplied clamps and exhaust sealant. A leaking
   exhaust joint indoors defeats the whole design.
4. Close the window down onto the board and stuff and tape the gaps. **Know which sealing is
   which:** the board's edges are for comfort; the exhaust joints are for life.

{{photo ducted-window-board}}

### Exhaust rules

- **Slope the exhaust slightly down and away** so condensation drains out, not back into the
  burner.
- **End it away from any window, door or vent,** and clear snow from around it after every storm
  (→ 08-02).
- **It gets very hot.** The manual cited here gives exhaust temperatures up to about **400 °C
  (about 750 °F)** (HCALORY, heater user manual). Keep the pipe off siding, buried combustibles and
  cord, use the supplied heat wrap and standoffs, and keep it where a child cannot touch it.
- **Never shorten the exhaust or run it indoors "temporarily".** There is no temporary CO.

{{photo ducted-exhaust-outside}}

## Fuel

- **Diesel or kerosene,** as your manual allows. Both are distillate fuels, close relatives of
  heating oil (EIA, Diesel Fuel Explained; EIA, Heating Oil Explained; → 29-01). Never gasoline.
- **Winter diesel gels** in cold weather, and the heater's thin fuel line clogs first. Use winter
  blend or anti-gel (→ 06-06).
- **Refuel outdoors, with the heater off and cool.**
- **Old or water-contaminated fuel** clogs the pump and fouls the burner. Whether old fuel is used
  after a test is a decision card: {{choice DC-17}} (→ 30-18).

## Power

- **At start:** the glow-plug cycle draws heavily for a couple of minutes; the manual cited here
  asks for a 12 V supply good for **12 A or more** (HCALORY, heater user manual).
- **Running:** about **1 to 4 A at 12 V** depending on the power level (same manual).
{{#if has.power_station}}- Your power stations ({{ gear.station_wh_total }} Wh in total) can run one
  from a 12 V outlet or through the unit's AC adapter; divide watt-hours by the running watts for a
  rough runtime (→ 29-02).
{{/if}}- **Let it finish its shut-down cycle.** The unit runs its fan after the flame is out to cool the
  burner. Cutting power to a hot heater damages the burner.

## CO plan anyway

Sealed combustion fails in dull ways: a cracked exhaust joint, a worn burner gasket, a kinked
intake that pulls room air, snow over the exhaust. **The CO alarm in the heated room is the
backstop for all of them.** Some units have a built-in CO sensor; treat it as a bonus, not a
replacement for the room alarm you test monthly. If the alarm sounds: everyone out, heater off,
→ 08-02.

## Altitude and won't-start

- **Altitude:** thin air makes the mixture too rich, which smokes and soots. Many controllers have
  an altitude ("plateau") mode that cuts the fuel rate; the manual cited here recommends it above
  roughly **2,000 m (about 6,600 ft)** (HCALORY, heater user manual).
  {{#if is.high_altitude}}Your home is above 5,000 ft: check your controller's setting.{{/if}}
- **Won't start in the cold:** usually fuel (gelled diesel, or air in the line after refuelling:
  repeat the priming cycle) or a weak power supply that sags under the glow-plug load. Check the
  voltage under load before blaming the unit.
- **Smoke at start:** a little white smoke from a cold start is normal. **Continuous black smoke means
  too much fuel**: wrong altitude setting or a fouled burner. Glow plugs and burners can be cleaned
  by the manual's maintenance section.

## Gear

| Item | Why | Notes |
|---|---|---|
| The heater and its manual | Your unit's numbers | Keep the manual with it |
| Pre-cut window board with sealed pass-throughs | The install is the safety | Made in advance, labelled |
| Exhaust extension, clamps, high-temperature sealant | Reach outdoors, sealed | Every joint clamped |
| Diesel or kerosene, anti-gel for diesel | Fuel that flows in the cold | → 06-06 |
| 12 V cable or AC adapter | Its power | Supply good for the start current |
| **Battery CO alarm for the heated room** | The backstop | Test before each season |
| Spare glow plug and burner gasket | The parts that fail | Cheap now, unobtainable later |

**No heater?** Any rigid sheet (plywood, foam board, doubled cardboard faced with foil tape) can
become a window board, but the exhaust sealing cannot be improvised loosely. Without the heater,
fall back on → 08-04 and → 08-06.

## When it runs out

- **Fuel is countable:** your manual lists fuel use per hour at each power level. Write it here:
  ______ per hour at low, ______ at high. Log cans on → 23-02.
- **Ration:** run it in bursts to warm the room, then coast under insulation (→ 08-01). Overnight,
  bedding and shared warmth save fuel.
- **Resupply:** diesel is often the most findable liquid fuel in rural areas; kerosene usually is
  not (→ 06-05). The glow plug and gaskets are the non-fuel clock: keep spares.

## Phase notes

- **A (at home):** a strong warm-room heater for a long winter outage: window-board install,
  battery power, CO alarm.
- **B (moving):** these began as vehicle heaters. A vehicle install is an option **only** with the
  same rules: exhaust fully outside and sealed, CO alarm in the cabin, never improvised at a rest
  stop (→ 22-05).
- **C (established somewhere else):** a good backup to wood heat (→ 08-08): it heats a room without
  tending a fire.

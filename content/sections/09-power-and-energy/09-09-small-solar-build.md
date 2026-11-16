---
id: 09-09-small-solar-build
section: 09-power-and-energy
title: "Building a small solar system step by step"
version: 1
revised: 2026-11-16
layer: core
danger_level: caution
phase: [A, C]
tags: [power, solar, build, diy, 12v, checklist, project]
derived_from: [09-09-small-solar-build]
sources:
  - us-department-of-energy-solar-energy-technologies-of-2a534a
  - us-department-of-energy-solar-energy-technologies-of-7bba95
  - us-department-of-energy-consumer-guide-to-residentia-1d87da
  - nfpa-national-fire-protection-association-lithium-io-0c7d64
related:
  - 09-01-power-priorities
  - 09-02-solar-basics
  - 09-03-batteries-and-storage
  - 09-05-solar-in-winter
  - 09-07-battery-chemistry
  - 09-08-wiring-and-safety
  - 09-10-power-for-medical
  - 09-12-ac-dc-cables-and-connectors
  - 24-04-blackout-weekend
  - 28-02-solar-panels-and-controllers
cards: []
explainers: [EX-02]
promote_when: []
photo_slots:
  - { id: power-box, caption: "Our power box: controller, fuses, monitor and battery, with the fuse ratings visible" }
figures: [fig-small-solar-system-layout, fig-series-vs-parallel]
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: null
---

# Building a small solar system step by step

**What this page is for.** A step-by-step build of a **portable, self-contained 12 V DC system**:
panels, a charge controller, a battery, fuses and a small inverter in one box. It plugs into nothing
and touches no house wiring. It is the repairable, expandable alternative (or companion) to a power
station (→ 09-03). Read → 09-08 before you cut a wire.

> **CAUTION.** This build is safe only if it is fused and wired correctly (→ 09-08). The moment you
> want it to power house circuits, it is a different project and it belongs to a licensed
> electrician.
>
> **Before the collapse:** a portable system that plugs into nothing usually needs no permit; anything
> wired to a building, or on a roof, generally does.

## Do this now
- **Build it now, while there is no pressure.** A system assembled on a calm weekend and actually
  used is worth ten still in boxes.
- **Then use it every month.** Run the lights from it for an evening; charge the phones from it.
  **Find the failures now**, when the fix is a trip to the store.
- **Draw the wiring diagram on paper, with fuse ratings, and keep it in this binder.** You will not
  remember it in a year, and a stranger may need to work on it.

## Why it works this way

### The design
Roughly **400 to 800 W of panels, 1.2 to 2.5 kWh of lithium iron phosphate, an MPPT controller and a
small pure sine inverter**, built as separate parts in a portable box, sized from your → 09-01 load
numbers and your **December** sun hours ({{ region.home.sun_hours_dec }} at home, → 09-05). It covers
Tier 0 and much of Tier 1 and grows by adding panels or a second battery.

{{figure fig-small-solar-system-layout}}

**Worked example: do this arithmetic with your own numbers.**
```
Tier 0 + Tier 1 daily need (from 09-01) ......   550 Wh/day
x 1.3 for inverter/charge losses ............   715 Wh/day  <- design target
December sun hours (09-05) ..................   2.5
Panel watts = 715 / (2.5 x 0.75) ............   ~380 W  -> buy 400-600 W (over-panel)
Battery for 3 days' autonomy = 715 x 3 ......   ~2,150 Wh usable
   LiFePO4 (use ~90%) .......................   ~2,400 Wh  -> 2 x 100 Ah 12 V
   Lead-acid (use ~50%) .....................   ~4,300 Wh  -> 4 x 100 Ah 12 V, and heavy
Inverter = largest set of AC loads at once ..   ~600 W running -> 1,000 W pure sine
```
Yours:
```
Daily need ________ Wh  x 1.3 = ________ Wh   December sun hours ________
Panel watts = ________ / (____ x 0.75) = ________ W
Battery = ________ x ____ days = ________ Wh usable
Inverter = ________ W
```

### The parts, in the order you will wire them
1. **Panels:** two to four rigid 100 to 200 W panels, plus one folding portable panel.
2. **Panel wiring:** MC4 connectors and extension cable; a **PV disconnect or breaker**.
3. **MPPT charge controller:** sized for the panels' current, with a **maximum PV input voltage
   that survives the coldest morning** (→ 09-02).
4. **Main battery fuse:** on the battery positive terminal, within inches.
5. **Battery:** lithium iron phosphate with a battery management system that blocks cold charging
   (→ 09-07).
6. **Shunt battery monitor:** between the battery negative and everything else.
7. **DC fuse block:** feeds the 12 V loads (USB, lights, cooler).
8. **Inverter:** on its own short, heavy, fused cables straight to the battery.

### Build it: the sequence
**Step 0: lay it out dry, on the floor, unconnected.** Check every cable reaches, every fuse rating
matches its wire, and you know what each wire does. Label both ends of everything now.

**Step 1: mount the electronics on a board.** Charge controller, fuse block, monitor display and
switches on a piece of plywood; battery below or beside it in its box. A **power box** on a hand
truck or in a crate is portable, protects the parts and keeps small children out. Leave ventilation
for the inverter and controller: they make heat.

**Step 2: battery negative to the shunt, shunt to the negative bus.** All negatives return through
the shunt, or the monitor reads nothing.

**Step 3: main fuse on the battery positive**, then to the positive bus. **This fuse goes in last,
after everything else is wired:** it is your master disconnect during the build.

**Step 4: charge controller to the battery**, fused as its manual says, **correct polarity**. Most
MPPT controllers must see the **battery first, panels second**; read the manual, because the wrong
order damages some controllers.

**Step 5: loads.** Fuse block off the positive bus; each branch (USB outlets, 12 V socket, LED
lights, the cooler) fused for its own wire size (→ 09-08).

**Step 6: inverter** on its own short heavy fused cables straight to the battery, not through the
fuse block.

**Step 7: panels last.** Wire the panels with the **PV breaker off** or the panels covered.
Series raises voltage (good for long runs and MPPT, but run the cold-voltage check on → 09-02);
parallel raises current (more tolerant of shade). {{figure fig-series-vs-parallel}} Then connect the
panels to the controller and switch on.

**Step 8: commission it.** Measure everything: battery voltage, panel open-circuit voltage, charging
current, load current. Confirm the controller shows charging. **Then run a real load and watch what
happens.**

**Step 9: test the failure modes on purpose.**
- Cover the panels: does it run cleanly on battery?
- Pull a fuse: does only that branch die?
- Run the bank down to 50%: how long did it take? **Write the number down.**
- Charge from low on a cloudy day: how much did you really get?
- {{#if is.cold_winters}}Leave the panels out on a January day: what does the cold do to the
  harvest and the voltage?{{else}}Run it through the hottest week: what does heat do to the
  controller and the battery?{{/if}}

**Step 10: document it.** Wiring diagram, fuse ratings, charging voltages and measured runtimes, on
paper, in this binder. {{photo power-box}}

### Common mistakes, all avoidable
- **Undersized wire between battery and inverter.** The classic fire.
- **No main battery fuse.** The classic catastrophic fire.
- **Controller maximum PV voltage too low for a cold clear morning.** A dead controller.
- **Lead-acid discharged below 50% again and again.** A dead bank in one season.
- **Lithium iron phosphate charged below freezing.** A permanently damaged battery.
- **Sizing on yearly-average sun hours.** Works in July, fails in January.
- **An inverter far larger than needed.** Big inverters have real idle draw that quietly eats the
  bank. Size it to the load and **switch it off when unused.**
- **Building it and never using it.** The most common failure of all.

## Gear and items

**Have it now (buy toward this):**

| Item | Why | Notes |
|---|---|---|
| 400 to 600 W of panels and one folding portable | Generation, plus the panel that travels | Over-panel for December |
| MPPT controller with generous voltage headroom | Efficiency and cold-weather survival | **Buy a spare**: the highest-value spare in this section |
| One or two 100 Ah lithium iron phosphate, low-temperature protection | Two to three days' autonomy | → 09-07 |
| 1,000 W pure sine inverter | AC when you need it, off when you do not | Watch the idle draw |
| Main fuse, fuse block, assorted fuses | Not negotiable | → 09-08 |
| Shunt battery monitor | The only honest fuel gauge on lithium | |
| Cable in several gauges, lugs, crimper, heat-shrink | Build and repair | Buy extra |
| MC4 connectors, PV extension cable, PV breaker | Panel side | → 09-12 |
| Plywood board, crate or toolbox, hand truck | Portable, child-safe | |
| Multimeter and DC clamp meter | Commissioning and diagnosis | |
| Adjustable A-frame mount (2×4s) and a snow broom | Steep winter tilt, sweepable | → 09-05 |

Panels and controllers by class: → 28-02.

**Scavenge or substitute:**
- **Panels** from RVs, campers, boats, signs and solar yard lights; **grid-tie panels are
  high-voltage: MPPT only** (→ 09-02).
- **Controllers, inverters, fuse blocks and DC sockets** from RVs, boats and campers: these are
  complete 12 V systems on wheels.
- **Batteries** from vehicles, UPS units, scooters, golf carts (→ 09-13, → 09-14).
- **Cable** from jumper cables, welding leads and vehicle harnesses; **fuses from any vehicle's fuse
  box**.
- **Mounting** from 2×4s, pallets, fence posts, angle iron.
- **Enclosure:** a plastic tote, an ammunition can, a toolbox, a crate.

## When it runs out
- **Keep a spare charge controller.** It is the small, cheap, fragile part whose failure stops the
  whole system. Panels and wire rarely fail; controllers and inverters do.
- **The batteries' life is the system's life** (→ 09-07). Log capacity over time.
- **Repairability is the design goal.** This is why a component build beats a sealed power station
  over the long term: **every part can be replaced with something salvaged.** Keep the diagram,
  spare parts and tools.
- **Shed by tier** as capacity fades (→ 09-01), and move loads to midday.
- **Practise the drill:** once a year, run the household from this system for a full weekend, in
  **winter** (→ 24-04). It is the only honest test.

## Phase notes
- **A (at home):** the power box lives indoors (warm battery); panels deploy in the yard on an
  adjustable frame you can sweep. Keep it on a cart so it can move fast.
- **B (moving):** the folding panel, one battery and the power banks go. **Design the box so the
  battery and controller come out in five minutes without tools**: decide that when you build it.
- **C (settled somewhere new):** rebuild larger and permanent. Longer runs make **24 V or 48 V** worth
  it (→ 09-08). Bring the small system: it becomes the backup and the portable unit.

## Cross-references
→ 09-01 load triage · → 09-02 sizing and the cold-voltage check · → 09-05 winter numbers · → 09-07
chemistry · → 09-08 wiring and fusing, read first · → 09-10 sizing for medicine cooling · → 24-04
blackout weekend

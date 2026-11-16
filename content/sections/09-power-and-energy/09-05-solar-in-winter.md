---
id: 09-05-solar-in-winter
section: 09-power-and-energy
title: "Solar in winter: short days, snow and cold"
version: 1
revised: 2026-11-16
layer: region
danger_level: caution
phase: [A, C]
tags: [power, solar, winter, snow, cold, sizing, sun hours, tilt]
derived_from: [09-05-winter-solar-reality]
sources:
  - us-department-of-energy-solar-energy-technologies-of-2a534a
  - us-department-of-energy-solar-photovoltaic-technolog-ca10f6
  - noaa-national-weather-service-during-extremely-cold-9c1973
  - american-red-cross-winter-storm-preparedness-and-bli-4bb6c0
related:
  - 09-01-power-priorities
  - 09-02-solar-basics
  - 09-03-batteries-and-storage
  - 09-04-generators
  - 09-07-battery-chemistry
  - 09-10-power-for-medical
  - 09-11-hand-and-alt-generation
  - 09-16-outage-day-one
  - 04-09-winter-cold-storage
  - 08-01-heating-one-room
  - 08-04-emergency-heat-options
  - 08-05-hypothermia-frostbite
  - 17-01-blizzards-and-ice
cards: []
explainers: [EX-02]
promote_when: [is.cold_winters, is.snow_region]
photo_slots:
  - { id: winter-panel-spot, caption: "Where our panels go in winter: facing true south, steep tilt, weighted, the cable's route indoors" }
figures: [fig-winter-panel-tilt]
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: null
---

# Solar in winter: short days, snow and cold

**What this page is for.** Almost every off-grid plan is sized in July and fails in January. Winter
stacks four penalties at once: fewer daylight hours, a low sun, snow on the panels, and batteries
that are damaged by charging in the cold. They arrive in the months when lighting, heating-related
and medical loads are highest. This page shows what your panels can really make in December at
home, and how to get through a dark week. The sizing method itself is on → 09-02.

## Do this now
- **Re-run your sizing from → 09-02 with the December sun-hour number, not the yearly average.**
  At home that is **{{ region.home.sun_hours_dec }}** peak sun hours in December against
  **{{ region.home.sun_hours_jun }}** in June. If your panels only break even in June, they are a
  summer convenience.
- **Buy a soft-headed snow rake or long-handled broom** and keep it with the panels. A snowed-over
  panel makes **nothing**, and that can last for days.
- **Keep every battery and power station indoors, in the heated room** (→ 08-01). Charging lithium
  iron phosphate below freezing causes permanent damage (→ 09-03, → 09-07).
- **Set the panel tilt steep in winter:** roughly your latitude plus 15°. It catches the low sun and
  sheds snow. {{figure fig-winter-panel-tilt}}
- **Over-panel deliberately.** Panels are the cheapest part. Extra panel watts turn a bad December
  week into a survivable one.
- **Choose the winter panel spot and the cable's route indoors now**, and photograph it.
  {{photo winter-panel-spot}}

## Why it works this way

### The four winter penalties, stacked

**1. Short days.** The further north you are, the shorter a December day: in the northern states
a midwinter day has only about 9 hours between sunrise and sunset, against more than 15 in June, and
only the middle part of that is useful generation.

**2. Low sun.** In December the sun stays low in the southern sky all day. A panel lying flat, or
tilted for summer, presents a poor face to it. Low sunlight also passes through more atmosphere,
which cuts its strength. **In December, tilt is most of the answer, not a refinement.**

**3. Snow and ice.** **Snow takes a panel to zero, not to "reduced".** A steep tilt helps snow
slide; smooth-framed panels shed better; a dark panel that gets any sun often clears itself as it
warms. But after wet snow or a freezing-rain glaze you clear it by hand or you make nothing. **This
is why ground-mounted or portable panels beat roof mounting for an emergency setup**: you cannot
safely sweep a snowy roof in deep cold, and that is when you will need to.
{{#if is.snow_region}}Home averages about **{{ region.home.snow_in }} inches** of snow a year:
plan for clearing as a routine, like shovelling the walk.{{/if}}

**4. Cold: one benefit, two hazards.**
- *Benefit:* **cold panels are more efficient.** On a clear, cold day with snow on the ground
  reflecting light, a well-aimed panel can briefly beat its summer output.
- *Hazard A:* **panel voltage rises as temperature falls.** A station or controller can be
  **over-volted and destroyed** on a clear frozen morning. Use the cold-voltage check on → 09-02
  (string Voc × 1.20, more for very cold places). Home's record low is
  **{{ region.home.record_low_f }} °F**; January's average low is **{{ region.home.jan_low_f }} °F**.
  Panels are rated at 77 °F, so every winter morning is far below the rating; never drop the factor
  on a "mild" morning.
- *Hazard B:* **charging most lithium batteries below freezing permanently damages them**
  (→ 09-07). Lead-acid charges poorly when cold, and a discharged lead-acid battery can **freeze and
  split.** Batteries live inside.

### The number that should worry you

**Worked example** (a northern location with about 6 peak sun hours in June and 2.5 in December), a
400 W set of panels:

| | Peak sun hours | Realistic daily yield |
|---|---|---|
| June | about 6 | about 1,800 Wh |
| December, clear, clean panels | about 2.5 | **about 750 Wh** |
| December, overcast | often 0.5 to 1 | **about 150 to 300 Wh** |
| December, snow-covered | | **0** |

**Yours** (daily Wh ≈ panel watts × sun hours × 0.75; → 09-02):

| | Peak sun hours at home | Our panels | Daily yield |
|---|---|---|---|
| June | {{ region.home.sun_hours_jun }} | {{ gear.solar_w_total }} W | ________ Wh |
| December, clear | {{ region.home.sun_hours_dec }} | {{ gear.solar_w_total }} W | ________ Wh |
| December, overcast | a fraction of the above | | a few hundred Wh at most |
| Snow-covered | | | **0** |

So the same panels deliver a fraction of their summer output on a good December day, and nothing on
a bad one, while your loads are up because it is dark by late afternoon and any medicine cooler still
has to run. **Two to three days of battery autonomy is a minimum where winter is long, and even that
assumes you can clear the panels afterwards.**

**Size on the conservative figure.** A tended, re-aimed panel on a perfect cold day can beat the
table; treat that as a best case to confirm by reading the station's input log, never as a sizing
number. When two numbers exist, the optimistic one gets used, and a plan sized on it fails on the
first ordinary clear day.

### How to get through winter
1. **Over-panel.** A December-sized set of panels looks far too big in July. That surplus is the
   insurance.
2. **Steep, adjustable tilt:** steep in winter, shallower in summer. Two adjustments a year.
3. **Reachable, sweepable mounting:** at ground level, where someone in boots with a broom can clear
   it in five minutes.
4. **Battery autonomy of three days or more**, kept warm indoors, sized on the winter number.
5. **A charging fallback:** a short generator run to bulk-charge the bank (→ 09-04), or a vehicle
   (→ 09-11). During a multi-day whiteout, this is what keeps Tier 0 alive.
6. **Shed load hard in winter.** Winter is Tier 0 and the barest Tier 1 (→ 09-01). Use daylight for
   work and go to bed early.
7. **Use power while the sun is up.** Charging and running the cooler hard at midday costs no
   storage.
{{#if is.cold_winters}}8. **Cold is also an asset.** In a winter as cold as yours, the outdoors can
   hold refrigerator temperatures for free, including for medicines, with freeze protection
   (→ 04-09, → 09-10). The cooler that was your hardest electrical load may become nearly free.
{{else}}8. **Where winters are mild, cooling loads stay year-round**, so the battery and panel
   margin matters even more (→ 09-10).
{{/if}}

### The winter routine for portable panels
Much of the advice above is written for a fixed array. Many households own **folding panels and
power stations that live indoors**. That changes winter from "maintain the array" to "deploy the
array", and it removes Hazard B, because nothing that charges ever goes outside.
- **Stations and batteries live indoors, warm, always.** The panels go to the cold; the batteries
  never do. Run the panel cable in through a window or door gap with a rolled towel stuffed in the
  opening: the heat lost through a towel-sealed one-inch gap is trivial against the harvest.
- **Deploy mid-morning, only in usable sun.** Panels on their kickstands, aimed true south at a
  steep tilt, **staked or weighted against wind**. A gust flips an unweighted kickstand panel, and a
  panel face-down on ice is a dead panel.
- **Wire for the cold:** use the configurations you worked out on → 09-03, and only those. In
  winter the safe choices are the ones whose cold voltage has the most margin.
- **Sweep with a soft brush, never a scraper,** whenever snow builds up. An inch of snow takes a
  panel to zero.
- **Re-aim once or twice** during the day if you are home: a portable panel following the low sun is
  the one advantage it has over a fixed mount.
- **Bring them in at dusk:** no wind loss, no theft, no one seeing them (→ 14-03), and the glass is
  warm and frost-free for the morning.

### The blizzard, concretely
A three-day blizzard (→ 17-01): whiteout, drifting, panels buried, temperatures well below zero,
wind chill that makes going outside dangerous (→ 08-05). Assume **zero generation for 72 hours or
more.** The plan for that window: batteries full going in (charge whenever the forecast turns),
Tier 0 loads only, a medicine cooling plan that needs no electricity when it is far below freezing
outside (→ 09-10), non-electric light, and heat from combustion with carbon monoxide alarms up first
(→ 08-04, → 08-01). **Then dig out and sweep.** If that sequence works on paper, your system is the
right size. If it does not, fix it now: more panel, more battery and less dependency, in that order.

## Gear and items

**Have it now (buy toward this):**

| Item | Why | Notes |
|---|---|---|
| Extra panels beyond the summer calculation | Winter output is a fraction | The cheapest watt you will buy |
| Adjustable tilt mount or A-frame | Steep winter angle, sheds snow | Buildable from 2×4s |
| Soft snow rake or long broom, non-abrasive head | The most-used winter solar tool | Never a metal scraper: it damages the glass coating |
| Controller or station with a **high maximum PV input voltage** | The cold voltage rise destroys undersized inputs | Run the → 09-02 check |
| Battery with low-temperature charge cutoff or internal heating | Prevents cold-charge damage | Indoors anyway |
| Insulated battery box or an interior battery spot | Cold batteries lose capacity and will not charge | In the heated room |
| Three or more days of battery autonomy | Storms last that long | Sized on the December number |
| Portable folding panel | Aim it, bring it in, carry it in Phase B | Backup if the main panels are buried |
| Stakes, sandbags or water jugs | Weight kickstand panels against wind | |
| Generator or vehicle charging path | The whiteout-week bridge | → 09-04, → 09-11 |

**Scavenge or substitute:**
- **Snow removal:** any soft broom, a push broom taped to a pole, a foam paint roller on an
  extension pole, a towel dragged across the glass.
- **Tilt:** anything that props a panel steeply facing south: the fence, a stepladder, pallets,
  snow banked into a wedge.
- **Reflectors:** white sheets, plywood or snow banked north of the panel bounce extra light onto it
  on clear days.
- **Battery warmth:** the heated room, an insulated box near (not on) the heat source, hot-water
  bottles in an insulated crate, a wool blanket. **Warm, not hot**, and never enclose a charging
  lead-acid battery without ventilation (→ 09-03).

## When it runs out
- **In winter, "running out" is a daily event.** The bank goes down every night and may not fully
  recover for days. Check the charge every morning; a bank that does not reach full after two sunny
  days is a fault to investigate.
- **Ration by tier and by time of day.** Electric things at midday. Shed Tier 1 the moment the bank
  drops below half. Defend Tier 0.
- **Substitutes for the dark half of the year:** light → lamps (→ 10-02); refrigeration → outdoor
  cold with freeze protection (→ 04-09, → 09-10); information → this binder.
- **Zero generation:** full batteries, a generator run, non-electric everything. **Zero generation
  and no fuel:** Tier 0 only, from a hand crank and a vehicle if one still runs (→ 09-11). Know where
  that floor is before winter.

## Phase notes
- **A (at home):** yard-deployed, sweepable, steeply tilted panels; batteries indoors.
- **B (moving):** **avoid moving in deep winter if there is any alternative** (→ 01-02, → 01-03). A
  folding panel in midwinter produces very little; assume you live on stored battery and vehicle
  charging for the move.
- **C (settled somewhere new):** room for a big, steep, ground-mounted array you can walk around.
  Open, windy sites also make a case for **small wind generation** as a winter complement where the
  windiest months are the least sunny (→ 09-11).

## Cross-references
→ 09-02 solar basics and the cold-voltage check · → 09-03 your wiring tables · → 09-07 cold limits
for batteries · → 09-04 the generator storm bridge · → 09-10 medicine cooling · → 09-16 outage day
one · → 08-01 heating one room · → 04-09 winter cold storage · → 17-01 blizzards and ice

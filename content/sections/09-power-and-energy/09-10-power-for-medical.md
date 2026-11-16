---
id: 09-10-power-for-medical
section: 09-power-and-energy
title: "Power for refrigerated medicine"
version: 2
revised: 2026-11-16
layer: core
danger_level: critical
phase: [A, B, C]
tags: [power, medical, refrigerated medicine, insulin, cold chain, cooler, sizing, thermometer]
derived_from: [09-10-power-for-medical]
sources:
  - us-fda-information-regarding-insulin-storage-and-swi-6448d3
  - american-diabetes-association-insulin-storage-and-sy-6f1f94
  - us-fda-epipen-epinephrine-injection-usp-auto-injecto-a9f17f
  - dometic-cfx3-35-product-page-r14
  - igloo-iceless-40-product-page-r14
related:
  - 09-01-power-priorities
  - 09-03-batteries-and-storage
  - 09-05-solar-in-winter
  - 09-06-charging-medical-devices
  - 09-16-outage-day-one
  - 01-02-go-no-go-decision
  - 02-01-cl01-type-1-diabetes-injections
  - 02-02-cl02-type-1-diabetes-pump-and-cgm
  - 02-03-cl03-anaphylaxis
  - 02-06-cl06-type-2-diabetes-on-insulin
  - 04-09-winter-cold-storage
  - 12-21-evaporative-cooling-pouches
  - 23-02-master-consumables-table
  - 29-07-ex07-refrigerated-medicines
  - 30-01-the-floors
  - 30-09-dc08-heat-exposed-medication
cards: [DC-08]
explainers: [EX-02, EX-07]
promote_when: [has.refrigerated_meds]
photo_slots:
  - { id: med-cooler, caption: "Our medicine cooler set up for an outage: which station port it plugs into, the thermometer inside" }
figures: []
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: { date: "2026-11-16", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "Cooling table re-sourced: compressor cooler (Dometic), thermoelectric limit (Igloo), fridge matched to EX-02/1.2 kWh; EpiPen storage as labelled (no 'frozen' claim); insulin 36-46 F and frozen floor checked against FDA" }
---

# Power for refrigerated medicine

**What this page is for.** Some medicines must stay cool: insulin, some injectable and biologic
drugs, some liquid antibiotics, some eye drops. Keeping them cool without the grid is often the
hardest electrical problem in the household. This page covers how to make and budget the
electricity, how to cut the load, and the non-electric paths to cold. **It does not tell you what
temperature or how long your medicine can tolerate.** That is on its label, in its condition module,
and on → 29-07.

> **SAFETY.** Take storage temperatures, in-use times and discard decisions **from the medicine's
> label and the condition module**, never from this page. Two rules apply everywhere:
> **A frozen-then-thawed insulin vial or pen is discarded.** Freezing destroys potency with no way to
> tell, and the published guidance is unanimous (→ 30-01). **Too cold is as dangerous as too warm.**
> Using a medicine after it has been too warm for longer than its published window is a decision
> card: {{choice DC-08}} (→ 30-09).
> For reference, unopened insulin is stored refrigerated at 36 to 46 °F (2 to 8 °C), not frozen (US
> FDA, Information Regarding Insulin Storage; American Diabetes Association, Insulin Storage).

## Do this now
- **Measure the real daily watt-hours of whatever you would use to cool medicine.** A full-size
  kitchen refrigerator (about 1,000 to 2,000 Wh a day) and a small 12 V compressor cooler (about
  280 Wh a day for one common model in a hot room) differ several times over, and that decides
  whether your system is adequate or hopeless. Plug it into a watt meter for 24 hours and
  write the number here: ________ Wh per day.
- **If you do not yet own a medicine cooler, a small 12 V compressor cooler is the purchase that
  matters.** Compressor, never thermoelectric (see below).
- **Build the non-electric cold plan at the same time** (→ 04-09, → 12-21). Electricity is one path to
  cold; it should never be the only one.
- **Turn off any power-saving ("ECO") setting on the station port the cooler will use.** Many
  stations switch an output off after an hour or more of tiny load, and a compressor cooler resting
  between cycles looks like nothing is plugged in. If the cooler's display is ever dark, re-enable
  the port and check the thermometer (→ 09-03).
- **Run the cooler for 24 hours on the station you will use, with a min/max thermometer inside,**
  before you ever need it. Confirm it holds the medicine's range; leave that thermometer in the
  cooler's box as the designated one. {{photo med-cooler}}
- **Decide the go/no-go trigger now, in writing:** if you cannot keep the medicine usable *and*
  cannot replace it, that is a decision about leaving (→ 01-02), not something to ride out.

## Why it works this way

### Why refrigeration is the expensive load
Cooling is a heat pump. It runs a motor and fights the room temperature all day, every day. That is a
different shape of load from a phone:

| Device | Running W | Wh per day | Notes |
|---|---|---|---|
| Phone | 5 to 20 W briefly (typical) | **10 to 20 Wh** (typical) | Trivial |
| **12 V compressor cooler**, example: Dometic CFX3 35 (36 litres) | Up to 90 W while the compressor runs (7.5 A rated) | **About 280 Wh** (0.98 amp-hours per hour at 12 V, room at 90 °F, inside at 39 °F) | Less in a cooler room; the duty cycle depends heavily on room temperature |
| Dorm or mini fridge | Label watts | **EnergyGuide label ÷ 365** | Measure it: small fridges are not always frugal |
| Full-size refrigerator | 100 to 200 W while the compressor runs (typical) | **About 1,000 to 2,000 Wh** (typical, → 29-02); EnergyGuide label ÷ 365 for yours | Big |
| **Thermoelectric ("Peltier") cooler** | Label watts, **drawn the whole time it cools** | **Label watts × 24** | **Cools only up to about 38 °F below the room (Igloo, Iceless 40). Avoid.** |

**Read the thermoelectric row carefully.** Those coolers are cheap, common and sold as "12 V
refrigerators", and they are the **worst choice** here. They cool only to a fixed amount below the
room (up to about 38 °F below it for one common model; Igloo), so on a hot day they may not reach
the medicine's range at all; and because they work by running continuously, their daily use is
simply their label watts × 24. Compare that with a compressor cooler's figure before you buy.

### Sizing against reality
**Worked example:** a cooler at about **350 Wh a day**, with 400 W of panels at a northern location
(→ 09-05):

| Condition | Panel yield | Cooler need | Result |
|---|---|---|---|
| June, clear | about 1,800 Wh | 350 Wh | Easy: big surplus |
| December, clear, panels swept | about 750 Wh | about 250 Wh (colder room = less work) | Workable, with margin |
| December, overcast | about 150 to 300 Wh | about 250 Wh | **Break-even at best: living off the battery** |
| Blizzard, panels buried | **0** | about 250 Wh | **Battery only: three days ≈ 750 Wh for the cooler alone** |

That table is the argument for over-paneling (→ 09-05), for three or more days of battery, and for
the non-electric paths below.

**How long our stations run the cooler** (estimates; the percentage on the screen is the truth):

Days per charge ≈ station Wh × 0.85 ÷ (cooler Wh per day + 24 × the station's idle watts).

The station's **idle draw** matters: with the AC inverter on, a station can use nearly as much
running itself as a small cooler uses. **Run the cooler from the 12 V port with the AC inverter off.**
Measure the idle: fully charged, inverter on, nothing plugged in, note the percentage after 12 hours.

| Station | Wh | Idle W (measured) | Cooler Wh per day | Days per charge |
|---|---|---|---|---|
{{#each stations as s}}| {{s.model}} | {{s.wh}} | ______ | ______ | ______ |
{{else}}| ______ | ______ | ______ | ______ | ______ |
{{/each}}

For a **full-size refrigerator** (about 1,000 to 2,000 Wh a day, → 09-01; this estimate uses
1,200 Wh), our whole bank of
{{ gear.station_wh_total }} Wh gives roughly **{{ derived.station_fridge_days }} days**: an estimate
that leaves out idle draw and anything else plugged in. Measure your own as above. Pick the
percentage at which you move the cooler to the next station, and write it here: ______ %.

**Having two stations makes the electric path redundant:** one dead inverter or one failed battery
no longer ends it. Either station's 12 V port can run the cooler, with ECO off on whichever it moves
to.

### Two ways to set up day to day
- **Station as a UPS:** the medicine lives in the cooler, the cooler on a station that stays plugged
  into the wall in pass-through or UPS mode (if your station supports it, → 09-03). A grid failure
  is then a switchover of milliseconds. Costs: the station is tied up, and it sits at full charge.
- **Kitchen fridge, cooler ready:** the medicine lives in the kitchen fridge; the cooler, the station
  and the designated thermometer are staged. When the power fails, you set up the cooler and move
  the medicine once the cooler reads within the label range (step by step on → 09-16). Costs: it
  depends on someone doing it within the first hours.

Our set-up: ________________________________________.

{{#if is.cold_winters}}
### The winter insight: cold can be free
For several months a year here the outdoors is a refrigerator, and often a freezer. A well-managed
insulated container in an unheated space, a shaded north side, a snow cache or a buried container can
hold refrigerator temperatures with **zero watts** (→ 04-09). Two cautions:
- **A garage with a thermostat-controlled heater is not "unheated" while the grid is up.** It
  becomes passive cold only when that heater is off.
- **Freezing is the winter danger.** The problem flips from "make cold" to "hold a narrow band and
  never freeze". That is a job for insulation, thermal mass and a **thermometer with min/max memory**,
  checked daily, not for a compressor.

**The seasonal pattern:**
- **Winter:** passive cold with freeze protection and a min/max thermometer. Electrical cooling load
  near zero, just when solar is weakest.
- **Summer:** solar is strongest, and so is the cooling load. Run the compressor cooler on the
  surplus.
- **Spring and autumn:** mixed. Cooler when it is warm; passive cold on cold nights; watch the
  thermometer.
{{else}}
### Where winters are mild
Here, cooling is a year-round load. The battery and panel margin matter more, and the evaporative
and ground-cooling paths below are your non-electric options. Winter nights can still dip below
freezing: keep a min/max thermometer in any passive store.
{{/if}}

### Making the cooling load smaller: cheaper than making more power
1. **Insulate the container heavily.** Extra rigid foam around a small cooler cuts the duty cycle a
   lot. Insulation costs nothing to run.
2. **Cool a small volume.** You are cooling **vials and pens**, not groceries.
3. **Add thermal mass.** Water bottles or gel packs inside hold the temperature through the night and
   a cloudy stretch, so the compressor can run at midday when the sun is up.
4. **Site it cool:** the coolest room, out of the sun, away from any heater.
5. **Open it rarely.** Every opening dumps the cold air.
6. **Run it on 12 V DC directly:** no inverter, no conversion loss, no inverter idle draw.
7. **Pre-cool at midday** and let it coast overnight.

### Other medicines with temperature rules
{{#if has.epinephrine}}**Epinephrine auto-injectors** are a different problem from insulin: EpiPen's
label says store at 68 to 77 °F, with short excursions allowed from 59 to 86 °F, protect from
light, and **do not refrigerate** (US FDA, EpiPen prescribing information). **Their winter risk is
cold.** In a house heated to one
room, the auto-injectors stay in the warm room with you, not in a cold car or a go-bag in the
garage. Check the label and → 02-03.
{{else}}**Epinephrine auto-injectors**, if anyone ever carries them, are stored at room temperature
(EpiPen: 68 to 77 °F, excursions 59 to 86 °F) and **not refrigerated** (US FDA, EpiPen prescribing
information); their winter risk is cold (→ 02-03).
{{/if}}
Test strips, glucagon and other supplies have their own ranges; see their modules. The electrical
answer is the same: small insulated volume, thermometer, seasonal plan.

### Redundancy: because this load is life-critical
Have **three independent paths to cold**, and know which one you are on:
1. **Electric:** a 12 V compressor cooler on a station or battery.
2. **Passive:** an insulated container using outdoor cold, ground temperature or a snow or ice cache
   (→ 04-09), with freeze protection.
3. **Evaporative or cold water:** evaporative cooling pouches made for medicine (→ 12-21), a wet
   cloth over a container in moving air, a sealed container in a cold stream or well.

Plus a **min/max thermometer** on the store, checked and logged daily. **Without a thermometer you
have a guess, not a cold chain.**

### Our refrigerated medicines
{{#if has.refrigerated_meds}}This household has at least one medicine marked refrigerated.{{/if}}
The household's medicine list (the "refrigerated" column shows which ones this page is about):

| Who | Medicine | Strength | Refrigerated? | Label storage range (copy from the label) |
|---|---|---|---|---|
{{#each meds as m}}| {{m.member}} | {{m.name}} | {{m.strength}} | {{m.refrigerated}} | ______ |
{{else}}| | | | | |
{{/each}}

## Gear and items

**Have it now (buy toward this):**

| Item | Why | Notes |
|---|---|---|
| **12 V compressor cooler**, small (15 to 25 qt) | The right electric cooling device: a fraction of the energy of anything else | **Never** thermoelectric |
| Rigid foam board and tape to over-insulate it | Cuts the duty cycle; costs no watts | Cheapest efficiency gain there is |
| **Min/max digital thermometers** with an external probe, several | You cannot manage a cold chain you cannot measure | Spare batteries |
| Insulated medicine travel case or evaporative pouches | Phase B and daily carry | → 12-21 |
| Gel packs or water bottles for thermal mass | Coast overnight and through cloud | Free if you use water |
| Battery capacity beyond the → 09-09 build, or a second station | This load is the reason to over-size | |
| A second cooling method, tested | Redundancy | Test it before you need it |
| Insulated cooler and a way to cache snow or ice | The winter and shoulder-season answer where it is cold | → 04-09 |
| Notebook for a daily temperature log | Turns a guess into evidence | Keep it with this binder |

**Scavenge or substitute:**
- **Insulation:** foam board, packing foam, bubble wrap, blankets, straw, sawdust, leaves: anything
  that traps air. More insulation lets less heat leak in, so the compressor runs less.
- **Passive cold:** a shaded pit on the north side, a basement floor, a buried container, a snow
  cache, a spring, a creek, a well. Ground a few feet down is remarkably stable.
- **Evaporative cooling:** a wet towel over a container in moving air; the pot-in-pot with damp sand
  between. Works best in dry heat.
- **Vehicle:** a running car's 12 V socket can power a cooler (→ 09-11). **Never leave medicine in a
  car in summer heat or a hard freeze.**
- **What you cannot substitute:** the thermometer, and the label's temperature rules.

## When it runs out
- **When the power runs out, cold does not have to.** Fall back in this order: **electric cooler →
  passive cold → evaporative, ground or water cooling →** the room-temperature times printed on the
  medicine's label and in its module.
- **Runway: work two numbers and write them on → 23-02:** (a) days of battery that will run the
  cooler alone with no generation, and (b) **days of medicine supply left**. **Whichever is shorter
  is your real clock**, and it is very often (b).
- **Ration:** shed every other load to defend this one. Shrink to the smallest cooled volume. Run
  the cooler at midday from direct generation and coast on thermal mass at night.
- **Resupply:** cooling can be improvised; **the medicine often cannot.** Medicine supply is a main
  input to the go/no-go decision (→ 01-02).
- **Escalation, written as decisions, not worries:**
  - Cold chain cannot be held **and** the weather is warm → act today.
  - Medicine supply below your written threshold with no resupply path → go/no-go (→ 01-02).
  - Cannot power the medical devices **and** cannot keep the medicine usable → the highest-priority
    emergency in this binder: the condition module and → 01-02, now.

## Phase notes
- **A (at home):** cooler on a station or battery when it is warm; passive cold with freeze
  protection when it is cold; thermometer logged daily. Build and **prove** all three paths.
- **B (moving):** an insulated case and thermal mass, or evaporative pouches (→ 12-21). **Cold is a
  packing problem while moving**, unless the vehicle can run the cooler. In winter the risk flips to
  freezing: keep medicine inside your clothing layers, not in an outside pocket or a pack strapped
  to a vehicle.
- **C (settled somewhere new):** a root cellar or buried store gives stable cool temperatures year
  round with zero energy (→ 04-09). Keep the 12 V cooler as the summer fine-control on top of it.

## Cross-references
→ 29-07 refrigerated medicines explained · → 09-01 load triage · → 09-03 stations, ports and ECO
settings · → 09-05 winter solar · → 09-06 device charging · → 09-16 outage day one (when and where
the cooler is set up) · → 04-09 winter cold storage · → 12-21 evaporative cooling pouches · → 01-02
go/no-go · → 30-09 heat-exposed medication card

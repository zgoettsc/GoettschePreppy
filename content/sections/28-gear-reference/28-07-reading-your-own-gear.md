---
id: 28-07-reading-your-own-gear
section: 28-gear-reference
title: "Reading your own gear: data plates, panel labels, BTU plates, safety marks and dates"
version: 1
revised: 2026-11-16
layer: gear
danger_level: caution
phase: [A, B, C]
tags: [data plate, rating label, nameplate, Voc, Isc, watts, amps, BTU, fuel type, UL, ETL, CSA, NRTL, date code, CO alarm, end of life, multimeter]
derived_from: [28-02-equipment-inventory, 28-03-solar-fundamentals, 28-08-deployment-procedure, 28-17-maintenance-schedule, 08-02-carbon-monoxide-safety]
sources:
  - osha-nrtl-program
  - cpsc-carbon-monoxide-questions-and-answers-783766
  - renogy-rsp200d-g3-datasheet
  - victron-smartsolar-mppt-100-30-100-50-datasheet
  - mr-heater-mh18b-big-buddy-manual-outdoor-edition
  - generac-gp3500io-owners-manual
  - nist-lpg-20-pound-cylinders-2021
related: [29-14-ex14-reading-a-label, 29-12-ex12-extinguishers-blankets-and-alarms, 29-02-ex02-batteries-and-power-stations, 28-01-power-stations, 28-02-solar-panels-and-controllers, 28-03-generators, 28-04-portable-heaters, 28-05-radios, 28-06-water-filters, 08-02-carbon-monoxide-safety, 09-12-ac-dc-cables-and-connectors, 09-02-solar-basics]
cards: []
explainers: [EX-02, EX-03, EX-14]
promote_when: [experience.new]
photo_slots:
  - { id: plates-power, caption: "Data plates of our power stations, generator and solar panels" }
  - { id: plates-heat, caption: "Rating plates of our heaters, and the dates on our CO and smoke alarms" }
figures: [fig-data-plate-example]
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: null
---

# Reading your own gear: data plates, panel labels, BTU plates, safety marks and dates

**What this page is for.** The tables in this section cover popular models. Yours may be another
brand, an older version, or a revision with different numbers under the same name. Every piece of
gear carries its own limits on a label or plate, and **that label is the authority**. This page
shows where to find the label on each kind of gear, what each number means, and which numbers to
copy into the "Our gear" tables (→ 28-01 to → 28-06). The general guide to labels, fuel cans,
cylinders and medicines is → 29-14.

**Do this now, while the power is on and you can still look things up:**

1. Find the label on every power station, panel, generator, heater, radio, filter and alarm.
2. Photograph each one into the app, close and sharp, and a second photo of where it is.
3. Copy the key numbers into the "Our gear" table on that kind of gear's page.
4. Write the date on anything that wears out: filters, CO alarms, batteries, fuel.

## Where the label is

| Gear | Usually found |
|---|---|
| Power station | Underside or back; input limits also printed beside each input port |
| Solar panel | Back of the panel, near the junction box; on folding panels inside a flap |
| Generator | Sticker or plate on the frame or engine cover; engine and emissions labels separate |
| Heater | Rating plate on the back, base or inside a door |
| Radio | Inside the battery compartment |
| Filter | Box, leaflet or the element itself; often not on the device. Keep the box |
| CO and smoke alarm | Back of the alarm: take it off its base |

## Electrical nameplates: volts, amps, watts

- **V (volts)**, **A (amps)**, **W (watts)**, and sometimes **VA** or **kVA** instead of watts
  (for planning, read 1.8 kVA as 1,800 W). Watts = volts × amps (→ 29-02).
- **"~" means AC** (household-type power); **"⎓" means DC** (battery-type power). "120V~ 15A"
  is an AC rating; "11–60V⎓15A" is a DC input range and current.
- **Rated, continuous or running** is what it does all day. **Max, peak, surge or starting** is a
  short burst.
- **Hz** (60 in the US) and **phase** (1 for household gear).
- **Input** lines tell you what may feed it. **Output** lines tell you what it can power. On a
  power station, copy every input line, especially the solar (PV or DC) input **voltage range**:
  that top number is the one never to exceed (→ 28-01).
- **Generators** also print the outlet types and often whether they are "transfer switch ready".
  The manual adds what the plate leaves out: Generac's, for example, says maximum power drops
  about 3.5 % per 1,000 ft of altitude (→ 28-03).

## Solar panel labels: Voc and Isc first

The panel label lists **Pmax** (watts), **Voc**, **Isc**, **Vmp** and **Imp** at **STC** (the
lab's standard bright sun at 77 °F), plus **maximum system voltage** and **maximum series fuse**.
A datasheet may add the **temperature coefficient of Voc** (Renogy's RSP200D sheet gives −0.28 %
per °C). Copy Voc and Isc for every panel; they set the cold check (→ 28-02, → 09-02).

**Check Voc with a multimeter** before the first connection of any panel or string:

1. Panel in full sun, **not connected to anything**.
2. Multimeter on **DC volts**, range above the expected reading.
3. Red probe to the panel's positive lead, black to negative (→ 09-12 for connector tips).
4. The reading should be close to the label Voc, higher on a cold morning. A string reads the sum.
5. Write the reading, the date and the air temperature on the label photo.

A controller label gives its limits the same way. Victron's model number carries two of them:
"100/30" is 100 V maximum solar voltage and 30 A charging current (→ 28-02).

## Heater rating plates: BTU and fuel

- **Input in BTU/h**, for each setting (LO, MED, HI).
- **Fuel type**: "Propane (LP)", "1-K kerosene", "natural gas". Never another fuel (→ 29-01).
- **Gas pressure** on propane heaters with hoses or quick-connects, for example "regulated to
  11 in W.C." (inches of water column) on the Big Buddy manual. That tells you which regulator
  and hose it needs.
- **The use wording**: "for indoor use", "emergency indoor use", "for outdoor use only", "not for
  use in living or sleeping areas". Copy it exactly (→ 28-04).
- **Clearances**, the **minimum fresh-air opening**, and any **altitude** line. Many are in the
  manual, not on the plate: keep the manual with the heater.

## Fuel cylinders

Propane cylinder collars are stamped with the DOT specification, **TW** (tare weight, the empty
weight) and the date of manufacture: → 29-14. A "20-lb" cylinder is often sold filled to 15 lb
(NIST); weigh it against TW to know what is in it (→ 28-04).

## Safety marks: UL, ETL, CSA and others

A small mark such as **UL**, **ETL** (Intertek) or **CSA**, often in a circle, means a **Nationally
Recognized Testing Laboratory** tested and certified the product to a product safety standard;
OSHA recognises these laboratories, and each uses its own registered mark, which the maker may
apply only after certification (OSHA, Nationally Recognized Testing Laboratory Program). The
words "listed" or "certified" go with the mark. **A mark does not make an outdoor-only heater
safe indoors**: it certifies the product for the use on its label.

## Dates: date codes, alarms and anything that wears out

- **Serial number and date code.** Most gear carries a serial number and often a date of
  manufacture, sometimes as a code. Write the purchase date beside it. Recall notices and
  manuals are matched by model and serial number (→ 29-14).
- **CO alarms.** Alarms have a recommended replacement age, given in the product literature or by
  the maker (CPSC, Carbon Monoxide Questions and Answers). Look on the back for the manufacture
  date and any "replace by" date, and write the replacement date on the front with a marker.
  **The test button tests the circuit, not whether the sensor still detects CO** (CPSC). An alarm
  past its date is replaced, not trusted. If the leaflet describes an end-of-life signal (a
  pattern of chirps), tape that page inside a cupboard door so nobody mistakes it for a low
  battery.
- **Smoke alarms:** follow the replacement age in their leaflet the same way (→ 29-12).
- **Batteries, filters, fuel:** write the first-use or fill date on each (→ 03-09, → 06-06).

{{figure fig-data-plate-example}}

## What we copied, and where

| Gear | Model and serial | Photo taken | Numbers copied to | Date-limited? Replace by |
|---|---|---|---|---|
| Power stations | ______ | yes / no | → 28-01 | — |
| Solar panels | ______ | yes / no | → 28-02 | — |
| Generator | ______ | yes / no | → 28-03 | — |
| Heaters | ______ | yes / no | → 28-04 | — |
| Radios | ______ | yes / no | → 28-05 | — |
| Water filters | ______ | yes / no | → 28-06 | ______ |
| CO alarms ({{ gear.co_alarms }}) | ______ | yes / no | this page | ______ |
| Smoke alarms ({{ gear.smoke_alarms }}) | ______ | yes / no | this page | ______ |

{{photo plates-power}}

{{photo plates-heat}}

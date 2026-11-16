---
id: 28-04-portable-heaters
section: 28-gear-reference
title: "Portable fuel heaters: the specs that keep you safe, and common models"
version: 2
revised: 2026-11-16
layer: gear
danger_level: critical
phase: [A, B, C]
tags: [heater, propane heater, kerosene heater, forced-air heater, BTU, oxygen depletion sensor, tip-over switch, ventilation, altitude, propane cylinder, cubic feet, spec table]
derived_from: [08-09-mr-heater-buddy, 08-10-dyna-glo-kerosene-heater, 08-04-emergency-heat-options, 08-01-heating-one-room, 28-12-generator-and-fuel]
sources:
  - enerco-group-mr-heater-manufacturer-portable-buddy-r-759ce5
  - ghp-group-inc-dyna-glo-manufacturer-portable-kerosen-477cfd
  - mr-heater-mh4b-little-buddy-manual
  - mr-heater-mh18b-big-buddy-manual-outdoor-edition
  - toyotomi-omni-230-product-introduction
  - dyna-glo-kfa-forced-air-kerosene-heater-manual
  - matheson-propane-physical-properties
  - nist-lpg-20-pound-cylinders-2021
  - cdc-carbon-monoxide-poisoning-basics-772153
  - cpsc-carbon-monoxide-questions-and-answers-783766
related: [08-01-heating-one-room, 08-02-carbon-monoxide-safety, 08-04-emergency-heat-options, 08-09-portable-propane-heaters, 08-10-wick-kerosene-heaters, 06-05-alternative-fuels, 06-06-fuel-storage-safety, 28-07-reading-your-own-gear, 29-01-ex01-fuels, 29-03-ex03-carbon-monoxide, 30-01-the-floors, 30-02-dc01-unvented-heater-overnight, 30-03-dc02-propane-cylinder-indoors, 30-04-dc03-refilling-1-lb-cylinders, 30-18-dc17-old-fuel]
cards: [DC-01, DC-02, DC-03, DC-17]
explainers: [EX-01, EX-03, EX-14]
promote_when: [has.unvented_heater, is.cold_winters]
photo_slots:
  - { id: heater-plates, caption: "The rating plate of each of our heaters: BTU, fuel, indoor or outdoor wording, vent opening" }
figures: []
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: { date: "2026-11-16", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "All 8 heater rows re-read against the manuals; Big Buddy run time filled from its manual; WK11C8 ODS cell reworded to what the manual says; 170 cu ft (Matheson 8.62 cu ft/lb) and 15-lb fill (NIST) re-read; LFL arithmetic added to match 08-09." }
---

# Portable fuel heaters: the specs that keep you safe, and common models

**What this page is for.** A portable fuel heater burns propane or kerosene in the room and lets
the exhaust out into the room. That is what "unvented" means. Every one of them makes carbon
monoxide (CO), uses up the room's oxygen and can start a fire. This page lists the numbers and
words on a heater's label and manual that decide where it may run, how much air it needs, and how
fast it uses fuel, then gives them for common models from the makers' own manuals. How to set up
and run one: propane → 08-09, kerosene wick → 08-10, the warm room → 08-01.

> **SAFETY.** Battery CO alarms on every level and outside sleeping areas, tested, whenever any
> fuel burns indoors (CPSC, Carbon Monoxide Questions and Answers; → 08-02). An ODS or tip-over
> switch is **not** a CO alarm.
> **Fuel is never stored or transferred near an open flame or a running appliance.** Vapour
> ignites. Refuel and change cylinders outdoors, with the heater off and cool (→ 30-01).
> A heater labelled **"For Outdoor Use Only"**, and any construction-type forced-air heater, is
> never run in living or sleeping space.

## What matters and why

1. **Heat, in BTU per hour (BTU/h).** A BTU is a unit of heat. More BTU/h warms more space and
   burns fuel faster. Many heaters have LO and HI settings; the manual may limit which setting is
   allowed in a small room.
2. **Fuel use per hour, or run time per cylinder or tank.** Lets you work out how long your fuel
   lasts (method: → 06-05). Run times are shorter in hard cold.
3. **Indoor or outdoor, in the maker's own words.** Read the exact wording on the label and in the
   manual: "for indoor use", "emergency indoor use", "small recreational enclosures", "for outdoor
   use only", "never use in living or sleeping areas". **The same family name can carry different
   wording**: the Big Buddy manual read for this kit says "For Outdoor Use Only" on its cover,
   while the Portable Buddy and Little Buddy manuals describe indoor use with fresh-air openings.
   Go by the label on yours.
4. **Oxygen depletion sensor (ODS) and tip-over switch.** An ODS shuts off the gas when the room's
   oxygen drops. A tip-over switch shuts it off if knocked over. Wick kerosene heaters usually
   have a tip-and-jar shut-off and **no ODS**: the Dyna-Glo WK11C8 manual lists only its automatic
   shut-off for when the heater is jarred or tipped. **Neither device measures
   CO** (→ 08-09).
5. **The fresh-air opening the manual specifies.** Each manual gives its own: a size of opening in
   square inches, or a rule based on room volume. It is part of the heater's safe operation, not
   a suggestion (examples in the table).
6. **Altitude limit.** Propane radiant heaters burn weakly and may shut off above 7,000 feet (Mr.
   Heater manuals). {{#if is.high_altitude}}Your home is about {{ region.home.elevation_ft }} ft
   up: read your heater's altitude line before you need it.{{/if}}
7. **Clearances** to anything that burns, and **the sleeping rule**: the Buddy manuals say never
   operate the heater while sleeping; the Dyna-Glo kerosene manual says turn it off before bed.
8. **Fuel type and connection.** Kerosene heaters take water-clear 1-K kerosene only (→ 29-01).
   Propane heaters take 1-lb cylinders, or a larger cylinder **kept outdoors** on the maker's
   hose, with the regulator in place.

**The two decisions this page does not make for you.** Running an unvented heater while people
sleep: {{choice DC-01}} → 30-02. A propane cylinder larger than 1 lb inside the house:
{{choice DC-02}} → 30-03. Refilling 1-lb cylinders: {{choice DC-03}} → 30-04. Old kerosene in a
heater: {{choice DC-17}} → 30-18. Each card explains the hazard, the maker's rule and the options.

## How much gas is in a propane cylinder

- A "20-lb" cylinder is named for the most propane it can safely hold. **Most are filled and
  labelled to 15 lb net**, even though the cylinder can safely hold 20 lb (NIST, Liquefied
  Petroleum Gas 20 Pound Cylinders). Weigh it: empty weight (stamped "TW" on the collar, → 28-07)
  plus the propane.
- One pound of propane makes about **8.6 cubic feet of gas** (8.62 cu ft per lb at 70 °F;
  Matheson, propane physical properties). So a full 20-lb cylinder holds about **170 cubic feet
  of gas**, and a 15-lb fill about 130. **Watch the decimal point: 170, not 1,700.**
- Propane burns when it makes up between 2.1 % and 9.5 % of the air (Matheson). At 2.1 %, the
  170 cubic feet in a full cylinder is enough to make about 8,000 cubic feet of air able to
  burn: more than a whole room. The Buddy heater manuals allow a 20-lb cylinder only outdoors
  (→ 08-09); whether one ever comes inside is a decision card (→ 30-03).
- Gallons, total BTU and the hours-per-cylinder method: → 06-05.

## Common models, from the makers' own manuals

"See label" means the document read for this kit did not give it. Rows marked with a manual
summary come from the kit pages that were written from that manual (→ 08-09, → 08-10).

| Model | Fuel | Heat, BTU/h | Fuel use or run time | Indoor wording in its manual | ODS | Tip-over | Fresh-air opening the manual specifies | Altitude | Source |
|---|---|---|---|---|---|---|---|---|---|
| Mr. Heater Little Buddy MH4B | Propane, 1-lb cylinder | 3,800 | About 5 h per 1-lb cylinder | "Emergency indoor use"; recreational or commercial enclosure with a window or roof vent; outdoors | Yes | Yes | **4 sq in** (2 × 2 in) | May shut off above 7,000 ft | Mr. Heater, MH4B owner's manual |
| Mr. Heater Portable Buddy MH9BX | Propane, 1-lb or outdoor cylinder up to 20 lb on hose | 4,000 LO / 9,000 HI | 3–6 h per 1-lb; 48–110 h per 20-lb | Indoor, with openings; bathroom LO only; never while sleeping | Yes | Yes | **9 sq in at ceiling level and 9 sq in at floor level** | Weak burning, possible shut-off above 7,000 ft | Enerco/Mr. Heater, Portable Buddy manual (→ 08-09) |
| Mr. Heater Big Buddy MH18B (edition read) | Propane, 1-lb or outdoor cylinder up to 20 lb on hose | 4,000 / 9,000 / 18,000 | Rough guide: 1.5–6 h per 1-lb cylinder; 24–108 h per 20-lb | **"For Outdoor Use Only"** on this edition; check yours | See label | Yes | **18 sq in** (4.25 × 4.25 in) | May shut off above 7,000 ft | Mr. Heater, MH18B owner's manual |
| Dyna-Glo WK11C8 (wick, convection) | 1-K kerosene | 10,500 | 0.079 gal/h; about 13 h per 1.1 gal tank | Indoor, with ventilation; off before bed | **None listed** | Tip-and-jar shut-off | If room has under **200 cu ft per 1,000 BTU/h**, open a window **at least 1 in** or open doors to other rooms; never a bathroom or small closed room | Not given | GHP Group/Dyna-Glo, WK11C8 manual (→ 08-10) |
| Toyotomi Omni 230 (wick) | Kerosene only | 23,000 | 0.659 L/h; 12–16 h per 7.5 L tank | See label and manual | See label | Automatic shut-off when bumped or tipped | See manual | See label | Toyotomi, Omni 230 product introduction |
| Dyna-Glo KFA50DGD (forced air) | 1-K kerosene preferred; manual also allows #1/#2 diesel or fuel oil, Jet A, JP-8; 120 V fan | 50,000 | 0.38 gal/h; 5.0 gal tank | **"Never use this heater in living or sleeping areas"** | No (flame-out sensor) | See label | **3 sq ft** of fresh outside air per 100,000 BTU/h | See label | GHP Group/Dyna-Glo, KFA forced-air manual |
| Dyna-Glo KFA80DGD (forced air) | As above | 80,000 | 0.60 gal/h; 5.0 gal tank | As above | No | See label | As above | See label | Same manual |
| Dyna-Glo KFA135DGD (forced air) | As above | 135,000 HI / 95,000 LO | 1.02 / 0.72 gal/h; 10.0 gal tank | As above | No | See label | As above | See label | Same manual |

The forced-air rows are here because they are sold beside home heaters and look like a quick fix.
Their manual says to use them only in well-ventilated areas, never in living or sleeping areas,
with 8 feet of clearance in front of the outlet and 4 feet at the sides, top and rear. **They
are not warm-room heaters.**

Heat Hog, Sengoku (KeroHeat, HeatMate) and other heaters were looked for and left out because the
kit could not read a manual from the maker itself. If you own one, its rating plate and manual
carry every number in these columns (→ 28-07).

## Our heaters

{{#if has.unvented_heater}}From settings:{{else}}We have not entered a fuel heater. If you get
one, add it here:{{/if}}

| Heater | Model | BTU/h LO / HI | Fuel | Run time per cylinder or tank | Indoor wording on label | ODS? | Vent opening required | Altitude limit |
|---|---|---|---|---|---|---|---|---|
{{#each heaters as h}}| {{h.kind_text}} | {{h.model}} | ______ / ______ | ______ | ______ | ______ | yes / no | ______ sq in | ______ ft |
{{else}}| ______ | ______ | ______ / ______ | ______ | ______ | ______ | yes / no | ______ sq in | ______ ft |
{{/each}}

Our propane on hand: **{{ gear.fuel.propane_1lb }}** 1-lb cylinders and
**{{ gear.fuel.propane_20lb }}** 20-lb cylinders. Our kerosene: **{{ gear.fuel.kerosene_gal }}**
gallons. CO alarms: **{{ gear.co_alarms }}**.

{{photo heater-plates}}

---
id: 30-03-dc02-propane-cylinder-indoors
section: 30-decisions-and-floors
title: "DC-02. A propane cylinder larger than 1 lb inside the house"
version: 1
revised: 2026-11-16
layer: card
danger_level: critical
phase: [A, C]
tags: [decision card, propane, cylinder, 20-lb tank, indoors, leak, explosion, heater]
derived_from: [08-09-mr-heater-buddy, 06-06-fuel-storage-safety, 08-04-emergency-heat-options, 08-01-heating-one-room]
sources:
  - enerco-group-mr-heater-manufacturer-portable-buddy-r-759ce5
  - nfpa-nfpa-58-liquefied-petroleum-gas-code-storage-of-13af35
  - propane-education-and-research-council-perc-safety-g-40ea6b
  - cdc-carbon-monoxide-poisoning-basics-772153
related: [08-09-portable-propane-heaters, 08-04-emergency-heat-options, 08-01-heating-one-room, 06-06-fuel-storage-safety, 06-05-alternative-fuels, 29-01-ex01-fuels, 29-03-ex03-carbon-monoxide, 30-02-dc01-unvented-heater-overnight, 30-01-the-floors]
cards: [DC-02, DC-01]
explainers: [EX-01, EX-03]
promote_when: [has.propane_heater]
card: DC-02
figures: [fig-propane-pools-low]
options:
  - id: never
    label: "Never indoors"
    summary: "Cylinders over 1 lb stay outdoors. If the hose-through-a-window route fails, use another heat source or the cold-night methods; the tank does not come in."
  - id: last-resort
    label: "Last resort: cylinder outside, hose through a window"
    summary: "The cylinder always stays outdoors. Only a heater rated for a remote cylinder is fed through the maker's hose, passed through a cracked window or door. The tank never comes inside."
  - id: indoors-with-rules
    label: "Indoors with rules"
    summary: "Only when the outdoor-hose route is impossible: an above-ground room, never a basement; valve closed whenever the heater is off; no pilot-light appliances nearby; leak test; CO alarm; adult awake; tank out as soon as possible."
settings_summary: "A 20-lb propane cylinder (the grill size) holds about twenty times the gas of a 1-lb camping cylinder. Heater makers and the national propane code keep anything over the 1-lb size out of the house. The reason: propane is heavier than air. A leak at the valve, hose or regulator flows along the floor, collects in low places such as basements, and explodes when it reaches a flame such as a pilot light or the heater itself. A cylinder warmed indoors can also vent gas through its safety valve on purpose. What helps most: tank outdoors (removes the risk); maker's hose through a window (reduces it a lot); if it must come in, above-ground room, valve closed when off, leak test, no pilot flames nearby, adult awake (reduces it a little)."
review_pass: null
---

# DC-02. A propane cylinder larger than 1 lb inside the house

**What this page is for.** When the power is out and it is very cold, it is tempting to bring
the grill tank inside to run a heater. This card explains why makers and the propane code say
no, what actually goes wrong, and what the household decides.

> **SAFETY.** Fuel is never stored or transferred near an open flame or a running appliance
> (floor, → 30-01). If you smell gas (a rotten-egg smell) near a cylinder indoors: do not
> switch anything on or off, close the tank valve if you can reach it, put out flames, get
> everyone out and open doors on the way.

## 1. The thing, in plain words

**Propane** is a fuel gas stored as a liquid under pressure in steel cylinders (→ 29-01). The
small green **1-lb cylinder** is the camping size. The **20-lb cylinder** is the grill tank.
Bigger tanks hold more. Propane in the air is **heavier than air**: it sinks and spreads along
the floor like invisible water. A rotten-egg smell is added so you can smell a leak, but only
if your nose is near where it pools.

Some indoor-rated propane heaters can run from a large cylinder through a hose. The heater
maker designs that for **the cylinder outdoors**, the hose through a window.

{{#if has.basement}}Your home has a basement. Propane that leaks anywhere in the house can
drain down to it.{{/if}}

## 2. The rule, and why it was set

- One widely sold indoor-rated propane heater's manual says, in a DANGER box, **never bring a
  refillable propane cylinder indoors**, and allows a cylinder up to 20 lb **only when the
  cylinder is located outdoors** (Enerco/Mr. Heater, propane heater owner's manual).
- NFPA 58, the national propane code, limits cylinders kept inside a home, attached garage
  included, to the 1-lb class (NFPA 58, storage of cylinders within residential buildings).
- The Propane Education & Research Council says store cylinders outdoors, upright, valve
  closed (PERC, Safety Guide for Portable Propane Cylinders).

**Why:** quantity, sinking gas and heat. A 20-lb cylinder holds about twenty times the propane
of a 1-lb cylinder, so a leak indoors is not a whiff; it can be enough to fill a room to the
point where it burns. Because propane sinks, the leak collects at floor level, below your nose,
and flows toward low rooms, stairwells and basements, where furnaces and water heaters often
have a pilot flame or igniter. And a cold cylinder brought into a warm house builds pressure;
its relief valve is designed to vent gas when that happens (PERC).

## 3. How it actually hurts people

A connection is not quite tight, a hose is cracked, or a valve seal is worn. Gas leaks slowly
overnight and spreads along the floor. Nobody smells it at standing height. Someone lights the
heater in the morning, or a water-heater pilot across the room catches the edge of the cloud.
The gas burns all at once: a flash fire or an explosion that injures everyone in the room and
can bring down walls. A second risk is the heater itself: running a heater in the same room as
its own fuel supply puts the flame and the leak side by side. The CO risks of the heater
(→ 30-02) come on top.

{{figure fig-propane-pools-low}}

## 4. What makes it safer

**Removes the risk**
- **The cylinder stays outdoors**, upright, valve closed until needed (PERC). Inside, use only
  heaters and 1-lb cylinders the heater maker allows indoors, or heat by other means
  (→ 08-04).

**Reduces it a lot**
- **Cylinder outdoors, the heater maker's own hose through a cracked window or door**, with
  the gap packed with a towel. The hose route is the maker's design; inspect the hose every
  use. The cracked window does not replace the heater's required ventilation (→ 08-09).

**Reduces it a little** (only if the cylinder must come in)
- An **above-ground room only**, never a basement or any room below ground level, so a leak
  can drain out a door at floor level.
- **Valve closed every time the heater is off.** Not turned low: closed.
- **Soapy-water leak test** at the valve and both hose ends before opening and again after
  lighting. Bubbles mean stop.
- **No pilot-light appliances** in or open to the room: doors to the furnace and water-heater
  area closed.
- The cylinder as far from the heater as the hose allows, never in front of it, never near
  any other heat.
- **An adult awake in the room** the whole time; no overnight burn with the tank inside.
- **Tank back outside the moment the hose route works again.**

## 5. The options

**`never`: Never indoors.**
You give up: heat from the big cylinder on a night when the window route fails. You accept:
falling back on other heat sources or cold-night methods (→ 08-04, → 08-01).

**`last-resort`: Last resort, cylinder outside, hose through a window.**
You give up: nothing the maker forbids; you need a heater rated for a remote cylinder and the
maker's hose, and a window or door you can crack. You accept: a small leak risk at the hose
inside the room, and a draft.

**`indoors-with-rules`: Indoors with rules.**
You give up: the maker's and the code's rule. You accept: a house-filling quantity of a
heavier-than-air fuel gas in the living space, controlled only by the rules above and an adult
who stays awake.

## 6. Our choice

{{card DC-02}}

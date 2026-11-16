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
  - cdc-carbon-monoxide-poisoning-basics-772153
  - minnesota-sfm-lp-gas-inside-buildings-r3
  - ysn-flame-king-manufacturer-training-program-1a-fill-a69318
related: [08-09-portable-propane-heaters, 08-04-emergency-heat-options, 08-01-heating-one-room, 06-06-fuel-storage-safety, 06-05-alternative-fuels, 29-01-ex01-fuels, 29-03-ex03-carbon-monoxide, 30-02-dc01-unvented-heater-overnight, 30-01-the-floors]
cards: [DC-02, DC-01]
explainers: [EX-01, EX-03]
promote_when: [has.propane_heater]
card: DC-02
figures: [fig-propane-pools-low]
options:
  - id: never
    label: "Never: no large cylinder indoors, no hose through a window"
    summary: "No cylinder larger than 1 lb comes indoors, and none feeds an indoor heater by a hose through a window or door either. Indoor propane heat, if any, runs only on 1-lb cylinders as the heater maker allows; otherwise other heat sources and the cold-night methods."
  - id: last-resort
    label: "Last resort: cylinder stays outside, hose through a window"
    summary: "Only when no other heat is possible: the cylinder stays outdoors, upright, and feeds a heater built for a remote cylinder through the maker's hose and fuel filter, passed through a cracked window or door. The cylinder itself never comes inside."
  - id: indoors-with-rules
    label: "Indoors with rules"
    summary: "The cylinder itself comes indoors, only when the outdoor-hose route is impossible: an above-ground room, never a basement; valve closed whenever the heater is off; no pilot-light appliances nearby; leak test; CO alarm; adult awake; tank out as soon as possible."
settings_summary: "A 20-lb propane cylinder (the grill size) holds about twenty times the gas of a 1-lb camping cylinder. Heater makers and the national propane code keep anything over the 1-lb size out of the house. The reason: propane is heavier than air. A leak at the valve, hose or regulator flows along the floor, collects in low places such as basements, and explodes when it reaches a flame such as a pilot light or the heater itself. A cylinder warmed indoors can also vent gas through its safety valve on purpose. What helps most: tank outdoors and not connected indoors (removes the risk); tank outdoors with the maker's hose through a window (reduces it a lot); if it must come in, above-ground room, valve closed when off, leak test, no pilot flames nearby, adult awake (reduces it a little)."
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
Bigger tanks hold more. Propane gas is about **1½ times heavier than air** and settles in low
areas (YSN/Flame King, Training Program 1A): it sinks and spreads along the floor like invisible
water. A rotten-egg smell is added so you can smell a leak, but only if your nose is near where
it pools.

Some indoor-rated propane heaters can run from a large cylinder through a hose. The heater
maker allows that only with **the cylinder outdoors**, its own hose and fuel filter, and it
describes the setup for recreational enclosures rather than for heating a home (Enerco/Mr.
Heater; → 08-09).

{{#if has.basement}}Your home has a basement. Propane that leaks anywhere in the house can
drain down to it.{{/if}}

## 2. The rule, and why it was set

- One widely sold indoor-rated propane heater's manual says, in a DANGER box, **never bring a
  refillable propane cylinder indoors**. It allows a remote cylinder of up to 20 lb, on the
  maker's hose and fuel filter, **only when the cylinder is located outdoors**, and it describes
  that setup for recreational enclosures; its line for emergency heating in a home names the
  1-lb disposable cylinder (Enerco/Mr. Heater, propane heater owner's manual).
- NFPA 58, the national propane code, limits cylinders used or stored inside a home, attached
  and detached garages included, to the 1-lb size, with no more than 2 lb in all per dwelling
  (Minnesota State Fire Marshal, LP Gas Inside Buildings, summarising NFPA 58).
- A maker of 1-lb refillable cylinders teaches the same line: up to two 1-lb cylinders may be
  stored in a home; any more must be outdoors, never above 125 °F or near a flame or other
  ignition source (YSN/Flame King, Training Program 1A).

**Why:** quantity, sinking gas and heat. A 20-lb cylinder holds about twenty times the propane
of a 1-lb cylinder, so a leak indoors is not a whiff; it can be enough to fill a room to the
point where it burns. Because propane sinks, the leak collects at floor level, below your nose,
and flows toward low rooms, stairwells and basements, where furnaces and water heaters often
have a pilot flame or igniter. And a cold cylinder brought into a warm house builds pressure;
its relief valve is designed to open and release gas when the pressure gets too high (YSN/Flame
King, Training Program 1A).

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
- **The cylinder stays outdoors**, upright, valve closed until needed. Inside, use only
  heaters and 1-lb cylinders the heater maker allows indoors, or heat by other means
  (→ 08-04).

**Reduces it a lot**
- **Cylinder outdoors, the heater maker's own hose and fuel filter through a cracked window or
  door**, with the gap packed with a towel. The cylinder never comes in; inspect the hose every
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

**`never`: Never: no large cylinder indoors, no hose through a window.**
No cylinder larger than 1 lb comes into the house, and none feeds an indoor heater by hose.
You give up: heat from the big cylinder altogether; indoor propane heat runs only on 1-lb
cylinders, as the heater maker allows. You accept: falling back on other heat sources or
cold-night methods when the 1-lb cylinders run out (→ 08-04, → 08-01).

**`last-resort`: Last resort, cylinder stays outside, hose through a window.**
Only when no other heat is possible. The cylinder stays outdoors; the hose comes in. You give
up: the manual's home-heating line, which names only the 1-lb cylinder (it describes the
remote-cylinder setup for recreational enclosures); you need a heater built for a remote
cylinder, the maker's hose and fuel filter, and a window or door you can crack. You accept: a
leak risk at the hose and its fittings inside the room, and a draft. The cylinder never comes
in.

**`indoors-with-rules`: Indoors with rules.**
The cylinder itself comes into the house, with every rule in the "reduces it a little" list.
You give up: the maker's and the code's rule. You accept: a house-filling quantity of a
heavier-than-air fuel gas in the living space, controlled only by the rules above and an adult
who stays awake.

## 6. Our choice

{{card DC-02}}

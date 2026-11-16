---
id: 17-06-tornado-shelter
section: 17-weather-and-regional-hazards
title: "Preparing a storm shelter spot"
version: 2
revised: 2026-11-16
layer: region
danger_level: critical
phase: [A, B, C]
tags: [tornado, shelter, safe room, basement, interior room, drill, children, medicines, pets, mobile home, apartment]
derived_from: [17-06-tornado-shelter]
sources:
  - noaa-national-weather-service-tornado-safety-ba75e0
  - noaa-national-weather-service-tornadoes-during-the-e-a1a3ad
  - noaa-storm-prediction-center-tornado-safety-faq-vehi-aba867
  - noaa-national-weather-service-noaa-weather-radio-all-5f13d8
  - fema-p-320-taking-shelter
related: [17-02-tornadoes, 17-13-hurricanes-and-tropical-storms, 17-18-hail-and-damaging-wind, 15-01-weather-alerts, 15-07-signals-and-codes, 12-08-medical-kit-tiers, 12-02-bleeding-and-wounds, 13-01-human-waste-no-plumbing, 00-07-household-roles, 20-04-teaching-kids-the-plan, 20-08-kids-and-fear, 20-09-pets, 22-03-go-bags-and-kits, 19-01-document-grab-kit, 24-02-drills, 25-09-family-medical-summary, 25-10-annual-review, 27-05-fallout-sheltering, 04-09-winter-cold-storage, 01-05-choosing-a-destination, 29-05-ex05-chlorine-products, 29-07-ex07-refrigerated-medicines, 30-01-the-floors]
cards: []
explainers: [EX-05, EX-07]
promote_when: [is.tornado_region, is.hurricane_region]
photo_slots:
  - { id: shelter-spot, caption: "Our shelter spot, stocked: helmets, shoes, lights, radio, kit, water" }
  - { id: shelter-overhead, caption: "What is on the floor above our shelter spot" }
figures: [fig-tornado-shelter-choices]
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: { date: "2026-11-16", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "Debris claim to SPC; fallout-room heater sentence aligned with DC-01 instead of a stated rule." }
---

# Preparing a storm shelter spot

**What this page is for.** In a tornado warning you will have minutes, and someone may be carrying
a child. This page turns "we would go to the basement" into a chosen, stocked and practiced spot
that works in the dark with nothing in your hands. For most homes it is an afternoon's work, not a
building project, and it is one of the best uses of an afternoon in this binder. What to do in a
warning is on → 17-02.

> **SAFETY.** The spot is: **lowest floor, most interior, as many walls between you and the
> outside as possible, away from windows, heads and necks covered** (NWS, Tornado Safety). **A
> mobile home, a vehicle, a garage or a shed is not a shelter.**

## Do this now

1. **Pick the spot** using the ranking below, and write it here: **{{ dwelling.shelter_room }}**.
   Pick a second spot in case the first is blocked or smells of gas: ______________.
2. **Clear it and keep it clear.** Shelves fixed to the wall, nothing heavy that can fall, stock
   on shelves off the floor.
3. **Stock it with the list below, permanently**, so you can arrive empty-handed.
4. **Shoes and helmets for everyone go in the spot.**
5. **Practice twice, once by day and once at night, timed** (→ 24-02). Fix what goes wrong.

{{photo shelter-spot}}

## Choosing the spot

Ranked, from the NWS and SPC guidance:

1. **An engineered safe room or storm shelter** built to FEMA's safe room criteria (FEMA P-320,
   Taking Shelter from the Storm). This is the best protection. It is a real construction project,
   and it is worth pricing.
2. **A basement**, in a corner away from windows, **under a sturdy workbench or the stairs**, and
   **not under heavy appliances on the floor above**. In a walkout basement, "away from windows"
   means away from the whole at-ground wall: stay on the buried side.
3. **No basement: the most interior room on the lowest floor.** A small bathroom, closet or
   hallway with no outside walls. **A bathtub with a mattress pulled over it** is the classic
   version.
4. **Never:** a room with windows, a large open room, a garage, a mobile home, or a vehicle.

{{figure fig-tornado-shelter-choices}}

**For your home:**
{{#if has.basement}}- You have a basement ({{ dwelling.basement }}). Walk it with this page.{{/if}}
{{#if has.shelter_room}}- Your named windowless room is **{{ dwelling.shelter_room }}**.{{/if}}
{{#if has.apartment}}- **Apartment:** find the lowest interior space you can reach in a minute or
  two: an interior hallway, stairwell or ground-floor interior room. Ask the building manager
  whether there is a designated shelter area. Do not use elevators.{{/if}}
{{#if has.mobile_home}}- **Mobile or manufactured home: there is no safe spot inside.** Your
  shelter is a sturdy building nearby: a neighbour's basement, a community shelter, a public
  building. Write it here: ______________, and how long it takes to reach: ______ minutes. **You
  go when the watch is issued or the sky turns bad**, because the warning does not leave enough
  time (NWS; SPC).{{/if}}

**Then look up and around.** What is on the floor directly above? (A refrigerator, a piano, a full
bathtub?) What on the shelves could fall on you? Clear it and fix the shelving.

{{photo shelter-overhead}}

**Things that often share a basement corner, and what to do about them:**
- **A gas furnace or water heater:** if you smell gas, you go to the second spot. Make that part of
  the drill.
- **A sump pit:** power out means pump out and possible flooding (→ 17-03). Stock goes on shelves.
{{#if has.pool}}- **Pool chemicals:** pool shock (calcium hypochlorite) gives off chlorine gas when
  wet or heated. Keep it sealed in a lidded container on a shelf, away from the furnace and the
  sump, and never next to acids or other cleaners. **Bleach or pool shock is never mixed with
  ammonia, acids or other cleaners** (→ 29-05, → 30-01).{{/if}}

## What lives in the spot, permanently

The goal: **you can go down with nothing in your hands and still be equipped.**

| What | Items |
|---|---|
| **Heads** | **A helmet for everyone** (bike helmets are fine). SPC: flying debris is the greatest danger in tornadoes |
| **Feet** | **Shoes for everyone**, children included: the aftermath is glass and nails (→ 12-02) |
| **Light** | Two or three headlamps or flashlights, spare batteries, a lantern, a chemical light stick (no battery to go flat) |
| **Warning** | **A second battery or crank NOAA Weather Radio** (→ 15-01) |
| **Medical** | First-aid and trauma kit (→ 12-08); a small kit of everyday medicines |
| **Water and food** | Several gallons of water, some shelf-stable food{{#if has.food_allergy}}, safe for every food allergy in the household{{/if}} |
| **Signalling** | **A whistle for everyone** (→ 15-07), to be heard from under debris |
| **Cover** | Mattress, heavy blankets or cushions |
| **Children** | A comfort item, a small toy or book, a blanket (→ 20-08) |
| **Papers** | Copy of the family plan and medical cards (→ 25-09) |
| **Tools** | Work gloves and a pry bar, in case the way out is blocked |
| **Sanitation** | A bucket with a lid and bags (→ 13-01) |

**Rotate water, food and batteries twice a year**, with the household inventory (→ 25-10).

## Medicines: decide the grab in advance

Some medicines should not live in the shelter because the spot gets too cold or too warm for the
label's storage range, or because they are in daily use. Read each label (→ 29-07).
{{#each meds as x}}- **{{x.name}}** ({{x.member}}): lives in the shelter / grabbed on the way
  (circle one). Grabbed by: __________.
{{else}}- No medicines are entered in your profile. If anyone takes a daily or rescue medicine,
  decide here whether it lives in the spot or is grabbed on the way.
{{/each}}
- **Rescue medicines** (epinephrine, inhalers) go with the person who needs them. A spare stored in
  the shelter only if a min/max thermometer shows the spot stays inside the label's range all year
  (→ 02-03).
- **Phones and powered medical devices** go too; a charged power bank lives in the spot.
- **Practice the grab** as part of the drill so it is automatic.

## Children, elders and pets

- **Assign roles now** (→ 00-07): who carries the smallest child, who takes an older child's hand,
  who helps an elder or anyone who uses a wheelchair or walker, who grabs the medicines. Do not
  negotiate it during a warning.
  {{#each members as m}}
  - {{m.label}}: goes with / helps __________.{{/each}}
- **Children who have practiced will go; children who have not may freeze or hide** (→ 20-04).
- **Shoes on during the watch.** This is the single biggest time-saver.
- **Make the spot less frightening:** a lantern a child is allowed to hold, a familiar blanket, a
  routine (→ 20-08).
{{#if has.mobility_aid}}- **Someone uses a wheelchair or walker.** If the spot is down stairs, decide
  how they get there and time it; if that is too slow, choose a ground-floor interior room instead
  and make it as strong a spot as you can.{{/if}}
{{#if has.pets}}- **Pets:** carriers live in or beside the spot with the doors open. Decide out loud,
  before any warning, whether anyone looks for a pet once the warning sounds. During a watch, shut
  pets into the shelter side of the house (→ 20-09).{{/if}}

## The drill

1. Announce a drill at a random time.
2. Everyone goes, carrying what they would carry.
3. Time it.
4. Ask: what went wrong? Shoes upstairs? Medicine not where you thought? A scared child? A dead
   light? Fix it.
5. Repeat once at night.
6. Re-drill every spring, and as children grow (→ 25-10).

## If you come up and the house is gone

That is why the spot holds water, food, medicine, papers, shoes and a pry bar.
- **Signal from under debris** with whistles (→ 15-07).
- **The way out may be blocked**: gloves and a pry bar.
- **The house may be unlivable.** Go-bags (→ 22-03) and the document kit (→ 19-01) should be
  reachable, but the spot's own stock is the fallback. In a long emergency, losing the house is a
  reason to move (→ 01-02).

## A tornado spot is not a fallout room

The spot is chosen for minutes. Sheltering for a day or two from fallout (→ 27-05) needs space,
heat, air and sanitation, and any fuel-burning heater there needs its fresh-air openings kept open
(→ 08-01; a heater running while people sleep is card DC-01, → 30-02). Choose the fallout room
separately on → 27-05; the tornado stock can be its supply.

## Gear

| Item | Why | Notes |
|---|---|---|
| **Helmets for everyone** | Debris head injury | Bike helmets are fine |
| **Shoes for everyone, kept in the spot** | Glass and nails afterward | Check children's sizes each spring |
| Second NOAA Weather Radio | You will be down there with no power | → 15-01 |
| Lights, lantern, spare batteries, light sticks | Power will be out | → 10-01 |
| First-aid and trauma kit | Cuts are the common injury | → 12-08 |
| Water and shelf-stable food | You may be there a while | Rotate |
| Whistles | Signal from under debris | → 15-07 |
| Mattress, blankets, cushions | Debris cover | |
| Gloves and pry bar | Blocked exit | |
| Bucket with lid and bags | Long stays | → 13-01 |
| Rotation date on the wall | Water, food, batteries | → 25-10 |

**If you do not have it:** any helmet, a hard hat, or a cushion held over head and neck; a sturdy
workbench, mattress or bathtub for cover; banging on a pipe to signal. **What you cannot
improvise is the practice, and the decision about who carries whom.**

## When it runs out

- **Nothing here runs out fast, but everything quietly expires:** batteries go flat, water gets
  old, food and medicines pass their dates. Put it on the annual review (→ 25-10).
- **The plan's fit changes** as children grow. Re-drill and re-assign roles every year.
- **If the house is destroyed, the spot's stock is what you have.** Keep more there than feels
  necessary. If you can only do one, do the shelter: it is where you will be.

## Phase notes

- **A (at home):** spot stocked and practiced, second spot agreed out loud, weather radio where you
  sleep and another in the spot.
- **B (moving):** there is no shelter on the move; the answer is not being out in severe weather
  (→ 17-02, → 17-11). At any house you stay in, **pick the best interior room in the first hour**:
  small, no outside walls, lowest floor, no windows. Do not assume last visit's answer is still
  right.
- **C (rural or new site):** a basement, cellar or safe room is a main test of a site (→ 01-05). A
  storm cellar also works as a root cellar (→ 04-09).

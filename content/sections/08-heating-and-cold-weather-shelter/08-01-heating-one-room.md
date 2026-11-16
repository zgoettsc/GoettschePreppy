---
id: 08-01-heating-one-room
section: 08-heating-and-cold-weather-shelter
title: "Heating one room instead of the house"
version: 2
revised: 2026-11-16
layer: core
danger_level: critical
phase: [A, C]
tags: [heating, warm room, winter, fuel, ventilation, carbon monoxide, kerosene, propane, strategy]
derived_from: [08-01-heating-one-room]
sources:
  - cdc-winter-weather-before-during-and-after-13bbd5
  - cdc-carbon-monoxide-poisoning-basics-772153
  - noaa-national-weather-service-during-extremely-cold-9c1973
  - american-academy-of-pediatrics-healthychildren-org-h-7bd7d0
  - american-red-cross-preventing-and-thawing-frozen-pip-003044
  - cdc-preventing-hypothermia-c53e0c
  - enerco-group-mr-heater-manufacturer-portable-buddy-r-759ce5
  - ghp-group-inc-dyna-glo-manufacturer-portable-kerosen-477cfd
  - minnesota-sfm-lp-gas-inside-buildings-r3
  - cpsc-carbon-monoxide-questions-and-answers-783766
related:
  - 08-02-carbon-monoxide-safety
  - 08-03-winterizing-the-home
  - 08-04-emergency-heat-options
  - 08-05-hypothermia-frostbite
  - 08-06-improvised-shelter-warmth
  - 08-07-ducted-heater-operation
  - 08-08-wood-heat-operation
  - 08-09-portable-propane-heaters
  - 08-10-wick-kerosene-heaters
  - 03-06-winter-water
  - 01-02-go-no-go-decision
  - 11-01-cold-weather-layering
  - 11-02-keeping-kids-warm
  - 09-16-outage-day-one
  - 21-02-long-haul-morale
  - 29-03-ex03-carbon-monoxide
  - 30-01-the-floors
  - 30-02-dc01-unvented-heater-overnight
  - 30-03-dc02-propane-cylinder-indoors
  - 30-10-dc09-infant-bed-sharing
  - 30-20-dc19-when-to-leave
  - 04-09-winter-cold-storage
  - 06-04-wood-supply-and-depletion
  - 10-06-winter-light-budget
  - 23-02-master-consumables-table
  - 29-07-ex07-refrigerated-medicines
  - 29-12-ex12-extinguishers-blankets-and-alarms
cards: [DC-01, DC-02, DC-09, DC-19]
explainers: [EX-01, EX-03, EX-12]
promote_when: [is.cold_winters]
photo_slots:
  - { id: warm-room, caption: "Our warm room set up: heater spot and barrier, the vent openings, door blankets, sleeping area, thermometer" }
  - { id: warm-room-co-alarm, caption: "The CO alarm in the warm room: opposite wall from the heater, at pillow height" }
figures: [fig-warm-room-layout]
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: { date: "2026-11-16", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "Buddy 9 sq in, Dyna-Glo 200 cu ft/1,000 BTU/h and 1 in, AAP and CDC re-read; CPSC never-unvented-while-sleeping added; NFPA 58 line traced via MN SFM; wick CO wording matched to manual." }
---

# Heating one room instead of the house

**What this page is for.** When the power or the fuel supply fails in winter, the most useful
single decision is to **stop heating the whole house and heat one room**. Everyone lives and
sleeps in that room. This page shows how to choose that room in your own home, how to close it
off, what the heater in it needs, and when it is time to stop holding the house. Carbon monoxide
(CO), the poison gas every flame makes, is explained on → 29-03; read → 08-02 before you bring
any heat source into the room.

> **SAFETY.** **Never run a generator, charcoal, or any engine indoors, in a garage, or near an
> open window.** Carbon monoxide kills in minutes with no warning; alarms fail; there is no
> mitigation that works every time (→ 30-01). A heater sold for indoor use is different: it may
> be used inside, but only by its manual, with a working battery CO alarm in the room first,
> the manual's air openings open, and an adult in the room while it burns. Whether one may
> burn while people sleep is a decision card, not a default: {{choice DC-01}} (→ 30-02).
> **CDC says people who are asleep can die from CO before they have any symptoms** (CDC,
> Carbon Monoxide Poisoning: Basics).

## Do this now

1. **Pick the warm room today, in writing** (box below). Small, few outside walls, enough floor
   for everyone to sleep, and able to meet your heater's air rules.
2. **Put a battery CO alarm and a smoke alarm in it** before any heater is lit: CO alarm on the
   wall opposite the heater, at the height of sleeping heads (→ 08-02).
3. **Close off the rest of the house.** Shut doors. Hang blankets over doorways and stairwells.
4. **Everyone sleeps in the warm room**, children and pets included. Body heat counts.
5. **Move cold-sensitive medicines there** (→ 29-07). Insulin must never freeze (→ 30-01).
6. **Fill every water container, then drain the plumbing** in the parts of the house that will
   freeze (→ 03-06).
7. **Tape the action ladder (below) inside the door,** next to a thermometer.

## Why it works

Heating a whole house with a wood fire or a portable heater is close to impossible. A house is
built to be heated by its furnace, and anything smaller loses the race against the walls and
windows. One room is a small fraction of the house's volume, so the same fuel lasts many times
longer. That is the difference between a woodpile or a fuel can lasting days and lasting weeks.

**Even better than heating a room is heating the people in it.** Layers (→ 11-01), sleeping
bags, shared body heat and a small shelter inside the room (→ 08-06) keep a family safe at room
temperatures that would otherwise be miserable. The room just has to be warm enough for that to
work.

## Choosing the room in your home

| What to look for | Prefer |
|---|---|
| Size | The smallest room that fits everyone sleeping |
| Outside walls | Fewest; an inside room loses heat slowest |
| Windows | Few, but a south-facing one gives free heat on sunny days |
| A real chimney | A room with a working, inspected fireplace or wood stove wins by default (→ 08-08) |
| Water and kitchen | Close is a plus for cooking and washing |
| Your heater's air | It can give the openings your heater's manual requires (table below) |
| Clearances | Floor space for the heater's clearances plus a barrier children cannot get past |

**Your home on file:** a {{ dwelling.type }}, basement: {{ dwelling.basement }}, main heat:
{{ dwelling.primary_heat }}.

{{#if has.apartment}}**In an apartment.** Your neighbours' walls, floor and ceiling are often
warmer than the outside air, so a room in the middle of the unit, away from the outside wall,
holds heat well. You cannot close off a stairwell, but you can close your own doors and hang
blankets. Building smoke and CO travel between units: keep your CO alarm working even if you
burn nothing yourself.

> **Before the collapse:** the national propane code (NFPA 58) does not allow propane cylinders
> larger than the 1-lb camping size to be stored or used inside a home (Minnesota State Fire
> Marshal, LP Gas Inside Buildings), and many leases forbid fuel heaters. Read yours.

{{/if}}{{#if has.mobile_home}}**In a mobile or manufactured home.** The rooms are small and the
walls are thin, so the whole home cools fast once heat stops. Choose the room with the fewest
outside walls and windows. Before using any fuel-burning heater, read its manual for a
mobile-home or RV warning: some unvented heaters may not be used in one at all. A small room
also reaches a heater's ventilation limit sooner (see the volume method below).

{{/if}}{{#if has.basement}}**Your basement.** Walls set in the ground lose heat slowly, because
the soil around them stays far warmer than winter air. That makes a basement room a strong warm
room for **non-burning** heat: bodies, blankets, a heated blanket on a battery, or a vented
furnace. For a **fuel-burning heater** it is a weak choice unless it has an outside door or
window at ground level: the heater needs that window for its air, and **propane is heavier than
air**, so a leak flows down into a basement and pools there until it reaches a flame
(Enerco/Mr. Heater, Buddy owner's manual). {{#if has.walkout}}Your basement is a **walkout**: a
room on the walkout side, with its door or window at ground level, can serve both purposes. With
a propane heater, a door cracked at the floor on that side is also a low air opening, and any
room holding a gas water heater or furnace pilot stays shut off from it.{{else}}Your basement is
not a walkout, so use it for a fuel-burning heater only if a room there has a window that opens
to the outside, and never with propane.{{/if}}

{{/if}}{{#if has.shelter_room}}**Your windowless room ({{ dwelling.shelter_room }}).** A room
with no windows is excellent at holding body heat and is a fine warm room if your heat comes
from bodies, bedding or electricity. It is the **wrong** room for any fuel-burning heater:
every portable heater needs fresh-air openings to the outside, and a propane heater on a hose
needs a window or door the hose can pass through.

{{/if}}**The trade-off to settle on paper.** "Inside room, few outside walls" pulls toward a room
without windows. Every fuel-burning portable heater needs a window. **If your heat will come from
a flame, a room with one window or outside door you can open beats an inside room**, and you
insulate the rest of that room's glass (→ 08-03). If your heat will come only from bodies,
bedding and battery power, the inside room wins.

### The heater's air: what the manuals require

| Heater class | What the manual requires | Page |
|---|---|---|
| Portable propane heater (Buddy family) | Fresh-air openings of 9 square inches (a 3 × 3 in opening) at ceiling level **and** at floor level; no other fuel-burning appliance in the space; the 20-lb tank outdoors, fed by the maker's hose | → 08-09 |
| Wick kerosene heater | If the room has less than 200 cubic feet of air per 1,000 BTU/h of heater, open a window at least 1 inch or keep doors to other rooms open; never a bathroom or small closed room | → 08-10 |
| Ducted diesel or kerosene heater | Combustion intake and exhaust both outside, sealed | → 08-07 |
| Fireplace or wood stove | A sound, inspected chimney | → 08-08 |

Sources: Enerco/Mr. Heater, Portable Buddy owner's manual; GHP Group/Dyna-Glo, Portable
Kerosene Heater owner's manual. **Your own heater's manual governs;** these are the figures from
one common model of each class.

**The volume method (wick kerosene heaters).** Measure the room: length × width × ceiling height
in feet = cubic feet. Divide the heater's BTU/h rating by 1,000 and multiply by 200: that is the
room volume the manual wants. Example: a 10,500 BTU/h heater wants 2,100 cubic feet, about a
13 × 20 ft room with an 8 ft ceiling. A smaller room means the window stays cracked at least an
inch whenever it burns. A warm room is usually smaller than this, so plan on the window being
open.

**A towel stuffed around a hose gap is a draught seal, not ventilation.** The openings the manual
asks for are still required.

{{figure fig-warm-room-layout}}

### Commit the warm room (fill in now, in ink)

> **OUR WARM ROOM IS:** ______________________
> **Room size L × W × H = ________ cu ft** (needed for the kerosene volume rule)
> **Window or outside door that opens for air:** ______________________
> **High and low openings for a propane heater will be:** ______________________
> **Where the heater stands, and the barrier around it:** ______________________
> **CO alarm goes:** ______________________ (opposite wall from the heater, pillow height)
> **Backup room if this one is damaged:** ______________________
> **Decided on:** ____________ **by:** ______________________

Once written, stage the blankets, hooks, sleeping bags, thermometer, alarm and window film in
that room now, not during the outage.

{{photo warm-room}}

{{photo warm-room-co-alarm}}

## The indoor-temperature action ladder

Tape a copy inside the warm-room door, beside the thermometer. Each rung is a decision made in
advance so nobody argues about it at 2 a.m. The temperatures are your household's to set; write
them in. The actions are what each rung should trigger.

| Warm-room reading | Action, starting now |
|---|---|
| **___ °F and falling** | **Consolidate.** Everyone moves into the warm room. Close off the rest of the house; door blankets up. Install and test the CO alarm now so a heater is ready |
| **___ °F** | **Protect the plumbing:** drip vulnerable taps, open cabinet doors under sinks, fill every container, and drain the rest of the house if the cold will keep falling (Red Cross; → 03-06). **Everyone sleeps in the warm room.** Light **one** heater if you have one, by its manual |
| **___ °F** | **Watch the people:** touch checks on children and elders (back of the neck, chest; → 08-05, → 11-02). Move medicines to the warmest spot in the room. Count fuel-hours left (→ 23-02). Start thinking about whether to leave (→ 01-02) |
| **___ °F and falling, no heat source recovering** | **The house can no longer be kept safe.** Make the go/no-go decision now, in daylight if at all possible (→ 01-02). When to leave is your household's own worksheet: {{choice DC-19}} (→ 30-20) |

**Run one fuel heater at a time.** The propane class's manual forbids other fuel-burning
appliances in the space, and two unvented burners add their CO and their oxygen use together.

## Heat while people sleep

Both common portable heater manuals say never run them while sleeping, and CPSC says never to
operate unvented fuel-burning appliances in any room where people are sleeping (CPSC, Carbon
Monoxide Questions and Answers). Running one overnight
keeps the room warm but leaves CO and fire with no one awake to notice them; turning it off
means a cold night, which is hardest on babies and frail elders. That trade-off is the
household's to decide, on the card, with its mitigations listed there (lowest correct setting,
alarm at pillow height, the manual's openings, a barrier, an adult who wakes to check):
{{choice DC-01}} (→ 30-02). Whatever the choice, the heater pages (→ 08-09, → 08-10) explain
what "lowest setting" means for each class, because on a wick heater a turned-down wick makes
smell and CO, not savings (GHP Group/Dyna-Glo, Portable Kerosene Heater owner's manual).

## Small children in the warm room

The American Academy of Pediatrics publishes **no numeric minimum room temperature** for babies.
Its guidance is to dress the baby for the room, keep loose bedding out of a baby's sleep space,
and avoid overheating (AAP, How to Keep Your Sleeping Baby Safe). CDC lists **babies sleeping in
cold bedrooms** among the people most at risk of hypothermia (CDC, Preventing Hypothermia). So in
a cold house the baby sleeps in the warm room, dressed in layers and a sleep sack, and is checked
by touch.

{{#if has.infant}}Your household has a child under 2: {{#each infants as c}}{{c.label}}
({{c.age_text}}); {{/each}}Whether a small child shares an adult bed for warmth is a decision
card, with the AAP rule for babies under 1 printed on it: {{choice DC-09}} (→ 30-10).{{else}}If a
baby or toddler joins the household, whether a small child shares an adult bed for warmth is a
decision card: {{choice DC-09}} (→ 30-10).{{/if}}

**Hot-water bottles and fire-warmed stones pre-warm a bed and come out before a child gets in.**
Skin that is asleep or numb burns without waking. **No electric blanket on or around a baby or
toddler** (→ 08-04, → 11-02).

## Sealing the room, and its limits

- **Blankets over doorways** and at the top or bottom of stairs. A stairwell is a chimney.
- **Towels and draught stoppers** at door gaps; window film, plastic sheeting or bubble wrap on
  the glass (→ 08-03).
- **Curtains closed at night**, south-facing ones open on sunny days.
- **Cover the floor** with rugs, blankets or cardboard. Cold comes up through it.
- **Do not make it airtight.** Draught-proofing is not the same as sealing. With a heater
  burning, the openings its manual requires stay open the whole time.

## The rest of the house

- **Let it go cold, on purpose.** Drain the plumbing (→ 03-06) or you trade a heating problem for
  a flood.
- **Cold rooms become food storage** (→ 04-09), but insulin and other medicines that must not
  freeze stay in the warm room (→ 29-07).
- **Walk the house twice a day:** burst pipes, snow load, and any smoke or CO drifting into
  unused rooms.

## Living in one room

Several people{{#if has.pets}} and their pets{{/if}} in one room for weeks is hard. Plan it as a
people problem, not only a heat problem: a sleeping spot for each person, a play corner if there
are children, a daily routine, and some way for each adult to get an hour of quiet (→ 21-02).
Morale in a one-room winter is part of survival.

## Gear

| Item | Why | Notes |
|---|---|---|
| **Battery CO alarm** for the warm room (you have {{ gear.co_alarms }}) | The only thing that detects CO | Plug-in alarms without a battery fail in an outage (→ 08-02) |
| Smoke alarm and an extinguisher in the room | Fire is the other way heaters kill | → 29-12 |
| Heavy or moving blankets, hooks or nails | Close off doorways and stairs | Cheap; large effect |
| Window film, bubble wrap or plastic sheeting | Cuts the biggest heat loss | → 08-03 |
| Cold-rated sleeping bags, child sizes too | Heat the people, not the room | |
| Foam pads, rugs, cardboard | Insulate from the floor | Sleeping on a cold floor is dangerous |
| Two thermometers: the room and where the baby sleeps | Know the real temperature | |
| A heater sold for indoor use, its manual and fuel | Supplemental heat | → 08-04 for the options |
| Headlamps and battery lanterns | The room is dark early | → 10-06 |

**No gear?** Curtains, comforters, tarps and cardboard make door covers and window insulation.
Furniture pushed against outside walls adds a still-air layer. A tent pitched inside the room is
the cheapest large gain of all (→ 08-06).

## When it runs out

- This page **is** the fuel strategy: shrinking the heated space is the biggest lever on how long
  fuel lasts (→ 06-04).
- **Ration in steps:** heat one room, then only the sleeping shelter inside it (→ 08-06), then
  only the people: layers, body heat, pre-warmed beds.
- **Spend effort on insulation first.** It is the only "fuel" that never runs out.
- **The last resort** is leaving: if the fuel is gone and the house cannot be kept safe, that is
  the go/no-go decision (→ 01-02), not something to endure with small children or frail elders.

## Phase notes

- **A (at home):** set the room up before you need it.
- **B (moving):** the same idea, smaller: the smallest insulated space you can warm with bodies.
  Never an unvented burner in a closed vehicle or tent (→ 08-02).
- **C (established somewhere else):** the same choice, often with a real stove. Pick the room
  with the chimney, after inspecting it (→ 08-08).

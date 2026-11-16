---
id: 17-02-tornadoes
section: 17-weather-and-regional-hazards
title: "Tornadoes, severe thunderstorms, derechos and lightning"
version: 2
revised: 2026-11-16
layer: region
danger_level: critical
phase: [A, B, C]
tags: [weather, tornado, severe thunderstorm, derecho, lightning, siren, mobile home, vehicle, overpass, hail]
derived_from: [17-02-tornadoes]
sources:
  - noaa-national-weather-service-tornado-safety-ba75e0
  - noaa-national-weather-service-tornadoes-during-the-e-a1a3ad
  - noaa-storm-prediction-center-tornado-safety-faq-vehi-aba867
  - noaa-storm-prediction-center-about-derechos-definiti-f84a2c
  - noaa-national-weather-service-wfo-des-moines-the-aug-3923bf
  - noaa-national-weather-service-lightning-safety-when-455ad7
  - noaa-national-weather-service-noaa-weather-radio-all-5f13d8
  - nws-destructive-thunderstorm-wea-2021
  - nssl-damaging-winds-basics
  - fema-nri-counties
  - nws-lightning-brochure-2018
  - nws-lightning-tips
related: [17-06-tornado-shelter, 17-10-reading-the-sky, 17-11-corridor-hazards, 17-18-hail-and-damaging-wind, 17-08-power-grid-failure, 15-01-weather-alerts, 15-07-signals-and-codes, 12-02-bleeding-and-wounds, 12-08-medical-kit-tiers, 12-18-choking-and-cpr, 16-12-grid-down-house-repairs, 18-01-mutual-aid, 20-04-teaching-kids-the-plan, 20-08-kids-and-fear, 24-02-drills, 29-10-ex10-weather-alert-words, 30-20-dc19-when-to-leave]
cards: [DC-19, DC-28]
explainers: [EX-10, EX-09]
promote_when: [is.tornado_region]
photo_slots:
  - { id: gas-shutoff, caption: "Our gas shutoff valve at the meter, and where the wrench hangs" }
figures: [fig-tornado-shelter-choices, fig-tornado-vehicle-choices]
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: { date: "2026-11-16", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "NRI rating note; 2020 derecho figures corrected to NWS DMX; derecho lead time softened per SPC; lightning to NWS brochure and tips." }
---

# Tornadoes, severe thunderstorms, derechos and lightning

**What this page is for.** A tornado warning gives you minutes, not hours. This page is what to
do in those minutes: what the alert words mean, where to go in each kind of building, what to do
in a vehicle, and what comes after. It also covers the same storms' other killers: straight-line
wind (including derechos) and lightning. Hail is on → 17-18; preparing the shelter spot is on
→ 17-06.
{{#if is.tornado_region}}**Your home county is rated 2 or 3 for tornadoes in the region data:
plan for this every spring and summer.**{{else}}Your home county is rated lower for tornadoes, but
tornadoes have struck every state; keep this page.{{/if}}
Ratings in this binder are FEMA's National Risk Index for your county, on a 1-to-3 scale: they measure expected harm to people and property there, not how likely the hazard is (→ 29-10).

> **SAFETY.** **Tornado warning: go now.** Lowest floor, most interior room, away from windows,
> as many walls between you and the outside as you can, and **protect your head and neck**
> (NWS, Tornado Safety). **A mobile home is not a shelter, even tied down. Leave it for a sturdy
> building before the storm arrives** (NWS; SPC). **Never shelter under a highway overpass.**

## Do this now

1. **Put a NOAA Weather Radio with SAME where you sleep** (→ 15-01, → 29-09). Enough tornadoes
   come after dark that a warning you sleep through is the whole problem.
2. **Pick your shelter spot today** and stock it (→ 17-06). Ours: **{{ dwelling.shelter_room }}**.
3. **Put shoes, a light, a whistle, a first-aid kit and water in the spot.** Decide who grabs the
   medicines and who carries whom on the way (below).
4. **Practice twice:** once by day, once at night, timed (→ 24-02). You will find problems both
   times.
5. **Know where you would shelter** at work, school, the store, and the houses you visit.

## Watch, warning, and the words that matter

| Alert | Meaning | What you do |
|---|---|---|
| **Tornado Watch** | Conditions favour tornadoes over a wide area, for hours | Radio on, plan reviewed, shoes on everyone, know where everyone is |
| **Tornado Warning** | A tornado is seen or shown on radar near you | **Shelter now** |
| **Severe Thunderstorm Warning** | Damaging wind (58 mph or more) or large hail (1 inch or more). Tornadoes can form from these storms with little added warning | Inside, away from windows; treat "destructive" as a tornado warning |

The NWS adds a **damage threat** tag to severe thunderstorm warnings: **"considerable"** means
hail of 1.75 inches or more or wind of 70 mph or more; **"destructive"** means hail of 2.75 inches
or more or wind of 80 mph or more, and only the destructive tag sets off a Wireless Emergency
Alert on phones (NWS, 2021). Wind like that does tornado-class damage with no funnel at all. More
alert words: → 29-10.

**Outdoor sirens** are an outdoor warning system. They are often not heard indoors, they can fail,
and **silence is not an all-clear**: there is no all-clear signal. Many places test sirens on a
fixed schedule. Your local test time: ______________. A siren at any other time is real. **The
weather radio, not the siren, is your primary warning** (NWS, NOAA Weather Radio).

## Where to go: by building

**The rule:** as low as possible, as far inside as possible, as many walls between you and the
outside as possible, and protect your head (NWS, Tornadoes: During the Event).

{{figure fig-tornado-shelter-choices}}

{{#if has.basement}}- **Your home has a basement** ({{ dwelling.basement }}). Go down. Get under a
  sturdy workbench or the stairs, away from windows, and **not under heavy appliances on the floor
  above** (a refrigerator or piano can come through).{{else}}- **No basement:** the most interior
  room on the lowest floor (a bathroom, closet or hallway), away from windows.{{/if}}
{{#if has.shelter_room}}- **Your named shelter room:** {{ dwelling.shelter_room }}.{{/if}}
{{#if has.apartment}}- **In an apartment:** get to the lowest floor you can reach quickly, into an
  interior hallway, stairwell or bathroom away from windows. Do not use the elevator; the power
  may fail. If you live on an upper floor, agree with a neighbour below where you will go.{{/if}}
{{#if has.mobile_home}}- **You live in a mobile or manufactured home. It is not safe in a tornado,
  even if it is tied down. Leave for a sturdy building or a community shelter when the watch is
  issued or the sky turns bad, not when the warning sounds** (NWS; SPC: "Get out!"). Know now
  where you will go and how long it takes to get there: ______________.{{/if}}
- **Cover your head and neck.** Helmets (bicycle helmets work) help: SPC says flying debris is
  the greatest danger in tornadoes.
- **Put a mattress, heavy blankets or couch cushions over you.**
- **Shoes on.** After a tornado the ground is glass, nails and broken wood (→ 12-02).
- **Never:** a room with windows, a big open room (gym, warehouse, big store aisle), a garage, a
  shed, a tent, a mobile home, or a vehicle if a building can be reached.

## Caught in a vehicle or in the open

NWS: **"Being in a vehicle during a tornado is not safe. The best course of action is to drive to
the closest shelter."** A sturdy building always wins. Failing that, in order (SPC, Tornado
Safety FAQ):

1. **If the tornado is far off and roads are open, drive at right angles to its path**, away from
   it, not along its track.
2. **Caught by extreme wind or flying debris:** park quickly, out of traffic lanes. SPC: **"Stay
   in the car with the seat belt on. Put your head down below the windows; cover your head with
   your hands and a blanket, coat, or other cushion if possible."**
3. **The ditch test.** SPC: **"If you can safely get noticeably lower than the level of the
   roadway, leave your car and lie in that area, covering your head with your hands."** It must
   be *noticeably* lower and reachable. A flat shoulder is not a ditch.
   {{#if has.young_child}}With small children buckled into car seats, the realistic choice is
   usually the vehicle, belted, heads below the windows: you cannot unbuckle and carry several
   children through tornado wind.{{/if}}
4. **Never shelter under an overpass.** SPC: overpasses create "deadly traffic hazards while
   offering little protection against flying debris." The wind speeds up in the gap. It feels
   safe; it kills.
5. **In the open with no vehicle:** the lowest spot you can reach, flat on the ground, head
   covered. It is a last resort.

{{figure fig-tornado-vehicle-choices}}

## Children, medicines and pets: solve them before the warning

- **Decide now who carries whom and who grabs what.** Do not negotiate it during a warning.
  {{#each members as m}}
  - {{m.label}} ({{m.age_text}}): goes with __________; grabs __________.{{/each}}
- **Children who have practiced will go; children who have not may freeze or hide** (→ 20-04).
  Practice it as a game. Keep a comfort item and a light a child may hold in the spot (→ 20-08).
- **Shoes on during the watch**, not the warning. It is the single biggest time-saver.
{{#if has.refrigerated_meds}}- **Refrigerated medicine** is grabbed on the way, in a small
  insulated container, not stored in the shelter if the spot gets too cold or too warm for its
  label (→ 29-07).{{/if}}
{{#if has.epinephrine}}- **Epinephrine** goes with the person who needs it. Check the storage
  range on the label before storing a spare in a basement (→ 02-03).{{/if}}
- **Phones, medical cards and the family plan** go too (→ 25-09).
{{#if has.pets}}- **Pets:** keep carriers in or beside the shelter spot, doors open. Decide out loud,
  in advance, whether anyone looks for a pet after the warning sounds, and who. During a watch,
  close pets into the shelter side of the house.{{/if}}

## After the tornado

- **Stay in shelter until the warning ends.** Outbreaks bring more than one tornado.
- **Shoes and gloves before you move** (→ 12-02).
- **Downed power lines:** assume every line is live. Keep everyone, children and pets well back.
- **Gas:** if you smell gas, get everyone out and shut the gas off at the meter (→ 16-12). **Do
  not turn it back on yourself while a utility exists.** If no utility will come, relighting
  yourself is a decision card: {{choice DC-28}} → 30-29 (→ 16-12).
- **Do not go into a badly damaged building.**
- **Check on neighbours** (→ 18-01). Right after a tornado, neighbours are the only rescue there
  is.
- **Expect cuts and debris wounds** (→ 12-08). Photograph damage for insurance if that system
  still works (→ 19-04).

{{photo gas-shutoff}}

## Derechos: hurricane-force wind across a whole region

**SPC definition:** a derecho is a **widespread, long-lived windstorm** from a line of storms, with
a damage swath of **at least about 250 miles**, gusts of **at least 58 mph** along most of it, and
several well-separated gusts of **75 mph or more**.

- **What one looks like:** on August 10, 2020, a derecho crossed Iowa and beyond. Its path ran
  **over 750 miles**, winds passed **100 mph** in two areas (gusts near Cedar Rapids were estimated
  at 120 mph or more), and **over 1.9 million customers** lost power, 1.4 million of them at once
  (NWS Des Moines, event summary).
- **Warning signs:** sometimes a shelf cloud across the horizon, an advancing wall of dust or
  rain, then a sudden wind blast. SPC: derechos usually move at 50 mph or more, so these signs
  appear on very short notice, often too short to act on; the radio warning is what gives you
  time (→ 17-10).
- **What you do:** the tornado posture without waiting for rotation. Same shelter, same helmets.
  Trees and power lines come down everywhere at once.
- **Afterward it is a long, wide outage** (→ 17-08). Plan on days, not hours.

## Lightning: the everyday killer in the same storms

- **"When thunder roars, go indoors,"** and stay in until **30 minutes after the last thunder**
  (NWS, Lightning Safety brochure). If you can hear thunder, it is time to get to a safe building
  or vehicle.
- **Safe places:** a substantial building with electricity or plumbing, or a hard-topped metal
  vehicle with the windows up (NWS). Inside, stay off corded phones and other equipment wired to
  the mains, and away from plumbing: sinks, baths and taps (NWS, Lightning Tips).
- **Never safe:** open areas, hilltops, lone trees, water, wire fences and power lines, and
  sheds, picnic shelters, tents or covered porches (NWS); add tractors and mowers in the open.
{{#if has.pool}}- **Pool or hot tub:** thunder means everyone out of the water, and it stays
  closed until 30 minutes after the last thunder.{{/if}}
- **Grid-down life means more hours outside.** The 30-minute clock does not shrink because the
  chores are urgent. Use the time for indoor work.
- **If someone is struck:** NWS says lightning victims do not carry an electrical charge and may
  need first aid at once; cardiac arrest is what kills. Touch them and **start CPR at once**
  (→ 12-18).
  Move everyone else out of the open; lightning does strike the same place twice.

## When the warning systems are gone

In a long grid failure there may be no sirens, no phone alerts, no ambulance and no hospital.
- **A battery or crank NOAA Weather Radio still works** while transmitters run (→ 15-01). Keep
  its batteries as a protected reserve.
- **Read the sky** (→ 17-10).
- **Keep the shelter stocked as if you might lose the house.** Losing the house is a reason to
  move (→ 01-02); when you would leave home is a household decision: {{choice DC-19}} → 30-20

## Gear

| Item | Why | Notes |
|---|---|---|
| **NOAA Weather Radio with SAME, where you sleep** | Night tornadoes | → 15-01 |
| Second battery or crank radio in the shelter | You will be down there when the power goes | |
| **Helmets for everyone** (bike helmets are fine) | Head injury from debris | Kept in the shelter |
| **Shoes for everyone in the shelter** | Glass and nails afterward | Children's sizes checked each spring |
| Lights and spare batteries | Power will be out | → 10-01 |
| First-aid and trauma kit | Cuts and debris wounds | → 12-08 |
| Water and some food | You may be there a while | Rotate |
| Whistle per person | Signal from under debris | → 15-07 |
| Mattress or heavy blankets | Debris cover | |
| Work gloves | The aftermath | |
| Printed family plan and medical cards | → 25-09 | In the shelter |

**If you do not have it:** a hard hat, sports helmet or cushion for heads; couch cushions or a
sturdy table for debris; a bathtub with a mattress over it as the no-basement spot; banging on a
pipe to signal.

## Phase notes

- **A (at home):** shelter spot stocked and practiced; radio by the bed; medicines ready to grab.
  Know your neighbours.
- **B (moving):** a vehicle is a bad place in a tornado. Watch the radio and the sky and do not
  drive into severe weather (→ 01-03, → 17-11).
- **C (rural or new site):** fewer sirens, longer response, neighbours far away. A basement,
  storm cellar or safe room is a main test of any site (→ 01-05, → 17-06).

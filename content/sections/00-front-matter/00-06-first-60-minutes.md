---
id: 00-06-first-60-minutes
section: 00-front-matter
title: "The first 60 minutes"
version: 1
revised: 2026-11-16
layer: core
danger_level: critical
phase: [A, B]
tags: [first hour, emergency, outage, carbon monoxide, water, medicines, heat, go/no-go]
derived_from: [00-06-first-60-minutes]
sources:
  - cdc-carbon-monoxide-poisoning-basics-772153
  - american-red-cross-power-outage-safety-6d07a8
  - foodsafety-gov-usda-hhs-food-safety-during-a-power-o-3894c1
  - us-fda-information-regarding-insulin-storage-and-swi-6448d3
  - noaa-national-weather-service-tornado-safety-ba75e0
  - cdc-how-to-create-and-store-an-emergency-water-suppl-f0c412
  - us-consumer-product-safety-commission-cpsc-what-to-k-3390a4
related: [00-02-emergency-quick-reference, 25-08-quick-reference-cards, 01-01-phase-a-shelter-in-place, 01-02-go-no-go-decision, 08-02-carbon-monoxide-safety, 08-01-heating-one-room, 03-02-storing-water, 22-03-go-bags-and-kits, 09-16-outage-day-one, 09-06-charging-medical-devices, 12-21-evaporative-cooling-pouches]
cards: [DC-01, DC-02, DC-20, DC-25]
explainers: [EX-03, EX-07, EX-02]
promote_when: []
photo_slots: []
figures: []
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: null
---

# The first 60 minutes

**What this page is for.** The hour when something has just happened and nobody knows how bad it
is. Read it top to bottom, in order, and do it. The first hour is about **people, safety, water
and information**, in that order. Everything else can wait an hour; some of these cannot wait ten
minutes.

> **SAFETY — CRITICAL.**
> - **Never run a generator, charcoal, or any engine indoors, in a garage, or near an open
>   window.** Carbon monoxide kills in minutes with no warning; alarms fail; there is no
>   mitigation that works every time.
> - **Never connect a generator to house wiring without a transfer switch, interlock, or a
>   cord-and-plug conversion with the main breaker locked off. Never backfeed through an
>   outlet.** It electrocutes line workers and neighbours and starts fires.
> - **Never loosen a tourniquet once placed while help can still come; mark the time.**
>   Re-bleeding and clot release kill. If no help will ever come, the conversion decision is
>   DC-25 (→ 30-26).
> - **Fuel is never stored or transferred near an open flame or a running appliance.** Vapour
>   ignites.
> - **A frozen-then-thawed insulin vial or pen is discarded.** It loses strength with no way to
>   tell; the published guidance is unanimous.
>
> The reasons are on → 30-01.

## Minute 0 to 5: people and immediate danger

- [ ] **ACCOUNT FOR EVERYONE.** Say the names out loud: {{ household.labels }}.{{#if has.pets}} And the pets.{{/if}}
- [ ] **Anyone injured?** Bleeding first, always (→ 12-02, → 12-01).
- [ ] **Immediate hazard?** Fire, gas smell, structural damage, rising water, a tornado warning:
      **get out or get to shelter first.** Nothing on this page outranks that.
  - Fire: out, and stay out.
  - Tornado: {{ dwelling.shelter_room }}, cover heads (→ 17-02, → 17-06).
  - Gas smell: out, no switches, no flames.
- [ ] **CO alarm sounding, or anyone with headache, dizziness or nausea, especially several people
      at once: EVERYONE OUTSIDE, CALL 911, DO NOT GO BACK IN** (CDC, Carbon Monoxide Poisoning:
      Basics; → 08-02). No 911: fresh air is the treatment; rest outside for hours; stop the
      source before anyone goes back in.
- [ ] **Already leaving?** Go to → 22-03 (the 60-second grab) and → 01-06.

## Minute 5 to 10: medicine, before anything else

- [ ] **Find the medical kit** (→ 22-06). Put it where everyone knows, near the exit.
{{#if has.epinephrine}}- [ ] **Epinephrine:** confirm you have it, it is in date, and you can reach it (→ 02-03).{{/if}}
- [ ] **Refrigerated medicine: is it at a safe temperature right now?** (→ 29-07)
{{#each meds as x}}  - {{x.member}}: {{x.name}} {{x.strength}}, refrigerated: {{x.refrigerated}}
{{/each}}  - **Power is off:** keep the fridge shut. A closed fridge stays cold for about 4 hours
    (FoodSafety.gov, Food Safety During a Power Outage). If the outage looks long, move the
    medicine into a powered cooler or a cooling pouch before then (→ 09-16, → 12-21).
  - **Cold weather:** it must **not freeze**. Keep it inside, against the body if necessary.
  - **Hot weather:** get it out of the heat and into the coolest cooling you have (→ 12-21).
- [ ] **Devices that need power**{{#if has.oxygen}} (oxygen){{/if}}{{#if has.cpap}} (CPAP){{/if}}: check every battery. **Medical devices
      come first on every power bank and power station** (→ 09-06, → 09-10).
- [ ] **Count the days of each life-sustaining medicine on hand. Write the numbers down.**
      **The shortest one is the governing number for every decision that follows** (→ 01-02,
      → 23-01).

| Person | Medicine | Days on hand |
|---|---|---|
{{#each meds as x}}| {{x.member}} | {{x.name}} | ______ |
{{else}}| | | ______ |
{{/each}}

## Minute 10 to 20: capture water (the window closes fast)

- [ ] **Fill every container while the pressure lasts:** bathtub, pots, jugs, bottles, buckets
      (→ 03-02). Water pressure can fail hours after the power does. This window does not come
      back.{{#if has.well}} **A well pump stops when the power stops**: what is in the pipes and
      pressure tank is all you get (→ 03-10).{{/if}}
- [ ] **Know the reserves:** {{#if has.water_heater_tank}}the water heater (about
      {{ dwelling.water_heater_gallons }} gallons; know the drain valve), {{/if}}the pipes, the
      toilet tanks (not the bowls).
- [ ] **Boil advisory or possible contamination?** Treat everything (→ 03-04).
- [ ] **Our numbers** (→ 03-01): drinking and minimal hygiene floor
      **{{ derived.water.floor_gal_day }} gallons a day** for this household; planning figure
      **{{ derived.water.plan_gal_day }} gallons a day**; stored water lasts about
      **{{ derived.water.stored_days }} days** at the floor.
- [ ] **Freezing risk and no heat?** Shut the water main and drain the pipes (→ 03-06, → 17-01).

## Minute 20 to 30: information and contact

- [ ] **Turn on the NOAA Weather Radio** (→ 15-01). What is actually happening? For how long?
      Our transmitters: {{#each region.home.nwr as t}}{{t.call}} {{t.freq}} MHz · {{/each}}
- [ ] **Local radio, any working channel.** Write down what you learn and the time (→ 25-05).
- [ ] **Text, do not call.** Message the out-of-area contact, {{ contacts.out_of_area.name }}:
      where you are, who is with you, that you are safe (→ 15-03).
- [ ] **Save phone battery from this moment:** airplane mode between check-ins, low-power mode,
      screen dim, no scrolling (→ 00-10).
- [ ] **Check on neighbours**, especially anyone elderly or alone. Two minutes now buys the
      relationship you may need for months (→ 18-01).

## Minute 30 to 45: stabilise the house

- [ ] **Fridge and freezer stay shut.** About 4 hours for the fridge, about 48 hours for a full
      freezer (FoodSafety.gov, Food Safety During a Power Outage; → 04-17).
- [ ] **Heat (cold weather):** pick **one room** and start closing the house down to it (→ 08-01).
  - **Only heaters rated for indoor use, and only after a CO alarm is installed and tested in that
    room** (→ 08-02, → 08-04).{{#if has.unvented_heater}} You own: {{#each heaters as hh}}{{hh.kind_text}} · {{/each}}(→ 08-09, → 08-10).{{/if}}
  - **Grill, camp stove, generator: never inside.**
  - A fuel-burning heater running while people sleep is a household choice.
    **Our choice:** {{choice DC-01}} (→ 30-02)
  - A propane cylinder larger than 1 lb inside the house is a household choice.
    **Our choice:** {{choice DC-02}} (→ 30-03)
  - Candles and open flames indoors are a household choice. **Our choice:** {{choice DC-20}} (→ 30-21)
- [ ] **Cool (hot weather):** lowest floor, shade, moving air, wet cloths; watch children, elders
      and anyone on heat-sensitive medicine (→ 17-04).
- [ ] **Light:** headlamps out, one per person; do not light empty rooms (→ 10-01).
- [ ] **Power priority:** 1. medical devices 2. light 3. communications 4. refrigeration
      5. everything else (→ 09-01).{{#if has.power_station}} Our power stations hold about
      {{ gear.station_wh_total }} watt-hours in total, very roughly {{ derived.station_fridge_days }}
      days of a full-size fridge (an estimate; → 09-03).{{/if}}{{#if has.generator}} The
      generator runs **outside only**, far from windows and doors (CPSC, Portable Generator
      Safety; → 09-04).{{/if}}
- [ ] **Secure:** doors locked{{#if has.garage}}, garage down{{/if}}{{#if has.vehicle}}, vehicles locked. Fuel level in each vehicle? (→ 22-05){{/if}}
{{#if has.pets}}- [ ] **Pets:** contained, fed, watered, carriers where you can reach them (→ 20-09).{{/if}}

## Minute 45 to 60: decide, and set the shape of the next day

- [ ] **Read the go/no-go triggers (→ 01-02)** and ask them honestly, out loud, together:
  - Is the house safe? Is there water? Can we stay warm (or cool)?
  - Are the medicines and medical supplies enough for how long this looks?
  - Is it safe to travel: weather, roads, daylight, everyone's condition?
  - **In a winter storm, leaving is usually the more dangerous option** (American Red Cross,
    Winter Storm Safety).
- [ ] **If staying:** Phase A (→ 01-01). Assign roles (→ 00-07). Start the daily log (→ 25-05).
- [ ] **If leaving:** → 22-03 (bags), → 22-05 (vehicle), → 01-03 (movement), → 01-07 (medical
      needs on the road). Medicine rides in the cabin with a person. Go early rather than
      perfectly.
- [ ] **Everyone eats and drinks something**, especially anyone with diabetes{{#if has.child}},
      the children{{/if}}{{#if has.pregnant}}, anyone pregnant{{/if}}{{#if has.nursing}}, anyone
      nursing{{/if}}.
{{#if has.child}}- [ ] **Tell the children what is happening**, calmly and truthfully, at their level (→ 20-08).
      Give each child old enough a real job. It is the best thing you can do for them right now
      (→ 20-07).{{/if}}
- [ ] **Write down** what happened, what you did, what you used, and the time (→ 25-05).

## What people get wrong in the first hour

| Mistake | Instead |
|---|---|
| **Waiting to see if it comes back on** | Fill water in the first twenty minutes. The window closes and does not reopen |
| **Opening the fridge to check** | Keep it shut: about 4 hours fridge, about 48 hours full freezer (→ 04-17) |
| **Bringing a grill, camp stove, generator or any heater not rated for indoors inside for heat** | **Never.** This is how people actually die in outages (CDC, Carbon Monoxide Poisoning: Basics). Indoor-rated heaters run only with the CO alarm up first (→ 08-02) |
| **Burning phone battery on news and social media** | One check, write it down, then save power (→ 00-10) |
| **Leaving into a storm because staying feels passive** | Stranded vehicles kill people. Stay unless the triggers say otherwise (→ 01-02, → 17-01) |
| **Forgetting the medicine that has no substitute** | Deal with its temperature and count it in the first ten minutes (→ 29-07) |
| **Rationing children's food or drinking water on day one** | **Never ration those** (→ 23-01) |
| **Telling the children nothing** | Calm truth beats an anxious guess. They already know something is wrong (→ 20-08) |

## After the first hour

- **Hours 1 to 6:** settle into Phase A (→ 01-01). Set up the one-room plan, sanitation
  (→ 13-01) and lighting. **Sleep is a resource** (→ 21-07).
- **Days 1 to 3:** count everything and work out how long it lasts (→ 22-04, → 23-02). Set a
  routine, children's first (→ 21-04, → 20-03).
- **Every day after:** ask the go/no-go questions again (→ 01-02). Log everything (→ 25-05).

## Cross-references

- → 00-02 the fuller quick reference · → 25-08 the quick-reference cards
- → 01-01 Phase A · → 01-02 go/no-go · → 01-03 movement · → 01-07 leaving with medical needs
- → 29-07 refrigerated medicines · → 08-02 carbon monoxide · → 03-02 capturing water
- → 09-01 power priorities · → 22-03 go-bags · → 25-05 the daily log

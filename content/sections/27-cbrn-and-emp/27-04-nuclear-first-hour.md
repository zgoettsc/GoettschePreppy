---
id: 27-04-nuclear-first-hour
section: 27-cbrn-and-emp
title: "Nuclear detonation: the first hour"
version: 2
revised: 2026-11-16
layer: core
danger_level: critical
phase: [A, B]
tags: [nuclear, detonation, fallout, get inside stay inside stay tuned, shelter, first hour, radiation]
derived_from: [27-04-nuclear-first-hour]
sources:
  - us-department-of-health-and-human-services-remm-nucl-652eb0
  - cdc-radiation-emergencies-62e24d
  - ready-gov-fema-nuclear-explosion-dac8c3
  - noaa-national-weather-service-noaa-weather-radio-all-5f13d8
  - fema-nuclear-detonation-response-guidance-72-hours-2023
  - cdc-what-to-do-get-inside-2024
related: [27-05-fallout-sheltering, 27-06-potassium-iodide, 27-01-how-to-think-about-this, 08-01-heating-one-room, 15-01-weather-alerts, 22-06-kit-medical, 00-04-family-emergency-plan, 01-01-phase-a-shelter-in-place, 01-02-go-no-go-decision, 17-06-tornado-shelter, 30-02-dc01-unvented-heater-overnight, 30-23-dc22-potassium-iodide-over-40]
cards: [DC-01, DC-22]
explainers: [EX-09]
promote_when: []
photo_slots:
  - { id: fallout-shelter-spot, caption: "Our fallout shelter spot, and where the mass gets stacked" }
figures: [fig-shelter-by-dwelling]
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: { date: "2026-11-16", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "Fallout timing corrected to Ready.gov (10 minutes or more); blast-wave minutes removed; protection factor and 24 h sourced to FEMA 72-hour guidance and REMM; CDC get-inside added." }
---

# Nuclear detonation: the first hour

**What this page is for.** The actions for the first hour after a nuclear explosion, in order,
for a household that is not at the blast itself. Fallout is radioactive dust that the explosion
throws up and that falls back over a wide area in the hours afterwards. It is the main danger at
a distance, and **sheltering inside is what protects you from it.**

> **SAFETY. If this is happening, the message is three words:**
> **GET INSIDE. STAY INSIDE. STAY TUNED.** (Ready.gov, Nuclear Explosion; CDC, Radiation
> Emergencies.)
> Do not go outside to look. Do not drive to collect anyone. Do not leave unless officials tell
> you to. **Sheltering beats travelling**: fallout is worst early and fades fast (→ 27-05), and a
> vehicle gives almost no protection. **Never run a generator, charcoal, or any engine indoors,
> in a garage, or near an open window**, even now.

## The first hour: do it in this order

```
IF YOU SEE A BRIGHT FLASH
[ ] DO NOT LOOK AT IT. Take cover behind anything that might protect you;
    outside, lie face down to protect bare skin from heat and flying
    debris (Ready.gov). Inside, get down away from windows.
[ ] STAY DOWN until the blast wave has passed. It can arrive some time
    after the flash, and it breaks windows and throws debris.

THEN, AT ONCE
[ ] GET INSIDE the best building you can reach in a FEW MINUTES. Ready.gov:
    you will have 10 minutes or more to find an adequate shelter before
    fallout arrives; if a multi-story building or basement is a few minutes
    away, go there immediately. Do not travel further for a "better" one:
    time outside is what hurts you.
[ ] GO DOWN AND IN: below ground if you can, otherwise the centre of the
    building, away from outside walls, windows and the roof. YOUR SPOT is
    in the box below this list.
[ ] COUNT EVERYONE: every person, and the pets.
[ ] TAKE THE MEDICAL KIT with you (22-06): medicines, epinephrine, go-bags.
[ ] CLOSE windows, doors and vents. Turn off fans, air conditioners and
    forced-air heating units that BRING AIR IN FROM OUTSIDE (Ready.gov;
    CDC): bathroom and kitchen exhaust fans, fresh-air intakes, window
    units. Close the fireplace damper.
    A furnace that only recirculates indoor air may keep running if it has
    power: in winter it is the shelter's heat.

WITHIN THE FIRST 10 TO 15 MINUTES
[ ] IF YOU ARE STILL WALKING IN THROUGH FALLOUT: cover mouth and nose with a
    mask, cloth or towel (CDC). Imperfect beats nothing. Do NOT spend extra
    minutes outside perfecting it.
[ ] IF YOU WERE OUTSIDE: take off outer clothing before going into the
    shelter space, bag it, leave it outside the living space, and wash
    exposed skin and hair gently with soap and water. Removing the outer
    layer of clothing can remove up to 90% of radioactive material (CDC).
    No hair conditioner (FEMA). Do not scrub skin raw. Full routine: 27-05.
[ ] Bring pets in (CDC). If they were outside, brush and wipe the coat
    before they join you (Ready.gov).
[ ] TURN ON A BATTERY RADIO (NOAA Weather Radio or AM/FM). It is your only
    reliable source of instructions. (15-01)

WITHIN THE FIRST HOUR
[ ] SETTLE IN FOR AT LEAST 24 HOURS (Ready.gov): water, food, light, toilet,
    bedding into the shelter space. (27-05)
[ ] MEDICAL: count medicine days, confirm epinephrine is with you, put the
    phone on a power bank. (23-02, 09-10)
[ ] Do NOT take potassium iodide unless public health officials say to. (27-06)
[ ] Write down the time of the event and what you see. (25-05)
[ ] Text, do not call, if phones work at all. Then save the battery. (15-03)
```

### Your shelter spot

{{figure fig-shelter-by-dwelling}}

{{#if has.mobile_home}}**You live in a mobile or manufactured home. It gives very little protection from fallout**: it is
a light frame building, the weakest kind in HHS REMM's ranking. If a sturdy brick or concrete
building (a school, church, store, a neighbour's basement) is a few minutes away, **go there
now**, before fallout arrives: Ready.gov says the safest buildings have brick or concrete walls. If not, go to the centre of the home,
the lowest point, and pile the heaviest things you own around you. Nearby sturdy building:
______________ minutes away: ______
{{/if}}{{#if has.basement}}**Basement.** Go to the corner that is most below ground, away from windows and window wells, and
stack heavy things between you and any glass or exposed wall.{{#if has.walkout}} **Your basement is a walkout**: one
side is at ground level with doors or windows, so it is much weaker. Use the buried side or
corner, and stack mass across the walkout glass and door (→ 27-05).{{/if}}
{{/if}}{{#if has.shelter_room}}**Your named interior room**: {{ dwelling.shelter_room }}. Good if it is on the lowest floor and has no
outside walls; stack mass on any side that faces outside.
{{/if}}{{#if has.apartment}}**Apartment.** In a large building, the best places are underground (a basement or underground
garage) or the **centre of the middle floors**, away from the roof, the ground floor's outside
walls and all windows. Not the top floor; not the ground floor near glass. Use the stairs.
{{/if}}Our spot: ______________. Second choice: ______________.

{{photo fallout-shelter-spot}}

**Shelter with heat in winter.** If the spot you pick is not where you normally keep warm, plan
now how you will heat it. An unvented heater in a closed shelter room is a carbon monoxide risk
that is immediate, while fallout through a cracked window is small and fading: keep the heater's
air openings open (→ 08-01). Running one while people sleep: {{choice DC-01}} → 30-02

## Why sheltering beats running

This is the part that goes most against instinct, and where people get hurt.
- **Fallout is most intense early and fades quickly** (→ 27-05). The hours when it is worst
  outside are the hours you would spend driving.
- **A car gives almost no protection.** It is thin metal and glass; Ready.gov marks a car as not
  safe, and CDC says to get inside a building right away.
- **You do not know where the fallout is heading.** Officials, with monitoring, do. That is what
  the radio is for.
- **Roads will be blocked** by everyone else who decided to run.

**Federal guidance is consistent.** CDC: the best way to protect yourself in a radiation
emergency is to **get inside, stay inside, and stay tuned** (CDC, Radiation Emergencies). FEMA's
message for the public after a detonation is the same, and adds: prepare to stay inside for at
least 24 hours unless officials say otherwise or the building is threatened by fire or collapse
(FEMA, Nuclear Detonation Response Guidance, 2023). The exception is when officials order an
evacuation: then follow the route they give.

## What protects you: mass and distance

HHS REMM puts it plainly: a brick building protects better than a brick-veneer one, which
protects better than a wood-frame one, and there is less exposure in interior rooms and below
ground (HHS REMM, Nuclear Explosion).

Planners measure a shelter by its **protection factor** (also called a dose reduction factor).
FEMA's example: a factor of 200 means a person in that spot would receive 1/200th of the dose of
a person out in the open (FEMA, Nuclear Detonation Response Guidance: Planning for the First 72
Hours, 2023; HHS REMM). So a protection factor of 10 means one-tenth. Higher is better.

| Best to worst | Where |
|---|---|
| **Best** | Below ground, in the middle, surrounded by earth; the centre of a large concrete or brick building |
| Good | Middle floors of a large masonry building, interior rooms, away from windows; a basement corner |
| Poor | Ground floor near windows and outside walls; the top floor under the roof; a small wood-frame house above ground |
| **Worst** | Outdoors, in a vehicle, or in a mobile home |

**Two directions matter:** away from the **outside walls**, and away from the **roof**, because
fallout settles on the roof and the ground around you.

A tornado spot and a fallout spot can be different rooms. A tornado spot is for twenty minutes; a
fallout spot is for a day or two, and needs room for water, a toilet, bedding, and heat or
cooling (→ 17-06, → 27-05).

## How far away matters

- **The realistic concern for most households is fallout arriving from far away, hours after an
  explosion somewhere else**, not blast or heat. Distant fallout is exactly the case that
  sheltering handles well: hours of warning, the best space in the house, and 24 to 48 hours of
  supplies is a truly effective response. It is also when the radio matters most, because there
  will be time to be told what is coming.
- Which way the wind usually blows where you live, and what lies upwind, is worth knowing as
  geography. It changes nothing in the list above.

## What this page does not contain

No weapon sizes, blast-radius tables, target lists or dose calculations. **None of them change
a single action above.** If you are close enough for those numbers to matter, no page helps; if
you are far enough away to act, the actions are the ones listed (→ 00-05).

## If someone is outside and cannot reach you

Hard, and best decided now rather than in the moment:
- **They shelter where they are**, in the best building they can reach, for the same 24 hours.
  That is better for them than travelling to you.
- **The family plan says so in advance** (→ 00-04): everyone knows the rule is **shelter where
  you are, reunite when officials say it is safe**, not "everyone come home now".
{{#if has.child}}- **Schools and daycares have shelter plans.** Find out now what your children's are, and write it
  on → 25-03.
{{/if}}

## After the first hour

Go to **→ 27-05**: sheltering through 24 to 48 hours, cleaning off contamination, and judging
when it is reasonable to come out. Then the rest of the binder takes over: this becomes a long
shelter-in-place with no power (→ 01-01).

## What you need

Nothing on this page is unique to nuclear events. The shelter spot needs the 24-to-48-hour
supplies on → 27-05: **water, the medical kit, a battery radio, light, a bucket toilet, bedding,
food{{#if has.child}}, and something to keep children busy{{/if}}.**

No money? **Mass is mass.** Filled water containers, books, boxes of earth, furniture and
appliances stacked between you and the outside walls all add protection, and you already own them
(→ 27-05).

## When it runs out

- **Runway:** the acute phase is roughly **24 to 48 hours**; the supplies are for that window
  plus whatever follows.
- **Ration:** do not ration water or children's food, even in the shelter (→ 23-01).
- **Resupply:** none until officials say it is safe to move.
- **Substitute:** after the acute phase, this is an ordinary long grid-down event and every
  other section applies.

## By phase

- **A, at home:** shelter in place, firmly, against the urge to move.
- **B, moving:** **do not travel during or soon after fallout** unless officials direct it. This
  overrides the usual stay-or-go reasoning (→ 01-02). If officials do direct movement, **follow
  their route, not your own plan**: they know where the fallout is going. **Do not spend minutes
  standing outside hitching a trailer or loading a roof box**: in the one scenario where minutes
  outside matter, speed beats capacity.
- **C, establishing:** distance from likely targets is a minor factor in choosing a destination
  (→ 01-05), well below water and ground.

Potassium iodide is for later and only on official direction (→ 27-06). Adults over 40:
{{choice DC-22}} → 30-23

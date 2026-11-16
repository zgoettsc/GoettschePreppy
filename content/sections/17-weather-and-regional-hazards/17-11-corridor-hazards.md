---
id: 17-11-corridor-hazards
section: 17-weather-and-regional-hazards
title: "Hazards on the road to each destination"
version: 2
revised: 2026-11-16
layer: household
danger_level: critical
phase: [B]
tags: [travel, route, corridor, destination, ground blizzard, tornado, vehicle, flood, low-water crossing, trailer, wind, shelter on the road]
derived_from: [17-11-corridor-hazards]
sources:
  - noaa-storm-prediction-center-tornado-safety-faq-vehi-aba867
  - noaa-national-weather-service-tornadoes-during-the-e-a1a3ad
  - noaa-national-weather-service-turn-around-don-t-drow-a6f9ff
  - noaa-national-severe-storms-laboratory-severe-weathe-62747d
  - noaa-national-weather-service-winter-weather-safety-49fc7a
  - ready-gov-floods
  - fema-nri-counties
  - nws-winter-storm-during
related: [01-02-go-no-go-decision, 01-03-phase-b-movement, 01-05-choosing-a-destination, 01-07-evacuating-with-medical-needs, 17-01-blizzards-and-ice, 17-02-tornadoes, 17-03-floods, 17-04-extreme-cold-and-heat, 17-06-tornado-shelter, 17-10-reading-the-sky, 17-13-hurricanes-and-tropical-storms, 17-14-wildfire-smoke-and-evacuation, 15-09-corridor-comms, 16-11-trailer-maintenance-and-repair, 22-05-kit-vehicle, 25-04-maps, 09-11-hand-and-alt-generation, 30-07-dc06-fuel-in-passenger-vehicle, 30-20-dc19-when-to-leave]
cards: [DC-06, DC-19]
explainers: [EX-10]
promote_when: [has.destinations]
photo_slots:
  - { id: route-atlas, caption: "Our paper atlas with each route, the low spots and the shelter stops marked" }
figures: [fig-tornado-vehicle-choices, fig-flood-water-depths]
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: { date: "2026-11-16", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "NRI meaning explained under the hazard table; empty-destination table fixed; NWS vehicle source." }
---

# Hazards on the road to each destination

**What this page is for.** A trip to a destination crosses country whose weather you may not know.
This page lists, for each of your destinations, what the weather does there and what it is likely
to do on the way, then gives the rules for the hazards that kill people in vehicles: ground
blizzards, tornadoes, flooded roads and high wind. Print it and keep a copy in the vehicle kit
(→ 22-05).

> **SAFETY. The route is checked before departure, not managed after.** A hazard you drive into on
> purpose is not weather; it is a planning failure. Three rules that are never relaxed:
> - **Never drive into flowing water** across a road: 6 inches knocks an adult down, 12 inches
>   carries away most cars, 2 feet carries away SUVs and trucks (NWS, Turn Around Don't Drown).
> - **A closed road means stop.** Never detour onto back roads in a winter storm.
> - **Never shelter under an overpass** in a tornado (SPC).

## Your destinations

{{#each destinations as x}}
### {{x.name}}

- **Where:** {{x.county}}, {{x.state_name}}. Status: **{{x.status_text}}**. About
  **{{x.approximate_miles}} miles**.
- **Climate there:** January nights about {{x.region.jan_low_f}} °F; July days about
  {{x.region.jul_high_f}} °F; about {{x.region.snow_in}} inches of snow a year; elevation about
  {{x.region.elevation_ft}} ft.
- **Weather office there:** {{x.region.nws_office}}. State emergency agency:
  {{x.region.state_em}}.
- **Your route notes:** {{x.route_notes}}
- **Shelter stops on this route** (sturdy buildings, full-service towns, rest areas): ______________
- **Low spots and flood-prone crossings on this route:** ______________
- **The point of no return** (past here, you are committed to open country or a long stretch with
  no services): ______________
{{else}}
No destination is entered. The rules below still apply to any trip, including a move toward town,
family or medical help. Add destinations in settings and regenerate.
{{/each}}

## The honest read for each route

{{ai corridor-hazards-read}}

## Home hazards, for comparison

| Hazard at home | Rating |
|---|---|
{{#each region.home.hazards as h}}| {{h.name}} | {{h.rating_text}} |
{{/each}}

**What the rating means.** The ratings come from FEMA's National Risk Index for each county, on a
1-to-3 scale (low, moderate, high). They measure expected harm to people and property, not how
likely the hazard is: a big city can rate high for a rare hazard because so much is exposed (Cook
County, Illinois, rates high for earthquakes), and a thinly settled county can rate low for a
hazard that does strike it. Use them to choose which pages to read first, never to decide that a
hazard on your route cannot happen (→ 29-10). Each destination's full hazard list is on its state
page in Section 32.

## Season and route: decide before you need to

When to leave is a household decision written in advance: {{choice DC-19}} → 30-20. For each
destination, fill in the table before the season starts.

{{#if has.destinations}}| Season or situation | {{#each destinations as x}}{{x.name}} | {{/each}}
|---|{{#each destinations as x}}---|{{/each}}
| Winter, storm anywhere on the route | {{#each destinations as x}}Wait / go: ____ | {{/each}}
| Winter, clear multi-day window | {{#each destinations as x}}Wait / go: ____ | {{/each}}
| Spring and summer storm season | {{#each destinations as x}}Wait / go: ____ | {{/each}}
| Hurricane or wildfire season | {{#each destinations as x}}Wait / go: ____ | {{/each}}
| Short warning, any season | {{#each destinations as x}}Wait / go: ____ | {{/each}}{{else}}| Season or situation | Any trip you might make: wait or go? |
|---|---|
| Winter, storm anywhere on the route | ____ |
| Winter, clear multi-day window | ____ |
| Spring and summer storm season | ____ |
| Hurricane or wildfire season | ____ |
| Short warning, any season | ____ |{{/if}}

**General rules that fit almost any route:**
- **Short trips can wait for a weather window.** A day's delay costs little; driving into a storm
  can cost everything.
- **Long trips suit only an early, seen-it-coming departure in a clear multi-day window** (→ 01-05).
- **In storm season, leave in the morning**; severe thunderstorms peak in the late afternoon and
  evening. Avoid driving at night when flash floods are possible.
- **Main highways are cleared and patrolled first.** In ice or snow, stay on them or do not go.

## Winter: the ground blizzard

A **ground blizzard** needs **no falling snow**: dry snow already on the ground plus strong wind
makes zero visibility at road level, sometimes under a blue sky (NSSL, Winter Weather Types). The
trap: you leave in sunshine and an hour later the road disappears.
- **The setup to recognise** (→ 17-10): fresh dry snow on the ground, a clearing sky, a rising
  barometer and strong northwest wind. **A beautiful cold morning after a snowstorm can be the most
  dangerous travel day of the year** in open country.
- **Closed road means stop.** Never detour onto back roads in winter: they drift shut, nobody plows
  or patrols them, and people die on them.
- **Whiteout while driving:** do not stop in a travel lane. Exit if you can; otherwise pull as far
  off the road as possible, lights on, and **stay with the vehicle** (→ 17-01: tailpipe clear,
  engine about 10 minutes each hour, a bright marker; NWS).
- **Fuel:** keep the tank at least half full in winter and fill at every chance (→ 22-05).

## Tornado while driving

NWS: **"Being in a vehicle during a tornado is not safe. The best course of action is to drive to
the closest shelter."** If a tornado is close and there is no building (SPC, Tornado Safety FAQ):
1. **If you can, drive away at right angles to its path.** Do not try to outrun it along its track.
2. **Caught by extreme wind or debris:** park out of traffic lanes. **"Stay in the car with the
   seat belt on. Put your head down below the windows; cover your head with your hands and a
   blanket, coat, or other cushion."**
3. **"If you can safely get noticeably lower than the level of the roadway, leave your car and lie
   in that area, covering your head with your hands."** Noticeably lower and reachable means
   ditch; otherwise stay belted in the vehicle below the windows.
   {{#if has.young_child}}With small children in car seats, the vehicle is usually the realistic
   choice.{{/if}}
4. **Never under an overpass.**
5. **Mobile home parks are not shelter.** Drive on to something sturdier.

{{figure fig-tornado-vehicle-choices}}

## Floods and low-water crossings

- **Never cross flowing water.** You cannot see whether the road is still there.
- **Back roads in hill country often cross creeks at fords and dips** that flood in minutes.
  When flood watches are up, stay on the main highways and do not drive at night (→ 17-03).
- **If your vehicle is trapped in rushing water, stay inside unless water is rising inside it;
  then get onto the roof** (Ready.gov, Floods; → 17-03).

{{figure fig-flood-water-depths}}

## Hurricanes, wildfire and smoke on the route

- **Hurricane evacuation routes jam.** Leave when told, or earlier, and know the official route
  (→ 17-13).
- **Wildfire closes roads without notice and smoke cuts visibility to nothing.** Never drive toward
  a fire to "get past it" (→ 17-05, → 17-14).

{{#if has.trailer}}## Towing a trailer

A tall trailer catches wind like a sail, and an empty or lightly loaded one is the worst case.
**No agency publishes crosswind limits for a household trailer**, so set your own, conservatively,
and test them on a windy day before it matters (→ 16-11):
- Slow to ______ mph when gusts reach ______ mph.
- Stop towing when gusts reach ______ mph.
- On ice or packed snow: ______ (many experienced towers simply stop).
- **When to drop the trailer:** sheltering from a tornado (seconds matter: leave it), a wind hold
  that is outlasting the daylight, or any time the vehicle must move and the trailer cannot.
  **Cargo can be replaced; people cannot.** Note where you left it and drive on. Practice
  unhitching once so it takes two minutes.
- Load heavy items low and over or just ahead of the axle; check the trailer brakes and lights
  before every trip.
{{/if}}

## Shelter on the road

Ranked, using the rule from → 17-02 (lowest floor, interior, walls between you and outside):
1. **Sturdy public buildings:** truck stops (interior restrooms), stores with interior rooms or walk-in
   coolers, banks, schools, churches, courthouses, hospitals.
2. **Rest areas** with solid masonry restroom buildings: adequate in a tornado warning, good for a
   wind or ice hold.
3. **Motels:** an interior ground-floor bathroom. Also the ice-storm answer: **ice on the route
   means stop early and take the room.** Driving on is how a trip becomes a rescue.
4. **The vehicle:** last resort, per the rules above.

{{photo route-atlas}}

## Gear

| Item | Why | Notes |
|---|---|---|
| **This page and a paper atlas with routes and shelter stops marked** | The plan must be on paper | → 25-04 |
| Winter vehicle kit | Stranding | → 22-05 |
| NOAA Weather Radio in the vehicle | Warnings where phones do not reach | → 15-09 |
| Fuel at least half, always | Closures strand you where you are | |
| List of truck stops and rest areas on each route | The shelter plan | On the atlas |

Carrying spare fuel inside the passenger area is a trade-off with its own card:
{{choice DC-06}} → 30-07

**If you do not have it:** any masonry building beats the vehicle; local AM radio reads road
closures; truck drivers at fuel stops know the road ahead. **What you cannot substitute is slack.**
Every rule here is a version of "leave early, stop early, wait a day."

## When it runs out

- **Fuel:** closures and detours burn it. Below a quarter tank in bad weather, stop at the next
  services and fill or stay.
- **Daylight:** winter gives few driving hours. A long trip may not fit in one winter day, which is
  itself a reason to choose the season.
- **Route knowledge:** roads close, bridges wash out. After any real event, the last traveller's
  information beats the map. Update the atlas notes every trip.
- **The decision habit:** at every fuel stop, decide the next leg only (→ 01-03). A trip is a chain
  of short decisions, not one long one.

## Phase notes

- **B (moving):** this whole page is the moving phase. Weather on the route turns "go" into "wait",
  and waiting is almost always right (→ 01-02, → 01-03, → 01-05).

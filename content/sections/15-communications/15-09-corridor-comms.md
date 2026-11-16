---
id: 15-09-corridor-comms
section: 15-communications
title: "Road communications: staying heard on the way"
version: 2
revised: 2026-11-16
layer: household
danger_level: caution
phase: [A, B]
tags: [travel, route, check-in, PACE, text first, "911", CB, GMRS, satellite, dead zones, visor card, charging, overdue]
derived_from: [15-09-corridor-comms]
sources: [fema-ready-gov-create-your-family-emergency-communic-584e89, us-government-publishing-office-ecfr-47-cfr-part-95-c8b55a, noaa-national-weather-service-noaa-weather-radio-all-5f13d8, nws-winter-storm-during, apple-support-use-emergency-sos-via-satellite-messag-68d4e2, ecfr-47-cfr-part-9-911-requirements, cdc-carbon-monoxide-poisoning-basics-772153]
related: [15-08-destination-comms, 15-03-family-comms-plan, 15-01-weather-alerts, 15-02-radio-options, 15-06-antennas-and-range, 17-11-corridor-hazards, 17-01-blizzards-and-ice, 17-08-power-grid-failure, 25-04-maps, 25-08-quick-reference-cards, 01-03-phase-b-movement, 01-07-evacuating-with-medical-needs, 09-03-batteries-and-storage, 09-14-car-batteries-in-practice, 22-05-kit-vehicle, 14-03-opsec, 08-02-carbon-monoxide-safety]
cards: [DC-19]
explainers: [EX-09, EX-03]
promote_when: [has.destinations, has.vehicle]
photo_slots: []
figures: []
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: { date: "2026-11-16", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "Stranded-vehicle CO advice sourced to NWS winter-storm page; 911 wording tightened." }
---

# Road communications: staying heard on the way

**What this page is for.** Keeping the people at both ends (the "nodes" on → 15-08) informed from
a moving vehicle, including the stretches where the phone shows no bars. The plan is a **PACE
ladder** (Primary, Alternate, Contingency, Emergency): channels written down, agreed with the
nodes, and used **in order** instead of improvised at a rest stop. The route hazards themselves
are on → 17-11 and the maps on → 25-04; this page is only about staying heard.

> **CAUTION.** **If the road stops you, stay with the vehicle, at a named town if you can, note
> the time, and wait**: the overdue trigger on → 15-08 is doing the searching. If you run the
> engine for heat while stopped, keep the tailpipe clear of snow and a window cracked: a blocked
> exhaust fills a car with carbon monoxide. The NWS says: stay in the vehicle, clear snow from the
> exhaust pipe, and open a window a little while the engine runs (NWS, What To Do If You're
> Caught in a Winter Storm; CDC, Carbon Monoxide Poisoning Basics; → 08-02).

## Do this now

1. **Print the visor card** (below), fill it in, and keep it in the vehicle with the node numbers
   from → 15-08.
2. **Drive each route once in good weather with this page out**, and pencil in the truth: where
   the phone really had signal, which check-in towns work, how long each leg took. **Every
   coverage guess is an assumption until you have done this.**
3. **Write down each adult's phone carrier.** A second phone on a different carrier is a real
   backup, because towers fail unevenly. Driver: ____________ Other adult: ____________ Same?
   ☐ (if so, that rung is thinner).
4. **Make sure the charging kit rides along**: a car charger and cables for every phone and radio.
   A dead phone deletes the whole first rung.

## Check-in points for each route

{{#each destinations as x}}### To {{x.name}} ({{x.state_name}}, about {{x.approximate_miles}} miles)

Your route notes: {{x.route_notes}}

| Leg | Check-in town | Signal there (pencil after the test drive) | Note |
|---|---|---|---|
| Departure | Home | ______ | Departure text to the node and the relay (→ 15-08) |
| 1 | ______________ | ______ | |
| Midpoint | ______________ | ______ | The midpoint text, before committing to the next leg |
| 3 | ______________ | ______ | Last good coverage before any known dead zone? |
| Arrival | {{x.name}} | ______ | **The arrival text cancels the overdue trigger** |

{{else}}No destinations are entered in your profile. Use the blank table for any long trip.

| Leg | Check-in town | Signal there | Note |
|---|---|---|---|
| Departure | Home | ______ | |
| Midpoint | ______________ | ______ | |
| Arrival | ______________ | ______ | |
{{/each}}

**Planning assumptions until a drive proves otherwise:** open country between towns, hills,
valleys and forests have weak or no signal; **assume no coverage at all in a blizzard**, when the
weather that strands you also floods the network (→ 17-01). **A missed midpoint check-in is
information, not an alarm; only the arrival deadline starts the calls** (→ 15-08).

## The PACE ladder on the road

| Rung | Channel | The reality |
|---|---|---|
| **P** | **Phone, and text first** | **A text queues and retries through weak, brief signal that a call cannot hold**; one sent in a dead zone often goes through at the next hilltop. Send check-ins as texts by default. **911 connects from any phone on any carrier's tower**, even when your own carrier shows "No Service", or with no plan, as long as some carrier's tower is in reach: call it rather than texting (47 CFR 9.10). Wi-Fi calling (→ 15-03) works over any gas-station or motel Wi-Fi |
| **A** | **The other adult's phone** | A different carrier means different towers. A stopped trucker's phone or a gas-station phone is also an alternate: the message matters, not whose phone |
| **C** | **GMRS and CB** | GMRS on the family channel near home or the destination where someone is listening (→ 15-03, → 15-08). On the open road, **CB channel 19 is where truckers are**: road news and a message someone will relay; **channel 9 is the traditional emergency channel, but assume nobody official listens.** A radio call to a stranger who will phone your node *is* reach-back |
| **SAT** | **Satellite texting** | Some phones (for example iPhone 14 and later) can send an **emergency SOS by satellite** with your location when there are no bars, and newer software can send ordinary texts by satellite (Apple Support, Emergency SOS via satellite). **Clear sky, step out of the vehicle, hold the phone up, follow the on-screen pointer; it is slow, so send one short line.** A satellite messenger does the same **only with a paid subscription.** Satellite internet in the vehicle needs a plan that allows use while moving (→ 15-02) |
| **E** | **NOAA Weather Radio: listening only** | When you can reach nobody, you can still **hear** warnings ahead (→ 15-01). **The emergency rung is: stop and wait** at a named town (→ 17-11), note the time, and let the arrival deadline do its job. **A vehicle stopped at a named town is what a search finds; one improvising across country is not** |

What our household has on each rung: P ______ A ______ C ______ SAT ______ E ______

## The visor card: print this

One sheet, folded to visor size, one per route (a master copy on → 25-08). Fill the clock lines at
departure, every trip, in pencil.

```
ROUTE TO: ______________    ROUTE: __________
DEPARTED: ____:____      ARRIVAL DUE: ____:____
OVERDUE TRIGGER STARTS AT: ____:____  (15-08)
CHECK-INS: 1)__________ 2)__________ 3)__________
NODE (destination): __________  ph __________
RELAY: {{ contacts.out_of_area.name }}  ph {{ contacts.out_of_area.phone }}
TEXT FIRST. WHO / STATUS (OK - NEED HELP - MOVING)
            / WHERE / NEXT CHECK-IN
C: GMRS ch ____ . CB 19 (truckers) / 9 (emergency)
SAT: SOS by satellite: clear sky, hold phone up
911 works on ANY carrier's tower
E: weather radio - step through all 7 channels
IF STOPPED: stay with vehicle, named town if you
can, note time, wait - the trigger is running
```

**The card is the plan a tired driver actually follows.**

## Charging on the road

The first rung dies with the phone battery.

- **Phones and power banks:** a good USB car charger in the 12 V socket, with a cable for every
  phone. Keep it in the vehicle kit (→ 22-05).
- **GMRS and amateur handhelds:** from the same USB charger, or their own 12 V cords.
- **Satellite internet**, if you carry it: it draws real power, so run it in short windows at
  check-in stops. Phones and radios charge first.
- **Satellite texting uses battery too**: the phone searches the sky at full power. Do it with
  plenty of charge, or on the car charger.
- {{#if has.hybrid}}**Your hybrid** can act as a parked generator while you wait, but keep the
fuel tank well above empty and the **carbon monoxide** rule in mind: tailpipe clear, never in a
closed space (→ 08-02).{{else}}**A running vehicle** charges everything while you wait, but keep
the tailpipe clear and never idle in a closed space (→ 08-02).{{/if}}
- **Phone habit on the road:** airplane mode through known dead zones, off at check-in points. A
  phone hunting for towers all day is dead by evening.

## Gear

| Item | Why | Notes |
|---|---|---|
| **A printed visor card per route, filled in** | The plan at eye level | → 25-08 |
| A USB car charger and cables | The first rung's lifeline | → 22-05 |
| A GMRS handheld in the vehicle | The contingency rung at both ends | → 15-02 |
| **CB (mobile or handheld) and a real antenna** | Channel 19 is where the road talks | → 15-02 |
| A weather radio in the vehicle | The emergency rung: incoming warnings | → 15-01 |
| A paper road atlas with routes and check-ins marked | Phones die | → 25-04 |
| A charged power bank in the cab | Bridges the phone between stops | → 09-03 |
| A phone with satellite texting, or a messenger with a subscription | The satellite rung | Try the demo at home |

**If you do not have it:**

- **No CB?** A GMRS or amateur handheld, plus asking a trucker at a stop: their CB and phone become
  yours for one message.
- **No car charger?** Any gas station sells one; a poor one beats a dead phone.
- **No working phone at all?** Every open business on the road has one. **The message is three
  lines (WHO, STATUS, WHERE): anyone can pass it to your node.**

## When it runs out

- **On the road, battery runs out first, then coverage.** The charging kit handles the first; the
  ladder handles the second.
- **Over the years the coverage picture changes**: carriers change, towers come and go. **Pencil in
  the dead zones again every time you drive the route.** The card is meant to be corrected.
- **When the whole network is down** (→ 17-08), the ladder shrinks to the contingency and emergency
  rungs, and the plan becomes → 15-08's phones-down routine: the nodes' trigger clocks still run.
  **The deadline you set at departure is the one piece of communication that works with no
  infrastructure at all.**

## By phase

- **A (at home):** preparation: the test drives, the printed card, the carriers written down, the
  charging kit in the vehicle (→ 22-05).
- **B (on the move):** **this page is the trip.** Text at every named point, go down the ladder in
  order, and if the road stops you, **stopping and waiting is a communications strategy**, because
  the overdue trigger (→ 15-08) is doing the searching (→ 01-03).
- **C (at a destination):** the card flips for the trip back: a new departure text, new clock
  lines, the same ladder.

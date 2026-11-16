---
id: 15-08-destination-comms
section: 15-communications
title: "Destination communications: the node book and the overdue trigger"
version: 1
revised: 2026-11-16
layer: household
danger_level: critical
phase: [A, B, C]
tags: [destination, node, relay, overdue, check-in, travel, arrival signal, missing traveller, GMRS, satellite, medical]
derived_from: [15-08-destination-comms]
sources: [fema-ready-gov-create-your-family-emergency-communic-584e89, noaa-national-weather-service-weather-ready-nation-b0a52f, us-government-publishing-office-ecfr-47-cfr-part-95-c8b55a, american-red-cross-power-outage-safety-6d07a8, federal-communications-commission-9-1-1-and-e9-1-1-s-a8c9c7]
related: [15-09-corridor-comms, 15-03-family-comms-plan, 15-02-radio-options, 15-05-ham-and-licensing, 15-06-antennas-and-range, 15-07-signals-and-codes, 01-05-choosing-a-destination, 01-07-evacuating-with-medical-needs, 01-03-phase-b-movement, 12-11-chronic-conditions, 17-11-corridor-hazards, 00-04-family-emergency-plan, 14-03-opsec, 25-03-regional-contacts, 25-04-maps, 25-10-annual-review, 30-20-dc19-when-to-leave]
cards: [DC-19]
explainers: [EX-09]
promote_when: [has.destinations]
photo_slots: []
figures: []
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: null
---

# Destination communications: the node book and the overdue trigger

**What this page is for.** The trip that goes quiet. When a household drives to a destination,
especially in one vehicle, the communications problem is **reach-back**: the people who need to
know you are safe are the ones you left and the ones you are driving toward. **If nobody at
either end knows when to expect you, nobody knows when to start looking.** This page is the
"node book": the people at fixed places who hold a copy of the plan and an agreed job, and the
**trigger that turns "late" into "call for help".**

> **SAFETY.** Agree the overdue trigger **before** every trip, out loud, with a clock time. A
> traveller who is overdue in winter, or who depends on medicine or a device they carry, is a
> medical emergency, not a logistics problem. **911 connects from any phone on any carrier's
> tower** (FCC, 9-1-1 and E9-1-1 Services). When to leave home at all is a household decision:
> {{choice DC-19}} → 30-20.

**What a node is:** a person at a fixed place with a phone, a copy of the plan, and an agreed job.
Most lines below are blank on purpose: **fill them in ink, then brief each node out loud.**

## Do this now

1. **Fill in a node card for the relay and for each destination** (below): phone, second phone,
   radio. **Call each node to brief them**, and write the date. An unbriefed node is a name, not a
   plan.
2. **Agree the overdue trigger with each node:** *"If you haven't heard I arrived by ___ o'clock,
   you call the numbers on your card."* Say the actual clock time before every trip.
3. **Agree an arrival signal** with each destination household (below) and write it down.
4. **Give each node a paper copy** of their own card, the road card (→ 15-09), and the medical
   facility list for the route (→ 01-07).

## The network

Home: {{ home.county }}, {{ home.state_name }}. The out-of-area relay:
**{{ contacts.out_of_area.name }}** (→ 15-03), far enough away that a regional disaster at home
does not take their phone down too, and the fixed point everyone reports through when direct
lines fail.

{{#if has.destinations}}Your destinations:
{{#each destinations as x}}- **{{x.name}}**, {{x.county}}, {{x.state_name}}, about
  {{x.approximate_miles}} miles. Status: **{{x.status_text}}**.
{{/each}}{{else}}No destination is entered in your profile. The relay card still applies to any
trip, and you can add destinations in settings and regenerate (→ 01-05).{{/if}}

## Node card: the relay

| Field | Value |
|---|---|
| Name | {{ contacts.out_of_area.name }} |
| Phone | {{ contacts.out_of_area.phone }} Verified by calling ☐ (date ______) |
| Second phone or other household member | ____________________ |
| Radio? | ☐ GMRS ☐ amateur ☐ none. Model: ____________ |
| Role | **The relay.** Everyone checks in through them when direct contact fails; they pass messages on (below). Daily check-in time from → 15-03: ______ |
| Briefed and agreed (date) | ____________ |

## Node cards: destinations

{{#each destinations as x}}### {{x.name}} ({{x.status_text}})

| Field | Value |
|---|---|
| Where | {{x.county}}, {{x.state_name}}; about {{x.approximate_miles}} miles |
| Who is there | {{x.who_is_there}} |
| How to reach them | {{x.how_to_reach_them}} |
| Second phone | ____________________ |
| Radio? | ☐ GMRS ☐ amateur ☐ none. Model: ____________ |
| Local NWS office | {{x.region.nws_office}} |
| Role | Destination node: holds this destination's overdue trigger and the facility list (→ 01-07) |
| Arrival signal agreed | ________________________________________ (date ______) |
| Briefed and agreed (date) | ____________ |

{{else}}No destinations entered.
{{/each}}

**If a destination's status is not "agreed"**, nobody there has accepted a node job and nobody
there should be expected to start calls. **For a trip to a place that has not agreed, the relay
holds the overdue trigger**, and you arrive self-sufficient (→ 01-05).

## The check-in routine, every trip

Three calls or texts (texts queue through weak signal, → 15-09), every trip:

1. **Departure:** "Leaving now, taking route ___, expect to arrive by ___." To the **destination
   node and the relay** (relay only if the destination has not agreed).
2. **Midpoint:** one line from a named midpoint town (the route list is on → 15-09): "Past ___, on
   schedule."
3. **Arrival:** "Here, safe." **This is the call that cancels the trigger.** It is not optional.

## The overdue trigger: the line that makes this a plan

**If the node has no arrival word by a set time after departure, the node starts calling the
route's emergency and hospital list.** Not worrying. Calling.

**Trigger = expected drive time + a buffer the household chooses.** Write both for each route
before you need them:

| Route to | Drive time | Buffer | Trigger (hours after departure) |
|---|---|---|---|
{{#each destinations as x}}| {{x.name}} | ______ h | ______ h | **______ h** |
{{/each}}| ______________ | ______ h | ______ h | **______ h** |

A shorter buffer means calls start sooner, sometimes for nothing; a longer one means help starts
later. In winter, at night, or with a traveller who depends on medicine, shorter is safer.

**What the node calls, in order** (each node's card carries this filled in):

1. The traveller's phone, then the other adult's phone, then the relay (word may have come
   through them).
2. **911 or the non-emergency dispatch for the county of the last check-in**: report an overdue
   traveller, the vehicle, the route, **and the medical facts below.**
3. **The state patrol for each state on the route:** ____________________________________
4. **The hospitals along the route** (→ 01-07): ____________________________________

**The medical line: say it plainly.** If the overdue traveller depends on a medicine, device or
supply they carry (insulin, oxygen, an epinephrine auto-injector, a refrigerated medicine), **it is
a medical emergency timeline.** A car in a ditch overnight is then a medical event, not a towing
problem. **The node's script to dispatch includes the condition in one sentence**, for example
"The missing driver is an insulin-dependent diabetic." That sentence changes search priority
(→ 12-11).{{#if has.condition.CL-01}} Your household includes someone with type 1 diabetes: write
this sentence on every node card.{{/if}}{{#if has.oxygen}} Your household includes someone on
oxygen: write the supply time on every node card.{{/if}}

Our sentence for dispatch: ______________________________________________________________

## The arrival signal: agree it before you need it

A no-notice arrival at a destination in a tense period is how misunderstandings happen (→ 14-03).
Agree **in advance, with each household**, what an approach looks like, and write it on their
card. A workable default to propose: **stop at the head of the drive, headlights off, interior
light on, one short horn, and wait to be waved in.** Whatever is agreed, both sides write it down;
it also covers *their* family arriving at *your* house.

## When the phones fail

- **GMRS at set times:** on the family channel (→ 15-03), on the hour for five minutes, once a
  node is within GMRS range (a few miles, → 15-06), which usually means the last part of the
  approach. Agreed listening time with each node: ____________
- **Relaying through the relay:** when home and a destination cannot reach each other, **both
  contact the relay, who passes messages both ways**, using the → 15-03 script (WHO, STATUS,
  WHERE, NEXT CHECK-IN).
- **When nothing electronic works:** the plan falls back to the note protocol (→ 15-03) at the
  destination, and **the trigger clock still runs**. The node's briefing covers this: "If the
  region is dark, you still start the calls at the trigger time, from wherever you have service."
- **Amateur radio:** {{#if has.ham}}a licensed member{{else}}a licensed operator{{/if}} can pass
  "health and welfare" messages through amateur nets when everything else is down (→ 15-05). Tell
  the nodes this channel exists so a relayed message does not surprise them.
- **Satellite texting** from a phone that has it, or a messenger, reaches the relay with a clear
  sky (→ 15-03). Tell the nodes it exists.
- **Satellite internet**, if the household has it activated (→ 15-02), gives a destination a
  messaging and Wi-Fi calling path that does not need local cell towers. An inactive dish is not a
  channel.

## Gear

| Item | Why | Notes |
|---|---|---|
| **This page filled in, in ink, with briefing dates** | Blank cards are not a plan | Re-check yearly (→ 25-10) |
| **A copy of each node's card at that node** | The node acts from their copy | Mail it or hand it over |
| **The relay's number, memorised and written** | One working relay rebuilds the network | Also on → 15-03 and → 00-04 |
| The road card in the visor | The traveller's half of this plan | → 15-09 |
| Route facility list | What the node dials at the trigger time | → 01-07 |
| A GMRS handheld at each willing node | The last mile when phones are down | → 15-02 |
| A prepaid phone card and coins or cash | Long distance sometimes works when local does not | Cheap insurance |

**If you do not have it:**

- **No number for a node?** Go through the relay. One working relay number rebuilds the network,
  which is why the relay's card is verified first.
- **No radio at a node?** Set listening times still work one way: you transmit on approach, and
  they only need ears. Any FRS radio on the family channel hears you.
- **No working phones anywhere?** Letters and travellers. Slow, but **an agreed silence deadline is
  what turns no news into action.**

## When it runs out

- **Nothing here gets used up; it goes stale.** Numbers change, agreements fade, people move. **The
  yearly review (→ 25-10) re-checks every line**, and any visit is a chance to re-brief a node in
  person.
- **What actually fails is the briefing.** A node who vaguely remembers agreeing two years ago will
  hesitate at the trigger time, and the whole value of the trigger is that nobody has to decide at
  the worst moment. **Say the clock time again at every departure.**
- **People at both ends who know the schedule and have agreed when to start calling** are the one
  cheap, renewable safety asset on the road. Paper and a few phone calls buy what no gear can.

## By phase

- **A (at home):** keep the node book up to date: check numbers, brief on visits, and keep the
  relay used to ordinary check-ins so the crisis is not the first time.
- **B (on the move):** **this page is live from the departure call.** The traveller runs → 15-09;
  the nodes run this page; the trigger clock runs for everyone.
- **C (at a destination):** on arrival this page turns around: home becomes the far node, and **the
  same trigger covers the trip back.** Agree the clocks again before returning.

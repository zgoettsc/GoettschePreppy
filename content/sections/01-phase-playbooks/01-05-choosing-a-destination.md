---
id: 01-05-choosing-a-destination
section: 01-phase-playbooks
title: "Choosing and securing a destination"
version: 1
revised: 2026-11-16
layer: household
danger_level: caution
phase: [A, B, C]
tags: [destination, phase C, agreed, unannounced, property only, pre-positioning, cache, how to ask, medical distance]
derived_from: [01-05-choosing-a-destination]
sources:
  - cdc-guidelines-for-testing-well-water-382a7a
  - american-red-cross-winter-storm-preparedness-and-bli-4bb6c0
  - fema-ready-gov-shelter-8572d8
related: [01-02-go-no-go-decision, 01-03-phase-b-movement, 01-04-phase-c-establish, 01-07-evacuating-with-medical-needs, 18-01-mutual-aid, 19-01-document-grab-kit, 15-08-destination-comms, 05-18-destination-garden-calendar, 05-19-destination-foraging-and-hazards]
cards: [DC-19]
explainers: []
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

# Choosing and securing a destination

**What this page is for.** Where this household would go if home stopped working, how sure each
place is, and what is left to do to make it real. A destination you have agreed, visited and
stocked turns Phase B from a gamble into a drive.

> **CAUTION.** **An unconfirmed destination fails exactly when it is needed.** Arriving somewhere
> nobody expects you, that you have never checked, can turn a plan into trespass with your
> household standing in the yard. Each destination below is printed with its honest status.
{{#if !has.agreed_destination}}> **This household has no agreed destination.** Until it does,
> staying is strongly preferred, and the realistic move is toward town, family or medical help
> (below).{{/if}}

## Do this now

1. **Read the status of each destination below** and agree, out loud, that it is true.
2. **For an agreed destination: settle the open questions** (below) on the next call, and **place
   the cache** on the next visit.
3. **Visit it.** Drive the route (→ 01-03). Look at the water, the heat, the space, the road, the
   storm shelter. Every ordinary visit is a route check.
4. **For an unannounced or undecided destination: decide whether to ask.** Asking is a normal
   conversation (below). If you choose not to, write down what that means: you arrive with
   everything, and you may be turned away.
5. **Write it down**: → 00-04 section 6 carries the destinations and how to reach them; → 01-02
   carries the fork rule; → 01-04 carries the arrival steps.

## Our destinations

| Destination | Where | About | Status | Who is there | How to reach them |
|---|---|---|---|---|---|
{{#each destinations as d}}| **{{d.name}}** | {{d.county}}, {{d.state_name}} | {{d.approximate_miles}} mi | **{{d.status_text}}** | {{d.who_is_there}} | {{d.how_to_reach_them}} |
{{else}}| **None entered** | | | | | |
{{/each}}

**What each status means:**

| Status | Meaning | What it lets you do | What it does not |
|---|---|---|---|
| **Agreed** | The people there have said yes, and know roughly how many and how long | Pre-position supplies; plan comms; arrive expected | It is still a favour. Revisit it every year |
| **Unannounced** | They have not been asked (by choice or not yet) | Arrive and ask at the door | Pre-position anything; count on a bed, water, food or heat |
| **Property only** | Nobody lives there; it is your land or someone's empty place you may use | Cache supplies if you control access | Count on anyone to have kept it warm, dry, stocked or empty of strangers |
| **Undecided** | A place you are still considering | Plan, visit, ask | Count on it at all |

### The honest read

{{ai destination-honest-read}}

### Each destination's region

| Destination | Zone | January mean low | July mean high | Annual snow | Weather office | Emergency management |
|---|---|---|---|---|---|---|
{{#each destinations as d}}| {{d.name}} | {{d.region.zone}} | {{d.region.jan_low_f}} °F | {{d.region.jul_high_f}} °F | {{d.region.snow_in}} in | {{d.region.nws_office}} | {{d.region.state_em}} |
{{/each}}

Hazards, plants and radio frequencies for each destination are in its state's pages in Section 32;
the garden calendar and foraging hazards are → 05-18 and → 05-19.

## Why / how it works

### Why a hoped-for destination is dangerous
- You arrive with **no agreement**, and a household with a medical need, an allergy, small
  children or elders is asking a lot of a host who was never asked.
- You arrive somewhere you have **never checked**: no idea whether the water works, the stove is
  safe, or the road is passable in snow.
- You may find **others already there**, or **nobody and a locked house**, which turns your plan
  into trespass.
- **You cannot pre-position anything** at a place you have not arranged.

### What makes a good destination

| What | Why | Best case |
|---|---|---|
| **People who expect you** | Everything else comes second | A standing agreement |
| **Distance** | Reachable in a day on the fuel you can carry, in winter (→ 01-03) | Within one tank, if you have the choice |
| **Water** | Well, spring, or reliable surface water | A hand pump or gravity option (→ 03-10) |
| **Heat** | Wood stove and wood | Dry wood already on site |
| **Shelter** | Heatable, weather-tight, room for {{ household.size }} plus the hosts | One good room beats a big cold house |
| **Storm shelter** | A basement or a safe inside room | Known before the first warning (→ 17-06) |
| **Medical distance** | The medicine clock (→ 01-07) | Near a town with a pharmacy and a hospital |
| **Access** | Passable in snow; not behind a single bridge | Two ways in |
| **Growing ground** | Long-term food | Garden space and a season to use it |
| **Community** | Rural survival is shared | Neighbours who know you |

**Note the tension:** the most "secure" remote place is also the furthest from medicine.
{{#if has.refrigerated_meds}}This household has refrigerated medicine, so a place near a working
small town usually beats one deep in the country.{{else}}For any household with a medical need, a
place near a working small town usually beats one deep in the country.{{/if}} Write that trade-off
down so it is not re-argued under stress.

### The open questions for each destination

Settle these on the next call or visit. Tick and write the answer.

{{#each destinations as d}}
**{{d.name}}** ({{d.status_text}})
- [ ] **Water:** well, town water or other? If town water, what is the backup when the pumps stop
      (stored water, rain catchment, a pool, a well)? ______________________
- [ ] **Heat:** what keeps one room warm with no power? Fuel on site? Chimney inspected?
      ______________________
- [ ] **Gas:** a utility line (stops when the system upstream stops) or a tank on site (months of
      stored fuel)? ______________________
- [ ] **Storm shelter:** basement or safe inside room? If none, what is the plan?
      ______________________
- [ ] **Power:** generator, safe house connection, solar? A furnace blower needs power whatever
      the fuel. ______________________
- [ ] **Medical:** nearest pharmacy, emergency room, children's emergency care; drive time
      ______________________ (→ 01-07)
- [ ] **Room:** how many people can they take, for how long? ______________________
- [ ] **Cache:** agreed? Where? ______________________
- [ ] **Comms:** how we reach them when phones fail (→ 15-08): ______________________
{{else}}
No destination entered. Use the list above when you start looking.
{{/each}}

### How to ask
It is a normal conversation, not a strange one. Something like:

> *"We've been putting together an emergency plan, and we want to know where we'd go if we ever
> had to leave home. Would you be open to us coming to you? And you'd be welcome with us, of
> course."*

Then agree the practicalities: how many people, for how long, what you would bring, whether you
can leave supplies there, and how you would contact each other (→ 15-08). Offer something in
return: skills, supplies, a standing welcome at your place. A reciprocal offer makes it durable
rather than a favour.

### Pre-positioning (a cache)
Once there is an agreement, a lot becomes possible:

- **Leave supplies there**: food, water containers, fuel, blankets, tools, clothing in the next
  size up{{#if has.anaphylaxis}}, food that is safe for the allergic person{{/if}}. Anything cached is
  weight you do not carry, and a hedge if you arrive with nothing.
- **Leave a printed copy of the key pages** of this binder and the medical action plans
  (→ 00-10, → 25-09).
- **Leave nothing that spoils with heat or cold: not insulin, not epinephrine, not other
  refrigerated medicine.** Those travel with you (→ 01-07, → 29-07). Medical supplies that are not
  temperature-sensitive (syringes, testing supplies, dressings) can be cached if their storage
  label allows the site's temperatures (→ 29-14).
- **Keep it modest and agreed.** Supplies at someone else's property are a favour; treat them as
  one.

### Unannounced, in practice
If you have decided not to ask, write down what that means so nobody is surprised:

- **No agreement.** The offer (your skills, your supplies, your labour) is made **at the door**,
  and the answer may be no. Plan for a no: → 01-02's four questions again.
- **Nothing is pre-positioned.** Everything rides with you, including the medicine cold chain and
  fuel for the return trip (→ 01-03).
- **You will probably not be the only ones.** Housing, water and food there are theirs to share,
  not yours to assume.
- **Refrigeration and power there are unknown.** Assume none until you have seen them (→ 01-07).
- **Comms:** with no plan in place, write "no contact until arrival" on the trip card (→ 15-08).

### If no destination can be secured
Be honest in the plan rather than pretending:

- **Staying becomes strongly preferred**, and the binder should be used to make home work as long
  as possible (→ 01-01).
- **The realistic Phase B is toward town, family or medical help**, not into the countryside.
- **Public shelters** are a real option in a declared disaster (FEMA, Shelter){{#if has.anaphylaxis}},
  with the serious caveat that **shared shelter food is dangerous for anyone with a food allergy**:
  carry their food and their epinephrine (→ 02-04){{/if}}{{#if has.pets}}. Not every shelter takes
  pets; ask in advance (→ 20-09){{/if}}.

When to leave for any of these is written on → 01-02. **Our triggers:** {{choice DC-19}} (→ 30-20)

## Gear / items

**Have now (buy toward this):**

| Item | Why | Notes |
|---|---|---|
| A written, mutual agreement | Even with family, write the practicalities down | A conversation, then a note |
| Printed maps with the routes marked | No GPS | → 25-04 |
| A cache at the destination | Weight you never carry | Agreed destinations only |
| Copies of medical action plans there | If you arrive separated or someone is impaired | → 25-09, → 19-01 |
| A reciprocal offer | Makes it durable, not a favour | Costs nothing now |

**Scavenge / substitute:** **this page is a conversation, not a purchase.** The substitute for a
secured destination is a stronger Phase A: more supplies, more efficiency, more community at home
(→ 18-01).

## When it runs out

- **Runway:** an agreement made and never revisited quietly becomes an assumption. **Its value
  decays if you never act on it.**
- **Resupply / substitute:** a second and third candidate, so one failure does not end the plan.
- **Review every year**, and after any change in the other household's life: a move, an illness, a
  new baby, a death.

## Phase notes

- **A (at home):** do the work now. It is a phone call and a drive.
- **B (moving):** you go to a named place, or you do not go.
- **C (arriving):** arriving somewhere expected is a completely different experience from arriving
  somewhere hoped-for (→ 01-04).

## Cross-references

- → 01-02 go/no-go (the destination is one of the four questions) · → 01-03 movement
- → 01-04 establishing · → 01-07 medical needs on the road and at the destination
- → 18-01 mutual aid · → 19-01 document kit · → 15-08 destination comms

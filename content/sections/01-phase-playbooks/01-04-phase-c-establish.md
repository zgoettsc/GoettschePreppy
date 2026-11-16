---
id: 01-04-phase-c-establish
section: 01-phase-playbooks
title: "Phase C: establish at a destination"
version: 1
revised: 2026-11-16
layer: core
danger_level: caution
phase: [C]
tags: [phase C, arrival, first 48 hours, site assessment, well water, chimney, carbon monoxide, neighbours, exit triggers]
derived_from: [01-04-phase-c-establish]
sources:
  - cdc-guidelines-for-testing-well-water-382a7a
  - cdc-carbon-monoxide-poisoning-basics-772153
  - cdc-preventing-hypothermia-c53e0c
  - chimney-safety-institute-of-america-csia-preventing-73b734
related: [01-03-phase-b-movement, 01-05-choosing-a-destination, 01-02-go-no-go-decision, 03-07-testing-water, 08-01-heating-one-room, 05-01-a-small-high-yield-garden, 18-01-mutual-aid, 20-02-child-safety-offgrid, 30-22-dc21-uninspected-fireplace-or-stove]
cards: [DC-21]
explainers: [EX-03, EX-06]
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

# Phase C: establish at a destination

**What this page is for.** What to do in the first 48 hours after you arrive somewhere that is not
home, how to size up a place quickly, and when to move again. It works for a planned destination,
a place where nobody expected you, or anywhere you end up.

> **CAUTION.** Arriving is not the end of the emergency; in many ways it is the start of a harder
> one. An unfamiliar building has an unfamiliar chimney (**carbon monoxide and chimney-fire
> risk**, → 08-02), unknown water (→ 03-07) and unknown neighbours. **Never run a generator,
> charcoal, or any engine indoors, in a garage, or near an open window.** **The first 48 hours
> set up everything that follows.** Work the sequence below rather than improvising.

## Do this now: the first 48 hours

1. **Shelter and warmth.** One heatable room, sealed up, before dark (→ 08-01).
2. **CO alarm in the sleeping space**, and **inspect any chimney, flue or stove before first
   use**. An unfamiliar chimney is an unknown until you have looked up it (CSIA, Preventing
   Chimney Fires). Lighting one that has not been inspected is a household choice.
   **Our choice:** {{choice DC-21}} (→ 30-22)
3. **Water.** Find the source; **treat everything until it is tested** (→ 03-04, → 03-07).
4. **Medicines stabilised**: a cool spot that cannot freeze for refrigerated medicines (→ 29-07),
   a room-temperature spot for rescue medicines such as epinephrine (→ 02-03).
5. **Sanitation sited**: downhill from and far from any water source, before anyone improvises
   (→ 13-07).
6. **Security and awareness**: who else is here, what are the ways in (→ 14-01).
7. **Introduce yourselves to the neighbours**, if there are any. In rural areas, being known is
   worth more than being invisible (→ 18-01).

## Why / how it works

### Sizing up a site fast

| Question | Why it matters |
|---|---|
| **Water**: well, spring, creek, pond, town water? Does the pump need power? | Everything depends on it (→ 03-07) |
| **Heat**: stove, fireplace, fuel on site? Chimney condition? | Surviving winter, and carbon monoxide |
| **Shelter**: weather-tight? Which room can be heated? | → 08-01 |
| **Sanitation**: septic, sewer? Where can a latrine go, away from water? | Disease prevention (→ 13-07) |
| **Storm shelter**: basement, or an inside room with no windows on the lowest floor? | → 17-06 |
| **Food**: anything stored, ground to grow on, game, fish? | Section 05 |
| **Access**: can you get out? Snowed in? One road? | An escape question and a defence question |
| **People**: neighbours, owners, others already there? | → 18-01, → 14-01 |
| **Medical**: nearest pharmacy, clinic, hospital, and how far? | The medicine clock (→ 01-07) |

**Do the water and heat checks before dark on day one.** Everything else can wait a day.

### Water at a new site
Rural water is usually **fresh**: it needs **disinfection**, not distillation (→ 03-04). But:

- **A well pump needs power.** Know whether there is a hand pump, a generator connection or a way
  to draw water by bucket **before** you rely on it (→ 03-10).
- **Town water stops when the town's pumps stop.** If the place is on public water, **fill every
  container on arrival**, before unloading anything but the medicines (→ 03-02).
- **Test it when you can** (→ 03-07). Wells in farm country can carry **nitrate** from fertiliser
  and livestock. The serious danger is to **infants under about 6 months** (a blood condition
  called methemoglobinemia), so it matters most if the household includes a young baby or anyone
  pregnant. **Boiling concentrates nitrate rather than removing it** (CDC, Guidelines for Testing
  Well Water).{{#if has.infant}} **This household has an infant: do not use untested well water
  for formula.**{{/if}}
- **Treat everything until it is tested.** Assume it is unsafe.

### Heat at a new site
- **Inspect the chimney and stove** before lighting anything. Blocked flues, birds' nests and
  creosote (tar-like soot) are common in a building nobody has used for a while, and all of them
  cause carbon monoxide or chimney fires (CSIA, Preventing Chimney Fires; → 06-09).
- **Firewood must be cut and dried ahead** (→ 06-03). Wood cut today is not fuel for months. If
  you arrive in autumn with no dry wood, that is a serious problem: look for standing dead trees,
  which are already partly dry.
- **Heat one room** (→ 08-01). Rural houses are often large, old and draughty.

### Food and the long game
- **Count anything on site** before planning.
- **Ground and season**: check the destination's growing zone and frost dates (Section 32 and the
  table below). If it is not spring, you are planning, not planting (→ 05-01, → 05-02).
- **Game, fish and foraging** (→ 05-06, → 05-07, → 05-08) add to the food supply but rarely feed a
  household alone.
{{#if has.anaphylaxis}}- **Safe food for anyone with an allergy stays the limit** (→ 02-04). Unfamiliar and shared food is
  the risk; food you grow yourself is the safest because you know everything in it.{{/if}}

| Destination | Hardiness zone | Last spring frost | First fall frost | Ecoregion |
|---|---|---|---|---|
{{#each destinations as d}}| {{d.name}} | {{d.region.zone}} | {{d.region.last_frost}} | {{d.region.first_frost}} | {{d.region.ecoregion}} |
{{else}}| (no destination entered) | | | | |
{{/each}}

### Children, elders and farm hazards
{{#if has.child}}A farm or rural property is full of things that kill children: farm ponds and open water, grain
bins and wagons (grain swallows a child), machinery and power take-off shafts, livestock, working
dogs, and chemicals in sheds. **One adult walks the property and agrees boundaries with the hosts
on day one** (→ 20-02).{{else}}A farm or rural property has hazards that are new to town people:
open water, grain bins, machinery, livestock, dogs and stored chemicals. Walk the property on day
one and ask the hosts what to stay away from (→ 20-02).{{/if}}{{#if has.elder}} Uneven ground, steps and
unlit outbuildings are where elders fall; light the paths and clear a route to the toilet (→ 02-21).{{/if}}

### People
Rural communities notice new arrivals at once. **Being known and useful beats being hidden**: you
cannot hide a household in a small community anyway. Offer your skills (→ 18-03), respect property
and boundaries, and say plainly what you need and what you can give (→ 18-01). A household with a
medical need needs a community more than most.

### Arriving by status
How you arrive depends on the destination's status (→ 01-05):

| Status | What arriving looks like |
|---|---|
| **Agreed** | Expected. Use what was pre-positioned. Fit into the hosts' routine from day one; their house, their rules |
| **Unannounced** | **Nobody expects you.** Everything you need rides with you. The first conversation is the ask you did not make in advance, and the answer may be no. Offer your skills plainly at the door. Expect others to have arrived first. If refused, go back to → 01-02's four questions, not an argument |
| **Property only** | Nobody is there. Check for squatters, damage and other people before unloading. Run the 48-hour list above exactly |
| **Undecided** | A place you hoped for. Treat it as unannounced |

{{#each destinations as d}}- **{{d.name}}** ({{d.status_text}}): {{d.who_is_there}}
{{/each}}

### When the destination fails: exit triggers
→ 01-02 applies in reverse: **a destination can stop working, and the trigger to move again must
be written down before you are tired, invested and reluctant.** Agreed by every adult:

| Trigger | Threshold | Response decided now |
|---|---|---|
| **Water fails** | Cannot produce {{ derived.water.floor_gal_day }} gallons a day and it cannot be fixed (pump dead with no power, well dry, source contaminated and untreatable) | Move toward working water: a town, another destination, or home if it is viable (→ 01-02's four questions, again) |
| **Medicine supply or cold chain fails** | No way to keep refrigerated medicine in range (→ 29-07), or the runway says supply runs out before resupply | Move **toward** medical help, a pharmacy town or a hospital, not deeper into the country (→ 01-07). This outranks any attachment to the place |
| **Security** | A threat the people there cannot manage (→ 14-01) | Leave together, early, with the hosts if they will come. Do not defend a site against the odds{{#if has.child}} with children present{{/if}} |
| **Medical emergency** | Someone needs care that cannot be given there | Toward the nearest working facility at once. One adult and the patient go, or everyone goes: decide by the security and fuel picture |
| ______________ | ______________ | ______________ |

**Run → 01-02's four questions again before any move.** The answer may be another destination, or
home. Leaving a failing site late is the same mistake as leaving home late.

## Gear / items

**Have now (buy toward this):**

| Item | Why | Notes |
|---|---|---|
| CO alarm in the go-bag | Unfamiliar chimney on night one | → 08-02 |
| Water test strips (nitrate, bacteria, dissolved solids) | Size up the water fast | → 03-07 |
| Headlamps and lanterns | Arrival is often at dusk | Section 10 |
| Axe, saw, shovel, hammer, wire | Make a building work | → 16-01 |
| Tarps, plastic sheeting, cordage, staple gun | Weather-tighten fast | → 08-03 |
| Seeds | Only useful if you brought them | → 05-03 |
| Flashlight and mirror for looking up a chimney | Inspect before lighting | → 06-09 |
| Printed maps of the destination area | Find your way without GPS | → 25-04 |

**Scavenge / substitute:**
- Any building, outbuilding or vehicle can be made into one heatable space (→ 08-06).
- Standing dead wood is the fastest usable fuel at a new site.
- Local knowledge from neighbours is worth more than any gear you brought.

## When it runs out

- **Runway:** at a rural site the tight limits change: **medicine supply** (further from
  pharmacies) and **dry firewood** (→ 06-03) get tighter; water often gets easier.
- **Ration:** the same discipline as Phase A, with longer resupply trips and less margin.
- **Resupply / substitute:** the local community becomes your resupply network (→ 18-02).
- **The strategic warning:** **do not move far from pharmacies with a short medicine runway**
  unless staying is worse. Distance from medical help is the price of rural safety, and for some
  households that price is counted in days of medicine (→ 01-02).

## Phase notes

- **A (at home):** keep the destination ready: visit, settle the open questions, place the cache
  (→ 01-05), so Phase C is arrival, not improvisation.
- **B (moving):** the trip is → 01-03; arrive with daylight left.
- **C (at the destination):** this page. Work the 48-hour sequence, then settle into the Phase A
  rhythm (→ 01-01) at the new place.

## Cross-references

- → 01-03 movement · → 01-05 choosing a destination · → 01-06 transition checklists
- → 03-07 testing water · → 08-01 heating one room · → 08-02 carbon monoxide and unfamiliar chimneys
- → 05-01 gardening · → 18-01 mutual aid · → 01-07 distance from medical help

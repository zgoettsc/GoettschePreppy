---
id: 01-02-go-no-go-decision
section: 01-phase-playbooks
title: "The go/no-go decision: triggers to leave"
version: 2
revised: 2026-11-16
layer: core
danger_level: critical
phase: [A, B, C]
tags: [go/no-go, leaving, triggers, thresholds, evacuation, medicine runway, winter travel, destination]
derived_from: [01-02-go-no-go-decision]
sources:
  - american-red-cross-power-outage-safety-6d07a8
  - ready-gov-winter-weather-r9
  - american-academy-of-pediatrics-aap-allergy-and-anaph-3e6f49
  - cdc-how-to-create-and-store-an-emergency-water-suppl-f0c412
related: [30-20-dc19-when-to-leave, 01-01-phase-a-shelter-in-place, 01-03-phase-b-movement, 01-04-phase-c-establish, 01-05-choosing-a-destination, 01-06-phase-transition-checklists, 01-07-evacuating-with-medical-needs, 23-02-master-consumables-table, 06-04-wood-supply-and-depletion]
cards: [DC-19]
explainers: []
promote_when: []
photo_slots: []
figures: []
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: { date: "2026-11-16", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "DC-19 worksheet kept blank; winter travel to Ready.gov; epinephrine to AAP; tank half full to Red Cross." }
---

# The go/no-go decision: triggers to leave

**What this page is for.** It turns "should we leave?" from a 3 a.m. argument into a checklist
your household wrote while it was calm. It lists the usual reasons to leave, asks you to set your
own threshold for each, and gives the four questions to answer before anyone gets in a vehicle.

> **SAFETY — CRITICAL.** This is the highest-stakes decision in the binder and the one most often
> made badly: too late, in a panic, in bad weather{{#if has.child}}, with children{{/if}}.
> **Decide the triggers now, in writing, while you are calm.** A threshold agreed in advance is
> worth more than any amount of judgement at 3 a.m. in a cold house. **Never set out into a
> winter storm unless staying is immediately deadly**: FEMA's advice is to stay off the roads in
> a winter storm if at all possible (Ready.gov, Winter Weather).

## Do this now

1. **Fill in the trigger worksheet below** and have every adult agree to it. Sign and date it.
   This worksheet is your answer to decision card DC-19. **Our triggers:** {{choice DC-19}}
   (→ 30-20)
2. **Understand the default: staying is safer.** Leave only for a real reason.
3. **Know the trigger most likely to move your household.** For many families it is heat or
   security. **If anyone depends on a medicine or a powered device, it is far more likely to be
   that supply**, and that trigger usually points **toward** medical help, not away from it.
4. **Never leave into a storm.** Wait for the weather unless the house is immediately unsafe.
5. **If you go, go early.** The worst version of this decision is leaving after you are out of
   supplies, out of fuel and out of daylight.

## Why / how it works

### The two ways to get it wrong
1. **Leaving when you should have stayed.** You trade a stocked, known, defensible position for
   exposure, unknown roads and whatever you can carry. This is the more common mistake.
2. **Staying when you should have left.** You burn your last options and then must move in the
   worst condition: no fuel, no food, no daylight, maybe sick.

The only defence against both is a **threshold decided in advance**, written down, that turns a
judgement call into a checklist.

### The trigger worksheet: fill this in and agree it

How to choose each threshold is in the notes under the table. Write a number of days, gallons or
devices, not a feeling.

| Trigger | Our threshold | Go where |
|---|---|---|
| **A life-sustaining medicine** (each one; → 23-02) | Start active resupply at ______ days left. Move toward medical supply at ______ days left with nothing secured | Toward pharmacies and a hospital (→ 01-07) |
| **Powered medical device** (oxygen, CPAP, other){{#if has.oxygen}} *(applies to us)*{{else}}{{#if has.cpap}} *(applies to us)*{{/if}}{{/if}} | Move when power for it is down to ______ days | Toward power and medical help (→ 09-10) |
| **Epinephrine** {{#if has.epinephrine}}*(applies to us)*{{/if}} | Resupply now when in-date devices drop to ______ | Toward medical supply (→ 02-03) |
| **Heating fuel, in winter** | ______ days left at one-room burn rates | Somewhere that can be heated |
| **Safe water** | Cannot produce ______ gallons a day (our floor is {{ derived.water.floor_gal_day }}) | Toward water |
| **Food for anyone on a special diet** (allergy, celiac, infant formula) | ______ days of safe food left | Toward food you can verify |
| **House unsafe** | Fire, structural damage, flooding (→ 17-03) | Immediately, anywhere safe |
| **Security** | A threat we cannot manage (→ 14-01) | Away, together |
| **Neighbourhood** | Fire spreading, mass departure, utilities gone for good | Follow the plan |
| **Medical emergency** | Someone needs care we cannot give | Toward care |
| ______________ | ______________ | ______________ |

**Signed:** ______________________ ______________________ **Date:** ____________

**How to choose the numbers:**

- **Medicines: use two stages.** The first number is when you start working hard on resupply
  while staying home: pharmacy runs, telehealth, mutual aid. The second, lower number is when the
  household moves toward medical supply if nothing has worked. Leave room between them for how
  long resupply actually takes, and for the trip itself (→ 01-07).
- **Epinephrine:** one reaction can need a second dose (AAP, Allergy and Anaphylaxis Emergency
  Plan), so count in pairs. Expired devices are a separate household choice (→ 30-05).
- **Heating fuel:** leave while the vehicle can still be loaded warm, not on the last log
  (→ 06-04).
- **Water:** the drinking-and-hygiene floor for this household is
  **{{ derived.water.floor_gal_day }} gallons a day** (→ 03-01, from the CDC and FEMA basis
  of one gallon per person per day). Below the floor, water is failing however much undrinkable
  water you can see.
- **Special diets:** food that is safe for one person is often the first thing to run out and the
  hardest to replace.

### The medicine clock deserves its own paragraph

Most survival writing assumes the reason to leave is danger. **For a household with a medical
dependency, it is more often arithmetic.**{{#if has.refrigerated_meds}} This household has at
least one refrigerated medicine (→ 29-07).{{/if}} If a medicine's runway drops below the
threshold you set, the right move is **toward** medical supply (a hospital, a pharmacy, a working
town), and that may mean **not** going to the countryside at all. **Do not let a general wish to
"get out of the city" override a medical reality.** → 01-07 covers the trip itself.

### Go or no-go: the four questions
Before moving, answer all four. If you cannot, you are not ready to go.

1. **Where exactly are we going?** A named place (→ 01-05). "Out of town" is not a plan.
2. **How do we get there, and is that route survivable right now?** Weather, distance, fuel,
   daylight (→ 01-03).
3. **What happens when we arrive?** Shelter, heat and water on day one (→ 01-04).
4. **Is it better than staying?** Honestly, compared with a stocked house you know how to heat.

**If any answer is weak, the answer is: stay, and fix that answer.**

### Timing
- **Weather first.** Never depart into a blizzard or extreme cold; wait it out unless the house is
  actively unsafe (Ready.gov, Winter Weather: stay off roads if at all possible).
- **Daylight.** Leave in the morning. Arriving in the dark, cold and somewhere unfamiliar is how
  people get hurt.
- **Earlier is better than later** once the decision is made: fuel in the tank, food in the packs,
  people still strong.
- **Do not split the household** except by an explicit plan with a meeting point (→ 15-03).

### Where we would go

| Destination | About | Status | Page |
|---|---|---|---|
{{#each destinations as d}}| {{d.name}} ({{d.county}}, {{d.state_name}}) | {{d.approximate_miles}} mi | {{d.status_text}} | → 01-05 |
{{else}}| **No destination entered.** Staying is strongly preferred; the realistic move is toward town, family or medical help (→ 01-05) | | | |
{{/each}}

**Match the destination to the warning you have.** A far destination needs a long, seen-it-coming
departure: days of warning, open roads, full fuel, and no storm on the route. A sudden,
short-warning event or bad winter weather points to **staying, or moving a short distance toward
town and medical help**, not to a long drive. Write your own fork rule here:

If ______________________________________________ → we go to ______________________.
Otherwise → ______________________________________________.

{{#if has.destinations}}A destination marked **unannounced** or **property only** means nobody
there is expecting you: you arrive with everything you need, and the first conversation is an ask
that may be refused (→ 01-05).{{/if}}

## Gear / items

**Have now (buy toward this):**

| Item | Why | Notes |
|---|---|---|
| This page, filled in and signed | Turns panic into a checklist | Every adult agrees |
| Paper maps of the region | Routes without GPS (→ 25-04) | Mark several routes out |
| Vehicle kept fuelled | You cannot refuel in an outage | At least half full (American Red Cross, Power Outage Safety; → 22-05) |
| NOAA Weather Radio | Never depart into a storm | → 15-01 |
| Go-bags, packed and current | Leave in minutes, not hours | → 22-03 |
| A written destination, route and arrival plan | The four questions, answered ahead | → 01-05 |

**Scavenge / substitute:** this page is decisions, not equipment. The decisions are free and must
be made now.

## When it runs out

- **Runway:** this page uses nothing; it **reads** every other runway in the binder. Keep → 23-02
  current or these triggers cannot be judged.
- **Ration:** every day you add to a runway (efficiency, mutual aid, resupply) is a day you do not
  have to make this decision.
- **Resupply / substitute:** local resupply almost always beats moving. Exhaust it first.
- **Review it every three months.** Thresholds change as people grow, supplies change, and a
  destination is secured or lost.

## Phase notes

- **A (at home):** the decision lives here. Review it at every daily check-in.
- **B (moving):** once you go, commit, but keep re-checking; **turning back is legitimate** if
  conditions change.
- **C (at a destination):** the same framework applies in reverse. A destination can stop working
  too, and the trigger to move again should be written down (→ 01-04).

## Cross-references

- → 30-20 the decision card for these triggers · → 01-01 Phase A · → 01-03 movement
- → 01-04 establishing at a destination · → 01-05 destinations · → 01-06 transition checklists
- → 01-07 leaving with medical needs · → 23-02 runways · → 06-04 fuel · → 14-01 security

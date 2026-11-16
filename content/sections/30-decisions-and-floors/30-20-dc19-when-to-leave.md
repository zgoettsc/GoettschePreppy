---
id: 30-20-dc19-when-to-leave
section: 30-decisions-and-floors
title: "DC-19. When to leave home: our triggers"
version: 1
revised: 2026-11-16
layer: card
danger_level: critical
phase: [A, B]
tags: [decision card, worksheet, evacuation, go no-go, triggers, leaving home, destination]
derived_from: [01-02-go-no-go-decision, 01-05-choosing-a-destination, 02-12-evacuation-medical-logistics]
sources:
  - american-red-cross-winter-storm-preparedness-and-bli-4bb6c0
  - noaa-national-weather-service-during-extremely-cold-9c1973
  - fema-ready-gov-create-your-family-emergency-communic-584e89
  - american-red-cross-power-outage-safety-6d07a8
related: [01-02-go-no-go-decision, 01-03-phase-b-movement, 01-05-choosing-a-destination, 01-06-phase-transition-checklists, 01-07-evacuating-with-medical-needs, 00-04-family-emergency-plan, 17-03-floods, 17-05-grassland-fire, 30-07-dc06-fuel-in-passenger-vehicle, 30-11-dc10-pets-when-you-cannot-keep-them]
cards: [DC-19, DC-06, DC-10]
explainers: [EX-10]
promote_when: [has.destinations]
card: DC-19
options:
  - id: worksheet
    label: "Write our own rule"
    summary: "The adults fill in the trigger table on this page with their own thresholds and destinations, agree it, sign and date it, and review it each year."
settings_summary: "This card has no multiple choice. Leaving home is the highest-stakes decision a household makes in a long emergency, and the one most often made badly: too late, in a panic, in bad weather, with children. Staying in a stocked, known home is usually safer than moving. Leaving into a storm or extreme cold kills people every winter, and the Red Cross and National Weather Service both say avoid travel in winter storms unless you must. But staying past the point where medicine, heat, water or safety runs out forces a move in the worst condition. The answer is thresholds written now, while calm, that turn a 3 a.m. judgement into a checklist. Fill in the trigger table on the page."
review_pass: null
---

# DC-19. When to leave home: our triggers

**What this page is for.** This card is a worksheet. It explains the two ways the leave-or-stay
decision goes wrong and gives the household a table to fill in with its own triggers. A
threshold agreed in advance is worth more than any judgement made at 3 a.m. in a cold house.

> **SAFETY.** If the house is on fire, collapsing, flooding or a wildfire is coming, leave now:
> that is not a threshold question (→ 17-03, → 17-05). Never run a generator, charcoal, or any
> engine indoors, in a garage, or near an open window (floor, → 30-01); people trapped in cars
> in snow die of this too.

> **Before the collapse:** if officials order an evacuation, follow it. The triggers below are
> for when no one is giving orders.

## 1. The thing, in plain words

**Sheltering in place** means staying at home and living off what you have (→ 01-01).
**Moving** means taking the household somewhere else, by vehicle or on foot (→ 01-03). A
**trigger** is a condition written in advance that means "start moving" or "start preparing to
move". A **destination** is a named place with shelter, heat and water, where someone expects
you (→ 01-05).

{{#if has.destinations}}Your destinations: {{#each destinations as d}}{{d.name}} ({{d.state_name}}, about {{d.approximate_miles}} miles, {{d.status_text}}); {{/each}}{{else}}You have not named a destination yet. "Out of town" is not a plan.{{/if}}

## 2. The rule as agencies state it, and why

- The Red Cross and the National Weather Service say stay off the roads in winter storms and
  extreme cold unless travel is necessary, and carry a winter car kit if you must go (Red Cross,
  Winter Storm Safety; NWS, During Extremely Cold Weather).
- FEMA asks every family to make a written plan in advance: where to meet, how to reach each
  other, where to go (FEMA/Ready.gov, Create Your Family Emergency Communication Plan).

**Why:** a stocked home you know how to heat is a strong position. A vehicle on a closed road
in a blizzard, with children, is a weak one. But a home without heat, water, medicine or safety
can become worse than the road, and the agencies cannot tell you where that line is for your
family.

## 3. How it actually hurts people

1. **Leaving when you should have stayed**: the family trades a stocked house for exposure,
   unknown roads and what fits in the car. A storm, a breakdown or an empty tank strands them.
   This is the more common mistake.
2. **Staying when you should have left**: the last fuel, insulin or water is used up, and the
   family has to move anyway, now with no fuel, no daylight, sick and weak.

Both happen because the decision is made in the moment, under fear and fatigue.

## 4. What makes it safer

**Removes much of the risk**
- **Write the triggers now** (below), agree them as adults, sign and date them.
- **Name a real destination** with someone expecting you, and a route (→ 01-05).

**Reduces it a lot**
- **Answer the four questions before moving**: Where exactly are we going? Is the route
  survivable right now (weather, fuel, daylight)? What happens when we arrive? Is it truly better
  than staying? If any answer is weak, stay and fix that answer.
- **Weather first, daylight second**: do not depart into a storm or extreme cold unless the house
  is actively unsafe; leave in the morning.
- **Once decided, go early**, with fuel in the tank and people still strong.
- **Medical triggers point toward care**, not away from it: if a life-sustaining medicine is
  running out, the move may be toward a town or hospital, not the countryside.

**Reduces it a little**
- Keep the vehicle fuelled above half and the go-bags packed (→ 22-03).
- Practise the load once (→ 01-06).

## 5. The worksheet: our triggers

Fill in each row. Leave none blank: write "not applicable" if it truly is.

| Trigger | Our threshold (start preparing / move) | Go where |
|---|---|---|
| Life-sustaining medicine remaining (each one) | ______ days / ______ days | ______________ |
| Emergency medicine (e.g. epinephrine devices) remaining | ______ / ______ | ______________ |
| Heating fuel remaining, winter | ______ days / ______ days | ______________ |
| Safe drinking water we can produce per day | below ______ gal | ______________ |
| Food remaining (including any special-diet food) | ______ days / ______ days | ______________ |
| House unsafe (fire, structure, flood) | immediately | ______________ |
| Security threat we cannot manage | __________________ | ______________ |
| Neighbourhood (fire spreading, mass departure, utilities gone for good) | __________________ | ______________ |
| Medical emergency we cannot treat | __________________ | ______________ |
| Other: __________________ | __________________ | ______________ |

Your household's medicines, for the first row: {{#each meds as m}}{{m.member}}: {{m.name}}; {{else}}none entered.{{/each}}

Weather rule (when we will not depart): _______________________________________________

Who decides if the adults are apart: ___________________________________________________

If we split up, we meet at: {{ contacts.meet.out_of_town }}

Signed: ______________________ ______________________ Date: __________ Reviewed: __________

## 6. Our choice

{{card DC-19}}

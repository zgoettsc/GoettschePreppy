---
id: 23-01-depletion-framework
section: 23-depletion-and-substitution
title: "The depletion framework"
version: 1
revised: 2026-11-16
layer: core
danger_level: caution
phase: [A, B, C]
tags: [depletion, planning, runway, rationing, substitution, framework, shortest clock]
derived_from: [23-01-depletion-framework]
sources:
  - cdc-how-to-create-and-store-an-emergency-water-suppl-f0c412
  - us-fda-information-regarding-insulin-storage-and-swi-6448d3
  - american-red-cross-power-outage-safety-6d07a8
  - university-of-missouri-extension-wood-fuel-for-heati-b63761
related: [23-02-master-consumables-table, 23-03-substitution-catalog, 23-04-resource-lifecycles, 23-05-skills-that-replace-supplies, 01-02-go-no-go-decision, 12-11-chronic-conditions, 12-07-meds-stockpile, 21-04-routine-and-structure, 22-04-household-inventory, 30-20-dc19-when-to-leave]
cards: [DC-19]
explainers: [EX-07, EX-13]
promote_when: []
photo_slots: []
figures: [fig-three-classes-of-consumable]
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: null
---

# The depletion framework

**What this page is for.** Everything you stock runs out, and each thing runs out at its own
speed. Planners call the number of days a supply will last its **runway** (think of a
plane running out of runway). This page gives you four questions to ask about every supply,
sorts supplies into three classes, and shows how to find the one that runs out first. **The
supply that runs out first sets your household's timeline.** The worksheet where you write the
numbers is → 23-02.

## Do this now

1. **Fill in the master consumables table** (→ 23-02). It takes an afternoon with a notebook,
   a measuring cup and a scale.
2. **Work out each prescription medicine's runway first** (→ 12-07) and write today's date
   next to it. For most households with a daily medicine, that is the shortest clock.
3. **Put a weekly check on the household routine** (→ 21-04) so the numbers stay true. A
   runway worked out once and never updated is a number you will misremember.
4. **Decide now, calmly, at what runway you act.** When to leave home is a household decision
   (→ 01-02). {{choice DC-19}} → 30-20

## The four questions for every supply

Every "When it runs out" block in this binder answers these four.

**1. Runway: how long does it last?**
- Amount on hand divided by real daily use. **Measure the use, do not guess it.** Most
  households are well off on their real consumption until they measure it.
- Use the hard case: winter wood use, summer water use, water use when someone is sick
  (→ 12-05). Not the average.
- Write the date. A runway shrinks every day.

**2. Ration: how do you stretch it?**
- What is the least that keeps the job done, rather than comfortable?
- What gets cut first, second and third. Decide it in advance, in writing.
- What is never rationed (see the rules below).

**3. Resupply: where does more come from?**
- Make or grow it (garden → 05-01, wood → 06-04, rain and snow → 03-05).
- Find it (→ 22-02).
- Trade for it (→ 18-02).
- **Or it cannot be resupplied.** Write that down plainly. It is the important case.

**4. Substitute: what does the job instead?**
- A different material, a different method, or a skill that replaces the supply (→ 23-05).
- **Or nothing does.** Name it (→ 23-03).

## The three classes of supply

Sorting every supply into one of three classes is the key move, because each class needs a
different kind of plan.

{{figure fig-three-classes-of-consumable}}

| Class | What it means | Examples | The plan |
|---|---|---|---|
| **A. Renewable** | You can make or gather more for as long as you need | Water (→ 03-05), wood (→ 06-04), garden food (→ 05-01), soap (→ 13-09), cordage (→ 16-03), fat lamps (→ 10-04) | **Build the ability to produce it.** How much you can make matters more than how much you hold |
| **B. Substitutable** | It runs out, but something else does the job | Batteries → daylight; gauze → boiled cloth (→ 12-02); tape → wire (→ 16-05); screws → lashings (→ 16-03) | **Stock it deeply and learn the substitute** |
| **C. Irreplaceable** | No way to make it, nothing replaces it, no local resupply | Prescription medicines the body depends on (insulin → 02-01, epinephrine → 02-03, seizure and heart medicines → 12-11), infant formula for a baby who is not breastfed (→ 20-05), supplies for medical devices | **The runway is the plan.** It drives the go/no-go decision (→ 01-02) |

**Class C is short, and it decides everything.** A household can be well prepared in classes
A and B and still have its whole timeline set by one item in class C.

### Your household's class C items

These come from your settings. Add anything missing by hand.

{{#each meds as m}}- **{{m.name}}** {{m.strength}} for {{m.member}}: about {{m.days_on_hand}} days on hand (from your settings; recount from the boxes).
{{else}}- No medicines are entered in settings. If anyone takes a daily prescription, add it in settings or here: ______________________ days on hand: ______
{{/each}}
{{#if has.infant}}- Infant formula, if the baby is not fully breastfed (→ 20-05). There is no safe homemade formula.
{{/if}}{{#if has.oxygen}}- Oxygen: cylinders and concentrator power (→ 02-08, → 09-10).
{{/if}}{{#if has.cpap}}- CPAP power and parts (→ 02-24, → 09-10).
{{/if}}{{#if has.condition.CL-02}}- Pump and sensor supplies (→ 02-02).
{{/if}}{{#if has.epinephrine}}- Epinephrine auto-injectors: their clock is the expiry date, not daily use (→ 02-03).
{{/if}}

## The clocks, in a typical order

The order matters more than the numbers. Your own numbers go in → 23-02.

| Clock | Class | Typical runway | Notes |
|---|---|---|---|
| **Daily prescription medicines** (→ 12-07) | **C** | **Whatever you hold** | **For most households with one, this is the governing clock** |
| **Epinephrine** (→ 02-03) | **C** | Until it expires | Cannot be made; it expires |
| Phone and medical-device batteries (→ 09-06) | B | Days | Charging plan and manual backups |
| Stored water (→ 03-02) | A | Days | Renewable: rain, snow, treatment (→ 03-04) |
| Refrigerated food (→ 04-17) | B | Hours to days | Winter outdoor cold substitutes for free (→ 04-09) |
| Generator fuel (→ 09-04) | B | Days to weeks | Solar substitutes (→ 09-02) |
| **Wood**, if it is your only heat (→ 06-04) | A | **Weeks** | Renewable but hard work; the winter clock |
| Batteries (→ 09-07) | B | Weeks | Solar plus rechargeables makes them renewable |
| Stored food (→ 04-01) | A/B | Months | Renewable through → 05-01 and → 05-07, slowly |
| First-aid supplies (→ 12-01) | B | Varies | Clean cloth and cleanliness substitute (→ 12-02) |
| Diapers (→ 13-08) | B | Days to weeks | Cloth substitutes; **the child also outgrows them** |
| Screws, wire, thread (→ 16-07, → 16-04) | B | Long | Plentiful to salvage (→ 22-02) |
| Skills (→ 23-05) | none | **Never runs out** | **Gets better with use** |

**Read the first row and the last row together.** The shortest clock is usually something
you have to buy, and the longest is something you know.

## Working it out honestly: the common mistakes

- **Using label or planning figures instead of measured ones.** Measure real use: power
  (→ 09-01), water (→ 03-01), wood (→ 06-04).
- **Averaging the seasons.** A plan built on yearly averages fails at both ends. It is the
  same mistake as sizing solar on yearly sun (→ 09-05) or water on spring conditions (→ 17-07).
- **Forgetting the spikes.** Illness raises water use (→ 12-05); a storm raises wood use
  (→ 17-01); heat raises water use (→ 11-08).
- **Counting the whole stock as usable.** Some of it is hard to reach, spoiled or held back as
  a reserve. Do not count the reserve you will not touch.
- **Ignoring the work.** A renewable supply you are too hurt or tired to produce is not
  renewable that week (→ 12-09, → 21-02).

## Rationing: the general rules

Every "When it runs out" block in this binder uses these.

1. **Ration by function, not comfort.** Keep what keeps you able to work and stay well; cut
   what is only pleasant. Rule 5 is the exception.
2. **Cut the biggest user first** where you can. Usually it is a comfort use.
3. **Never ration** drinking water (→ 03-01), handwashing (→ 13-02), prescribed medicine
   (→ 12-11), children's food (→ 20-01) or sleep (→ 21-07). Each costs far more than it saves.
   **Stretching a prescription by skipping or cutting doses is not a household decision**: talk
   to the prescriber now about what to do if supply is cut off (→ 12-07).
4. **Protect the class C items absolutely.** Everything else can be bargained.
5. **Do not ration morale to zero** (→ 21-06). A household that saves every pleasure for a
   worse day finds that every day is the worse day.
6. **Decide the order of cuts in advance**, in writing, so it is not an argument (→ 21-05).

## What you need

| Item | Why | Where |
|---|---|---|
| **The filled-in master consumables table** | The thing this section exists to produce | → 23-02 |
| A notebook for the weekly check | Runways shrink; numbers must be current | → 21-04, → 25-05 |
| **Measuring tools**: a plug-in watt meter, a marked jug, a kitchen or bathroom scale | Measured beats estimated, every time (→ 29-13) | → 09-01, → 03-01 |
| The household inventory | You cannot work out a runway on an unknown stock | → 22-04 |
| **Written action points** | So the leave-or-stay decision is calm and decided ahead | → 01-02 |
| Calendar reminders for expiry dates | Medicines, batteries, food, epinephrine | → 25-10 |

No money? The framework is free: four questions, a notebook and an afternoon. Estimate where
you cannot measure, but measure the important ones: water, power, wood and medicine.

## When it runs out

- **The framework does not run out; the habit of keeping it does.** Keep the weekly check on
  the routine (→ 21-04).
- **The decision point.** When the shortest clock nears the action point you set in advance,
  go to → 01-02. **Set it early so you act while you still have fuel, roads, daylight and
  choices.** A decision made at the last dose is made with nothing left to carry it out.
- **The direction to push.** Over time, move supplies from class C to B to A: build
  production, learn substitutes, gain skills (→ 23-04, → 23-05). Some prescription medicines
  can never move. Almost everything else can.
- **What this means for the whole plan.** If your timeline is set by a bought medicine, the
  most valuable preparations are: building that supply through legitimate means while
  pharmacies work (→ 12-07); making the decision early (→ 01-02); and building the community
  and skills that make everything else survivable in the meantime (→ 18-01, → 23-05).

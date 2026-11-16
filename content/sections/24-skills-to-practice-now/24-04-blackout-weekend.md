---
id: 24-04-blackout-weekend
section: 24-skills-to-practice-now
title: "Running a blackout weekend"
version: 2
revised: 2026-11-16
layer: core
danger_level: caution
phase: [A, B, C]
tags: [blackout, exercise, practice, outage, measurement, debrief, children, carbon monoxide]
derived_from: [24-04-blackout-weekend]
sources:
  - cdc-carbon-monoxide-poisoning-basics-772153
  - american-red-cross-power-outage-safety-6d07a8
  - foodsafety-gov-usda-hhs-food-safety-during-a-power-o-3894c1
  - us-fda-information-regarding-insulin-storage-and-swi-6448d3
  - us-epa-emergency-disinfection-of-drinking-water-6aa91f
related: [24-01-skills-checklist, 24-02-drills, 24-03-seasonal-practice-plan, 09-01-power-priorities, 09-10-power-for-medical, 08-01-heating-one-room, 08-02-carbon-monoxide-safety, 04-17-food-safety-power-outage, 22-04-household-inventory, 22-07-priority-purchase-order, 23-02-master-consumables-table, 20-08-kids-and-fear, 21-04-routine-and-structure, 30-01-the-floors, 30-02-dc01-unvented-heater-overnight, 30-21-dc20-open-flame-indoors]
cards: [DC-01, DC-02, DC-20]
explainers: [EX-02, EX-03, EX-04, EX-07]
promote_when: []
photo_slots:
  - { id: breaker-labels, caption: "Our breaker panel, labelled, with the circuits that stay on during the exercise marked" }
figures: []
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: { date: "2026-11-16", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "FoodSafety.gov 4 h / 48 h / 24 h and CDC 20 ft verified; 'three times as long' removed." }
---

# Running a blackout weekend

**What this page is for.** The most valuable exercise in this binder. Forty-eight hours with the
main breaker off finds more real gaps than a lot of money spent on gear or a year of reading,
and it finds them while the fix is a trip to the hardware store. This page gives four levels,
from one evening to a winter weekend, the safety limits, a schedule, and the measurements that
make the rest of the binder's numbers real.

> **Caution: the exercise has hard limits.** Three things are **never** part of the test:
> **medical devices stay powered**, **medicines that need cold stay cold**, and **the ability
> to call 911 or end the exercise at once stays available.** Everything else can go dark.
> **A working, tested battery carbon monoxide alarm is required.** **Never run a generator,
> charcoal, or any engine indoors, in a garage, or near an open window.**

{{#if has.refrigerated_meds}}> **Medicine first, breakers second.** Your household has refrigerated medicine
> ({{#each refrigerated_meds as r}}{{r.name}} for {{r.member}}; {{/each}}). Before any breaker goes
> off, do **one** of these: **(a)** leave the fridge's circuit on (find and label that breaker
> now), or **(b)** set up the real outage method first: the medicine cooler running on battery,
> a thermometer inside showing the label's temperature range, and only then move the medicine
> (→ 09-10, → 12-21, → 29-07). Medicine left in a dark fridge for 48 hours may be pushed onto its
> label's room-temperature time limit (FDA, Information Regarding Insulin Storage and Switching
> Between Products in an Emergency). **A frozen-then-thawed insulin vial or pen is discarded.**
{{/if}}

{{photo breaker-labels}}

## Do this now

1. **Pick a date and put it on the calendar**: spring and autumn (→ 24-03). A date on a calendar
   is the only version of this that ever happens.
2. **Tell the household a week ahead**{{#if has.child}}, children included, and **call it an
   adventure** (→ 20-08){{/if}}. Announced, not sprung.
3. **Do the first one in mild weather.** Winter versions come later and teach the most.
4. **Print the debrief worksheet below** (or keep it open) for the whole weekend.

## What you are actually testing

Not "can we survive". You can; it is 48 hours. You are testing **whether this binder's plan
fits the house you actually live in**:
1. **Do the systems work?** Not in theory: the actual filter, stove, panel, bucket toilet.
2. **What do we reach for that is not there?** This list is always longer than you expect, and
   it is the main result of the weekend.
3. **How much do we really use?** Water per person per day, fuel per meal, battery per evening.
   **These numbers make → 23-02 real**; everything before them is a guess.
4. {{#if has.child}}**How do the children cope?** A young child's tolerance for dark and boredom is a real planning
   number (→ 20-08, → 21-04).{{else}}**How do the adults cope** with dark, cold and boredom (→ 21-02)?{{/if}}
5. **What breaks first, the equipment or the mood?** Usually the mood, which is why Section 21
   is in this binder.

## The safety limits: read these twice

| Never part of the test | Why |
|---|---|
| **Medical device power**{{#if has.cpap}} (CPAP){{/if}}{{#if has.oxygen}} (oxygen){{/if}}{{#if has.condition.CL-02}} (pump, sensor, phone){{/if}} | You may **measure** the battery drain, but the devices stay powered. Do not test them by doing without (→ 09-10) |
| **Medicines that need cold** | Correctly stored the whole time (FDA): fridge circuit left on, or the battery cooler running and checked before the main goes off |
| **Epinephrine**{{#if !has.epinephrine}} (if anyone carries it){{/if}} | In place, in date, findable, always |
| **The phone and 911** | One charged phone stays available all the time |
| **Ending the exercise** | Anyone can call it off, for any reason, without argument. Especially a child |

| Absolute rules |
|---|
| **Battery carbon monoxide alarms, tested**: one where people sleep and one on every level ({{ gear.co_alarms }} in settings), installed and tested **before** any fuel-burning heater is lit (→ 08-02) |
| **Indoor heat only from an appliance rated for indoor use**, run exactly by its manual and its page (→ 08-10, → 08-09, → 08-08), with the alarm up first and the fresh-air openings the manual gives. Never two fuel heaters in one room. **Never indoors, under any circumstances:** camp stove, grill, generator, charcoal |
| **Overnight heat** is a household decision: {{choice DC-01}} → 30-02. A propane cylinder larger than 1 lb indoors: {{choice DC-02}} → 30-03. **Anyone waking with a headache or feeling sick = everyone out**, then call (→ 29-03) |
| **Candles and open flame indoors:** {{choice DC-20}} → 30-21. Battery lights are safer (→ 10-01) |
| **Generators outdoors only**, at least 20 feet from windows and doors, never in a garage (CDC; → 09-04) |
| **Cooking happens outdoors** (fire, rocket stove, camp stove) or on an appliance made for indoor use (→ 07-01) |
| **Do not let the pipes freeze.** In cold weather keep the house above freezing, or shut off and drain the water (→ 17-01, → 08-03) |
| **Food safety is real, not simulated:** a closed fridge keeps food safe about 4 hours; a full closed freezer about 48 hours, a half-full one about 24 (FoodSafety.gov, Food Safety During a Power Outage; → 04-17) |
| **Do not drive anywhere for supplies.** If you must, the exercise is over: write down why |

## Level 1: an evening blackout (start here)

**Four to six hours, one evening.** Switch off every breaker except any circuit that must stay
on (above). Cook, light the house, do dishes, do bedtime. **Turn the power back on before bed the
first time.**
*What it usually finds:* flashlights with dead batteries, matches nobody can find, an electric
can opener, bedtime in the dark harder than expected{{#if has.young_child}}, and a small child who
thinks it is the best night of the year{{/if}}.

## Level 2: a 24-hour blackout

**Friday evening to Saturday evening.** One full night and three meals.
*What it usually finds:* charging is the bottleneck, water is heavier than you think, cooking
takes far longer, and nobody planned lunch.

## Level 3: a full weekend, water off too

**48 hours, breakers off, main water valve off.** This is the real exercise.
{{#if has.refrigerated_meds}}Level 3 is the right weekend to do the medicine-cooler option (b) for real.{{/if}}
*What it usually finds:* your real water use (almost always higher than the planning figure of
{{ derived.water.plan_gal_day }} gal a day), that washing dishes and laundry by hand is a job
(→ 13-04), that the bucket toilet works but the cover material runs out, and that the shortest
runway in the house is not the one you assumed.

## Level 4: a winter weekend

**Only after levels 1 to 3 have gone well, and with a plan for stopping.** One room heated,
everything else cold. {{#if has.gas_any}}With the breakers off, most gas furnaces do not run: their fan and controls need
power.{{/if}} "One room heated" means the warm-room plan on → 08-01, with your heat source
run exactly by its page. **Watch the pipes, watch the CO alarm, watch the
{{#if has.child}}children{{else}}people{{/if}}.** Drill 8's practice lights (→ 24-02) get their first
overnight here.
*What it usually finds:* how much fuel a night really costs (→ 23-02){{#if has.child}}, that keeping
children warm is a full-time job (→ 11-02){{/if}}, that batteries die fast in cold (→ 09-05), and
that the one-room plan needs adjusting to your actual house.{{#if !is.cold_winters}} Where winters are
mild, run Level 4 in your hottest week instead: no air conditioning, and watch for heat illness
(→ 11-08, → 17-04).{{/if}}

## The schedule for a level 3 weekend

| When | Do |
|---|---|
| **The week before** | Tell everyone. Fill water containers. **Install and test the CO alarms** (→ 08-02). Lay out the gear. Plan meals. Charge the medical power banks and every power station to full. **Find and label every breaker**, especially any that stays on |
| **Friday, 5 p.m.** | {{#if has.refrigerated_meds}}**Medicine step first:** fridge breaker confirmed on and labelled, or the cooler running, thermometer reading in range, medicine moved. **Do not touch the panel until this is done.**{{else}}Medical devices on battery and charged; phones charged.{{/if}} |
| **Friday, 6 p.m.** | **Breakers off** (except any circuit you decided stays on). **Water main off.** Write down the time and the meter readings if you can |
| **Friday evening** | Cook dinner off-grid. Light the house. Bedtime by lamplight. **Log everything used** |
| **Saturday morning** | Breakfast. A water-treatment run (EPA, Emergency Disinfection of Drinking Water). Bucket toilet in service. {{#if has.child}}Children's jobs given out (→ 20-07){{else}}Jobs shared out{{/if}} |
| **Saturday midday** | A normal day: {{#if has.child}}schoolwork (→ 20-03), {{/if}}chores, laundry by hand, a walk. **Measure the solar output**{{#if !has.solar}} if you have panels{{/if}} |
| **Saturday afternoon** | Practise one skill from → 24-01: fire in bad conditions, sharpening, sewing |
| **Saturday evening** | Cook, eat, and **make the evening good**: a game, a story, something that turns it into a good memory (→ 21-06) |
| **Sunday morning** | Breakfast. **Read the numbers**: water, fuel, battery used |
| **Sunday midday** | **Debrief while it is fresh.** Fill in the worksheet. Restore power and water |
| **Sunday afternoon** | **Fix the top three findings the same day**, while they are vivid |

## The measurements: the real result

Write these down; they replace guesses on → 23-02 with facts.

```
WATER used, total: ______ gal  ÷ {{ household.size }} people ÷ 2 days = ______ gal/person/day
   (compare with the planning figure on 03-01: ______)
FUEL or WOOD burned: ______   meals cooked: ______   per meal: ______
BATTERY / SOLAR: started ____ %  ended ____ %   solar produced: ______ Wh
MEDICAL device battery drain: ______ % over ____ hours → projected runtime: ______ h
LIGHT: hours of lamp use ______   fuel or battery used ______
FOOD: meals cooked ____   eaten versus planned: ______
TIME: hours spent on water, cooking, heating, sanitation: ______  <- the real finding
```

**The last line is the one nobody expects.** Living without the grid is a full-time job before
anything productive happens, and knowing your number changes how you plan phase C.

## The debrief worksheet

```
DATE: __________  LEVEL: ____  WEATHER: ______________  LENGTH: ______

THINGS THAT DID NOT WORK
1. ______________________________  fix: ______________________
2. ______________________________  fix: ______________________
3. ______________________________  fix: ______________________

THINGS WE REACHED FOR AND DID NOT HAVE
1. ______________  2. ______________  3. ______________  4. ______________

WHAT SURPRISED US
______________________________________________________________________

HARDEST PART (be honest: it is usually not the gear)
______________________________________________________________________

CHILDREN'S EXPERIENCE (what worked / what to change)
______________________________________________________________________

BINDER PAGES TO UPDATE
______  ______  ______  ______

BUY THIS WEEK (add to 22-07)
1. ______________  2. ______________  3. ______________

NEXT BLACKOUT WEEKEND: __________  LEVEL: ____
```

## Making it good for {{#if has.child}}the children{{else}}everyone{{/if}}

{{#if has.child}}The exercise **fails** if the children come out of it frightened, and it **succeeds beyond its
purpose** if they come out thinking blackouts are fun.
- **Call it camping.** It is.
- **Give each child a real job**: carrying the lamp, counting the water jugs{{#if has.pets}}, feeding the pets{{/if}} (→ 20-07).
- **Keep bedtimes and mealtimes normal.** Routine keeps children steady (→ 21-04, → 20-03).
- **Plan one deliberately great thing**: a fire, a Dutch-oven dessert, shadow puppets, everyone
  sleeping in one room (→ 21-06).
{{#if has.infant}}- **Babies just need warmth, feeding, sleep and clean diapers on the usual schedule.** If any of
  that is at risk, end the exercise. That is not a failure; it is the finding (→ 20-01).
{{/if}}- **In a winter weekend, watch the children for cold all the time** (→ 11-02, → 08-05).
{{else}}- **Plan one deliberately good thing** each evening: a fire, a good meal, a game (→ 21-06).
- **Keep normal mealtimes and bedtimes** (→ 21-04).
{{/if}}{{#if has.elder}}- **Older adults** feel cold and heat sooner and may hide it. Check on them on a schedule, and
  end the exercise if they are struggling (→ 02-21, → 08-05).
{{/if}}

## The most common findings (you will probably hit these)

1. **Charging is the bottleneck**, not lighting.
2. **Water is heavy**, and moving it is most of the work.
3. **Cooking takes about three times longer** and uses more fuel than expected.
4. **Nobody planned lunch.** Or the dishes. Or where the wash water goes.
5. **The bucket toilet works; the cover material runs out.**
6. **Sleep gets worse**, and everything is harder because of it (→ 21-07).
7. **The evenings are long.** Boredom, not danger, is the mood problem (→ 21-02).
8. **The house is colder or hotter than you assumed** without heating or cooling.

## What you need

Nothing new: **that is the point.** Use exactly what you own. The list of things to buy is a
**result** of the weekend, and it goes on → 22-07. Two things worth having first: **battery CO
alarms, installed**, and **a way to measure** (a bucket marked in gallons, a kitchen scale, a
battery monitor or a cheap plug-in watt meter, a fridge thermometer).

No money? Improvise during the weekend and **write down what you improvised**. That is the most
valuable page of notes you will make all year, and it feeds → 23-03.

## When it runs out

The exercise ends after 48 hours by design. What runs out is **how long the findings stay
true**:
- **Runway:** about a year. {{#if has.child}}Children grow, {{/if}}gear changes, the house changes.
- **Ration:** if a full weekend is impossible, **do a level 1 evening.** About a quarter of the
  value for a small part of the effort, and far better than nothing.
- **Resupply:** twice a year (→ 24-03).
- **Substitute:** none. Every other page in this binder is theory until this weekend tests it.

## By phase

- **A, at home:** this rehearses the most likely emergency: a multi-day outage at home
  {{#if is.cold_winters}}in winter {{/if}}is not a hypothetical in {{ home.state_name }}.
- **B, moving:** add a travel version: do the grab (→ 22-03), load the vehicle, drive an hour of
  the route, and camp out of the vehicle overnight (→ 22-05, → 01-03).
- **C, establishing:** a blackout weekend is a **preview of ordinary life** somewhere rural. If 48
  hours is miserable, list what would make it bearable: that list is your phase C build order
  (→ 01-04, → 23-04).

---
id: 00-02-emergency-quick-reference
section: 00-front-matter
title: "Emergency quick reference"
version: 1
revised: 2026-11-16
layer: household
danger_level: caution
phase: [A, B, C]
tags: [emergency, quick reference, triage, anaphylaxis, bleeding, CPR, carbon monoxide, poison control, "911", tornado]
derived_from: [00-02-emergency-quick-reference]
sources:
  - cdc-recognizing-and-responding-to-anaphylaxis-645825
  - cdc-carbon-monoxide-poisoning-basics-772153
  - cdc-diabetic-ketoacidosis-55a7c2
  - noaa-national-weather-service-tornado-safety-ba75e0
  - american-red-cross-winter-storm-preparedness-and-bli-4bb6c0
  - noaa-national-weather-service-flood-safety-c02f3a
  - national-capital-poison-center-poison-control-1-800-e428c9
  - 988-suicide-and-crisis-lifeline-samhsa-988-suicide-a-5f45b0
  - us-fda-information-regarding-insulin-storage-and-swi-6448d3
related: [00-06-first-60-minutes, 25-08-quick-reference-cards, 25-03-regional-contacts, 12-02-bleeding-and-wounds, 12-18-choking-and-cpr, 08-02-carbon-monoxide-safety, 17-02-tornadoes, 17-06-tornado-shelter, 02-03-cl03-anaphylaxis, 12-17-poisoning-and-ingestion, 09-16-outage-day-one, 01-02-go-no-go-decision]
cards: [DC-01, DC-08, DC-25]
explainers: [EX-03, EX-07]
promote_when: []
photo_slots: []
figures: []
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: null
---

# Emergency quick reference

> **Find the row. Do the first action. Then go to the page.**
> This page gets you to the right page in under ten seconds. **The first action in each row is
> the one that must happen before you read anything.** For the first hour of a general emergency,
> use → 00-06 instead.
>
> **If phones are dead, every "call 911" below is replaced by the "No 911" action in the same
> row.** The first actions do not change; only the second half of the plan does. Decide now who
> runs to the neighbour with medical training (→ 18-01, → 25-03).

## Who in this household needs what

| Person | Role | Age | Conditions |
|---|---|---|---|
{{#each members as m}}| {{m.label}} | {{m.role}} | {{m.age_text}} | {{m.conditions}} |
{{/each}}

**Allergies:** {{#each allergies as a}}{{a.member}}: {{a.allergen}} ({{a.severity}}) · {{else}}none entered{{/each}}

**Medicines and what to do if doses are missed** are on → 25-09 and each condition's page in
Section 02. **Epinephrine is kept:** __________________________ **Glucagon or other rescue
medicine is kept:** __________________________

## Life-threatening: act before you read anything else

| If this is happening | Do this first | Then go to |
|---|---|---|
| **Anaphylaxis** (throat tightening, trouble breathing, swelling of lips or tongue, hives over the body, repeated vomiting, collapse, often minutes after a food, sting or medicine) | **EPINEPHRINE INTO THE OUTER THIGH, NOW.** Then call 911. **A second dose 5 to 15 minutes later if not improving** (CDC, Recognizing and Responding to Anaphylaxis). Antihistamines are not a treatment. *No 911: lie them down (on their side if vomiting), keep watching for hours* | → 02-03 |
| **Severe bleeding** | **Hard direct pressure.** Life-threatening limb bleed: **tourniquet 2 to 3 inches above the wound (never over a joint), tight until the bleeding stops, write the time. Never loosen it while help can still come.** *No help will ever come: the conversion decision is DC-25 (→ 30-26)* | → 12-02 |
| **Not breathing, no pulse** | **CPR. Call 911.** *No 911: CPR is unchanged; → 12-18 is the memory aid, → 12-16 the hard calls* | → 12-18 |
| **CO alarm, or several people with headache, nausea or dizziness at once** | **EVERYONE OUTSIDE. CALL 911. DO NOT GO BACK IN.** Turn a heater off only if it is within arm's reach on the way out. *No 911: fresh air is the treatment; rest outside for hours; find and stop the source, then air the house out before anyone goes back in* | → 08-02 |
| **Severe low blood sugar** (someone with diabetes is unconscious, seizing or cannot swallow) | **NOTHING BY MOUTH. Glucagon if they have it. Call 911.** *No 911: on their side; fast sugar once awake and able to swallow; recheck every 15 minutes* | → 02-01, → 02-05 |
| **High blood sugar with ketones, vomiting, belly pain, fruity breath or fast deep breathing** | **This may be DKA (diabetic ketoacidosis). Fluids. Get medical help** (CDC, Diabetic Ketoacidosis). *No 911: sick-day rules on the condition page; insulin is never stopped* | → 02-01, → 02-02 |
| **Choking** | **Coughing: let them cough. Silent: act.** Under 1 year: back blows and chest thrusts. 1 year and older: abdominal thrusts. *Goes limp: CPR* | → 12-18 |
| **Fire in the house** | **OUT. STAY OUT. Meeting place. Call 911.** *No 911: fight it only while it is smaller than a trash can and your exit is behind you; past that, the house is lost, people are not* | → 29-12, → 24-02 |
| **Poisoning, swallowed something** | **Poison Control 1-800-222-1222** (America's Poison Centers). *No phone: do not make them vomit, keep the container, follow the label's first-aid statement* | → 12-17 |
| **Gas smell in the house** | **OUT. No light switches, no flames, no phones inside.** Call the gas emergency number from outside: {{ contacts.utility.gas.phone }}{{#if has.gas_any}} ({{ contacts.utility.gas.provider }}){{/if}}. Shut the gas at the meter only if you know how. If a propane heater was running from an outdoor tank, close the tank valve outside. Air the house out before anything is relit | → 08-02, → 17-08 |
| **Tornado warning** | **Lowest floor, innermost room, no windows, cover heads.** Our spot: {{ dwelling.shelter_room }}{{#if has.mobile_home}}. **A mobile home is not a shelter: leave for a sturdy building before the storm** (NWS, Tornado Safety){{/if}} | → 17-02, → 17-06 |
| **Suicidal crisis** | **Stay with them. Call or text 988.** *No phone: never leave them alone, remove the means, get them through tonight* | → 12-15, → 21-03 |

## Urgent: minutes to hours

| Situation | First action | Page |
|---|---|---|
| **A medical device fails** (pump, oxygen concentrator, CPAP, monitor) | Go to the written backup plan on that condition's page | Section 02, → 09-06 |
| **Refrigerated medicine froze** | **A frozen-then-thawed insulin vial or pen is discarded**, even once, even if it looks normal: it loses strength with no way to tell (FDA, Insulin Storage in an Emergency). For other refrigerated medicines, follow the label (→ 29-07) | → 29-07, → 12-21 |
| **Refrigerated medicine got too warm** | Get it cool now (→ 12-21). Whether to use it past its published window is a household choice. **Our choice:** {{choice DC-08}} (→ 30-09) | → 30-09 |
| **Hypothermia** (shivering stops, confusion, clumsiness) | Get them dry, insulated and warmed gradually. **Handle gently** | → 08-05 |
| **Frostbite** | Do not rub. Rewarm only if it will not refreeze | → 08-05 |
| **Serious burn** | Cool with clean water. Cover. No ice | → 12-03 |
| **Broken bone, bad fall** | Keep it still. Check the circulation beyond the injury | → 12-09 |
| **Hit their head** | **Start the head-injury watch**; the red flags decide everything | → 12-19 |
| **Deep or dirty wound** | Wash it out thoroughly, dress it, **check for infection daily** | → 12-04, → 12-14 |
| **Dehydration, especially a child** | **Oral rehydration solution**, small sips, often | → 12-05 |
| **Stranded in a vehicle** | **STAY WITH IT.** Clear snow from the exhaust pipe before running the engine | → 22-05, → 01-03 |
| **Flooding** | **Never drive or walk through floodwater.** Go to high ground (NWS, Flood Safety) | → 17-03 |
| **Someone at the door, a confrontation** | **Calm voice, distance, doors** | → 14-13, → 14-02 |

## System failures: hours to days

| Situation | First action | Page |
|---|---|---|
| **Power is out** | **Run outage day one.** Fill water containers now; fridge and freezer stay shut; medical devices first on any battery | → 09-16, → 00-06 |
| **Water is off or unsafe** | Use stored water; treat everything else. Know the water-heater and pipe reserves | → 03-02, → 03-04 |
| **We need heat, power out in winter** | **One warm room. CO alarm installed and tested BEFORE any fuel-burning heater is lit.** Only heaters rated for indoor use. Heat while people sleep is a household choice. **Our choice:** {{choice DC-01}} (→ 30-02) | → 08-01, → 08-04, → 08-02 |
| **No way to cook** | Fire, grill or camp stove **outdoors only** | → 07-01, → 07-02, → 07-05 |
| **Toilets do not work** | **Bucket toilet.** Stop flushing with drinking water | → 13-01 |
| **Freezer thawing** | Cook or preserve the contents, most perishable first | → 04-17, → 04-06 |
| **Fuel or wood running low** | Burn less first, then other fuels | → 06-04, → 06-05 |
| **Phones and internet down** | Weather radio, handheld radios, the written comms plan | → 15-01, → 15-03 |
| **A medicine or medical supply is running out** | **This is a reason to consider leaving, not just a rationing problem** | → 01-02, → 01-07 |

## Weather: this region

Your home county's hazards and their ratings, from the region data (Section 32):

| Hazard | Rating | Page |
|---|---|---|
{{#each region.home.hazards as h}}| {{h.name}} | {{h.rating_text}} | Section 17 |
{{/each}}

| Event | First action | Page |
|---|---|---|
| **Blizzard, extreme cold** | Stay put. One room. **Do not travel** (American Red Cross, Winter Storm Safety) | → 17-01, → 08-01 |
| **Tornado** | {{ dwelling.shelter_room }}, cover heads | → 17-02, → 17-06 |
| **Flood** | High ground. Never drive through water | → 17-03 |
| **Extreme heat** | Shade, fluids, cool cloths; watch children, elders and heat-sensitive medicines | → 17-04 |
| **Wildfire, grass fire** | Leave early. Do not wait to see | → 17-05 |
| **Long grid failure** | → 00-06, then Phase A | → 17-08, → 01-01 |
| **Illness outbreak** | Handwashing, distance, separate the sick | → 17-09, → 13-11 |

## Numbers

| Who | Number |
|---|---|
| **Emergency** | 911 |
| **Poison Control** | 1-800-222-1222 |
| **Suicide and crisis line** | 988 (call or text) |
| **Out-of-area contact**: {{ contacts.out_of_area.name }} | {{ contacts.out_of_area.phone }} |
| **Electric outages**: {{ contacts.utility.electric.provider }} | {{ contacts.utility.electric.phone }} |
| **Gas emergency**: {{ contacts.utility.gas.provider }} | {{ contacts.utility.gas.phone }} |
| **Water**: {{ contacts.utility.water.provider }} | {{ contacts.utility.water.phone }} |
{{#each local_contacts as c}}| {{c.name}} ({{c.relationship}}) | {{c.phone}} |
{{/each}}

Utility numbers are printed exactly as you typed them from your bills; the binder does not look
them up. State emergency management: {{ region.home.state_em }}. Weather office:
{{ region.home.nws_office }}. More numbers: → 25-03.

## The decisions

| Question | Page |
|---|---|
| **Do we stay or do we go?** | → 01-02: ask it every day |
| **Leaving with someone who has a medical need?** | → 01-07 |
| **How long do our supplies last?** | → 23-02, → 22-04 |
| **What do we do first, every day?** | → 01-01 |
| **What do we do about the children?** | Section 20, especially → 20-08 |
| **Who does what?** | → 00-07 |
| **A terrible medical call?** | → 12-16 |

## Five things to remember when nothing else comes to mind

1. **AIR, then BLEEDING, then WARMTH, then WATER, then FOOD.** In that order.
2. **Never burn anything indoors unless it is rated for indoor use and the CO alarm is up first.**
   Carbon monoxide kills silently (CDC, Carbon Monoxide Poisoning: Basics).
3. **Fill water containers early.** The window closes.
4. **Medicines that keep someone alive have no substitute.** They are the clock.
5. **Never ration:** drinking water, handwashing, medicine, children's food, sleep.

## Cross-references

- → 00-06 the first 60 minutes · → 25-08 the quick-reference cards · → 00-03 the full page index
- → 01-02 go/no-go · → 25-03 phone numbers · → 25-09 the family medical summary

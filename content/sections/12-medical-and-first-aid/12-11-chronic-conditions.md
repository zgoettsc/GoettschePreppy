---
id: 12-11-chronic-conditions
section: 12-medical-and-first-aid
title: "Long-term conditions without a clinic: the condition library index"
version: 4
revised: 2026-11-18
layer: core
danger_level: critical
phase: [A, B, C]
tags: [medical, chronic conditions, condition library, medications, supply clock, planning]
derived_from: [12-11-chronic-conditions]
sources:
  - us-fda-information-regarding-insulin-storage-and-swi-6448d3
  - cdc-managing-sick-days-18c7c8
  - cdc-recognizing-and-responding-to-anaphylaxis-645825
  - cdc-antibiotic-use-appropriate-use-and-antibiotic-re-ea0e27
  - cdc-urgent-maternal-warning-signs-and-symptoms-hear-7927cc
related:
  - 02-01-cl01-type-1-diabetes-injections
  - 02-03-cl03-anaphylaxis
  - 02-27-a-condition-not-in-the-library
  - 12-07-meds-stockpile
  - 12-16-triage-and-hard-calls
  - 01-02-go-no-go-decision
  - 01-07-evacuating-with-medical-needs
  - 25-09-family-medical-summary
  - 23-02-master-consumables-table
  - 30-01-the-floors
cards: [DC-04, DC-08, DC-15]
explainers: [EX-07, EX-14]
promote_when: [has.refrigerated_meds, has.epinephrine, has.oxygen, has.cpap, has.mobility_aid]
photo_slots: []
figures: []
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: { date: "2026-11-18", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "Frozen-insulin floor added; blank conditions/allergies read 'none in settings'; no numbers needing source. K1 (G34): 'When there is no prescriber' section added: every module prints published label, agency or society guidance and the binder's rule; general rules for missed doses and supply that will run out; 'never one this binder answers' removed." }
---

# Long-term conditions without a clinic: the condition library index

**What this page is for.** Every long-term condition this binder covers, in one table: what
it is, what runs out and how fast, the sign that means an emergency, and the page with the
full module. Your household's conditions are listed first. Then the questions to settle for
each condition while help still exists.

> **SAFETY**
> - **Never stop a medicine suddenly without knowing whether that is dangerous.** Several
>   medicines cause serious harm when stopped at once. Ask the prescriber which, now. With no
>   prescriber, the label in the box and the module's "When there is no prescriber" part say
>   which, as published.
> - **The binder never calculates, stretches or adjusts a dose.** Published tables are printed
>   as published. Everything about your own medicines comes from your bottles and your
>   prescriber, written in the "my meds" table (→ 12-07).
> - **Some medicines have no household substitute**: insulin, epinephrine, and others marked on
>   the condition pages. For those, the plan when supply runs out is a decision, not a
>   substitution (→ 01-02).

## Conditions in this household

{{#each members as m}}
- **{{m.label}}** ({{m.age_text}}): conditions {{#if m.conditions}}{{m.conditions}}{{else}}none in settings{{/if}}; allergies {{#if m.allergies}}{{m.allergies}}{{else}}none in settings{{/if}}.
{{else}}
- No members entered yet. Add them in settings and tick their conditions.
{{/each}}

**Your modules, read these first:**

{{#if has.condition.CL-01}}- **CL-01 Type 1 diabetes (injections)** → 02-01
{{/if}}
{{#if has.condition.CL-02}}- **CL-02 Type 1 diabetes with pump and sensor** → 02-02
{{/if}}
{{#if has.condition.CL-03}}- **CL-03 Anaphylaxis (any cause)** → 02-03
{{/if}}
{{#if has.condition.CL-04}}- **CL-04 Food allergy (child or adult)** → 02-04
{{/if}}
{{#if has.condition.CL-05}}- **CL-05 Type 2 diabetes (tablets and non-insulin)** → 02-05
{{/if}}
{{#if has.condition.CL-06}}- **CL-06 Type 2 diabetes on insulin** → 02-06
{{/if}}
{{#if has.condition.CL-07}}- **CL-07 Asthma** → 02-07
{{/if}}
{{#if has.condition.CL-08}}- **CL-08 COPD and oxygen dependence** → 02-08
{{/if}}
{{#if has.condition.CL-09}}- **CL-09 High blood pressure and heart disease** → 02-09
{{/if}}
{{#if has.condition.CL-10}}- **CL-10 Blood thinners (anticoagulants)** → 02-10
{{/if}}
{{#if has.condition.CL-11}}- **CL-11 Epilepsy and seizure disorders** → 02-11
{{/if}}
{{#if has.condition.CL-12}}- **CL-12 Pregnancy, birth and after birth** → 02-12
{{/if}}
{{#if has.condition.CL-13}}- **CL-13 Infant feeding (nursing and formula)** → 02-13
{{/if}}
{{#if has.condition.CL-14}}- **CL-14 Thyroid disease** → 02-14
{{/if}}
{{#if has.condition.CL-15}}- **CL-15 Kidney disease and dialysis** → 02-15
{{/if}}
{{#if has.condition.CL-16}}- **CL-16 Mental-health medicines** → 02-16
{{/if}}
{{#if has.condition.CL-17}}- **CL-17 Opioid dependence and chronic pain** → 02-17
{{/if}}
{{#if has.condition.CL-18}}- **CL-18 Immunosuppression and transplant** → 02-18
{{/if}}
{{#if has.condition.CL-19}}- **CL-19 Celiac and severe gut disease** → 02-19
{{/if}}
{{#if has.condition.CL-20}}- **CL-20 Adrenal insufficiency** → 02-20
{{/if}}
{{#if has.condition.CL-21}}- **CL-21 Dementia and elderly care** → 02-21
{{/if}}
{{#if has.condition.CL-22}}- **CL-22 Mobility impairment** → 02-22
{{/if}}
{{#if has.condition.CL-23}}- **CL-23 Hearing and vision aids** → 02-23
{{/if}}
{{#if has.condition.CL-24}}- **CL-24 Sleep apnoea (CPAP)** → 02-24
{{/if}}
{{#if has.condition.CL-25}}- **CL-25 Contraception and menstrual health** → 02-25
{{/if}}
{{#if has.condition.CL-26}}- **CL-26 Severe obesity and bariatric surgery** → 02-26
{{/if}}

A condition you typed that is not in the library is on → 02-27, with the module's twelve
headings left blank for you to fill from the prescriber and the pharmacy leaflet.

## Do this now

1. **Read the module for each condition above**, start to finish, while nothing is wrong.
2. **Fill in the "my meds" table** (→ 12-07) from the bottles: name, strength, schedule, fridge
   or not, and **what the prescriber says to do if doses are missed**, in their words.
3. **Write each person's supply clock** (days of medicine and supplies on hand) on → 23-02, and
   update it as you use them.
4. **Make sure at least two adults can do every life-critical routine**: give the injection, use
   the auto-injector, change the device, recognise the emergency. Not "has watched"; **has
   done it.** → 12-09 explains why.
5. **Write the family medical summary** (→ 25-09): every condition, medicine, allergy,
   prescriber and blood type, on paper.

> **Before the collapse:** book a conversation with each prescriber. Say it plainly: "I'm doing
> emergency preparedness. If we could not reach care for a long time, what should I have, what
> should I know, and what warning signs must I not miss?" Clinicians have this conversation
> regularly. For each medicine, ask what happens if supply runs low or stops, which medicines
> must never stop suddenly, and what to do if a dose is missed. Write the answers in the "my
> meds" table and on the condition page.

## The full library

"Yes" marks a condition someone in your household has. The supply clock and emergency sign are
one-phrase reminders; the module has the detail.

| Yours | Id | Condition: what it is | What runs out | Emergency sign | Page |
|---|---|---|---|---|---|
| {{#if has.condition.CL-01}}**Yes**{{/if}} | CL-01 | **Type 1 diabetes (injections)**: The body makes no insulin; insulin by injection keeps the person alive. | Insulin every day; it needs cold storage and has a limited life once opened. | Vomiting, deep fast breathing, fruity breath, confusion (high-sugar crisis); or shaking, sweating, confusion, passing out (low sugar). | → 02-01 |
| {{#if has.condition.CL-02}}**Yes**{{/if}} | CL-02 | **Type 1 diabetes with pump and sensor**: As type 1, with insulin given by a pump and sugar read by a sensor. | Pump supplies, sensors and charging on top of insulin; when a device fails, back to injections. | As type 1, plus a pump or sensor failing with no injection supplies to fall back on. | → 02-02 |
| {{#if has.condition.CL-03}}**Yes**{{/if}} | CL-03 | **Anaphylaxis (any cause)**: A sudden, severe allergic reaction that can close the airway or drop blood pressure. | Epinephrine auto-injectors expire; heat and freezing damage them. | After a trigger: trouble breathing, swelling of tongue or throat, faintness, widespread hives. Epinephrine now. | → 02-03 |
| {{#if has.condition.CL-04}}**Yes**{{/if}} | CL-04 | **Food allergy (child or adult)**: A food that the immune system reacts to, sometimes with anaphylaxis. | Safe, labelled food; traded or scavenged food may hide the allergen. | Any sign of anaphylaxis after eating (as CL-03). | → 02-04 |
| {{#if has.condition.CL-05}}**Yes**{{/if}} | CL-05 | **Type 2 diabetes (tablets and non-insulin)**: The body uses insulin poorly; managed with diet, tablets or non-insulin injections. | Pills on hand; most tablets keep well. | Extreme thirst and urination with confusion (very high sugar); shaking and confusion on some drugs (low sugar). | → 02-05 |
| {{#if has.condition.CL-06}}**Yes**{{/if}} | CL-06 | **Type 2 diabetes on insulin**: Type 2 diabetes that now needs insulin injections. | Insulin cold storage and supply, as type 1. | Low sugar: shaking, sweating, confusion, passing out; or very high sugar with confusion. | → 02-06 |
| {{#if has.condition.CL-07}}**Yes**{{/if}} | CL-07 | **Asthma**: The airways tighten and swell; inhalers open and calm them. | Inhaler canisters empty; smoke, cold air and dust make attacks more likely. | Cannot speak in full sentences, lips going blue, rescue inhaler not helping. | → 02-07 |
| {{#if has.condition.CL-08}}**Yes**{{/if}} | CL-08 | **COPD and oxygen dependence**: Long-term lung damage; some people need extra oxygen. | Oxygen concentrators need power; cylinders run empty. | Severe breathlessness, blue lips, new confusion or drowsiness. | → 02-08 |
| {{#if has.condition.CL-09}}**Yes**{{/if}} | CL-09 | **High blood pressure and heart disease**: Strain on the heart and blood vessels, managed with daily medicines. | Daily pills; some are dangerous to stop suddenly. | Chest pain or pressure; sudden face droop, arm weakness or slurred speech (stroke). | → 02-09 |
| {{#if has.condition.CL-10}}**Yes**{{/if}} | CL-10 | **Blood thinners (anticoagulants)**: Medicines that slow clotting to prevent strokes and clots. | Daily pills; missed doses raise clot risk. | Bleeding that will not stop, any head injury, black or bloody stool; sudden leg swelling or breathlessness. | → 02-10 |
| {{#if has.condition.CL-11}}**Yes**{{/if}} | CL-11 | **Epilepsy and seizure disorders**: The brain has repeated seizures; daily medicine prevents them. | Daily medicine; missed doses cause seizures. | A seizure that does not stop, or one after another without waking up. | → 02-11 |
| {{#if has.condition.CL-12}}**Yes**{{/if}} | CL-12 | **Pregnancy, birth and after birth**: Carrying a baby, giving birth, and the weeks after. | The due date; prenatal vitamins; birth supplies. | Heavy bleeding, severe headache or vision changes, seizure, severe belly pain, trouble breathing. | → 02-12 |
| {{#if has.condition.CL-13}}**Yes**{{/if}} | CL-13 | **Infant feeding (nursing and formula)**: Feeding a baby by breast or bottle. | Formula and safe water; the nursing parent's food and water. | A baby with few wet diapers, no tears, sunken soft spot, or too sleepy to feed. | → 02-13 |
| {{#if has.condition.CL-14}}**Yes**{{/if}} | CL-14 | **Thyroid disease**: The thyroid gland makes too little or too much hormone. | Daily tablet; a long clock, and the tablets keep well. | Extreme drowsiness and confusion; or a racing heart with fever and agitation. | → 02-14 |
| {{#if has.condition.CL-15}}**Yes**{{/if}} | CL-15 | **Kidney disease and dialysis**: The kidneys cannot clean the blood; some people need dialysis. | Dialysis sessions; every missed session counts. Fluid and potassium limits. | Breathlessness, swelling, an irregular heartbeat, confusion. | → 02-15 |
| {{#if has.condition.CL-16}}**Yes**{{/if}} | CL-16 | **Mental-health medicines**: Medicines for depression, anxiety, bipolar disorder, psychosis and more. | Daily medicine; several are dangerous to stop suddenly. | Thoughts of suicide, losing touch with reality, severe withdrawal (→ 12-15). | → 02-16 |
| {{#if has.condition.CL-17}}**Yes**{{/if}} | CL-17 | **Opioid dependence and chronic pain**: The body depends on opioid medicines, or pain is long-term. | Daily medicine; withdrawal begins when it stops. | Overdose: slow or no breathing, tiny pupils, cannot be woken. Naloxone. | → 02-17 |
| {{#if has.condition.CL-18}}**Yes**{{/if}} | CL-18 | **Immunosuppression and transplant**: Medicines or illness that weaken the body's defence against infection. | Anti-rejection or immune medicines daily; missed doses risk rejection. | Any fever or sign of infection. | → 02-18 |
| {{#if has.condition.CL-19}}**Yes**{{/if}} | CL-19 | **Celiac and severe gut disease**: Food or gut disease that causes damage, pain or diarrhoea. | Safe food supply; dehydration risk. | Dehydration, blood in the stool, severe belly pain. | → 02-19 |
| {{#if has.condition.CL-20}}**Yes**{{/if}} | CL-20 | **Adrenal insufficiency**: The body cannot make enough of the stress hormone cortisol; daily steroid replaces it. | Daily steroid; illness and injury need extra (published sick-day rules and injection amounts on 02-20). | Vomiting, severe weakness, collapse (adrenal crisis). | → 02-20 |
| {{#if has.condition.CL-21}}**Yes**{{/if}} | CL-21 | **Dementia and elderly care**: Memory and judgement failing; frailty in old age. | Medicines someone must manage; warmth; supervision. | Sudden worse confusion, a fall, getting cold, wandering off. | → 02-21 |
| {{#if has.condition.CL-22}}**Yes**{{/if}} | CL-22 | **Mobility impairment**: Needing a wheelchair, walker or help to move. | Batteries for powered chairs; spare parts; helpers. | Pressure sores turning red-hot or smelly; being unable to leave in an evacuation. | → 02-22 |
| {{#if has.condition.CL-23}}**Yes**{{/if}} | CL-23 | **Hearing and vision aids**: Hearing aids, glasses, contact lenses. | Hearing-aid batteries; spare glasses; a written prescription. | Lost or broken aids in an emergency or evacuation. | → 02-23 |
| {{#if has.condition.CL-24}}**Yes**{{/if}} | CL-24 | **Sleep apnoea (CPAP)**: Breathing stops repeatedly in sleep; a CPAP machine keeps the airway open. | Power every night. | Dangerous daytime sleepiness when driving or working. | → 02-24 |
| {{#if has.condition.CL-25}}**Yes**{{/if}} | CL-25 | **Contraception and menstrual health**: Birth control and period care. | Pill packs and supplies run out. | Very heavy bleeding; signs of pregnancy (→ 02-12). | → 02-25 |
| {{#if has.condition.CL-26}}**Yes**{{/if}} | CL-26 | **Severe obesity and bariatric surgery**: Very high body weight, or after weight-loss surgery. | Lifelong vitamins after surgery; medicines absorbed differently. | Vomiting that will not stop, severe belly pain. | → 02-26 |

## For every condition, answer five questions

Do this for every condition in the household, with the prescriber while you can.

1. **What is the supply clock?** Days of medicine and supplies on hand, from the "my meds"
   table. It changes daily and belongs on → 23-02.
2. **What happens when it runs low?** Ask the prescriber what to do if doses are missed, and
   write their answer down. **Never work it out alone under stress.** If no prescriber is left,
   the module's "When there is no prescriber" part prints the published answer (below).
3. **What are the warning signs?** Written down, specific, known to every adult. What does
   "getting worse" look like, and when does it become an emergency?
4. **What is the fallback?** Is there a simpler version of the treatment that needs no power or
   device? For diabetes on a pump, it is insulin by syringe and a fingerstick meter (→ 02-02).
   Knowing the fallback turns a device failure into an inconvenience instead of a crisis.
5. **What is the decision point?** At what supply clock does this become the reason to move,
   seek care or change the plan? **Decide in advance and write it down** (→ 01-02, → 01-07).

## When there is no prescriber

In a long emergency there may be no prescriber, pharmacist or clinic at all. The binder does not
leave a household with "ask your prescriber" as its only answer. Every condition module that
depends on a prescriber has a **"When there is no prescriber"** part that prints, as published and with the publisher named,
what the medicine's FDA-approved label, the federal agency or the condition's national society
says about a missed dose, a vomited dose, running out and stopping, and then the rule this
binder follows when the sources differ. Where no published guidance exists, the module says so
plainly and gives the safest general rule the sources support. The rules that run through all
of them:
1. **The label in the box is published guidance.** Its "missed dose", "stopping" and "ask a
   doctor" lines are copied into the "my meds" table now, word for word (→ 12-07, → 29-14).
2. **A missed dose:** take it when remembered, unless the label says otherwise; never double it
   unless the label or the condition's national society says it is safe (as the thyroid society
   does for levothyroxine, → 02-14).
3. **A medicine that must not stop suddenly, with supply that will certainly run out:** do not
   take full doses to the last day. Spread the reduction over at least the period the label
   gives, so it ends when the supply does. The binder prints the label's period; it never works
   out the steps for a person.
4. **A prescriber's written plan, made before the collapse, always comes first.** The
   worksheets on every module are how to get one.

## Principles for any long-term condition

- **Daily habits matter more when supply is short**: food, activity, sleep, stress and warmth all
  affect long-term conditions, and all are things you control.
- **Illness knocks long-term conditions off balance** (→ 12-05; CDC, Managing Sick Days). Plan
  for the combined event, not the single one. Ask each prescriber for written sick-day
  instructions.
- **Stress is physical, not just emotional** (→ 21-01). Months of crisis affect blood sugar,
  blood pressure, sleep and immunity.
- **Storage without power** is its own skill. Refrigerated medicines (→ 29-07, → 12-21), heat
  exposure and freezing (→ 12-07) each have published rules. **A frozen-then-thawed insulin vial
  or pen is discarded** (floor, → 30-01). Your household's choices on the
  related trade-offs: heat-exposed medicine {{choice DC-08}} (→ 30-09); expired medicine
  {{choice DC-04}} (→ 30-05); someone else's prescription {{choice DC-15}} (→ 30-16).
- **Write everything down.** Symptom, sugar and medicine logs (→ 25-05) replace the clinic's
  chart, and they matter enormously if you reach care.

## The honest part

**A household cannot make insulin, epinephrine or most other medicines.** No preparation changes
that. What preparation does:
- **Lengthens the supply clock**: a legitimate buffer, good storage, careful use (→ 12-07).
- **Makes the fallbacks work**, so a dead battery or a broken device is not a crisis.
- **Buys decision time**, so the decision to stay or go (→ 01-02) is made early, deliberately,
  with the resources to act on it.
- **Prevents the avoidable crises**: allergen discipline, sick-day management, infection
  prevention.

That is a great deal of value. It is not the same as solving the problem, and this binder does
not pretend otherwise. **For many conditions, the realistic best outcome in a long event is
reaching working medical care in time.** That is why the supply clock is a trigger on → 01-02,
and why closeness to surviving medical care belongs on the list when choosing a destination
(→ 01-05).

## Gear

| Item | Why | Notes |
|---|---|---|
| **A conversation with each prescriber** | The most valuable item in this section | Before the collapse |
| **Family medical summary, printed** | Conditions, medicines, allergies, blood types, prescribers | → 25-09 |
| The largest legitimate medicine buffer | The supply clock is everything | 90-day fills, early refills (→ 12-07) |
| Each module's supply list, in full | What that condition depends on | → 02-NN pages above |
| Power-free fallback supplies | Work when devices fail | Each module's "power and devices" part |
| Cooling for refrigerated medicines | Cold chain without the grid | → 12-21, → 09-10 |
| **Written care instructions any adult can follow** | The usual carer may be the one hurt | → 12-09 |
| Symptom, sugar and medicine logs | Replace the clinic's chart | → 25-05 |
| Written decision points | So → 01-02 is not improvised | → 01-02 |
| Medical ID for each person with a condition | Matters if people are separated | Cheap |

## When it runs out

- **Write the plan now, calmly:**
  - **Supply clock thresholds** for every life-critical medicine, with dates, checked weekly
    (→ 23-02).
  - **A trigger** at which the household stops sheltering and seeks resupply or care (→ 01-02).
    **Set it early enough that you still have the resources to act**, not at the last dose.
  - **A resupply plan**: where, who, what is realistic.
  - **A conversation, in advance, among the adults** about what happens if resupply fails
    (→ 12-16, → 21-03). Hard, and far better had now.
- **Rationing a prescription medicine is a prescriber's decision** while one exists, made in
  advance and written in the "If doses are missed" column. With no prescriber, the only
  reductions this binder prints are the labels' own stopping instructions, used when supply
  will certainly run out (rule 3 above). Never improvise a lower dose from a book.
- **Scavenging and trade:** pharmacies and clinics early in an event may still have supply; that
  window closes fast. Other households, nurses, pharmacists and doctors in the community are
  enormously valuable (→ 18-01, → 18-03). Never take unlabelled medicine (→ 12-07).
- **The strategic move is community and location.** A group with medical skill, or a place near
  surviving care, changes this problem more than any stockpile.

## Phase notes

- **A (at home):** the best phase for this. Pharmacies, clinicians and supply may work for a
  while. **Use that window hard** for building the buffer and for the conversations. Track the
  supply clock from day one.
- **B (moving):** life-critical medicines are the most important cargo, protected from heat and
  cold, carried on a person (→ 22-03, → 01-07). **The reason to move is often the medicine
  itself** (→ 01-02). A serious medical event on the road means heading for the nearest working
  care; the destination can wait.
- **C (resettled):** no resupply and further from care. Find out where the nearest working
  medical care is and write it on → 25-03.

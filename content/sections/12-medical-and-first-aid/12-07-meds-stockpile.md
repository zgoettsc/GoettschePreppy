---
id: 12-07-meds-stockpile
section: 12-medical-and-first-aid
title: "Family medicine stockpile and over-the-counter list"
version: 1
revised: 2026-11-16
layer: core
danger_level: caution
phase: [A, B, C]
tags: [medical, medications, my meds, OTC, stockpile, rotation, allergies, storage, expiry]
derived_from: [12-07-meds-stockpile]
sources:
  - cdc-antibiotic-use-appropriate-use-and-antibiotic-re-ea0e27
  - us-fda-information-regarding-insulin-storage-and-swi-6448d3
  - us-fda-food-allergies-627fb6
  - cdc-yellow-book-travelers-diarrhea-oral-rehydration-a1b9d8
  - nih-national-library-of-medicine-dailymed-pepto-bism-e5f5a9
  - nih-medlineplus-bismuth-subsalicylate-drug-informati-190927
  - lyon-rc-et-al-journal-of-pharmaceutical-sciences-95-1d6bf3
  - us-fda-fda-drug-safety-communication-diphenhydramine-bab442
related:
  - 12-01-first-aid-kit
  - 12-04-infection-and-antibiotics
  - 12-05-common-illness-and-dehydration
  - 12-11-chronic-conditions
  - 12-13-pain-and-fever
  - 12-21-evaporative-cooling-pouches
  - 25-09-family-medical-summary
  - 23-02-master-consumables-table
  - 22-04-household-inventory
  - 30-01-the-floors
  - 30-05-dc04-expired-medication
  - 30-09-dc08-heat-exposed-medication
  - 30-16-dc15-someone-elses-prescription
  - 29-07-ex07-refrigerated-medicines
  - 29-14-ex14-reading-a-label
cards: [DC-04, DC-08, DC-15, DC-16]
explainers: [EX-07, EX-14]
promote_when: [has.refrigerated_meds]
photo_slots:
  - { id: meds-storage, caption: "Our locked medicine box and where it goes when only one room is heated" }
figures: []
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: null
---

# Family medicine stockpile and over-the-counter list

**What this page is for.** Your household's own "my meds" table, the over-the-counter (OTC,
no prescription needed) categories worth stocking, how to store medicines without power, and
what expiry dates really mean.

> **This page does not tell anyone what to take or how much.** It covers which categories to
> have, how to store them and how to rotate them. Choosing and dosing belong to each product's
> label, your pharmacist and your prescriber. The binder never calculates or adjusts a dose.
>
> **Two rules for every household:**
> 1. **Check every medicine against every person's allergies** (→ 25-09). Inactive ingredients
>    in liquids, chewables and suspensions can include food allergens, and children's products
>    especially (FDA, Food Allergies). **Read every label** (→ 29-14).
> 2. **Life-critical medicines are kept, counted and protected separately** from the general
>    stockpile: insulin, epinephrine, glucagon, rescue inhalers, seizure medicines and any
>    medicine its prescriber says must not stop (→ 12-11).

## Do this now

1. **Fill in your "my meds" rows in settings** so the table below prints. Type each one from
   the bottle and the prescriber's instructions, word for word.
2. **Write the medicine and allergy list for every person** (→ 25-09): prescriptions, strength,
   prescriber, pharmacy, drug allergies and what the reaction was. An unconscious person cannot
   tell you.
3. **Count what you own, with expiry dates**, and set a twice-a-year review (→ 22-04, → 25-10).
4. **Buy the OTC categories in real quantities.** {{ household.size }} people in a long event go
   through far more than the small bottles most homes keep.
5. **Sort out storage before you stockpile**: cool, dark, dry, locked (below).

> **Before the collapse:** talk to each prescriber and your pharmacist about an emergency
> supply. Ask about 90-day fills, mail order, refilling at the earliest allowed date, and
> **which of your medicines are dangerous to stop suddenly and what to do if you run out.**
> Write their answers in the "If I miss doses" column, in their words.

## My meds

This table prints your household's rows exactly as typed. The last three columns are for you to
fill in by hand and keep current.

| Who | Medicine | Strength | Schedule | Needs fridge? | If doses are missed (prescriber's words) | Where kept | Days on hand | Expires |
|---|---|---|---|---|---|---|---|---|
{{#each meds as m}}| {{m.member}} | {{m.name}} | {{m.strength}} | {{m.schedule}} | {{m.refrigerated}} | {{m.if_missed}} | ____ | ____ | ____ |
{{else}}| (no medicines entered yet) | | | | | | ____ | ____ | ____ |
{{/each}}

**Days on hand** is the number of days your supply lasts at the schedule printed in the row. Work
it out from the bottle, not from this page, and write it on → 23-02. For life-critical
medicines, that number is the household's most important clock (→ 01-02).

{{#if has.refrigerated_meds}}**Someone in your household has a medicine that needs a fridge.**
Read the storage section below, → 12-21 and → 29-07 now, before the power goes out.{{/if}}

## Two tiers, kept apart

**Tier 1: life-critical prescription medicines.** Insulin and its supplies, epinephrine,
glucagon, rescue inhalers, seizure medicines, and anything else a condition page (→ 12-11) marks
as critical. These have no substitute. They get their own storage, their own count and their own
tracking, **not the general medicine cabinet.**

**Tier 2: general household medicines (this page).** OTC and routine prescriptions. Worth
stocking deeply, but the household survives shortages of them.

## OTC categories worth stocking (not brands, not doses)

| Category | What it is for | Notes |
|---|---|---|
| **Pain and fever relievers** (acetaminophen and ibuprofen) | The most-used category by far | Adult **and** children's products; → 12-13 |
| **Oral rehydration salts** | Possibly the most life-saving OTC item here | → 12-05; stock heavily |
| Antihistamines | Allergic reactions, itching | **Not a substitute for epinephrine** in a severe allergic reaction (→ 02-03). Children's diphenhydramine Drug Facts label: **"Do not use to make a child sleepy"; under 2 years, do not use; 2 to 5 years, do not use unless directed by a doctor** (Children's Benadryl Allergy, Drug Facts label). More than the label dose can cause serious heart problems, seizures, coma or death (FDA, Drug Safety Communication on diphenhydramine). Children's options are on → 12-13 |
| Anti-diarrhoea medicine | Function and comfort; **not for every case** | Loperamide label: **under 2 years, do not use; 2 to 5 years, ask a doctor; do not use with bloody or black stool; ask a doctor first with fever** (Imodium A-D, Drug Facts label). CDC: antimotility drugs alone are not recommended for bloody diarrhoea or diarrhoea with fever (CDC Yellow Book) |
| **Bismuth subsalicylate** (pink stomach-relief chewables or liquid) | Upset stomach, diarrhoea | Label: **ages 12 and over; under 12 ask a doctor.** It is a **salicylate**, aspirin's chemical family: **children and teenagers who have or are recovering from chickenpox or flu-like symptoms must not use it (Reye's syndrome, a rare and dangerous brain and liver illness).** Not with an aspirin allergy or other salicylates. **Ask a doctor or pharmacist first if taking any medicine for diabetes.** It can turn the tongue and stool black, which is harmless (MedlinePlus), but **do not use it if you already have bloody or black stool**, which can mean bleeding (DailyMed, Drug Facts label). Keep it out of the children's medicine bin |
| Anti-nausea | Illness; helps keep fluids down | → 12-05 |
| Antacids and acid reducers | Common, cheap, useful | |
| Antibiotic ointment | Minor wounds | → 12-02 |
| Antifungal cream (clotrimazole or miconazole) | Feet, skin folds, yeast diaper rash (bright red with small spots at the edges, → 20-06); likely when washing is limited | Underrated |
| Hydrocortisone cream | Itching, rashes, insect bites | |
| Cough and cold remedies | Comfort; expect a lot of respiratory illness | Check children's products carefully |
| Laxatives and stool softeners | **A stored-food diet causes constipation** | Fibre matters too (→ 04-18) |
| Electrolyte supplements | Heavy sweating, illness (→ 11-08) | |
| Eye drops and saline | Wind, dust, smoke, flushing an eye | Also for washing wounds |
| Lice and scabies treatments | Crowded conditions, no laundry | Miserable and treatable |
| Multivitamin and vitamin D | A stored-food diet has gaps{{#if is.cold_winters}}, and your winters are long and dark{{/if}} | → 04-18 |
| Aspirin | Specific uses only (→ 12-16 heart attack) | **Not for children or teenagers** (Reye's syndrome) |
| Petroleum jelly | Dressings, chapped skin, fire starting | Cheap, many uses |

**Children's products.** Every children's medicine must be label-checked for allergens:
flavourings, colourings and suspension bases are real risks (FDA, Food Allergies; → 02-04).
Buy an oral dosing syringe for each liquid; never a kitchen spoon.

{{#if has.nursing}}**Someone in your household is nursing.** Every OTC Drug Facts label carries
the line "if pregnant or breast-feeding, ask a health professional before use." Before the
collapse, ask a clinician or pharmacist which medicines on this page are fine while nursing,
and write the answer on → 25-09 so another adult can follow it. Aspirin and other salicylates
(including bismuth subsalicylate), sedating antihistamines and combination cough and cold
products are the usual items to ask about.{{else}}**Pregnancy and nursing.** Every OTC Drug
Facts label says "if pregnant or breast-feeding, ask a health professional before use." Ask now
and write the answer on → 25-09.{{/if}}

## Building a buffer legitimately

- **Talk to the prescriber.** Say you are building emergency preparedness. Ask about **90-day
  fills**, mail order, and refilling at the earliest allowed date.
- **Refill early, consistently.** Filling a few days early each cycle builds a buffer without
  doing anything irregular.
- **Know what each medicine is for and what happens if it stops.** Some medicines are
  dangerous to stop suddenly. Ask which, and what the plan would be (→ 12-11).
- **Antibiotics** are a separate question (→ 12-04, CDC Antibiotic Use). Your household's
  choice on antibiotics without a prescription: {{choice DC-16}} (→ 30-17).
- **Someone else's prescription:** a bottle prescribed for one person may be the only one in
  reach for another. The risks are the wrong drug, a dose set for a different body, allergies,
  and leaving the owner short. Your household's choice: {{choice DC-15}} (→ 30-16).

## Storage: where stockpiles quietly fail

- **Cool, dark, dry.** Heat and humidity damage medicines faster than time does. **The bathroom
  cabinet is one of the worst places in the house**: hot and humid.
- **The number, so "cool" is not a guess:** many OTC Drug Facts labels say **"store between
  20-25°C (68-77°F)"** (for example Children's Benadryl Allergy and Imodium A-D, Drug Facts
  labels). Your own label governs. Below freezing, liquids and suspensions can be ruined; long
  heat ages everything faster.
- **Not the garage, not the car, not an unheated room.** Freezing damages many medicines; heat
  damages most. **When the house is heated to one room** (→ 08-01), that room is where the
  medicines live, on the side away from the heater. Photograph where they go:

{{photo meds-storage}}

- **Refrigerated medicines** (insulin, some injectables, some liquid antibiotics, some eye
  drops) have their own rules. Each label or package insert gives an unrefrigerated window; the
  FDA's insulin storage guidance prints the published windows (FDA, Information Regarding
  Insulin Storage). Methods for keeping them cool without power are on → 12-21 and → 29-07.
- **A frozen-then-thawed insulin vial or pen is discarded.** It loses strength with no way to
  tell, and the published guidance is unanimous. This is a floor (→ 30-01), not a choice.
- **Heat-exposed refrigerated medicine** is a trade-off. Following the published unrefrigerated
  window exactly is the safe rule; some households, with no alternative, would use it beyond the
  window and watch more closely. Card DC-08 sets out the risk.
  Your household's choice: {{choice DC-08}} (→ 30-09)
- **Epinephrine auto-injectors must not freeze and must not sit in a hot car** (→ 02-03). In
  winter, freezing is the risk that gets forgotten.
- **Locked away from children.** Child-resistant caps are not child-proof. A locked box is the
  answer; "high up" is not (→ 20-02). **Children do not have access to firearms, fuel,
  medications or chlorine products.** This is a floor (→ 30-01).
- **Original containers with labels intact.** Loose pills in a bag cannot be identified six
  months later, which is dangerous.
- **Rotate.** First in, first out. Twice-a-year review (→ 22-04).

## Expiry dates: the honest version

An expiry date marks the period the manufacturer guarantees full strength. It is not a cliff.
The FDA ran the Shelf Life Extension Program for the US military's stockpiled medicines. Of
3,005 lots of 122 products, properly stored and laboratory-tested, **88% could be extended at
least a year past their date, on average by 66 months, but the extra time varied a great deal
and could only be confirmed by testing each lot** (Lyon RC et al., Journal of Pharmaceutical
Sciences, 2006). A household cannot test, so treat any extra life as uncertain.

**The documented exceptions** do not hold up the same way: **liquids and suspensions**
(including children's bottles and any antibiotic mixed with water), **insulin**, **epinephrine**,
**nitroglycerin** and **eye drops**. **Anything that has changed colour, smell, clarity or
texture** (cloudy, crumbling, discoloured) is discarded.

**Using an expired medicine when nothing in date exists is a trade-off** your household decides.
The life-critical ones are exactly those where reduced strength matters most, so rotate them
rigorously while rotation is possible. Card DC-04 explains the risk and options, including
epinephrine.
Your household's choice: {{choice DC-04}} (→ 30-05)

Ask your pharmacist while there is one.

## The paperwork that makes it work

On paper in this binder (→ 25-09):
- Every person's medicines, strengths and prescribers
- **Every person's drug allergies and what the reaction was**
- Food allergens in full (→ 02-04)
- Blood types, long-term conditions, vaccination dates (tetanus especially, → 12-04)
- Pharmacy and clinic contacts
- **Where each medicine is kept**

## Gear

| Item | Why | Notes |
|---|---|---|
| **Medicine and allergy list for everyone, printed** | Prevents a preventable disaster | → 25-09 |
| The OTC categories above, in bulk | Small bottles do not cover a household for a year | Adult and children's |
| **Oral rehydration salts, heavily stocked** | → 12-05 | |
| Lockable medicine box | Child-resistant is not child-proof | Not just "up high" |
| Cool, dark, dry storage container | Heat and humidity are the enemies | Not the bathroom |
| A min/max thermometer with the medicines | Tells you what they have been through | Cheap |
| Thermometers plus spare batteries | → 12-04 | |
| Pill organiser, labels, marker | Managing a sick person over days | |
| Oral dosing syringes and cups | Accurate liquid doses | Never a kitchen spoon |
| Inventory log with expiry dates | Untracked stock expires | → 22-04, → 25-05 |
| Cooling for refrigerated medicines | Tier 1: separate system | → 12-21, → 09-10 |

## Scavenge or substitute

- **From other households (→ 22-02):** medicine cabinets are among the most useful finds.
  **Identify everything by its original label, check it against everyone's allergies, and never
  take unidentified pills.** Loose, unlabelled medicine is a hazard, not a resource.
- **Traditional and herbal remedies** exist for many minor complaints and some have real
  evidence. **They are not equal to the medicines above, they interact with prescription drugs,
  and their strength is unreliable.** Learn them properly and in advance, and **never use them
  in place of a life-critical medicine.**
- **Comfort measures cover a lot:** warmth, fluids, rest, raising an injured limb, cold packs,
  salt-water rinses, honey for a cough (**never under 12 months**).
- **What has no substitute:** life-critical medicines (→ 12-11).

## When it runs out

- **Runway:** for each medicine, days on hand from the "my meds" table. Put every one on → 23-02.
  For life-critical medicines, that number drives the decision to stay or leave (→ 01-02).
- **Ration OTC medicines for function, not comfort alone**, as supplies fall: a fever reducer
  that lets someone drink and sleep is a good use; one for mild aches is not, when supply is
  short. **This never applies to a prescription medicine.** Changing how you take a prescription
  is a decision for the prescriber; write their answer in the "If doses are missed" column now.
- **Resupply:** pharmacies early; scavenging with strict identification; trade. Medicines are
  among the most valuable trade goods (→ 18-02), so holding them is a security matter (→ 14-03).
- **Substitute:** comfort, hygiene, food and rest do a surprising amount. Willow bark and
  similar remedies exist; their strength is unreliable and they carry the same risks as the
  drugs they resemble.
- **The plan for a life-critical medicine running out is not a substitution; it is a
  decision** (→ 01-02, → 12-16). That is why each condition page has a supply clock.

## Phase notes

- **A (at home):** build the buffer while pharmacies work. Get the list written, the storage
  sorted and the rotation habit going. **The first weeks of any event are when medicine problems
  can still be solved.**
- **B (moving):** **life-critical medicines go first, in the most protected place you have, on
  the body where possible** (→ 22-03, → 01-07). A compact general kit (pain relief, ORS,
  antihistamine, anti-diarrhoea, antibiotic ointment) covers most of what happens on the move.
  Watch the temperature of medicines in a vehicle, both hot and cold.
- **C (resettled):** no resupply at all. The runway figures become real, and community matters
  most: a group with a pharmacist, nurse or doctor in it is in a different situation (→ 18-01,
  → 18-03).

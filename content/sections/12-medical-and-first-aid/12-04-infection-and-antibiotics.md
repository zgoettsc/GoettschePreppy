---
id: 12-04-infection-and-antibiotics
section: 12-medical-and-first-aid
title: "Infection, fever and antibiotics"
version: 3
revised: 2026-11-16
layer: core
danger_level: critical
phase: [A, B, C]
tags: [medical, infection, antibiotics, sepsis, fever, tetanus, hygiene, abscess]
derived_from: [12-04-infection-and-antibiotics]
sources:
  - cdc-about-sepsis-a8304b
  - cdc-antibiotic-use-appropriate-use-and-antibiotic-re-ea0e27
  - cdc-about-tetanus-3fc6c0
  - cdc-tetanus-clinical-guidance-wound-management-td-td-5580f4
  - cdc-about-hygiene-handwashing-and-infection-preventi-61142e
related:
  - 12-02-bleeding-and-wounds
  - 12-03-burns
  - 12-05-common-illness-and-dehydration
  - 12-07-meds-stockpile
  - 12-13-pain-and-fever
  - 12-14-wound-closure
  - 12-16-triage-and-hard-calls
  - 12-20-field-dentistry
  - 13-02-hygiene-and-handwashing
  - 25-09-family-medical-summary
  - 30-16-dc15-someone-elses-prescription
  - 30-17-dc16-antibiotics-without-a-prescription
  - 12-22-antibiotics-by-condition
  - 12-23-antibiotics-by-drug
  - 12-24-tccc-antibiotics-as-published
cards: [DC-15, DC-16]
explainers: [EX-14]
promote_when: []
photo_slots: []
figures: []
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: { date: "2026-11-16", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "Tetanus table rebuilt from CDC clinical guidance (completed series; dirty/major examples; TIG for incomplete/unknown); 48-72 h removed; sepsis signs checked. L7 (G28): DC-16 paragraph now points to the published dose pages 12-22/12-23/12-24 and the card's three options." }
---

# Infection, fever and antibiotics

**What this page is for.** Spotting infection early, recognising sepsis, knowing when a wound
needs a tetanus booster, and what a household can do when antibiotics are scarce or absent.
It is written for people with no doctor in the house.

> **SAFETY**
> - **Infection is the most likely way a survivable injury becomes a fatal one when there is
>   no clinic.** Before antibiotics, ordinary wounds routinely killed healthy adults.
> - **This page does not tell you which antibiotic to use or how much.** The right drug depends
>   on what the infection is, the germ, the person, their allergies and their other medicines.
>   **Getting it wrong causes harm and breeds resistance** (CDC, Antibiotic Use). Published
>   doses, each printed as its publisher printed it, are on → 12-22 (by infection) and the
>   drugs' dangers on → 12-23. This binder never calculates or suggests a dose.
> - **Sepsis is a medical emergency.** Know its signs by heart (below).

## Do this now: is this wound infected?

1. **Look at the wound at every dressing change.** Healing wounds get *less* red, swollen and
   painful after day two or three.
2. **Worse instead of better, red streaks, pus or a foul smell:** it is infected. Open the
   dressing, flush it again with lots of clean water (→ 12-02), keep it open, keep it clean.
3. **Take the temperature and write it down with the time** (→ 25-05).
4. **Confusion, fast breathing, fast heartbeat, clammy skin, extreme pain:** this may be
   sepsis. If any care exists, go now. If not, → 12-16.
5. **Check the tetanus rule below** for every wound.

## Do this now: preparation

- **Get everyone's tetanus vaccination up to date and write the dates on → 25-09.** Puncture
  wounds are common in a long emergency and there is no home treatment for tetanus (CDC, About
  Tetanus). **A booster six years old is not enough for an axe wound** (rule below).
- **Write down every household member's drug allergies now** (→ 25-09). Any medicine you ever
  give will be checked against that list.
- **Build the hygiene system: it is the real defence** (→ 13-02). Soap, clean water,
  handwashing, clean dressings. Prevention is not the consolation prize here; it is the main
  strategy.
- **Learn the sepsis signs and post them** where everyone can see them.

> **Before the collapse:** talk to a clinician about emergency preparedness while you can. It is
> an ordinary conversation and clinicians have it regularly. Ask about tetanus status for
> everyone, about each person's long-term conditions (→ 12-11), and whether they would
> prescribe anything for your situation, with written instructions for when and how to use it.
> Write the answers here, with the clinician's name and the date:
>
> ____________________________________________________________________
>
> ____________________________________________________________________

## Recognising infection early

A healing wound gets **less** painful, **less** red and **less** swollen after the first day
or two. Anything moving the other way is a warning.

**Infection in the wound:**
- Redness, swelling, warmth and pain that **increase** after day 2 or 3
- Pus, cloudy fluid, or a foul smell
- **Red streaks spreading** from the wound toward the body
- The wound reopening, or a hard, tender, swollen lump (an **abscess**, a closed pocket of pus)

**Infection spreading through the body:**
- **Fever, chills, shaking**
- Feeling clearly, unmistakably unwell
- Loss of appetite, weakness

**Sepsis: a life-threatening emergency** (the body's overwhelming reaction to infection; CDC,
About Sepsis):
- **Confusion or disorientation**
- **Fast breathing; fast heartbeat**
- Extreme pain or discomfort
- Clammy or sweaty skin
- **Shortness of breath**

**Confusion in someone with an infection is the sign that changes everything.** When care
exists, that is an immediate trip to a hospital. Without it, → 12-16.

## Fever: a signal, not the disease

Fever is the body fighting infection. It is useful information, which is why the kit list has
several thermometers.
- **Track it.** Write temperatures down with the time (→ 25-05). A trend tells you far more
  than one reading.
- **Treating a fever** with over-the-counter medicine makes the person more comfortable and
  helps them drink and rest (→ 12-13). Adults follow the label. For children, use only the
  published tables printed on → 12-13 and the label.
- **Fever plus dehydration is the dangerous combination in small children** (→ 12-05).
- **Fever in a baby is different and more urgent** than fever in an adult. The American Academy
  of Pediatrics' fever guidance on → 12-13 says when it is an emergency.{{#if has.infant}} Your
  household has an infant: read that section before you need it.{{/if}}
- **Some conditions change the rules when illness hits.** Diabetes (→ 02-01, → 02-02, → 02-05,
  → 02-06), adrenal insufficiency (→ 02-20) and a weakened immune system (→ 02-18) each have
  their own sick-day steps. Read that condition's page as soon as fever starts.
{{#each members as m}}
  - {{m.label}}: conditions {{#if m.conditions}}{{m.conditions}}{{else}}none in settings{{/if}}
{{/each}}

## Tetanus: the after-a-wound booster rule

Tetanus (lockjaw) is caused by a germ found in soil and manure. There is no home treatment once
it starts. The whole defence is the vaccine, and after any wound the question is **whether a
booster is due now.** The CDC wound rule, for people who **completed** the childhood series of
tetanus shots (the "primary series") (CDC, Tetanus clinical guidance):

| Wound | Last tetanus dose **less than 5 years** ago | **5 to 10 years** ago | **10 or more years** ago |
|---|---|---|---|
| **Clean and minor** | nothing | nothing | **Td or Tdap booster** |
| **Dirty or major**: punctures; dirt, soil, faeces or saliva in it (animal or human bites); burns, crush injuries, frostbite, open fractures, dead tissue | nothing | **Td or Tdap booster** | **Td or Tdap booster** |

- **Never vaccinated, an incomplete primary series, or an unknown history:** CDC says vaccinate
  **for any wound**. For a dirty or major wound, these people also need **tetanus immune
  globulin (TIG)**; CDC says TIG is never needed for a clean minor wound. TIG is a clinic item,
  so this is a wound to take toward care while any clinic functions.
- **Get the booster as soon as you can.** While pharmacies and urgent care work, a wound turns
  straight into that errand.
- **Adults who cannot remember their last booster count as an unknown history.**

## Prevention: the actual plan

Antibiotics may be unavailable, scarce, or wrong for the germ. **The household's infection
strategy is prevention, and it has to be taken seriously.**

1. **Handwashing** with soap and clean water, properly: before food, before wound care, after
   the toilet, after animals (CDC, About Hygiene). **This is the most powerful medical step a
   household with no clinic can take.** It needs soap (→ 13-09) and water (→ 03-01), so budget
   both.
2. **Clean water** for drinking, cooking and washing wounds (→ 03-04).
3. **Sanitation**: human waste handled properly, away from water and food (→ 13-01, → 13-07).
   Historically, sanitation failures kill more people than injuries do.
4. **Food safety**: cooking temperatures, no cross-contamination (→ 04-17, → 05-16). For
   households with food allergies, the same kitchen discipline protects them (→ 02-04).
5. **Wound care**: flushing, cleanliness, and **not closing dirty wounds** (→ 12-02, → 12-14).
6. **Not getting hurt**: sharp tools, safe technique, traction on ice.
7. **Keeping sick people apart** within the household where you can (→ 13-11).
8. **Tetanus vaccination**, current, for everyone (CDC).

## Antibiotics: the honest discussion

People ask about this constantly, so here is the straight answer.
- **Antibiotics are prescription medicines for good reasons.** The right drug depends on the
  diagnosis. The wrong one does not work, delays the right treatment, causes side effects and
  breeds resistance (CDC, Antibiotic Use).
- **Most infections a household sees do not need antibiotics at all**, and most coughs and
  colds are viral, where antibiotics do nothing (CDC). Using them wrongly wastes something you
  cannot replace.
- **The safest route to a contingency supply is a clinician**, with **written instructions**
  for when and how to use it, while clinics still exist.
- **Any antibiotic must be checked against the patient's allergies and other medicines** before
  use (→ 25-09).
- **Take an antibiotic exactly as the prescription or written plan directs**: the right drug,
  dose and length, not improvised and not stopped early because someone "feels better" on day
  two. Current guidance has moved from "always finish the bottle" to "exactly as prescribed":
  many modern courses are deliberately short. The point is that the plan decides, not the
  patient halfway through.

### Two trade-offs your household decides

**Antibiotics without a prescription.** Some households keep veterinary, aquarium or leftover
antibiotics as a last resort for a life-threatening infection when nothing else exists. Those
products are not checked for human use, their labels do not translate to people, and using
any antibiotic without a diagnosis risks the wrong drug, an allergic reaction, a delay and
resistance. Card DC-16 explains the risk and the options: never, last resort for adults only,
or last resort with children included. Under either last-resort option, the drug and dose come
only from a clinician's written plan (the box above) or from the published rows on → 12-22,
where each adult and child dose is printed as WHO, IDSA, CDC or the FDA label printed it, with
the publisher named. Check the drug's dangers on → 12-23 first. The military battlefield
antibiotic list is printed on → 12-24; it is written for medics treating combat wounds. A dose
is never worked out or adjusted by the household.
Your household's choice: {{choice DC-16}} (→ 30-17)

**Giving someone else's prescription.** A bottle prescribed for one person may be the only one
in reach for another. The risks are the wrong drug for this illness, a dose set for a different
body, allergies and interactions, and leaving the owner without their own medicine. Card DC-15
sets out the options.
Your household's choice: {{choice DC-15}} (→ 30-16)

Whatever you choose, a small antibiotic supply is irreplaceable and expires. If you have one,
it is for a genuinely life-threatening infection, not for a cold, a scrape or "just in case".

## What you can do without antibiotics

- **Flush and clean, thoroughly and repeatedly** (→ 12-02).
- **Opening and draining an abscess** is the historical standard treatment for a closed pocket
  of pus. **It is also a procedure** with real risks depending on where the abscess is. Read
  → 12-14 and a real medical reference in advance, and learn it on a course if you can.
- **Do not close dirty wounds** (→ 12-14). Trapping infection is worse than an open wound.
- **Warm compresses, raising the infected part, and rest.**
- **Honey and sugar dressings** both have traditional and evidence-supported use on suitable
  wounds. **Never honey for a baby under 12 months** (infant botulism), and neither replaces
  care.
- **Support the person:** fluids (→ 12-05), food, warmth, sleep. A well-fed, well-watered,
  rested person fights infection much better than a cold, dehydrated, exhausted one. That makes
  water, food and heat medical supplies too.
- **Recognise when it is beyond you** (→ 12-16), and if any medical care is within reach,
  **go**. "There is no hospital" is often less absolute than people assume.

## Gear

| Item | Why | Notes |
|---|---|---|
| **Current tetanus vaccination for everyone** | No home treatment exists | Before the collapse |
| **A conversation with a clinician, now** | The safest route to any contingency plan | Write the answers in the box above |
| Thermometers ×2 to 3 plus spare batteries | Fever is the main whole-body signal | {{#if has.child}}Include one suited to children{{else}}One spare{{/if}} |
| **Soap in large quantity** | The most powerful medical supply you can own | Plus → 13-09 to make more |
| Water purification | Clean water underlies everything | → 03-04 |
| Nitrile gloves by the box | Stops germs passing either way | |
| Wound flushing supplies | Mechanical cleaning stands in for antibiotics | → 12-02 |
| Povidone-iodine, chlorhexidine | Cleaning skin | Bulk |
| Raw or medical-grade honey | Traditional dressing with real support | **Never under 12 months** |
| Written allergy and medicine list for everyone | Prevents a preventable disaster | → 25-09 |
| *Where There Is No Doctor* on paper | Real guidance on infection and abscesses | → 12-01 |
| Fever and symptom log sheets | Trends matter more than one reading | → 25-05 |

## Scavenge or substitute

- **Soap** can be made (→ 13-09) and is the thing most worth making.
- **Clean water** by boiling or filtering (→ 03-04).
- **Dressings** from boiled clean cloth (→ 12-02).
- **Antiseptics:** diluted bleach has documented uses for **surfaces** (→ 29-05); alcohol for
  skin and instruments. **Do not improvise antiseptic strengths for use inside wounds.**
  Flushing with clean water is safer and works.
- **What you cannot scavenge or improvise:** a diagnosis or a clinician. That is why prevention
  carries the weight here.

## When it runs out

- **Soap and clean water matter most** for infection control, more than any dressing. Budget
  them as medical supplies, not household ones (→ 23-02), and learn to make soap (→ 13-09).
- **A household's ability to treat serious infection is limited and shrinks over time.** That
  should change how you weigh risk for good. Tool safety (→ 16-02), fire safety (→ 12-03),
  sanitation (→ 13-01) and water treatment (→ 03-04) become medical priorities, not chores.
- **Substitute:** cleanliness, drainage, rest, fluids, food and time. That is what people had
  before antibiotics, and it worked more often than people assume, though not always. That is
  what → 12-16 is for.
- **The best long-term move is a person, not a supply.** Finding and supporting someone with
  real medical training in your community is worth more than any stockpile (→ 18-01, → 18-03).

## Phase notes

- **A (at home):** clean water and soap are available, and pharmacies may work for a while.
  **Use the early period to settle tetanus status, talk to a clinician and build the hygiene
  system.** Early is when medical problems can still be solved.
- **B (moving):** hygiene gets worse exactly when wound risk rises. Carry soap and hand
  sanitiser, clean thoroughly at each stop with real water, and treat any wound from the road as
  dirty (→ 12-02).
- **C (resettled):** further from care, more injuries, and animals in the picture, which adds
  bites, scratches and diseases caught from animals (→ 05-04, → 05-15). **Where you put the
  latrine matters enormously at a new site** (→ 13-07): getting waste and water apart on day one
  prevents the illness that would otherwise arrive in month two.

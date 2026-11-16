---
id: 02-04-cl04-food-allergy
section: 02-medical-conditions
title: "CL-04. Food allergy (child or adult)"
version: 2
revised: 2026-11-16
layer: condition
danger_level: critical
phase: [A, B, C]
tags: [condition library, food allergy, allergens, label reading, cross-contact, stockpile, unlabeled food, barter, communal meals, anaphylaxis]
derived_from: [02-08-allergen-safe-food-plan, 02-06-hugh-anaphylaxis-action-plan, 12-11-chronic-conditions]
sources:
  - fda-food-allergies-what-you-need-to-know
  - us-fda-food-allergies-627fb6
  - american-academy-of-pediatrics-aap-allergy-and-anaph-3e6f49
  - world-health-organization-cholera-outbreaks-q-and-a-162558
related:
  - 02-03-cl03-anaphylaxis
  - 02-13-cl13-infant-feeding
  - 04-01-calorie-and-stockpile-math
  - 04-02-building-a-pantry
  - 04-19-freeze-dried-stockpile
  - 05-06-foraging-and-deadly-look-alikes
  - 13-10-dishwashing-and-food-hygiene
  - 18-01-mutual-aid
  - 18-02-barter-and-trade-goods
  - 20-02-child-safety-offgrid
  - 22-03-go-bags-and-kits
  - 01-07-evacuating-with-medical-needs
  - 30-19-dc18-unlabeled-food-and-allergies
  - 30-15-dc14-questionable-food
  - 30-05-dc04-expired-medication
  - 30-27-dc26-allergy-safe-food-reserve
cards: [DC-18, DC-14, DC-04, DC-19, DC-26]
explainers: [EX-14]
promote_when: [has.condition.CL-04, has.anaphylaxis]
photo_slots:
  - { id: safe-food-shelf, caption: "Our allergy-safe food shelf, labelled, above the other food" }
  - { id: allergen-card, caption: "The allergen card posted where food is made" }
figures: []
plates: []
condition: CL-04
gear: null
explainer: null
card: null
review_pass: null
---

# CL-04. Food allergy (child or adult)

**What this page is for.** In a crisis, food becomes unlabelled, shared, donated, traded,
scavenged, foraged and cooked in one pot over one fire. Every one of those is a way for a
food-allergic person to eat their allergen. When epinephrine is limited and no ambulance comes
(→ 02-03), **avoidance stops being the cautious option and becomes the main defence.** This
module is how to build a food supply around the allergic person, read labels while they exist,
cook without cross-contact, and handle the food you did not buy.

{{#if has.condition.CL-04}}**Someone in your household has this condition.** This module is at the front of the medical section for you.{{else}}**Nobody in your household is marked with this condition.** The module stays in the binder for guests, neighbours, and allergies that appear later.{{/if}}

Your household's allergy rows: {{#each allergies as a}}**{{a.member}}**: {{a.allergen}} ({{a.severity}}). {{else}}none entered.{{/each}}

> **SAFETY**
> - **A reaction is treated on → 02-03: epinephrine first.** This page is prevention.
> - **If you cannot name every ingredient and how it was prepared, the allergic person does not
>   eat it** unless your household has chosen otherwise on the card: {{choice DC-18}} (→ 30-19).
> - **A mild reaction does not mean a mild allergy.** FDA says any allergic reaction has the
>   potential to lead to anaphylaxis (FDA, Food Allergies: What You Need to Know). Treat the
>   symptoms in front of you, not the history.

## Do this now

**The person may have eaten their allergen:**
1. **Watch them closely** and keep epinephrine in hand. Any sign of anaphylaxis (→ 02-03):
   **give epinephrine at once.**
2. **Stop the meal**: FDA says stop eating the food immediately. Keep what they ate (the
   package, the dish) to work out what it was (FDA, Food Allergies: What You Need to Know).
3. **Do not make them vomit.** Wipe the mouth and hands.
4. **Stay with them for hours**, with a device in reach.

**Preparation, this week:**
1. **Post the allergen card** where food is made: each person's allergens, the words to look for
   on labels, and "if in doubt, no".
2. **Mark the safe food** "SAFE FOR ______" in thick marker, and store it apart.
3. **Ask the allergist the questions in part 7** and write the answers.

{{photo allergen-card}}

## 1. What it is

A food allergy is the immune system treating a food as an attack. Reactions range from itching
and hives to anaphylaxis, which can kill in minutes. There is no household cure; the plan is to
avoid the food and to be ready to treat a reaction.

## 2. What runs out, and how fast

| What | Clock | When it is gone |
|---|---|---|
| **Safe, labelled food** | Count it separately from the household's food (→ 04-01). It is usually the shorter clock. | The person depends on food nobody can verify. |
| **Epinephrine** | Printed expiry (→ 02-03). | No treatment for a reaction. |
| Labels and ingredient lists | Gone once food is repackaged, traded or donated. | Verification is impossible. |
| Dedicated cookware | Lost, borrowed, mixed up. | Cross-contact. |
| Wash water and soap | Scarce off-grid (→ 13-10). | Pans and hands carry traces. |

**Write the clock:** safe food for ________ (person) lasts ________ days; on → 23-02 as its own
line.

## 3. Storing safe food without power

- **Keep the labels.** Cut out and file the ingredient panel of anything you repackage into
  buckets or jars, and tape it inside the lid. A bucket of unlabelled flour is a hazard.
- **Label twice, in thick marker:** "SAFE FOR ______" or "NOT SAFE". Assume the person serving
  is tired, cold and working in poor light.
- **Store safe food apart**, on its own shelf or bin, **above** other food so nothing spills into
  it.
- **Depth matters more for the allergic person.** Others can eat whatever is available; they
  cannot. Their staples should have the longest clock in the pantry.

{{photo safe-food-shelf}}

## 4. Day by day without it

When safe food runs short, the pressure to "just try" a doubtful food rises every day. That is
the danger point. Plan now:
- **Who eats the safe food, and when.** Sharing the allergy-safe food with everyone shortens the
  allergic person's runway; holding it as their reserve means everyone else eats other food first.
  This is a decision card: {{choice DC-26}} (→ 30-27).
- **Hunger is survivable; anaphylaxis without epinephrine may not be.** If safe food runs out and
  only unverifiable food remains, that is a reason to move toward supply (→ 01-02), the same way a
  short medicine clock is.

## 5. Warning signs that mean an emergency

Any sign of anaphylaxis after eating, in more than one body system or severe in one: hives with
vomiting, swelling of lips or tongue, cough, wheeze, hoarse voice, faintness, or in a small
child a sudden change in behaviour (FDA, Food Allergies: What You Need to Know; AAP, Allergy
and Anaphylaxis Emergency Plan). Symptoms can start within a few minutes or a few hours of
eating (FDA). **Epinephrine first** (→ 02-03).

## 6. Sick-day basics

- **During illness, keep to food the person has always tolerated.** A sick day is the wrong day
  to find out something new.
- **Oral rehydration** (→ 12-05): commercial packets list their ingredients; check them. The WHO
  home recipe is water, sugar and salt only (WHO, Cholera Q&A).
- **Medicines and supplements can hide allergens** (for example in coatings and flavourings).
  Ask the pharmacist now and note any on the card.

## 7. What to stock, and how much

**Labels, while they exist.** US law requires packaged foods to declare the **nine major food
allergens**: milk, eggs, fish, crustacean shellfish, tree nuts, peanuts, wheat, soybeans and
sesame (FDA, Food Allergies: What You Need to Know). They appear in the ingredient list or a
"Contains" line. Three things catch people out:
- **Anything outside those nine is not called out.** Banana, mustard, legumes other than peanut
  and soy, and many others are found only by reading the **full ingredient list**.
- **"May contain" and "made in a facility with" lines are not required by law** (FDA, Food
  Allergies), so their absence proves nothing. Treat them as a yes until the allergist says
  otherwise.
- **The FDA labelling law does not cover everything.** Meat, poultry and egg products (regulated
  by USDA), raw farm produce, and food wrapped at a counter after you order it are outside it
  (FDA, Food Allergies).
- **Highly refined oils made from a major allergen are exempt** from the allergen declaration
  under US labelling law (FDA, Food Allergies). Some allergic people tolerate them; that is an
  allergist's call, not a book's.

**What a food allergy does to a normal stockpile.** Many classic prepper staples hold common
allergens: peanut butter, canned fish, powdered egg, soy-based "vegetable oil", ration bars,
freeze-dried meals, trail mix, bread and crackers (often sesame, egg, soy, milk, wheat). **Build
the allergic person's supply from single-ingredient staples you can verify**: plain rice, plain
oats, plain dried beans (other than their allergen), plain flour if tolerated, sugar, salt, plain
canned vegetables and fruit, meat you preserved yourself. Check every freeze-dried pouch and bar
by its label (→ 04-19).

**Ask the allergist now, while you can, and write the answers here:**

| Question | Answer |
|---|---|
| Does a trace or "may contain" matter for this person? | ______________________ |
| Highly refined oils from the allergen: tolerated? | ______________________ |
| Baked forms (egg or milk baked into bread): tolerated? | ______________________ |
| Related foods that may cross-react (other nuts, legumes, shellfish, edible insects)? | ______________________ |
| Safe brands they reliably eat | ______________________ |
| Can new foods be introduced, and under what conditions? | ______________________ |
| Can cooking steam or smoke from the allergen cause a reaction? | ______________________ |

**Stock arithmetic.** The medicines tagged for this condition in settings are printed; if none are tagged, every household medicine row is, so use the ones for this condition.

| Item | On hand | Used per day | Days on hand | Days you want | Still to get |
|---|---|---|---|---|---|
{{#each meds_for.CL-04 as m}}
| {{m.name}} {{m.strength}} ({{m.member}}) | ____ | ____ | ____ | ____ | ____ |
{{else}}
{{#each meds as m}}
| {{m.name}} {{m.strength}} ({{m.member}}) | ____ | ____ | ____ | ____ | ____ |
{{/each}}
{{/each}}
| Safe staple: ____________ | ____ | ____ | ____ | ____ | ____ |
| Safe staple: ____________ | ____ | ____ | ____ | ____ | ____ |
| Safe staple: ____________ | ____ | ____ | ____ | ____ | ____ |
| Safe snacks for the go-bag | ____ | ____ | ____ | ____ | ____ |
| Dedicated pot, pan, spoon, cutting board (one colour) | ____ | | | ____ | ____ |
| Thick markers and labels | ____ | | | ____ | ____ |
| Allergen card, wallet copy and go-bag copy | ____ | | | ____ | ____ |

## 8. Sourcing when the pharmacy is closed

Here the "pharmacy" is the food supply.

**Cooking over one fire without cross-contact:**
- **Cook the allergic person's food first**, in clean, dedicated cookware, before the allergen
  enters the kitchen.
- **One colour of pot, pan, spoon and board** for safe food, stored apart. A single shared spoon
  defeats everything else.
- **Scarce wash water makes dedicated gear more important, not less**, because thorough washing
  between uses stops being possible (→ 13-10).
- **Surfaces and hands:** boards, the table, the grill grate, the server's hands.
- **Children share food.** Small children hand each other things; the whole household enforces
  the rule constantly (→ 20-02).

**The three highest-risk sources:**
1. **Donated and communal food.** Well meant and impossible to verify. Take it for the others if
   you wish (→ 18-01).
2. **Traded food.** The same problem, plus a reason for the trader to overstate it (→ 18-02).
3. **Foraged food.** Unlabelled by definition, with misidentification risk too (→ 05-06). The
   allergic person should not be the one who tries a new wild food.

Your household's rule for these is the card: {{choice DC-18}} (→ 30-19). Food past its date,
dented cans and food from a failed freezer are a separate card: {{choice DC-14}} (→ 30-15).

**When scavenging for the allergic person:** sealed, labelled, intact original packaging only;
single-ingredient wherever possible. Bulk bins, repackaged goods and damaged labels are out.
Your own garden is the best possible source: you know everything in it.

**Raising food at home** can bring an allergen on site (hens bring eggs; fishing brings fish).
That can be managed with separate handling and cookware, but ask the allergist first.

## 9. Power and devices

None for the allergy itself. Epinephrine storage is on → 02-03. A **freezer failure** forces
quick decisions about food; the allergic person's safe frozen food is eaten or preserved first,
by them.

## 10. Travel and evacuation

- **Carry the allergic person's food for the whole trip and more.** Shelter meals, roadside
  charity and communal pots are the highest-risk food they will meet (→ 01-07, → 22-03).
- **The allergen card** goes with them, in their pocket and in the go-bag: allergens, "no
  unlabelled food", epinephrine location, and how to give it.
- **Say it plainly** to anyone who feeds them, every time.

## 11. Decision cards that apply

- **Unlabelled, traded or scavenged food for the allergic person:** {{choice DC-18}} (→ 30-19).
- **Allergy-safe food held in reserve for the allergic person:** {{choice DC-26}} (→ 30-27).
- **Food past its date, dented cans, failed freezer:** {{choice DC-14}} (→ 30-15).
- **Expired epinephrine:** {{choice DC-04}} (→ 30-05).
- **When to leave:** {{choice DC-19}} (→ 30-20). Running out of safe food is a trigger.

## 12. My meds

Medicines your household tagged for this condition in settings are printed below. **If none
are tagged, every medicine row your household entered is printed instead: tick the rows for
this condition (epinephrine, antihistamines, inhalers)** and cross out the rest. Fill any blank columns by hand from the boxes
and bottles, and add untagged medicines in the empty rows.

| For this? | Who | Medicine | Strength | Schedule | Fridge? | If doses are missed (prescriber's words) | Where kept | Days on hand | Expires |
|---|---|---|---|---|---|---|---|---|---|
{{#each meds_for.CL-04 as m}}
| ☐ | {{m.member}} | {{m.name}} | {{m.strength}} | {{m.schedule}} | {{m.refrigerated}} | {{m.if_missed}} | {{m.where_kept}} | {{m.days_on_hand}} | {{m.expiry}} |
{{else}}
{{#each meds as m}}
| ☐ | {{m.member}} | {{m.name}} | {{m.strength}} | {{m.schedule}} | {{m.refrigerated}} | {{m.if_missed}} | {{m.where_kept}} | {{m.days_on_hand}} | {{m.expiry}} |
{{else}}
| ☐ | (no medicines entered yet) | | | | | | ____ | ____ | ____ |
{{/each}}
{{/each}}
| ☐ | ____ | ____ | ____ | ____ | ____ | ____ | ____ | ____ | ____ |
| ☐ | ____ | ____ | ____ | ____ | ____ | ____ | ____ | ____ | ____ |
| ☐ | ____ | ____ | ____ | ____ | ____ | ____ | ____ | ____ | ____ |

**Allergen card** (copy it; post one in the kitchen, one in the wallet, one in the go-bag):

| Person | Allergens that cause anaphylaxis | Other reactions | Tolerated (allergist confirmed) | Epinephrine kept |
|---|---|---|---|---|
| ________ | ________________ | ________________ | ________________ | ________ |
| ________ | ________________ | ________________ | ________________ | ________ |

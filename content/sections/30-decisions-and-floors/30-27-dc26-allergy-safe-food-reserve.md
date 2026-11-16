---
id: 30-27-dc26-allergy-safe-food-reserve
section: 30-decisions-and-floors
title: "DC-26. Holding the allergy-safe food in reserve for the allergic person"
version: 1
revised: 2026-11-16
layer: card
danger_level: caution
phase: [A, B, C]
tags: [decision card, food allergy, anaphylaxis, rationing, safe food, stockpile, runway]
derived_from: [02-08-allergen-safe-food-plan]
sources:
  - us-fda-food-allergies-627fb6
  - american-academy-of-pediatrics-aap-allergy-and-anaph-3e6f49
related: [02-04-cl04-food-allergy, 02-03-cl03-anaphylaxis, 04-01-calorie-and-stockpile-math, 04-02-building-a-pantry, 04-18-meal-planning-scarcity, 04-19-freeze-dried-stockpile, 23-02-master-consumables-table, 01-02-go-no-go-decision, 30-19-dc18-unlabeled-food-and-allergies]
cards: [DC-26, DC-18, DC-19]
explainers: [EX-14]
promote_when: [has.food_allergy, has.condition.CL-04]
card: DC-26
options:
  - id: share-everything
    label: "Share everything: all safe food is eaten by everyone"
    summary: "Food that is safe for the allergic person is part of the household's general stock and is eaten by everyone, in the normal order. The household plans one menu that suits all, for as long as it lasts."
  - id: reserve-for-allergic
    label: "Reserve it: everyone else eats other stock first"
    summary: "Food verified safe for the allergic person is set aside as that person's reserve. Everyone else eats the food the allergic person cannot eat first, and the safe stock is used by others only when nothing else is left."
settings_summary: "When someone has a food allergy, only part of the stockpile is safe for them: food whose label has been read and checked against their allergens. Everyone else can eat almost anything. If the whole household eats the safe food in the normal order, it runs out first for the one person who has no other choice, and the pressure to give them doubtful food grows every day. A reaction with no ambulance may need more than one dose of epinephrine. Keeping the safe food as their reserve stretches it, but the others eat less-liked food first, which can feel unfair and can be hard to keep to. What helps most: stocking enough safe food for everyone (removes most of the question); tracking the safe food's own runway (reduces it a lot)."
review_pass: null
---

# DC-26. Holding the allergy-safe food in reserve for the allergic person

**What this page is for.** In a household where one person has a food allergy, the food that is
safe for them is usually a small part of the whole stockpile. This card is about who eats that
safe food, and when. It is a rationing choice, not a medical rule, and households answer it
differently.

> **SAFETY.** In anaphylaxis, **give epinephrine first** and think second (→ 02-03). The rule
> for food that has no label is a separate card: {{choice DC-18}} (→ 30-19). Running out of safe
> food is a reason to move toward supply (→ 01-02).

## 1. The thing, in plain words

- A **food allergy** is the immune system reacting to a food protein as if it were a threat. The
  worst reaction, **anaphylaxis**, closes the throat and drops the blood pressure (→ 02-04).
- **Safe food** here means food whose full ingredient label has been read and checked against the
  person's allergen list, or food made at home from such ingredients, in clean pots.
- A **reserve** is food set aside and not eaten in the normal order.
- The **runway** is how many days the food lasts at the rate it is being eaten (→ 04-01).

{{#each allergies as a}}{{a.member}}: {{a.allergen}} ({{a.severity}}). {{else}}No allergy rows entered in settings.{{/each}}

## 2. The rule, and why it was set

There is no agency rule about who eats which food first. The rules that drive this card are the
allergy rules:

- **FDA:** "People with food allergies should read labels and avoid the foods they are allergic
  to." US law requires the nine major allergens (milk, eggs, fish, crustacean shellfish, tree nuts,
  peanuts, wheat, soybeans and sesame) to be named on packaged food. "May contain" statements are
  voluntary, and raw farm products, highly refined oils and most unpackaged food are not covered
  (FDA, Food Allergies).
- **The emergency plan:** give epinephrine at once for severe symptoms, call 911, and give a second
  dose "if symptoms get worse, continue, or do not get better in 5 minutes" (American Academy of
  Pediatrics, Allergy and Anaphylaxis Emergency Plan).

**Why it matters for the stockpile:** a label is the only practical way to know what is in food.
Once the labelled safe food is gone, the allergic person is left with food nobody can verify, and
no ambulance behind the epinephrine.

## 3. How it actually hurts people

**Sharing everything:** the household eats in the normal order, oldest first. Much of the
allergy-safe food is ordinary food (plain rice, oats, canned vegetables), so it goes as fast as
everything else. Weeks later the others still have peanut butter, fish and egg powder; the
allergic person has almost nothing. The household now faces the unlabelled-food card (→ 30-19)
every day, under hunger, and each reaction uses up epinephrine that may not be replaced.

**Reserving:** the others eat their less-liked food first and watch "the good rice" sit on a
shelf. Children notice. In a long shortage, a parent may go hungrier while food sits reserved,
and a rule that feels unfair is a rule people quietly break, usually on a bad night.

## 4. What makes it safer

**Removes most of the question**
- **Stock enough safe food for everyone.** Build the bulk staples around foods the allergic person
  can eat, so one pot feeds the whole household and nothing needs reserving (→ 04-02, → 02-04).

**Reduces it a lot**
- **Track the safe food's runway separately** from the household total (→ 04-01, → 23-02). The
  number that matters for the allergic person is their own.
- **Label every safe container** "SAFE FOR ______" and keep it on its own shelf, above other food,
  so the rule can be followed in the dark (→ 02-04).
- **Plan substitutions now** against the allergen list, not in the moment.

**Reduces it a little**
- Grow food you can trace from seed to plate (Section 05).
- Agree the rule out loud with every adult and older child before it is needed.

## 5. The options

**`share-everything`: Share everything: all safe food is eaten by everyone.**
You give up: the longer runway for the allergic person. You accept: that their safe food may run
out well before the household's food does, and that the unlabelled-food decision (→ 30-19)
arrives sooner.

**`reserve-for-allergic`: Reserve it: everyone else eats other stock first.**
You give up: the others' choice of food while other stock lasts. You accept: a rule that can feel
unfair, that must be explained and kept, and that leaves the others eating the less-liked food
first.

If more than one person has allergies, write the answer for each person beside the box.

## 6. Our choice

{{card DC-26}}

---
id: 30-19-dc18-unlabeled-food-and-allergies
section: 30-decisions-and-floors
title: "DC-18. Feeding a food-allergic person unlabeled, traded or scavenged food"
version: 2
revised: 2026-11-16
layer: card
danger_level: critical
phase: [A, B, C]
tags: [decision card, food allergy, anaphylaxis, unlabeled food, barter, scavenging, cross-contact, epinephrine]
derived_from: [02-08-allergen-safe-food-plan, 02-07-epinephrine-storage-and-supply]
sources:
  - us-fda-food-allergies-627fb6
  - american-academy-of-allergy-asthma-and-immunology-aa-7f3939
  - american-academy-of-pediatrics-aap-allergy-and-anaph-3e6f49
  - cdc-recognizing-and-responding-to-anaphylaxis-645825
  - american-academy-of-allergy-asthma-and-immunology-aa-1ca82e
related: [02-04-cl04-food-allergy, 02-03-cl03-anaphylaxis, 18-02-barter-and-trade-goods, 22-02-scavenging-field-guide, 05-06-foraging-and-deadly-look-alikes, 30-05-dc04-expired-medication, 30-15-dc14-questionable-food]
cards: [DC-18, DC-04, DC-14]
explainers: [EX-14]
promote_when: [has.anaphylaxis, has.condition.CL-04]
card: DC-18
options:
  - id: never
    label: "Never: only food with a full, readable label"
    summary: "The allergic person eats only food whose full ingredient label has been read, or food the household made itself from labelled ingredients in a clean kitchen. No traded, donated, scavenged or foraged food, ever."
  - id: single-ingredient-only
    label: "Single-ingredient foods only"
    summary: "Unlabelled or traded food is allowed only if it is one plain, recognisable ingredient (whole rice, dry beans, a whole vegetable or fruit, a whole cut of meat) that is not on the person's allergen list, washed and cooked in the household's own clean pots."
  - id: with-epinephrine-in-hand
    label: "With epinephrine in hand, by our own line"
    summary: "Unlabelled food may be tried by the household's own written line, only with in-date epinephrine in hand, an adult who knows the plan watching, the first taste small, and never alone or at night."
settings_summary: "When stores close, food arrives without labels: bartered, donated, scavenged, repackaged or foraged. For a person with a food allergy, a label is how you find the hidden egg, peanut, milk, sesame or soy. US law requires the nine major allergens to be declared on packaged food, but only while labels exist. Without one, a trace of the allergen, or a pot or spoon that touched it, can cause anaphylaxis: throat swelling, trouble breathing, collapse, death within minutes to hours without epinephrine. With no ambulance, epinephrine is the only treatment, and a reaction can need more than one dose. What helps most: a deep stock of verified safe food and kept labels (removes most of it); single-ingredient foods cooked in the household's own pots (reduces it a lot)."
review_pass: { date: "2026-11-16", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "Avoid/carry re-cited to AAAAI Anaphylaxis page; unsupported 'reactions return' replaced by AAP 5-minute second-dose wording." }
---

# DC-18. Feeding a food-allergic person unlabeled, traded or scavenged food

**What this page is for.** In a long emergency, food stops coming with labels. For someone with
a serious food allergy that is the moment the danger jumps. This card explains why, what makes
it safer, and what the household decides for each allergic person.

> **SAFETY.** In anaphylaxis, **give epinephrine first** and think second (→ 02-03).
> Children do not have access to firearms, fuel, medications or chlorine products (floor,
> → 30-01).

## 1. The thing, in plain words

A **food allergy** is the immune system reacting to a food protein as if it were a threat.
**Anaphylaxis** is the most severe reaction: swelling of the throat or tongue, trouble
breathing, wheezing, vomiting, a drop in blood pressure, collapse (CDC, Recognizing and
Responding to Anaphylaxis). **Epinephrine** is the drug that treats it, usually from an
auto-injector. **Cross-contact** means a safe food picking up traces of an allergen from a pot,
a spoon, a cutting board or hands.

{{#each allergies as a}}{{a.member}}: {{a.allergen}} ({{a.severity}}). {{else}}No allergy rows entered in settings.{{/each}}

## 2. The rule, and why it was set

- FDA: US food labels must declare the **nine major allergens**: milk, eggs, fish, crustacean
  shellfish, tree nuts, peanuts, wheat, soybeans and sesame (FDA, Food Allergies).
- Allergy specialists' advice: **avoid the allergens** that trigger your reactions, and if you are
  at risk of anaphylaxis, **carry epinephrine** (AAAAI, Anaphylaxis). FDA: "People with food
  allergies should read labels and avoid the foods they are allergic to." The emergency plan:
  epinephrine at once for severe symptoms, call 911, and a second dose "if symptoms get worse,
  continue, or do not get better in 5 minutes" (AAP, Allergy and Anaphylaxis Emergency Plan).

**Why:** the label is the only practical way to find an allergen hidden in a sauce, bread,
ration bar or seasoning. Without the label there is no way to know, and the amount that triggers
a reaction can be very small.

## 3. How it actually hurts people

A neighbour trades a loaf of bread. It looks plain; it was made with egg and brushed with
sesame. Or plain rice is cooked in a pot that just held peanut stew. The allergic child eats it.
Within minutes: itching mouth, hives, coughing, vomiting, then trouble breathing (symptoms
usually start within 5 to 30 minutes, AAAAI). Epinephrine is given; the symptoms do not get
better in 5 minutes and a second dose is needed (AAP plan). With no ambulance and limited
devices, each exposure uses up the stock that protects against the next one.

Foraged food adds two problems: a new food can trigger a new allergy, and some wild plants are
simply poisonous (→ 05-06).

## 4. What makes it safer

**Removes most of the risk**
- **A deep stock of verified safe food** for the allergic person, bought by brand, labels read
  and kept (cut out and filed when food is repackaged), marked "SAFE for ______" (→ 02-04).
- **The allergic person's own food first**; trade other food, not theirs.

**Reduces it a lot**
- **Single-ingredient foods only** from outside sources: whole grains, dry beans, whole
  vegetables and fruit, whole cuts of meat or fish if those are safe for that person. Nothing
  mixed, baked, sauced or seasoned by someone else.
- **Wash it and cook it in your own clean pots**, with utensils kept only for the allergic
  person.
- **Epinephrine in date, in reach, and enough of it** (→ 02-03, → 30-05).

**Reduces it a little**
- Ask the giver exactly what is in it and how it was made; remember that answers can be wrong.
- First taste small, in daylight, with an adult who knows the plan watching, never alone.
- A written allergen card that travels with the person and goes to anyone who feeds them.

## 5. The options

**`never`: Never: only food with a full, readable label.**
You give up: food you cannot verify, which may mean a narrower diet and hunger if the safe stock
runs low. You accept: needing a larger safe stock.

**`single-ingredient-only`: Single-ingredient foods only.**
You give up: mixed, baked and prepared foods from outside. You accept: a small cross-contact risk
from how the food was grown, stored or handled before it reached you.

**`with-epinephrine-in-hand`: With epinephrine in hand, by our own line.**
You give up: avoidance as the main protection. You accept: that a reaction is possible and that
epinephrine, a watching adult and the household's own written line are the protection.
Write the line here: ____________________________________________

If more than one person has allergies, answer for each person beside the box.

## 6. Our choice

{{card DC-18}}

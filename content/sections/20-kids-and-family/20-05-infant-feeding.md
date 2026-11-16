---
id: 20-05-infant-feeding
section: 20-kids-and-family
title: "Feeding babies and toddlers without the supply chain"
version: 2
revised: 2026-11-16
layer: core
danger_level: critical
phase: [A, B, C]
tags: [infant, toddler, breastfeeding, nursing, formula, whole milk, water, bottles, shortage, weaning]
derived_from: [20-05-infant-feeding]
sources:
  - cdc-breastfeeding-infant-and-toddler-nutrition-5d9a3a
  - cdc-infant-formula-preparation-and-storage-29a24f
  - cdc-infant-and-toddler-nutrition-foods-and-drinks-fo-e9c989
  - cdc-about-hygiene-handwashing-and-infection-preventi-61142e
  - cdc-cleaning-infant-feeding-items
  - who-powdered-infant-formula-2007
  - ife-core-group-operational-guidance-v3
  - usda-hhs-dietary-guidelines-for-americans-2020-2025-4b2013
  - aap-choking-prevention
  - fda-homemade-infant-formula-advisory
  - cdc-breast-milk-storage-and-preparation
  - aap-recommended-drinks-young-children-r16
related: [20-01-toddler-and-infant-needs, 20-06-diapers-and-hygiene, 02-13-cl13-infant-feeding, 02-12-cl12-pregnancy-birth-and-postpartum, 03-01-daily-water-needs, 03-04-purifying-water, 04-01-calorie-and-stockpile-math, 04-14-powdered-and-canned-dairy, 04-17-food-safety-power-outage, 12-05-common-illness-and-dehydration, 12-18-choking-and-cpr, 13-10-dishwashing-and-food-hygiene, 01-02-go-no-go-decision, 22-03-go-bags-and-kits, 23-02-master-consumables-table, 02-04-cl04-food-allergy]
cards: []
explainers: [EX-06]
promote_when: [has.infant, has.nursing, has.condition.CL-13]
photo_slots: []
figures: []
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: { date: "2026-11-16", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "Matched to CL-13 and CDC: dilution and homemade-formula harms as CDC/FDA say; under 2 months, sanitise daily per CDC; breast milk times re-read; milk 16 oz per AAP; evaporated-milk ratio and 48 h RTF removed." }
---

# Feeding babies and toddlers without the supply chain

**What this page is for.** The household routine for feeding a baby or toddler when stores,
power and clean tap water may be gone: the three feeding paths, how to hold each one together,
the right milk at each age, and what to do in a formula shortage. The medical side (the nursing
parent's own medicines, warning signs in a baby, and the formula clock as a condition) is the
infant-feeding module, → 02-13. The water arithmetic is → 03-01.

> **SAFETY. Two rules that are absolute.**
>
> **(1) Never dilute infant formula to make it last longer.** Too much water means the formula
> will not meet the baby's nutritional needs; too little water strains the baby's kidneys and
> digestive system (CDC, Infant Formula Preparation and Storage). Mix exactly as the label
> says, every time.
>
> **(2) Never make homemade infant formula.** FDA advises against it: home recipes, including
> ones from evaporated milk, goat milk, plant milks or "old recipes", have caused serious
> illness and hospital stays in babies (FDA, Homemade Infant Formula advisory; → 02-13). A
> baby's needs are specific and unforgiving. **A formula shortage is a medical and public-health emergency, not a kitchen
> project.**
>
> This page gives **no formula recipes and no dilution ratios**, on purpose. It does print the
> holding times and water temperatures as CDC and WHO publish them, because off-grid this binder
> may be the only reference.

**Your youngest:** {{#each infants as i}}{{i.label}} ({{i.age_text}}); {{/each}}{{#if !has.infant}}no member under 2 is entered.{{/if}}{{#if has.nursing}} **Someone in your household is nursing.**{{/if}}

## Do this now

1. **Ask your baby's doctor now:** "What happens if we cannot get our milk or formula for a
   month?" Write the answer in the box below.
2. **If formula is in use, stock it deeply and rotate it.** It expires. It is a short-runway,
   no-substitute supply; treat it as seriously as insulin (→ 23-02).
3. **Secure safe water for preparation and cleaning** (→ 03-04). That need does not relax in a
   crisis.
4. **Write each child's actual feeding in pen** and re-date it every few months. Every plan on
   this page branches on it:

```
AS OF: __________  Child: __________  Age: ______
Breastfed?  YES / NO   When: ____________________
Formula?    YES / NO   Brand and type: __________  Amount per day: ______
Family foods?  YES / NO     Milk (12 to 23 months): WHOLE  ______ oz/day
Doctor's answer for "no formula or milk for a month": ______________
____________________________________________________________________
```

## The three feeding paths

| Path | How it holds up in a crisis | What it needs |
|---|---|---|
| **Breastfeeding** | **The most robust there is:** no supply chain, no water treatment, no sterilising, right temperature, protection against infection (CDC) | **The nursing parent fed, watered and rested** |
| **Formula** | **The most fragile:** a manufactured product that needs safe water and clean equipment | Supply, safe water, fuel and water for cleaning |
| **Family foods (from about 12 months)** | **More robust every month:** the child eats what the household eats | Household food, allergy care |

Every month a child moves along the third path, the household loses a supply-chain dependency.

## Breastfeeding

- **It is the most crisis-resistant way to feed a baby** (CDC), and the immune protection comes at
  exactly the time infection risk rises (→ 13-11).
- **The nursing parent's food and water are not optional.** The Dietary Guidelines add about 330
  calories a day in the first 6 months of nursing and about 400 in the second 6 months (USDA/HHS,
  Dietary Guidelines for Americans 2020-2025), and the water plan adds extra (→ 03-01). This is the
  thing people most often forget. {{#if has.nursing}}Your water floor already includes it:
  {{ derived.water.floor_gal_day }} gallons a day for the household.{{/if}}
- **Stress and exhaustion affect supply**, and a crisis brings both. Rest, food, water and support
  are the practical help (→ 21-02). Sudden weaning under stress is a real risk: protecting the
  nursing parent **is** the baby's food security.
- **Expressing and storing milk** (CDC, Breast Milk Storage and Preparation, as published):
  - Freshly expressed: **up to 4 hours at room temperature** (77 °F or cooler); **up to 4 days in
    a fridge** (40 °F or colder); frozen, **about 6 months is best, 12 months acceptable**.
  - Thawed milk: once at room temperature or warmed, within 2 hours; thawed in the fridge,
    within 24 hours of fully thawing; **never refreeze**.
  - Left over from a feed: use within 2 hours or throw away. Never thaw or heat breast milk in a
    microwave.
  - In winter an unheated porch or shed works as a fridge only if a thermometer shows it holding
    between 32 and 40 °F (→ 04-09). In summer it does not (→ 09-10).
- **Clean pump parts and bottles** as in CDC's infant feeding-item guidance: wash, then sanitise
  (CDC, How to Clean, Sanitize, and Store Infant Feeding Items; → 13-10).
- **Medicines while nursing** (the parent's own) are in → 02-13.

## Formula

**Follow CDC's guidance and the label exactly.**
- **Safe water every time** (→ 03-04). **Boil the water** (a rolling boil, then let it cool).
- **For a baby younger than 2 months, born early (before 37 weeks), or with a weak immune
  system:** CDC says boil the water, **wait about 5 minutes**, then mix in the powder, to protect
  against *Cronobacter* germs that can live in the powder; WHO's guidance is to mix powder into
  water of at least **158 °F (70 °C)** (CDC, Infant Formula Preparation and Storage; WHO/FAO,
  Safe Preparation of Powdered Infant Formula). **Then cool the bottle** and test a few drops on
  your wrist: warm, not hot. Never microwave a bottle (CDC).
- **Clean bottles and feeding items** after every use. CDC says sanitise them daily (or more
  often) if the baby is less than 2 months old, was born prematurely, or has a weakened immune
  system; one way is to boil the taken-apart items for 5 minutes. Daily sanitising may not be
  needed for older, healthy babies if items are cleaned carefully after each use (CDC, How to
  Clean, Sanitize, and Store Infant Feeding Items). This costs real water and fuel (→ 13-10);
  budget it.
- **Holding times** (CDC, as published):
  - Mixed formula: **use within 2 hours of mixing**; if it will not be used within 2 hours,
    refrigerate it at once and use it within 24 hours.
  - **Once a feed starts, use it within 1 hour** and throw away what is left in the bottle
    (saliva lets germs grow).
  - Opened ready-to-feed: capped and refrigerated, used within the time printed on its label;
    same 1-hour rule once a feed starts.
  - **No fridge: mix one feed at a time.**
  - Opened powder: lid tight, cool and dry, not in the fridge; most must be used within 1 month
    of opening (check the label). Never use formula after its "Use By" date (CDC).
- **Never add anything to a bottle:** no cereal, no sugar, no honey.
- **Ready-to-feed formula needs no water and no mixing.** That makes it right for go-bags and for
  moving (→ 22-03), despite the weight and cost.
- **Powdered formula stores longest** and is right for the bulk stock.
- **Check every label against the household's allergies.** Formulas based on soy and on cow's
  milk both exist (→ 02-04).

## The right milk after 12 months

- **From 12 to 23 months the milk is plain, pasteurised whole milk** (CDC: whole cow's milk from
  12 months, not before; plant milks not before 12 months): about **16 ounces (2 cups) a day**
  (AAP, Recommended Drinks for Children Age 5 and Younger). Nonfat or low-fat milk from age 2
  (AAP). Toddler "transition" milks are unnecessary for most children (AAP).
- **Most pantries stock nonfat dry milk.** That is cooking milk and milk for over-2s, **not
  toddler milk**. Stock for a toddler: **whole-milk powder** or **shelf-stable (UHT) whole milk**,
  rotated (→ 04-14).
- **Canned evaporated milk** is another shelf-stable milk (→ 04-14). Whether it, made up as its
  label directs, can stand in for whole milk for your child over 12 months is a question for
  the child's doctor now: write the answer in the box above. It is **never infant formula** and
  never the "homemade formula" of the warning above.
- **If none of these is available,** the fat comes from the family plate: butter or ghee, oils,
  full-fat dairy where there is any, eggs if no allergy forbids them. Ask the child's doctor now
  and write the answer in the box above. Milk still needs safe handling (→ 04-17).

## A formula shortage: what to actually do

The right actions all face outward:
1. **Contact the baby's doctor at once.** They have options and information you do not.
2. **Contact the pharmacy, WIC if you use it, and public health.** Shortages are handled as public
   health matters, and relief agencies follow international guidance on feeding babies in
   emergencies (IFE Core Group, Infant and Young Child Feeding in Emergencies).
3. **Ask the clinician which alternatives suit a child of this age.** At 12 months there are more
   options than at 2 months; that is a clinician's call.
4. **Ask other parents and the community** (→ 18-01). Formula sharing happens.
5. **Do not dilute. Do not improvise formula.** Repeated because it is the thing people do.
6. **If there is no access at all, that is a reason to move toward supply** (→ 01-02), the same
   logic as for insulin. It is not a shelter-in-place problem.

## Moving to family foods

From CDC's infant and toddler nutrition guidance (read it in the original if you can):
- **From about 6 months, other foods start alongside breast milk or formula.**
- **By about 12 months, a child eats a good share from the family table.** Lean that way in a
  crisis: every food the child can eat from the household supply removes a dependency.
- **Soft, mashable, small pieces.** The choking list is on → 20-01 (AAP) and the response on
  → 12-18.
- **Variety and nutrient density** need deliberate attention on a stored-food diet (→ 04-18).
- **New allergenic foods:** plan with the child's doctor, especially if a sibling has a food
  allergy (→ 02-04).

## Water for babies

- **Safe water matters more for babies than for adults.** Use CDC's guidance for preparing
  formula and for any water a baby drinks (→ 03-04; what "safe" means: → 29-06).
- **Plain water comes in only from about 6 months, and only a little** (AAP: about 4 to 8 ounces
  a day at 6 to 12 months). Before that, breast milk or formula is the baby's water.
- **In illness, oral rehydration solution (ORS) is the answer, not plain water** (→ 12-05). A
  small child dries out dangerously fast.

## Gear

**Have it now (buy toward this):**

| Item | Why | Notes |
|---|---|---|
| **Formula (if used), deep stock, rotated** | Short runway, no substitute | Check dates; powdered for bulk |
| **Ready-to-feed formula for the go-bag** | No water, no mixing | → 22-03 |
| **Safe water capacity and spare filters** | Preparation needs it | → 03-04 |
| Bottles, nipples, brushes: spares | They wear out and get lost | And a way to sanitise |
| Pot and fuel for boiling water and equipment | Sanitising costs fuel and water | → 07-01, → 13-10 |
| Breastfeeding supplies | Pump parts, storage bags | And the nursing parent's food and water |
| **Whole-milk powder or UHT whole milk (12 to 23 months)** | Nonfat powder is the wrong milk | → 04-14 |
| Shelf-stable toddler foods the child eats | The direction things go | → 20-01 |
| **ORS** | Illness in a baby is a fast emergency | → 12-05 |
| Thermometer for food and cold storage | Holding times depend on temperature | → 04-09 |
| Written feeding plan on each child's card | Any caregiver needs it | → 15-03, → 25-09 |

**Scavenge or substitute:**
- **Family foods**, mashed and softened, after about 12 months (CDC).
- **Other parents and the community** (→ 18-01).
- **Doctor, pharmacy, WIC, public health:** the right channels in a shortage.
- **Clean cloth and boiled water** for cleaning feeding equipment when soap or hot water is short
  (→ 13-10).
- **What you must not substitute: infant formula itself.** No dilution, no homemade recipes, no
  animal-milk "formula". (Whole cow's milk **as a drink for a child over 12 months** is a
  different thing and is fine; other shelf-stable milks for a toddler, ask the doctor.)

## When it runs out

- **Formula is one of the shortest-runway, least replaceable supplies in the binder.** Put it on
  the consumables table (→ 23-02) and check it weekly while it is in use.
- **Runway = cans (or ounces) on hand ÷ daily use.** Work out the number and know it.
- **You cannot ration a baby's food.** Ration everything else to protect it, and answer a
  shortage by **seeking supply**, not stretching what you have.
- **Whole milk's runway:** whole-milk powder, then UHT, then whatever the doctor's answer above
  allows, then fat from the family plate.
- **Escalation trigger:** if a baby's feeding cannot be met, that is a go/no-go event (→ 01-02).
  Decide the threshold in advance.
- **The reassuring part:** this dependency has a natural end. Each month a baby is closer to
  family food.

## By phase

- **A (shelter in place):** stock deeply, keep safe-water capacity, keep in touch with the
  doctor, and move toward family foods as fast as the doctor advises. Stores are the resupply
  window; use it.
- **B (moving):** **ready-to-feed formula** and safe water for everything else. This is the one
  place where the heavy, expensive option is clearly right (→ 22-03). The nursing parent's water
  and food travel first.
- **C (establish):** no resupply. A child eating family food is a much easier problem, and a
  garden, eggs and animals (→ 05-01, → 05-04) make a good toddler diet possible.

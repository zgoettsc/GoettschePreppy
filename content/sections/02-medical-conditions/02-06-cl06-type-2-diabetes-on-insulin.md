---
id: 02-06-cl06-type-2-diabetes-on-insulin
section: 02-medical-conditions
title: "CL-06. Type 2 diabetes on insulin"
version: 3
revised: 2026-11-16
layer: condition
danger_level: critical
phase: [A, B, C]
tags: [condition library, type 2 diabetes, insulin, cold chain, low blood sugar, high blood sugar, sick days, supply clock]
derived_from: [02-02-insulin-without-the-grid, 02-01-t1d-overview-and-supply-math, 02-04-cgm-conservation-and-dka, 02-05-sourcing-insulin-supplies, 12-11-chronic-conditions]
sources:
  - us-fda-information-regarding-insulin-storage-and-swi-6448d3
  - american-diabetes-association-insulin-storage-and-sy-6f1f94
  - american-diabetes-association-switching-between-insu-9c5595
  - cochrane-human-insulin-less-temperature-sensitive-th-28a2b9
  - cdc-type-2-diabetes
  - cdc-low-blood-sugar-hypoglycemia
  - cdc-treatment-of-low-blood-sugar-r7
  - niddk-low-blood-glucose-hypoglycemia-r10
  - cdc-managing-sick-days-18c7c8
  - cdc-diabetic-ketoacidosis-55a7c2
  - american-diabetes-association-dka-ketoacidosis-and-k-f0301a
  - us-fda-best-way-to-get-rid-of-used-needles-and-other-a67780
related:
  - 02-01-cl01-type-1-diabetes-injections
  - 02-05-cl05-type-2-diabetes
  - 02-02-cl02-type-1-diabetes-pump-and-cgm
  - 12-11-chronic-conditions
  - 12-05-common-illness-and-dehydration
  - 12-21-evaporative-cooling-pouches
  - 09-10-power-for-medical
  - 22-06-kit-medical
  - 01-07-evacuating-with-medical-needs
  - 23-02-master-consumables-table
  - 29-07-ex07-refrigerated-medicines
  - 30-01-the-floors
  - 30-09-dc08-heat-exposed-medication
  - 30-05-dc04-expired-medication
  - 30-16-dc15-someone-elses-prescription
cards: [DC-08, DC-04, DC-15, DC-19]
explainers: [EX-07, EX-14]
promote_when: [has.condition.CL-06]
photo_slots:
  - { id: insulin-outage-spot-t2, caption: "Where the insulin goes in an outage, with its thermometer" }
figures: [fig-insulin-cooler-barrier]
plates: []
condition: CL-06
gear: null
explainer: null
card: null
review_pass: { date: "2026-11-16", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "FDA switching/mixes/once-weekly text re-checked word for word; Awiqli storage window added as published; ADA vs FDA difference noted; meds_for tables. L8 (G31): ADA disaster switching sheet (Aug 2020, re-read from archive and live PDF, identical) printed as published next to FDA's text, not reconciled; prescriber box now covers both." }
---

# CL-06. Type 2 diabetes on insulin

**What this page is for.** Many people with type 2 diabetes eventually need insulin, often a
long-acting injection once or twice a day, sometimes with meal-time insulin as well. The insulin
has the same storage problem as in type 1: it needs to stay cool and must never freeze. The
clock is usually less brutal than in type 1, because the body still makes some insulin of its
own, but losing insulin still means dangerously high sugar, and taking it without food still
means dangerous lows. This module covers both. The tablets side of type 2 is on → 02-05, and the
fuller storage detail on → 02-01.

{{#if has.condition.CL-06}}**Someone in your household has this condition.** This module is at the front of the medical section for you.{{else}}**Nobody in your household is marked with this condition.** The module stays in the binder so you can help someone else, or add the condition later in settings.{{/if}}

> **SAFETY**
> - **A frozen-then-thawed insulin vial or pen is discarded.** Freezing breaks the insulin and it
>   can look normal afterwards; FDA and the American Diabetes Association both say do not use it
>   (floor, → 30-01).
> - **Insulin plus missed meals or hard work causes lows.** In a crisis, both happen. Keep fast
>   sugar within reach and know the first aid below.
> - **This page never calculates, adjusts or suggests a dose.** What to do when food is short,
>   when sick, or when insulin runs low comes from the prescriber, written in the blanks below.
>   FDA's and ADA's emergency switching texts are printed as published in part 8, for the
>   prescriber to confirm.

## Do this now

**Low blood sugar (shaky, sweaty, confused, odd behaviour):**
1. If they can swallow safely: **CDC's 15-15 rule**: 15 grams of fast carbohydrate (glucose
   tablets or gel by their label, or half a cup, 4 ounces, of juice or regular soda), wait 15
   minutes, check; if still below 70 mg/dL, repeat (CDC, Treatment of Low Blood Sugar). **If the
   person also takes a tablet that slows the digestion of carbohydrate, use glucose tablets or
   gel**: NIDDK says other sugars will not act fast enough (NIDDK, Low Blood Glucose).
2. **Cannot swallow or not awake: nothing by mouth.** On their side. Glucagon if the prescriber
   supplied it, exactly as its label shows; CDC says to get emergency medical care right after a
   glucagon injection, so send for any that exists.
3. Food once awake. Long-acting insulin keeps working: **check again within the hour and through
   the night.**

**Very high sugar, vomiting, deep fast breathing, fruity breath, confusion:** keep giving insulin
(CDC's sick-day advice is to keep taking it as usual; not eating is not a reason to stop it;
CDC, Managing Sick Days), fluids by small sips,
check ketones if you have strips, follow the sick-day plan in part 6, and seek care if any
exists. CDC's emergency signs: sugar staying at **300 mg/dL or above**, fruity breath, vomiting
so persistent that no food or fluid stays down, trouble breathing (CDC, Diabetic Ketoacidosis).

## 1. What it is

Type 2 diabetes means the body uses insulin poorly and over time makes less of it (CDC, Type 2
Diabetes). When tablets are no longer enough, injected insulin tops up what the body makes.

## 2. What runs out, and how fast

| What | Clock | When it is gone |
|---|---|---|
| **Insulin** | Days on hand (part 7). An opened vial or pen lasts only as long as its label allows. | Sugar climbs over days; risk of collapse from very high sugar and dehydration. |
| Pen needles or syringes | Count with the insulin. | Insulin cannot be given. |
| Tablets taken alongside | From the bottle (→ 02-05). | As → 02-05. |
| Meter strips, lancets | Count them. | Lows and highs go unseen. |
| Fast sugar | Cheap now. | Lows cannot be treated. |

**Write the clock:** units of insulin on hand ________ ÷ units used a day ________ = **________
days**, on ________ (date). Copy it to → 23-02. The units-a-day figure is the person's own,
from their log or prescriber.

## 3. Storing insulin without power

**The published rules (FDA, Information Regarding Insulin Storage and Switching Between Products
in an Emergency; ADA, Insulin Storage and Syringe Safety):**
- Unopened insulin normally in a refrigerator at about **36 to 46 °F**.
- With no power, vials and cartridges, opened or unopened, **may be kept at 59 to 86 °F for up to
  28 days** and still work (FDA). Each product's label gives its own in-use days; write yours in
  part 12.
- **The once-weekly insulin has its own window.** FDA, as published: "Awiqli (insulin icodec) is
  only available as a prefilled pen. It has a longer unrefrigerated storage window than other
  insulin products. Unopened Awiqli FlexTouch pens stored in a refrigerator (36°F to 46°F) may
  be kept until the expiration date. Once removed from the refrigerator, or when in use, Awiqli
  pens may be stored at room temperature below 86°F for up to 12 weeks. The total combined time
  at room temperature, whether opened or unopened, must not exceed 12 weeks. Do not freeze
  Awiqli; do not use if it has been frozen." (FDA, Information Regarding Insulin Storage and
  Switching Between Products in an Emergency)
- Above 86 °F, insulin loses strength; FDA says under emergency conditions you might still need
  to use insulin stored above 86 °F, and to replace it when properly stored insulin is available.
  Your household's line: {{choice DC-08}} (→ 30-09).
- **Frozen: do not use** (FDA, ADA). Floor: discard.
- Regular (clear) insulin with particles or discoloration, or NPH (cloudy) insulin with frosting
  or crystals on the bottle or small particles or clumps, is not used (ADA).
- Planning context: a Cochrane review found unopened vials and cartridges of specific types of
  human insulin kept their strength up to six months at up to 77 °F and two months at up to
  99 °F (Cochrane, Human insulin less temperature-sensitive than previously thought). It did not
  cover the newer "analog" insulins. Not
  permission to store warm; a reason not to throw away a stockpile after one hot afternoon.

**The cold ladder:** a fridge or 12-volt cooler on battery or solar that cannot freeze
(→ 09-10); a buffered cooler in winter cold with a min/max thermometer; ice with a barrier;
evaporative pouches in summer (→ 12-21); the coolest stable spot in the house. Each step is
explained on → 29-07 and → 02-01.

{{figure fig-insulin-cooler-barrier}}

{{photo insulin-outage-spot-t2}}

## 4. Day by day without it

- **Days:** sugar rises; thirst, peeing, tiredness, blurred vision.
- **Days to weeks:** dehydration builds, especially in heat, illness or old age. Very high sugar
  with dehydration can cause confusion, drowsiness and collapse, which needs fluids and medical
  care.
- **Ketoacidosis (DKA)** is less common than in type 1 but can happen, especially during
  illness (CDC, Diabetic Ketoacidosis; ADA, DKA).

**What helps:** regular meals, fewer sugary and starchy foods, daily activity, plenty of water.
These lower sugar, and **lower sugar plus the same insulin can mean lows**. A big change in food
or work is a reason to check more often and to follow the prescriber's written plan.

**Do not "make it last" by taking less on your own.** Ask the prescriber now what to do if the
supply runs short, and write it in part 6.

## 5. Warning signs that mean an emergency

- **Low blood sugar** below 70 mg/dL (CDC): shaky, sweaty, fast heartbeat, confused, dizzy, then
  seizure or unconsciousness. First aid in "Do this now". **Every adult in the house should be
  able to give glucagon if it is kept.**
- **Very high sugar with dehydration:** extreme thirst, dry mouth, confusion, drowsiness.
- **DKA:** vomiting, belly pain, deep fast breathing, fruity breath, confusion; blood ketones of
  **1.6 mmol/L or higher** need emergency care (ADA, DKA).

Decide now what "emergency" means without an emergency room: usually the trigger to move toward
care (→ 01-02, → 01-07). Write it: ______________________________________________

## 6. Sick-day basics

CDC's published steps (CDC, Managing Sick Days): **keep taking insulin**; check sugar **every 4
hours**; drink plenty of water; try to eat; if meals are impossible, about **50 grams of
carbohydrate every 4 hours** (for example 1½ cups of unsweetened applesauce or fruit juice);
weigh daily; temperature morning and evening; test urine for ketones. CDC's emergency-room list
includes ketones in the urine, no liquids kept down for more than 4 hours, sugar below 60 mg/dL,
and vomiting or severe diarrhoea for more than 6 hours. Dehydration treatment is on → 12-05.

**Ask your prescriber now, while you can, and write it here:**
- Insulin changes when sick and not eating: ____________________________________________
  ______________________________________________________________________________________
- Insulin changes when food is short or work is heavy: __________________________________
  ______________________________________________________________________________________
- What to do if insulin is running out: _______________________________________________
- Which tablets to pause when vomiting: ______________________________________________

## 7. What to stock, and how much

**Days on hand = on hand ÷ used per day.** The medicines tagged for this condition in settings are printed; if none are tagged, every household medicine row is, so use the ones for this condition.

| Medicine or supply | On hand | Used per day | Days on hand | Days you want | Still to get |
|---|---|---|---|---|---|
{{#each meds_for.CL-06 as m}}
| {{m.name}} {{m.strength}} ({{m.member}}) | ____ | ____ | ____ | ____ | ____ |
{{else}}
{{#each meds as m}}
| {{m.name}} {{m.strength}} ({{m.member}}) | ____ | ____ | ____ | ____ | ____ |
{{/each}}
{{/each}}
| Pen needles or syringes (syringes must match the insulin strength, usually U-100) | ____ | ____ | ____ | ____ | ____ |
| Meter strips, lancets | ____ | ____ | ____ | ____ | ____ |
| Ketone strips | ____ | | | ____ | ____ |
| Glucagon (if prescribed) | ____ | | | ____ | ____ |
| Fast sugar | ____ | | | ____ | ____ |
| Sharps bottle, min/max thermometer | ____ | | | ____ | ____ |

Used needles go in a heavy plastic bottle with a screw cap (FDA, Best Way to Get Rid of Used
Needles). Never share a pen or syringe (ADA).

> **Before the collapse:** ask for the largest emergency supply the prescriber will write; 90-day
> fills; refill at the earliest allowed date. In many states, older human insulins (Regular, NPH
> and their mixes) can be bought at the pharmacy counter without a prescription; ask the pharmacist
> what your state allows, and ask the prescriber now whether one of them could serve as this
> person's backup, and how. Write it here: _________________________________________

## 8. Sourcing when the pharmacy is closed

Pharmacies, clinics, hospitals and disaster medical points while they run; other people with
diabetes (→ 18-01). Someone else's prescription is a card: {{choice DC-15}} (→ 30-16). **Never
veterinary insulin, never unlabelled vials, never insulin of unknown storage.**

**If only a different insulin can be found:** FDA and the ADA publish emergency switching
guidance and both say switching should be done with a physician and close sugar checks (FDA;
ADA, Switching Between Insulin Products in Disaster Response Situations). **The two documents
do not give the same amounts**: the ADA sheet, written for health professionals, lowers the dose
in most switches, while FDA's mostly keeps the same number of units. That is one more reason to
have the prescriber decide now. Both are bound behind this page in the Large download. **This binder does not convert doses**; FDA's published text
follows, then ADA's, side by side and not reconciled, for your prescriber to confirm.

### As published, for your prescriber to confirm

FDA's emergency guidance on switching insulin is printed here **exactly as published**, so that
you can show it to the prescriber **now** and have them confirm or change it for this person
(FDA, Information Regarding Insulin Storage and Switching Between Products in an Emergency,
content current as of 09/28/2026). It is not this binder's advice, and the binder does not work
out any amount from it. Brand names are FDA's examples.

> **FDA:** "Always switch insulin under a doctor's care, with close monitoring of your blood
> sugar. If you cannot reach a doctor during an emergency, follow the guidance below — but
> monitor your blood sugar closely and see a doctor as soon as you can."

> **FDA, Short-acting (regular insulin) and Rapid-acting Insulins:** "In an emergency, you can
> switch one brand of regular insulin (such as Humulin R or Novolin R) for another brand of
> regular insulin, or for a rapid-acting insulin (such as Apidra, Fiasp, Humalog, or NovoLog),
> and vice versa. Use the same number of units.
>
> Inject regular insulins approximately 30 minutes before the start of each meal. Rapid-acting
> insulins begin working more rapidly than regular insulin and are to be injected no more than
> 15 minutes before the start of each meal to avoid dangerously low blood sugar levels."

> **FDA, Intermediate and Long-acting Insulins:** "In an emergency, you can switch one brand of
> intermediate-acting insulin (such as, Humulin N, Novolin N) for another intermediate-acting
> insulin on a unit-per-unit basis. You can also switch intermediate-acting insulins for
> long-acting insulins (e.g., Lantus, Toujeo, Tresiba) on a total unit-per-day basis, or vice
> versa.
>
> Important: If you switch from a once-daily long-acting insulin (e.g., Lantus, Toujeo, Tresiba)
> to an intermediate-acting insulin, keep your total daily dose the same but split it into two
> equal injections. Give half in the morning with breakfast and half in the evening with dinner
> to avoid a dangerously low blood sugar.
>
> If you switch from an intermediate-acting to a once-daily long-acting insulin, add up the total
> amount of intermediate-acting insulin units for one day, and give it as a single long-acting
> insulin dose once a day.
>
> Close monitoring of blood sugar and adjustment of your insulin dose may be needed in the
> transition."

> **FDA, Once-weekly Long-acting Insulin:** "If you use the once-weekly long-acting insulin,
> Awiqli (insulin icodec) and need to switch to a once-daily long-acting or intermediate-acting
> insulin in an emergency, base your dose on your total weekly dose.
>
> When switching from a once-daily long-acting insulin to insulin icodec, give the first insulin
> icodec dose on the day after your last daily long-acting insulin dose. For Week 1, multiply
> your previous total daily dose by 7, then by 1.5, and round to the nearest 10 units.
>
> Important: Because insulin icodec stays active for about one week, its blood sugar-lowering
> effect continues for several days after the last dose. If you switch from Awiqli to a basal
> (background) long-acting insulin, switching should be done under close medical supervision
> with increased blood sugar monitoring to avoid low blood sugar (hypoglycemia).
>
> Note: Insulin icodec must not be used in an insulin pump, mixed with other insulins, or drawn
> from the pen into a syringe."

> **FDA, Insulin Mixes:** "Switching between types of insulin should be done with a doctor's
> guidance and close blood sugar monitoring. [...] Insulin mixes combine two types of insulin,
> intermediate- and short/rapid-acting, in one dose. The first number shows how much
> intermediate insulin is in the mix and the second number shows how much short/rapid-acting
> insulin. For example, each dose of a 70/30 mix contains 70% intermediate-acting insulin and
> 30% short/rapid-acting insulin.
>
> [...] If you use a pre-mixed insulin (e.g., Humulin 70/30, Humalog Mix 75/25, Novolin 70/30,
> NovoLog Mix 70/30), here are your options in an emergency:
>
> In an emergency, you can switch one insulin mix for another on a unit-per-unit basis.
>
> Insulin mixes with rapid-acting insulin analog (e.g., Humalog Mix, Novolog Mix) should be
> injected closer (within 15 minutes) to the start of the meal compared to mixes containing
> regular insulin (e.g., Humulin 70/30).
>
> If an insulin mix is not available, patients should follow this two-step process:
>
> Step one: replace an intermediate-acting part of the mix (about 70% of the total units for
> each dose) with an intermediate-acting or a long-acting insulin on a unit-per-unit basis.
>
> - With an intermediate-acting insulin:
>   - Give 70% of total units for each dose
> - With a long-acting insulin:
>   - Add up the total insulin units given in one day
>   - Give 70% as one daily dose
>
> Step two: if regular or rapid-acting insulins are also available, use them before major meals.
> The dose should be about 30% of your total of pre-mixed insulin for that meal, in addition to
> the intermediate- or long-acting.
>
> Note: Inject longer and shorter acting insulins separately unless your doctor tells you
> otherwise."

**ADA's sheet, printed next to FDA's and not reconciled with it.** The American Diabetes
Association's sheet is written **for health care professionals**. It is printed here **exactly
as published** (American Diabetes Association, Switching Between Insulin Products in Disaster
Response Situations; approved by the American Diabetes Association, Endocrine Society and JDRF,
updated August 2020). Where it and FDA give different amounts, **neither is this binder's
answer**: show both to the prescriber. Brand names and worked examples are ADA's.

> **ADA:** "IMPORTANT: These recommendations are intended to be used only for disaster response
> situations when patients are not on their usual schedule, may have limited monitoring
> capabilities, or don't have access to their prescribed insulins.
>
> - Individuals with type 1 diabetes have priority for receiving insulin. Even a few hours of
>   interrupted insulin therapy can result in life-threating diabetic ketoacidosis (DKA).
> - These guidelines do not replace clinical judgment and are intended to assist with short-term
>   diabetes management until the patient can resume their prescribed care regimen.
> - A reduction in insulin dose by 20% is recommended when switching to another insulin under
>   disaster response situations to avoid hypoglycemia. This may result in short-term, mild
>   hyperglycemia until the patient is back to a normal routine and insulin regimen.
> - Consultation with an experienced healthcare professional is advised for patients with
>   complicated insulin needs, e.g. pregnancy, dialysis, insulin pump, or concentrated insulins
>   (i.e., U200, U300, and U500)."

> **ADA, Rapid-acting and Regular insulins:** "RAPID-ACTING AND REGULAR INSULINS are typically
> given before meals to regulate the rise in glucose after a meal.
>
> - Rapid-acting insulins should be injected no more than 15 minutes before the start of a meal
> - Regular insulin can be injected up to 30 minutes before the start of a meal
>
> IF PATIENT IS TAKING THIS: Rapid-Acting Insulins such as: Humalog® (insulin lispro U-100 &
> U-200); Admelog® (insulin lispro U-100); Novolog® or Fiasp® (insulin aspart U-100); Apidra®
> (insulin glulisine U-100). Short-Acting Insulins: Regular insulin brand name examples:
> Humulin®R; Novolin®R; ReliOn R from Walmart.
>
> INTERCHANGE RECOMMENDATIONS:
> - Rapid- and Short-acting insulins may be interchanged with a 20% reduction in the dose
>   - Example: Humalog® 10 units before meals can be switched to Regular 8 units before meals
>     (80% of 10 units = 8 units)
>   - Example: Regular 10 units before meals can be switched to Novolog® 8 units before meals
>     (80% of 10 units = 8 units)"

> **ADA, Intermediate-acting and basal insulins:** "Intermediate-acting and basal insulin analogs
> are typically given once or twice daily to provide basal insulin needs (to prevent high
> glucose between meals and overnight).
>
> IF PATIENT IS TAKING THIS: Intermediate-Acting Insulins: NPH insulin brand name examples:
> Humulin®N; Novolin®N; ReliOn NPH from Walmart.
>
> INTERCHANGE RECOMMENDATIONS: Intermediate-acting insulins may be interchanged with another
> intermediate-acting insulin or basal insulin analog with a 20% reduction in dose
>
> - NPH ONCE daily to a basal insulin analog
>   - Example: NPH 20 units daily can be switched to Levemir® 16 units daily
> - NPH TWICE daily to a basal insulin analog
>   - Add all the units of NPH injected per day and give 80% as a single dose of a basal insulin
>     analog daily
>     - Example: NPH 34 units AM and 16 units PM can be switched to Lantus® 40 units daily (80%
>       of 50 units daily = 40 units)
>
> IF A PATIENT IS TAKING THIS: Basal insulin analogues such as: Levemir® (detemir U-100);
> Lantus®, Basalgar® (glargine U-100); Toujeo® (glargine U-300); Tresiba® (degludec U-100 &
> U-200).
>
> INTERCHANGE RECOMMENDATIONS: Basal insulin analogs may be interchanged with NPH with a 20%
> reduction in dose and divided based on predicted meal frequency
>
> - If eating 2 meals per day, split the new dose into ½ NPH with first meal of the day and ½
>   NPH with second meal of the day
> - Basal insulin analogs (with the exception of Tresiba®) may be interchanged with another basal
>   insulin analog with a 20% reduction in dose
> - Tresiba® (80 units or less) may be interchanged with another basal insulin analog with a 20%
>   reduction in dose
> - Tresiba® (greater than 80 units) may be interchanged with another basal insulin analog with a
>   20% reduction in dose, but the other basal insulin must be split into two equal doses given
>   12 hours apart.
>   - Example: Tresiba® 100 units daily can be switched to Basalgar® 40 units (80% of 100 units
>     = 80 units/2) every 12 hours"

> **ADA, Premixed insulins:** "PREMIXED INSULINS combine an intermediate-acting insulin or basal
> insulin analog with a rapid or regular insulin. The ratio of the mixture is indicated in the
> name. e.g. 70% intermediate or long-acting with 30% rapid or short-acting.
>
> IF PATIENT IS TAKING THIS: PREMIXED INSULINS with Regular insulin: NPH/Regular (Humulin® 70/30,
> Novolin® 70/30, or ReliOn 70/30). PREMIXED INSULINS with rapid-acting insulin: Humalog® Mix
> 75/25; Humalog® Mix 50/50; Novolog® Mix 70/30. PREMIXED INSULIN with rapid- and ultra-long
> acting insulins: Ryzodeg® 70/30 (degludec/aspart).
>
> INTERCHANGE RECOMMENDATIONS: Regular and Rapid-acting PREMIXED insulins may be interchanged with
> another PREMIXED insulin with a 20% reduction in the dose
>
> - Insulin mixes containing a rapid-acting insulin should be injected no more than 15 minutes
>   before the start of a meal
> - Insulin mixes containing Regular insulin can be injected up to 30 minutes before the start of
>   a meal
> - PREMIXED insulin may be interchanged with NPH using a 20% reduction in dose"

> **ADA, Unique insulin therapies:** "Concentrated Insulin: Humulin® R U500 insulin. Strongly
> recommend consulting a healthcare professional with experience in U500 insulin if switching to
> another insulin"

> **ADA:** "THE RECOMMENDATIONS DO NOT REPLACE CLINICAL JUDGMENT"

**Prescriber, please read the FDA and ADA texts above and confirm one for this person, or write
what to do instead.** Person: ____________________
Agree as printed ☐  Change as written here: _________________________________________________
_____________________________________________________________________________________________
Prescriber: ____________________ Initials: ______ Date: __________

**Ask your prescriber now, while you can, and write it here:** "If all we can get is ________,
what do we give, how much, and when?"
_____________________________________________________________________________________________
Prescriber: ____________________ Date: __________

## 9. Power and devices

Cold storage in summer is the only big power load (→ 09-10). A meter runs months on its battery;
keep spares and a boxed spare meter in a metal box against an EMP (→ 27-03). If a sensor or pump
is used, see → 02-02.

## 10. Travel and evacuation

- **Insulin on the person**, inside the coat in winter, in an evaporative pouch or insulated bag
  in summer; never in a trunk or parked car (→ 12-21, → 01-07).
- The go-bag (→ 22-06): insulin, needles, meter, strips, fast sugar, glucagon if kept, sharps
  bottle, the written plan, a copy of the prescription.
- Walking and missed meals cause lows: check more often, carry sugar in a pocket.

## 11. Decision cards that apply

- **Heat-exposed insulin:** {{choice DC-08}} (→ 30-09).
- **Expired medicine and supplies:** {{choice DC-04}} (→ 30-05).
- **Someone else's prescription:** {{choice DC-15}} (→ 30-16).
- **When to leave:** {{choice DC-19}} (→ 30-20).
- **Frozen insulin is a floor:** discard (→ 30-01).

## 12. My meds

Medicines your household tagged for this condition in settings are printed below. **If none
are tagged, every medicine row your household entered is printed instead: tick the rows for
this condition** and cross out the rest. Fill any blank columns by hand from the boxes
and bottles, and add untagged medicines in the empty rows.

| For this? | Who | Medicine | Strength | Schedule | Fridge? | If doses are missed (prescriber's words) | Where kept | Days on hand | Expires |
|---|---|---|---|---|---|---|---|---|---|
{{#each meds_for.CL-06 as m}}
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

**Label days for each insulin** (from the box or leaflet, → 29-14): out of the fridge, unopened
________ days; opened ________ days. Write the date on each vial or pen the day it leaves the
fridge.

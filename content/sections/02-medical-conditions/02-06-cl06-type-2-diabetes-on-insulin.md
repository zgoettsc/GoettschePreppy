---
id: 02-06-cl06-type-2-diabetes-on-insulin
section: 02-medical-conditions
title: "CL-06. Type 2 diabetes on insulin"
version: 1
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
review_pass: null
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

## Do this now

**Low blood sugar (shaky, sweaty, pale, confused, odd behaviour):**
1. If they can swallow safely: **CDC's 15-15 rule**: 15 grams of fast carbohydrate (glucose
   tablets or gel by their label, half a cup of juice or regular soda), wait 15 minutes, check;
   if still below 70 mg/dL, repeat (CDC, Low Blood Sugar).
2. **Cannot swallow or not awake: nothing by mouth.** On their side. Glucagon if the prescriber
   supplied it, exactly as its label shows.
3. Food once awake. Long-acting insulin keeps working: **check again within the hour and through
   the night.**

**Very high sugar, vomiting, deep fast breathing, fruity breath, confusion:** keep giving insulin
(never stop it because the person is not eating; CDC, Managing Sick Days), fluids by small sips,
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
- Above 86 °F, insulin loses strength; FDA says under emergency conditions you might still need
  to use insulin stored above 86 °F, and to replace it when properly stored insulin is available.
  Your household's line: {{choice DC-08}} (→ 30-09).
- **Frozen: do not use** (FDA, ADA). Floor: discard.
- Clear insulin that turns cloudy or coloured, or cloudy insulin with clumps or frosting on the
  glass, is not used (ADA).
- Planning context: a 2023 Cochrane review found unopened vials of some human insulins kept their
  strength up to six months at up to 77 °F and two months at up to 99 °F (Cochrane, 2023). Not
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

- **Low blood sugar** below 70 mg/dL (CDC): shaky, sweaty, fast heartbeat, confused, pale, then
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

**Days on hand = on hand ÷ used per day.** Every household medicine row is printed; use the ones
for this condition.

| Medicine or supply | On hand | Used per day | Days on hand | Days you want | Still to get |
|---|---|---|---|---|---|
{{#each meds as m}}| {{m.name}} {{m.strength}} ({{m.member}}) | ____ | ____ | ____ | ____ | ____ |
{{/each}}| Pen needles or syringes (syringes must match the insulin strength, usually U-100) | ____ | ____ | ____ | ____ | ____ |
| Meter strips, lancets | ____ | ____ | ____ | ____ | ____ |
| Ketone strips | ____ | | | ____ | ____ |
| Glucagon (if prescribed) | ____ | | | ____ | ____ |
| Fast sugar | ____ | | | ____ | ____ |
| Sharps bottle, min/max thermometer | ____ | | | ____ | ____ |

Used needles go in a heavy plastic bottle with a screw cap (FDA, Best Way to Get Rid of Used
Needles). Never share a pen or syringe (ADA).

> **Before the collapse:** ask for the largest emergency supply the prescriber will write; 90-day
> fills; refill at the earliest allowed date. In most states, older human insulins (Regular, NPH
> and their mixes) are sold at the pharmacy counter without a prescription; ask the pharmacist
> what your state allows, and ask the prescriber now whether one of them could serve as this
> person's backup, and how. Write it here: _________________________________________

## 8. Sourcing when the pharmacy is closed

Pharmacies, clinics, hospitals and disaster medical points while they run; other people with
diabetes (→ 18-01). Someone else's prescription is a card: {{choice DC-15}} (→ 30-16). **Never
veterinary insulin, never unlabelled vials, never insulin of unknown storage.**

**If only a different insulin can be found:** FDA and the ADA publish emergency switching
guidance and both say switching should be done with a physician and close sugar checks (FDA;
ADA, Switching Between Insulin Products in Disaster Response Situations). Both are bound behind
this page in the Large download. **This binder does not convert doses.**

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

Every medicine row your household entered is printed, because the binder cannot pick out one
condition's rows. **Tick the rows for this condition**, cross out the rest, and fill the last
three columns by hand.

| For this? | Who | Medicine | Strength | Schedule | Fridge? | If doses are missed (prescriber's words) | Where kept | Days on hand | Expires |
|---|---|---|---|---|---|---|---|---|---|
{{#each meds as m}}| ☐ | {{m.member}} | {{m.name}} | {{m.strength}} | {{m.schedule}} | {{m.refrigerated}} | {{m.if_missed}} | ____ | ____ | ____ |
{{else}}| ☐ | (no medicines entered yet) | | | | | | ____ | ____ | ____ |
{{/each}}| ☐ | ____ | ____ | ____ | ____ | ____ | ____ | ____ | ____ | ____ |
| ☐ | ____ | ____ | ____ | ____ | ____ | ____ | ____ | ____ | ____ |
| ☐ | ____ | ____ | ____ | ____ | ____ | ____ | ____ | ____ | ____ |

**Label days for each insulin** (from the box or leaflet, → 29-14): out of the fridge, unopened
________ days; opened ________ days. Write the date on each vial or pen the day it leaves the
fridge.

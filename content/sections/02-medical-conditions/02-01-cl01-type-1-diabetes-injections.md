---
id: 02-01-cl01-type-1-diabetes-injections
section: 02-medical-conditions
title: "CL-01. Type 1 diabetes on injections"
version: 2
revised: 2026-11-16
layer: condition
danger_level: critical
phase: [A, B, C]
tags: [condition library, type 1 diabetes, insulin, injections, cold chain, DKA, ketones, low blood sugar, glucagon, sick days, supply clock]
derived_from: [02-01-t1d-overview-and-supply-math, 02-02-insulin-without-the-grid, 02-04-cgm-conservation-and-dka, 02-05-sourcing-insulin-supplies, 09-10-power-for-medical]
sources:
  - us-fda-information-regarding-insulin-storage-and-swi-6448d3
  - american-diabetes-association-insulin-storage-and-sy-6f1f94
  - american-diabetes-association-switching-between-insu-9c5595
  - cochrane-human-insulin-less-temperature-sensitive-th-28a2b9
  - cdc-diabetic-ketoacidosis-55a7c2
  - american-diabetes-association-dka-ketoacidosis-and-k-f0301a
  - cdc-managing-sick-days-18c7c8
  - cdc-low-blood-sugar-hypoglycemia
  - cdc-treatment-of-low-blood-sugar-r7
  - niddk-low-blood-glucose-hypoglycemia-r10
  - us-fda-best-way-to-get-rid-of-used-needles-and-other-a67780
  - world-health-organization-cholera-outbreaks-q-and-a-162558
related:
  - 02-02-cl02-type-1-diabetes-pump-and-cgm
  - 02-06-cl06-type-2-diabetes-on-insulin
  - 12-11-chronic-conditions
  - 12-07-meds-stockpile
  - 12-05-common-illness-and-dehydration
  - 12-21-evaporative-cooling-pouches
  - 09-10-power-for-medical
  - 09-06-charging-medical-devices
  - 22-06-kit-medical
  - 01-07-evacuating-with-medical-needs
  - 01-02-go-no-go-decision
  - 23-02-master-consumables-table
  - 25-09-family-medical-summary
  - 29-07-ex07-refrigerated-medicines
  - 30-01-the-floors
  - 30-09-dc08-heat-exposed-medication
  - 30-05-dc04-expired-medication
  - 30-16-dc15-someone-elses-prescription
  - 30-20-dc19-when-to-leave
cards: [DC-08, DC-04, DC-15, DC-19]
explainers: [EX-07, EX-14]
promote_when: [has.condition.CL-01]
photo_slots:
  - { id: insulin-outage-spot, caption: "Where our insulin goes when the power is out: the cooler or fridge, the thermometer, the barrier between insulin and ice" }
  - { id: low-sugar-kits, caption: "Our fast-sugar and glucagon spots: bedside, coat, go-bag, kitchen" }
figures: [fig-insulin-cooler-barrier, fig-recovery-position]
plates: []
condition: CL-01
gear: null
explainer: null
card: null
review_pass: null
---

# CL-01. Type 1 diabetes on injections

**What this page is for.** Everything a household needs to keep a person with type 1 diabetes
alive when pharmacies, power and ambulances stop: what runs out, how to keep insulin good without
a fridge, what goes wrong and how fast, what to do in the two emergencies (sugar too low, and
the acid build-up called DKA), and what to stock. It never tells you how much insulin to give.
That comes from the prescriber, written in the blanks on this page while you can still ask.
Pumps and sensors have their own module (→ 02-02); read this one first either way.

{{#if has.condition.CL-01}}**Someone in your household has this condition.** This module is at the front of the medical section for you.{{else}}**Nobody in your household is marked with this condition.** The module stays in the binder so you can help someone else, or add the condition later in settings.{{/if}}

> **SAFETY**
> - **Insulin cannot be skipped, stretched or replaced.** A person with type 1 diabetes makes no
>   insulin. Without it, diabetic ketoacidosis (DKA) follows and kills; the ADA's disaster sheet
>   says even a few hours of interrupted insulin can bring on life-threatening DKA (ADA,
>   Switching Between Insulin Products). Nothing grown, foraged or bought over a counter replaces it.
> - **A frozen-then-thawed insulin vial or pen is discarded.** Freezing breaks the insulin and it
>   can look normal afterwards; FDA and the American Diabetes Association both say do not use it
>   (floor, → 30-01).
> - **Heat is different from freezing.** Warm insulin loses strength slowly. Whether to use it
>   past the published window is your household's decision card: {{choice DC-08}} (→ 30-09).
> - **This page never calculates, adjusts or suggests a dose.** Your doses, and what to do when
>   sick or short, come from the prescriber and go in the blanks below. FDA's emergency
>   switching text is printed as published in part 8, for the prescriber to confirm.

## Do this now

**Low blood sugar: shaky, sweaty, confused, odd behaviour, or "feels low":**
1. If they can swallow safely: **fast sugar now**. CDC's 15-15 rule: eat or drink 15 grams of
   fast carbohydrate (glucose tablets or gel by their label, or half a cup, 4 ounces, of juice or
   regular soda), wait 15 minutes, check sugar; if still below 70 mg/dL, repeat (CDC, Treatment of
   Low Blood Sugar).
2. **Not awake, cannot swallow, or having a seizure: nothing by mouth.** Give **glucagon** exactly
   as its label shows. Roll them onto their side (→ figure below). Stay with them. CDC says to get
   emergency medical care right after a glucagon injection: if any exists, send for it.
3. When they are awake and can swallow, give food. Check sugar again within the hour.

**Signs of DKA: thirst, peeing a lot, vomiting, belly pain, deep fast breathing, fruity breath, confusion:**
1. **Check ketones** (urine strip or blood meter). **Keep giving the person's insulin.** CDC's
   sick-day advice is to keep taking insulin as usual (CDC, Managing Sick Days); not eating is
   not a reason to stop it.
2. **Fluids, small sips often.** Follow the sick-day plan the prescriber wrote in part 6.
3. ADA says a blood ketone level of **1.6 mmol/L or higher** needs emergency care; CDC says
   ketones in the urine mean the emergency room (ADA, DKA; CDC, Managing Sick Days). If any care
   exists, go now (→ 01-07).

{{figure fig-recovery-position}}

## 1. What it is

Type 1 diabetes means the body has stopped making insulin, the hormone that lets sugar from food
into the cells. Without injected insulin, sugar piles up in the blood, the body burns fat
instead, and the acids from burning fat (ketones) poison the blood (ADA, DKA).

## 2. What runs out, and how fast

| What | Clock | What happens when it is gone |
|---|---|---|
| **Insulin** | Your days on hand (part 7). One opened vial or pen lasts only as long as its label allows. | DKA, which can start within hours (ADA). **This is the household's master clock.** |
| Syringes or pen needles | Count them with the insulin. | A vial you cannot draw from is not usable insulin. |
| Glucose meter strips and lancets | Your check rate times your count. | Dosing blind; lows go unnoticed. |
| Ketone strips | Opened bottles have a printed use-within date; check yours. | DKA is caught late. |
| Glucagon | Printed expiry. | No way to treat a low in someone who cannot swallow. |
| Fast sugar | Anything sweet works; it is cheap now. | Lows cannot be treated. |
| Meter batteries | Printed on the meter. | No readings. |

**Write the master clock where everyone sees it:**
`total units of insulin on hand ÷ average units used per day = days of insulin`
Units on hand ________ ÷ units a day ________ = **________ days**, on ________ (date).
Copy it to → 23-02 and check it weekly. The units-per-day figure comes from the person's own
log or the prescriber, never from this page.

**The opened-vial clock matters.** Once a vial or pen is opened, or kept out of the fridge, its
label gives a number of days before it must be discarded; FDA's emergency guidance is up to 28
days at 59 to 86 °F (FDA, Insulin Storage and Switching). If the person uses less than one vial
in that time, the rest is lost. Open one at a time, oldest first, and ask the prescriber whether a
smaller package would waste less.

## 3. Storing insulin without power

**The published rules (FDA, Information Regarding Insulin Storage and Switching Between Products
in an Emergency; ADA, Insulin Storage and Syringe Safety):**

| Situation | Rule as published |
|---|---|
| Normal storage, unopened | Refrigerator, about **36 to 46 °F**. |
| No power, opened or unopened vial or cartridge | May be kept at **59 to 86 °F for up to 28 days** and still work (FDA). Each product's label gives its own in-use days; some are shorter. Write yours in part 12. |
| Above 86 °F | Strength drops; the longer and hotter, the more. FDA: under emergency conditions you might still need to use insulin stored above 86 °F, and replace it as soon as properly stored insulin is available. Your household's line: {{choice DC-08}} (→ 30-09). |
| Frozen | **Do not use** (FDA, ADA). Floor: discard. |
| Insulin taken out of its original vial or diluted | Discard within two weeks (FDA). |
| Looks wrong | Regular (clear) insulin with particles or discoloration, or NPH (cloudy) insulin with "frosting" or crystals on the inside of the bottle or small particles or clumps, is not used (ADA). |
| Expired | ADA says do not use past the expiry date. Your household's line on expired medicine: {{choice DC-04}} (→ 30-05). |

**Planning context, not permission:** a Cochrane review found that unopened vials and cartridges
of specific types of **human** insulin kept their strength for up to six months at up to 77 °F
(25 °C) and up to two months at up to 99 °F (37 °C) (Cochrane, Human insulin less
temperature-sensitive than previously thought). The review was about human insulin; it does not
cover the newer "analog" insulins that many people now use. Freezing is a cliff; heat is a slope.

**The cold ladder, best first** (→ 29-07 explains each step):
1. A **powered fridge or 12-volt compressor cooler** on a battery or solar, set so it **cannot
   freeze**, with a thermometer inside (→ 09-10).
2. **Winter cold, buffered:** an insulated cooler in a cold spot, never directly against ice or a
   frozen wall, checked with a **min/max thermometer** (one that remembers the highest and lowest
   reading). Outdoors, a garage or a car swings below freezing at night. Aim for the label's 36
   to 46 °F, and never let it freeze.
3. **Ice or cold packs with a barrier**: a towel or a box between the ice and the insulin so it
   cannot freeze (→ figure).
4. **Evaporative cooling pouches** in warm months: they keep insulin below air temperature with
   only water (→ 12-21).
5. **The coolest stable place in the house**: basement, interior closet, a cooler buried in the
   ground, checked by thermometer.

{{figure fig-insulin-cooler-barrier}}

{{photo insulin-outage-spot}}

**Supplies have bands too.** Meter strips and ketone strips read wrong if they freeze, cook or
get damp: keep them capped, dry, and in the room where the people are. Glucagon is a
room-temperature product; read its label and keep it out of the fridge, the car and the cold
garage.

## 4. Day by day without it

This is what public sources describe when insulin stops. It is here so nobody mistakes the
early hours for a reprieve.

- **First:** blood sugar rises. Thirst and peeing increase (CDC, Diabetic Ketoacidosis).
- **Then:** ketones appear and rise. Tiredness, headache, sick stomach.
- **DKA:** vomiting, belly pain, deep fast breathing, fruity breath, confusion, then collapse.
  Hospital treatment is fluids, salts and insulin through a drip (CDC).
- **How fast:** ADA says DKA can develop quickly, and its disaster sheet says even a few hours
  of interrupted insulin can bring it on (ADA, DKA; ADA, Switching Between Insulin Products).
  Do not plan on days. **Without insulin, nothing at home reverses it.**

**"Rationing" insulin does not work.** Taking less than the body needs leads to DKA, not to
savings. What you can ration is **waste**: cold-chain failures, spilled or frozen vials, a pen
discarded half full. That is why storage gets so much space on this page.

## 5. Warning signs that mean an emergency

**Low blood sugar (hypoglycaemia), the fast danger.** Below 70 mg/dL is low (CDC). Signs: fast
heartbeat, shaking, sweating, nervousness, irritability or confusion, dizziness, hunger; then
weakness, trouble walking or seeing clearly, acting strange, seizures, fainting (CDC, Low Blood
Sugar). Lows are more likely with physical activity, too little carbohydrate for the insulin
taken, alcohol, and at night (CDC). Activity can keep lowering sugar for up to 24 hours
afterwards (NIDDK, Low Blood Glucose). **Treat first, check second** if no meter is at hand. The first-aid steps are in "Do
this now" above. **Every adult must be able to give glucagon.** Not "has watched"; has done it
with a trainer or a practice kit.

**DKA, the slow danger.** CDC's emergency list: blood sugar staying at **300 mg/dL or above**,
fruity breath, vomiting so persistent no food or fluid stays down, trouble breathing, several
DKA signs together (CDC, Diabetic Ketoacidosis). ADA adds blood ketones **1.6 mmol/L or higher**
(ADA, DKA). There is no household cure for DKA beyond insulin and fluids. **The defence is
catching ketones early**, which is why ketone strips are on the stock list.

**Decide now what "emergency" means when there is no emergency room.** For most households it
is the trigger to move toward working medical care (→ 01-02, → 01-07). Write the household's
answer: ______________________________________________

## 6. Sick-day basics

Illness, even a cold or diarrhoea, pushes blood sugar up and can start DKA in a person who is
taking their insulin. CDC's published sick-day steps (CDC, Managing Sick Days):
- **Keep taking insulin** (and any diabetes pills) as usual.
- **Check blood sugar every 4 hours** and write it down.
- **Drink plenty of water** to prevent dehydration.
- **Try to eat as normal.** If meals are impossible, CDC says to take about **50 grams of
  carbohydrate every 4 hours**, for example 1½ cups of unsweetened applesauce or 1½ cups of
  fruit juice.
- **Weigh daily** (losing weight without trying is a sign of high sugar) and **check temperature
  morning and evening** (fever may mean infection).
- **Test urine for ketones** (an over-the-counter kit); if ketones are present, call the doctor
  right away.

CDC's emergency-room list for a sick person with diabetes, as published: trouble breathing;
ketones in the urine; cannot keep liquids down for more than 4 hours, or food for more than 24
hours; losing 5 pounds or more during the illness; blood sugar lower than 60 mg/dL; vomiting
and/or severe diarrhoea for more than 6 hours; temperature over 101 °F for 24 hours.

**Dehydration multiplies everything.** High sugar drains water; vomiting and diarrhoea drain more.
Oral rehydration solution is the treatment; the World Health Organization's home recipe is 1
litre of safe water, 6 teaspoons of sugar and half a teaspoon of salt (WHO, Cholera
Q&A), with the safety notes on → 12-05. The sugar in it counts: write it in the log.

**Ask your prescriber now, while you can, and write it here:**
- How to change insulin when sick and not eating: ______________________________________________
  ______________________________________________________________________________________________
- The sugar level at which to check ketones: ____________ What to do at each ketone level:
  ______________________________________________________________________________________________
- How to treat a low when vomiting (some prescribers use small glucagon doses; only theirs counts):
  ______________________________________________________________________________________________

## 7. What to stock, and how much

The binder shows the arithmetic; you fill it in from your own bottles. The medicines tagged for this condition in settings are printed; if none are tagged, every household medicine row is, so use the ones for this condition. **Days on hand = on hand ÷ used per day.**

| Medicine or supply | On hand | Used per day | Days on hand | Days you want | Still to get |
|---|---|---|---|---|---|
{{#each meds_for.CL-01 as m}}
| {{m.name}} {{m.strength}} ({{m.member}}) | ____ | ____ | ____ | ____ | ____ |
{{else}}
{{#each meds as m}}
| {{m.name}} {{m.strength}} ({{m.member}}) | ____ | ____ | ____ | ____ | ____ |
{{/each}}
{{/each}}
| Syringes or pen needles (match the insulin strength, usually U-100) | ____ | ____ | ____ | ____ | ____ |
| Meter strips (count rises without a sensor) | ____ | ____ | ____ | ____ | ____ |
| Lancets | ____ | ____ | ____ | ____ | ____ |
| Ketone strips (urine or blood) | ____ | ____ | ____ | ____ | ____ |
| Glucagon (earliest expiry: ____) | ____ | emergency | | ____ | ____ |
| Glucose tablets, gel, juice | ____ | as needed | | ____ | ____ |
| Spare meter and its batteries | ____ | | | ____ | ____ |
| Sharps container (a rigid screw-cap bottle works) | ____ | | | ____ | ____ |
| Min/max thermometers (one per storage spot) | ____ | | | ____ | ____ |

**A second insulin type is the most common gap.** If the person uses only one kind (only
long-acting, or only rapid-acting), ask the prescriber now whether the household should hold the
other kind as a backup, and what the plan for it is. **Syringes must match the insulin strength.**
Insulin syringes are marked in units for one concentration; most US insulin is U-100. A
mismatched syringe is a dosing error. Check the vial and the syringe every time.

Used needles go in a heavy plastic bottle with a screw cap (FDA, Best Way to Get Rid of Used
Needles). Never share a syringe (ADA).

{{photo low-sugar-kits}}

> **Before the collapse:** ask the prescriber for the largest emergency supply they will write,
> move to 90-day fills, and refill at the earliest allowed date. Rotate: newest to the back of the
> fridge, use from the front. Ask whether manufacturer or nonprofit assistance programs can lower
> the cost if cost limits the buffer. In many states, older human insulins (Regular and NPH) can be
> bought at the pharmacy counter without a prescription; you must ask the pharmacist, and the
> rules differ by state. Ask your pharmacist what your state allows, and write it here: __________

## 8. Sourcing when the pharmacy is closed

| Source | Realistic? | Notes |
|---|---|---|
| Your pharmacy and others | First | A printed prescription, ID and the family medical summary (→ 25-09) help at any counter. |
| Hospitals, clinics, urgent care, disaster clinics, Red Cross, health department | Yes, while they run | Insulin is a recognised disaster need. A clinician there can direct a switch. |
| Other people with diabetes | Real | Neighbours and community groups (→ 18-01). Giving or taking someone else's prescription is a decision card: {{choice DC-15}} (→ 30-16). |
| Veterinary insulin | **No** | Different products and strengths; not an equivalent. |
| Unlabelled vials, or insulin of unknown storage | **No** | Unknown strength; may have been frozen. |

**Check anything you get:** product name, strength (U-100 or other), expiry, and appearance. Ask
how it was stored. Frozen at any point means discard (floor).

**If the only insulin you can find is a different kind** (for example, older Regular and NPH
instead of the person's usual insulin): switching changes timing and amounts. FDA and the ADA
both publish emergency switching guidance, and both say switching should be done with a
physician and close sugar monitoring (FDA; ADA, Switching Between Insulin Products in Disaster
Response Situations). **The two documents do not give the same amounts**: the ADA sheet, written
for health professionals, lowers the dose in most switches, while FDA's mostly keeps the same
number of units. That disagreement is one more reason to have the prescriber decide now. In the
Large download both documents are bound behind this page. **This binder does not convert
doses**; FDA's published text follows, for your prescriber to confirm.

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

**Prescriber, please read the FDA text above and confirm it for this person, or write what to
do instead.** Person: ____________________
Agree as printed ☐  Change as written here: _________________________________________________
_____________________________________________________________________________________________
Prescriber: ____________________ Initials: ______ Date: __________

**Ask your prescriber now, while you can, and write it here:** "If all we can get is ________
insulin, what do we give, how much, and when?"
_____________________________________________________________________________________________
_____________________________________________________________________________________________
Prescriber: ____________________ Date: __________

## 9. Power and devices

On injections, the only powered item that matters is **cold storage in summer** (→ 09-10). A
glucose meter runs for months on its small battery; keep spares. If the person uses a phone app
or a sensor, see → 02-02 and → 09-06. Nothing in this module is lost to an EMP (an
electromagnetic pulse; → 27-03) except the meter: keep a spare meter, still boxed, with its
batteries, in a metal box.

## 10. Travel and evacuation

- **Insulin rides on a person, never in a trunk or a parked car.** In winter, inside the coat
  against the body; in summer, in an evaporative pouch or insulated bag out of the sun
  (→ 12-21, → 01-07).
- **The go-bag holds a complete kit** (→ 22-06): insulin for the trip and more, syringes or pen
  needles, meter, strips, ketone strips, glucagon, fast sugar, the sharps bottle, the written plan
  from this page, and a copy of the prescription.
- **Exertion, cold and missed meals make lows more likely.** Check more often on the road and
  carry fast sugar in a pocket, not in a pack.
- **Count the clock before you leave.** If the days of insulin are fewer than the days the trip
  might take plus a margin, the trip is toward resupply or care, not away from it (→ 01-02).

## 11. Decision cards that apply

- **Heat-exposed insulin:** {{choice DC-08}} (→ 30-09).
- **Expired medicine and supplies:** {{choice DC-04}} (→ 30-05).
- **Using or giving someone else's prescription:** {{choice DC-15}} (→ 30-16).
- **When to leave home:** {{choice DC-19}} (→ 30-20). For this condition, the insulin clock is
  usually the trigger. Write the number of days at which you start looking for resupply
  (________) and the number at which you move toward care (________).
- **Frozen insulin is not a card.** It is a floor: discard (→ 30-01).

## 12. My meds

Medicines your household tagged for this condition in settings are printed below. **If none
are tagged, every medicine row your household entered is printed instead: tick the rows for
this condition** and cross out the rest. Fill any blank columns by hand from the boxes
and bottles, and add untagged medicines in the empty rows.

| For this? | Who | Medicine | Strength | Schedule | Fridge? | If doses are missed (prescriber's words) | Where kept | Days on hand | Expires |
|---|---|---|---|---|---|---|---|---|---|
{{#each meds_for.CL-01 as m}}
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

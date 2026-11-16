---
id: 02-02-cl02-type-1-diabetes-pump-and-cgm
section: 02-medical-conditions
title: "CL-02. Type 1 diabetes with an insulin pump and a sensor"
version: 3
revised: 2026-11-16
layer: condition
danger_level: critical
phase: [A, B, C]
tags: [condition library, type 1 diabetes, insulin pump, CGM, sensor, closed loop, fallback ladder, injections, device failure, charging, EMP]
derived_from: [02-03-pump-to-injection-fallback, 02-01-t1d-overview-and-supply-math, 02-02-insulin-without-the-grid, 02-04-cgm-conservation-and-dka, 29-06-total-failure-escalation, 29-10-kit-and-maintenance, 09-10-power-for-medical]
sources:
  - us-fda-information-regarding-insulin-storage-and-swi-6448d3
  - american-diabetes-association-switching-between-insu-9c5595
  - american-diabetes-association-dka-ketoacidosis-and-k-f0301a
  - cdc-diabetic-ketoacidosis-55a7c2
  - cdc-managing-sick-days-18c7c8
  - cdc-low-blood-sugar-hypoglycemia
  - fda-accessgudid-omnipod-dash-pod-device-record-stora-d28d08
  - dexcom-dexcom-g7-user-guide-sensor-storage-2-30-c-36-cf83a2
  - dexcom-dexcom-g7-sensor-wear-time-and-12-hour-grace-2b732d
  - fda-unauthorized-diabetes-devices-2019
  - loopdocs-loop-and-learn-community-updating-or-rebuil-a9d793
  - loopdocs-loop-and-learn-community-omnipod-faqs-a-pod-98ac37
  - androidaps-openaps-community-aaps-official-documenta-96e2ab
related:
  - 02-01-cl01-type-1-diabetes-injections
  - 12-11-chronic-conditions
  - 09-06-charging-medical-devices
  - 09-10-power-for-medical
  - 27-03-protecting-electronics
  - 12-21-evaporative-cooling-pouches
  - 22-06-kit-medical
  - 01-07-evacuating-with-medical-needs
  - 25-05-blank-logs
  - 29-02-ex02-batteries-and-power-stations
  - 29-07-ex07-refrigerated-medicines
  - 30-01-the-floors
  - 30-09-dc08-heat-exposed-medication
  - 30-05-dc04-expired-medication
  - 30-20-dc19-when-to-leave
cards: [DC-08, DC-04, DC-15, DC-19]
explainers: [EX-02, EX-07, EX-14]
promote_when: [has.condition.CL-02]
photo_slots:
  - { id: pump-settings-screens, caption: "Photos of every pump settings screen (basal program, ratios, correction factor, targets), retaken after each change" }
  - { id: device-spares-box, caption: "Our device spares box: spare pump supplies, sensors, charger, cables, backup controller" }
plates: []
figures: [fig-device-fallback-ladder]
condition: CL-02
gear: null
explainer: null
card: null
review_pass: { date: "2026-11-16", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "FDA pump text re-checked word for word (Novolog spelling, headings split, list kept); FDA pump storage updated to current text (48 h unless device says otherwise); ADA weight-based difference noted; meds_for tables. L8 (G31): ADA disaster switching sheet (Aug 2020, re-read from archive and live PDF, identical) printed as published next to FDA's text, not reconciled; prescriber box now covers both." }
---

# CL-02. Type 1 diabetes with an insulin pump and a sensor

**What this page is for.** An insulin pump and a continuous glucose sensor do a great deal of
the thinking in type 1 diabetes. They also add things that run out and break: pump supplies,
sensors, batteries, a phone, and sometimes software with an expiry date. This module is the
device layer. It sets out the **fallback ladder** from full automation down to a syringe and a
fingerstick meter, so that a dead battery or an empty box of sensors is an inconvenience and not
a crisis. **Read → 02-01 too**: the insulin, the cold chain, the emergencies and the sick-day
rules there apply in full.

{{#if has.condition.CL-02}}**Someone in your household has this condition.** This module is at the front of the medical section for you.{{else}}**Nobody in your household is marked with this condition.** The module stays in the binder so you can help someone else, or add the condition later in settings.{{/if}}

> **SAFETY**
> - **A pump holds only fast-acting insulin and has no reserve in the body.** When a pump stops,
>   for any reason, ketones can build within hours. **Never leave a pump failure "until
>   morning".** Go down the ladder within the hour.
> - **A frozen-then-thawed insulin vial or pen is discarded.** Freezing breaks the insulin and it
>   can look normal afterwards; FDA and the American Diabetes Association both say do not use it
>   (floor, → 30-01).
> - **The bottom rung must already be in the house:** injectable insulin, syringes or pens, a
>   meter and strips, and the prescriber's written fallback plan. A pump household without them
>   is one broken device away from DKA.
> - **This page never calculates or converts a dose.** The fallback plan is the prescriber's,
>   written in part 7 below. FDA's and ADA's emergency switching texts are printed there as
>   published, for the prescriber to confirm.

## Do this now: the device has failed

1. **Is it the device or the insulin?** Check for an alarm, a kinked or pulled-out tube or pod, a
   wet or bloody site, an empty reservoir. Check sugar with a fingerstick, and ketones.
2. **Try one fix, quickly:** new site and supplies, fresh battery or charge, restart the
   controller or phone. Give it no more than the time the system's own manual allows.
3. **Not fixed within the hour: go down the ladder** (part 4). Pump without automation if the
   pump still works; otherwise **injections, using the prescriber's plan in part 7.**
4. **Check sugar and ketones often for the first two days** after a change. The sick-day and
   emergency rules are on → 02-01.

## 1. What it is

Type 1 diabetes means the body makes no insulin (→ 02-01). An **insulin pump** is a small
device that drips fast-acting insulin under the skin all day through a tube or a stick-on
"pod". A **continuous glucose monitor (CGM)** is a sensor worn on the skin that reads sugar
every few minutes and sends it to a reader or a phone. When the pump and sensor talk to each
other and adjust insulin automatically, it is called a **closed loop** or **automated insulin
delivery**.

## 2. What runs out, and how fast

| What | Clock | When it is gone |
|---|---|---|
| Insulin | Days on hand (→ 02-01, part 2). | DKA within days. |
| Pump supplies: reservoirs or pods, infusion sets, inserters | Changed every few days by label. Count changes left. | Step down to injections. |
| Sensors | Each lasts a set number of days by label; most cannot be restarted. | Step down to fingersticks; strip use rises sharply. |
| Pump and controller power | Hours to days per charge or battery. | No delivery, or no control. |
| Phone (if it is the controller or reader) | A day or two per charge; breaks, gets lost. | Use the backup controller, then step down. |
| Software (some systems) | Some phone apps and home-built systems stop working after a set date unless rebuilt or renewed. | The app will not open; step down. |
| Adhesive patches, tape, skin wipes | Count them. | Sites fall off early, wasting supplies. |

**Write the device clocks here** and on → 23-02:
Pump supplies: ________ changes × ________ days each = ________ days.
Sensors: ________ × ________ days each = ________ days.
Software expiry date (if any): ________ Renew or rebuild before: ________

**Sensors:** wear each one for its full labelled session; some makes allow a short grace period
after the session ends (for example, one maker's 10-day sensor reads for a further 12 hours;
Dexcom, G7 sensor wear time FAQ). Change at a convenient hour, inside that window. Protect the
site with an overpatch so knocks and sweat do not end it early. Decide now at what sensor count
you stop wearing them daily and save the last ones for illness and travel: ________.

## 3. Storing insulin and supplies without power

**Insulin:** the published rules, the cold ladder and the frozen-insulin floor are on → 02-01
part 3; nothing changes for a pump user. FDA's emergency guidance adds two pump lines, printed
as published (FDA, Information Regarding Insulin Storage and Switching Between Products in an
Emergency, content current as of 09/28/2026):

> **FDA, Special Storage: Insulin Pumps:** "Insulin in the pump's infusion set (such as the
> reservoir, tubing, catheters) should be thrown away after 48 hours. Unless your pump device's
> instructions are different. For example, NovoLog, Kirsty, and Humalog U-100 specify up to 6–7
> days in the reservoir; Fiasp PumpCart specifies 4 days. Always follow the specific product's
> prescribing information and your pump device's instructions for use.
>
> If the pump insulin is exposed to temperatures above 98.6°F, throw it away."

Write your own insulin's and pump's reservoir time here: ________ (→ 29-14). A pump worn under clothes in a heatwave, or left in the sun, is the
case to watch.

**Devices and sensors have storage bands too.** Read each box (→ 29-14) and write the band
below. Two examples from labels: one tubeless pod's FDA device record gives **32 to 86 °F**
(FDA AccessGUDID, pod device record); one sensor's user guide gives **36 to 86 °F** (Dexcom, G7
User Guide). A frozen or cooked pod or sensor may fail when you start it, wasting days of
supply at the worst moment. **Spare supplies live in the room where the people live**, not a
cold garage, a car, or an unheated storeroom.

| Item | Storage band from its label | Where we keep it |
|---|---|---|
| Pump supplies (reservoirs, sets, pods) | ________ | ________ |
| Sensors | ________ | ________ |
| Meter strips, ketone strips | ________ | ________ |
| Spare pump, controller, phone | ________ | ________ |

## 4. Day by day without it: the fallback ladder

Each step down trades convenience for reliability. **Never jump further down than the failure
forces; never stay above a step that has stopped working.**

{{figure fig-device-fallback-ladder}}

| Rung | What it is | Needs | What you lose |
|---|---|---|---|
| **1. Full automation** | Pump and sensor adjust insulin together. | Pump, supplies, sensor, controller or phone, power, insulin. | Nothing. |
| **2. Backup controller or reader** | A spare phone, the pump maker's own handheld controller, or a second reader app. | The spare, charged, already set up. | Little, if it was prepared. |
| **3. Pump without automation** | The pump runs its programmed basal rates; you give meal and correction doses by button. | Pump, supplies, insulin, sugar readings, the settings copy below. | Automatic adjustment, especially overnight. Check more often. |
| **4. Injections with a sensor** | Long-acting insulin for the background, fast-acting for meals, by syringe or pen. | Both insulin types, syringes or pens, **the prescriber's plan (part 7)**. | The pump's fine control. |
| **5. Injections with a fingerstick meter** | As rung 4, sugar read by finger. | Meter, many strips, lancets. | Overnight warning. Set an alarm for a night check. |
| **6. Fast-acting insulin only** | No long-acting insulin in the house. | Frequent small injections around the clock, on a plan **only the prescriber can write**. | Sleep and margin. A bridge to getting long-acting insulin, not a way to live. |

**Rungs 4 and 5 are how most of the world manages type 1 diabetes, and they need no
electricity.** They are also the rungs pump households most often fail to prepare: no
long-acting insulin, no syringes, no written plan.

**Two things that surprise people:**
- **Some pumps and pods are tied to the controller that started them.** On some systems a pod
  started by a phone app cannot be taken over by the maker's handheld controller or another
  phone; you must start a new one (LoopDocs, Omnipod FAQs). Read your system's manual now and
  write the rule here: ______________________________________________
- **Some phone apps and home-built systems expire.** A build may stop opening after a fixed
  number of days and cannot be renewed without internet and a computer (LoopDocs, Updating or
  Rebuilding). Write the date and renew before it.

**Home-built ("do-it-yourself") closed loops exist.** Some people run open-source software that
links a pump and a sensor. FDA has warned against using devices not authorised for sale in the
United States (FDA Safety Communication, 2019). This binder does not cover building or
configuring them. **If your household uses one, save its full documentation offline now**, on
every phone and on paper for the key pages, because the community websites will not be there
when the internet is gone (LoopDocs; AndroidAPS documentation).

## 5. Warning signs that mean an emergency

Everything on → 02-01 part 5 applies: low blood sugar and DKA, with the same first aid.
Device-specific signs:
- **Sugar rising for hours with no explanation:** assume the pump is not delivering. Check
  ketones, give insulin by syringe or pen per the prescriber's plan, change the site.
- **A sensor reading that does not match how the person looks or feels:** check with a
  fingerstick before acting. Treat the person, not the number.
- **Alarm fatigue at night:** if the sensor is gone, set a timed alarm for a night fingerstick.

## 6. Sick-day basics

The sick-day rules on → 02-01 part 6 apply. With a pump, add one: **when ketones are present,
many prescribers want correction insulin given by syringe or pen, not through the pump, and the
site changed**, in case the pump is the problem. Ask yours.

**Ask your prescriber now, while you can, and write it here:** sick-day changes for a pump user;
when to switch to injections; the ketone level that means "change everything now".
_____________________________________________________________________________________________
_____________________________________________________________________________________________

## 7. What to stock, and how much

**First, copy the pump's settings to paper.** You already run every setting; this puts them
where a dead battery cannot take them. Copy them from the pump or app screens, date them, and
re-copy after every change. Photograph each screen too.

```
DATE COPIED: ____________      (re-copy after every settings change)
Basal program (time: rate per hour) ______________________________________
Total daily basal (the pump shows it) ________ units
Carbohydrate ratio(s) ____________________________________________________
Correction factor(s) _____________________________________________________
Target sugar ____________   Average total daily insulin (from the pump) ________ units
```

{{photo pump-settings-screens}}

**Then the plan that turns those settings into injections.** FDA and the ADA publish emergency
guidance on switching from a pump to injections, and both say it should be done with a
physician (FDA; ADA, Switching Between Insulin Products in Disaster Response Situations). **The
two documents do not give the same amounts**: FDA's pump section replaces the pump's doses unit
for unit, while the ADA sheet, written for health professionals, works from body weight instead.
That disagreement is one more reason to have the prescriber write the plan now. Both documents
are bound behind this page in the Large download. **This binder does not convert
doses**; FDA's published text follows, then ADA's, side by side and not reconciled, for your
prescriber to confirm.

### As published, for your prescriber to confirm

FDA's emergency guidance on switching insulin is printed here **exactly as published**, so that
you can show it to the prescriber **now** and have them confirm or change it for this person
(FDA, Information Regarding Insulin Storage and Switching Between Products in an Emergency,
content current as of 09/28/2026). It is not this binder's advice, and the binder does not work
out any amount from it. Brand names are FDA's examples.

> **FDA:** "Always switch insulin under a doctor's care, with close monitoring of your blood
> sugar. If you cannot reach a doctor during an emergency, follow the guidance below — but
> monitor your blood sugar closely and see a doctor as soon as you can."

> **FDA, Insulin Pumps:** "If your pump supplies are not available or your pump is not working
> properly, you may need to switch to injected insulin. This should be done with a doctor's
> guidance and close blood sugar monitoring whenever possible."

> **FDA, Insulin Pumps, Using a Different Insulin in Your Insulin Pump:** "In an emergency, you
> may be able to swap one rapid-acting insulin (such as Apidra, Fiasp, Humalog, Novolog) for
> another on a unit-per-unit basis. Check your pump's instructions to make sure the available
> insulins are compatible with your devices.
>
> Note: Not all rapid-acting insulins are approved for pump use. Merilog (insulin aspart-szjj) is
> not currently labeled for insulin pump use. Humalog U-200 and Lyumjev U-200 must NOT be used in
> insulin pumps. Always check the specific insulin product labeling before use in a pump."

> **FDA, Insulin Pumps, Switching from an Insulin Pump to Injected Insulin:** "If you must switch
> from your pump to injected insulin, use the following guidance:
>
> - Replace your pump's total 24-hour basal (background) dose with insulin on a unit-per-unit
>   basis.
> - For intermediate-acting insulin, split the 24-hour basal (background) dose into two equal
>   injections per day. For example, if your 24-hour basal (background) dose is 24 units, inject
>   12 units twice daily.
> - For long-acting insulin, give the full 24-hour basal (background) dose as one injection per
>   day.
> - If regular or rapid-acting insulin is also available, use it with each meal. Match your
>   pump's bolus (mealtime) dose on a unit-per-unit basis.
>   - For example, if your pump gives a bolus (mealtime) of 5 units to cover breakfast, inject 5
>     units of regular or rapid-acting insulin to cover that meal"

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

> **FDA, Short-acting (regular insulin) and Rapid-acting Insulins:** "In an emergency, you can
> switch one brand of regular insulin (such as Humulin R or Novolin R) for another brand of
> regular insulin, or for a rapid-acting insulin (such as Apidra, Fiasp, Humalog, or NovoLog),
> and vice versa. Use the same number of units.
>
> Inject regular insulins approximately 30 minutes before the start of each meal. Rapid-acting
> insulins begin working more rapidly than regular insulin and are to be injected no more than
> 15 minutes before the start of each meal to avoid dangerously low blood sugar levels."

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

> **ADA, Insulin pump:** "Insulin pump patients may only substitute Humalog®, Novolog®, Fiasp®,
> Apidra®, Admelog® or regular insulin in the pump
>
> - Substitutions cannot include an intermediate-acting insulin or a basal insulin analog or
>   concentrated insulin (i.e., U200, U300, or U500)
> - Individuals with type 1 diabetes have priority for receiving insulin. Even a few hours of
>   interrupted insulin therapy can result in life-threating Diabetic Ketoacidosis (DKA). If
>   patient does not have a back-up plan, consult with a healthcare professional experienced in
>   insulin pump management
> - When the insulin pump cannot be used, basal insulin is the primary need, with rapid- or
>   short-acting insulin as circumstances permit:
>   - Give 0.3 units/kg of a basal insulin analog as a once daily dose
>     - Example: patient weighs 60 kg, give 18 units of a basal insulin analog once daily
>   - If rapid or short acting insulin is available, give 0.3 units/kg divided by 6 at each meal
>     - Example: patient weighs 60 kg, give 3 units of rapid or short-acting insulin with each
>       meal"

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

> **ADA:** "THE RECOMMENDATIONS DO NOT REPLACE CLINICAL JUDGMENT"

**Prescriber, please read the FDA and ADA texts above and confirm one for this person, or write
what to do instead.** Person: ____________________
Agree as printed ☐  Change as written here: _________________________________________________
_____________________________________________________________________________________________
Prescriber: ____________________ Initials: ______ Date: __________

**Ask your prescriber now, while you can, and write it here** (have them write it, and initial it):
- Long-acting insulin product: ______________ Amount: ________ When: ______________
- Meals and corrections by syringe or pen: ___________________________________________
- When to stop the pump after the first long-acting dose: ____________________________
- If only fast-acting insulin is available (rung 6): __________________________________
- If only Regular and NPH are available: ____________________________________________
Prescriber: ____________________ Initials: ______ Date: __________

**Stock arithmetic.** Days on hand = on hand ÷ used per day. The medicines tagged for this condition in settings are printed; if none are tagged, every household medicine row is, so use the ones for this condition.

| Medicine or supply | On hand | Used per day | Days on hand | Days you want | Still to get |
|---|---|---|---|---|---|
{{#each meds_for.CL-02 as m}}
| {{m.name}} {{m.strength}} ({{m.member}}) | ____ | ____ | ____ | ____ | ____ |
{{else}}
{{#each meds as m}}
| {{m.name}} {{m.strength}} ({{m.member}}) | ____ | ____ | ____ | ____ | ____ |
{{/each}}
{{/each}}
| Pump supplies (reservoirs, sets or pods) | ____ | ____ | ____ | ____ | ____ |
| Sensors | ____ | ____ | ____ | ____ | ____ |
| **Long-acting insulin for the fallback** | ____ | ____ | ____ | ____ | ____ |
| **Syringes or pen needles** (match the insulin strength) | ____ | ____ | ____ | ____ | ____ |
| Meter, strips (count at fingerstick rate), lancets | ____ | ____ | ____ | ____ | ____ |
| Ketone strips | ____ | ____ | ____ | ____ | ____ |
| Pump batteries or charger, cables | ____ | | | ____ | ____ |
| Overpatches, tape, skin wipes | ____ | ____ | ____ | ____ | ____ |
| Glucagon, fast sugar, sharps bottle | ____ | | | ____ | ____ |

{{photo device-spares-box}}

> **Before the collapse:** ask the prescriber for a long-acting insulin prescription to keep as
> a backup, and syringes or pens. Practise one injection day with their agreement, so the first
> time is not the real one. Ask the pump maker about a loaner or backup pump program, and keep
> the maker's support number and your pump's serial number on → 25-09.

## 8. Sourcing when the pharmacy is closed

Insulin sources are on → 02-01 part 8. For devices:
- **Pump supplies and sensors fit only their own system.** Another brand's pods or sensors will
  not work. Write your exact part numbers here: ________________________________
- **Other people with the same system** are the realistic source of spare supplies (→ 18-01).
- **Syringes** are sold without a prescription in many states, at the pharmacist's discretion;
  ask yours now.
- **Never use a pump with insulin it was not made for** without checking its manual; FDA notes
  pump users should check that a substitute insulin is compatible with the device (FDA).

## 9. Power and devices

- **Every powered item, with its charge clock,** goes on → 09-06: pump (battery type or
  charging), controller, phone, sensor reader. Phones are the weak link: keep them charged from a
  power station or solar (→ 29-02), and keep a spare charged.
- **Heat and cold:** do not leave pumps, phones or supplies in a car, in direct sun, or in a
  freezing room. Batteries lose capacity in the cold; keep the pump under clothing.
- **EMP and geomagnetic storms** (→ 27-03): a spare controller, a spare phone with the app
  installed, and a spare meter, stored in a closed metal box, give the best chance of surviving.
  The bottom of the ladder (syringes, insulin, a battery meter in a metal box) is the part that
  survives for certain.
- Write each device's charge clock: pump ________ controller ________ phone ________ reader ________

## 10. Travel and evacuation

- **Injections travel better than a pump**: no charging, no pairing. On a long move, carry the
  full injection kit even if the pump is running (→ 01-07, → 22-06).
- Insulin on a person, never in a trunk (→ 02-01 part 10). Spare pods and sensors in the cabin,
  inside their storage band.
- **Before leaving, renew any software that expires during the trip,** charge every device, and
  pack the paper settings copy and the prescriber's plan.
- A serious device failure on the road is a reason to head for the nearest working care.

## 11. Decision cards that apply

- **Heat-exposed insulin:** {{choice DC-08}} (→ 30-09).
- **Expired supplies and medicine:** {{choice DC-04}} (→ 30-05).
- **Someone else's prescription or supplies:** {{choice DC-15}} (→ 30-16).
- **When to leave:** {{choice DC-19}} (→ 30-20).
- **Frozen insulin is a floor, not a card:** discard (→ 30-01).

## 12. My meds

Medicines your household tagged for this condition in settings are printed below. **If none
are tagged, every medicine row your household entered is printed instead: tick the rows for
this condition** and cross out the rest. Fill any blank columns by hand from the boxes
and bottles, and add untagged medicines in the empty rows.

| For this? | Who | Medicine | Strength | Schedule | Fridge? | If doses are missed (prescriber's words) | Where kept | Days on hand | Expires |
|---|---|---|---|---|---|---|---|---|---|
{{#each meds_for.CL-02 as m}}
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

**Devices:** pump model ______________ serial ______________ controller ______________
sensor model ______________ maker's support line ______________ (copy to → 25-09).

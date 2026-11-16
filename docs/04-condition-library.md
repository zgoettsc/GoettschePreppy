# Condition library

Owner decision G3: medical content at the level a careful person could find on the internet,
customised to the household, with no doctor visit needed to fill it in. The whole library is in
every binder so a condition can be added later. The household's selected conditions are promoted
to the front of the medical section and feed three other pages automatically: the medical go-kit,
power for medical devices, and protecting electronics.

## The hard rule

**No derived dosing.** The binder never calculates, adjusts or suggests a dose, a ratio or a
schedule. Where an agency or manufacturer publishes a table (epinephrine by weight band, potassium
iodide by age, oral rehydration recipe, insulin storage temperatures and days), the module prints
the table as published with the publisher named. Everything about the household's own medication
comes from the household, typed from their own bottles and their prescriber's instructions, and is
printed as written in a "my meds" table.

The household binder's T1D pages carry a physician-signed basal fallback and a daily-dose line.
Those do not come across. The module says instead: "Ask your prescriber now, while you can, what to
do if your pump fails, and write it here," with the line to write it on.

## Module template

Every module has the same twelve parts so a reader learns the shape once.

1. **What it is**, in two sentences a stranger understands.
2. **What runs out, and how fast.** The supplies and devices the condition depends on, and the
   clock on each (days of medication, sensor life, battery life, refrigeration).
3. **Storing the medication without power.** Heat, cold, freezing, light, humidity, with the
   published windows and the publisher named. Frozen-then-thawed and heat-exposed rules.
4. **Day by day without it.** What a reasonable public source says happens as the supply or
   device is lost: hours, days, weeks. Honest, not dramatic.
5. **Warning signs that mean an emergency**, and the first-aid response a layperson can give.
6. **Sick-day basics**: fever, vomiting, diarrhoea, not eating, dehydration, and how this condition
   changes them.
7. **What to stock, and how much**, as a worksheet keyed to the household's own "my meds" rows
   (the household multiplies; the binder shows the arithmetic blank).
8. **Sourcing when the pharmacy is closed**: over-the-counter equivalents where they exist,
   what to ask neighbours for, what to look for when scavenging, what is dangerous to substitute.
9. **Power and devices**: what needs charging, what breaks in heat and cold, what to protect from
   EMP (feeds the power and electronics pages).
10. **Travel and evacuation**: the supply clock on the road, cold-chain in a vehicle, what goes in
    the go-bag.
11. **Decision cards that apply** (for example DC-04 expired medication, DC-08 heat-exposed
    medication, DC-16 antibiotics without a prescription).
12. **My meds** table: name, strength, schedule, refrigerated, "if I miss doses" in the
    prescriber's words, where it is kept, how many days on hand, expiry.

Each module is 2 to 6 pages. Sources: the condition's national society fact sheets, FDA labels
and storage guidance, CDC and NIH pages, the relevant chapters of the public-domain military and
Red Cross-equivalent manuals where public domain. Copyrighted sources are fetched into the
household's private copy at download (see `07-sources-and-fetch.md`).

## The first 26 modules

| Id | Condition | Why it is in the first set | Seed in the household binder |
|---|---|---|---|
| CL-01 | Type 1 diabetes (injections) | Life-dependent on a refrigerated drug within days. | 02-01, 02-02, 02-04, 02-05, 09-10 |
| CL-02 | Type 1 diabetes with pump and CGM | Same, plus device clocks and a tech-failure ladder. | 02-03, 29-xx (method only, no loop-build) |
| CL-03 | Anaphylaxis (any cause) | Minutes matter; epinephrine storage and expiry. | 02-06, 02-07 |
| CL-04 | Food allergy (child or adult) | Unlabeled food, traded food, cross-contact. | 02-08 |
| CL-05 | Type 2 diabetes (oral and non-insulin) | Most common chronic condition; hypoglycaemia with some drugs. | 12-11 |
| CL-06 | Type 2 diabetes on insulin | As CL-01 without the same clock. | 02-02 |
| CL-07 | Asthma | Inhaler supply, triggers (smoke, cold, dust) all worse off-grid. | 12-11 |
| CL-08 | COPD and oxygen dependence | Oxygen concentrators need power; cylinders run out. | 09-06, 27-03 |
| CL-09 | High blood pressure and heart disease | Common; abrupt stopping of some drugs is dangerous; chest-pain response. | 12-11 |
| CL-10 | Anticoagulants (blood thinners) | Bleeding control changes; missed doses have a clock. | 12-02 |
| CL-11 | Epilepsy and seizure disorders | Missed doses cause seizures; seizure first aid. | 12-11 |
| CL-12 | Pregnancy, birth and postpartum | Normal birth, the emergencies, newborn care. | 12-12 |
| CL-13 | Infant feeding (nursing and formula) | Water and hygiene; formula clock; nursing parent needs. | 20-05, 03-01 |
| CL-14 | Thyroid disease | Long clock but real; levothyroxine stability. | 12-11 |
| CL-15 | Kidney disease and dialysis | Hardest case; honest about limits; fluid and potassium basics. | new |
| CL-16 | Mental-health medications | Several are dangerous to stop abruptly; the crisis page. | 12-15, 21-xx |
| CL-17 | Opioid dependence and chronic pain | Withdrawal timeline; non-drug pain methods; naloxone. | 12-13 |
| CL-18 | Immunosuppression and transplant | Infection avoidance; drug clock. | new |
| CL-19 | Celiac and severe GI disease | Food plan; dehydration. | 04-xx |
| CL-20 | Adrenal insufficiency | Stress dosing is life-critical and must come from the prescriber; printed as a worksheet. | new |
| CL-21 | Dementia and elderly care | Wandering, medication management, falls, warmth. | new |
| CL-22 | Mobility impairment | Evacuation, pressure injuries, toileting without plumbing. | 13-xx |
| CL-23 | Hearing and vision aids | Batteries, spares, backups; glasses prescription on file. | new |
| CL-24 | Sleep apnoea (CPAP) | Power budget; what happens without it. | 09-06 |
| CL-25 | Contraception and menstrual health | Supply clock; alternatives; hygiene. | 13-08 |
| CL-26 | Severe obesity and bariatric surgery | Nutrition and medication absorption off-grid; mobility. | new |

A household may also type a condition that is not in the library. The binder then prints the
template's twelve headings with blank space and the sentence: "This condition is not in the library
yet. Fill these headings from your prescriber and your pharmacy's printed information while you
still can."

## The library index page

Replaces the household binder's `12-11` page. One row per module: what it is, the supply clock in
one phrase, the emergency sign in one phrase, and the page. Selected modules are bold and first.

## What the generation model may touch in a module

Only the slots: member labels, the "my meds" rows (copied verbatim), refrigerated flags, device
names from the gear and member answers, and which decision-card choices to print. The module text
itself is frozen and shipped unchanged.

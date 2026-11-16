---
id: 02-03-cl03-anaphylaxis
section: 02-medical-conditions
title: "CL-03. Anaphylaxis (severe allergic reaction, any cause)"
version: 1
revised: 2026-11-16
layer: condition
danger_level: critical
phase: [A, B, C]
tags: [condition library, anaphylaxis, allergy, epinephrine, auto-injector, nasal epinephrine, storage, expiry, biphasic reaction, action plan]
derived_from: [02-06-hugh-anaphylaxis-action-plan, 02-07-epinephrine-storage-and-supply, 02-10-evaporative-cooling-pouches, 12-11-chronic-conditions]
sources:
  - cdc-recognizing-and-responding-to-anaphylaxis-645825
  - american-academy-of-allergy-asthma-and-immunology-aa-7f3939
  - american-academy-of-allergy-asthma-and-immunology-aa-1ca82e
  - american-academy-of-pediatrics-aap-allergy-and-anaph-3e6f49
  - american-academy-of-pediatrics-sicherer-sh-simons-fe-f0952d
  - us-fda-epipen-epinephrine-injection-usp-auto-injecto-a9f17f
  - us-fda-neffy-epinephrine-nasal-spray-prescribing-inf-b42222
  - annals-of-internal-medicine-epinephrine-auto-injecto-ea9564
  - american-college-of-allergy-asthma-and-immunology-fr-d6c10d
  - us-fda-fda-drug-safety-communication-diphenhydramine-bab442
related:
  - 02-04-cl04-food-allergy
  - 02-07-cl07-asthma
  - 12-11-chronic-conditions
  - 12-07-meds-stockpile
  - 12-18-choking-and-cpr
  - 22-06-kit-medical
  - 22-04-household-inventory
  - 26-08-expiry-and-rotation-tracker
  - 01-07-evacuating-with-medical-needs
  - 08-01-heating-one-room
  - 12-21-evaporative-cooling-pouches
  - 24-02-drills
  - 25-09-family-medical-summary
  - 29-07-ex07-refrigerated-medicines
  - 29-14-ex14-reading-a-label
  - 30-05-dc04-expired-medication
  - 30-19-dc18-unlabeled-food-and-allergies
  - 30-16-dc15-someone-elses-prescription
cards: [DC-04, DC-18, DC-15, DC-19]
explainers: [EX-07, EX-14]
promote_when: [has.condition.CL-03, has.anaphylaxis, has.epinephrine]
photo_slots:
  - { id: epinephrine-locations, caption: "Where our epinephrine lives: each spot, with the device and its expiry" }
  - { id: action-plan-signed, caption: "The signed anaphylaxis action plan from the prescriber" }
figures: [fig-auto-injector-outer-thigh, fig-anaphylaxis-positions]
plates: []
condition: CL-03
gear: null
explainer: null
card: null
review_pass: null
---

# CL-03. Anaphylaxis (severe allergic reaction, any cause)

**What this page is for.** Anaphylaxis kills in minutes, and the only drug that stops it is
epinephrine (adrenaline). This module is the response every adult in the house must be able to
do without reading, then the parts that change when there is no ambulance: how to keep
epinephrine working through heat and cold, what to do with expired devices, how many to hold,
and what to ask the prescriber now. Food allergy prevention is on → 02-04.

{{#if has.condition.CL-03}}**Someone in your household has this condition.** This module is at the front of the medical section for you.{{else}}**Nobody in your household is marked with this condition.** The module stays in the binder because anaphylaxis can strike someone with no known allergy, from a sting, a food or a medicine.{{/if}}

Your household's allergy rows: {{#each allergies as a}}**{{a.member}}**: {{a.allergen}} ({{a.severity}}; carries epinephrine: {{a.carries_epinephrine}}). {{else}}none entered.{{/each}}

> **SAFETY**
> - **Epinephrine first.** At the first sign of a serious reaction, give it at once. Delay is
>   the main cause of death. When unsure, give it (AAAAI; CDC).
> - **Antihistamines and asthma inhalers do not treat anaphylaxis.** They are never a substitute
>   for epinephrine (CDC, Recognizing and Responding to Anaphylaxis).
> - **Use the device in reach.** Whether an expired or once-frozen device is used when nothing
>   else exists is your household's decision card: {{choice DC-04}} (→ 30-05).
> - **This page prints published dose bands as published.** Which device a person carries is the
>   prescriber's choice, written on the signed action plan.

## Do this now

1. **Give epinephrine.** Auto-injector into the **outer thigh**, through clothing if needed,
   following the device's own instructions. For one common pen the label says hold it in place
   for **3 seconds** (count slowly 1, 2, 3), then rub the spot for 10 seconds (FDA, EpiPen
   label). For a nasal spray, one spray into one nostril (FDA, neffy label).
2. **Note the time.** Say it aloud or write it.
3. **Call for help** if any exists: 911, and say "anaphylaxis".
4. **Position:** lying flat with legs raised. Vomiting: on their side. Struggling to breathe:
   sitting up. **Do not stand them up or walk them** (AAAAI).
5. **Second dose** if not improving or symptoms return: AAAAI's plan says a second dose may be
   given **5 to 15 minutes** after the first; the nasal spray's label says a second spray in the
   same nostril **starting 5 minutes** after the first.
6. **Wheeze or cough after eating, in someone with asthma: epinephrine first, inhaler after.**
7. **Stay with them for hours.** Symptoms can come back without a new exposure (a "biphasic"
   reaction). Keep a second device in reach. Nothing to eat or drink until they are clearly well.

{{figure fig-auto-injector-outer-thigh}}

{{figure fig-anaphylaxis-positions}}

## 1. What it is

Anaphylaxis is a sudden, severe allergic reaction that involves the whole body. The airway can
swell shut and blood pressure can fall until the person collapses. Common triggers are foods,
insect stings, medicines and latex; sometimes no trigger is found.

## 2. What runs out, and how fast

| What | Clock | When it is gone |
|---|---|---|
| **Epinephrine devices** | Printed expiry on each device. Damaged by heat, freezing and light. | No treatment. Avoidance is the only defence. |
| Trainer devices | Do not expire, but get lost. | Carers lose practice. |
| Antihistamines (for itching and hives only, after epinephrine) | Printed expiry. | Comfort only; not life-saving. |
| Asthma inhalers, if the person has asthma | Dose counter. | Asthma makes reactions worse (→ 02-07). |

**Write the clock:** devices in date ________; earliest expiry ________; expired devices kept
________ (sorted newest first). Update at every inventory (→ 22-04) and on → 26-08.

## 3. Storing epinephrine without power

The labels, as published:

| Product | Store at | Excursions allowed | Never |
|---|---|---|---|
| Auto-injector (EpiPen and EpiPen Jr label) | **68 to 77 °F** | **59 to 86 °F** | Refrigerate or freeze; leave in a car or glove box. Keep in its carrier tube: epinephrine is damaged by light (FDA, EpiPen label). |
| Nasal spray (neffy label) | **68 to 77 °F**, in its blister pack | **Up to 122 °F** for a few days | Freeze. The label says it freezes below **5 °F** and **will not spray** if frozen; if a frozen one is needed in an emergency, do not wait for it to thaw: use another device and seek care (FDA, neffy label). |
| Other devices | Read the label (→ 29-14) and write it here: ________ | ________ | ________ |

**Check the window.** The liquid should be clear and colourless. Brown, pink, cloudy or with
particles means replace it (FDA, EpiPen label). Whether a discoloured or expired device is used
when nothing else exists is on the card (→ 30-05).

**What testing outside the label found** (planning context, printed as published):
- 40 EpiPen and EpiPen Jr devices up to 50 months past expiry all still held at least 80
  percent of the labelled dose (Cantrell and others, Annals of Internal Medicine, 2017).
- EpiPens frozen for 24 hours and thawed delivered the same dose volume as unfrozen ones
  (Cooper and others, American College of Allergy, Asthma and Immunology, 2018).

**Cold weather is the bigger risk.** In a house heated to one room (→ 08-01), the epinephrine
lives in the warm room, not in the coat on a cold hook or a pack by the door. Outdoors in
winter, carry it **inside your layers, against the body**. In summer, never in a parked car; an
insulated pouch out of the sun. Evaporative pouches are made for cooling and are not a fix for
cold (→ 12-21, → 29-07).

{{photo epinephrine-locations}}

## 4. Day by day without it

There is no "day by day" in anaphylaxis: a reaction runs its course in minutes to hours.
Without epinephrine, a severe reaction can kill (CDC). **When devices run out, the person's
only protection is strict avoidance of the trigger** (→ 02-04 for food). That is a thin margin,
and it should shape decisions about food, travel, and how close to stay to working care
(→ 01-02).

## 5. Warning signs that mean an emergency

Anaphylaxis usually involves **more than one body system**, but a severe reaction in one system
is still anaphylaxis (AAAAI; CDC).

| System | What it looks like |
|---|---|
| Skin | Hives, flushing, itching; swelling of lips, tongue, eyelids, face |
| Breathing | Cough, wheeze, hoarse voice, throat tightness, trouble breathing or swallowing |
| Gut | Vomiting, diarrhoea, cramps |
| Circulation | Pale or blue colour, weak pulse, dizziness, fainting, collapse |
| Behaviour (young children) | Sudden irritability, frantic crying, clinging, going quiet, "my mouth feels funny" |

**In a small child, trust behaviour.** A child who has just eaten and suddenly changes may be
reacting before any rash. If the person stops breathing, start CPR (→ 12-18).

**Antihistamines** may be given for itching and hives **after** epinephrine, by the prescriber's
plan. FDA warns that diphenhydramine must not be used to make a child sleep, and is not for
children under 2 (FDA, Drug Safety Communication).

## 6. Sick-day basics

- **Asthma, colds and other illness make reactions more severe.** Keep asthma well controlled
  (→ 02-07).
- **Exercise, heat, alcohol and some medicines** can make a reaction worse or trigger one in a
  person with a known allergy; the prescriber can tell you which apply.
- **After any reaction, the person is "sick" for the rest of the day:** watch them, keep a
  device in reach, no new foods.
- Vomiting and diarrhoea during a reaction can dehydrate a child; small sips once breathing is
  clearly normal (→ 12-05).

## 7. What to stock, and how much

**Published dose bands, printed as published.** The prescriber picks the device and writes it
on the action plan; this table is so you understand the plan and know when to ask for a change.

| Source | Weight band as published | Device and dose |
|---|---|---|
| FDA, EpiPen label | 15 to 30 kg (33 to 66 lb) | EpiPen Jr, 0.15 mg |
| FDA, EpiPen label | 30 kg (66 lb) or more | EpiPen, 0.3 mg |
| FDA, neffy label (ages 4 and up) | 15 kg to less than 30 kg | neffy 1 mg, one spray |
| FDA, neffy label | 30 kg or more | neffy 2 mg, one spray |
| AAP clinical report, Epinephrine for First-aid Management of Anaphylaxis (2017) | 7.5 to 15 kg (about 16 to 33 lb) | 0.15 mg auto-injector is acceptable when a 0.1 mg device is not available |
| AAP clinical report and AAP action plan | About 25 kg (55 lb) and up | AAP suggests the 0.3 mg device from this weight; the label says 30 kg. The prescriber decides. |

Weights on file (re-weigh children every few months; the band can change):
{{#each members as m}}{{m.label}}: {{m.weight_text}}. {{else}}No members entered yet.{{/each}}

**How many devices.** Devices come in two-packs, and a reaction may need two doses. Each place
the person spends time needs a pair: on the person, the home's warm room, the go-bag. When
asking the prescriber, say plainly that you are planning for a time with **no ambulance**.
The EpiPen label says that if more than two injections are needed for one reaction, only a
healthcare provider should give more (FDA, EpiPen label).

**Ask your prescriber now, while you can, and write it here:**
- Device and dose for each person, and the weight at which to change: ___________________
- How many devices to hold for a time with no ambulance: ____________
- What to do if two doses are not enough and no help is coming: _________________________
  ______________________________________________________________________________________
- If the household holds epinephrine vials and syringes as a deep backup: the exact amount to
  draw up for each person, with which syringe, written by the prescriber: ____________________
  ______________________________________________________________________________________
- Antihistamine for each person, product and amount, for itching and hives after epinephrine:
  ______________________________________________________________________________________
Prescriber: ____________________ Date: __________

{{photo action-plan-signed}}

**Stock arithmetic.** The medicines tagged for this condition in settings are printed; if none are tagged, every household medicine row is, so use the ones for this condition.

| Medicine or supply | On hand | In date | Earliest expiry | Pairs wanted | Still to get |
|---|---|---|---|---|---|
{{#each meds_for.CL-03 as m}}
| {{m.name}} {{m.strength}} ({{m.member}}) | ____ | ____ | ____ | ____ | ____ |
{{else}}
{{#each meds as m}}
| {{m.name}} {{m.strength}} ({{m.member}}) | ____ | ____ | ____ | ____ | ____ |
{{/each}}
{{/each}}
| Epinephrine devices | ____ | ____ | ____ | ____ | ____ |
| Trainer device for each device type | ____ | | | ____ | ____ |
| Insulated pouch for each carry set | ____ | | | ____ | ____ |
| Min/max thermometer where devices are stored | ____ | | | ____ | ____ |
| Medical ID (bracelet or card) | ____ | | | ____ | ____ |

**Everyone who cares for the person practises with a trainer**, for every device type in the
house: they inject differently. Rehearse the whole sequence, not just the click (→ 24-02).

> **Before the collapse:** get a signed action plan from the prescriber, refill before expiry,
> and set calendar reminders for every expiry date. Ask about a needle-free nasal device as a
> second form: its label allows short heat excursions that would ruin an auto-injector, but it
> fails if frozen (FDA, neffy label).

## 8. Sourcing when the pharmacy is closed

- **There is no household substitute for epinephrine.** Antihistamines are not one; inhalers are
  not one.
- **Pharmacies, clinics and disaster medical points** are the realistic resupply. Keep the
  prescription printed (→ 25-09).
- **Other households** with allergic members may hold devices. Using someone else's prescription
  is a decision card: {{choice DC-15}} (→ 30-16). Decide it before a reaction, not
  during one.
- **When scavenging**, check expiry and the window. A device left in a hot car or a frozen
  vehicle has had a hard life; your household's rule on using it is on → 30-05.

## 9. Power and devices

Epinephrine needs no power. Some auto-injectors have a small battery for spoken instructions;
the injection still works if the voice fails. Nothing here is lost to an EMP (→ 27-03). The
power question is **heat in summer**: if the house has no cooling, find the coolest stable spot
and use a thermometer.

## 10. Travel and evacuation

- **Devices travel on the person, inside layers in winter, out of the sun in summer.** Never in
  a trunk, a roof box or a parked car (→ 01-07).
- **Two devices at least in every carry set**, plus the action plan and the prescription
  (→ 22-06).
- **Communal, donated and roadside food is the highest-risk food on a move** (→ 02-04). Carry
  enough safe food that the allergic person never needs it.
- **Know where care is** along the route, and decide in advance that a reaction on the road means
  heading for it.

## 11. Decision cards that apply

- **Expired, frozen or heat-exposed epinephrine:** {{choice DC-04}} (→ 30-05).
- **Unlabelled, traded or scavenged food for the allergic person:** {{choice DC-18}} (→ 30-19).
- **Someone else's prescription:** {{choice DC-15}} (→ 30-16).
- **When to leave:** {{choice DC-19}} (→ 30-20). Running out of in-date devices, or of safe food,
  is a reason to move toward supply.

## 12. My meds

Medicines your household tagged for this condition in settings are printed below. **If none
are tagged, every medicine row your household entered is printed instead: tick the rows for
this condition** and cross out the rest. Fill any blank columns by hand from the boxes
and bottles, and add untagged medicines in the empty rows.

| For this? | Who | Medicine | Strength | Schedule | Fridge? | If doses are missed (prescriber's words) | Where kept | Days on hand | Expires |
|---|---|---|---|---|---|---|---|---|---|
{{#each meds_for.CL-03 as m}}
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

**Device log** (one line per device; copy to → 26-08):

| Where | Device and dose | Expiry | Window clear? | Checked (date) |
|---|---|---|---|---|
| On the person | ________ | ______ | ☐ | ______ |
| Warm room at home | ________ | ______ | ☐ | ______ |
| Go-bag | ________ | ______ | ☐ | ______ |
| Other: ________ | ________ | ______ | ☐ | ______ |

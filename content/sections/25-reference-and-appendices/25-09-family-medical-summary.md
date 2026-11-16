---
id: 25-09-family-medical-summary
section: 25-reference-and-appendices
title: "Family medical summary sheet"
version: 1
revised: 2026-11-16
layer: household
danger_level: critical
phase: [A, B, C]
tags: [medical summary, responder, medicines, allergies, conditions, devices, prescribers]
derived_from: [25-09-family-medical-summary]
sources:
  - cdc-recognizing-and-responding-to-anaphylaxis-645825
  - american-academy-of-allergy-asthma-and-immunology-aa-7f3939
  - cdc-diabetic-ketoacidosis-55a7c2
  - us-fda-information-regarding-insulin-storage-and-swi-6448d3
  - usa-gov-replace-your-vital-documents-cde79b
related: [22-06-kit-medical, 25-08-quick-reference-cards, 19-01-document-grab-kit, 19-03-records-and-backups, 25-03-regional-contacts, 25-10-annual-review, 01-07-evacuating-with-medical-needs, 12-07-meds-stockpile, 02-03-cl03-anaphylaxis, 20-09-pets]
cards: []
explainers: [EX-07, EX-14]
promote_when: [has.refrigerated_meds, has.anaphylaxis, has.oxygen, has.cpap, has.mobility_aid]
photo_slots: []
figures: []
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: null
---

# Family medical summary sheet

**What this page is for.** This sheet lets **someone who has never met your family keep them
alive**: a paramedic, an emergency-room nurse, a neighbour, a relative, a shelter volunteer. It
holds conditions, allergies, medicines, devices and contacts, filled from your settings, with
blanks for the rest. **It contains no treatment instructions on purpose.** Those are the
prescribers' written plans, which are attached to it.

> **SAFETY — CRITICAL.**
> - **Fill it in with your prescribers, not from memory**, and have them check it.
> - **Medicines are printed exactly as typed from the bottles.** The binder never works out or
>   changes a dose.
> - **Attach each condition's signed or written plan** (anaphylaxis action plan, pump-failure
>   plan, seizure plan, sick-day plan). A summary without the plans is half a document.

## Do this now

1. **Check every printed line against the bottles and devices**, and fill the blanks at your
   next appointments.
2. **Make copies**: the medical kit (→ 22-06), every go-bag (→ 22-03), every vehicle, one with
   the out-of-area contact{{#if has.child}}, and one at each school or daycare{{/if}}.
3. **Attach the plans** to every copy.
4. **Photograph it and store the photo off-site** (→ 19-03); keep a copy in the document kit
   (→ 19-01).
5. **Re-check it every year and after any change** in medicine, device, weight of a growing
   child, or prescriber (→ 25-10).

## What this sheet is, and is not

| It IS | It is NOT |
|---|---|
| A **record**: conditions, allergies, medicines, devices, contacts | A prescription or a dosing sheet |
| What you hand to a responder | A substitute for the prescribers' written plans |
| A supply snapshot for planning (→ 22-04, → 23-02) | Medical advice of any kind |

**Two rules:** write **exactly** what the label and the prescriber say (medicine, strength,
device model), and **date every version**. An undated medical summary is dangerous because
nobody can tell how old it is.

## First, in a box at the top

{{ai responder-first-three}}

Copy these lines by hand onto an index card for every wallet today, before the full sheet is
finished.

## Household medical summary

```
DATE COMPLETED: ____________   VERSION: ______   COMPLETED BY: ____________
NEXT REVIEW DUE: ____________
ADDRESS (write by hand): __________________________________________
```

Emergency contact (out of area): {{ contacts.out_of_area.name }} · {{ contacts.out_of_area.phone }}

{{#each members as m}}

### {{m.label}} ({{m.role}}, {{m.age_text}})

| | |
|---|---|
| **Full name** | ______________________________ |
| **Date of birth** | ____________ |
| **Weight** | {{m.weight_text}} · re-weighed on ______: ______ |
| **Blood type** | ______ |
| **Conditions** | {{m.conditions}} |
| **Allergies** | {{m.allergies}} |
| **Medicines** | {{m.meds}} (details in the table below) |
| **Pregnant or nursing** | {{m.pregnant_or_nursing}} |
| **Devices** (model and serial; device support phone from the box) | ______________________________ |
| **Plans attached** (name and date of each) | ______________________________ |
| **Other conditions, surgeries, implants** | ______________________________ |
| **Immunisations; last tetanus booster** | ______________________________ |
| **Glasses or hearing aids** (prescription, where spares are) | ______________________________ |
| **Prescribers and phones** | ______________________________ |
| **Pharmacy and phone** | ______________________________ |
| **Insurance and member number** | ______________________________ |
| **Medical ID worn? Wording** | ______________________________ |
| **Communication needs** (language, hearing, memory) | ______________________________ |
{{/each}}

## Medicines, exactly as typed from the bottles

| Person | Medicine | Strength | Schedule | Refrigerated | If doses are missed (prescriber's words) | Where kept | Expiry | Days on hand |
|---|---|---|---|---|---|---|---|---|
{{#each meds as x}}| {{x.member}} | {{x.name}} | {{x.strength}} | {{x.schedule}} | {{x.refrigerated}} | {{x.if_missed}} | {{x.where_kept}} | {{x.expiry}} | {{x.days_on_hand}} |
{{else}}| none entered | | | | | | | | |
{{/each}}

{{#if has.refrigerated_meds}}**Refrigerated medicine is in this household.** It must not freeze; **a frozen-then-thawed
insulin vial or pen is discarded** (FDA, Insulin Storage in an Emergency; → 29-07).
{{/if}}

## Allergies

| Person | Allergen | Severity | Carries epinephrine |
|---|---|---|---|
{{#each allergies as a}}| {{a.member}} | {{a.allergen}} | {{a.severity}} | {{a.carries_epinephrine}} |
{{else}}| none entered | | | |
{{/each}}

{{#if has.anaphylaxis}}**Anaphylaxis risk in this household. Epinephrine is the first treatment; antihistamines are
not. A second dose is often needed** (CDC, Recognizing and Responding to Anaphylaxis; AAAAI,
Anaphylaxis Emergency Action Plan). Epinephrine locations, all of them: ______________________
Total devices: ______ · earliest expiry: ______
{{/if}}

## Supply snapshot (update weekly in a long event; → 23-02)

| Item | Count | Days at normal use | Earliest expiry |
|---|---|---|---|
{{#each meds as x}}| {{x.member}}: {{x.name}} | ______ | {{x.days_on_hand}} | {{x.expiry}} |
{{/each}}| Device supplies: ______________ | ______ | ______ | ______ |
| Rescue medicines: ______________ | ______ | n/a: never rationed | ______ |

{{#if has.pets}}
## Pets

| Pet | Count | Medicines | Food per day | Vet and phone | Microchip numbers |
|---|---|---|---|---|---|
{{#each pets as p}}| {{p.type}} | {{p.count}} | {{p.medications}} | {{p.food_per_day}} | ______________ | ______________ |
{{/each}}
{{/if}}

## Household notes

```
BLOOD TYPES (all): ______________________________________________
DRUG ALLERGIES (all, together): _________________________________
ADVANCE DIRECTIVES / MEDICAL POWER OF ATTORNEY, where kept: ______
WHERE THE MEDICAL KIT LIVES: ____________________________________
WHERE THE PLANS ARE POSTED: _____________________________________
COPIES OF THIS SHEET ARE AT: ____________________________________
```

## Gear

**Buy toward:** a waterproof sleeve or laminator for each copy, **medical ID jewellery or tags**
for anyone with a life-threatening condition or allergy, a small stapler to attach the plans, a
phone for the off-site photo, and **each prescriber's written plan, printed, signed and dated**.

**If you do not have it:** a hand-written index card carrying the box at the top of this page
is a real, useful substitute: **write it today.** Perfect is the enemy of having anything at all
in a wallet.

## When it goes stale

The sheet does not run out; **its accuracy does, quickly.**

- **About a year at most**, and **at once** after any change of medicine, device, prescriber,
  or a growing child's weight.
- **Never make fewer copies to save paper.** A copy that is not where the emergency is does
  nothing.
- **Re-check at the annual review and after every appointment** (→ 25-10).
- The cards (→ 25-08) carry the emergency part, but not the prescriber contacts, device serials
  or supply counts that make **this** sheet the one a clinic needs.

## Phase notes

- **A (shelter in place):** keep it current and spread around. Most of its value is in ordinary
  life: a hospital visit, a babysitter, a school form.
- **B (moving):** it travels in the medical kit and the document kit, and a copy is with the
  out-of-area contact. **It lets someone else speak for your family** if you cannot (→ 01-07).
- **C (establish):** it is what you hand a clinician, a pharmacist or a mutual-aid group in a
  new place. Keep the supply snapshot current: it decides what you have to ask for (→ 12-07).

Related: → 22-06 the medical kit this lives in · → 25-08 the card version · → 19-01 document kit
· → 19-03 off-site copies · → 25-03 prescriber contacts · → 25-10 review · → 01-07 medical needs
on the road.

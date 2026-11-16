---
id: 26-08-expiry-and-rotation-tracker
section: 26-pre-disaster-acquisition-checklist
title: "Expiry and rotation tracker"
version: 1
revised: 2026-11-16
layer: core
danger_level: caution
phase: [A, B, C]
tags: [expiry, rotation, tracker, medicines, bleach, batteries, food dates]
derived_from: [26-08-expiry-and-rotation-tracker]
sources:
  - us-fda-information-regarding-insulin-storage-and-swi-6448d3
  - us-epa-emergency-disinfection-of-drinking-water-6aa91f
  - national-center-for-home-food-preservation-nchfp-gen-c43991
  - cdc-recognizing-and-responding-to-anaphylaxis-645825
  - fsis-food-product-dating
  - usfa-smoke-alarms
related: [26-03-checklist-life-safety, 04-10-rotation-and-inventory, 22-03-go-bags-and-kits, 22-05-kit-vehicle, 12-07-meds-stockpile, 03-04-purifying-water, 25-10-annual-review, 29-14-ex14-reading-a-label, 26-09-shopping-list-and-budget]
cards: [DC-04, DC-14]
explainers: [EX-14]
promote_when: []
photo_slots: []
figures: []
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: null
---

# Expiry and rotation tracker

**What this page is for.** Expiry is the failure nobody notices until the morning it matters.
This sheet puts every date found on the walk (→ 26-02) in one place you can scan in thirty
seconds. **It prints no shelf-life figures on purpose**: the label is the authority, and for
medicine so are your pharmacist and prescriber. How to read the dates: → 29-14.

> **CAUTION.**
> - **Never quietly rely on an expired medicine.** If something critical is close to expiry,
>   that is a conversation with the prescriber now, not a decision in an emergency (→ 12-07).
>   What the household does when nothing in date exists: {{choice DC-04}} → 30-05.
> - **A frozen-then-thawed insulin vial or pen is discarded**, whatever its date.
> - **Bulging, leaking or spurting cans are thrown out, unopened.**

## Do this now

1. **Copy every date you found on the walk** onto this sheet, soonest first.
2. **Circle anything expiring within six months.** That is this year's replacement list; it
   goes to → 26-09.
3. **Re-run this sheet on the two kit-check dates** with the go-bags (→ 22-03).

## Three kinds of expiry

| Kind | What it means | Examples |
|---|---|---|
| **Hard** | Stops working or becomes unsafe. **Replace on schedule** | Rescue medicines, insulin and other refrigerated medicines, glucagon, test and ketone strips, infant formula, canning lids |
| **Fading** | Loses strength or performance slowly: still there, works less well | **Bleach** (weakens on the shelf; → 29-05), batteries, sunscreen, fuel, seed |
| **Quality** | A best-quality date, not a safety cliff (USDA FSIS, Food Product Dating) | Most dry staples; canned goods stored cool and dry. Dented or rusty cans: {{choice DC-14}} → 30-15 |

**Treat every medical row as hard, always.** Everything else can be judged; those cannot.

## The rule for rotation

**Store what you eat, eat what you store, oldest first** (→ 04-10). Anything used only in an
emergency is the thing most likely to be expired when the emergency comes, which is why go-bag
and vehicle food need a set rotation date, not good intentions.

## Dates that are not printed on the product

Some things have no stamp but still have a clock. Write the date you got them, in marker, on
the item:

- **Bleach**: the **purchase** date; it loses strength over months (EPA, Emergency Disinfection
  of Drinking Water; → 03-04).
- **Stored water**: the **fill** date (→ 03-02).
- **Firewood**: when it was **split and stacked**; seasoning takes 6 to 12 months (→ 06-03).
- **Seed**: the **packet year**; germination falls each year (→ 05-03).
- **Fuel**: when it was bought and when stabiliser was added (→ 06-06).
- **Filter elements**: **gallons used**, not a date (→ 03-09).
- **Home-canned food**: the **date canned** and the recipe (NCHFP; → 04-05).
{{#if has.child}}- **Children's clothing**: the **size**, which expires faster than any date on this page.
{{/if}}

## The tracker, soonest first

```
DATE COMPLETED: ____________        NEXT REVIEW: ____________

KIND   ITEM                              LOCATION            EXPIRES     ACTION
_____  ________________________________  __________________  __________  ________
_____  ________________________________  __________________  __________  ________
_____  ________________________________  __________________  __________  ________
_____  ________________________________  __________________  __________  ________
_____  ________________________________  __________________  __________  ________
_____  ________________________________  __________________  __________  ________
_____  ________________________________  __________________  __________  ________
_____  ________________________________  __________________  __________  ________
_____  ________________________________  __________________  __________  ________
_____  ________________________________  __________________  __________  ________
_____  ________________________________  __________________  __________  ________
_____  ________________________________  __________________  __________  ________
_____  ________________________________  __________________  __________  ________
_____  ________________________________  __________________  __________  ________
_____  ________________________________  __________________  __________  ________
_____  ________________________________  __________________  __________  ________

KIND:   H = hard (replace on schedule) · F = fading · Q = quality only
ACTION: R = replace now · 6 = replace within 6 months · U = use it up first · OK
```

## The medical block: check this one separately, every time

**Medicines from settings:**

| Person | Medicine | Where kept | Expires | Days on hand |
|---|---|---|---|---|
{{#each meds as x}}| {{x.member}} | {{x.name}} | {{x.where_kept}} | {{x.expiry}} | {{x.days_on_hand}} |
{{else}}| none entered | | | | |
{{/each}}

**Everything else medical:**

| Item | Location | Expires |
|---|---|---|
{{#if has.epinephrine}}| Epinephrine: the allergic person's bag | ______ | ______ |
| Epinephrine: each adult's bag | ______ | ______ |
| Epinephrine: house kit | ______ | ______ |
| Epinephrine: school, daycare or work | ______ | ______ |
| Epinephrine: each vehicle (backup) | ______ | ______ |
{{/if}}| Other rescue medicines (glucagon, inhaler, seizure, naloxone) | ______ | ______ |
| Device supplies (sensors, pump parts, test and ketone strips, CPAP filters) | ______ | ______ |
{{#if has.infant}}| Infant formula | ______ | ______ |
| Infant fever reducer | ______ | ______ |
{{/if}}{{#if has.child}}| Children's pain and fever medicine | ______ | ______ |
{{/if}}| Adult pain and fever medicine | ______ | ______ |
| Antibiotics, if prescribed | ______ | ______ |
| Oral rehydration salts | ______ | ______ |
{{#if has.pets}}| Pet medicines | ______ | ______ |
{{/if}}

```
SOONEST MEDICAL EXPIRY: ______________________ on ____________
SHORTEST MEDICAL CLOCK: ______________________ = ______ days   (23-01)
```

{{#if has.epinephrine}}> **Every location holding epinephrine gets its own line**, because the one that expires is
> always the one nobody checks: the spare in the car. A second dose is often needed, so each
> location needs a pair (CDC, Recognizing and Responding to Anaphylaxis).
{{/if}}

## The date-stamped items

| Item | Date got or done | Notes |
|---|---|---|
| Bleach | ______ | Replace on schedule (→ 03-04) |
| Stored water | ______ | Rotate (→ 03-02) |
| Firewood stacked | ______ | Seasoned when? (→ 06-03) |
| Seed packets | ______ | Year (→ 05-03) |
| Fuel + stabiliser | ______ | (→ 06-06) |
| Filter element | ______ gal used of ______ | (→ 03-09) |
| Smoke and CO alarm batteries | ______ | The alarms themselves wear out: read the date on the back (USFA, Smoke Alarms; → 29-12) |
| Fire extinguisher | ______ | Gauge in the green? |
| Go-bag food rotated | ______ | (→ 22-03) |
| Vehicle kit food rotated | ______ | (→ 22-05) |
{{#each members as m}}| {{m.label}}: clothing size now | ______ | Next size on hand? |
{{/each}}

## Gear

**Buy toward:** a permanent marker (write the purchase date on each item the day it comes home:
the single habit that makes most of this page unnecessary), labels, and a wall calendar with the
two kit-check dates marked.

**If you do not have it:** any notebook. **The substitute for tracking is discovering it in an
emergency**, which is not a substitute.

## When it goes stale

- **About six months**, less for anything medical.
- **If you track only one block, track the medical block.**
- **Refresh** on the two kit-check dates (→ 22-03), fully at the yearly review (→ 25-10).

## Phase notes

- **A (shelter in place):** keep it current; most of its value is in ordinary life.
- **B (moving):** only the medical block matters, and it travels with → 25-09.
- **C (establish):** restart it in the first month; the clocks keep running wherever you are.

Related: → 26-03 where the medical dates come from · → 04-10 food rotation · → 22-03 and → 22-05
kit checks · → 12-07 medicine supply · → 03-04 bleach strength · → 29-14 reading a label ·
→ 25-10 review.

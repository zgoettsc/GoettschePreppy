# ai block: responder-first-three

- **Used on:** `25-09-family-medical-summary` (household layer), under "First, in a box at the
  top", above the per-person tables.
- **Written by:** C02, 2026-11-16.

## Purpose

The household binder's medical summary opened with a hand-written box: "the three things a
responder must know first" (who is dependent on which medicine or device, who has anaphylaxis
and to what, and what has no substitute). A template can print every row, but it cannot pick out
the few life-critical facts across members, conditions, allergies, medicines and devices and
order them by urgency. This block does that, from the household's own answers only.

## Inputs (exact context paths; nothing else)

- `members[]`: `label`, `role`, `age_text`, `conditions` (condition-library titles, plus any
  free-text "other" condition), `pregnant_or_nursing`
- `allergies[]`: `member`, `allergen`, `severity`, `carries_epinephrine`
- `meds[]`: `member`, `name`, `refrigerated` (do **not** use `strength`, `schedule`,
  `if_missed`, `days_on_hand`)
- flags: `has.anaphylaxis`, `has.epinephrine`, `has.refrigerated_meds`, `has.oxygen`,
  `has.cpap`, `has.mobility_aid`, `has.pregnant`, `has.nursing`, `has.infant`,
  `has.condition.CL-NN`

## Output

- A Markdown blockquote of **one to five numbered lines**, most urgent first, each in capitals
  for the person's label and the key fact, in this shape:
  `> 1. LABEL (age): CONDITION OR ALLERGY. What it depends on. → 02-NN`
- Order of urgency: anaphylaxis (any `allergies` row with severity anaphylaxis); dependence on a
  medicine whose absence is an emergency within days (insulin, adrenal insufficiency, anti-seizure,
  anti-rejection, as named by the person's conditions); oxygen or other powered device;
  pregnancy or a newborn; mobility or memory needs that change how a responder moves the person;
  then anything else a condition page marks as an emergency.
- For anaphylaxis lines: name the allergen(s) exactly as typed and add "EPINEPHRINE FIRST" if
  `has.anaphylaxis` is true. Do not add device strengths.
- For medicine lines: name the medicine exactly as typed and add "REFRIGERATED" if
  `refrigerated` is true. Never a dose, strength or schedule.
- End with one final line, always: `> Medicines and devices listed below have no substitute in
  this household's plan. Plans from the prescribers are attached.`
- If no member has any condition, allergy, medicine or device marked in settings, output exactly:
  `> No condition, allergy, medicine or device is entered for this household. If that changes,
  update settings and regenerate.`

## Constraints

- **Never introduce** a dose, strength, timing, number, phone number, product name, diagnosis,
  law or procedure not in the inputs. Do not infer a condition from a medicine name or a medicine
  from a condition.
- Do not describe treatment beyond "EPINEPHRINE FIRST" for anaphylaxis. Treatment lives in the
  attached plans and the condition pages.
- Medicine and allergen names exactly as typed. Labels exactly as typed.
- Use only the page references `→ 02-NN` where NN is the CL number of a selected condition, and
  `→ 02-03` for anaphylaxis.
- Plain words, calm. No headings, no tables.

## Length

At most six lines in total, each at most 25 words.

## Example shape (illustrative only; never copy)

> 1. SAM (6): ANAPHYLAXIS TO PEANUT. EPINEPHRINE FIRST. → 02-03
> 2. ALEX (41): TYPE 1 DIABETES, INSULIN DEPENDENT. Insulin (REFRIGERATED). → 02-01
> 3. RIVER (9 months): INFANT; FEEDING PLAN ATTACHED. → 02-13
> Medicines and devices listed below have no substitute in this household's plan. Plans from the prescribers are attached.

# ai block: roles-must-know

- **Used on:** `00-07-household-roles` (household layer), directly under "The one that is not
  optional".
- **Written by:** C01, 2026-11-16.

## Purpose

Name, for this household, the life-sustaining routines that every adult must be able to run, and
whose routine each one is, so the generic paragraph above it becomes concrete. The template cannot
do this because it needs to pick out, from members, conditions, allergies, medicines and devices,
only the items that are life-sustaining, and group them by person.

## Inputs (exact context paths; nothing else)

- `members[]`: `label`, `role`, `age_text`, `conditions` (condition-library ids and titles, plus
  the free-text "other" condition if present)
- `allergies[]`: `member`, `allergen`, `severity`, `carries_epinephrine`
- `meds[]`: `member`, `name`, `refrigerated` (do **not** use `strength`, `schedule` or `if_missed`)
- flags: `has.anaphylaxis`, `has.epinephrine`, `has.refrigerated_meds`, `has.oxygen`, `has.cpap`,
  `has.mobility_aid`, `has.infant`, `has.pregnant`, `has.nursing`, `has.condition.CL-NN`
- the titles and kit page ids of the selected condition-library modules (Section 02 page ids,
  `02-NN`, where `NN` is the CL number)

## Output

- A Markdown bullet list, one bullet per person who has at least one life-sustaining routine, in
  the order of `members[]`. Each bullet: the person's label in bold, then the routine(s) in plain
  words, each followed by the page reference in the form `→ 02-NN` (the condition module) or
  `→ 02-03` (anaphylaxis), `→ 29-07` (refrigerated medicines), `→ 09-06` (powered devices).
- What counts as a routine: giving or backing up a refrigerated or daily medicine; recognising and
  treating that condition's emergency as the module describes it (name it only, e.g. "a severe
  low", "anaphylaxis", "a seizure"; do not describe treatment steps); keeping a powered device
  running (oxygen, CPAP); moving someone who uses a wheelchair or walker; infant feeding.
- After the list, one sentence: "Each of these has its own page; every adult reads it and practises
  the emergency part with a trainer or the prescriber (→ 24-01)."
- If no member has any such routine: output exactly one sentence: "No one in this household has a
  condition, allergy, medicine or device marked life-sustaining in settings. If that changes,
  regenerate the binder, and the routine will be listed here."

## Constraints

- **Never introduce** a number, dose, timing, phone number, product name, law or procedure that is
  not in the inputs. Do not restate strengths or schedules. Do not explain how to treat anything:
  the condition pages do that.
- Do not infer a condition from a medicine name, or a medicine from a condition. Use only what is
  typed.
- Do not rank people or judge the household. No reassurance, no alarm.
- Plain words, short sentences, the binder's voice (calm, direct). No headings, no tables.
- Medicine names exactly as typed.

## Length

At most 8 bullets, each at most 30 words; total at most 220 words.

## Example shape (illustrative only; never copy)

- **Alex**: daily refrigerated medicine and its cold chain (→ 29-07); recognising a severe low
  (→ 02-01).
- **Sam**: anaphylaxis to a food; epinephrine first (→ 02-03).

Each of these has its own page; every adult reads it and practises the emergency part with a
trainer or the prescriber (→ 24-01).

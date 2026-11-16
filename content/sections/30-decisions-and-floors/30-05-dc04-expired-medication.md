---
id: 30-05-dc04-expired-medication
section: 30-decisions-and-floors
title: "DC-04. Expired or heat-exposed epinephrine, and other expired medication"
version: 1
revised: 2026-11-16
layer: card
danger_level: critical
phase: [A, B, C]
tags: [decision card, medication, expired, epinephrine, anaphylaxis, shelf life, storage]
derived_from: [02-07-epinephrine-storage-and-supply, 12-07-meds-stockpile, 02-06-hugh-anaphylaxis-action-plan]
sources:
  - us-fda-epipen-epinephrine-injection-usp-auto-injecto-a9f17f
  - annals-of-internal-medicine-epinephrine-auto-injecto-ea9564
  - american-college-of-allergy-asthma-and-immunology-fr-d6c10d
  - lyon-rc-et-al-journal-of-pharmaceutical-sciences-95-1d6bf3
  - fda-dont-be-tempted-to-use-expired-medicines
  - american-academy-of-allergy-asthma-and-immunology-aa-7f3939
  - cdc-recognizing-and-responding-to-anaphylaxis-645825
related: [02-03-cl03-anaphylaxis, 02-04-cl04-food-allergy, 12-07-meds-stockpile, 26-08-expiry-and-rotation-tracker, 22-04-household-inventory, 29-07-ex07-refrigerated-medicines, 29-14-ex14-reading-a-label, 30-09-dc08-heat-exposed-medication, 30-01-the-floors]
cards: [DC-04, DC-08]
explainers: [EX-07, EX-14]
promote_when: [has.epinephrine, has.anaphylaxis]
card: DC-04
options:
  - id: discard
    label: "Discard at the printed date"
    summary: "Expired, frozen-and-thawed or heat-damaged medication is replaced and not used. The household keeps enough in-date supply that it never faces the question."
  - id: use-if-clear
    label: "Use if clear and colourless; keep seeking in-date stock"
    summary: "When no in-date supply exists: in anaphylaxis, an expired or thawed epinephrine device whose liquid is clear and colourless is used at once. Intact tablets past date may be used. Liquids that changed are not. Keep looking for in-date stock."
settings_summary: "Every medicine has an expiry date: the date until which the maker guarantees full strength. Labels also give a storage range; epinephrine auto-injectors (EpiPen type) should not freeze or get hot. After the date, or after freezing or heat, strength can drop slowly, and some liquids can change. In anaphylaxis (a severe allergic reaction), a weak dose is worse than a full one, but no dose can be fatal. Published studies found most expired auto-injectors still held most of their dose, and frozen-then-thawed ones delivered a normal dose. What helps most: keep enough in-date supply, rotated, at the right temperature (removes it); check the window for clear, colourless liquid (reduces it a lot). This card does not cover insulin: frozen insulin is always thrown away."
review_pass: null
---

# DC-04. Expired or heat-exposed epinephrine, and other expired medication

**What this page is for.** When supplies stop, the medicine you have may be past its date, or
may have frozen in a car or cooked in a hot room. This card is about whether to use it when
nothing in-date exists. It is not a dosing guide.

> **SAFETY.** A frozen-then-thawed insulin vial or pen is discarded (floor, → 30-01). That
> floor is not part of this card. In anaphylaxis, give epinephrine first and think second;
> → 02-03.

## 1. The thing, in plain words

**Epinephrine** (adrenaline) is the drug that treats **anaphylaxis**, a severe allergic
reaction that can close the airway and drop blood pressure within minutes. It usually comes in
an **auto-injector** (EpiPen type), a pen you press against the thigh. It has a small window to
see the liquid.

An **expiry date** is the date until which the maker guarantees full strength and safety when
stored as the label says (→ 29-14). After it, most medicines lose strength slowly; a few change
in ways that matter. **Storage range** is the temperature band on the label.

Your household's allergy rows: {{#each allergies as a}}{{a.member}}, {{a.allergen}} ({{a.severity}}); {{else}}none entered.{{/each}}

## 2. The rule, and why it was set

- The FDA prescribing information for the EpiPen says store it at room temperature (68 to
  77 °F, brief trips 59 to 86 °F), do not refrigerate or freeze it, and replace it if the
  liquid is discoloured or has particles (FDA, EpiPen prescribing information).
- FDA advises the public not to use expired medicines, because strength and safety after the
  date are not guaranteed (FDA, Don't Be Tempted to Use Expired Medicines).

**Why:** a maker can only promise what it has tested. Strength and stability are tested up to
the printed date under the printed storage conditions. Beyond that, the maker does not know,
so the label says replace.

**What testing outside the label has found:**
- 40 EpiPen and EpiPen Jr devices tested up to 50 months past their date all still held at
  least 80 percent of the labelled dose, most over 90 percent (Cantrell and others, Annals of
  Internal Medicine, 2017).
- EpiPens frozen for 24 hours and thawed delivered the same dose volume as unfrozen ones
  (Cooper and others, American College of Allergy, Asthma and Immunology, 2018).
- The US military's Shelf Life Extension Program found most intact tablets and capsules,
  stored well, stayed potent years past their dates; liquids and some drugs were exceptions
  (Lyon and others, Journal of Pharmaceutical Sciences, 2006).

## 3. How it actually hurts people

**Using it:** an older or heat-damaged device may give somewhat less drug. In anaphylaxis a
weaker first dose can mean the reaction is not stopped and a second dose is needed sooner.
A liquid that has turned brown, pink or cloudy has broken down and may do little.

**Not using it:** anaphylaxis treated with no epinephrine can kill within minutes to hours
(CDC, Recognizing and Responding to Anaphylaxis). Waiting to find an in-date pen is the
failure that kills.

**Other medicines:** an expired liquid (children's syrups, mixed antibiotic suspensions, eye
drops) may have lost strength or grown germs. Some drugs where small strength losses matter
(heart, seizure, thyroid, transplant medicines) can fail quietly. Insulin and frozen
medicines follow their own rules (→ 30-09, → 30-01).

## 4. What makes it safer

**Removes the risk**
- **Never be in the position**: keep enough in-date supply, replaced before expiry, logged on
  the rotation tracker (→ 26-08), stored inside the label's temperature range.

**Reduces it a lot**
- **Look through the window first.** Use only epinephrine that is **clear and colourless**,
  with no flakes or crystals (FDA label's own check).
- **Keep devices on a person in the cold** (inside the coat, never in a car or pack) and out of
  hot cars in summer (→ 02-03).
- **Use the newest expired device first**; keep expired stock sorted by date.
- **Give the second dose sooner** if the first device was old and the person is not improving,
  following the written anaphylaxis plan (AAAAI, Anaphylaxis Emergency Action Plan).

**Reduces it a little**
- For tablets and capsules: use only intact ones stored cool and dry; discard anything
  crumbling, discoloured, sticky or smelling different.
- Do not use expired liquids, eye drops or anything that has changed in look or smell.
- Ask a pharmacist or clinician about each long-term medicine while you still can, and write
  their answer on → 12-07.

## 5. The options

**`discard`: Discard at the printed date.**
You give up: whatever strength the old medicine still had. You accept: that if in-date
supply runs out, there may be nothing to give.

**`use-if-clear`: Use if clear and colourless; keep seeking in-date stock.**
You give up: the label's guarantee. You accept: that an older device or tablet may be weaker,
and that you must watch more closely and be ready to give another dose. Discoloured or cloudy
epinephrine is a last resort only when nothing else exists.

## 6. Our choice

{{card DC-04}}

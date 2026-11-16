---
id: 30-09-dc08-heat-exposed-medication
section: 30-decisions-and-floors
title: "DC-08. Using insulin or other refrigerated medication after a heat excursion"
version: 2
revised: 2026-11-16
layer: card
danger_level: critical
phase: [A, B, C]
tags: [decision card, insulin, refrigerated medication, heat, cold chain, diabetes, potency]
derived_from: [02-02-insulin-without-the-grid, 02-05-sourcing-insulin-supplies, 02-10-evaporative-cooling-pouches]
sources:
  - us-fda-information-regarding-insulin-storage-and-swi-6448d3
  - american-diabetes-association-insulin-storage-and-sy-6f1f94
  - american-diabetes-association-switching-between-insu-9c5595
  - cochrane-human-insulin-less-temperature-sensitive-th-28a2b9
  - cdc-diabetic-ketoacidosis-55a7c2
  - american-diabetes-association-dka-ketoacidosis-and-k-f0301a
related: [02-01-cl01-type-1-diabetes-injections, 02-02-cl02-type-1-diabetes-pump-and-cgm, 02-06-cl06-type-2-diabetes-on-insulin, 12-21-evaporative-cooling-pouches, 09-10-power-for-medical, 29-07-ex07-refrigerated-medicines, 30-05-dc04-expired-medication, 30-01-the-floors]
cards: [DC-08, DC-04]
explainers: [EX-07, EX-14]
promote_when: [has.refrigerated_meds, has.condition.CL-01]
card: DC-08
options:
  - id: discard-after-window
    label: "Follow the published window exactly"
    summary: "Insulin out of the fridge is used only inside the published room-temperature window (FDA emergency guidance: 59 to 86 °F for up to 28 days) or the product label; after that, or after heat above it, it is replaced."
  - id: use-and-watch
    label: "Use beyond the window if nothing else; watch closely"
    summary: "If no properly stored supply exists, heat-exposed or out-of-window insulin is used rather than none, with more frequent glucose checks and ketone checks, expecting it may work less well. Replaced as soon as possible."
settings_summary: "Insulin and some other medicines are stored in the fridge. Without power, FDA's emergency guidance says insulin can be kept at 59 to 86 °F for up to 28 days. Above that, or for longer, it slowly loses strength, and you cannot see the loss. Weaker insulin means higher blood sugar and, for type 1 diabetes, a risk of diabetic ketoacidosis (DKA), which can kill. But no insulin at all causes DKA for certain. FDA says that in an emergency you may still need to use insulin stored above 86 °F until proper supply returns. What helps most: keep it in the band with a powered fridge or cooler and a thermometer (removes it); evaporative pouches, cool spots, rotation (reduces it a lot). Frozen insulin is never used (floor)."
review_pass: { date: "2026-11-16", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "ADA claims corrected (switching sheet vs storage page); Cochrane figures quoted; DKA wording to CDC/ADA; unsourced 'within days' removed." }
---

# DC-08. Using insulin or other refrigerated medication after a heat excursion

**What this page is for.** Insulin and some other medicines need to stay cool. In a long
outage, or a summer move, they may get warmer than the label allows. This card is about
whether to use warmed medicine when nothing better exists. It is not a dosing guide.

> **SAFETY.** A frozen-then-thawed insulin vial or pen is discarded (floor, → 30-01). That is
> not a choice on this card. Insulin that should be clear but is cloudy, coloured or clumped is
> not used.

## 1. The thing, in plain words

**Cold chain** means keeping a medicine inside its temperature band from the factory to the
dose (→ 29-07). **Insulin** is a protein hormone people with type 1 diabetes, and some with
type 2, must inject to live. Unopened insulin is stored in a fridge. A **heat excursion** is
any time it gets warmer than its label allows: a hot car, a summer room with no air
conditioning, a bag in the sun.

Heat damage and freeze damage are different. **Freezing is a cliff**: the insulin is ruined
and it is a floor. **Heat is a slope**: strength drops gradually, faster the hotter it gets.

Your household's medicine rows: {{#each meds as m}}{{m.member}}, {{m.name}} {{m.strength}} (refrigerated: {{m.refrigerated}}); {{else}}none entered.{{/each}}

## 2. The rule, and why it was set

- FDA's emergency guidance: insulin, opened or unopened, may be left unrefrigerated between
  **59 and 86 °F for up to 28 days** and still keep its strength. Keep it out of direct heat
  and sunlight. FDA adds that under emergency conditions **you might still need to use
  insulin that has been stored above 86 °F**, and should replace it when properly stored
  insulin is available (FDA, Information Regarding Insulin Storage and Switching Between
  Products in an Emergency).
- The American Diabetes Association's disaster guidance gives the same band for opened vials
  and pens (59 to 86 °F for up to 28 days) and says that under emergency conditions insulin
  stored above 86 °F may be used if necessary, then discarded once properly stored insulin is
  available (ADA, Switching Between Insulin Products in Disaster Response Situations). Its
  everyday storage page says insulin kept at room temperature lasts about one month (ADA,
  Insulin Storage and Syringe Safety).
- Each product's label gives its own in-use days. Some are shorter than 28.

**Why:** makers test strength at set temperatures for set times. Outside those, they cannot
promise the dose on the label is the dose you get, so the label says discard.

**What the evidence adds:** a Cochrane review (Richter and others) found that unopened vials
and cartridges of specific types of human insulin could be stored at up to 25 °C (77 °F) for at
most 6 months, and up to 37 °C (99 °F) for at most 2 months, without a clinically relevant loss
of activity; its authors list mixed insulins, pumps and opened vials as needing more research
(Cochrane, Human insulin less temperature-sensitive than previously thought). This is planning
context, not permission to store warm.

## 3. How it actually hurts people

**Using it:** weaker insulin brings blood sugar down less. Blood sugar runs high. In type 1
diabetes, not enough insulin lets acids called ketones build up: **diabetic ketoacidosis
(DKA)**, with nausea and vomiting, rapid deep breathing and confusion (CDC, Diabetic
Ketoacidosis; ADA, DKA and Ketones). ADA calls it a medical emergency that can become
life-threatening if it is not treated. The danger is that nobody knows how much strength is gone, so a "normal"
dose quietly underperforms.

**Not using it:** DKA develops when the body lacks insulin, and ADA says it can develop
quickly, often during illness or missed insulin (ADA, DKA and Ketones). With no insulin at all,
a person with type 1 diabetes will go into DKA. Throwing away warmed insulin with nothing to replace it is the
error that kills fastest.

**Other refrigerated medicines** (some injected arthritis, bowel and skin drugs, some
antibiotic suspensions, some eye drops) each have their own label. Ask your pharmacist now what
each one does when warm, and write the answer on its condition page.

## 4. What makes it safer

**Removes the risk**
- **Keep it in the band.** A small 12-volt fridge on a power station or solar (→ 09-10), with
  a **thermometer inside**, set and checked so it can never freeze. In winter a cooler buffered
  against outdoor cold, never directly on ice (→ 02-01).

**Reduces it a lot**
- **Evaporative cooling pouches** in warm months, which keep insulin below air temperature
  without power (→ 12-21).
- The coolest stable spot available: a basement, an interior closet, a buried cooler, checked
  with a min/max thermometer.
- **Rotate**: use the oldest in-band vial first; keep the unopened stock in the best storage.
- Know your product's in-use days from the label (→ 29-14) and write the date each vial or pen
  left the fridge on it.

**Reduces it a little**
- **Check glucose more often** and check ketones when glucose runs high, following the plan in
  the condition module (→ 02-01, → 02-02).
- Keep a log of temperatures so you know how bad the excursion was.

## 5. The options

**`discard-after-window`: Follow the published window exactly.**
You give up: insulin that might still have worked. You accept: running out sooner if
replacement is not available.

**`use-and-watch`: Use beyond the window if nothing else; watch closely.**
You give up: the label's guarantee of strength. You accept: that the dose may do less than
expected, so glucose and ketones must be checked more often, and the insulin is replaced as
soon as anything properly stored can be found. This is what FDA's emergency statement
describes when no alternative exists.

## 6. Our choice

{{card DC-08}}

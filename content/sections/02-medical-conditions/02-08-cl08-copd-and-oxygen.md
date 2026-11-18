---
id: 02-08-cl08-copd-and-oxygen
section: 02-medical-conditions
title: "CL-08. COPD and oxygen dependence"
version: 3
revised: 2026-11-18
layer: condition
danger_level: critical
phase: [A, B, C]
tags: [condition library, COPD, emphysema, chronic bronchitis, oxygen, concentrator, cylinders, fire risk, power, flare-up, inhalers]
derived_from: [12-11-chronic-conditions, 09-06-charging-medical-devices, 09-10-power-for-medical, 27-03-protecting-electronics]
sources:
  - nhlbi-copd
  - usfa-oxygen-tank-safety-r10
  - american-lung-association-using-oxygen-safely-r10
  - epa-wildfire-smoke-guide
  - cdc-carbon-monoxide-poisoning-basics-772153
  - american-red-cross-power-outage-safety-6d07a8
related:
  - 02-07-cl07-asthma
  - 02-24-cl24-sleep-apnea-cpap
  - 12-11-chronic-conditions
  - 12-04-infection-and-antibiotics
  - 09-06-charging-medical-devices
  - 09-10-power-for-medical
  - 09-04-generators
  - 28-01-power-stations
  - 28-07-reading-your-own-gear
  - 27-03-protecting-electronics
  - 12-03-burns
  - 22-06-kit-medical
  - 01-07-evacuating-with-medical-needs
  - 29-02-ex02-batteries-and-power-stations
  - 29-12-ex12-extinguishers-blankets-and-alarms
  - 30-01-the-floors
  - 30-21-dc20-open-flame-indoors
  - 30-02-dc01-unvented-heater-overnight
  - 30-03-dc02-propane-cylinder-indoors
cards: [DC-20, DC-01, DC-02, DC-04, DC-15, DC-16, DC-19]
explainers: [EX-02, EX-03, EX-12]
promote_when: [has.condition.CL-08, has.oxygen]
photo_slots:
  - { id: oxygen-setup, caption: "Our oxygen setup: concentrator, cylinders secured upright, the no-flame zone marked, the power source" }
figures: [fig-oxygen-no-flame-zone]
plates: []
condition: CL-08
gear: null
explainer: null
card: null
review_pass: { date: "2026-11-18", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "5-ft oxygen rule re-cited to USFA and ALA (NFPA sheet unreadable); NHLBI COPD 911 list verbatim; fire rules per ALA; meds_for tables. K1 (G34): 'When there is no prescriber' added: keep the prescribed oxygen flow (ALA), no published way to stretch oxygen said plainly, inhaler label for flare-ups." }
---

# CL-08. COPD and oxygen dependence

**What this page is for.** COPD (chronic obstructive pulmonary disease) is long-term lung damage
that makes every breath work harder. Many people with it manage on inhalers; some need extra
oxygen all day or at night. Oxygen is the hardest supply in this binder after insulin: a
concentrator needs electricity every hour it runs, cylinders run empty, and oxygen makes fire
far more dangerous in a house lit and heated by flame. This module covers the flare-up response,
the oxygen clock, fire safety, power, and the questions for the prescriber and the oxygen
supplier now.

{{#if has.condition.CL-08}}**Someone in your household has this condition.** This module is at the front of the medical section for you.{{else}}**Nobody in your household is marked with this condition.** The module stays in the binder so you can help someone else, or add the condition later in settings.{{/if}}
{{#if has.oxygen}}**Someone in your household uses oxygen.** Read part 3 (fire) and part 9 (power) today.{{/if}}

> **SAFETY**
> - **Oxygen makes things burn more readily.** No smoking, no candles, no open flame and no
>   stove near oxygen. The US Fire Administration says keep oxygen tanks at least **5 feet**
>   from a heat source, open flames or electrical devices (USFA, Oxygen Tank Safety); the
>   American Lung Association gives the same 5 feet.
> - **Never run a generator, charcoal, or any engine indoors, in a garage, or near an open
>   window.** Carbon monoxide kills in minutes with no warning; alarms fail; there is no
>   mitigation that works every time (floor, → 30-01).
> - **Do not turn the oxygen flow up or down on your own.** The American Lung Association says
>   never change the flow rate from what the doctor prescribed (ALA, Using Oxygen Safely). The
>   flow is the prescriber's, written in part 7.

## Do this now: a bad breathing spell

1. **Sit them upright**, leaning forward with arms resting on a table or knees. Loosen clothes.
2. **Rescue inhaler** (quick-relief) as their written plan says, or with no plan, as the
   inhaler's own label says (→ 02-07 part 7).
3. **Oxygen at the prescribed flow**, if they use it. Check the tubing is not kinked, the
   cylinder is not empty, and the concentrator is running.
4. **Slow breathing out:** in through the nose, out slowly through pursed lips, as if blowing
   on soup. Stay calm with them.
5. **Danger signs** (part 5): cannot catch their breath or talk, blue or grey lips, not alert,
   a very fast heartbeat, or the treatment is not working:
   **follow the prescriber's plan, if there is one, and seek any care that exists.**

## 1. What it is

COPD is a group of lung diseases, mainly emphysema and chronic bronchitis, that block airflow and
make breathing hard. It gets worse over years, and "flare-ups" (sudden worsening, often with a
chest infection) can be serious enough to need hospital care (NHLBI, COPD). Some people need
**oxygen therapy**: extra oxygen through tubes resting in the nose or a face mask (NHLBI, COPD),
from a concentrator, a metal tank (cylinder) or a liquid-oxygen unit (ALA, Using Oxygen Safely).

## 2. What runs out, and how fast

| What | Clock | When it is gone |
|---|---|---|
| **Oxygen from a concentrator** | Only as long as there is power. Write its watts from the label: ________ W. | Back to cylinders, then none. |
| **Oxygen cylinders** | Hours, depending on size and flow. Get the supplier's chart for your cylinders at your flow and copy it here: ________ | The person is without oxygen. |
| **Liquid oxygen** | Slowly evaporates even when not in use; ask the supplier how fast. | As above. |
| Portable concentrator batteries | Hours per charge, from the label. | Plug in, or switch source. |
| Rescue and daily inhalers | Dose counters. | Flare-ups become more frequent and worse. |
| Tubing, nose pieces, filters, humidifier bottles | Count them. | Infection, poor flow. |
| Steroid tablets or antibiotics for flares (if prescribed) | Count them. | Flares last longer. |

**Write the oxygen clock:** cylinders ________ × hours each at the prescribed flow ________ =
**________ hours** without power. Concentrator hours on the household's stored power: ________
(→ 09-10). Copy both to → 23-02.

## 3. Storing oxygen and medicines safely

**Fire is the oxygen hazard.** Oxygen does not burn by itself, but it supports burning:
materials burn more readily where there is extra oxygen (ALA, Using Oxygen Safely). The rules,
in plain words (USFA, Oxygen Tank Safety; ALA, Using Oxygen Safely):
- **No smoking** near the person, by anyone; "No Smoking" and "No Open Flames" signs in and
  outside the home.
- **At least 5 feet** between the oxygen and any heat source, open flame or electrical device.
- **Never a candle, match, lighter or other open flame near medical oxygen.** No oxygen while
  cooking with gas. Oil lamps and wood stoves are open flame too.
- **No aerosol sprays, vapour rubs, petroleum jelly or oil-based lotions**; never oil the
  equipment or handle it with greasy hands. Use water-based products.
- **Turn the oxygen off when not in use**, and do not lay a running nose tube or mask on the bed
  or a chair.

**In a house lit and heated by flame, this changes the plan.** Put the oxygen user in a room
with **no** flame, or move the flame. Your household's choices on indoor flame and heaters are
cards: {{choice DC-20}} (→ 30-21), {{choice DC-01}} (→ 30-02), {{choice DC-02}} (→ 30-03).
Whatever those say, oxygen and flame stay apart. Keep an extinguisher in reach (→ 29-12) and
know the burn page (→ 12-03).

{{figure fig-oxygen-no-flame-zone}}

**Cylinders and units:** secure tanks so they cannot fall; keep a liquid-oxygen unit upright at
all times; never store oxygen in an enclosed space like a closet or a car trunk (ALA, Using
Oxygen Safely). Keep concentrators a few inches from walls and curtains, with nothing on top. Inhalers: room temperature, away from heat and
flame (→ 02-07).

{{photo oxygen-setup}}

## 4. Day by day without it

- **Without daily inhalers:** more breathlessness and cough over days to weeks; flare-ups more
  likely.
- **Without prescribed oxygen:** depends on how much the person needs. Someone on oxygen only at
  night or with exertion may manage short gaps by resting and limiting effort; someone on
  continuous oxygen may become confused, drowsy and gravely ill within hours to days. **Ask the
  prescriber now which describes this person** (part 7).
- **What helps:** rest, pacing every task, sitting upright, slow pursed-lip breathing, staying
  warm, avoiding smoke and dust, treating chest infections early, and plenty of fluids so mucus
  stays thin.

## 5. Warning signs that mean an emergency

NHLBI says to call 911 during a flare-up if (NHLBI, COPD):
- the person is having a hard time catching their breath or talking;
- **lips or fingernails have turned blue or grey**, a sign of a low oxygen level in the blood;
- people around them notice they are **not mentally alert**;
- the heartbeat is **very fast**;
- the recommended treatment for the symptoms is not working.

Also watch for fever and yellow or green phlegm, signs of a chest infection that can start a
flare-up (NHLBI, COPD; → 12-04). New confusion or drowsiness can also be carbon monoxide if any
fuel is burning indoors (→ 29-03). With no 911, these are the signs to seek any care that
exists.

## 6. Sick-day basics

- **Chest infections are the usual cause of a bad flare-up.** Handwashing, keeping away from
  sick people, and vaccines while they exist are the prevention.
- **Act early**: the prescriber's flare-up plan (part 7) is for the first day of worse symptoms,
  not the third.
- **Fluids, rest, sitting up.** Watch for the danger signs above.

## 7. What to stock, and how much

**Ask your prescriber now, while you can, and write it here:**
- The oxygen flow at rest ________, with exertion ________, at night ________.
- What to do if the oxygen runs short or stops: ________________________________________
  ______________________________________________________________________________________
- The flare-up plan (inhalers, steroid tablets, antibiotics, when to start): ______________
  ______________________________________________________________________________________
- Danger signs specific to this person: ______________________________________________
Prescriber: ____________________ Date: __________

**When there is no prescriber.** The published rule on oxygen is the American Lung
Association's: never change the flow rate from what the doctor prescribed (ALA, Using Oxygen
Safely). The prescribed flow is on the oxygen order, the concentrator settings or the supplier's
paperwork; copy it into the line above now. No source we read tells a patient how to make
oxygen last longer by lowering the flow, so the binder does not: keep the prescribed flow,
stretch the supply by power and resupply instead (part 9, part 8), and as it runs low move
toward care early, before it is gone (part 5). For a flare-up, the rescue inhaler's label is
the published instruction (→ 02-07 part 7). No source we read gives a patient a way to start
steroid tablets or antibiotics alone; antibiotics without a prescription are a card:
{{choice DC-16}} (→ 30-17).

**Ask the oxygen supplier now:** their emergency plan; how many backup cylinders they will
supply; the cylinder duration chart at the prescribed flow; whether a battery-powered portable
concentrator is possible. Supplier name and number: ________________________ (→ 25-09).

**Stock arithmetic.** The medicines tagged for this condition in settings are printed; if none are tagged, every household medicine row is, so use the ones for this condition.

| Medicine or supply | On hand | Used per day | Days on hand | Days you want | Still to get |
|---|---|---|---|---|---|
{{#each meds_for.CL-08 as m}}
| {{m.name}} {{m.strength}} ({{m.member}}) | ____ | ____ | ____ | ____ | ____ |
{{else}}
{{#each meds as m}}
| {{m.name}} {{m.strength}} ({{m.member}}) | ____ | ____ | ____ | ____ | ____ |
{{/each}}
{{/each}}
| Oxygen cylinders (full) | ____ | ____ | ____ | ____ | ____ |
| Tubing, nose pieces, filters | ____ | ____ | ____ | ____ | ____ |
| Spare concentrator batteries and charger | ____ | | | ____ | ____ |
| No-smoking sign, extinguisher by the oxygen | ____ | | | ____ | ____ |
| Pulse oximeter (finger clip that reads oxygen level) and batteries | ____ | | | ____ | ____ |

> **Before the collapse:** the American Red Cross advises anyone who relies on powered medical
> equipment to make a power-outage plan with their health care provider (American Red Cross,
> Power Outage Safety). Tell the electric utility too; many keep a list of such customers. Ask the supplier for
> backup cylinders. Keep vaccinations up to date while they are offered. Ask about pulmonary
> rehabilitation: the breathing and pacing skills it teaches need no supplies.

## 8. Sourcing when the pharmacy is closed

- **The oxygen supplier, hospitals and disaster shelters** are the realistic sources while they
  run; some shelters can plug in a concentrator.
- **Welding and industrial oxygen** is a different product with different purity rules and
  fittings; this binder does not cover substituting it. Ask the prescriber or supplier now if it
  worries you, and write the answer: ________________________________
- **Inhalers from other households:** {{choice DC-15}} (→ 30-16). Expired ones: {{choice DC-04}}
  (→ 30-05).

## 9. Power and devices

- **A concentrator is a continuous load.** Read its watts on the label (→ 28-07), multiply by
  the hours a day it runs, and compare with the household's stored and generated power
  (→ 09-10, → 29-02). That number decides how long the concentrator runs without the grid.
- **Generators run outdoors only** (floor above). Run cords to the concentrator; never backfeed
  the house (→ 09-04).
- **Power stations and solar** can run a concentrator for a time; size them on → 28-01 and
  → 09-10.
- **Heat and cold:** concentrators and batteries have operating ranges on their labels.
- **EMP and geomagnetic storms** may damage a concentrator; cylinders and a manual regulator
  need no electronics (→ 27-03).
- Write the clocks: concentrator on station ________ hours; portable battery ________ hours;
  cylinders ________ hours.

## 10. Travel and evacuation

- **Oxygen sets the range of any move.** Count cylinder hours against travel hours, with a
  margin, before leaving (→ 01-07). Secure cylinders upright in the vehicle; never leave them in
  a closed, hot car.
- A portable concentrator needs vehicle power or charged batteries for the whole trip.
- Cold air and exertion make breathing harder: scarf over the mouth, short legs, rest often.
- **Head toward oxygen**: a hospital or a shelter with power.

## 11. Decision cards that apply

- **Indoor open flame:** {{choice DC-20}} (→ 30-21). Never near oxygen.
- **Unvented heater overnight:** {{choice DC-01}} (→ 30-02).
- **Propane cylinder indoors:** {{choice DC-02}} (→ 30-03).
- **Expired medicine:** {{choice DC-04}} (→ 30-05).
- **Someone else's prescription:** {{choice DC-15}} (→ 30-16).
- **When to leave:** {{choice DC-19}} (→ 30-20). The oxygen clock is usually the trigger.

## 12. My meds

Medicines your household tagged for this condition in settings are printed below. **If none
are tagged, every medicine row your household entered is printed instead: tick the rows for
this condition** and cross out the rest. Fill any blank columns by hand from the boxes
and bottles, and add untagged medicines in the empty rows.

| For this? | Who | Medicine | Strength | Schedule | Fridge? | If doses are missed (prescriber's words) | Where kept | Days on hand | Expires |
|---|---|---|---|---|---|---|---|---|---|
{{#each meds_for.CL-08 as m}}
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

**Oxygen equipment:** concentrator model ______________ watts ______ cylinder size ______
supplier ______________ phone ______________

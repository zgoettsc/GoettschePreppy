---
id: 02-24-cl24-sleep-apnea-cpap
section: 02-medical-conditions
title: "CL-24. Sleep apnoea (CPAP)"
version: 1
revised: 2026-11-16
layer: condition
danger_level: caution
phase: [A, B, C]
tags: [condition library, sleep apnea, sleep apnoea, CPAP, power budget, humidifier, distilled water, drowsy driving, battery, DC adapter]
derived_from: [09-06-charging-medical-devices, 12-11-chronic-conditions]
sources:
  - nhlbi-sleep-apnea
  - nhlbi-cpap
  - cdc-about-sleep-1bf86b
  - cdc-carbon-monoxide-poisoning-basics-772153
  - american-red-cross-power-outage-safety-6d07a8
related:
  - 12-11-chronic-conditions
  - 09-01-power-priorities
  - 09-03-batteries-and-storage
  - 09-04-generators
  - 09-06-charging-medical-devices
  - 09-10-power-for-medical
  - 09-16-outage-day-one
  - 27-03-protecting-electronics
  - 28-01-power-stations
  - 28-07-reading-your-own-gear
  - 21-07-sleep
  - 13-02-hygiene-and-handwashing
  - 02-08-cl08-copd-and-oxygen
  - 02-26-cl26-severe-obesity-and-bariatric-surgery
  - 02-16-cl16-mental-health-medications
  - 02-17-cl17-opioid-dependence-and-chronic-pain
  - 22-06-kit-medical
  - 01-07-evacuating-with-medical-needs
  - 23-02-master-consumables-table
  - 25-09-family-medical-summary
  - 29-02-ex02-batteries-and-power-stations
  - 30-01-the-floors
  - 30-16-dc15-someone-elses-prescription
cards: [DC-15]
explainers: [EX-02, EX-03]
promote_when: [has.condition.CL-24, has.cpap]
photo_slots:
  - { id: cpap-power-label, caption: "The CPAP power supply label (volts, amps or watts) and the DC cable, if you have one" }
figures: []
plates: []
condition: CL-24
gear: null
explainer: null
card: null
review_pass: null
---

# CL-24. Sleep apnoea (CPAP)

**What this page is for.** In obstructive sleep apnoea the airway closes again and again during
sleep. A **CPAP** machine (continuous positive airway pressure) blows air through a mask to hold
it open. CPAP needs power every night. **For most people a few nights without it are not an
emergency**, but weeks without it bring dangerous daytime sleepiness at exactly the time when
people are driving, using tools, keeping watch and making hard decisions. This module covers the
power budget, running the machine off-grid, what happens without it, and what else helps.

{{#if has.condition.CL-24}}**Someone in your household has this condition.** This module is at the front of the medical section for you.{{else}}{{#if has.cpap}}**Someone in your household uses CPAP.** This module applies to them.{{else}}**Nobody in your household is marked with this condition.** The module stays in the binder so you can help someone else, or add the condition later in settings.{{/if}}{{/if}}

> **SAFETY**
> - **Never run a generator, charcoal, or any engine indoors, in a garage, or near an open
>   window.** Carbon monoxide kills in minutes with no warning; a generator running at night for
>   a CPAP, while everyone sleeps, is the classic case (floor, → 30-01; CDC, Carbon Monoxide
>   Poisoning: Basics).
> - **Do not drive or run dangerous tools while very sleepy.** Drowsy driving kills (part 5).
> - **Alcohol and sleeping pills make apnoea worse** (NHLBI, Sleep Apnea).

## Do this now

**Power is out tonight:**
1. **Run the CPAP from a battery or power station, humidifier off** (part 9). The heated
   humidifier is usually the biggest power user; the manual says how much.
2. **No power at all:** sleep on the side, head and chest raised on pillows, no alcohol or
   sedatives (part 4).
3. **Generator:** outdoors only, at least 20 feet from windows and doors, exhaust pointed away,
   CO alarms inside (CDC; → 09-04).
4. **Next day:** no driving if sleepy; nap when you can.

## 1. What it is

**Obstructive sleep apnoea** means the throat relaxes and closes during sleep, stopping breathing
for seconds at a time, many times an hour. The person wakes briefly each time, often without
knowing it, so sleep is broken and oxygen drops (NHLBI, Sleep Apnea). Loud snoring, gasping and
daytime sleepiness are common signs. Over years it strains the heart and raises blood pressure.
**CPAP** keeps the airway open with gentle air pressure (NHLBI, CPAP). Some people use a mouth
device or have had surgery instead; they need no power.

## 2. What runs out, and how fast

| What | Clock | When it is gone |
|---|---|---|
| Power for the CPAP | Every night. Battery hours depend on the machine and the settings (part 9). | Sleep without CPAP (part 4). |
| Distilled water for the humidifier | Nights per jug. | Run with the humidifier off. |
| Masks, cushions, tubing, filters | Cushions and filters wear out over weeks to months. | Leaks, sore skin, dirty air. |
| The person's alertness | A few bad nights. | Dangerous daytime sleepiness. |

## 3. Storing the device without power

- **Machine:** dry, clean, out of heat and freezing. If it has been very cold, let it warm to room
  temperature before use so condensation does not form inside.
- **Spare mask, cushions, tubing and filters** sealed, out of sun.
- **Water tank:** empty it daily and let it dry; stale water grows germs.

## 4. Day by day without it

What public sources describe: without treatment, breathing pauses return, sleep is broken, and
daytime sleepiness builds. NHLBI lists daytime sleepiness, trouble concentrating, morning
headaches and irritability, and warns that untreated sleep apnoea raises the risk of accidents
(NHLBI, Sleep Apnea). **One night** is usually just a bad night. **Several nights to weeks:** the
sleepiness and poor judgement become a real hazard. Over months: blood pressure and heart strain
(→ 02-09).

**What helps without CPAP** (NHLBI, Sleep Apnea; CDC, About Sleep):
- **Sleep on the side,** not the back; a rolled towel or a backpack worn in bed stops rolling over.
- **Raise the head and chest** with pillows or blocks under the head of the bed.
- **No alcohol and no sedating medicines** at night unless the prescriber has said they are
  safe; they relax the throat further. If the person takes opioids or sedating mental-health
  medicines, see → 02-17 and → 02-16.
- **A regular sleep time,** a dark, quiet, cool room, and naps by day if possible (→ 21-07).
- **Weight loss** helps many people over months (→ 02-26).

## 5. Warning signs that mean an emergency

- **Falling asleep while driving, working with tools, cooking on a fire or on watch.** Stop the
  task; someone else takes over.
- **Gasping, choking awake, or blue lips at night** that do not settle with position change.
- **Morning confusion or severe headache,** especially with heart or lung disease: possible low
  oxygen or high carbon dioxide; get care. Someone on oxygen too: → 02-08.
- **Headache, dizziness or nausea in several people** in a house with a generator or heater:
  carbon monoxide (→ 29-03). Get everyone into fresh air.

## 6. Sick-day basics

- **A cold or blocked nose** makes the mask hard to use; a full-face mask or saline rinse can help.
  Ask the prescriber now.
- **Sedating cold medicines** worsen apnoea; check the label.
- **Clean the mask and tubing** more often when sick, with mild soap and water, and let them dry
  completely (→ 13-02).

## 7. What to stock, and how much

**Ask the sleep doctor or equipment supplier now, while you can, and write it here:**
- The machine's make, model and pressure setting: ______________________________________
- Does it have a DC (12-volt) cable or a battery made for it? ______________________________
- The power it draws with and without the humidifier, from the label or manual: ___________
- Can it run safely from a power station or inverter? ____________________________________
- If CPAP is impossible for weeks, what else should we do? ________________________________
Doctor or supplier: ____________________ Date: __________

{{photo cpap-power-label}}

**Night budget.** Nights on battery = battery watt-hours available ÷ watt-hours the machine uses
per night. The power station's watt-hours are on its label and on → 28-01; your household total
is {{ gear.station_wh_total }} Wh. The machine's use per night comes from its manual or a plug-in
meter test, not from this page.

| Supply | On hand | Used per night or month | Nights on hand | Nights you want | Still to get |
|---|---|---|---|---|---|
| Battery or power station watt-hours for CPAP | ____ | ____ | ____ | ____ | ____ |
| Distilled water | ____ | ____ | ____ | ____ | ____ |
| Mask cushions | ____ | ____ | ____ | ____ | ____ |
| Filters | ____ | ____ | ____ | ____ | ____ |
| Tubing, spare mask, headgear | ____ | | | ____ | ____ |
| DC cable or approved battery | ____ | | | ____ | ____ |
| Wedge pillow or blocks for raising the bed | ____ | | | ____ | ____ |
{{#each meds as m}}| {{m.name}} {{m.strength}} ({{m.member}}) | ____ | ____ | ____ | ____ | ____ |
{{/each}}

> **Before the collapse:** run the CPAP for one night on your power station and write down how
> much charge it used, with and without the humidifier. That one test is worth more than any
> table. Ask the supplier about the maker's DC cable. Tell your electric company you use a
> medical device ({{ contacts.utility.electric.provider }}, {{ contacts.utility.electric.phone }}).
> Keep the prescription and settings on → 25-09.

## 8. Sourcing when the pharmacy is closed

- **Medical equipment suppliers and pharmacies** while they run; masks and tubing are standard
  sizes within each system.
- **Another person's CPAP** can be borrowed only if it is cleaned well and its pressure is right
  for this person; pressure settings are prescribed. That is the same trade-off as someone else's
  prescription: {{choice DC-15}} (→ 30-16).
- **Distilled water** can be replaced by running the humidifier dry (off). Do not use tap or
  untreated water in the tank; it leaves minerals and can grow germs.

## 9. Power and devices

- **CPAP is a medical load on the household power plan** (→ 09-01, → 09-06, → 09-10). Put it on
  the list with its nightly watt-hours.
- **Humidifier off** reduces power use the most; the heated tube too, if fitted.
- **A DC cable from the maker** runs the machine straight from a 12-volt source without the
  losses of an inverter (→ 29-02). Use only the maker's cable or one the supplier approves.
- **Power stations:** charge by day from solar, car or generator; run the CPAP at night
  (→ 28-01). Read your own machine's label (→ 28-07).
- **Car battery:** possible with the right DC cable, but a car battery run flat may not start
  the car. Keep the engine off while sleeping; never run it in a garage (floor).
- **EMP and storms:** a spare power supply in a metal box (→ 27-03).

## 10. Travel and evacuation

- The machine, mask, tubing, power supply and DC cable go with the person (→ 01-07, → 22-06).
  Shelters may have power outlets; ask for a spot near one (American Red Cross, Power Outage
  Safety).
- On the road: side-sleeping and a raised head if the CPAP cannot run.
- **Driver rota:** the person with untreated apnoea drives short legs only, and never while sleepy.

## 11. Decision cards that apply

- **Someone else's prescription or equipment:** {{choice DC-15}} (→ 30-16).

## 12. My meds

Every medicine row your household entered is printed, because the binder cannot pick out one
condition's rows. **Tick the rows for this condition**, cross out the rest, and fill any blank
columns by hand. Write the CPAP settings in part 7.

| For this? | Who | Medicine | Strength | Schedule | Fridge? | If doses are missed (prescriber's words) | Where kept | Days on hand | Expires |
|---|---|---|---|---|---|---|---|---|---|
{{#each meds as m}}| ☐ | {{m.member}} | {{m.name}} | {{m.strength}} | {{m.schedule}} | {{m.refrigerated}} | {{m.if_missed}} | {{m.where_kept}} | {{m.days_on_hand}} | {{m.expiry}} |
{{else}}| ☐ | (no medicines entered yet) | | | | | | ____ | ____ | ____ |
{{/each}}| ☐ | ____ | ____ | ____ | ____ | ____ | ____ | ____ | ____ | ____ |
| ☐ | ____ | ____ | ____ | ____ | ____ | ____ | ____ | ____ | ____ |
| ☐ | ____ | ____ | ____ | ____ | ____ | ____ | ____ | ____ | ____ |

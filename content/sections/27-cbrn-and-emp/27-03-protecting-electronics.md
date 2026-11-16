---
id: 27-03-protecting-electronics
section: 27-cbrn-and-emp
title: "Protecting electronics, and the medical devices"
version: 1
revised: 2026-11-16
layer: core
danger_level: critical
phase: [A, B, C]
tags: [EMP, electronics, shielding, Faraday, medical devices, insulin pump, CGM, CPAP, oxygen, backups, redundancy]
derived_from: [27-03-protecting-electronics]
sources:
  - us-fda-information-regarding-insulin-storage-and-swi-6448d3
  - cdc-diabetic-ketoacidosis-55a7c2
  - noaa-space-weather-prediction-center-noaa-space-weat-038109
  - cdc-managing-sick-days-18c7c8
related: [27-01-how-to-think-about-this, 27-02-emp-and-geomagnetic-storm, 02-01-cl01-type-1-diabetes-injections, 02-02-cl02-type-1-diabetes-pump-and-cgm, 02-08-cl08-copd-and-oxygen, 02-24-cl24-sleep-apnea-cpap, 02-23-cl23-hearing-and-vision-aids, 09-10-power-for-medical, 09-06-charging-medical-devices, 22-06-kit-medical, 26-08-expiry-and-rotation-tracker, 24-01-skills-checklist, 29-07-ex07-refrigerated-medicines, 30-01-the-floors]
cards: [DC-08]
explainers: [EX-02, EX-07]
promote_when: [has.condition.CL-02, has.oxygen, has.cpap, has.refrigerated_meds]
photo_slots:
  - { id: shielded-spares, caption: "Our shielded spares container: where it is and what is inside" }
figures: [fig-shielded-container]
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: { date: "2026-11-16", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "No numbers; floor wording matches 30-01; claims are qualitative and hedged." }
---

# Protecting electronics, and the medical devices

**What this page is for.** Which of your household's electronics actually matter, what really
threatens them, and the cheap, honest hedge for spares. The answer that protects people is
**redundancy and a backup that needs no electricity**, not a box.

> **SAFETY: read this limit first.** **Nothing on this page will protect a device from an event
> nobody can describe in advance.** Home shielding is untested against any real threat, and anyone
> who tells you a container is "EMP-proof" is selling something. **What protects people is a
> backup that needs no power, practised in advance** (→ 24-01). **No dosing appears here**: every
> backup plan for a medicine or device comes from the person's own prescriber, written down now.
> **A frozen-then-thawed insulin vial or pen is discarded** (floor, → 30-01).

## Your household's devices

From your settings. Add anything missing by hand.

{{#if has.condition.CL-02}}- **Insulin pump, glucose sensor (CGM) and the phone or controller that runs them** (→ 02-02).
  Backup: **syringes or pens, a simple meter, strips, lancets, ketone strips**, and the
  prescriber's written plan for switching to injections.
{{/if}}{{#if has.diabetes}}- **Blood glucose meter** (→ 02-01, → 02-05, → 02-06). Backup: a second meter and strips, in date.
{{/if}}{{#if has.oxygen}}- **Oxygen concentrator** (→ 02-08). Backup: **oxygen cylinders with a regulator that needs no
  power**, a written plan from the supplier, and the supplier's emergency number on paper.
{{/if}}{{#if has.cpap}}- **CPAP machine** (→ 02-24). Backup: a battery made for it or a power station with a DC cable,
  and the clinician's advice now on what to do on nights without it.
{{/if}}{{#if has.refrigerated_meds}}- **The medicine fridge or cooler and its thermometer** (→ 29-07, → 12-21). Backup:
  evaporative cooling pouches and a non-electronic thermometer. Your refrigerated medicines:
  {{#each refrigerated_meds as r}}{{r.name}} ({{r.member}}); {{/each}}
{{/if}}{{#if has.condition.CL-23}}- **Hearing aids and their batteries or charger** (→ 02-23). Backup: spare disposable-battery
  aids or an older pair, spare batteries, and the glasses prescription on paper.
{{/if}}{{#if has.mobility_aid}}- **Power wheelchair or scooter, if used** (→ 02-22). Backup: a manual chair.
{{/if}}- Every household: **phones**, **a battery or hand-crank radio** (→ 15-01), **flashlights**.
- Other devices someone depends on: ______________________ backup: ______________________

## Do this now

1. **Practise the no-power backup for each device above**, with the prescriber's or supplier's
   written instructions (→ 24-01, → 24-02). It works for a dead battery, a failed part, a lost
   phone, a flood, and every scenario in this section.
2. {{#if has.diabetes}}**Keep a backup glucose meter, strips and lancets that need no network**, in date (→ 26-08).
   A meter is the backup for a sensor; a sensor is not the backup for anything.{{else}}**Keep the simple, non-electronic version of every medical tool** (a manual thermometer, a
   manual blood-pressure cuff if one is used), in date (→ 26-08).{{/if}}
3. {{#if has.condition.CL-02}}**Keep enough syringes or pens for the insulin you hold**, as prescribed (→ 02-01).{{else}}**Keep the supplies each backup needs**, as prescribed or as the supplier advises.{{/if}}
4. **Store backups apart from the daily devices.** Same house, different place. Most real losses
   are ordinary: a bag left in a hot car, a flooded basement, a dropped phone.
5. **If you want the shielded-container hedge, do it cheaply** (below), and never let it replace
   any of the above.

## The honest threat model

The question is never "will my devices survive an EMP?" It is:

> **What happens to the person who depends on this device if it, its controller and its power
> all stop working at once, and stay stopped?**

That question has a good answer, and it does not involve shielding: **the no-power backup.**
{{#if has.condition.CL-02}}For type 1 diabetes, insulin cannot simply stop: without it,
diabetic ketoacidosis (a dangerous build-up of acids in the blood) can develop (CDC, Diabetic
Ketoacidosis). So the plan has to be **continuity**, not protection.{{/if}}

**Every failure has the same answer**, which is why it is worth practising:

| What fails | Answer |
|---|---|
| Phone or controller dies, is lost or breaks | The device's own backup controls if it has any, then the no-power backup |
| Device supplies run out (pump sets, sensors, filters, tubing) | The no-power backup |
| Batteries and charging are gone | → 09-10, then the no-power backup |
| Devices damaged by any event | The no-power backup |
| **All of these at once** | **The no-power backup** |

## Where the real risk is (it is not exotic)

The likely ways a household loses its medical electronics, most likely first:
1. **Ordinary breakage or loss**: dropped, wet, left behind, stolen.
2. **Supplies run out** because resupply stopped (→ 12-07). This binder plans for it.
3. **A power cut long enough to drain everything** (→ 09-10).
4. **Heat or cold in a vehicle**: common, and it damages **medicines** too (FDA, Information
   Regarding Insulin Storage and Switching Between Products in an Emergency; → 29-07). Using
   medicine after a heat excursion is a decision card: {{choice DC-08}} → 30-09
5. **A wide-area electromagnetic event.** Last, and least (NOAA, Space Weather Scales; → 27-02).

**Preparing fully for 1 to 4 also covers 5.** Preparing for 5 alone covers nothing.

## The shielded container: what it can and cannot be

**What is reasonable to say:** a sealed, fully enclosing metal container, with the contents
insulated from the metal, will weaken some radiated fields. That is basic physics, and it costs
nothing with things you own. (A container like this is often called a **Faraday cage**.)

**What is not reasonable to say:** that it is "EMP-proof", that it is tested, or that it makes any
particular device survive any particular event. **None of that can be known at home**, and this
binder will not print it.

**So treat it as** a cheap hedge for **spare** equipment you are not using: never as protection
for devices in daily use, and never as a reason to hold fewer spares.

{{figure fig-shielded-container}}

```
[ ] A metal container that FULLY encloses: a metal trash can with a tight metal
    lid, an ammo can, a metal toolbox. Unbroken metal contact all round the lid
    matters more than thickness.
[ ] Contents INSULATED from the metal: a cardboard box, bubble wrap or foam inside.
[ ] Contents are SPARES ONLY, checked and rotated like anything else (26-08).
[ ] Nothing in it that expires unnoticed, and nothing you need daily.
[ ] Stored dry. Rust and damp are far likelier to ruin the contents than any pulse.
```

{{photo shielded-spares}}

### What is worth putting in it

Small spares whose loss would really hurt, and that you can afford to leave idle:
{{#if has.condition.CL-02}}- **Pump and sensor spares** you are not using: a spare controller or phone set up for the
  device, if your clinic and supplier provide one, with the settings printed on paper beside it
  (→ 02-02). Never all spares in one container or one room.
{{/if}}{{#if has.diabetes}}- **A backup glucose meter, strips and lancets** (in date, → 26-08).
{{/if}}{{#if has.cpap}}- **A spare CPAP power supply and DC cable**, if you have one.
{{/if}}{{#if has.condition.CL-23}}- **Spare hearing aids** and a charger.
{{/if}}- **A small power station or power bank, a folding solar panel and the cables**: a reserve
  power tier you never use day to day (→ 09-03). It comes out for its quarterly charge check
  (→ 24-03) and goes straight back.
- **A small 12-volt inverter** (the box that turns 12-volt battery power into household
  power, → 29-02) that can run from a vehicle's 12-volt socket.
- **A spare battery or hand-crank radio** (→ 15-01) and **a spare handheld radio** (→ 15-02).
- **A spare phone with this binder installed** (→ 00-10) and **a drive with copies of your
  documents** (→ 19-03).
- **A spare headlamp and spare batteries** (→ 10-01).

**Testing a shielding bag:** seal a phone inside and call it. If it rings, the bag leaks. That only
checks phone frequencies: **a bag that fails is certainly leaking; a bag that passes proves
little.** Each quarter, check the stored spares still hold a charge and still work with the
devices they back up (→ 24-03).

**What never goes in it: medicine.** Medicines need a temperature range, not shielding (FDA). A
sealed metal box in a garage or car is a way to destroy them (→ 29-07).

## Working units and the reserve: the honest trade-off

A power station kept plugged into the wall as a backup for a medicine fridge, a CPAP or an oxygen
concentrator is connected to the longest conductor in the house: the power line. That is the path
an electromagnetic event uses. **It is still usually the right choice**: it gives instant backup
power in every ordinary outage, and ordinary outages are far more likely than an electromagnetic
event (ranked 1 to 4 above, against 5). A daily medical benefit outweighs a rare,
unpredictable hedge.

The way to have both:
```
NORMAL TIMES
[ ] Working power stations: connected and doing their job (09-03, 09-16).
    Their protection is the reserve tier below, not a box.
RESERVE TIER (never in daily use)
[ ] A small station or power bank + a folding panel + cables, kept IN the
    shielded container or at least stored unplugged and uncoupled.
SOLAR PANELS AND WIRING
[ ] Panels and their cable runs stored UNCONNECTED when not in use. A connected
    string of panels is a long conductor; a stack of disconnected panels is
    close to inert. Connect a string only to use it.
```

{{#if has.power_station}}Your stations: {{#each stations as s}}{{s.model}} ({{s.wh}} Wh); {{/each}}decide which one is the reserve: ______________{{/if}}

## The things that need no protection at all

This is the more important list:
{{#if has.diabetes}}- **Syringes and insulin pens.** Mechanical.
{{/if}}{{#if has.oxygen}}- **Oxygen cylinders and a regulator that needs no power.**
{{/if}}- **Paper**: printed copies of the medical summary (→ 25-09), each person's emergency plans,
  contact cards (→ 25-03), maps (→ 25-04).
- **Manual tools, matches, hand pumps, the woodpile.**
- **Skills** (→ 23-05).

**A household whose critical paths are all mechanical or on paper need not worry much about this
section.** Getting there is the real goal.

## What you need

| Item | Why | Notes |
|---|---|---|
| **The no-power backup for each device** (syringes or pens, oxygen cylinders, a manual chair, as applies) | The backup that always works | As prescribed; → 12-07 |
| {{#if has.diabetes}}**Backup meter, strips, lancets**{{else}}**Simple non-electronic medical tools**{{/if}} | Not networked, cheap, in date | → 26-08 |
| **A second power bank** | Runtime for the devices and phones | → 09-10 |
| A metal container with a tight lid, and an insulating liner | The honest hedge, cheaply | See the limits above |
| A small 12-volt inverter | Gives the reserve tier household power from a vehicle | → 09-11 |
| A spare battery or hand-crank radio | News when nothing else works | → 15-01 |
| Printed plans and medical summary | Paper is immune to all of this | → 25-09 |

No money? An ammo can, a metal filing-cabinet drawer or a metal trash can all enclose. **The
substitute that matters is not a container at all: it is a practised no-power routine and the
supplies it needs.**

## When it runs out

| Item | Runway | Ration? | Resupply | Substitute |
|---|---|---|---|---|
| **Prescription medicine** | Your count (→ 23-02) | **No: never a household decision** (→ 12-11) | → 12-07 | **None** |
| Device supplies (pump sets, sensors, tubing, filters) | Count | Only as the prescriber or supplier says | → 12-07 | The no-power backup |
| Test strips | Count | Test as the clinician advises (CDC, Managing Sick Days) | → 12-07 | Poor |
| Device batteries | Days | → 09-01 | Solar, vehicle (→ 09-11) | The no-power backup |

**The point:** every row except the first has a substitute, and the first has none. **The
electronics can be replaced and the medicine cannot** (→ 23-04).

## By phase

- **A, at home:** hold spares, practise the backup, keep the printed plans current.
- **B, moving:** the medical kit rides in the passenger space, not the trunk (→ 22-05); the backup
  plan travels on paper.
- **C, establishing:** electronics get harder to replace and to charge (→ 09-05). The mechanical
  path becomes the normal one, not the backup.

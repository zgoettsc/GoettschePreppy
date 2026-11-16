---
id: 09-06-charging-medical-devices
section: 09-power-and-energy
title: "Keeping phones and medical devices charged"
version: 2
revised: 2026-11-16
layer: core
danger_level: critical
phase: [A, B, C]
tags: [power, medical, phone, charging, power bank, cpap, oxygen, cgm, pump, devices]
derived_from: [09-06-charging-medical-devices]
sources:
  - usfa-battery-fire-safety-r14
  - usfa-blog-lithium-ion-batteries-2026-r8
  - american-red-cross-power-outage-safety-6d07a8
  - resmed-airsense-11-user-guide-r14
  - caire-airsep-newlife-technical-manual-r14
related:
  - 09-01-power-priorities
  - 09-03-batteries-and-storage
  - 09-10-power-for-medical
  - 09-11-hand-and-alt-generation
  - 09-12-ac-dc-cables-and-connectors
  - 01-02-go-no-go-decision
  - 02-01-cl01-type-1-diabetes-injections
  - 02-02-cl02-type-1-diabetes-pump-and-cgm
  - 02-08-cl08-copd-and-oxygen
  - 02-22-cl22-mobility-impairment
  - 02-23-cl23-hearing-and-vision-aids
  - 02-24-cl24-sleep-apnea-cpap
  - 12-11-chronic-conditions
  - 22-03-go-bags-and-kits
  - 27-03-protecting-electronics
cards: []
explainers: [EX-02, EX-07]
promote_when: [has.cpap, has.oxygen, has.condition.CL-02, has.mobility_aid]
photo_slots:
  - { id: charging-kit, caption: "Our known-good charging kit: cables, bricks, 12 V adapters, power banks, labelled" }
figures: []
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: { date: "2026-11-16", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "Lithium charging re-cited to USFA (NFPA archive empty); CPAP 56/73 W (ResMed AirSense 11) and 5-L concentrator 350 W (AirSep) from maker specs; unsourced power-bank delivery and days figures replaced by a measurement" }
---

# Keeping phones and medical devices charged

**What this page is for.** For many households the most important electrical load is not a
refrigerator; it is a phone that runs a medical app, a CPAP, an oxygen concentrator, a power
wheelchair, or the charger for a pump or hearing aids. This page lists the devices this household's
conditions depend on, how much power they need, and how to stretch a phone from one day to several.
Keeping medicine **cold** is the separate, harder problem on → 09-10.

> **SAFETY.** **Power planning buys time; the manual fallback in each condition module is what
> keeps a person safe when the power is gone.** Every medical device that needs electricity has a
> non-electric fallback described in its module (→ 12-11 lists them). Rehearse it now, while you
> can still check your work.
> **Charging lithium safely** (US Fire Administration): charge on a solid, flat surface, never on a
> bed, couch or pile of clothes (soft surfaces trap heat); not in direct sun; store packs away from
> anything that burns and away from exits; use the original charger or a certified replacement,
> not a cheap knock-off. **Stop using a battery that shows an odd smell, a change in colour, too
> much heat, a change in shape, leaking or odd noises** (USFA, Battery Fire Safety, from NFPA), or
> that is smoking, hissing, punctured or swollen: get everyone away from it.
> {{#if has.young_child}}A young child lives here: power banks and cables stay out of reach; a
> toddler will chew a cable.{{/if}}

## Do this now
- **Keep three or four 20,000 mAh USB power banks charged.** At about 70 Wh each (20 Ah × the cell's
  3.6 to 3.7 V), one refills a phone several times. The cheapest, simplest, most reliable answer to the most common critical load, and
  it needs no wiring, no solar and no knowledge.
- **Standing rule: every phone and power bank goes on the charger every night, grid or no grid.**
  The outage you do not see coming arrives with your phone at 12%.
- **Find, test and label one known-good set of every cable and charger you need**, and put it in a
  bag with the go-bag (→ 22-03). Cables fail more often than batteries. {{photo charging-kit}}
- **Print the offline essentials** for every device: settings, the fallback method from the
  condition module, the medication list and contacts, on paper in this binder, so a dead phone does
  not take the information with it.
- **Ask your medical equipment supplier now**, while you can: how many watts each device draws,
  whether a 12 V DC cord or a battery pack is made for it, which settings cut its power use on
  battery, and how long its own battery lasts. Write the answers in the table below. The Red Cross
  advises planning back-up and non-power alternatives for medical devices and refrigerated medicine,
  and discussing the plan with your primary care or medical device providers (American Red Cross,
  Power Outage Safety).
- **Practise one full day in low-power mode** with the phone, and measure what it actually drew.
  Write it on → 09-01.

## The devices this household depends on

{{#if has.condition.CL-02}}- **Phone running an insulin pump or CGM app; CGM receiver; pump controller; any radio bridge between
  phone and pump.** The phone is a medical device: a dead phone can mean losing automated insulin
  delivery and glucose readings at the same moment. Keep a **second phone** with the apps installed
  and configured, and a fingerstick glucose meter on ordinary cells. The tech-failure fallback is
  in → 02-02; rehearse it.
{{/if}}{{#if has.condition.CL-01}}- **Glucose meter (fingerstick).** Runs on ordinary coin or AAA cells and needs no charging: the most
  robust glucose tool you own. Stock its batteries and strips heavily; rotate strips for expiry
  (→ 02-01).
{{/if}}{{#if has.cpap}}- **CPAP.** One common machine lists a typical power use of 56 W and a peak of 73 W (ResMed,
  AirSense 11 user guide): about 450 Wh over an 8-hour night at the typical figure. Find out whether
  yours has a DC cord or battery pack, and measure its draw with and without the humidifier. The
  module says what happens without it (→ 02-24).
{{/if}}{{#if has.oxygen}}- **Oxygen concentrator.** A motor-and-compressor load: read its label watts. One common 5-litre
  home unit is rated at 350 W (AirSep NewLife technical manual): about 8,400 Wh a day around the
  clock, so a station may run it only for hours. Cylinders and portable-concentrator
  batteries are the backup; know your cylinder hours (→ 02-08).
{{/if}}{{#if has.mobility_aid}}- **Power wheelchair or scooter.** Large battery; charge it whenever there is surplus, and know its
  range. A manual chair is the fallback (→ 02-22).
{{/if}}{{#if has.condition.CL-23}}- **Hearing aids and other small aids.** Rechargeable or disposable cells: stock spares and the
  charger (→ 02-23).
{{/if}}{{#if has.condition.CL-07}}- **Nebuliser** (if used). Electric; inhalers need no power (→ 02-07).
{{/if}}{{#if has.condition.CL-15}}- **Home dialysis equipment** (if used). Beyond any portable system; the module is honest about this
  (→ 02-15).
{{/if}}- **Phones for everyone:** information, alerts, contact, this binder.
- **Radio and weather radio** (→ 15-02), **headlamps and flashlights** (→ 10-01).

**Our device table** (fill in from labels and the supplier's answers):

| Device | Who | Watts | Wh per day | DC cord or battery pack? | Its own battery lasts | Non-electric fallback (module) |
|---|---|---|---|---|---|---|
| Phone | | 5 to 20 W charging | 10 to 20 | USB | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |

## Why it works this way

**Charging small devices is easy; it is cooling medicine and running motors that is hard.** A phone
is roughly **10 to 20 Wh a day** (typical; measure yours), less when managed. A 20,000 mAh power bank
holds about 70 Wh, but less than that reaches the phone after conversion losses; count how many
full phone charges one bank really gives you and write it here: ______. That is usually **days** of
a carefully managed phone. A CPAP or an oxygen concentrator is a different scale: size them on
→ 09-01 and → 09-03 like any other load.

**Stretching a phone from one day to several: the highest-value skill here.**
1. **Airplane mode, with Bluetooth on if a medical device needs it.** A phone searching for a dead
   cell tower is one of the biggest drains there is. **Check now that your medical app keeps working
   correctly in airplane mode before you rely on it.**
2. **Screen brightness to minimum, screen timeout to shortest.** The display is the largest consumer.
3. **Turn off background refresh, location and notifications** for everything except the medical
   apps.
4. **Turn off always-on display and raise-to-wake.**
5. **Keep it warm.** Lithium batteries lose capacity in the cold. A phone in a pocket against your
   body lasts far longer than one on a cold counter.
6. **Do not run it to 0% or store it at 0%.** A phone that dies overnight in the cold may not restart
   until it warms.
7. **Charge slowly from the power bank.** Fast charging makes heat and wastes energy.

**Redundancy beats capacity.** Two phones each holding a day are better than one holding two days,
because the failures that matter (dropped, wet, cracked, bricked by an update, lost in a move) are
not battery failures. Where a phone runs a medical app, keep an old phone with the app installed,
configured, charged and in a hard case. Test that it can actually take over.

**Batteries, not just charging.** Anything that takes AA or AAA cells can be fed by solar if you own
**rechargeable cells and a USB charger**. Stock the disposable cells your meters and aids use.

**Charge the efficient way.** A 12 V-to-USB adapter from a battery or station uses one conversion; a
wall charger plugged into an inverter uses two, plus the inverter's idle draw (→ 09-12).

## Gear and items

**Have it now (buy toward this):**

| Item | Why | Notes |
|---|---|---|
| 20,000 mAh USB power banks (three or four) | About 70 Wh each; days of phone per bank | Keep them charged |
| Small folding solar panel (20 to 60 W) with USB output | Recharges banks and phones with no system at all | Works in Phase B, in a car, on a fence |
| Spare cables of each type and wall chargers | Cables fail more than batteries | A known-good set sealed in the go-bag |
| 12 V USB adapters (car-socket type), including USB-C PD | Charges straight from a battery or station | → 09-12 |
| Backup phone, configured with the medical apps | Redundancy for the critical function | Test it every three months |
| Rechargeable AA and AAA cells and a USB charger | Makes every AA device solar-compatible | Meters, headlamps, radio |
| Stock of the disposable cells and strips your devices use | The no-charging fallback | Rotate for expiry |
| DC cords or battery packs for CPAP or concentrator, if made | Skips the inverter | Ask the supplier |
| Hard case or dry bag for the phone | The real failure is physical | Especially in Phase B |
| Printed settings and fallback methods | Survive a dead phone | In this binder |

**Scavenge or substitute:**
- **A vehicle's 12 V socket** charges phones for a long time (→ 09-11). The socket often stays live
  with the key on, and a car battery holds many phone charges; do not flatten a battery you need to
  start the car (→ 09-14).
- **Laptop USB ports**, cordless-tool batteries with USB adapters, UPS units, other people's power
  banks.
- **Solar yard lights** hold small cells and a panel: poor, but real.
- **Hand-crank chargers:** slow and tiring, better than nothing (→ 09-11).
- **Cables:** almost any USB cable will do; test with a cheap USB light before the medical device.

## When it runs out
- **Device charging rarely runs out first.** What runs out is the whole system (→ 09-05), the fuel
  (→ 09-04), or the medicine (→ 09-10).
- **Runway:** count power banks in days-of-phone (from the full charges you counted above) and write
  the total on → 23-02. Add the vehicle as a large reserve.
- **Ration:** airplane mode, screen dark, checked at intervals. **If you are down to one device and
  no way to charge it, switch to the module's non-electric fallback deliberately, while there is
  still enough battery to check the change-over**, not after the last 5% is gone.
- **Substitute, in order:** power bank → 12 V direct from a battery → vehicle socket → hand crank →
  **the non-electric method in the condition module**, which is the real floor.
- **Escalation:** if you cannot keep a life-sustaining device powered and have no working fallback,
  that is a go/no-go input (→ 01-02), not something to endure.

## Phase notes
- **A (at home):** power banks charged from the house system daily; phone managed but not rationed;
  backup phone charged. Build the habits and rehearse the fallbacks.
- **B (moving):** power banks are the whole plan: light, robust, nothing to set up. Carry them full.
  A small folding USB panel on a pack trickles through the day. Keep the phone against your body in
  cold weather.
- **C (settled somewhere new):** rebuild the house system, and keep the power-bank habit: it is the
  layer that survives a controller failure or a dead bank.

## Cross-references
→ 09-01 load triage · → 09-03 batteries and stations · → 09-10 power for refrigerated medicine ·
→ 09-12 cables and USB-C · → 12-11 the condition library and each module's fallback · → 27-03
protecting electronics · → 01-02 go/no-go

---
id: 00-04-family-emergency-plan
section: 00-front-matter
title: "Our family emergency and communications plan"
version: 1
revised: 2026-11-16
layer: household
danger_level: none
phase: [A, B, C]
tags: [family plan, meeting places, out-of-area contact, communications, shutoffs, children, caregivers, destinations]
derived_from: [00-04-family-emergency-plan]
sources:
  - fema-ready-gov-create-your-family-emergency-communic-584e89
  - american-red-cross-winter-storm-preparedness-and-bli-4bb6c0
  - cdc-recognizing-and-responding-to-anaphylaxis-645825
  - cdc-positive-parenting-tips-child-development-by-age-1e16c6
  - noaa-national-weather-service-tornado-safety-ba75e0
  - noaa-national-weather-service-nwr-county-coverage-an-c6207f
  - fema-ready-gov-utility-shut-off-and-safety-natural-g-7965ad
related: [15-03-family-comms-plan, 00-07-household-roles, 20-04-teaching-kids-the-plan, 25-03-regional-contacts, 22-03-go-bags-and-kits, 24-02-drills, 25-09-family-medical-summary, 25-08-quick-reference-cards, 01-05-choosing-a-destination]
cards: []
explainers: [EX-09]
promote_when: []
photo_slots:
  - { id: meet-near-home, caption: "Meeting place 1, near home: exactly where everyone stands" }
  - { id: gas-shutoff, caption: "Gas shutoff: the valve, which way is off, and where the wrench hangs" }
  - { id: water-main, caption: "Water main shutoff: the valve and which way is off" }
  - { id: electric-panel, caption: "Electric panel: the main breaker marked" }
figures: []
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: null
---

# Our family emergency and communications plan

> **Fill this in, print it, and put a copy everywhere.** A plan that lives in one adult's head
> fails exactly when that adult is away, injured or unreachable. **Every blank on this page is a
> decision made now instead of under stress.** Blanks marked "(fill in)" are answers you skipped
> in settings; plain blanks are things the binder deliberately never asks a web page for.

**What this page is for.** It is the household's one-page operating plan for being separated,
reaching each other, getting the children, and leaving. Most of it was filled from your answers;
the rest you write by hand.

## Do this now

1. **Fill in every blank in one sitting.** Half an hour, and the most valuable half hour in this
   binder.
2. **Choose the out-of-area contact and actually ask them.** Someone far enough away not to be in
   the same event, willing to be the hub, who answers their phone (FEMA, Create Your Family
   Emergency Communication Plan).
3. **Walk to each meeting place** with everyone who would need to get there{{#if has.child}},
   children included{{/if}}.
4. **Make copies**: fridge, every go-bag, every vehicle, the out-of-area contact{{#if has.child}},
   and each school or daycare{{/if}}.
{{#if has.child}}5. **Teach each child their part** (section 8, → 20-04).{{/if}}

## Why / how it works

### The five decisions this plan makes in advance
1. **Where do we meet** if we are separated and cannot call?
2. **Who is the hub** everyone reports to?
3. **Who gets the children or dependants** if the usual adults cannot?
4. **What does a caregiver need to know** to keep everyone alive?
5. **Who does what** in the first hour (→ 00-07)?

**Text, do not call.** When the network is busy, a text often gets through when a call will not,
and it waits for a phone that is switched off (American Red Cross; FEMA).

## THE PLAN

Completed: ____________ · Reviewed: ____________ · Next review: ____________

### 1. Who we are

| Name | Role | Age | Conditions | Mobile phone | Work or school, and its phone |
|---|---|---|---|---|---|
{{#each members as m}}| {{m.label}} | {{m.role}} | {{m.age_text}} | {{m.conditions}} | ____________ | ____________ |
{{/each}}

{{#if has.pets}}**Pets:** {{#each pets as p}}{{p.count}} {{p.type}} · {{/each}} Vet and phone: ______________________{{/if}}

Home address (write by hand, never typed into a web page): ______________________________________

### 2. Meeting places

{{photo meet-near-home}}

| | Place | Use it when |
|---|---|---|
| **1. Near home** | {{ contacts.meet.near_home }} | Fire or sudden evacuation of the house. **Go there and stay.** Never back toward the house, never behind a parked car where you cannot be seen |
| **2. In town** | {{ contacts.meet.in_town }} | You cannot get home. A house with people you know beats a landmark: it works at 2 a.m., in winter, in pyjamas. **Ask them first** |
| **Backup if 2 is unreachable** | ______________________ | |
| **3. Out of town** | {{ contacts.meet.out_of_town }} | You cannot get back into town |

**Rule:** go to the nearest one you can safely reach, and **wait**. Do not go looking for each
other.

### 3. Communications

**Out-of-area contact (the hub: everyone reports here)**

| Name | {{ contacts.out_of_area.name }} |
|---|---|
| Phone | {{ contacts.out_of_area.phone }} |
| Second phone | ______________________ |
| They have agreed and have a copy of this page | Yes / No |

**Local backup contact:** ______________________ Phone: ______________

**If phones work:** text first, call second, keep it short, save battery (→ 00-10).

**If phones do not work:** handheld radios (→ 15-02, → 29-09).

| | |
|---|---|
| Our radio channel | ______________ Privacy code: ______ |
| Repeater, if any (→ 15-06) | ______________ |
| Daily check-in time with the hub | ______ ; if missed, again at ______ ; two misses in a row = overdue (→ 15-03) |

**NOAA Weather Radio for our county** (→ 15-01):

| Transmitter | Frequency (MHz) | SAME code |
|---|---|---|
{{#each region.home.nwr as t}}| {{t.call}} | {{t.freq}} | {{t.same}} |
{{/each}}

**If nothing works:** go to the meeting places on this schedule: ________________________________.
**Leave a written note at home** saying where you went and when.

### 4. Who collects the children and dependants

| Authorised to collect | Relationship | Phone | On file at school or daycare? |
|---|---|---|---|
| ______________________ | ____________ | ____________ | ______ |
| ______________________ | ____________ | ____________ | ______ |
| ______________________ | ____________ | ____________ | ______ |

**Each one has:** a copy of section 5 below, {{#if has.anaphylaxis}}the anaphylaxis action plan
and an epinephrine pair or knows where one is, {{/if}}and a copy of → 25-09.

**If the usual adults cannot care for the children or dependants, the guardian is:**
______________________ Phone: ______________ Documented where: ______________________

### 5. The medical essentials a caregiver must know

**Allergies:**

| Person | Allergen | Severity | Carries epinephrine |
|---|---|---|---|
{{#each allergies as a}}| {{a.member}} | {{a.allergen}} | {{a.severity}} | {{a.carries_epinephrine}} |
{{else}}| none entered | | | |
{{/each}}

{{#if has.anaphylaxis}}**For anaphylaxis: EPINEPHRINE FIRST, into the outer thigh. Antihistamines
are not a treatment. A second dose is often needed** (CDC, Recognizing and Responding to
Anaphylaxis; → 02-03). Epinephrine is kept: ______________________________________{{/if}}

**Medicines, exactly as typed from the bottles:**

| Person | Medicine | Strength | Schedule | Refrigerated | If doses are missed (prescriber's words) |
|---|---|---|---|---|---|
{{#each meds as x}}| {{x.member}} | {{x.name}} | {{x.strength}} | {{x.schedule}} | {{x.refrigerated}} | {{x.if_missed}} |
{{else}}| none entered | | | | | |
{{/each}}

**Each condition's emergency signs and first steps** are on its page in Section 02. Attach the
signed plans from your prescribers here. Medical supplies are kept: ______________________

Full detail: → 25-09, the family medical summary.

### 6. If we have to leave

| | Where |
|---|---|
| Go-bags | ______________________ |
| Medical kit | ______________________ |
| {{#if has.pets}}Pet carriers{{else}}Other carriers or aids{{/if}} | ______________________ |
| Document kit (→ 19-01) | ______________________ |
| Vehicle keys | ______________________ |

**Who carries whom, who grabs what in the first 60 seconds:** see → 00-07.

**Destinations** (full detail and what each status means: → 01-05):

| Destination | Where | About | Status | Who is there | How to reach them |
|---|---|---|---|---|---|
{{#each destinations as d}}| {{d.name}} | {{d.county}}, {{d.state_name}} | {{d.approximate_miles}} mi | {{d.status_text}} | {{d.who_is_there}} | {{d.how_to_reach_them}} |
{{else}}| none entered (→ 01-05) | | | | | |
{{/each}}

Routes, primary and alternate: → 01-03 and → 25-04. **We will leave a note at:**
______________________

### 7. Utilities and the house

{{photo gas-shutoff}}

| | Where | Notes |
|---|---|---|
| **Gas shutoff** | ______________________ | {{#if has.gas_any}}Quarter turn so the handle is **across** the pipe. Tool: ______ kept ______. **Smell gas: everyone out, no switches, call the gas emergency number from outside.** Only the utility turns it back on (FEMA, Utility Shut-off and Safety){{else}}No gas service entered{{/if}} |
| **Water main** | ______________________ | Know which way is off; practise it |
| **Electric panel** | ______________________ | The main breaker is marked |
| **Water heater drain** | ______________________ | {{#if has.water_heater_tank}}About {{ dwelling.water_heater_gallons }} gallons of stored water (→ 03-02){{/if}} |
| **Fire extinguishers** ({{ gear.extinguishers }}) | ______________________ | → 29-12 |
| **Smoke alarms** ({{ gear.smoke_alarms }}) and **CO alarms** ({{ gear.co_alarms }}) | ______________________ | One CO alarm in the room where people sleep; installed and tested **before** any fuel-burning heater is lit (→ 08-02) |
| **Tornado shelter spot** | {{ dwelling.shelter_room }} | Backup spot: ______________ (→ 17-06) |

{{photo water-main}}
{{photo electric-panel}}

| Utility | Provider | Phone, as typed from your bill |
|---|---|---|
| Electric | {{ contacts.utility.electric.provider }} | {{ contacts.utility.electric.phone }} |
| Gas | {{ contacts.utility.gas.provider }} | {{ contacts.utility.gas.phone }} |
| Water | {{ contacts.utility.water.provider }} | {{ contacts.utility.water.phone }} |

**Every adult has physically operated the shutoffs:** Yes / No

{{#if has.child}}
### 8. The children's part (teach it, do not just write it)

For each child old enough, tick when they can do it without help:

- [ ] Their full name, and the full names of the adults they live with
- [ ] What the smoke alarm sounds like and where meeting place 1 is
- [ ] "If you feel funny or someone is hurt, tell a grown-up right away"
- [ ] How to blow their whistle
- [ ] That a grown-up will always come for them
- [ ] Their job in the grab drill: ______________________________

**Each child carries:** a card with names and the out-of-area number, a whistle, a comfort item,
and snacks that are safe for them.
{{#if has.infant}}**Infants and toddlers are carried, always.** No exceptions (→ 22-03).{{/if}}
{{else}}
### 8. Dependants and visitors

If a child, an elder or anyone who needs help ever lives with or visits you, write their part
here: what they must know, what they carry, who is responsible for them. ______________________
{{/if}}

### 9. Neighbours and mutual aid

| Neighbour | Phone | Can help with |
|---|---|---|
{{#each local_contacts as c}}| {{c.name}} ({{c.relationship}}) | {{c.phone}} | {{c.notes}} |
{{/each}}| ______________________ | ____________ | ______________ |
| ______________________ | ____________ | ______________ |

**Who near us would need our help** (elderly, alone, medically fragile): ________________________

**Who knows about our household's medical needs:** ______________________________________

### 10. Signatures and copies

Agreed by: ______________________ · ______________________ · Date: ________

Copies are at: fridge ____ · go-bags ____ · vehicles ____ · school or daycare ____ ·
out-of-area contact ____

### Making the plan real

A written plan that has never been walked is a wish. **Do these four things:**

1. **Walk to each meeting place** with everyone (→ 24-02).
2. **Run the 60-second grab drill**, timed (→ 22-03).
3. **Call the out-of-area contact and tell them what the role means.**
4. **Operate the shutoffs**: every adult, hands on, at least once.

## Gear / items

**Have now (buy toward this):** printed copies for every location in sheet protectors; wallet
cards with the out-of-area number for every adult{{#if has.child}} and child{{/if}}; a whistle for
each child; a magnet or clip for the fridge copy; the signed plans from your prescribers to attach.

**Scavenge / substitute:** an index card with **the out-of-area number, the meeting places, and
anyone's life-threatening allergy or condition** is most of the value of this page. Write it
today, put one in every wallet, and finish the rest later.

## When it runs out

- **Runway:** about a year. People move, numbers change, children's abilities change fast.
- **Ration:** if you fill in only two sections, fill in **2 (meeting places) and 5 (medical)**.
- **Resupply:** the annual review (→ 25-10), and regenerate after any move, new job, new school or
  new household member.
- **Substitute:** none. **An unwritten plan is a different plan in each adult's head**, and they
  disagree at exactly the wrong moment.

## Phase notes

- **A:** the plan covers ordinary emergencies too: a fire, a storm, a school lockdown, a hospital
  trip. That is most of its real use.
- **B:** sections 2, 3 and 6 are the operating plan. **The copies in the vehicles are the ones
  that matter.**
- **C:** rewrite it for the new place within the first week: new meeting places, neighbours,
  shutoffs, emergency numbers and weather radio frequencies (Section 32).

## Cross-references

- → 15-03 the full communications plan · → 00-07 roles · → 00-06 the first 60 minutes
- → 20-04 teaching the children · → 24-02 drills · → 25-03 contacts · → 25-09 medical summary
- → 22-03 go-bags · → 25-08 the card version · → 01-05 destinations

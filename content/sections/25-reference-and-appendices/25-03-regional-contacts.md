---
id: 25-03-regional-contacts
section: 25-reference-and-appendices
title: "Regional contacts and resources"
version: 1
revised: 2026-11-16
layer: region
danger_level: none
phase: [A, B, C]
tags: [contacts, phone numbers, NWS, NOAA weather radio, SAME, emergency management, utilities, poison control, extension]
derived_from: [25-03-regional-contacts]
sources:
  - federal-communications-commission-9-1-1-and-e9-1-1-s-a8c9c7
  - national-capital-poison-center-poison-control-1-800-e428c9
  - 988-suicide-and-crisis-lifeline-samhsa-988-suicide-a-5f45b0
  - samhsa-disaster-distress-helpline-28957e
  - national-domestic-violence-hotline-national-domestic-8e50ea
  - noaa-national-weather-service-nwr-county-coverage-an-c6207f
  - noaa-national-weather-service-noaa-weather-radio-all-5f13d8
  - fema-ready-gov-create-your-family-emergency-communic-584e89
related: [15-01-weather-alerts, 15-03-family-comms-plan, 15-04-monitoring-and-info, 25-08-quick-reference-cards, 19-01-document-grab-kit, 25-09-family-medical-summary, 12-07-meds-stockpile, 18-01-mutual-aid, 25-10-annual-review, 00-04-family-emergency-plan]
cards: []
explainers: [EX-09, EX-10]
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

# Regional contacts and resources

**What this page is for.** The phone numbers and offices you will want when the phone's contact
list is dead or the internet is gone, in one place you can print or copy. Three kinds of entry:
**national numbers** that are the same everywhere (printed); **your region's offices** from the
binder's region data (printed by name); and **local numbers** you type in settings or write by
hand. **This binder never looks up or guesses a local phone number**: one wrong digit in an
emergency is worse than a blank.

## Do this now

1. **Fill in every blank row in pencil, today.** The printed rows are the easy half; the blank
   ones (your clinic, your pharmacy, your neighbours) are the half that actually gets used.
2. **Make copies**: one in each go-bag (→ 22-03), each vehicle (→ 22-05), and one with the
   out-of-area contact.
3. **Program your NOAA Weather Radio** with your county's SAME code below, and check that the
   radio receives the transmitter (→ 15-01).
4. **Call each local number once** and tick its box. A number you have never dialled is a guess.
5. **Introduce yourself to two neighbours** and get their numbers. That one act is worth more in
   a real emergency than most of the gear in → 22-01 (→ 18-01).

## Emergency: the same everywhere

| Who | Number |
|---|---|
| **Police, fire, ambulance** | **911**. Any working cell phone can call 911, on any carrier's tower, even without service of its own (FCC, 9-1-1 and E9-1-1 Services) |
| **Poison Help (24 hours)** | **1-800-222-1222**: connects to your local poison center (Poison Control) |
| **988 Suicide & Crisis Lifeline** (call or text) | **988** |
| **Disaster Distress Helpline** (call or text, 24 hours) | **1-800-985-5990** (SAMHSA) |
| **National Domestic Violence Hotline** (24 hours) | **1-800-799-7233** · text **START** to **88788** |
| Road conditions | In many states, dial **511** |

Animal poisoning: your vet, or a pet poison line written here: ______________________

## Utilities (as typed in settings)

| Service | Provider | Number | Dialled once ☐ |
|---|---|---|---|
| **Electric outage** | {{ contacts.utility.electric.provider }} | {{ contacts.utility.electric.phone }} | ☐ |
| **Gas leak or gas emergency** | {{ contacts.utility.gas.provider }} | {{ contacts.utility.gas.phone }} | ☐ |
| **Water** | {{ contacts.utility.water.provider }} | {{ contacts.utility.water.phone }} | ☐ |

**If you smell gas: leave the building first, then call 911 and the gas company from outside**
(FEMA, Utility Shut-off and Safety; → 16-12). Shutoffs: → 00-04.
{{#if has.propane_service}}Propane supplier and its emergency line: ______________________ ☐
{{/if}}

## Weather and hazards: home

| Resource | Detail |
|---|---|
| **NWS forecast office for {{ home.county }}, {{ home.state_name }}** | {{ region.home.nws_office }}. Office phone, if you want it: ______________ |
| **State emergency management agency** | {{ region.home.state_em }}. Phone: ______________ |
| **County or city emergency management** | ______________________ Phone: ______________ ☐ |
| **Non-emergency police or sheriff** | ______________________ Phone: ______________ ☐ |
| Local radio and TV for weather (call letters, frequency) | ______________________ |

**NOAA Weather Radio transmitters that cover home** (program the radio with the SAME code: the
six-digit county code that makes it sound only for your county; → 29-09):

| Transmitter (call sign) | Frequency (MHz) | SAME county code | Received on our radio ☐ |
|---|---|---|---|
{{#each region.home.nwr as t}}| {{t.call}} | {{t.freq}} | {{t.same}} | ☐ |
{{else}}| ______ | ______ | ______ | ☐ |
{{/each}}

Coverage changes; the NWS publishes which transmitters cover each county (NOAA/NWS, NOAA Weather
Radio Coverage by County). Re-check at the annual review (→ 25-10). Neighbouring counties' SAME
codes, if you want warnings for them too: ______ ______ ______

{{#if has.destinations}}
## Weather and hazards: destinations

| Destination | County, state | NWS office | State emergency management |
|---|---|---|---|
{{#each destinations as d}}| {{d.name}} | {{d.county}}, {{d.state_name}} | {{d.region.nws_office}} | {{d.region.state_em}} |
{{/each}}

Their NOAA Weather Radio transmitters and SAME codes are on each state's page in Section 32;
copy them here: ______________________. Program them **on arrival** (→ 15-08).
{{/if}}

## Monitoring card (copy to → 25-08; full table on → 15-04)

```
NWR (home) ............ ______ MHz  call ______   received ☐
SAME (home county) .... ______
SAME (neighbours) ..... ______  ______  ______
SAME (destinations) ... ______  ______
Family radio channel .. ______  privacy code: none / ______   (15-02)
Repeater (if any) ..... ______  offset ____  tone ____        (15-06)
AM news station ....... ______   FM ______
```

## Medical

| Contact | Name | Phone | Dialled ☐ |
|---|---|---|---|
| **Primary care** | ______________________ | ______________ | ☐ |
| **Pediatrician**{{#if !has.child}} (if children){{/if}} | ______________________ | ______________ | ☐ |
| **Each specialist** (condition: __________) | ______________________ | ______________ | ☐ |
| **Each specialist** (condition: __________) | ______________________ | ______________ | ☐ |
| **Device support** (pump, sensor, oxygen, CPAP: the number on the box) | ______________________ | ______________ | ☐ |
| **Pharmacy, primary** | ______________________ | ______________ | ☐ |
| **Pharmacy, backup** (a different chain) | ______________________ | ______________ | ☐ |
| Mail-order pharmacy | ______________________ | ______________ | ☐ |
| Nearest emergency room (address) | ______________________ | ______________ | ☐ |
| Nearest urgent care | ______________________ | ______________ | ☐ |
| Dentist | ______________________ | ______________ | ☐ |
{{#if has.pets}}| **Vet**, and the nearest 24-hour emergency vet | ______________________ | ______________ | ☐ |
{{/if}}| Health insurance (member number) | ______________________ | ______________ | |
| State health department | ______________________ | ______________ | |

> **Ask every prescriber about emergency supply, 90-day fills and early-refill overrides.**
> That conversation is the most valuable item on this page (→ 12-07).

## Food, farming and skills

| Resource | Name and phone |
|---|---|
| **County Extension office** (the land-grant university's local office) | ______________________ |
| Master Gardener programme | ______________________ |
| State fish and wildlife agency (hunting and fishing rules, pre-collapse) | ______________________ |
| Feed store or farm supply | ______________________ |
| Butcher or meat locker | ______________________ |
| Farmers' market (days and place) | ______________________ |

**Extension is the most underused resource in this binder.** It is free, local, and staffed by
people whose job is teaching gardening, food preservation and livestock, and it is the best
answer to much of → 24-01. The National Center for Home Food Preservation is the national
authority for tested canning methods (→ 04-04, → 04-05).

## Community and mutual aid (these matter most)

| Contact | Name | Phone |
|---|---|---|
| **Out-of-area contact** (everyone reports here if separated; → 15-03) | {{ contacts.out_of_area.name }} | {{ contacts.out_of_area.phone }} |
{{#each local_contacts as c}}| {{c.relationship}} | {{c.name}} | {{c.phone}} |
{{/each}}| Neighbour | ______________________ | ______________ |
| Neighbour | ______________________ | ______________ |
| Family, local | ______________________ | ______________ |
| Family, out of state | ______________________ | ______________ |
{{#if has.child}}| School or daycare | ______________________ | ______________ |
{{/if}}| Faith community | ______________________ | ______________ |
| Local ham radio club | ______________________ | ______________ |
| Skilled people we know (mechanic, nurse, welder, gardener, hunter) | ______________________ | ______________ |

## Practical services

| Service | Name and phone |
|---|---|
| Bank or credit union | ______________________ |
| Home and auto insurance (policy numbers) | ______________________ |
| State insurance department (consumer line, pre-collapse) | ______________________ |
| Fuel or propane supplier | ______________________ |
| Firewood supplier | ______________________ |
| {{#if has.well}}Well service{{else}}Plumber{{/if}} | ______________________ |
| {{#if has.septic}}Septic service{{else}}Electrician{{/if}} | ______________________ |
| Hardware store | ______________________ |
| Auto repair and towing | ______________________ |

## National resources worth knowing by name

You cannot reach these without the internet or a phone line, but their documents are behind the
pages that cite them in this binder{{#if size.large}} (this is the Large copy){{else}} (the Large copy holds the full documents; this Small copy names them){{/if}}.

| Resource | Use |
|---|---|
| USA.gov, Replace Your Vital Documents | Replacing lost documents (→ 19-01) |
| IRS, Reconstructing Records After a Disaster | Tax and property records after a loss (→ 19-03) |
| FoodSafety.gov | Food after a power cut; cooking temperatures (→ 04-17) |
| EPA, Emergency Disinfection of Drinking Water | Water treatment (→ 03-04) |
| CDC, How to Create and Store an Emergency Water Supply | Storage and quantities (→ 03-02) |

## The offline problem

**Every website is useless the moment the internet is.** That is why the binder carries its
sources inside, why this page holds numbers and not links, and why **the most valuable contacts
here are the human ones**: neighbours, family, the ham club, the person who keeps chickens two
streets over. They work when nothing else does (→ 18-01).

**What you need:** a printed copy in every bag and vehicle, laminated wallet cards with the
essentials (→ 25-08), a pencil, and a small paper address book kept with the document kit
(→ 19-01). **The best substitute of all is memorised numbers**: make sure everyone old enough to
speak knows the out-of-area contact's number.

## When it goes stale

- **Numbers stay right for about a year.** Offices move; people move more.
- **Do not skip the blank rows**: they are the ones that fail silently.
- **Re-check at the annual review** (→ 25-10), then reprint.
- **When phones and agencies are gone**, the contacts that still work are the ones you can walk
  to (→ 18-01, → 18-03).

## Phase notes

- **A (shelter in place):** all of these work. Use them now, especially Extension, your
  prescribers and the neighbours.
- **B (moving):** the out-of-area contact and the meeting places are what matter; most
  institutional rows stop working (→ 15-03).
- **C (establish):** rebuild this page for the new place on arrival: county Extension office,
  nearest clinic and pharmacy, the local emergency manager, and the neighbours. Do it in the
  first week.

Related: → 15-01 weather alerts and SAME codes · → 15-03 the family comms plan · → 25-08 the
card version · → 19-01 document kit · → 25-09 medical summary · → 12-07 medicine supply ·
→ 18-01 mutual aid · → 25-10 annual re-check · Section 32 for every state's offices.

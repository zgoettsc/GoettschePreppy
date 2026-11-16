---
id: 15-03-family-comms-plan
section: 15-communications
title: "Family communications plan: contacts, rally points, relay and cards"
version: 1
revised: 2026-11-16
layer: household
danger_level: caution
phase: [A, B, C]
tags: [family plan, out-of-area contact, rally point, reunification, note protocol, medical card, relay, PACE, text, "911", satellite, GMRS channel, children]
derived_from: [15-03-family-comms-plan]
sources: [noaa-national-weather-service-weather-ready-nation-b0a52f, american-red-cross-power-outage-safety-6d07a8, american-red-cross-winter-storm-preparedness-and-bli-4bb6c0, noaa-national-weather-service-noaa-weather-radio-all-5f13d8, apple-support-use-emergency-sos-via-satellite-messag-68d4e2, federal-communications-commission-9-1-1-and-e9-1-1-s-a8c9c7, fema-ready-gov-create-your-family-emergency-communic-584e89]
related: [00-04-family-emergency-plan, 15-01-weather-alerts, 15-02-radio-options, 15-05-ham-and-licensing, 15-06-antennas-and-range, 15-07-signals-and-codes, 15-08-destination-comms, 15-09-corridor-comms, 14-03-opsec, 12-11-chronic-conditions, 01-07-evacuating-with-medical-needs, 02-03-cl03-anaphylaxis, 02-04-cl04-food-allergy, 20-04-teaching-kids-the-plan, 20-05-infant-feeding, 20-08-kids-and-fear, 18-01-mutual-aid, 24-02-drills, 25-03-regional-contacts, 25-04-maps, 25-08-quick-reference-cards, 25-09-family-medical-summary, 25-10-annual-review, 01-03-phase-b-movement, 10-01-lighting-options]
cards: []
explainers: [EX-09]
promote_when: [has.child, has.anaphylaxis, has.refrigerated_meds]
photo_slots: []
figures: []
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: null
---

# Family communications plan: contacts, rally points, relay and cards

**What this page is for.** The situation this page exists for: **the household is separated when
something happens.** One adult at work and one at home; separated during a move; someone goes
for water and does not come back on time. This page is the plan: who to contact, where to meet,
how long to wait, how to leave notes, which channels to try in which order, and the cards that
let a stranger care for someone who cannot speak for themselves. It follows FEMA's family
communication plan approach (FEMA, Create Your Family Emergency Communication Plan).

> **CAUTION.** **Write the plan down, give copies to everyone, practise it once.** A plan that
> lives in one adult's head is not a plan. {{#if has.anaphylaxis}}**In your household,
> separation is also a medical problem:** someone has a severe allergy, and anyone who might end
> up caring for them needs the allergen list and the epinephrine plan on paper, in advance
> (→ 02-03).{{/if}}{{#if has.refrigerated_meds}} Someone depends on refrigerated medicine, which
> has to travel with them (→ 01-07).{{/if}}

## Do this now

1. **Fill in the one-page plan below**, print it, and put a copy in every wallet, every go-bag,
   the vehicle and this binder. Give one to the out-of-area contact.
2. **Make a medical card for everyone who needs one**: conditions, allergies, medicines, what to
   do, contacts. Laminate them. A stranger or neighbour may be the one reading it (→ 25-09).
3. **Agree an out-of-area contact.** In a regional emergency, local phone lines jam while
   long-distance calls and texts sometimes still get through. One relative or friend in another
   area whom everyone checks in with turns a scattered family into a connected one.
4. **Teach every child old enough** their full name, their parents' names, the rally point,
   and any allergy, as a game (→ 20-04).
5. **Agree the rally points and wait times out loud**, every adult.

## The plan on one page

**Contacts**

| | Name | Phone | Notes |
|---|---|---|---|
| Out-of-area contact (the relay) | {{ contacts.out_of_area.name }} | {{ contacts.out_of_area.phone }} | Everyone checks in here |
{{#each local_contacts as c}}| {{c.relationship}} | {{c.name}} | {{c.phone}} | {{c.notes}} |
{{/each}}| Clinician or pharmacy | ______________ | ______________ | Copy from → 25-03 |
| School or daycare | ______________ | ______________ | Write their release and reunification procedure (→ 00-04) |

**Rally points**

| | Place | When to use it |
|---|---|---|
| **Primary** | Home | The default. Everyone comes home |
| **Secondary, near home** | {{ contacts.meet.near_home }} | If the house is unsafe or cannot be reached. Ask the people there first |
| **Out of the neighbourhood** | {{ contacts.meet.in_town }} | If the area is unsafe. Somewhere everyone can name |
| **Out of town** | {{ contacts.meet.out_of_town }} | Leaving the area (→ 01-03) |

**Wait times** (the household decides; write them in pen and initial):

- Separated in town: each of us goes to the primary rally point and waits ______ hours.
- If nobody comes, go to the secondary point and leave a note (below). Wait ______ hours.
- **Check in with the out-of-area contact** whenever you can, from wherever you are, using the
  relay script below.
- If we cannot reconnect within ______ hours, we: ____________________________________________
  ______________________________________________________________________________
- **Medical override.** If the missing person depends on a medicine, device or supply that they
  carry on their body, waiting uses up **their** supply, not yours. For them, shorten every wait
  above (our shortened times: ______), treat the search as a medical search from the start, and
  tell every contact and responder what the condition is (→ 12-11). The same applies if someone
  with a severe allergy is with the missing party and the epinephrine is with them.

## The note protocol: the low-tech thing that works

- **A pre-agreed hidden spot at each rally point** where notes are left. **Not on the door**: that
  tells everyone the house is empty (→ 14-03). Under a particular rock, inside a particular
  container, taped inside a particular place.
- **The note says:** who was here, the date and time, where they went, and when they expect to be
  back or where to follow. **Nothing about supplies, weapons or the household's situation.**
- **Everyone knows the spot, and everyone checks it.** Keep the spots off any list a stranger
  could read.

## Medical and identity cards

One card per person who could not explain their own needs to a stranger: every child, and every
adult with a condition, allergy or medicine that matters in an emergency. The household's
members, as entered in settings:

{{#each members as m}}- **{{m.label}}** ({{m.age_text}}). Conditions: {{m.conditions}}. Allergies:
  {{m.allergies}}. Medicines: {{m.meds}}.
{{/each}}

{{#if has.anaphylaxis}}**Severe allergies in your household:**
{{#each allergies as a}}- {{a.member}}: **{{a.allergen}}** ({{a.severity}}). Carries epinephrine:
  {{a.carries_epinephrine}}.
{{/each}}{{/if}}

Each card carries:

- Full name, age, parents' or carers' names and phone numbers, the out-of-area contact.
- **Conditions and what an emergency looks like**, in plain words. For conditions that can look
  like drunkenness or confusion, such as low blood sugar, say so: it is what a bystander most
  needs to know (→ 12-11, and the person's own condition page in Section 02).
- **Allergies, and the severe ones in capitals**, with where the epinephrine is and how to use it
  (→ 02-03). For a child with a food allergy: **"Must not eat any food that an adult who knows this
  list has not approved"** (→ 02-04).
- Medicines (name and strength as on the bottle), and the clinician.
- For an infant or toddler: feeding needs (→ 20-05).

**Put the cards on the children**: a jacket pocket, a bracelet, a backpack, not only in an
adult's wallet.

## Channels, in the order they survive

1. **Text messages.** They use far less network capacity than calls and often get through when
   calls do not. **Text first.** Three things few people know:
   - **911 connects from any phone on any carrier's tower**, even with no service plan or no SIM
     card (FCC, 9-1-1 and E9-1-1 Services). Call it rather than texting: text-to-911 exists only
     in some areas. Ours: ☐ yes ☐ no ☐ unknown.
   - **A phone searching for a signal all day is flat by evening.** Use airplane mode between
     attempts (→ 15-09).
   - **Wi-Fi calling and app messaging work over any internet connection**, including a
     neighbour's or a satellite dish. Turn Wi-Fi calling on in each phone's settings now.
2. **The out-of-area contact.** Local lines jam; long distance sometimes does not.
3. **Satellite texting from the phone itself.** Some phones (for example iPhone 14 and later) can
   send an emergency SOS text with your location, and newer software can send ordinary texts, by
   satellite when there are no bars at all: clear sky, phone held up, follow the on-screen pointer
   (Apple Support, Emergency SOS via satellite). **Try the demo now** if your phone has it. A
   dedicated satellite messenger does the same job, **but only with a paid subscription.**
   Our phones with satellite texting: ______________________
4. **Satellite internet**, if the household has it and it is activated (→ 15-02). An inactive dish
   is not a channel.
5. **Radio** (→ 15-02): GMRS for local coordination, on a pre-agreed channel and schedule (below).
6. **Notes at the rally points.** The one that always works.
7. **Walking there** (→ 18-01). In a neighbourhood this is often the fastest and most reliable,
   and people forget it.
8. **Visual and sound signals** (→ 15-07): whistles, lights, a cloth in a window.

## The relay card: print it, and give the contact a copy

The out-of-area contact ({{ contacts.out_of_area.name }}) is the **switchboard**: in a crisis,
everyone reports to them, and they pass messages between family members{{#if has.destinations}}
and destinations (→ 15-08){{/if}} who cannot reach each other directly.

**The script: every call, text or relayed message uses these four lines, in this order:**

1. **WHO** is calling (name, and who is with them)
2. **STATUS**, one word: **OK / NEED HELP / MOVING**
3. **WHERE** (as specific as is safe to say, → 14-03)
4. **NEXT CHECK-IN**: when this person will report again

**The schedule** (the same words everywhere it is printed: → 00-04, → 15-08, → 25-08):
daily check-in with the relay at ______ (time and time zone); if missed, at ______ the next
morning; **two missed check-ins in a row = overdue** (what happens then: → 15-08).

**On the relay's copy:** *"When anyone asks, pass on the latest WHO, STATUS, WHERE and NEXT
CHECK-IN you have for the others."*

Briefed (date) ____________ Agreed (date) ____________. A relay who has not heard the plan out
loud is a phone number, not a relay.

## The household channel ladder

P = try first, A = alternate, C = contingency, E = emergency or last resort. Fill it in; keep the
words short enough to copy onto a wallet card (→ 25-08).

| Situation | P | A | C | E |
|---|---|---|---|---|
| **Separated in town** | Text, then call | Out-of-area relay | GMRS channel ____, at the agreed times | Rally points and notes; walk there |
| **Regional outage** | Text; Wi-Fi calling over any working internet | Relay at the agreed time | Satellite text; GMRS or amateur radio (→ 15-05) | Notes at rally points; neighbours; signals (→ 15-07) |
| **On the road** | Text from named check-in towns (→ 15-09) | Another adult's phone on a different carrier | GMRS; CB channel 19 (road) and 9 (emergency); satellite SOS | Weather radio for news only; stop and wait (→ 15-09) |
| **At a destination** | Call or text home and the relay | The destination household's phones | Satellite text; GMRS at the agreed time (→ 15-08) | Relay; letters; travellers |

## The radio plan: pre-agreed

Radios only help if people listen at the same time.

- **Primary channel:** ______ **Backup channel or repeater:** ______ (→ 15-02). Use no "privacy
  code" for the family channel unless every radio is set the same: codes filter what you hear,
  they hide nothing.
- {{#if has.ham}}**Amateur frequencies** for the licensed members: ______ (→ 15-05).{{else}}If
  someone becomes licensed, add amateur frequencies here (→ 15-05).{{/if}}
- **Listening times:** for example five minutes on the hour: ______. **Listening all the time
  drains batteries and exposes you** (→ 14-03); set times do neither. (The weather radio is the
  exception: it stays on, → 15-01.)
- **Short and bland on the air.** Names and places only as needed; nothing about what you have
  (→ 15-07).

## Teaching the children

{{#if has.child}}You have children in the household.{{/if}}

- **A preschooler can learn** their full name, their parents' full names, the rally point, "I have
  allergies" if they do, and **"find a grown-up with a badge, or a grown-up with children"**.
  Practise it as a game, often, without making it frightening (→ 20-04, → 20-08).
- **They carry their card and know they have it.**
- **Babies and toddlers cannot do any of this**, so their identification and feeding information
  have to be **on them**.
- **Every child knows where the go-bags are**, and that one belongs to them.

## Practise it once

**Run one drill** (→ 24-02): "We're separated. What does everyone do?" Walk to the rally point.
Check the note spot. Try the radios. **You will find three things wrong with the plan, which is
the point.**

## Gear

| Item | Why | Notes |
|---|---|---|
| **The printed plan, many copies** | Wallets, go-bags, vehicle, binder, relay | Update yearly (→ 25-10) |
| **Laminated medical and ID cards** | A stranger may be reading it | → 25-09 |
| Medical ID bracelets or tags for children and anyone with a condition | Works when the card is lost | Cheap; truly valuable |
| GMRS radios on the agreed channel | Local coordination | → 15-02 |
| A whistle for every person, children included | Carries farther than a voice; no power | → 15-07 |
| Paper, pencil, waterproof bags | The note protocol | Pencil works wet and cold |
| A printed local map with rally points marked | Phones die | → 25-04 |
| The relay's number, **memorised and written** | The one number everyone should know | |
| A small flashlight per person | Signalling and safety | → 10-01 |
| A phone with satellite texting, or a messenger with a subscription | Reaches the relay with no bars | Try the demo; note which phones have it |

**If you do not have it:**

- **Notes and markers:** chalk, pencil, tape, scratched into a surface, or a pre-agreed object
  moved to a pre-agreed place. A signal that is not writing is harder for others to read (→ 15-07).
- **Identification for children:** name and details on a card in a pocket, written inside a
  jacket, or written on the child's skin with a marker (a real practice in disaster response).
- **Signalling:** whistle, mirror, flashlight, a bright cloth in a particular window (→ 15-07).
- **Messages:** neighbours (→ 18-01). Where people know each other, word travels faster than any
  technology.

## When it runs out

- **The materials barely wear out**; what goes wrong is the plan's accuracy. Numbers change,
  children grow, rally points stop making sense, medical details change. **Review it every year**
  (→ 25-10) and after any change in anyone's health.
- **The phone network is what runs out**, usually early. **Everything after "text messages" on the
  channel list is designed to survive that**, which is why the notes and rally points matter more
  than the technology.
- **Being reunited quickly is worth more than almost any supply in this binder**, above all when
  someone's medicine, device or allergy plan is carried by a different person.

## By phase

- **A (at home):** phones while they work; radios, rally points and notes when they do not.
  **Neighbours are part of the plan** (→ 18-01): a neighbour who knows your children and their
  needs is a real safety asset.
- **B (on the move):** **the plan is most likely to be needed and hardest to follow here.**
  Everyone carries their card and whistle, everyone knows the next rally point before you set off,
  and **nobody goes ahead out of sight with a child** (→ 01-03).
- **C (rural or a new place):** distances are longer and neighbours farther away, so **radio
  matters more** (→ 15-05, → 15-06). Set new rally points and note spots **on arrival**, and teach
  the children the new plan: their old one is now wrong.

---
id: 00-01-how-to-use-this-binder
section: 00-front-matter
title: "How to use this binder"
version: 3
revised: 2026-11-16
layer: core
danger_level: none
phase: [A, B, C]
tags: [front matter, orientation, app, offline, search, decision cards, regenerate, printing]
derived_from: [00-01-how-to-use-this-binder]
sources:
  - cdc-how-to-create-and-store-an-emergency-water-suppl-f0c412
  - us-epa-emergency-disinfection-of-drinking-water-6aa91f
  - national-center-for-home-food-preservation-nchfp-gen-c43991
related: [00-05-safety-disclaimer, 00-09-private-copy-notice, 00-10-install-and-charge-discipline, 00-02-emergency-quick-reference, 00-06-first-60-minutes, 00-03-master-index, 00-08-binder-map, 01-01-phase-a-shelter-in-place, 29-15-ex15-how-this-binder-was-made, 25-10-annual-review]
cards: []
explainers: [EX-15]
promote_when: []
photo_slots: []
figures: [fig-three-phases]
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: { date: "2026-11-16", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "Card range to 30-30; Sources row describes Small, Large and Everything via size.large/size.everything. L8: card range extended to DC-31 (→ 30-32) for new cards DC-30, DC-31." }
---

# How to use this binder

> **If something is happening right now, stop reading this page.** Go to → 00-06 (the first 60
> minutes) or → 00-02 (emergency quick reference). This page is for a calm afternoon.

**What this page is for.** It explains what this binder is, how to find things in it on a phone
with no internet, how each page is laid out, and how to keep it true as your household changes.

## Do this now

1. **Read → 00-05 (the disclaimer) and → 00-09 (the private-copy notice).** Both are short. They
   are the frame for everything else.
2. **Install it properly** (→ 00-10): on more than one device, tested in airplane mode, with the
   key pages printed.
3. **Read Section 01, the phase playbooks.** Seven pages. Every other section hangs off them.
4. **Answer the decision cards you left open** (→ 30-02 to → 30-32). Any page that depends on an
   open card prints "Not decided yet".
5. **Count what you actually have** (→ 26-01, then → 22-04). Every runway in the binder needs that
   number.
6. **Put the quick-reference cards** (→ 25-08) where they belong: fridge, go-bags, vehicles.

## What this binder is

An offline survival reference for **{{ household.name }}**: {{ household.size }} people
({{ household.labels }}) with a home base in {{ home.county }}, {{ home.state_name }}. It was
generated from the answers you gave in settings, while the power and internet worked, for a time
when they do not. It assumes:

- **A long outage is possible**: weeks to months without power, phones, pharmacies or help.
  Short events are a smaller version of the same thing.
- **You may be new to all of this.** Every term is explained the first time it appears, or points
  to an explainer in Section 29.
- **You know your household better than the binder does.** Where a choice involves real risk, the
  binder explains it and asks you to decide (→ 30-02 to → 30-32).

**Everything is always included.** Your answers change the order and the wording: your home
region comes first, your household's medical conditions lead Section 02, your gear's pages lead
their sections. Nothing is left out because you did not tick it; a condition or a piece of gear
you add later is already in the binder.

## The three phases: the spine

{{figure fig-three-phases}}

| Phase | Meaning | Pages |
|---|---|---|
| **A** | **Shelter in place** at home for as long as home works | → 01-01 |
| **B** | **Movement**: the decision to leave, the route, the trip | → 01-02, → 01-03, → 01-07 |
| **C** | **Establish** at a destination, or anywhere you end up | → 01-04, → 01-05 |

{{#if has.destinations}}Your destinations, with their status (agreed, unannounced, property only
or undecided), are on → 01-05.{{else}}You have not entered a destination. → 01-05 explains why
that matters and what to do instead.{{/if}} The checklists for moving between phases are → 01-06.
Every topic page has a **Phase notes** block saying what changes in A, B and C.

## Finding things

- **Search** (the box at the top) searches every page, explainer, card and condition, offline.
- **The emergency row** at the top of every screen goes straight to → 00-02 and → 00-06.
- **Cross-references** look like `→ 08-02`. Tap one to go to that page. On paper, the number is
  the page id, in order.
- **The master index** (→ 00-03) lists every page; **the binder map** (→ 00-08) shows the sections
  and what each is for.
- **The region picker** in Section 32 shows any state's climate, hazards, radio frequencies and
  plants. Your home state comes first{{#if has.destinations}}, then your destinations'{{/if}}.
- **The condition picker** in Section 02 shows any medical condition in the library, not only the
  ones you ticked.

## Anatomy of a page

Every topic page has the same blocks in the same order, so you can find things by position even
when you cannot concentrate:

| Block | What it is for |
|---|---|
| **What this page is for** | One paragraph, plain words |
| **Safety callout** (if any) | The thing that will hurt you, and the floors that apply. Read it first |
| **Do this now** | The action list. **If you read nothing else, read this** |
| **Why / how it works** | The understanding, so you can adapt when reality differs |
| **Gear / items** | What to have now, and what to scavenge or substitute |
| **When it runs out** | How long it lasts, how to ration it, how to resupply, what replaces it |
| **Phase notes** | What changes in A, B and C |
| **Cross-references** | Where to go next |

### The header on every page

| Field | Meaning |
|---|---|
| **Page id** (`NN-MM-slug`) | Stable. Cross-references use the `NN-MM` part |
| **Version and revised date** | If two copies disagree, the newer date wins |
| **Danger level** | `none`, `caution` or `critical` (below) |
| **Stamp** | "AI-reviewed, not human-verified" on every page (→ 00-05) |
| **Sources** | Title, publisher and date of each source. {{#if size.everything}}In your Everything binder every source document is bound behind the page that cites it.{{else}}{{#if size.large}}In your Large binder the documents cited by the life-safety sections (medical, water, food storage, fire and fuel, heating, power, first aid, hazards, children, radiation and chemical events, cards and floors) are bound behind the page; the others are in the Everything download (→ 00-09).{{else}}In the Small binder no document is inside; Large carries those behind the life-safety sections and Everything carries all of them (→ 00-09).{{/if}}{{/if}} |

### Danger levels

| Level | Meaning | What to do |
|---|---|---|
| **none** | Getting it wrong wastes time or money | Normal care |
| **caution** | Getting it wrong causes injury, illness or loss | Read the safety callout; follow the cited source |
| **critical** | Getting it wrong can **kill someone** | Read the whole page. Plan it with a professional now, while you can (→ 00-05). Examples: medicines, anaphylaxis, canning, carbon monoxide, water treatment, foraging, firearms, children's safety |

### Kinds of page

| Kind | What it means for you |
|---|---|
| **Core** | The same text in every household's binder. Method and facts that are true everywhere |
| **Region** | Filled from public datasets for your state and county |
| **Household** | Written from your answers: your plan, your people, your destinations. Only as good as what you typed |
| **Condition** | A medical module from the condition library (Section 02), with your own "my meds" rows |
| **Gear** | A module for a class of gear, with a spec row for your model or a blank to fill from the label |
| **Explainer** | Section 29: the words and ideas other pages assume |
| **Decision card** | Section 30: a real trade-off, with your household's answer |
| **Floors** | → 30-01: the rules that are never a choice |

More on what to trust, and why: → 29-15.

## Blanks, choices and photos

- **A blank line with "(fill in)"** means you skipped that question, or the binder will not guess
  it. Write it on the printed copy, and add it in settings next time you regenerate.
- **"Our choice:" lines** print your household's answer to a decision card, or "Not decided yet"
  with the card's page. Change a choice in settings, or cross it out on paper and write the new
  one with the date.
- **Photo frames** ("Add a photo in the app") are places to attach your own photo: the gas
  shutoff, the warm room, a meeting place. Photos stay on your device (→ 00-09, → 00-10).

## Reading it under stress: the three-layer rule

1. **Cards** (→ 25-08): ninety seconds, on the fridge and in every bag.
2. **"Do this now"**: the top block of the page you need.
3. **The rest of the page**: when there is time to understand, adapt and decide.

**Practise at layer 3 so you can act at layer 1** (→ 24-01).

## Keeping it current

The binder is regenerated, not edited. Keep your saved answers file (`profile.json`) somewhere
safe. When something changes, open the settings page, load that file, change the answer, and
generate a new binder. Then replace every copy (→ 00-10).

**Regenerate after:** a move; a new household member, baby or pet; a new medical condition or
medicine; new gear; a changed destination or contact; a changed decision card; and at the annual
review (→ 25-10).

**Write on the paper copy** in between: your measured water use, your frost dates, how much wood
a cold week took, what broke. Carry those notes into settings at the next regeneration. **A binder
that never changes is a binder nobody is using.**

### The habits that keep it true

| Cadence | What | Page |
|---|---|---|
| **Twice a year** (pick two dates, for example when clocks change) | Kit checks, expiry dates, children's sizes, full inventory | → 22-03, → 22-04 |
| **Twice a year** | A blackout weekend | → 24-04 |
| **Every three months** | One household drill | → 24-02 |
| **Each season** | That season's skills, garden and fuel | → 24-03 |
| **Once a year** | The full review, then regenerate | → 25-10 |

## Where to start, honestly

| If you have | Do this |
|---|---|
| **10 minutes** | Read → 00-06, and put the cards from → 25-08 on the fridge |
| **An hour** | Read Section 01 (the phases) and fill in → 00-04 (the family plan) |
| **An afternoon** | Walk the house with → 26-01 and → 26-02, then count everything into → 22-04 |
| **A weekend** | Run → 24-04, a blackout weekend. It finds more than anything else in the binder |
| **Some money** | Work down → 22-07 in order |
| **No money** | → 24-01 (skills), → 18-01 (neighbours), → 01-05 (secure a destination) |

## Gear / items

**Have now (buy toward this):** the binder on at least two devices; a power bank for each phone;
a printed copy of the key pages (→ 00-10) in a sturdy ring binder with tab dividers; sheet
protectors for pages that live in wet or greasy places (water, cooking, medical); sandwich bags or
a laminator for the cards; pencils (they write in the cold).

**Scavenge / substitute:** any folder or clip will hold paper. **What matters is that it is on
paper, in the house, where the family can find it in the dark.**

## When it runs out

Paper and files do not run out; **accuracy does.**

- **Runway:** about a year before medicines, contacts and children's sizes are noticeably wrong.
- **Ration:** if you can only keep part of it current, keep **your Section 02 condition pages,
  → 22-06 (the medical kit) and → 25-09 (the family medical summary)** current.
- **Resupply:** the twice-yearly checks, the annual review (→ 25-10) and regenerating.
- **Substitute:** none. **An out-of-date binder is a confident document full of stale facts**,
  which is worse than no document at all.

## Phase notes

- **A:** the whole binder is live. Read it, practise it, correct it.
- **B:** what you carry matters: the printed key pages, Section 01, your condition pages and the
  go-bag lists (→ 22-03, → 22-05). The binder device rides on a person, charged (→ 00-10).
- **C:** Sections 05, 06, 16 and 23 become the daily working pages. **Re-check everything
  local**: a new place changes the hazards, plants, frequencies and contacts. Use the region
  picker for your new county.

## Cross-references

- → 00-02 emergency quick reference · → 00-06 the first 60 minutes · → 00-05 the disclaimer
- → 00-09 the private-copy notice · → 00-10 install and charging
- → 00-08 the binder map · → 00-03 the master index · → 00-04 the family plan · → 00-07 roles
- → 29-15 how this binder was made · → 25-10 keeping it true

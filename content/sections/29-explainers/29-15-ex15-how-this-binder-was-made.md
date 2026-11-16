---
id: 29-15-ex15-how-this-binder-was-made
section: 29-explainers
title: "How this binder was made, and what to trust"
version: 2
revised: 2026-11-16
layer: explainer
danger_level: none
phase: [A, B, C]
tags: [about this binder, AI-reviewed, layers, decision cards, floors, sources, Small, Large, Everything, profile file, regenerate, private copy, explainer]
derived_from: []
sources: []
related: [00-01-how-to-use-this-binder, 00-05-safety-disclaimer, 00-09-private-copy-notice, 00-10-install-and-charge-discipline, 02-27-a-condition-not-in-the-library, 25-06-source-bibliography, 30-01-the-floors]
cards: []
explainers: []
promote_when: [experience.new]
photo_slots: []
figures: []
plates: []
condition: null
gear: null
explainer: EX-15
card: null
review_pass: { date: "2026-11-16", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "Small/Large/Everything rewritten to G25 and the app (size.everything, life-safety sections, maps, upgrade); review stamp section matches review.js (kit-build review plus per-binder checks)." }
---

# How this binder was made, and what to trust

**What this page is for.** Before you rely on a reference in an emergency, you should know who
wrote it, how it was checked, and where its limits are. This page explains how
this binder was put together, what the stamp on every page means, and how to
change or rebuild it later.

## Built in layers

| Layer | What it is | Who wrote it |
|---|---|---|
| **Core** | Method and fact that are true everywhere: water, food, fire and fuel, heat, power, first aid, sanitation, tools, communications. Plus these explainers (Section 29) and the decision cards (Section 30) | Written once from a fact-checked family binder, with that family's details removed, then frozen. Every household gets the same text |
| **Region** | Climate, hazards, plants, trees, weather offices and radio codes for every state and DC (Section 32). Your home base is moved to the front; the rest stays one tap away, because you may have to cross the country | Built from public datasets, not from memory |
| **Household** | Your people, contacts, meeting places, destinations, house, gear and supply lists | Filled in from your answers in settings; a few paragraphs, such as the story of the route to a destination, are written by the AI from those answers. Every number on these pages traces to something you typed or to a dataset |
| **Condition library** | Modules for common medical conditions (Section 02). The whole library is in every binder; the ones you ticked are moved to the front | Written once and frozen. No doses are worked out for anyone; published tables are printed as published |
| **Gear library** | How to read and run common classes of gear (Section 28) | Written once; your models are filled in from your answers |

Your copy was made at the **{{#if experience.new}}"new to all of this"{{/if}}{{#if experience.some}}"some experience"{{/if}}{{#if experience.experienced}}"experienced"{{/if}}**
level you chose: that sets whether these explainers sit at the front of each section or in the
back.

## "AI-reviewed, not human-verified": what the stamp means

Every page carries this stamp. It means exactly what it says. **No doctor, engineer,
electrician or other professional has checked your copy.** Two kinds of automatic check were run
instead:

- **When the kit was built**, an AI reviewed every page of the shared text once. Every number on
  a page marked critical or caution was traced to a named source that was read, or the number
  was corrected or removed. Pages were compared so that one rule, one number and one name are
  used throughout, and the floors are worded the same everywhere. Anything left over from the
  family whose binder the core came from was removed, and the text was checked for plain
  language.
- **When your binder was generated**, checks ran on your copy: no web address anywhere, nothing
  left from that family, and every fill-in slot checked against your answers. The pages whose
  text depends on your answers were then reviewed again by the AI for consistency, numbers,
  stray names and plain language.

Anything the review could not fix is listed on the **review notes** page. **The known limit:**
if every public source is wrong in the same way, an AI review will not catch it. Where this
binder and a professional disagree, **the professional is right**. While normal services work,
use them.

## Sources, and why there are no links

There is no internet in the situation this binder is for, so it never prints a web address.
Each fact names its source by title, publisher and date in the sentence, preferring US federal
agencies (CDC, EPA, FDA, USDA, NWS, FEMA, CPSC, OSHA, FCC), then national societies and
manufacturers, then university Extension services. **Laws, licences and codes** appear only in
boxes marked **Before the collapse**: they are true while government works, and they never
decide a survival procedure.

## Decision cards and floors

Some choices have no single right answer: running a heater overnight, keeping fuel in the
garage, using an expired medicine. For each, a **decision card** (Section 30) explains the
hazard, why the maker or agency set its rule, how people actually get hurt, what makes it safer,
and the options. **Your household chooses**; your answer is printed wherever the subject comes
up, or "not decided yet". The choice, and the responsibility for it, are yours.

A few things are **floors**, not choices: where there is no mitigation and the failure is death
or permanent injury without warning, such as an engine running indoors or mixing bleach with
ammonia. They are stated as rules with the reason, the same words every time, and no options
box. → 30-01

## Small, Large and Everything

{{#if size.everything}}**This is the Everything copy.**{{else}}{{#if size.large}}**This is the Large copy.**{{else}}**This is the Small copy.**{{/if}}{{/if}}

- **Small** has every page, explainer, card, condition and gear module, the national region
  appendix and all plant plates. Each citation shows title, publisher and date; no source
  document is bound inside. It carries only this kit's own text and public-domain material, and
  fits on any phone.
- **Large** is Small plus the full documents cited by the life-safety sections (medical
  conditions, water, food storage and canning, fire and fuel, heating, power, first aid, hazards, kids, CBRN, and the
  decision cards and floors), each bound behind the page that cites it. It also carries
  topographic maps for your home county and destinations, and for the counties along your routes
  if you chose them. Documents cited only by other sections are listed as "in the Everything
  download". It needs a phone with room to spare.
- **Everything** is Large plus every other cited document. It is the largest file and is meant
  for a laptop.
- In Large and Everything, the documents are fetched for your household when you download. Some
  publishers refuse automatic fetching: those are listed on the **Sources not captured** page.
  The page that cites each one still stands on its own text; save the document yourself while
  the internet works.
- A Small copy can be upgraded to Large or Everything later from your saved answers file and
  this binder file, without the pages being written again.

## Changing it later

- **Your answers are never stored by us.** If you chose to save them, they are in a file called
  `profile.json` on your own device. Keep a copy somewhere safe.
- **To add a medical condition, a person, a pet or new gear:** open the settings page, load your
  `profile.json`, change the answer, and generate again. The whole condition library stays in the
  app, so a condition added later gets its full module. A condition that is not in the library
  has its own page: → 02-27.
- **To rebuild from scratch** (a new phone, a lost file): load `profile.json` and generate.
  Without the file, you answer the questions again.
- **Photos you add** to pages stay in your copy on your device and are never sent anywhere.

## This file is your private copy

{{#if size.large}}Your copy contains the full text of documents written by other people and
organisations, fetched for your personal use when you downloaded it. Those documents are
copyrighted by their publishers. **Giving this file to someone else copies their work without
permission and breaks copyright. Keep it within your household.**{{else}}Your Small copy carries
only this kit's own text and public-domain material, but it is still built from your household's
private answers. **Keep it within your household.**{{/if}} If a friend wants a binder, send them
to the settings page so they can make their own. → 00-09

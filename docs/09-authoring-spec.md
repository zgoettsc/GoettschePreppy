# Authoring spec: the contract between content and app

Every content worker and every app worker builds against this document. If something here is
ambiguous, the worker writes the question into its notes file (section 10) and makes the
conservative choice; it does not invent a new convention.

## 1. Kit sections

Section numbers follow the household binder where the subject is the same, so provenance stays
readable. Sections 28 to 30 are reused for the new libraries; 32 is new.

| No. | Folder | Contents |
|---|---|---|
| 00 | `00-front-matter` | Disclaimer, private-copy notice, install and charge discipline, how to use, quick reference, family plan, roles, map of the binder |
| 01 | `01-phase-playbooks` | Shelter in place, go/no-go, movement, establish, destinations, transition checklists |
| 02 | `02-medical-conditions` | Condition library: one page per module CL-01 to CL-26 (page 02-NN = CL-NN), plus 02-27 "a condition that is not in the library" |
| 03 to 27 | as the household binder | Core subject sections (water, food, fire and fuel, cooking, heating, power, lighting, clothing, medical and first aid, sanitation, security, comms, tools, weather and hazards, community, documents, kids, morale, master lists, depletion, skills, reference, acquisition checklist, CBRN) |
| 28 | `28-gear-reference` | Spec tables for common gear by class (power stations, panels and controllers, generators, portable heaters, radios, water filters) and how to read your own gear's label. Gear-specific procedures stay in their subject section (heaters in 08, generators in 09). |
| 29 | `29-explainers` | One page per explainer EX-01 to EX-15 (page 29-NN = EX-NN) |
| 30 | `30-decisions-and-floors` | 30-01 the floors; 30-02 to 30-25 decision cards DC-01 to DC-24 (page 30-(NN+1) = DC-NN) |
| 31 | `31-sere-field-reference` | Air Force Handbook 10-644, public domain, unchanged |
| 32 | `32-region-appendix` | Generated from `data/regions/`: one page per state plus DC, national plant and tree plates by ecoregion |

Section folder names for 03 to 27 and 31 are copied from the household binder.

**`data/page-plan.json` is the authoritative list of kit pages**: every household page that carries
over (`from_household`, with its `kit_id`) and every new page (`new_pages`). Kit ids keep the
household number so cross-references stay stable; a few slugs change to drop owner specifics, and a
few pages move: pets to 20-09, evaporative cooling pouches to 12-21, evacuating with medical needs
to 01-07. Household Section 02 pages have no kit page of their own; they are source material for
the condition library. When a household page cites `→ 02-06`, the kit page cites the library
module instead (→ 02-03 anaphylaxis, → 02-04 food allergy, → 02-01/02-02 type 1 diabetes, → 20-09
pets, → 12-21 pouches, → 01-07 evacuation). Cross-references to dropped household pages (28, 29,
30, 02-11, 05-20) are removed or pointed at the nearest kit page.

## 2. Page file

`content/sections/<folder>/<NN-MM-slug>.md`, YAML frontmatter then Markdown body.

```yaml
---
id: 08-01-heating-one-room          # NN-MM-slug, stable
section: 08-heating-and-cold-weather-shelter
title: "Heating one room instead of the house"
version: 1
revised: 2026-11-16
layer: core                          # core | region | household | condition | gear | explainer | card | floors | generated
danger_level: critical               # none | caution | critical
phase: [A, B, C]
tags: [heat, warm room, carbon monoxide]
derived_from: [08-01-heating-one-room]   # household-binder page ids this was written from ([] if new)
sources: [cdc-co-prevention, nws-wind-chill]   # keys in sources/index.json; never URLs
related: [08-02-carbon-monoxide-safety, 30-02-dc01-unvented-heater-overnight]
cards: [DC-01, DC-02]                # decision cards this page relies on
explainers: [EX-03]                  # explainers this page assumes
promote_when: [has.cold_winters]     # flags that move the page to the front of its section; [] = normal order
photo_slots:                         # places the household may attach its own photo (never uploaded)
  - { id: warm-room, caption: "Our warm room: heater spot, both vents, the barrier, the CO alarm" }
figures: [fig-warm-room-layout]      # ids in figures/index.json (requested, drawn later)
plates: []                           # plant keys (region and foraging pages)
condition: null                      # CL-NN on condition pages
gear: null                           # GM-NN on gear pages
explainer: null                      # EX-NN on explainer pages
card: null                           # DC-NN on card pages
review_pass: null                    # set by the review pipeline, never by authors
---
```

`schema/page.schema.json` is authoritative; `npm run validate` checks every page.

## 3. Body conventions

- **Opening.** A one-paragraph "What this page is for" in plain words, then, on critical pages, a
  `> **SAFETY**` callout with the floor(s) that apply, then the content.
- **Quick then detail.** Pages that someone will use during an emergency start with a numbered
  "Do this now" list that fits one phone screen, then the explanation.
- **Cross-references** are written `→ 08-02` (arrow, space, NN-MM). The renderer turns them into
  links and adds the short title. Never write a bare page title as a reference.
- **Citations** name the source in the sentence: "(CDC, Carbon Monoxide Poisoning Prevention,
  2024)". Never a URL, never "see the website", never "search for". The source's key goes in
  `sources:`.
- **Pre-collapse notes.** Law, licensing, codes and permits are true only while government works.
  Put them in a callout: `> **Before the collapse:** South Dakota requires ...`. Never let a law
  decide a survival procedure.
- **Decision cards.** Where a page touches a trade-off from `docs/05-decision-cards.md`, it says
  what the trade-off is in one sentence and inserts `{{choice DC-NN}}` (the household's choice,
  one line) with a `→ 30-NN` reference. It never states a different rule. It never presents the
  owner household's choice as the answer.
- **Floors** (`docs/05-decision-cards.md`, part B) are stated as rules with the reason, on every
  page where they apply, worded the same way each time (copy from `30-01`).
- **No derived dosing.** Never calculate, adjust or suggest a dose, ratio or schedule for a
  person's own medication. Published tables are printed as published with the publisher named.
- **Numbers.** Every number on a critical page must come from a cited source, a profile value, or
  a derived value in `schema/context.json`. If you cannot source a number, write the method and
  leave the number out.
- **Writing level.** The reader has never prepped. First use of any term is explained in the
  sentence or points to an explainer (`→ 29-NN`). Short sentences. Concrete. No jargon without a
  definition. No "obviously". No brand loyalty: name gear by class first, model second.
- **Tone.** Calm, direct, honest about limits. Not militaristic, not alarmist, not cute.
- **No owner household.** Nothing from the owner's family may appear in a kit page: no names,
  places, phone numbers, gear models chosen for their reasons, house layout, destinations,
  rules they decided. `npm run validate` fails on the token list in `scripts/owner-tokens.json`.
  Use the household's own values through slots instead.
- **No links.** No URL, no `www.`, no Markdown link to anything outside the binder. The validator
  fails on them.

## 4. Template syntax

Rendered in the browser before Markdown, by `app/lib/template.js`. Only these forms exist.

| Form | Meaning |
|---|---|
| `{{ path }}` | A value from the context (`schema/context.json`). Missing or empty prints a fill-in blank `__________` with a small "(fill in)" mark. |
| `{{#if flag}} ... {{else}} ... {{/if}}` | Conditional on a flag from `schema/context.json`. `!flag` negates. No other expressions. Nesting allowed. |
| `{{#each list as x}} ... {{x.field}} ... {{/each}}` | Repeat over a list from the context (`members`, `pets`, `destinations`, `meds`, ...). Empty list renders the `{{else}}` part if present. |
| `{{choice DC-NN}}` | One line: the household's chosen option label, or "Not decided yet → 30-NN". |
| `{{card DC-NN}}` | The full choice box (used only on the card page itself and the summary page). |
| `{{photo slot-id}}` | The household's photo for that slot (from `photo_slots`), or an empty frame with the caption and "Add a photo in the app". |
| `{{figure fig-id}}` | A figure from `figures/`. Unknown ids render as a captioned placeholder and are listed in the review notes. |
| `{{plates}}` | The page's `plates:` rendered as identification plates. |
| `{{ai block-id}}` | A block the generation model writes at generation time from the spec in `content/ai-blocks/<block-id>.md`. Allowed only on `household` pages. |

Rules for authors:

- **Everything is always included.** Owner decision: the binder has everything. Never use `#if`
  to remove a whole topic; use it to tailor wording, examples and order. A household without a
  pool still gets the pool water page; it just is not promoted.
- **Every flag and path must exist in `schema/context.json`.** If you need one that does not
  exist, use the nearest existing one and write the request in your notes file.

## 5. Layers in practice

| Layer | Author does | Generation does |
|---|---|---|
| core | Writes the full page with slots and flags. | Fills slots; nothing else. |
| region | Writes the method text and inserts `{{ region.home.* }}` values; the national appendix pages (32) are produced by `scripts/build-region-pages.mjs`. | Fills slots. |
| household | Writes a template with slots, `#each`, and at most a few `{{ai}}` blocks for prose that cannot be templated (destination narrative, route hazards summary). | Fills slots, writes ai blocks. |
| condition, gear, explainer, card, floors | Full frozen text with slots for the household's own items. | Fills slots. |
| generated | Nothing; scripts build these. | Nothing. |

## 6. Sources

- `sources/index.json` holds every source: `key`, `title`, `org`, `date`, `licence_class`
  (`public-domain`, `open`, `restricted`, `blocked`), `url` (used only by the fetcher), `cited_by`.
- Seeded from the household binder's 391 sources. Reuse an existing key whenever the same
  document is meant.
- A worker that needs a new source adds it to `sources/additions/<worker-id>.json` (same fields),
  checked: real document, publisher named, licence class judged from the publisher's terms. The
  coordinator merges additions.
- Prefer, in order: US federal (public domain), the condition's national society or the
  manufacturer, university Extension, other. A page marked critical cites at least one federal or
  manufacturer or national-society source.

## 7. Region data paths (for region-layer authors)

`region.home` and each `region.dest[i]` expose the fields listed in `schema/context.json` under
`region`: state name, county name, hardiness zone, first and last frost dates, January mean low,
July mean high, record low and high, annual precipitation, snowfall, the hazard list with a
1-to-3 rating each (tornado, blizzard, ice storm, flood, wildfire, earthquake, hurricane, extreme
heat, extreme cold, drought, volcano, tsunami, landslide), NWS office name, NOAA Weather Radio
transmitters with frequency and SAME code, state emergency management agency name, poison
control (national, constant), ecoregion, and the plant and tree key lists for that ecoregion.

## 8. Figures and photos

Request a figure by listing an id in `figures:` and writing a one-line description in your notes
file (`figure: fig-id — what it must show`). The figures worker draws SVGs or sources public-domain
plates. Photo slots are free to add on pages where a household photo would prevent a mistake.

## 9. Section 31

Section 31 is copied from the household binder by `scripts/import-section-31.py` with frontmatter
converted. Nobody edits it by hand.

## 10. Worker notes

Every worker writes `notes/workers/<worker-id>.md` with: pages written, flags or paths requested,
figures requested, sources added, questions, and anything it could not finish. The coordinator
reads these and nothing else to integrate.

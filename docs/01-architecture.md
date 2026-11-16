# Architecture

## 1. The three layers, and two libraries

| Layer | What it is | Who writes it | When |
|---|---|---|---|
| **L0 Core** | Method and fact that are true everywhere: water, food storage and preservation, fire and fuel, heating a room, carbon monoxide, power basics, lighting, clothing, first aid, sanitation, tools, security principles, communications principles, kids, morale, depletion math, skills, CBRN basics, the Air Force survival handbook. | Re-authored once from the household binder (249 pages tagged core in `03-layer-map.md`), then frozen and versioned. | Build time. Ships to every household unchanged. |
| **L1 Region** | Everything that depends on where you are: climate normals and growing season, hazards, hardiness zone, poison plants and look-alikes, safe plants, firewood trees, game and fish, NWS office and transmitter frequencies, SAME codes, state emergency contacts, state law one-liners (as pre-collapse notes). | Curated datasets, not model memory. Assembled into pages by templates. | Build time for the national appendix. Generation time only to promote the home base and destinations. |
| **L2 Household** | Family members and ages, contacts, meeting places, destinations and routes, roles, go-bags, inventory, the house (water, heat, fuel, warm room, shelter spots), gear owned. | The model, from templates and the profile, with every number traceable to a profile field or a dataset row. | Generation time. |
| **Condition library** | About 26 medical condition modules at WebMD level. The whole library is in every binder; selected conditions are promoted to the medical section's front and feed the medical go-kit, the power-for-medical page and the device-protection page. | Authored once, frozen. Slots for "my meds". | Build time; selection at generation time. |
| **Gear library** | Modules for classes of gear: portable propane heater, wick kerosene heater, ducted diesel/kerosene heater, wood stove, power station and panels, generator, well, pool, septic, trailer, firearms platform. Each has a spec table keyed by common models. | Authored once. Model slots from a fixed spec table; unknown models get a blank spec row the household fills from the label. | Build time; selection at generation time. |

The explainers (`06-explainers.md`) are core pages. The decision cards (`05-decision-cards.md`)
are core pages with one slot each: the household's choice.

## 2. What the model does, and does not do

Does: select modules from the profile; fill slots; write the household pages in the binder's voice
from templates; promote the home base and destination regions; write the index and cross-references;
run the review passes.

Does not: author a safety procedure; recall a plant, law, phone number, dose or device limit from
memory; relax a floor (`05-decision-cards.md`, part B) because the household asked.

Enforced by: structured outputs validated against `schema/profile.schema.json` and per-page slot
schemas; a frozen template corpus in a cached system prompt; a post-check that every number on a
page marked `danger_level: critical` traces to a profile field, a dataset row or the template text.

## 3. Generation pipeline

1. **Settings page** (static, in the browser). Collects the profile. Shows the never-stored notice
   on every step. Validates against the schema. Offers "save my answers to a file on this device".
2. **Generate.** Browser sends the profile and access key to the relay. Relay checks the key hash,
   increments a counter, forwards to the Claude API with the cached template corpus, streams the
   result back. The browser assembles pages as they arrive.
3. **Review passes** (same relay, same statelessness), run on the assembled binder before it is
   shown: (a) slot and schema validation, (b) consistency pass across pages (one rule, one number,
   one name everywhere), (c) source-trace pass on critical pages, (d) leftover-personal-token scan
   (nothing from the owner's household may survive into anyone else's binder), (e) readability pass
   against the novice level. Findings are fixed automatically where mechanical, otherwise the page
   is marked and listed on a "review notes" page in the binder.
4. **Fetch at download.** The browser asks the relay for each cited source document not already in
   the public kit. The relay fetches it from the publisher and streams it through without storing
   it. The browser binds the document behind the citing page. Hosts that refuse automated fetching
   are listed on the "sources not captured" page with the kit's own summary text in place.
5. **Download.** One HTML file. The notice is shown again. Nothing remains on the server.

A full run is 10 to 20 minutes with the tab open; the page says so and shows progress.

## 4. The output: one offline app file

Same family as the household binder's phone app: a single HTML file with every page, every bound
source (PDF pages rendered to images or text), every plate and figure inline, full-text search, a
region picker for the national appendix, a condition picker for the library, and a PDF export
button that produces the printed volumes with the sources behind each tab. Expect 250 to 400 MB
with sources; the download screen shows the size before fetching and offers "pages only" as a
smaller first download.

Install guidance is the first page after the disclaimer and notice: how to keep the file on a phone
and a laptop, how to open it with no connection, why a printed copy still matters, and a charging
discipline card.

## 5. Privacy architecture

- No application server, no database, no analytics, no cookies.
- Relay: one edge function. Inputs: access-key hash check, request forwarding, source fetch
  pass-through. State: a per-key request counter. Logs: none beyond the counter. Source code
  published in this repository (`worker/`).
- The one unavoidable third party is the model provider. The notice says so in plain words and does
  not promise more than is true.
- Household photographs (see `08-pictures-plan.md`) are attached in the browser and never leave it;
  they are not part of the generation request.

## 6. Hosting and cost

- Static settings page and renderer on GitHub Pages or Cloudflare Pages.
- Relay on Cloudflare Workers (free tier is enough for a handful of friends).
- Generation: assume 300 generated or slot-filled pages at about 1,500 output tokens each, plus the
  review passes, on an Opus-class model. Order of magnitude $15 to $25 per binder at current list
  prices; a Sonnet-class model for slot-filling pages would roughly halve it. Synchronous streaming,
  never the Batch API (batch results are retained by the provider for weeks, which is storage).
- Source fetch: bandwidth only.

## 7. Repository layout (target)

```
core/            L0 pages, same frontmatter and validator as the household binder, plus
                 `layer`, `slots`, `cards`, `review_pass` fields; `verified_by_human` removed
conditions/      one folder per module; module.md + slots.json
gear/            one folder per module; module.md + specs.json (keyed by model)
regions/         national datasets: climate, hazards, zones, plants (with plates), trees,
                 nws, same-codes, state-contacts, state-law-notes; one JSON per dataset
explainers/      EX pages (core)
cards/           DC pages (core, one slot each)
schema/          profile.schema.json, page.schema.json, slot schemas
sources/         index.json (URLs live here only), public-domain archive shipped with the kit
app/             settings page, renderer, PDF export
worker/          relay function
scripts/         build, validate, review passes, archive/fetch, plates pipeline
tests/           the owner's household as the first test profile; expected-output checks
```

## 8. Phases

1. **React to these documents.** Owner reviews `00` to `08`; decisions O1 to O6 closed.
2. **De-personalise and re-author the core.** 249 pages; 44 rewrites, 60 templates, remainder ship
   after de-personalising. Parallel workers by section with exclusive page ownership, the same
   method as the fact-check and fix pass. Validator extended to fail on any owner token.
3. **Explainers, decision cards, condition library, gear library.** New writing; smaller than
   phase 2.
4. **Region datasets and plates.** Start with the owner's region as the known-good case, then the
   whole country by state and ecoregion. Plates are the slow part.
5. **Settings page, relay, renderer, review passes.** Regenerate the owner's binder from a profile
   and compare.
6. **Pilot with three to five friends in different regions.** Their binders get the automated
   review passes; the owner reads the review-notes page of each.

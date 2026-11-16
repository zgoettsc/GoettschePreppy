# GoettschePreppy

A build-your-own, off-grid survival reference for US households, generated from a profile the
household fills in and delivered as a single offline app file. Derived from one family's
391-page SHTF binder after a full fact-check and fix pass (November 2026).

**Status: design phase.** Nothing here generates a binder yet. The documents in `docs/` are the
decisions and specifications to react to before any page is re-authored.

## What it is, in one paragraph

A friend opens a hosted settings page, enters an access key, answers questions about where they
live, who is in the house, what gear they own, which medical conditions apply, and how much risk
they accept on about two dozen named trade-offs. Nothing they type is stored anywhere. Their
answers go, once, to an AI model that assembles a binder from a verified core, national region
datasets, a condition library and gear modules, then runs automated review passes. The result is
one HTML file they download and keep on their phone and laptop. It works with no internet, contains
every source document inline, has no links anywhere, and can export itself to PDF for printing.

## Repository layout

```
docs/
  00-decisions.md          Owner decisions that bound the design (the "we make the rules" log)
  01-architecture.md       Layers, generation pipeline, privacy architecture, hosting, cost
  02-profile-schema.md     Every question the settings page asks, and why
  03-layer-map.md          All 391 household-binder pages tagged core / region / household /
                           condition / gear / generated / drop, with the action for each (generated)
  04-condition-library.md  The medical condition modules: template and the first 26 conditions
  05-decision-cards.md     Risk trade-offs the household decides, and the floors nobody can switch off
  06-explainers.md         Novice explainer pages (fuels, batteries, CO, chlorine, meds, radio ...)
  07-sources-and-fetch.md  Sources inline, no links, per-user fetch at download, the private-copy notice
  08-pictures-plan.md      Figures, diagrams and the household's own photos
schema/profile.schema.json The profile the settings page produces (JSON Schema, draft 2020-12)
data/layer-map.json        Machine-readable form of docs/03-layer-map.md
scripts/build-layer-map.py Regenerates the layer map from the household binder's manifest.json
```

Planned (not yet present): `core/` (L0 pages), `regions/` (L1 datasets), `conditions/`,
`gear/`, `app/` (settings page and binder-app renderer), `worker/` (stateless generation and
fetch function), `scripts/` (build, validate, review passes).

## Licence

Code: MIT (`LICENSE`). Written content: CC BY-NC-SA 4.0 (`LICENSE-CONTENT.md`). A generated
binder additionally contains third-party documents fetched for that household's personal use; the
in-app notice (`NOTICE-TO-USERS.md`) tells the household the copy is private and not to be shared.

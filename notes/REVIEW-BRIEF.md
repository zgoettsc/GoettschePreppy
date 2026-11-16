# Review brief (kit review pass, owner decision G6: AI reviews everything)

You review and fix a set of GoettschePreppy kit pages. You are the last check before strangers rely on
these pages with no internet and no professional. Read: notes/WORKER-BRIEF.md (authoring rules),
docs/09-authoring-spec.md, docs/05-decision-cards.md (cards DC-01..DC-29 and the floors), the
floors page content/sections/30-decisions-and-floors/30-01-the-floors.md, schema/context.json, and
notes/COORDINATOR.md (open items; fix any that concern your pages).

Kit repo: /home/user/goettschepreppy. Household binder (READ ONLY): /home/user/SHTF; its archived
source documents are in /home/user/SHTF/sources/archive/<key>.{md,pdf} (look up a kit source key in
/home/user/goettschepreppy/sources/index.json; household keys match). Do not run git. Never rewrite
.gitignore. Edit ONLY your assigned pages, plus your findings file and sources/additions/<your-id>.json.

## Passes, per page
1. **Source trace.** Every number, threshold, time, temperature, ratio, distance and dose-like figure on
   `critical` and `caution` pages must be supported by a source in the page's `sources:` that you have
   actually read (archive copy, or fetch it). If unsupported: find and cite a source that supports it,
   correct it, or remove the number and keep the method. Do not leave an unsupported number on a
   critical page. Spot-check `none` pages.
2. **Consistency.** Floors worded as on 30-01; card references match the card's options and page ids
   (DC-NN is on 30-(NN+1)); no page states a rule different from a card or floor; the same fact has the
   same number across the kit (check related pages with grep: water per person, bleach ratios, CO alarm
   placement, generator distance, insulin storage, fuel shelf life "months, not years", propane 170 cu ft).
3. **Owner residue.** Nothing from the owner household (names, places, their gear, their rules stated as
   defaults, their quantities). Section 32 and 31 excepted.
4. **Novice readability.** Terms defined or pointed to an explainer; emergency steps short; no jargon walls.
5. **Rendering.** `node scripts/validate.mjs <your sections>` 0 errors, and render your pages against the
   three test profiles (see scripts/test-generate.mjs or app/lib/template.js `render` with
   `buildContext` from app/lib/context.js and app/build/kit.json) with no leftover `{{`, no broken tables,
   no sentence that reads wrong when a value is blank.

When a page passes, set its frontmatter `review_pass: { date: "2026-11-16", passes: [source-trace,
consistency, owner-residue, readability, rendering], notes: "<one line>" }` and bump `version` by 1 if you
changed content.

## Findings file
`reviews/2026-11-16-kit-review/<your-id>.md`: one line per change (page, what, why, source), then a list
of things you could not resolve (with the reason) and any owner questions. Final message to the
coordinator: 5 to 10 lines with counts (pages reviewed, numbers verified, numbers fixed/removed,
unresolved).

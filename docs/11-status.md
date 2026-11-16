# Status (2026-11-16)

## What is built

| Part | State |
|---|---|
| Content | 441 authored pages in 32 sections plus 52 generated region pages; every authored page (outside the verbatim Section 31 and generated Section 32) carries an AI `review_pass` from two review waves, a kit-wide consistency sweep and targeted re-checks |
| Decision cards | 31 cards (DC-01 to DC-31) and the floors page |
| Condition library | 26 modules plus "a condition not in the library" |
| Explainers | 15 novice explainers |
| Region data | All 3,144 US counties: climate, frost, zone, NWS office, NOAA Weather Radio, FEMA National Risk Index hazards, ecoregion, sun hours, state emergency agency |
| Plants | 321 species (deadly, edible, firewood) with 599 public-domain photographs for 285 species, mapped to 106 ecoregions |
| Figures | 112 (diagrams and public-domain plates); 110 of 162 requested figures render |
| Sources | 876 entries; cited documents by licence class: public domain 358, restricted 354, blocked 55, open 3 |
| Settings page | Nine-step walkthrough, never stores answers, save/load answers file without the access key, three download sizes |
| Generator | Template engine, context builder, review passes, Small/Large/Everything, PDF sources rendered to page images, maps, upgrade without regenerating |
| Relay | Cloudflare Worker: key check, model lock, streaming pass-through, allowlisted source and map fetch, per-key count only |

Measured sizes from the current build: Small 42 to 56 MB; Large 238 to 629 MB (two maps; 195 of 575 documents measured, the rest averaged); Everything about 0.5 to 1 GB.

## Tests (all passing at the last run)

```
node scripts/validate.mjs            # 441 pages, 0 errors
npm run test:generate                # unit, generation (dry-run relay), offline browser checks
node app/settings/tests/walkthrough.mjs
npm run test:worker                  # 53 relay tests
```

## What the owner does to go live

Follow `docs/10-deploy.md`: create the Cloudflare account, set the two secrets (Anthropic API key,
access-key hashes), deploy the Worker and Pages, set `relayBase` in `app/settings/config.js`, make
one access key per friend with `scripts/make-access-key.mjs`. Then make one real binder for the
owner's own household and read it before giving any friend a key: no real generation (with the
live model) has been run yet; everything so far used the dry-run relay.

## Open items

1. **Antibiotic doses:** verified. All 133 dose rows on 12-22 and 37 figures on 12-23 were checked
   against the complete source documents; every published number matched; 21 wording and citation
   fixes and one label strength were corrected (reviews/2026-11-16-kit-review/V1.md).
2. **Aspirin (G27):** the AHA/Red Cross line is marked "reported, not read at source"; nobody could
   open an AHA page from here.
3. **Sources that could not be read from this environment** (FSIS, NHTSA, NFPA, AHA, ATF, parts of
   CDC and Red Cross): their numbers were removed or replaced. Re-check when reachable, especially
   the ATF suppressor letter (14-10) and FSIS food temperatures.
4. **Figures:** 52 requested figures still open (`figures/REQUESTS.md`), mostly FEMA shelter
   cutaways and other government art not reachable here.
5. **Large size:** the upper estimate (629 MB) is above the 300 to 400 MB target. Measure a real
   Large build; if it is too big, lower the page-image resolution only after checking small print.
6. **Region data:** state emergency agency names come from a 2016 FEMA list with 15 manual
   updates; `is.humid` is always false (no humidity field yet).
7. **Owner questions still open** (from reviewers' findings files):
   - DC-16: confirm the third option, a published child antibiotic dose from 12-22.
   - DC-25: should a medic-trained member get the 2-to-6-hour conversion window?
   - Thyroid missed dose (ATA allows doubling, MedlinePlus says never).
   - Dietary Guidelines edition for calorie math (2020-2025 used).
   - One canning row still cites South Dakota State Extension.
   - CL-02 names Dexcom, Omnipod and LoopDocs as one-maker examples.
   - Clothing counts per person kept as suggestions.

Full working notes: `notes/COORDINATOR.md` and `reviews/2026-11-16-kit-review/`.

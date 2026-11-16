---
id: 30-14-dc13-drinking-pool-or-surface-water
section: 30-decisions-and-floors
title: "DC-13. Drinking water from a pool, hot tub or untreated surface source"
version: 2
revised: 2026-11-16
layer: card
danger_level: critical
phase: [A, B, C]
tags: [decision card, water, pool, hot tub, surface water, distillation, chlorine, filter, boil]
derived_from: [03-03-pool-water-desalination, 03-04-purifying-water, 03-08-keeping-water-from-going-bad]
sources:
  - cdc-how-to-make-water-safe-in-an-emergency-5d78b5
  - us-epa-emergency-disinfection-of-drinking-water-6aa91f
  - fema-477-food-and-water-in-an-emergency
  - cdc-water-disinfection-for-travelers-cdc-yellow-book-df8e45
  - awwa-water-technology-distillation-ensures-safe-drin-7ba482
  - cdc-yellow-book-travelers-diarrhea-oral-rehydration-a1b9d8
related: [03-03-pool-water-desalination, 03-04-purifying-water, 03-05-rain-and-snow-water, 03-07-testing-water, 03-09-filter-care-and-maintenance, 12-05-common-illness-and-dehydration, 29-05-ex05-chlorine-products, 29-06-ex06-water-words, 30-24-dc23-extra-strength-chlorination, 30-01-the-floors]
cards: [DC-13, DC-23]
explainers: [EX-05, EX-06]
promote_when: [has.pool, has.hot_tub]
card: DC-13
options:
  - id: distill-only
    label: "Distil before drinking"
    summary: "Water from a pool, hot tub or untreated stream, pond or lake is drunk only after distilling (boil it and collect the steam). Undistilled, it is used for flushing, washing and cleaning only."
  - id: filter-and-chlorinate
    label: "Fresh pools: filter and chlorinate"
    summary: "A freshwater (not salt) pool known to hold no algaecide or other additive may be drunk after settling, filtering and disinfecting by the published method. Salt pools and hot tubs still need distilling; surface water still needs distilling."
  - id: drink-treated-surface-water
    label: "Surface water through the treatment ladder"
    summary: "Streams, ponds and lakes away from obvious fuel, chemical or farm runoff are drunk after the full ladder: settle, filter, then boil or disinfect by the published method. Fresh pools as in the option above; salt pools and hot tubs are still distilled."
settings_summary: "A swimming pool or a nearby stream can look like a large water supply. Germs in water (bacteria, viruses, parasites) are killed by boiling, and most by chlorine used as CDC and EPA describe. Chemicals are not. Pool water holds chlorine, stabilizer, often algaecide, and in a salt pool, salt that no boiling or filter removes. Hot tubs hold bromine and body oils. Streams and ponds can carry fuel, farm or industrial runoff. CDC says water containing fuel or toxic chemicals cannot be made safe by boiling or disinfecting. FEMA and the Red Cross say not to drink from pools or spas. Distillation (boil and catch the steam) removes salt and most chemicals, but it is slow and uses fuel. What helps most: pool and hot-tub water for flushing and washing, stored water for drinking (removes most of it); distil what you drink from them (reduces it a lot)."
review_pass: null
---

# DC-13. Drinking water from a pool, hot tub or untreated surface source

**What this page is for.** When stored water runs low, a pool, hot tub or nearby stream can
look like the answer. This card separates the germ problem, which boiling and chlorine solve,
from the chemical problem, which they do not, and asks the household to decide which sources it
will drink and how.

> **SAFETY.** Bleach or pool shock is never mixed with ammonia, acids or other cleaners
> (floor, → 30-01). **Salt water is never drunk unless distilled**: boiling, chlorine and
> ordinary filters leave the salt in, and salt water makes dehydration worse. Water that may
> hold fuel or toxic chemicals cannot be made safe by boiling or disinfecting (CDC).

## 1. The thing, in plain words

Read → 29-06 for the water words.
- **Pool water** has chlorine (or salt that a machine turns into chlorine), a stabilizer called
  cyanuric acid, acid or base to adjust pH, and often an **algaecide** (some contain copper).
- **Hot-tub water** is hot and full of skin oils, and usually treated with bromine.
- **Surface water** is any stream, pond, lake or ditch.
- **Boiling** and **disinfecting** (bleach, pool shock dissolved by the published method,
  → 29-05) kill germs. **Filtering** removes dirt, parasites and most bacteria, not viruses.
  **Distilling** means boiling water and collecting the steam, which leaves salt and most
  chemicals behind in the pot.

{{#if has.pool}}Your pool holds about {{ dwelling.pool_gallons }} gallons.{{#if has.saltwater_pool}} It is a salt pool: drinking it always needs distilling.{{/if}}{{/if}}

## 2. The rule, and why it was set

- CDC's emergency guidance: boil water, or disinfect it with unscented bleach at the published
  dose after letting cloudy water settle and filtering it; and **water contaminated with fuel or
  toxic chemicals will not be made safe by boiling or disinfection** (CDC, How to Make Water Safe
  in an Emergency; EPA, Emergency Disinfection of Drinking Water).
- FEMA and the Red Cross list **swimming pools and spas** among the water in a home that **should
  not be used** for drinking, and say to use salt water only if you distil it first (FEMA and
  American Red Cross, Food and Water in an Emergency).
- The same booklet: distillation "will remove microorganisms that resist these methods, as well as
  heavy metals, salts, and most other chemicals" (FEMA and American Red Cross; see also Water
  Technology, Distillation Ensures Safe Drinking Water During an Emergency, written by a distiller
  maker).

**Why:** pool chemicals are made for swimming water, not for drinking water. Surface water's germs are well understood and handled by the
methods above; its chemicals depend on what lies upstream, which you usually cannot know.

## 3. How it actually hurts people

- **Germs from untreated surface water**: diarrhoea and vomiting from bacteria, viruses and
  parasites such as Giardia and Cryptosporidium. In a baby, an elder or someone with diabetes,
  diarrhoea quickly becomes dangerous dehydration (CDC Yellow Book, Travelers' Diarrhea; → 12-05).
- **Salt**: drinking salt-pool water pulls water out of the body; thirst gets worse, not better.
- **Chemicals**: copper algaecide, stabilizer, and fuel or farm chemicals in runoff are not removed
  by boiling or chlorine; some build up over weeks. A child, smaller and drinking more for its
  size, gets the larger share.
- **Cryptosporidium** resists ordinary chlorine; boiling or a fine filter is needed (CDC Yellow
  Book, Water Disinfection for Travelers).

## 4. What makes it safer

**Removes most of the risk**
- **Use pool and hot-tub water for flushing, washing and cleaning**, and keep stored, rain or snow
  water for drinking (→ 03-05). This alone can stretch drinking water a long way.
- **Distil** pool, hot-tub or suspect surface water before drinking (→ 03-03). Distilling removes
  salt and most chemicals, but not those that boil off with the steam, so water with a fuel smell
  or sheen is not used at all.

**Reduces it a lot**
- **Choose the cleanest source**: rain and snow first; flowing water upstream of roads, farms and
  buildings; never water with a fuel sheen or chemical smell.
- **The treatment ladder** for surface water: let it settle, pour off the clear part, filter
  through cloth, then through a filter with pores under 1 micron (most portable microfilters, CDC
  Yellow Book), then **boil** or **disinfect** by the published bleach dose and wait 30 minutes
  (CDC; → 03-04). Boil 1 minute at a rolling boil; above 5,000 feet, boil 3 minutes (EPA's line;
  CDC uses 6,500 feet; this binder uses the lower, safer figure).
  {{#if is.high_altitude}}**Your home is at about {{ region.home.elevation_ft }} ft: boil for 3 minutes.**{{/if}}
- For a freshwater pool: know exactly what has been added. No algaecide, no "multi-action"
  products.

**Reduces it a little**
- Activated carbon filters reduce some chemicals and taste.
- Test strips for chlorine and pH, if you have them (→ 03-07).

## 5. The options

**`distill-only`: Distil before drinking.**
You give up: easy volume; distilling is slow and burns fuel (→ 03-03). You accept: needing more
stored, rain and snow water.

**`filter-and-chlorinate`: Fresh pools: filter and chlorinate.**
You give up: certainty about what is in the water. You accept: drinking pool chemicals at low
levels for as long as the outage lasts. Salt pools, hot tubs and surface water are not covered.

**`drink-treated-surface-water`: Surface water through the treatment ladder.**
You give up: protection from chemicals upstream. You accept: that boiling or chlorine handles the
germs but not fuel or farm runoff, so source choice matters.

## 6. Our choice

{{card DC-13}}

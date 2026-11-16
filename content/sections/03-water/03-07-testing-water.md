---
id: 03-07-testing-water
section: 03-water
title: "Judging and testing water quality"
version: 2
revised: 2026-11-16
layer: core
danger_level: caution
phase: [A, B, C]
tags: [water, testing, nitrate, coliform, TDS, pH, well, source ranking]
derived_from: [03-07-testing-water]
sources: [cdc-guidelines-for-testing-well-water-382a7a, cdc-private-drinking-water-and-public-health-dc08f9, cdc-how-to-make-water-safe-in-an-emergency-5d78b5, us-epa-national-primary-drinking-water-regulations, us-epa-emergency-disinfection-of-drinking-water-6aa91f]
related: [03-03-pool-water-desalination, 03-04-purifying-water, 03-05-rain-and-snow-water, 03-08-keeping-water-from-going-bad, 03-10-well-water-without-power, 12-05-common-illness-and-dehydration, 17-03-floods, 20-01-toddler-and-infant-needs, 20-05-infant-feeding, 29-06-ex06-water-words]
cards: []
explainers: [EX-06]
promote_when: [has.well, has.infant]
photo_slots: []
figures: []
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: { date: "2026-11-16", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "Nitrate 10 mg/L sourced to EPA NPDWR (as nitrogen); CDC retest triggers corrected; boiling-nitrate wording tied to EPA; destination water source slot." }
---

# Judging and testing water quality

**What this page is for.** How to rank water sources from bad to worse, what a real test can
tell you, and which tests to buy now while labs and shops are open.

> **CAUTION.** You cannot see, smell or taste the things that matter most: bacteria, nitrate
> and most chemicals. **Clear water is not safe water** (→ 29-06). Treat every unknown source
> as contaminated and disinfect it (→ 03-04). This page helps you choose between sources; it
> is not a way to declare water safe by looking at it.

## Do this now

1. **Test now, while labs exist.** If you have a well or might ever use one, get a baseline
   test through a **state-certified lab** for **total coliform bacteria, nitrate, total
   dissolved solids and pH**: the CDC's yearly list (CDC, Guidelines for Testing Well Water).
   Your county or state health department can name a certified lab.
2. **Nitrate matters most for infants.** EPA says infants under six months who drink water
   with nitrate above the limit can become seriously ill and, untreated, may die ("blue-baby
   syndrome": their blood cannot carry oxygen properly). Know the number before you ever mix
   formula with well or surface water. **Boiling does not remove nitrate** (EPA: boiling does
   not remove salts or most chemicals), and because some water boils away, what is left is
   slightly stronger.{{#if has.infant}} You have an infant: this is your
   most important water test.{{/if}}
3. **Buy test strips now** (free chlorine, pH, nitrate, hardness) and a pocket TDS meter. They
   are cheap, small, and impossible to buy later.
4. **At a new site with a well**, the first job is a coliform and nitrate test. Treat every
   gallon until you have the result (→ 03-04), and carry the kit so you can test on the first
   day. Record it below.
5. **When in doubt, distil** (→ 03-03). It is the only home method that deals with salt, most
   chemicals and germs in one step.

## What testing can and cannot tell you

**Private wells are not regulated.** The EPA's public-water rules do not apply to them;
nobody checks or treats that water but you (CDC, Private Drinking Water and Public Health).
The CDC recommends testing a well **at least once a year** for **total coliform, nitrate,
total dissolved solids and pH**, and testing again when someone in the house becomes pregnant
or a child joins the household, after flooding or nearby land disturbance, after well repairs,
or when the water's taste, color or smell changes.

| Test | What it means | Why it matters |
|---|---|---|
| **Total coliform** | Indicator bacteria. If they are present, harmful bacteria, viruses or parasites probably are too | The disease test. Positive means do not drink it untreated |
| **Nitrate** | Runoff from fertilizer, animal waste, septic systems, sewage (CDC; EPA) | **Dangerous to infants.** A real risk in farm country |
| **TDS** (total dissolved solids) | How much salt and mineral is dissolved in the water | Tells you whether distilling is needed (pool water, brackish sources) |
| **pH** | How acidic the water is | Affects pipe corrosion and how well chlorine works |

**Disinfecting does not remove nitrate, salts or most chemicals** (EPA, Emergency Disinfection
of Drinking Water). Boiling leaves them in, slightly concentrated as water boils off. That is the most dangerous misunderstanding in
emergency water, and it is why nitrate and TDS deserve a real test.

### Well test record

Fill this in at the wellhead, for your well or any well you use.

{{#each destinations as d}}**{{ d.name }}** ({{ d.county }}, {{ d.state_name }}): water source {{ d.water_source_text }}
{{/each}}

- Well: __________ Date sampled: ________ Lab or kit: ________
- Total coliform: ☐ absent ☐ PRESENT (treat all water until it is fixed, → 03-04, → 03-10)
- Nitrate: ________ mg/L. **Over 10 mg/L (EPA's drinking-water limit, measured as nitrogen)
  is not safe for an infant's formula or feeding** (US EPA, National Primary Drinking Water
  Regulations). Check which unit your lab or strip reports. Use other water for the baby;
  boiling does not help.
- TDS: ________ ppm · pH: ________
- Retest due (one year, or after flooding): ________

## Judging a source in the field

Use this to *choose between* sources and to decide how hard to treat. Never to skip
treatment.

**Prefer, in this order:** stored or bottled water → rain caught off a clean surface → clean
snow or ice → a working well or spring → a clear flowing stream → a still pond → pool water
(needs distilling).

**Warning signs that push a source down the list or off it:**

- **Any smell of fuel, solvent or chemicals:** reject it. Boiling, bleach and filters do not
  fix that, and boiling makes some of it worse.
- **A sheen, foam or oily rainbow on the surface:** reject.
- **A strong rotten-egg or sewage smell:** reject for drinking.
- **Dark color, very cloudy, floating material:** do not use it. If you must, clear it, then
  distil rather than only disinfect.
- **Dead animals, mats of algae or livestock upstream:** heavy germ load. Boil or distil,
  never chemicals alone.
- **Downstream of a crop field, feedlot, road or industrial site:** assume nitrate and
  chemicals. Distil only.
- **Near a flooded area:** assume sewage and chemicals are mixed in (→ 17-03).

{{#if is.rural}}**Farm country.** Where crops and livestock surround you, surface water often
carries nitrate and manure runoff, and spring floods mix sewage with field runoff. Rain, snow
and distilled water are often *safer* than the nearest creek: the opposite of what instinct
says.{{else}}**Towns and cities.** Urban streams and ponds collect road runoff, sewage
overflows and industrial waste. Rain off a clean surface and snow are usually safer than any
nearby creek or pond.{{/if}}

## Gear and supplies

| Item | Why | Notes |
|---|---|---|
| Lab test of any well you might use | The only real answer on nitrate and coliform | State-certified lab; keep the report behind this page |
| Nitrate and nitrite test strips | The contaminant most dangerous to infants | Cheap; check the expiry date |
| Pocket TDS meter | Shows how salty a source is and whether a still is working | → 03-03 |
| Free-chlorine and pH strips | Confirms disinfection worked | Also for pool water (→ 03-08) |
| Total-coliform home test kits (present or absent) | Home check for bacteria | Not lab grade, far better than guessing |
| Clear glass sample jars with lids | Judge clarity, settling and smell in good light | |
| Printed results sheet | The numbers survive a dead phone | File it behind this page |

**If you don't have it:**

- **A clear jar and daylight.** Fill it, let it stand an hour, look at what settles and what
  floats, and smell the air at the top. Crude, but it separates obviously bad from possible.
- **Distilling** (→ 03-03) removes what you cannot test for. Slow and fuel hungry, but it is
  the honest answer.

## When it runs out

- **Runway:** test strips expire. Check dates and rotate them like batteries.
- **Ration:** test the *source*, not every batch. Once a source is known and unchanged, treat
  it the same way every time, and re-test only when something changes: heavy rain, flooding,
  a new smell, or anyone falling ill.
- **Resupply:** when tests run out, rank sources and use the strongest treatment you can
  afford in fuel. Distil anything doubtful.
- **The health signal:** if people start having diarrhea, treat the water supply as guilty
  until proven otherwise (→ 12-05).

## Phase notes

- **A (sheltering at home):** city water is tested until it is not. Once the grid is down,
  treat the last tap water as stored water and everything after as unknown.
- **B (moving):** no lab, no time. Rank the source, treat everything, and prefer rain, snow
  and springs over standing water.
- **C (rural or at a destination):** the first job at a new place is learning its water.
  Bring strips; test a well or spring before it becomes the family supply, and re-test after
  floods. On town water plus roof catchment, test the catchment.

## Cross-references

→ 03-04 purifying water · → 03-03 distilling · → 03-05 rain and snow · → 17-03 floods ·
→ 03-10 well water without power · → 20-01 infant needs · → 12-05 illness and dehydration

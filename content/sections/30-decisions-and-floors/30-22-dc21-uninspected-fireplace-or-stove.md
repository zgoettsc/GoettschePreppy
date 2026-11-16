---
id: 30-22-dc21-uninspected-fireplace-or-stove
section: 30-decisions-and-floors
title: "DC-21. Using a fireplace or wood stove that has not been inspected this year"
version: 2
revised: 2026-11-16
layer: card
danger_level: critical
phase: [A, C]
tags: [decision card, fireplace, wood stove, chimney, creosote, chimney fire, carbon monoxide, inspection]
derived_from: [06-09-chimney-and-creosote, 08-08-wood-heat-operation, 08-02-carbon-monoxide-safety]
sources:
  - csia-homeowner-resources-faqs-r3
  - chimney-safety-institute-of-america-csia-preventing-73b734
  - u-s-fire-administration-fema-fireplace-and-wood-stov-851c8d
  - epa-burn-wise-best-wood-burning-practices-0c1680
  - cdc-carbon-monoxide-poisoning-basics-772153
related: [06-09-chimney-and-creosote, 08-08-wood-heat-operation, 06-03-firewood-basics, 08-02-carbon-monoxide-safety, 08-04-emergency-heat-options, 29-12-ex12-extinguishers-blankets-and-alarms, 29-03-ex03-carbon-monoxide, 30-02-dc01-unvented-heater-overnight]
cards: [DC-21]
explainers: [EX-03, EX-12]
promote_when: [has.fireplace, has.wood_stove]
card: DC-21
options:
  - id: inspect-first
    label: "Inspect first, using the chimney page"
    summary: "No fire until the household has done the inspection on the chimney page (cold flue, light and mirror, scrape test, cap and blockages) or a professional has. A flue with glaze, cracks or a blockage is not used until fixed."
  - id: use-with-small-fires-and-watch
    label: "Use it with small hot fires and a watch"
    summary: "If it cannot be inspected now: small, hot fires of dry wood only, never smouldering overnight, CO and smoke alarms in the room, an extinguisher in reach, someone checking the chimney and attic, and an inspection at the first chance."
settings_summary: "A fireplace or wood stove can heat a house with no power, but the chimney is part of the appliance. Wood smoke leaves a tar called creosote on the inside of the chimney; it builds up faster with damp wood and slow, smoky fires, and it burns. A chimney fire can crack the chimney and set the house alight. A chimney blocked by a nest, leaves or fallen brick sends smoke and carbon monoxide back into the room. The national chimney standard (NFPA 211), the US Fire Administration and the Chimney Safety Institute of America all say inspect at least once a year. What helps most: inspect first, by a professional or with the household's own light-and-mirror check (removes most of it); dry wood, small hot fires, alarms, an extinguisher and a watch on the chimney (reduces it a lot)."
review_pass: { date: "2026-11-16", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "NFPA 211 annual and CSIA 1/8 in re-cited to CSIA FAQs; EPA stub key replaced by Best Wood-Burning Practices; USFA card details added." }
---

# DC-21. Using a fireplace or wood stove that has not been inspected this year

**What this page is for.** A fireplace or wood stove is one of the best heat sources without
power. In an emergency it may not have been checked in years, or ever. This card explains what
can be wrong with a chimney you cannot see into, and what the household decides before the first
fire.

> **SAFETY.** If you hear a roar like a freight train in the chimney, see flames or heavy sparks
> from the top, or the chimney wall is hot: everyone out, shut the stove's air or close the
> fireplace doors, wet the roof around it, do not pour water down the flue, and watch the attic
> for hours (→ 06-09). If a CO alarm sounds: everyone out, → 08-02.

## 1. The thing, in plain words

- The **firebox** is where the fire burns. The **flue** is the passage inside the chimney that
  carries smoke out. The **damper** opens and closes the flue.
- **Creosote** is a black, sticky or crusty tar from wood smoke that sticks to the flue. It burns
  very hot. Thin, flaky soot brushes off; a hard, shiny glaze does not.
- A **chimney fire** is creosote burning inside the flue.
- An **inspection** means looking up the cold flue with a strong light and a mirror, scraping the
  wall to see how thick the deposit is, and checking the cap and top for blockages (→ 06-09).

{{#if has.fireplace}}Your home has an indoor fireplace.{{/if}} {{#if has.wood_stove}}Your household has a wood stove.{{/if}} Firewood on hand: {{ gear.fuel.firewood_cords }} cords.

## 2. The rule, and why it was set

- NFPA 211, the national standard for chimneys, fireplaces and wood-burning appliances, says:
  "Chimneys, fireplaces, and vents shall be inspected **at least once a year** for soundness,
  freedom from deposits, and correct clearances" (quoted by CSIA, Homeowner Resources and FAQs).
- The Chimney Safety Institute of America says creosote "is highly combustible", that restricted
  air, unseasoned wood and a cool chimney make it build up faster (CSIA, Preventing Chimney
  Fires), and that a masonry fireplace should be swept at 1/8 inch of sooty buildup, sooner if
  there is any glaze (CSIA, Homeowner Resources and FAQs).
- The US Fire Administration says have the chimney inspected and cleaned each year by a
  professional, keep a glass or metal screen in front of the fireplace, keep anything that can
  burn at least 3 feet away, and put the fire out before you go to sleep or leave the house (USFA,
  Fireplace and Wood Stove Safety).

**Why:** you cannot see the inside of a chimney from the room. Creosote, cracked flue tiles,
missing mortar and nests build up silently over seasons. An inspection finds them before a fire
does.

## 3. How it actually hurts people

- **Chimney fire**: a long burn, or a hot fire after weeks of slow smouldering ones, lights the
  creosote. The flue reaches very high temperatures, cracks tiles and can ignite the wood framing
  around the chimney. With no fire department coming, the house can be lost.
- **Carbon monoxide**: a bird's nest, leaves or a collapsed tile blocks the flue. Smoke and CO
  come back into the room. CO has no smell and the smoke may not be obvious overnight (CDC).
- **Sparks and embers**: no screen, a cracked stove door, or a damaged chimney cap lets embers
  reach the floor or the roof.

## 4. What makes it safer

**Removes most of the risk**
- **Inspect before the first fire**: a professional sweep now while they work, or the household's
  own cold-flue check with light, mirror and scrape test (→ 06-09). Fix or sweep what you find.

**Reduces it a lot**
- **Dry, seasoned wood only**: EPA says do not burn wet or green wood, and wood burns best below
  20 percent moisture (EPA Burn Wise, Best Wood-Burning Practices); unseasoned wood speeds
  creosote buildup (CSIA; → 06-03).
- **Small, hot fires**, not a damped-down fire smouldering all night: "For most appliances, a
  smoldering fire is not safe or efficient" (EPA Burn Wise).
- **Smoke and CO alarms** in the room and on every level; an **extinguisher** in reach (→ 29-12).
- **Screen or closed doors**, and nothing that can burn within 3 feet (USFA).
- **Check the chimney top and the attic** around the chimney during the first fires: smell, heat,
  sparks.

**Reduces it a little**
- Chimney-fire suppressant sticks kept beside the fireplace.
- Ashes in a metal container with a lid, outside, at least 10 feet from the house (USFA).
- Watch the smoke from outside: thick dark smoke means a cool, dirty burn.

## 5. The options

**`inspect-first`: Inspect first, using the chimney page.**
You give up: heat until the inspection is done, which may be a cold night or two. You accept:
learning to inspect, or paying for it now.

**`use-with-small-fires-and-watch`: Use it with small hot fires and a watch.**
You give up: knowing the state of the flue. You accept: the risk of a hidden blockage or deposit,
controlled by small hot fires, dry wood, alarms, an extinguisher and someone watching the
chimney.

## 6. Our choice

{{card DC-21}}

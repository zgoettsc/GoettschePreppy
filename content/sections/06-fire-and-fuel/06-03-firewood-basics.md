---
id: 06-03-firewood-basics
section: 06-fire-and-fuel
title: "Firewood: species, cords, seasoning, splitting"
version: 3
revised: 2026-11-16
layer: core
danger_level: caution
phase: [A, C]
tags: [firewood, seasoning, cord, face cord, species, splitting, moisture, creosote, trees]
derived_from: [06-03-firewood-basics]
sources:
  - university-of-missouri-extension-wood-fuel-for-heati-b63761
  - usda-nrcs-plants-database-plant-profiles-and-image-l-a7089c
  - epa-burn-wise-best-wood-burning-practices-0c1680
related:
  - 06-02-sustaining-fire
  - 06-04-wood-supply-and-depletion
  - 06-05-alternative-fuels
  - 06-09-chimney-and-creosote
  - 08-01-heating-one-room
  - 14-03-opsec
  - 16-01-essential-hand-tools
  - 16-02-sharpening
  - 16-06-axes-and-saws
  - 30-25-dc24-children-and-dangerous-jobs
cards: [DC-24]
explainers: [EX-01, EX-13]
promote_when: [has.wood_stove, has.fireplace, is.cold_winters]
photo_slots:
  - { id: woodpile, caption: "Our woodpile: where it is, how it is stacked and covered" }
figures: [fig-cord-measure, fig-splitting-stance]
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: { date: "2026-11-16", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "Species table realigned to data/plants/species.json heat classes and MU G5450 Table 2 (pines medium, white pine low; apple removed); unsupported pine 2,700 lb and over-50-percent water corrected; face cord per MU; 15 ft splitting distance removed. Wave 2 (R18): a plates tag added so the home firewood trees render (region-plates fix); unsupported \"rank for each\" claim removed." }
---

# Firewood: species, cords, seasoning, splitting

**What this page is for.** Firewood is only fuel if it is dry, and only enough if you measure
it honestly. This page explains how to measure a woodpile, why moisture matters more than
anything else, which kinds of trees burn best, how to dry ("season") wood, and how to split it
without hurting yourself.

> **CAUTION.** Two things here hurt people. **Splitting injuries**: an axe glancing off a log
> is a leg wound, possibly with no emergency room. **Burning the wrong material**: never burn
> treated, painted or pressure-treated wood, plywood, OSB, particleboard, driftwood or trash.
> The smoke is poisonous and the residue damages the chimney (EPA, Best Wood-Burning Practices;
> MU Extension, Wood Fuel for Heating).

## Do this now

1. **Measure your stack honestly, in cords.** A **cord is 128 cubic feet**: a stack 4 ft high,
   4 ft deep and 8 ft long. A "face cord" or "rick" is one row 4 ft high and 8 ft long but only
   16 to 24 inches deep, so a **third to a half** of a cord, and it is often sold as a "cord" (MU
   Extension, G5450). This is where people badly overestimate what they have.
2. **Get a moisture meter** (a cheap hand tool with two pins) and check what you own. The
   target is **below 20 percent** (EPA, Best Wood-Burning Practices).
3. **Start seasoning now.** Fresh-cut hardwood is very wet (about 75 percent moisture by MU
   Extension's measure, so close to half its weight is water) and needs **at least six months**
   of drying (EPA), a year for dense hardwoods (MU Extension).
4. **Stack it off the ground, covered on top, open on the sides.** Wood dries by moving air,
   not by being wrapped in a tarp.
5. **Split it.** Split wood dries much faster than whole rounds.

{{figure fig-cord-measure}}

This household's firewood on hand: **{{ gear.fuel.firewood_cords }} cords**.

{{photo woodpile}}

## Moisture is everything

University of Missouri Extension gives these figures for hardwood (MU Extension, Wood Fuel for
Heating, G5450):

- one pound of **oven-dry** hardwood holds about **8,600 BTU** (a BTU is a unit of heat);
- **air-dried to about 20 percent** moisture: about **7,100 BTU per pound**;
- **fresh-cut at about 75 percent** moisture: about **4,900 BTU per pound**.

That is roughly **a third of the energy lost** to boiling off the wood's own water. Wet wood
also gives a smoky, hard-to-manage fire and builds **creosote** in the chimney, a tar that can
catch fire and can block the flue (→ 06-09, → 08-02). **Green (fresh-cut) wood in a crisis is
close to useless.** That is the strongest reason to season wood ahead, every year.

## Species: a cord is not a fixed amount of heat

At the same moisture, **heavier (denser) wood holds more heat**: a given volume of oak or hickory
gives more heat than the same volume of cottonwood or willow (MU Extension, G5450). MU Extension
puts a seasoned cord of oak or other dried hardwood at about **3,600 lb**. A cord of a light wood
weighs much less and carries much less usable heat.

The groups below are common US firewood trees sorted by heat per cord, the same classes used on
the region plates in Section 32 (MU Extension, G5450; → 32-00). They are general:
which of them grow near you depends on your region.

| Burn quality | Common US examples | Best use |
|---|---|---|
| **High (dense hardwoods)** | Oaks, hickories and pecan, sugar maple, white ash, beech, yellow birch, black locust, honey locust, Osage orange (hedge), mulberry, ironwood (hophornbeam), mesquite | **Overnight burns, cold nights, banking** (→ 06-02) |
| **Medium** | Elm, red and silver maple, green ash, paper birch, cherry, walnut, hackberry, sycamore, most pines (ponderosa, lodgepole, loblolly, shortleaf and other southern pines), Douglas-fir, larch (tamarack), junipers and eastern redcedar | General burning |
| **Low (light woods)** | Cottonwood, aspen, willow, basswood, boxelder, tuliptree (yellow-poplar), eastern white pine, spruces, true firs, hemlocks, northern white-cedar, western redcedar | Quick cooking heat and kindling. Burn fast and leave little coal |

**Pines and other conifers** are resinous: fine outdoors and as kindling, and in a flue burn them
only dry and hot, and check the chimney more often (→ 06-09). Osage orange throws many sparks: not
for an open fireplace without a screen (MU Extension).

**Strategy:** burn the light, fast woods for **cooking**; save the dense woods for **overnight
heat and banking** (→ 06-02).

**Elm is common and famously hard to split.** Use a maul and wedges, or leave it in rounds for
long overnight burns.

**Your region's trees.** Your home ecoregion is **{{ region.home.ecoregion }}**. The firewood
trees recorded there are listed below; the high-heat ones come first, with photographs. Each
state's page in Section 32 lists the trees of every ecoregion in that state (→ 32-00). **Learn
the bark**: in winter, and on a log already on the ground, bark and grain are all you have to go
on.

{{plates}}

## Seasoning properly

- **Split first, then stack.** Bark is waterproof; the split faces are where water leaves.
- **Off the ground**: pallets, rails or scrap lumber. Wood touching the ground rots and soaks
  water back up.
- **Cover the top only.** A tarp over the whole pile traps moisture.
- **Sun and wind**, not shade. A spot with sun and moving air dries fastest.
- **Single rows dry faster** than deep blocks.
- **Time:** at least **six months** for most woods (EPA); dense hardwoods such as oak need a year
  or more (MU Extension), and the slowest oaks up to two years.
- **Check with the meter** instead of guessing. Split a piece and test the fresh face: a
  surface that reads 20 percent may read 35 percent inside.

## Splitting safely

- **Chopping block** at about knee height. Never split on the ground.
- **Feet apart and out of the swing line.** If the blade glances off, it should hit the block
  or the dirt, not your shin.
- **Maul for splitting, axe for felling and limbing.** A splitting maul has a wedge-shaped head
  that does the work; a sharp felling axe gets stuck in rounds (→ 16-06).
- **Wedges and a sledgehammer** for knotty, twisted and stringy wood such as elm.
- **Nobody near you while you split**, especially children: keep everyone well clear of the
  swing and of flying chips and pieces.
- **Frozen wood splits easier.** Winter is a good time to split.
- **Stop when you are tired.** Most splitting injuries happen on a tired swing.

Whether teenagers split wood is the household's call: {{choice DC-24}} → 30-25.

{{figure fig-splitting-stance}}

## Stacking and storage

- Keep a **working supply** near the door (a few days' worth, under cover) and the **main
  stack** further out.
- **Bring tomorrow's wood inside** to warm and dry; it lights far better.
- **Mice, rats and insects** live in woodpiles. Keep the main stack away from the house.
- **Do not stack against the house**: moisture, pests and fire spread.
- **A big woodpile shows the street you have supplies** (→ 14-03). Think about what can be
  seen.

## Gear

**Have now:**

| Item | Why | Notes |
|---|---|---|
| Splitting maul | The main tool | And a spare handle |
| Two or more splitting wedges and a sledgehammer | Knots, big rounds, elm | Steel wedges |
| Bow saw and spare blades | Cuts wood with no fuel, quietly | Keep plenty of blades |
| Chainsaw with fuel, bar oil, files, spare chain | Fast while fuel lasts | Runs out: back it up with hand tools |
| Felling axe with a file or stone | Limbing and felling | Keep sharp (→ 16-02) |
| **Moisture meter** | Know what will burn | The cheapest efficiency purchase there is |
| Chopping block | Safety and speed | A big round of tough wood such as elm |
| Pallets or rails | Keep the stack off the ground | Free from many businesses |
| Tarps (top cover only) | Keep rain off, let air through | Weight with rocks or tie down |
| Heavy gloves, eye protection, sturdy boots | Splitting injuries | Steel toes if you have them |
| Log carrier or sled | Hauling in snow | Saves your back |

**If you do not have it:**

- **Standing dead and storm-downed wood** is already partly seasoned: the best crisis fuel.
- Untreated pallets and clean scrap lumber burn fine. Pull the nails; **never** treated wood.
- Fruit-tree and hedge prunings, windbreak thinnings.
- A car jack, or wedges and a sledgehammer, can stand in for a log splitter.

## When it runs out

- **Count** your days of wood: cords on hand divided by cords burned per day (→ 06-04).
  Recount honestly.
- **Stretch it:** light woods for cooking, dense woods overnight; bank the fire (→ 06-02); heat
  one room instead of the house (→ 08-01).
- **Always be seasoning next season's wood.** In a long emergency the rhythm becomes: burn this
  year's, cut and stack next year's.
- **The trap:** a pile of green wood is not a fuel supply. Staying a season ahead is the whole
  discipline of heating with wood.

## Phase notes

- **A (sheltering at home):** {{#if is.urban}}town lots have little room and few trees. Storm
  debris and scrap are the main resupply (→ 06-04).{{else}}storm debris, deadfall and windbreak
  thinnings are the nearest resupply (→ 06-04).{{/if}} Season everything you gather.
- **B (on the move):** carry no wood; gather dry, standing dead wood at stops.
- **C (settled somewhere new):** more wood, but you must cut and season **ahead**. A winter's
  heat is several cords. Build a woodshed early.

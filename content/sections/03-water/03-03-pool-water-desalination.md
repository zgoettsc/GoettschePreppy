---
id: 03-03-pool-water-desalination
section: 03-water
title: "Pool and hot tub water: utility water, and distilling it to drink"
version: 2
revised: 2026-11-16
layer: gear
danger_level: critical
phase: [A, C]
tags: [water, pool, saltwater pool, hot tub, distillation, still, desalination]
derived_from: [03-03-pool-water-desalination]
sources: [cdc-how-to-make-water-safe-in-an-emergency-5d78b5, us-epa-emergency-disinfection-of-drinking-water-6aa91f, awwa-water-technology-distillation-ensures-safe-drin-7ba482, fema-477-food-and-water-in-an-emergency, fema-ready-gov-water]
related: [03-01-daily-water-needs, 03-04-purifying-water, 03-05-rain-and-snow-water, 03-08-keeping-water-from-going-bad, 06-04-wood-supply-and-depletion, 09-02-solar-basics, 23-02-master-consumables-table, 29-05-ex05-chlorine-products, 29-06-ex06-water-words, 30-01-the-floors, 30-14-dc13-drinking-pool-or-surface-water]
cards: [DC-13]
explainers: [EX-05, EX-06]
promote_when: [has.pool, has.hot_tub]
photo_slots:
  - { id: pool-still-setup, caption: "Our still: pot, lid or sealed tube, condenser bath, collection jar" }
figures: [fig-cup-on-lid-still, fig-tube-condenser-still]
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: { date: "2026-11-16", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "Distillation method re-sourced to FEMA 477 (not on current CDC page); hot tub aligned with DC-13 (always distil); unsourced yield/wood/Wh estimates replaced by measure-your-own method." }
---

# Pool and hot tub water: utility water, and distilling it to drink

**What this page is for.** A swimming pool or hot tub is a large store of water already at
your house. This page explains what that water is good for, why you cannot simply drink it,
and how to distil it (boil it and collect the steam) when you must.
{{#if has.pool}}Your pool holds about {{ dwelling.pool_gallons }} gallons.{{else}}{{#if has.hot_tub}}Your hot tub holds about {{ dwelling.pool_gallons }} gallons.{{/if}}{{/if}}

> **SAFETY.**
> - **A saltwater pool cannot be made drinkable by boiling, bleach or an ordinary filter.**
>   None of them removes salt, and drinking salt water makes dehydration worse. Only
>   **distillation** removes salt.
> - **Pool and hot tub water also holds chemicals:** chlorine or bromine, stabilizer
>   (cyanuric acid), and sometimes algaecide or metals. Distillation removes salts and most of
>   these.
> - **Floor:** Bleach or pool shock is never mixed with ammonia, acids or other cleaners.
>   Pool supplies include acids ("pH down", muriatic acid); keep them apart. The mix gives off
>   chlorine gas. (→ 30-01)
> - **Floor:** Children do not have access to firearms, fuel, medications or chlorine
>   products. Pool chemicals count as chlorine products. (→ 30-01)

## Do this now

1. **Use stored, tap or bottled water first.** Distilling is slow and burns a lot of fuel. It
   is the fallback, not the main supply.
2. **Use untreated pool water freely for everything except drinking and cooking:** flushing
   toilets, washing floors, cleaning, fighting fires. This is the pool's real value: once the
   pool covers flushing and washing, every gallon of stored water can go to drinking.
3. **Never drink saltwater pool water straight, boiled or bleached.** The salt stays in.
4. **Drinking fresh (chlorine) pool water without distilling it is a decision.** Your
   household's choice: {{choice DC-13}} (→ 30-14). Whatever you chose, follow it the same way
   every time. **Hot-tub water is distilled before drinking under every option on the card.**
5. **To distil:** boil the water and catch the **steam**, which turns back into clean water.
   The salt and most chemicals stay behind in the pot. Method below.
6. **Cover the pool** to cut evaporation and keep out leaves, animals and children.

## What kind of water is in it

| Water | What is in it | Without distilling it is | To drink |
|---|---|---|---|
| **Saltwater pool** (salt chlorinator) | Dissolved salt, chlorine made from the salt, stabilizer, maybe algaecide or metals | Utility water only | **Distil.** No other home method removes salt |
| **Chlorine pool** (fresh water) | Chlorine, stabilizer, maybe algaecide or metals; bacteria and algae once the pump stops | Utility water | Distil; or the household's choice on → 30-14 |
| **Hot tub or spa** | Bromine or chlorine, body oils and sweat from bathers, often a warm breeding ground for germs | Utility water | **Distil.** No option on → 30-14 drinks it undistilled |

A home saltwater pool is much less salty than the sea, but **far too salty to drink**. Your
salt chlorinator's manual gives the salt level it runs at; write it here: ______ ppm ("ppm"
means parts per million, → 29-05). Less salty does not mean safe to sip.

**The trade-off for fresh pools, in one sentence:** filtering and chlorinating a fresh pool
uses far less fuel than distilling it, but leaves in the stabilizer, algaecide and any metals
that distilling would remove. The card lays out the risks and options (→ 30-14). FEMA's
own list of household water sources says not to drink from swimming pools or spas (FEMA,
Food and Water in an Emergency).

## Why distillation works

Distillation boils water into steam and turns only the steam back into liquid. Salt, metals
and most chemicals do not boil off with the water, so they are **left behind** in the pot.
FEMA and the Red Cross say distillation removes germs that resist boiling and chlorine, **as
well as heavy metals, salts and most other chemicals**, and that salt water is used only if it
is distilled first (FEMA, Food and Water in an Emergency; AWWA, distillation in an emergency).
Boiling and bleach kill germs but leave salt and chemicals in place (EPA).

### The cup-on-lid still (FEMA and Red Cross method)

{{figure fig-cup-on-lid-still}}

1. **Pre-filter:** pour the water through a cloth or coffee filter to remove leaves, insects
   and grit. This keeps the pot cleaner and the still faster.
2. Fill a pot **halfway** with the filtered water.
3. Tie a cup to the handle of the pot lid so that, when the lid is put on **upside down**, the
   cup hangs **right side up** inside the pot. The cup must **not** touch the water.
4. Put the lid on upside down. Steam hits the lid, runs to the low middle point and drips into
   the cup.
5. **Boil for 20 minutes.** The water that drips from the lid into the cup is distilled
   (FEMA). Let it cool before drinking.

**Yield:** measure it. Pour the cup into a measuring cup after a timed run and write the
result here: ______ cups an hour. FEMA says a normally active person needs about three quarters of
a gallon of fluid a day (FEMA, Ready.gov Water; → 03-01): about 12 cups each, for each of your
{{ household.size }} people, before cooking. Divide by your measured rate to see how many
hours of boiling that takes. For most households the cup-on-lid still is a
demonstration and a stopgap, not a supply. That is why the tube still below, fuel, and rain
and snow (→ 03-05) matter.

### The larger still: pot, lid and tube condenser

The cup-on-lid wastes most of the steam. Piping the steam out through a tube and cooling it
outside the pot captures nearly all of it: same fire, several times the water.

{{figure fig-tube-condenser-still}}

**Materials (stores in a shoebox):**

- **10 to 20 ft of soft copper tubing, 3/8 or 1/2 inch.** Copper carries heat away fast and
  handles steam. Food-grade silicone tubing is fine for a short flexible joint. **Never use
  vinyl or PVC tubing**: it releases chemicals at steam temperature.
- **A lid you can seal the tube into:** drill a spare pot lid and fit a compression or barbed
  fitting, or, with no tools, seal heavy aluminum foil over the pot with the tube pushed
  through and crimped tight.
- **A cooling bath:** a bucket or basin of cold water (snow in winter works well) that the
  copper coil runs through, sloping **downhill** the whole way to the collection jar.
- A collection jar, and cloth or coffee filters.

**Running it:** pot half full of pre-filtered water at a low rolling boil. Steam leaves
through the tube, turns to water in the cold coil and drips into the jar. Keep the bath cold
(change the water or add snow). Keep the tube sloping so water cannot pool in it. **Never let
the pot boil dry**: the salts scorch and the pot warps. Throw away the salty liquid left in
the pot.

{{photo pool-still-setup}}

**Rules that keep the water clean:**

- Before the first drinking batch, run a new copper coil once with vinegar and water, then
  once with plain water. New copper carries oil from manufacturing.
- **Lead-free fittings only.** No lead solder, no brass of unknown origin.
- Pour the leftover brine far from gardens and rain barrels. Salt kills soil.
- **Do not look for a reverse-osmosis unit** to use on pool water. Home units need water
  pressure, power and replacement membranes. A still is the practical route.

**Planning numbers: measure your own still once.** No published table gives the output of a
home-built still; it depends on the seal, the fire and how cold the coil is.

- **Yield:** time a run with a watch and measure the water in the jar. Write it here:
  ______ quarts an hour.
- **Fire time:** 4 quarts make a gallon, so hours of fire per gallon = 4 ÷ your quarts an
  hour = ______. Your household's drinking share alone is several gallons a day, so
  **distilling cannot carry a household by itself.** Run the still on fires already burning
  for heat and cooking (→ 06-04), and use it to cover dry spells. Rain and snow must be the
  main supply.
- **Wood:** weigh the wood you burn during that timed run, and divide by the gallons you
  made: ______ lb of wood per gallon. Turning water into steam takes several times the heat of
  bringing it to a boil, and an open fire wastes most of its heat, so expect it to be a large
  number. Put it on the consumables table (→ 23-02).
- **Check the output:** a cheap TDS meter ("total dissolved solids", a pen that reads how much
  is dissolved in water) should read near zero on distilled water. If it reads salty, the
  seal is leaking boiling splash into the tube. Reseat the seal and fix the slope.

**Do not distil on battery power.** Turning water to steam takes several times the energy of
bringing the same water to a boil, and a battery holds very little heat energy by that
standard. {{#if has.power_station}}Your power stations hold about
{{ gear.station_wh_total }} watt-hours in total.{{else}}A power station's label gives its
watt-hours.{{/if}} An electric distiller's label gives its watts and the liters it makes per
hour. Watts ÷ liters per hour = watt-hours per liter; divide the station's watt-hours by that
to see how few liters a full charge would make.
Distillation is a wood-fire job. An electric countertop distiller running on a strong solar
day nets only a few liters: useful for drinking water, never the household's supply
(→ 09-02).

## Gear and supplies

| Item | Why | Notes |
|---|---|---|
| Large stockpot with a domed lid that can sit upside down | The still | Stainless steel; a rounded lid sends drips to the center |
| Heat-safe cup and wire or cord | Catches the distilled water | A metal cup will not melt |
| 10 to 20 ft soft copper tubing, 3/8 to 1/2 inch, and a fitting | The tube still | Never vinyl tubing |
| A drilled spare lid, or heavy aluminum foil | Seals the tube into the pot | Foil needs no tools |
| Cloth or coffee filters | Pre-filter | Cheap; stock many |
| Unscented bleach or pool shock | Disinfecting distilled water before storage | **Dose only from → 03-04.** Pool shock only by the two-step method there, never as dry granules |
| TDS meter | Confirms the still is working | Reads near zero on good distillate |
| Food-safe storage containers | Finished water | Label "DRINKING" and "POOL / UTILITY" |
| Electric countertop distiller | Much faster if you have power | Power hungry; a supplement only |

**If you don't have it:**

- Any pot with a bowl set inside and an upside-down domed lid is a still. Weight the center of
  the lid so drips fall into the bowl.
- Clear tubing and two sealed containers over heat make a rough condenser.
- Plastic sheeting over a frame floating on the pool surface makes a solar still: slow, but it
  needs no fuel. Measure its daily output before you count on it.

## When it runs out

- **Runway:** a pool is a lot of *volume*. Your real limits are **fuel to boil it** and
  **time**. Wood or propane (→ 06-04) is the binding constraint, not water.
- **Ration:** distil only what you need to drink and cook with. Use untreated pool water for
  all washing, flushing and cleaning.
- **Resupply:** rain and snowmelt need only disinfecting, **not** distilling, which takes far
  less fuel (→ 03-05). In wet or snowy months, use those first and save the pool for dry
  spells.
- **Gardens:** do not water a garden with saltwater-pool water. Salt harms soil and plants.

## Phase notes

- **A (sheltering at home):** the pool is a large reserve already in place. Once the grid is
  down, **stop adding chemicals by default**, cover the pool, and treat it as your utility
  tank. Keeping a measured chlorine level to slow algae is an option with its own rules
  (→ 03-08).
- **B (moving):** you cannot take the pool. Carry stored or distilled water, and know the
  water sources on the route.
- **C (rural or at a destination):** a still kit is light. Bring it for brackish or doubtful
  sources even if you do not expect to need it. Fresh well water is disinfected, not
  distilled (→ 03-10).

## Cross-references

→ 03-01 how much you need · → 03-04 purifying fresh water · → 03-05 rain and snow ·
→ 03-08 keeping pool water from going bad · → 06-04 wood supply · → 30-14 the pool-water card ·
→ 29-05 chlorine products

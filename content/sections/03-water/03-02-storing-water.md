---
id: 03-02-storing-water
section: 03-water
title: "Storing water safely"
version: 1
revised: 2026-11-16
layer: core
danger_level: caution
phase: [A, B, C]
tags: [water, storage, containers, bleach, water heater, rotation]
derived_from: [03-02-storing-water]
sources: [cdc-how-to-create-and-store-an-emergency-water-suppl-f0c412, cdc-how-to-make-water-safe-in-an-emergency-5d78b5, us-consumer-product-safety-commission-tap-water-scal-4cdd1a]
related: [03-01-daily-water-needs, 03-04-purifying-water, 03-05-rain-and-snow-water, 03-06-winter-water, 03-08-keeping-water-from-going-bad, 13-02-hygiene-and-handwashing, 13-10-dishwashing-and-food-hygiene, 13-05-winter-sanitation, 22-04-household-inventory, 29-05-ex05-chlorine-products, 30-01-the-floors]
cards: []
explainers: [EX-05, EX-06]
promote_when: []
photo_slots:
  - { id: stored-water-location, caption: "Where our stored water lives: the jugs, the cases, the bladder, the scoop" }
  - { id: water-heater-drain-valve, caption: "Our water heater: the gas control or breaker, the cold inlet valve on top, the drain valve at the base" }
figures: []
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: null
---

# Storing water safely

**What this page is for.** How to store drinking water so it is still safe when you need it:
which containers, how to clean them, where to keep them, and how to get the water already in
your house (including the water heater) out safely.

> **CAUTION.** Stored water goes bad because of **what you put it in** and **what you touch it
> with**, far more often than because of age. A contaminated 55-gallon drum is not a water
> supply; it is 55 gallons of disease. Follow the container and handling rules exactly.
>
> **Floor:** bleach or pool shock is never mixed with ammonia, acids or other cleaners. The
> mix gives off chlorine gas. (→ 30-01)

## Do this now

1. **Fill everything when the forecast turns bad, not when the power fails.** Ice storm
   warning, blizzard warning, hurricane watch, severe thunderstorm watch: fill the bathtub
   bladder and every container then. City water pressure often holds for **12 to 48 hours**
   after a grid failure, but it **fades before it stops**: weak flow upstairs first, then
   sputtering and air. **By the time you notice, you are at the end of the buffer, not the
   start.** A bathtub bladder takes 20 to 30 minutes at full pressure and much longer at low
   pressure. This is the only water job with a hard deadline.
2. **When pressure comes back after an outage, assume the water is contaminated.** Empty
   pipes suck in dirty water at leaks and joints. Filter and chlorinate (→ 03-04) until the
   water utility says it is safe.
   {{#if has.municipal_water}}Your water utility: {{ contacts.utility.water.provider }},
   phone {{ contacts.utility.water.phone }} (check it against a current bill).{{/if}}
3. **Use food-grade containers** with tight lids: water jugs and drums made for drinking
   water, or clean 2-litre soda bottles. **Never** reuse containers that held chemicals, and
   do not use milk jugs.
4. **Sanitize before filling:** wash with soap, rinse, then swirl **1 teaspoon of unscented
   5 to 9 percent household bleach in 1 quart of water** over the whole inside. Wait
   **30 seconds**, pour it out, let it air dry (CDC). Bleach basics: → 29-05.
5. **Label** every container **"DRINKING WATER"** with the **date filled**.
6. **Store at 50 to 70 °F, in the dark, off bare concrete**, away from gasoline, pesticides
   and solvents (fumes pass through plastic).
7. **Replace home-filled water every 6 months.** Store-bought sealed bottles: use the printed
   date.
8. **Never put hands or a dirty cup into stored water.** Pour it, or use a clean scoop kept
   only for that.

## Why it works this way

Tap water from a city system leaves the plant with a little chlorine in it. That chlorine
fades in storage. Once it is gone, whatever got in (from the container, the air or a hand)
can multiply. That is why the CDC's rules are mostly about **clean containers, sealed lids
and clean handling**, not about water "expiring" (CDC, How to Create and Store an Emergency
Water Supply).

{{#if has.well}}Well water usually has no chlorine in it to begin with, so clean handling
matters even more. Many households add the CDC bleach dose (→ 03-04) to well water before
long storage.{{/if}}

### Container choices

| Option | Gallons | Good | Bad |
|---|---|---|---|
| Bottled water, sealed | varies | Safest, no preparation, portable | Costs most per gallon; bulky |
| 5 to 7 gal jugs | 5 to 7 | Can be moved when full, stack, good for leaving home | Modest volume; about 50 lb each |
| 55-gal food-grade drum | 55 | Cheapest per gallon; two weeks in one container | About 460 lb full: it never moves again; needs a pump |
| Bathtub bladder | about 100 | Huge and cheap | Only works if filled **before** the water stops |
| Clean 2-litre soda bottles | 0.5 | Free, tough, good for freezing and for children to carry | Work to fill and rotate |

### Where to put it

A basement or an inside room is best: dark, cool, steady temperature. {{#if has.basement}}Your
basement is the right place.{{/if}} {{#if has.garage}}**An attached garage is the wrong place
for winter.** In a grid-down cold spell the garage drops below freezing and bottles split.
Move any water stored there inside before winter, or on the first day of an outage at the
latest (→ 03-06).{{/if}} Water expands when it freezes: leave a little air space at the top of
any container that might get cold, and never use glass for cold storage.

**Write down where your water is** so anyone in the house can find it (→ 22-04).

{{photo stored-water-location}}

### Handling

One person's dirty hands can spoil a whole drum. Use a spigot, pump or pour spout kept only
for water; keep it capped; never pour unused water back into the container.

**If stored water tastes flat,** pour it back and forth between two clean containers to put
air back in it, or add a pinch of salt per quart. The CDC suggests this for boiled water and it
works the same here.

## The water heater: the biggest store already in your house

{{#if has.water_heater_tank}}Your tank water heater holds about {{ dwelling.water_heater_gallons }}
gallons.{{else}}A tank water heater holds 30 to 80 gallons. If you have one, or reach a house
that does, this applies.{{/if}} It is also the most dangerous water in the house to get at
carelessly.

- **It is hot.** Water heaters are usually set at 120 to 140 °F. At 140 °F, water scalds a
  child's skin in seconds (US Consumer Product Safety Commission, Tap Water Scalds).
- **A gas heater keeps heating** while gas flows, grid or no grid. An electric one stops when
  the power stops, but stays hot for many hours.
- **Until you drain it, it is your only safe hot washing water.** Use it for the first days'
  hand washing and dishes before you drain it for drinking (→ 13-02, → 13-10).

{{photo water-heater-drain-valve}}

**Draining the water heater: six steps, in this order.**

1. **Turn the heat off.** On a gas heater, turn the gas control to **OFF** (not "pilot"). On an
   electric heater, switch its breaker off. Draining with the burner or elements live will
   fire them on an emptying tank and ruin it.
2. **Close the cold-water inlet valve** on the pipe at the top of the tank.
3. **Open a hot tap** somewhere higher in the house (a bathroom sink) and leave it open. This
   lets air in so the tank will drain.
4. **Put a hose or bucket on the drain valve at the base, then open it slowly. THE WATER CAN BE
   SCALDING.** Wear gloves and long sleeves and keep children out of the room. If you can, let
   the tank cool for hours first, or run the first water into a lidded bucket and walk away
   from it.
5. **The first gallon or two carries sediment** (sand and scale from the bottom of the tank).
   Let it settle, pour off the clear water and throw away the sludge. If the tank has sat for
   weeks, treat the water before drinking (→ 03-04).
6. **Do not turn the heat back on until the tank is full again:** inlet valve open, hot tap
   running steadily with no air. A heater fired empty burns out.

Every other page that says "drain the water heater" means this procedure.

## Gear and supplies

| Item | Why | Notes |
|---|---|---|
| Food-grade water jugs, 5 to 7 gal | Water you can move; for leaving home | Rigid, with a spigot or cap you trust |
| 55-gal food-grade drum, bung wrench and pump | Bulk storage | Put it where it will live for ever before you fill it |
| Bottled water by the case | Safest, no preparation | Use by the printed date |
| Unscented household bleach, 5 to 9 percent | Cleaning containers **and** treating water | Buy fresh; it weakens within months (→ 29-05) |
| A scoop, pour spout or pump kept only for water | Keeps hands out of the supply | Store it capped and clean |
| Waterproof labels and a marker | Date and name every container | "DRINKING" or "UTILITY" |
| Bathtub bladder | Large cheap volume at the warning stage | Practise putting it in the tub once |

**If you don't have it:**

- Clean 2-litre soda bottles are good containers: free and strong.
- Food-grade buckets from bakeries or restaurants. Ask what was in them; avoid anything oily.
- The water heater (above), toilet tanks (not bowls) and ice in the freezer.

## When it runs out

- **Runway:** stored gallons ÷ {{ derived.water.plan_gal_day }} gallons a day, your plan rate
  from → 03-01. The floor rate ({{ derived.water.floor_gal_day }}) is a crisis ration, not the
  number to divide by.
- **Ration:** the moment the tap is in doubt, stop using stored water for anything but
  drinking, cooking, infant feeding and medical needs. Everything else uses rain or untreated
  water.
- **Resupply:** refill containers with treated rain, snowmelt or other treated water
  (→ 03-04, → 03-05, → 03-06). **Clean the container again** before each refill.
- **Rotation is the quiet failure.** Water you stored and forgot is water you will not trust
  when it matters. Put the six-month swap on the calendar with the smoke-alarm batteries.

## Phase notes

- **A (sheltering at home):** fill the bladder and every container the moment a warning is
  issued, before pressure is lost.
- **B (moving):** only jugs and bottles travel. Water weighs 8.3 lb a gallon; carry one to two
  days and a way to treat more, not a week.
- **C (rural or at a destination):** set up storage at once (a cistern, drums or barrels) so
  you are not hauling water every day. The same cleaning rules apply to anything you press
  into service.

## Cross-references

→ 03-01 daily water needs · → 03-04 purifying water · → 03-05 rain barrels ·
→ 03-06 winter water · → 03-08 keeping water from going bad · → 22-04 where everything is ·
→ 29-05 chlorine products

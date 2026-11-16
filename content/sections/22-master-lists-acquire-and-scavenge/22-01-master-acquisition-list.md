---
id: 22-01-master-acquisition-list
section: 22-master-lists-acquire-and-scavenge
title: "Master acquisition list"
version: 1
revised: 2026-11-16
layer: household
danger_level: none
phase: [A, B, C]
tags: [lists, buying, acquisition, consumables, shopping, gear]
derived_from: [22-01-master-acquisition-list]
sources:
  - cdc-how-to-create-and-store-an-emergency-water-suppl-f0c412
  - us-epa-emergency-disinfection-of-drinking-water-6aa91f
  - american-red-cross-power-outage-safety-6d07a8
  - american-red-cross-winter-storm-preparedness-and-bli-4bb6c0
  - nfpa-national-fire-protection-association-lithium-io-0c7d64
  - ready-gov-build-a-kit
related: [22-07-priority-purchase-order, 22-02-scavenging-field-guide, 22-04-household-inventory, 22-03-go-bags-and-kits, 22-05-kit-vehicle, 22-06-kit-medical, 23-02-master-consumables-table, 23-04-resource-lifecycles, 26-01-how-to-run-the-check]
cards: [DC-01, DC-02, DC-05, DC-13]
explainers: [EX-01, EX-02, EX-03, EX-05, EX-06]
promote_when: []
photo_slots: []
figures: []
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: null
---

# Master acquisition list

**What this page is for.** Every subject page in this binder ends with a list of things to own.
This page collects all of them in one place, grouped by what they do (water, food, heat and so
on), so you can shop, budget and tick things off. **→ 22-07 puts the same items in buying
order** (what to buy first). **→ 22-02 is the same list read backwards:** what to look for when
there is nothing left to buy. Where your settings already say what you own, the number is
printed; everything else you tick by hand.

## Do this now

1. **Print this page and walk the house with it** (the route is → 26-02). Mark each row
   ✔ have it, ~ partly, ✗ none. Most households find they already own a good share of it and
   have never counted.
2. **Buy the ✗ items in → 22-07's order**, not this page's order. This page is grouped by
   subject; → 22-07 is ordered by what hurts people soonest.
3. **Rows marked ★ are load-bearing:** the plan has a hole without them. If you buy nothing
   else this year, buy those.
4. **Log what you buy in → 22-04** as it arrives, or you will end up guessing at your own
   supplies.
5. **Owning is not the same as working.** The tests (does it turn on, does it fit, is it in
   date) are on → 26-03 to → 26-07.

## How to read the list

| Mark | Meaning |
|---|---|
| **★** | Load-bearing. The plan has a hole without it |
| **§** | Has a **consumable**: buy the spares at the same time (filter elements, fuel, lids, batteries) |
| **№** | **Quantity matters more than quality.** Several cheap ones beat one good one |
| **⌛** | **Time-sensitive.** Takes months or years to become useful (seasoned wood, soil, skill, seed) |

**The three buying mistakes this list is built to prevent:**

1. **Buying the tool and not the consumable (§).** A water filter with no spare element, a
   canner with no lids, a saw with no file, a radio with no batteries. Many "prepared"
   households fail exactly here.
2. **Buying one of something every person needs (№).** One headlamp in a household of
   {{ household.size }} is an argument.
3. **Buying late what needed years (⌛).** Soil, seed, seasoned firewood and skill cannot be
   bought in a hurry at any price.

## 1. Water (→ 03-01 to → 03-10)

**Your numbers:** stored now {{ gear.water.stored_gal }} gal · two-week target
{{ derived.water.two_weeks_gal }} gal (→ 03-01).

| ✔ ~ ✗ | Item | Notes | Page |
|---|---|---|---|
| [ ] | **★§ Gravity or pump water filter + spare elements** | The element is the consumable. Buy two spares. A filter does not remove salt or dissolved chemicals (→ 29-06) | → 03-04, → 03-09 |
| [ ] | **★ Unscented household bleach**, fresh, plus a dropper | Write the purchase date on it: bleach loses strength over months (→ 29-05) | → 03-04 |
| [ ] | **★№ Food-grade water containers** (5-gal jugs and/or larger drums) | Store cool and dark (CDC, How to Create and Store an Emergency Water Supply) | → 03-02 |
| [ ] | Water preserver or stabiliser | For long-term stored water; follow its label | → 03-02 |
| [ ] | **§ Distillation setup** (large pot, lid, collection vessel, or a purpose-built still) | The only home method that removes salt. {{#if has.pool}}Your pool or hot tub ({{ dwelling.pool_gallons }} gal) is raw material, not drinking water.{{else}}Needed only if your fallback water is salty or chemically contaminated.{{/if}} Drinking pool or untreated surface water is a household choice: {{choice DC-13}} → 30-14 | → 03-03 |
| [ ] | Rain barrels + downspout diverter + screen | The screen keeps mosquitoes out. {{#if is.cold_winters}}Drain before the hard freeze or the ice splits it.{{/if}} | → 03-05 |
| [ ] | №Buckets with lids (food grade), and a separate, labelled non-potable set | Never cross-use | → 03-02 |
| [ ] | Test strips (limited use: read → 03-07 first) | They say almost nothing about germs | → 03-07 |
| [ ] | Mosquito larvicide (Bti) for standing water | Treats water you are not drinking | → 03-08 |
| [ ] | Hoses, siphon pump, funnel | Moving water is most of the work | → 03-02 |
| [ ] | Well bailer (a narrow cylinder bucket) + rope long enough for the well | {{#if has.well}}Your no-power fallback for the well (→ 03-10).{{else}}Only if you have, or may move to, a drilled well.{{/if}} | → 03-10 |

## 2. Food storage (→ 04-01 to → 04-19)

**Your numbers:** pantry about {{ gear.food.pantry_days }} days by your estimate ·
freeze-dried {{ gear.food.freeze_dried_servings }} servings · household need about
{{ derived.calories.day }} kcal a day (→ 04-01).

| ✔ ~ ✗ | Item | Notes | Page |
|---|---|---|---|
| [ ] | **★ Staples you actually eat**: rice, beans, oats, flour, sugar, salt, oil | Store what you eat; eat what you store | → 04-01, → 04-02 |
| [ ] | **★ Mylar bags + oxygen absorbers + food-grade buckets** | Turns staples that keep a year into staples that keep many years | → 04-03 |
| [ ] | **§ Pressure canner** + spare gaskets | The only safe method for low-acid food (→ 29-08) | → 04-05 |
| [ ] | **§ Water-bath canner**, jars, **lids** (lids are single-use) | Buy lids by the case | → 04-04 |
| [ ] | § Dehydrator, or screens for sun and oven drying | | → 04-06 |
| [ ] | Canning or pickling salt (not iodised table salt), vinegar, sugar, honey | Preserving, not just cooking | → 04-13, → 04-07 |
| [ ] | **Fats and oils** | The hardest food to store and the easiest to run out of. Rotate | → 04-12 |
| [ ] | Powdered or canned dairy, shelf-stable protein | | → 04-14 |
| [ ] | Coffee, tea, comfort food | Morale is a supply line | → 21-02 |
{{#if has.anaphylaxis}}| [ ] | **★ Allergen-safe staples**, stored and labelled separately | A dedicated bin and dedicated utensils for the allergic person | → 02-04 |
{{else}}| [ ] | Special-diet staples (allergy, celiac, infant), stored separately | Only if someone needs them | → 02-04, → 02-19 |
{{/if}}| [ ] | Rodent-proof bins and gamma lids | Rodents find bulk grain | → 04-11 |
| [ ] | Sprouting jars + sprouting seed | Fresh food in the dead of winter | → 04-16 |
| [ ] | Permanent marker, labels, a rotation log | An unlabelled bucket is a mystery in two years | → 04-10 |

## 3. Food production (→ 05-01 to → 05-19)

| ✔ ~ ✗ | Item | Notes | Page |
|---|---|---|---|
| [ ] | **★⌛ Open-pollinated (heirloom) seed** in quantity | Hybrid seed does not come true when you save it | → 05-03 |
| [ ] | ⌛ Compost bin or pile; a fork to turn it | Soil is a multi-year project | → 05-11 |
| [ ] | Garden hand tools: fork, spade, hoe, rake, trowel | | → 05-01, → 16-01 |
| [ ] | Row cover, cold frame or low-tunnel materials | Lengthens both ends of the season (your season: → 25-01) | → 05-02 |
| [ ] | Containers and potting mix | For a patio, balcony or windowsill | → 05-10, → 05-14 |
| [ ] | Grow light + shelf for seedlings | | → 05-14 |
| [ ] | Watering cans, soaker hose | Hand-watering is many trips | → 05-01 |
| [ ] | ⌛ Fruit trees and bushes, **planted now** | Harvest is years away; choose for your zone, {{ region.home.zone }} | → 05-13 |
| [ ] | Chicken or rabbit setup | Check local rules first (pre-collapse) | → 05-04, → 05-05 |
| [ ] | Fishing tackle{{#if is.cold_winters}}, ice auger and ice-fishing gear{{/if}} | Protein that needs no ammunition | → 05-08 |
| [ ] | №Traps and snare wire | | → 05-15 |
| [ ] | Game processing: knives, sharpener, bone saw, gambrel, game bags | | → 05-09 |
| [ ] | Two regional field guides **with photographs** | Foraging is read-only until you learn in person | → 05-06 |

## 4. Fire, fuel, cooking and heat (→ 06, → 07, → 08)

**Your numbers:** gasoline {{ gear.fuel.gasoline_gal }} gal · diesel {{ gear.fuel.diesel_gal }}
gal · kerosene {{ gear.fuel.kerosene_gal }} gal · propane 1-lb {{ gear.fuel.propane_1lb }},
20-lb {{ gear.fuel.propane_20lb }} · firewood {{ gear.fuel.firewood_cords }} cords · CO alarms
{{ gear.co_alarms }} · smoke alarms {{ gear.smoke_alarms }} · extinguishers
{{ gear.extinguishers }}. What each fuel is: → 29-01.

| ✔ ~ ✗ | Item | Notes | Page |
|---|---|---|---|
| [ ] | **★ Battery CO alarms on every level and outside every sleeping area + spare batteries §** | Non-negotiable with any burning indoors (→ 29-03) | → 08-02 |
| [ ] | CO detector with a number (ppm) display | The number shows a slow leak before the alarm sounds | → 08-02 |
| [ ] | **★ Smoke alarms and fire extinguishers** (ABC type) | → 29-12 | → 26-03 |
| [ ] | **★№ Ignition, three ways**: lighters (many), ferro rod, stormproof matches | Redundancy is cheap here | → 06-01 |
| [ ] | Tinder, bought or homemade | | → 06-01 |
| [ ] | **★⌛ Seasoned firewood**{{#if has.fireplace}} (you have a fireplace){{/if}}{{#if has.wood_stove}} (you have a wood stove){{/if}} | Wood cut today is next year's fuel | → 06-03, → 06-04 |
| [ ] | Axe, splitting maul, wedges, bow saw + spare blades §, chainsaw file | The consumables around the tools go first | → 16-06 |
| [ ] | §Propane: 20-lb cylinders and 1-lb canisters, plus adapters | Bridges the gap before wood becomes the plan. Cylinders larger than 1 lb inside the house: {{choice DC-02}} → 30-03 | → 06-05, → 07-05 |
| [ ] | Approved fuel cans, labelled, and stabiliser | **Fuel is never stored or transferred near an open flame or a running appliance.** Where cans live is a household choice: {{choice DC-05}} → 30-06 | → 06-06 |
| [ ] | Fuel-transport hardware: cans, ratchet straps, an exterior rack | Fuel that cannot ride safely is range you do not have | → 06-08 |
| [ ] | Manual fuel transfer pump, labelled for the one fuel it moves | Can to tank without lifting | → 06-07 |
| [ ] | An indoor-rated heater and its fuel, if heat is your gap | Unvented heaters put all their exhaust in the room. Overnight use: {{choice DC-01}} → 30-02 | → 08-04, → 08-09, → 08-10 |
| [ ] | § Heater spares: wicks, filters, hoses, fuses | A heater you cannot fix mid-winter is not a heater | → 08-09, → 08-10, → 08-07 |
| [ ] | Rocket stove or efficient wood stove | A fraction of the wood of an open fire | → 07-02 |
| [ ] | Cast iron: Dutch oven, skillet, griddle | Works on coals; lasts forever | → 07-04 |
| [ ] | Grill grate, tripod, long tongs, heavy gloves | For outdoor cooking | → 07-01 |
| [ ] | Solar oven, bought or built | Free cooking on a sunny day | → 07-03 |
| [ ] | Chimney brush kit sized to your flue + chimney-fire suppressant | {{#if has.fireplace}}You have a fireplace: measure the flue first.{{else}}Only if you burn wood indoors.{{/if}} | → 06-09 |
| [ ] | Moisture meter for firewood | Burn wood under 20 % moisture | → 08-08 |
| [ ] | Vacuum flasks (thermos), large | One boil keeps water hot for hours and saves fuel | → 07-02 |
| [ ] | Window film, weatherstripping, door sweeps, plastic sheeting, tape | One-room heating hardware | → 08-01, → 08-03 |
| [ ] | Heavy quilts, sleeping bags rated for your coldest nights | Your record low: {{ region.home.record_low_f }} °F | → 08-06, → 11-01 |

## 5. Power and light (→ 09, → 10)

**Your numbers:** power stations {{ gear.station_wh_total }} Wh in total · solar
{{ gear.solar_w_total }} W · generator {{ gear.generator_watts }} W running, fuel
{{ gear.generator_fuel }}, connection {{ gear.house_connection }}. What the units mean: → 29-02.

| ✔ ~ ✗ | Item | Notes | Page |
|---|---|---|---|
| [ ] | **★ Power for medical devices first**: power bank(s) or a power station sized to them | {{#if has.cpap}}CPAP is in this household. {{/if}}{{#if has.oxygen}}Oxygen is in this household. {{/if}}Size to the device's watt-hours per day, measured | → 09-10, → 09-06 |
| [ ] | Solar panels + charge controller + battery or power station | Sized for your December sun, not June's | → 09-02, → 09-05 |
| [ ] | §№ Rechargeable AA/AAA + a charger that runs from 12 V or USB | | → 09-03 |
| [ ] | § Alkaline batteries in the sizes your devices actually take | Check every device | → 09-03 |
| [ ] | 12 V accessories: inverter, socket splitter, jump pack | The car is a generator you already own | → 09-11 |
| [ ] | Multimeter, fuses, wire, connectors | | → 09-08 |
| [ ] | Generator + fuel + an outdoor run spot | **Never run a generator, charcoal, or any engine indoors, in a garage, or near an open window.** | → 09-04 |
| [ ] | Heavy-duty outdoor extension cords sized for the load | **Never connect a generator to house wiring except through a transfer switch, or an interlock kit with the main breaker off. Never backfeed through an outlet with a double-male ("suicide") cord.** | → 09-04, → 29-04 |
| [ ] | **★№ LED headlamp, one per person** + lanterns | Headlamps beat flashlights for work | → 10-01 |
| [ ] | №Candles, lamp oil, oil lamps + spare wicks § | Open flame indoors is a household choice (→ 30-21) | → 10-02 |
| [ ] | Blackout curtains or window covering | Light discipline is security | → 10-05 |

Lithium batteries and power stations can burn; store and charge them as their makers say
(NFPA, Lithium-Ion Battery Safety; → 09-03).

## 6. Medical (→ 12, Section 02) — the full carry kit is → 22-06

| ✔ ~ ✗ | Item | Notes | Page |
|---|---|---|---|
| [ ] | **★ The most legitimate on-hand supply of every daily and rescue medicine your prescribers allow** | The household's medical clock. Ask now (→ 12-07) | → 22-06 |
{{#if has.anaphylaxis}}| [ ] | **★ In-date epinephrine, a pair for every place the allergic person spends time** | A second dose is often needed (CDC, Recognizing and Responding to Anaphylaxis) | → 02-03 |
{{/if}}{{#if has.refrigerated_meds}}| [ ] | **★§ Cold chain for refrigerated medicine**: a 12 V fridge or cooler, a thermometer, an evaporative cooling pouch | → 29-07 | → 12-21, → 09-10 |
{{/if}}| [ ] | **★ Trauma kit**: tourniquet, pressure dressings, wound-packing gauze, and the training | | → 12-02 |
| [ ] | General first-aid supplies; wound closure; splints | | → 12-01, → 12-09, → 12-14 |
| [ ] | Over-the-counter medicines in quantity, adult and child forms, with a written list | **Children do not have access to firearms, fuel, medications or chlorine products.** | → 12-13, → 12-07 |
| [ ] | Oral rehydration salts | Dehydration kills more people in long events than trauma | → 12-05 |
| [ ] | Dental first aid: temporary filling material, clove oil | No dentist for a long time | → 12-06 |
| [ ] | Thermometers: one for people, one for the fridge or medicine store | | → 12-05 |
| [ ] | Spare prescription glasses, reading glasses, hearing-aid batteries | Cheap, and you cannot function without them | → 02-23 |
| [ ] | Lockable box for medicines | Out of children's reach, even in an emergency | → 20-02 |

## 7. Sanitation and hygiene (→ 13)

| ✔ ~ ✗ | Item | Notes | Page |
|---|---|---|---|
| [ ] | **★ Bucket toilet**: buckets, snap-on seat, **§ liners**, cover material (sawdust, peat, ash) | | → 13-01 |
| [ ] | **★§ Bleach and/or pool shock (calcium hypochlorite)** | Doubles for water. **Bleach or pool shock is never mixed with ammonia, acids or other cleaners.** | → 13-11, → 29-05 |
| [ ] | №Soap in bulk; hand sanitiser | And the skill to make more | → 13-02, → 13-09 |
| [ ] | Toilet paper in bulk, plus washable cloth alternatives | | → 13-01 |
| [ ] | Heavy trash bags | | → 13-03 |
| [ ] | Washboard or plunger washer, tubs, wringer, clothesline | Laundry by hand is real work | → 13-04 |
| [ ] | Menstrual supplies (disposable and reusable){{#if has.infant}}; diapers at this size **and the next**{{/if}} | Reusable is the long game | → 13-08 |
| [ ] | Shovel + lime or ash for latrine work | | → 13-07 |
| [ ] | Heavy rubber gloves, N95 masks, eye protection | Waste handling and clean-up | → 13-11 |
{{#if has.pets}}| [ ] | Pet litter and waste bags, and a plan for when they run out | Sand, ash, shredded paper | → 20-09 |
{{/if}}

## 8. Clothing and warmth (→ 11)

| ✔ ~ ✗ | Item | Notes | Page |
|---|---|---|---|
| [ ] | **★ Wool or synthetic base layers for every person**, children included | Cotton holds water and steals heat | → 11-01, → 11-05 |
| [ ] | **★ Insulated waterproof boots** + spare liners for everyone | | → 11-06 |
| [ ] | №Wool socks, many. Mittens over gloves for children | | → 11-04, → 11-02 |
| [ ] | Shell layers, {{#if is.cold_winters}}snow pants, balaclavas, goggles{{else}}rain gear, a warm hat{{/if}} | Your January mean low: {{ region.home.jan_low_f }} °F | → 11-01 |
{{#if has.child}}| [ ] | **⌛ The next two sizes of everything for each child** | The clock nobody plans for | → 11-02, → 11-09 |
| [ ] | Car-seat ponchos or blankets that go over the buckled harness | No bulky coat under a harness (AAP) | → 11-02 |
{{/if}}| [ ] | Drying rack for indoor drying | Gear that never dries is dangerous gear | → 11-03 |
| [ ] | Chainsaw chaps + eye and ear protection | A saw injury with no emergency room is the scenario | → 11-05 |
| [ ] | Sun protection and light layers for summer | {{#if is.hot_summers}}Your July mean high is {{ region.home.jul_high_f }} °F.{{/if}} | → 11-08 |

## 9. Tools and repair (→ 16)

| ✔ ~ ✗ | Item | Notes | Page |
|---|---|---|---|
| [ ] | **★ A good axe, a good knife, a good file** | Best lifetime value of any tools | → 16-01, → 16-02, → 16-06 |
| [ ] | Hand tools: hand drill, hand saws, hammers, pliers, wrenches, vise | Power tools stop; these do not | → 16-01 |
| [ ] | § Sharpening: stones, files, honing compound, strop | A dull tool is a dangerous tool | → 16-02 |
| [ ] | №§ Cordage: paracord, rope, wire, zip ties, duct tape | Never enough | → 16-03 |
| [ ] | Sewing kit: heavy needles, awl, waxed thread, patches | | → 16-04 |
| [ ] | Adhesives and sealants: epoxy, silicone, wood glue | | → 16-05 |
| [ ] | №§ Fasteners: screws, nails, bolts, hose clamps, baling wire | Buy the assortment boxes | → 16-07 |
| [ ] | Tarps, plastic sheeting, lumber, plywood | Roof and window repair | → 08-03, → 16-05 |
| [ ] | Push-fit pipe couplings in your pipe sizes + a small tube cutter | A burst pipe becomes a short repair | → 16-12 |
| [ ] | Bicycle + tubes, patch kit, pump, chain tool; a wagon or sled | Transport when fuel is gone | → 16-09 |
{{#if has.trailer}}| [ ] | Trailer spare wheel, bearing kit, coupler and tongue locks | One bearing or tyre can end a move | → 16-11 |
{{/if}}| [ ] | Work gloves (№), safety glasses, ear protection | Injury is what you cannot afford | → 16-01 |

## 10. Security (→ 14)

Firearms pages are in every binder; these rows matter only if you own them, except storage and
home hardening, which matter to everyone.

| ✔ ~ ✗ | Item | Notes | Page |
|---|---|---|---|
| [ ] | **★ Locking storage for every firearm**, opened by every adult who needs it | **Children do not have access to firearms, fuel, medications or chlorine products.**{{#if has.child}} This household has children.{{/if}} | → 14-14, → 20-02 |
| [ ] | Ammunition for each calibre you own, stored cool and dry{{#if !has.firearms}} (none owned per settings){{/if}} | Match the stamp on the box to the stamp on the gun (→ 29-11) | → 14-07 |
| [ ] | § Cleaning kit, solvent, oil; spare small parts | Small and cheap now, unobtainable later | → 14-05, → 14-06 |
| [ ] | Optic batteries, backup sights | | → 14-09 |
| [ ] | Hearing and eye protection | | → 14-05 |
| [ ] | Home hardening: door reinforcement, locks, window film, exterior lighting | The cheapest security spend there is | → 14-02 |
| [ ] | Outdoor padlocks for gates and sheds, with the keys stored where every adult can find them | A lost key locks you out | → 14-02 |
| [ ] | Pepper spray, one per adult who will carry it | A step between words and a firearm | → 14-13 |
| [ ] | Binoculars, a good light, a whistle | | → 14-01 |

## 11. Communications (→ 15)

| ✔ ~ ✗ | Item | Notes | Page |
|---|---|---|---|
| [ ] | **★ NOAA Weather Radio** (battery or crank, with SAME county coding){{#if has.noaa_radio}}: owned{{/if}} | The best early warning there is (→ 29-09) | → 15-01 |
| [ ] | FRS/GMRS handhelds (№) + rechargeable batteries{{#if has.gmrs}}: owned{{/if}} | Yard-to-neighbourhood range | → 15-02 |
| [ ] | Shortwave or scanner receiver for listening | | → 15-04 |
| [ ] | Amateur ("ham") radio + **a licence earned now**{{#if has.ham}}: in the household{{/if}} | The exam takes time | → 15-05 |
| [ ] | Antenna wire, connectors, coax | | → 15-06 |
| [ ] | Satellite messenger or satellite internet{{#if has.satellite}}: owned; it is a channel only once activated and tested{{/if}} | | → 15-02 |
| [ ] | Printed family comms plan and contact cards | | → 15-03, → 25-08 |
| [ ] | Analog barometer | The pressure trend is a forecast with no forecast | → 17-10 |

## 12. Children, family, documents, morale (→ 19, → 20, → 21)

| ✔ ~ ✗ | Item | Notes | Page |
|---|---|---|---|
| [ ] | **★ Document kit**: copies of everything, waterproof, grab-and-go | | → 19-01 |
| [ ] | **★ Cash in small bills** | Cards stop working with the power | → 19-02 |
| [ ] | Backup drive + paper copies of records | | → 19-03 |
{{#if has.infant}}| [ ] | Diapers and wipes at the current size **and the next**; formula if used | | → 20-06, → 20-05 |
{{/if}}{{#if has.child}}| [ ] | Carriers, child-size work gloves, comfort items | | → 20-01, → 20-07 |
| [ ] | School supplies, printed books, workbooks | The internet goes with the grid | → 20-03 |
{{/if}}{{#if has.pets}}| [ ] | Pet food, carriers, medicines, records | | → 20-09 |
{{/if}}| [ ] | Games, cards, instruments, treats, decorations | Morale is a supply line | → 21-02, → 21-06 |
| [ ] | Paper, pencils, notebooks, a wall calendar | Logs, letters, schooling, sanity | → 21-04, → 25-05 |
| [ ] | This binder installed on more than one charged device | → 00-10 | → 00-01 |

## The ★ list, all together

If you do nothing else: water filter + elements, bleach, water containers, staples you eat,
mylar + oxygen absorbers, special-diet food if anyone needs it, open-pollinated seed, ignition
three ways, seasoned firewood, CO alarms, smoke alarms and extinguishers, power for medical
devices, a headlamp per person, the fullest legitimate medicine supply, rescue medicines in
pairs, a trauma kit, a bucket toilet, bleach or pool shock, base layers and boots for everyone,
an axe, knife and file, locked firearm storage if you own firearms, a NOAA radio, the document
kit, and cash. **Audit against the rows, not this paragraph.**

## When the shops close

This is a list of things to acquire, so "runs out" means **the shops close**.

- **Every ⌛ item becomes unobtainable at that moment**, permanently. Seed, seasoned wood and
  soil cannot be improvised. Buy them first even though they feel least urgent.
- **Every § consumable sets the real life of its tool.** Count the spares, not the tools: that
  is → 22-04, and it feeds → 23-02.
- **Everything above has a scavenged equivalent**: → 22-02. The six categories worth picking up
  whenever you see them are **containers, cloth, fasteners, cordage, fuel and blades**.

## Phase notes

- **A (shelter in place):** the whole list applies; the house is the store.
- **B (moving):** only what fits in the vehicle and the bags (→ 22-03, → 22-05). This list is
  what you are leaving behind, which is why the go-bag contents are chosen from it in advance.
- **C (establish):** the ⌛ items and the ones that produce (→ 23-04) matter most: seed, tools
  and skill.

Related: → 22-07 what to buy first · → 22-02 the scavenging version · → 22-04 inventory log ·
→ 22-03 go-bags · → 22-05 vehicle kit · → 22-06 medical kit · → 23-04 which purchases last ·
→ 23-02 counting what you have. A general national kit list: Ready.gov, Build A Kit.

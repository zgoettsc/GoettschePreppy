---
id: 22-04-household-inventory
section: 22-master-lists-acquire-and-scavenge
title: "Household inventory log"
version: 1
revised: 2026-11-16
layer: household
danger_level: none
phase: [A, B, C]
tags: [inventory, worksheet, counting, runway, insurance, records, locations]
derived_from: [22-04-household-inventory]
sources:
  - internal-revenue-service-reconstructing-records-afte-28669f
  - foodsafety-gov-usda-hhs-food-safety-during-a-power-o-3894c1
  - cdc-how-to-create-and-store-an-emergency-water-suppl-f0c412
  - consumer-financial-protection-bureau-disasters-and-e-44eaa3
related: [23-02-master-consumables-table, 22-01-master-acquisition-list, 22-07-priority-purchase-order, 04-10-rotation-and-inventory, 19-03-records-and-backups, 19-04-insurance-and-claims, 25-05-blank-logs, 25-10-annual-review, 26-02-walk-the-house]
cards: []
explainers: [EX-13, EX-14]
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

# Household inventory log

**What this page is for.** You cannot ration what you have not counted, and you cannot claim
what you cannot prove. This worksheet does three jobs at once: it feeds the "how many days do
we have" numbers in → 23-02, it shows what is still missing from → 22-01, and it is the record
an insurer or a disaster-assistance programme will ask for (→ 19-04). Numbers your settings
already hold are printed; everything else you write in pencil.

## Do this now

1. **Do the count in one sitting, room by room** (route: → 26-02), with a pencil and a phone
   camera. It takes an afternoon, and nothing else in this binder returns more for one
   afternoon.
2. **Photograph every room and every open storage container**, plus serial numbers on anything
   valuable. Store the photos **off-site**: a copy that burns with the house proves nothing
   (IRS, Reconstructing Records After a Disaster; CFPB, Disasters and Emergencies; → 19-03).
3. **Copy the totals into → 23-02.** That is where quantity becomes days.
4. **Set the recount dates**: the same two dates a year as the go-bag check (→ 22-03).
5. **Count the medical rows against the actual boxes and the actual prescriptions**, not memory.

## Four rules that make an inventory useful

1. **Count in units you will use in a decision.** "3 cases" is useless; "36 cans, about 14,000
   calories" answers a question (→ 04-01).
2. **Record the date, always.** An undated inventory is a guess within a month.
3. **Record where it is.** In an emergency someone else needs to find it.
4. **Record the earliest expiry in a group, not the latest.** Rotation is driven by the front
   of the shelf (→ 04-10).

This page is the **stock** view: what exists, where, how much, expiring when. → 23-02 is the
**runway** view: the same numbers divided by daily use. Fill this one first.

## Header

```
INVENTORY DATE: ____________   COUNTED BY: ____________________
NEXT RECOUNT DUE: ____________ PHOTOS STORED AT (off-site): ____________
```

Household: {{ household.size }} people ({{ household.adults }} adults, {{ household.children }}
children){{#if has.pets}}, pets: {{#each pets as p}}{{p.count}} {{p.type}} · {{/each}}{{/if}}.

## Where things are (fill in once, update when you move them)

| Item | Location | Notes |
|---|---|---|
| Electrical panel and main breaker | ____________ | Label the breakers (→ 29-04) |
| Water main shutoff | ____________ | Operate it once (→ 03-02) |
| Gas shutoff and the tool it needs{{#if !has.gas_any}} (none per settings){{/if}} | ____________ | Procedure: → 16-12 |
| Water heater ({{ dwelling.water_heater_gallons }} gal){{#if !has.water_heater_tank}} (tankless or none per settings){{/if}} | ____________ | An emergency water reserve (→ 03-02) |
| Fire extinguishers ({{ gear.extinguishers }}) | ____________ | → 29-12 |
| Smoke alarms ({{ gear.smoke_alarms }}) and CO alarms ({{ gear.co_alarms }}) | ____________ | Battery type? ______ |
| Shelter room{{#if has.shelter_room}}: {{ dwelling.shelter_room }}{{/if}} | ____________ | → 17-06 |
| Medical kit and rescue medicines | ____________ | → 22-06 |
| Go-bags | ____________ | → 22-03 |
| Document kit and cash | ____________ | Location only; never write a safe combination in this binder (→ 19-01) |
| Fuel storage | ____________ | Outside the living space (→ 06-06) |

## A. Medical (count these first, against the boxes)

**The medicines your settings list:**

| Person | Medicine | Strength | Where kept | Expiry | On hand (count) | Days at normal use |
|---|---|---|---|---|---|---|
{{#each meds as x}}| {{x.member}} | {{x.name}} | {{x.strength}} | {{x.where_kept}} | {{x.expiry}} | ______ | ______ |
{{else}}| none entered | | | | | | |
{{/each}}

**Everything else medical:**

| Item | On hand | Unit | Earliest expiry | Location | Notes |
|---|---|---|---|---|---|
{{#if has.epinephrine}}| **Epinephrine devices**, every location | | devices | | | Never rationed (→ 02-03) |
{{/if}}{{#if has.condition.CL-01}}| Diabetes supplies: syringes or pens, sensors, pump parts, test strips, **ketone strips**, glucagon, fast sugar | | | | | → 02-01, → 02-02 |
{{/if}}{{#if has.cpap}}| CPAP filters, masks, tubing | | | | | → 02-24 |
{{/if}}{{#if has.oxygen}}| Oxygen cylinders and tubing | | hours | | | → 02-08 |
{{/if}}| Other device supplies: ______________ | | | | | |
{{#if has.infant}}| Infant formula and feeding supplies | | | | | → 02-13 |
{{/if}}| First-aid consumables (gauze, tape, dressings) | | | | | → 12-01 |
| Trauma items: tourniquets ___ · wound-packing gauze ___ · pressure bandages ___ · CPR mask ___ | | | | | → 12-02 |
| Over-the-counter: adult pain and fever ___ · child pain and fever ___ · dosing syringes ___ · anti-diarrhoeal ___ · oral rehydration salts ___ | | | | | Adult-only items kept apart from children's (→ 12-13) |
| Spare glasses, hearing-aid batteries | | | | | → 02-23 |
{{#if has.pets}}| Pet food and pet medicines | | | | | → 20-09 |
{{/if}}

> **Reconcile this block against your condition pages and → 22-06 every time.** It is the block
> that sets the household's real timeline (→ 23-01).

## B. Water

| Item | On hand | Unit | Location | Notes |
|---|---|---|---|---|
| Stored drinking water | {{ gear.water.stored_gal }} | gallons | | Date filled: ______ |
| Water heater and pipes | {{ dwelling.water_heater_gallons }} | gallons | | Know the drain valve (→ 03-02) |
| Pool or hot tub (raw, not drinkable){{#if !has.pool}} (none per settings){{/if}} | {{ dwelling.pool_gallons }} | gallons | | Treatment: → 03-03 |
| Filters | | units | | Element life left: ______ |
| **Spare filter elements** | | | | |
| Unscented bleach | | fl oz | | **Purchase date:** ______ |
| Pool shock (calcium hypochlorite) | | lb | | Stored sealed, dry, away from fuel (→ 29-05) |
| Purification tablets | | | | Expiry: ______ |
| Empty containers (capacity) | | gallons | | |
| Rain barrels | | gallons | | |

Two-week target for this household: {{ derived.water.two_weeks_gal }} gallons (→ 03-01).

## C. Food

| Category | On hand | Unit | Earliest expiry | Location | Est. calories |
|---|---|---|---|---|---|
| Rice and grains | | lb | | | |
| Beans and lentils | | lb or cans | | | |
| Flour, oats, pasta | | lb | | | |
| Canned meat and fish | | cans | | | |
| Canned vegetables and fruit | | cans | | | |
| **Fats and oils** | | | | | |
| Sugar and honey | | lb | | | |
| **Salt** (canning or pickling) | | lb | | | |
| Powdered or canned milk | | | | | |
| Freeze-dried | {{ gear.food.freeze_dried_servings }} | servings | | | |
{{#if has.anaphylaxis}}| **Allergen-safe food**, in its own bin | | | | | Separate bin (→ 02-04) |
{{/if}}{{#if has.child}}| Food the children reliably eat | | | | | |
{{/if}}| Freezer contents | | lb | | | The clock starts at the outage (→ 04-17) |
| Home-canned jars | | jars | | | Year canned: ______ |
| Dried and dehydrated | | | | | |
| Seeds for sprouting | | | | | |
| **TOTAL ESTIMATED CALORIES** | | | | | **______** |
| **÷ daily household need, {{ derived.calories.day }} kcal** | | | | | **= ______ days** |

## D. Fuel, heat and cooking

| Item | On hand | Unit | Location | Notes |
|---|---|---|---|---|
| Firewood, seasoned | {{ gear.fuel.firewood_cords }} | cords | | Split and stacked since: ______ |
| Firewood, green | | cords | | Not usable this season |
| Propane, 20-lb cylinders | {{ gear.fuel.propane_20lb }} | cylinders | | Full / part / empty: ______ |
| Propane, 1-lb cylinders | {{ gear.fuel.propane_1lb }} | cylinders | | |
| Kerosene | {{ gear.fuel.kerosene_gal }} | gal | | Date bought; jar-checked (→ 29-01) |
| Gasoline | {{ gear.fuel.gasoline_gal }} | gal | | Stabilised on: ______ (→ 06-06) |
| Diesel | {{ gear.fuel.diesel_gal }} | gal | | |
| Charcoal | | lb | | Outdoors only |
| Vehicle fuel in the tanks | | gal | | |
| Lighters, matches, ferro rods | | | | |
| Stoves | | | | |

**Heaters your settings list:**
{{#each heaters as h}}- {{h.kind_text}}: {{h.model}}. Location: ____________. Spare wicks, filters or fuses: ____________
{{else}}- None entered.
{{/each}}

## E. Power and light

| Item | On hand | Capacity | Location | Notes |
|---|---|---|---|---|
{{#each stations as s}}| Power station: {{s.model}} | 1 | {{s.wh}} Wh | | Charged on: ______ (→ 09-03) |
{{/each}}{{#each panels as pn}}| Solar panels: {{pn.model}} | {{pn.count}} | {{pn.watts}} W each | | Label: open-circuit volts {{pn.voc}}, short-circuit amps {{pn.isc}} (→ 28-07) |
{{/each}}{{#if has.generator}}| Generator | 1 | {{ gear.generator_watts }} W running | | Fuel {{ gear.generator_fuel }} · {{ gear.generator_volts }} · connection {{ gear.house_connection }} (→ 09-04) |
{{/if}}| Power banks | | Wh | | Medical devices first (→ 09-10) |
| AA, AAA and other batteries | | count | | Expiry: ______ |
| Rechargeables + charger | | | | |
| Headlamps and flashlights | | count | | One per person: {{ household.size }} |
| Candles and lamp oil | | | | |

Totals from settings: {{ gear.station_wh_total }} Wh of power station, {{ gear.solar_w_total }} W of solar.

## F. Sanitation and hygiene

| Item | On hand | Unit | Location | Days |
|---|---|---|---|---|
| Toilet paper | | rolls | | |
| **Bucket and bin liners** | | count | | Usually runs out first |
| Soap and detergent | | | | |
| Bleach (sanitation share) | | | | Same bottle as water: **count once** |
{{#if has.infant}}| Diapers, size ___ | | count | | Sizes change! |
| Wipes | | | | |
{{/if}}| Menstrual supplies | | | | |
| Cover material (sawdust, peat, ash) | | | | |
| Gloves and N95 masks | | | | |
{{#if has.pets}}| Pet litter and waste bags | | | | |
{{/if}}

## G. Clothing, tools, security, comms

**Clothing per person** (fits **now**?):

| Person | Base layers | Insulated boots | Warm coat | Hat and mittens | Next size on hand |
|---|---|---|---|---|---|
{{#each members as m}}| {{m.label}} ({{m.age_text}}) | | | | | |
{{/each}}

| Item | Count | Notes |
|---|---|---|
| Sleeping bags and heavy blankets | | Temperature rating: ______ |
| Axes, saws, files | | |
| Sharpening stones | | |
| Cordage, tape, fasteners | | |
| Sewing and repair supplies | | |
| Firearms storage (locked){{#if !has.firearms}} (no firearms per settings){{/if}} | | → 14-14 |
| Ammunition, calibre ______ | | Stored cool and dry (→ 14-07) |
| Ammunition, calibre ______ | | |
| Ammunition, calibre ______ | | |
| Cleaning supplies and spare parts | | → 14-05, → 14-06 |
| NOAA weather radio, SAME code programmed: ______ | | → 15-01 |
| Two-way radios | | Batteries: ______ |
| Cash on hand, small bills | | → 19-02 |

**Vehicles your settings list:**
{{#each vehicles as v}}- {{v.type_text}} ({{v.fuel_text}}; four-wheel drive {{v.four_wheel_drive}}; can tow {{v.can_tow}}): spare tyre present? ____ jack? ____ kit checked on ______ (→ 22-05)
{{else}}- None entered.
{{/each}}

## H. Summary (copy to → 23-02)

```
SHORTEST RUNWAY: ______________________ = ______ days   <- this governs the plan
Water: ______ days    Food: ______ days    Heat/fuel: ______ days
Power: ______ days    Sanitation: ______ days    Medical: ______ days

TOP 5 GAPS TO BUY (feed into 22-07):
1. ______________________  4. ______________________
2. ______________________  5. ______________________
3. ______________________

NEXT RECOUNT: ______________
```

## What to do with the finished sheet

- **One copy in the binder** (or photographed into the app's photo slots), one **stored
  off-site** (→ 19-03), and the photo-inventory status on → 19-04 updated.
- **Copy the numbers to → 23-02** and re-rank → 22-07.
- **Give a copy to every adult.** An inventory only one person knows is a single point of
  failure.
- **Keep last year's sheet.** The difference between two years is your real rate of use,
  better data than any estimate in this binder.

**What you need:** a clipboard, pencils, a tape measure, a kitchen or luggage scale, a
permanent marker and labels, a phone for photos, and a fireproof, waterproof box for the paper
copy (→ 19-01). **Pencil, not pen:** pens freeze and run; pencil works wet and cold and erases
when counts change.

## When it goes stale

- **How long it stays true:** about **six months**, less if you are using your stores.
- **Never skip the medical block** to save time; it is the one that matters.
- **Refresh:** the twice-a-year recount, on the go-bag dates (→ 22-03).
- **A guessed inventory is worse than none**, because it produces confident, wrong decisions on
  → 01-02.

## Phase notes

- **A (shelter in place):** full inventory twice a year, plus a running log of what is used
  (→ 25-05).
- **B (moving):** the only inventory that matters is what is in the vehicle and the bags.
  **Count it at each stop**, out loud, so every adult knows (→ 01-03).
- **C (establish):** restart the full inventory in the first week. **What you arrived with is
  your whole world** until production starts (→ 23-04).

Related: → 23-02 turns these counts into days · → 22-01 what the gaps mean you should buy ·
→ 22-07 spending order · → 04-10 food rotation · → 19-03 off-site copies · → 19-04 insurance ·
→ 25-05 more blank logs · → 25-10 annual review.

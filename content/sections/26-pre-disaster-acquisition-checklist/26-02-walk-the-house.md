---
id: 26-02-walk-the-house
section: 26-pre-disaster-acquisition-checklist
title: "Walk the house, room by room"
version: 1
revised: 2026-11-16
layer: core
danger_level: none
phase: [A]
tags: [walk-through, rooms, route, shutoffs, photos, checklist]
derived_from: [26-02-walk-the-house]
sources:
  - cdc-carbon-monoxide-poisoning-basics-772153
  - american-red-cross-winter-storm-preparedness-and-bli-4bb6c0
  - internal-revenue-service-reconstructing-records-afte-28669f
  - fema-ready-gov-utility-shut-off-and-safety-natural-g-7965ad
related: [26-01-how-to-run-the-check, 26-03-checklist-life-safety, 26-04-checklist-water-food, 26-05-checklist-heat-power-light, 26-06-checklist-shelter-tools-security, 26-07-checklist-family-records, 26-08-expiry-and-rotation-tracker, 08-02-carbon-monoxide-safety, 06-06-fuel-storage-safety, 03-02-storing-water, 19-03-records-and-backups, 19-04-insurance-and-claims, 22-03-go-bags-and-kits, 00-04-family-emergency-plan]
cards: [DC-05]
explainers: [EX-03, EX-04, EX-12]
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

# Walk the house, room by room

**What this page is for.** The checklists are organised by subject (water, heat, tools). Your
home is organised by room. This page is the route that joins the two: walk it once, in order,
and you cover everything without doubling back. **Photograph each room and each open container
as you go**: that record is also your insurance evidence (IRS, Reconstructing Records After a
Disaster; → 19-04).

Our home: {{ dwelling.type }}, {{ home.setting }}. Basement: {{ dwelling.basement }}. Water:
{{ dwelling.water_supply }}. Sewer: {{ dwelling.sewer }}. Main heat: {{ dwelling.primary_heat }}.

## Do this now

1. **Follow the route below in order.** It ends at the door with the go-bags, which is where the
   walk should finish.
2. **Check the fixed safety items where they are** (alarms, extinguishers, shutoffs). They
   cannot be judged from a shelf.
3. **Open every closed container.** The unlabelled bucket in the basement is exactly what this
   walk is for.

## The route

Work from the inside rooms outward and top down, so you never carry things past a room you have
finished. Skip any room you do not have; do not skip a room because it is messy.

### 1. Kitchen

| Look for | Checklist |
|---|---|
| Pantry staples, canned goods, oils, salt, sugar{{#if has.anaphylaxis}}; **the allergen-safe bin**{{/if}} | → 26-04 |
| Fridge and freezer contents (and what a two-day power cut would cost) | → 26-04 |
| Water containers, bottled water, filter, bleach (**note the purchase date**) | → 26-04 |
| Pots big enough to boil water, cast iron, a manual can opener, a kettle | → 26-04, → 26-05 |
| Canning gear: canner, jars, **lids** (single-use: count them) | → 26-04 |
| Refrigerated medicine, if it lives here: is it out of children's reach? | → 26-03 |
| First-aid kit if it lives here; fire extinguisher; **smoke alarm nearby** | → 26-03 |
| Matches, lighters, candles in drawers | → 26-05 |

**The kitchen question:** *if the power went off right now, what could I cook, and how?*

### 2. Bathrooms

Medicine cabinet (**every expiry date: copy to → 26-08**), over-the-counter medicines,
first-aid supplies, soap, toilet paper, menstrual supplies{{#if has.infant}}, diapers and wipes{{/if}},
**spare glasses**, a thermometer. **Children do not have access to firearms, fuel, medications or
chlorine products.**

**The bathroom question:** *how many days of every medicine are actually here?*

### 3. Bedrooms and closets

Base layers, coats, boots, hats, mittens, wool socks: **for each person, in the size that fits
now**. Blankets, sleeping bags (note the temperature rating), spare bedding.{{#if has.child}}
**Each child's next two sizes.**{{/if}} A smoke alarm in or outside every sleeping area, and a CO
alarm outside every sleeping area (CDC, Carbon Monoxide Poisoning: Basics).

**The bedroom question:** *could everyone dress for {{#if is.cold_winters}}the coldest night here ({{ region.home.record_low_f }} °F on record){{else}}a cold, wet night{{/if}}, right now?*

{{#if has.child}}
### 4. Children's rooms

Comfort items, children's medicines (out of reach), books and games that need no screen,
whistles, clothing in the next sizes{{#if has.infant}}; diapers and wipes at the **current** size,
formula and feeding gear, carriers{{/if}}.

**The children's question:** *what will each child need in the next three months that we do not
have?*
{{/if}}

### 5. Living areas

Lighting: lamps, candles, headlamps, flashlights: **turn each one on**. Board games, cards,
books, paper and pencils.{{#if has.fireplace}} Fireplace tools; the damper works.{{/if}} Blackout
curtains.

### 6. {{#if has.basement}}Basement and utility room{{else}}Utility closet or laundry{{/if}}

| Look for | Checklist |
|---|---|
| **Water heater**{{#if has.water_heater_tank}} ({{ dwelling.water_heater_gallons }} gal){{/if}}: **find the drain valve** | → 26-04 |
| **Water main shutoff. Operate it.**{{#if has.gas_any}} **Gas shutoff and the tool it needs**{{/if}} (FEMA, Utility Shut-off and Safety) | → 26-06 |
| Electrical panel: which breaker is which; the main breaker (→ 29-04) | → 26-05 |
| Bulk food storage, buckets, mylar, cool storage space | → 26-04 |
| Bucket-toilet supplies, cover material, liners, bleach | → 26-06 |
| Sump pump and any backup | → 26-06 |
{{#if has.well}}| **Well pump, pressure tank, and how the pump is wired** | → 03-10 |
{{/if}}{{#if has.septic}}| Septic access and what a long outage means for it | → 13-12 |
{{/if}}

**The utility question:** *can every adult find and operate every shutoff in the dark?*

### 7. {{#if has.garage}}Garage, shed{{else}}Storage space, shed or storage unit{{/if}}

| Look for | Checklist |
|---|---|
| Hand tools, axes, saws, files, sharpening stones, vise | → 26-06 |
| **Fuel: propane cylinders, gasoline, kerosene, stabiliser**: labelled, caps tight, away from ignition. Where fuel is stored is a household choice: {{choice DC-05}} → 30-06 | → 26-05 |
| Generator, solar gear, batteries, power banks, chargers, extension cords | → 26-05 |
| Cordage, tape, fasteners, tarps, plastic sheeting, lumber | → 26-06 |
| Camping gear: stove, lanterns, sleeping pads, tent | → 26-05, → 26-06 |
| Garden tools, seed, containers, hose, compost | → 26-04 |
| Bicycles, tubes, patch kit, pump, wagon{{#if is.snow_region}}, sled{{/if}} | → 26-06 |
| Firearms, ammunition by calibre, cleaning kit, spare parts: **locked** | → 26-06 |

**Fuel is never stored or transferred near an open flame or a running appliance.**
**The garage question:** *which tool do I own whose consumable I do not?*

### 8. Vehicles

{{#each vehicles as v}}- {{v.type_text}}: kit, blankets, shovel, traction, jump pack, first aid, water,{{#if has.child}} children's gear in the current size,{{/if}} paper maps, cash, **fuel level**, spare tyre and jack.
{{else}}- No vehicle entered. If you borrow or rent one in an emergency, the vehicle kit (→ 22-05) goes with you.
{{/each}}

Note anything a parked car's summer heat or winter cold has ruined (→ 22-05).
**The vehicle question:** *if we were stranded tonight, in tonight's weather, for twelve hours?*

### 9. Office and files

Documents (IDs, passports, deeds, titles, insurance, prescriptions), cash, backup drive,
**off-site copies**, printed contact list, this binder on a charged device. **Photograph the
document kit** (→ 19-03).
**The office question:** *if the house burned tonight, what could we not replace?*

### 10. Yard and outside{{#if has.apartment}} (balcony, building, shared spaces){{/if}}

{{#if has.apartment}}Stairwells and exits (two ways out), the building's water and gas shutoffs and who has the
keys, any storage unit, a balcony for a grill or solar panel if the building allows it.{{else}}Firewood: **how much, and is it really seasoned?** Rain barrels and gutters, garden beds,
{{#if has.pool}}the pool or hot tub and its equipment, {{/if}}{{#if has.outdoor_fire}}the fire pit or outdoor fireplace, {{/if}}fencing, outdoor
lighting, downspouts{{#if is.snow_region}}, snow shovels{{/if}}.{{/if}}
**The outside question:** *how many days of cooking and heating are really out there?*

### 11. Finish at the door

Go-bags: **open each one and check it against → 22-03**, weigh it, check every expiry, and
re-size the clothing inside.{{#if has.pets}} Pet carriers.{{/if}} The medical kit.
**The door question:** *could we be out of here in sixty seconds with everything that matters?*

### 12. Anything kept somewhere else

The rooms cannot answer this one: **what already lives somewhere else, and what should?**

{{#each destinations as d}}- **{{d.name}}** ({{d.status_text}}): what is already there? ______ · what should ride there on the next visit? ______ · has anyone there agreed to hold it, and where? ______
{{else}}- No destination entered. If you agree one later, a tote per visit beats hauling everything on the worst day (→ 01-05).
{{/each}}
- Storage unit, workplace, a relative's house: ______________________
- Where is the list of things kept elsewhere, so it counts in → 22-04? ______________________

## Fixed safety items: check these where they are

| ✔ | Item |
|---|---|
| [ ] | **Smoke alarm** in or near every sleeping area and on every level: test pressed, battery fresh (we have {{ gear.smoke_alarms }}) |
| [ ] | **CO alarms** on every level and outside every sleeping area: test pressed (we have {{ gear.co_alarms }}) (→ 08-02) |
| [ ] | **Fire extinguishers**: in date, reachable, every adult knows how (PASS: → 29-12) (we have {{ gear.extinguishers }}) |
| [ ] | **Water main shutoff**: found, **operated**, the tool present if one is needed |
| [ ] | **Gas shutoff**{{#if !has.gas_any}} (none per settings){{/if}}: found; the wrench hung beside it; every adult has seen it |
| [ ] | **Electrical panel**: labelled; every adult knows the main breaker |
| [ ] | **Water heater drain valve**: found, and a hose that fits it (→ 03-02) |
| [ ] | **Shelter spot**{{#if has.shelter_room}} ({{ dwelling.shelter_room }}){{/if}}: clear, stocked, shoes and a light there (→ 17-06) |
| [ ] | **Window escape routes** clear; ladders for upstairs bedrooms |
| [ ] | **Fuel** stored away from the living space and ignition, in labelled containers (→ 06-06) |

## The room-by-room tally

```
ROOM              ✔    ~    ✗    BIGGEST GAP FOUND
Kitchen         ____ ____ ____  ________________________________
Bathrooms       ____ ____ ____  ________________________________
Bedrooms        ____ ____ ____  ________________________________
Children's      ____ ____ ____  ________________________________
Living areas    ____ ____ ____  ________________________________
Utility         ____ ____ ____  ________________________________
Garage / shed   ____ ____ ____  ________________________________
Vehicles        ____ ____ ____  ________________________________
Office / files  ____ ____ ____  ________________________________
Outside         ____ ____ ____  ________________________________
Go-bags         ____ ____ ____  ________________________________

PHOTOS TAKEN? ____    STORED OFF-SITE? ____        (19-03)
```

**What you need:** a clipboard, pencils, a battery tester, a headlamp (basements and crawl
spaces), a tape measure, and a phone for photos. Nothing else but time; **do not skip the photo
record**: it takes minutes and it is what an insurer asks for.

## When it goes stale

- The walk is good for a year; **the expiry dates you collect are good for months**.
- **If you only walk three places,** walk the **bathroom cabinet, the garage and the go-bags**:
  that is where the worst gaps hide.
- Re-walk the go-bags on the two kit-check dates (→ 22-03), and everything yearly (→ 25-10).

## Phase notes

- **A (shelter in place):** the whole route.
- **B (moving):** only the vehicle and go-bag stops matter.
- **C (establish):** re-walk everything in the first week; a new building has different
  shutoffs, storage and hazards.

Related: → 26-01 the method · → 26-03 to → 26-07 the checklists · → 26-08 expiry · → 08-02 CO
alarms · → 06-06 fuel storage · → 03-02 the water heater as a reserve · → 19-03 and → 19-04 the
photo record · → 22-03 the go-bag check · → 00-04 shutoff photos.

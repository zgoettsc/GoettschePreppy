---
id: 22-05-kit-vehicle
section: 22-master-lists-acquire-and-scavenge
title: "Vehicle kit"
version: 1
revised: 2026-11-16
layer: household
danger_level: caution
phase: [A, B, C]
tags: [vehicle, car kit, stranded, winter, heat, evacuation, spare tyre, trailer, cargo]
derived_from: [22-05-kit-vehicle]
sources:
  - american-red-cross-winter-storm-preparedness-and-bli-4bb6c0
  - noaa-national-weather-service-winter-weather-safety-49fc7a
  - osha-cold-stress-protecting-workers-in-cold-environm-56bc81
  - cdc-carbon-monoxide-poisoning-basics-772153
  - us-fda-information-regarding-insulin-storage-and-swi-6448d3
  - nhtsa-us-department-of-transportation-trailer-safety-807982
  - american-academy-of-pediatrics-healthychildren-org-w-7400c5
  - noaa-national-weather-service-heat-safety-66fd15
related: [22-03-go-bags-and-kits, 22-06-kit-medical, 22-01-master-acquisition-list, 01-02-go-no-go-decision, 01-03-phase-b-movement, 01-07-evacuating-with-medical-needs, 17-01-blizzards-and-ice, 08-02-carbon-monoxide-safety, 08-05-hypothermia-frostbite, 11-02-keeping-kids-warm, 06-06-fuel-storage-safety, 06-08-fuel-transport, 16-09-bicycle-and-transport, 16-10-tire-failures-roadside, 16-11-trailer-maintenance-and-repair, 25-04-maps]
cards: [DC-06, DC-08, DC-20]
explainers: [EX-03, EX-01]
promote_when: [has.vehicle]
photo_slots:
  - { id: vehicle-kit-stowed, caption: "Where the vehicle kit rides, and what is under the cargo floor (spare? jack?)" }
  - { id: door-jamb-sticker, caption: "The tyre and loading sticker on the driver's door frame: payload and tyre pressures" }
figures: []
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: null
---

# Vehicle kit

**What this page is for.** The kit that lives in each vehicle all year, the add-ons for your
seasons, and the evacuation load that waits in the house ready to go in. It also covers the
spare tyre, how much a vehicle can really carry, and why medicine and batteries ride in a
vehicle but never live in one.

> **CAUTION.**
> - **If you are stranded in a winter storm, stay with the vehicle.** It is shelter, and it is
>   what searchers look for (NWS, Winter Weather Safety; American Red Cross, Winter Storm
>   Safety).
> - **Before running the engine for heat, clear snow from the exhaust pipe and crack a window.**
>   Carbon monoxide builds up silently (CDC, Carbon Monoxide Poisoning: Basics; → 29-03).
>   **Never run a generator, charcoal, or any engine indoors, in a garage, or near an open
>   window.**
> - **Medicine never stays in a parked vehicle.** It leaves with a person at every stop
>   (FDA, Insulin Storage in an Emergency; → 01-07).
> - **Never leave a child or a pet in a parked vehicle**, in any season (NWS, Heat Safety).

## Do this now

1. **Build the all-year kit below for each vehicle**, in one duffel or tote so it stays one
   grabbable unit.
{{#if is.cold_winters}}2. **Add the winter add-on before the first snow** and leave it in until spring. The storm that
   strands you is never the one you planned around.
{{else}}2. **Add the seasonal add-on that fits your weather** (winter or heat, below).
{{/if}}3. **Keep the fuel tank at least half full**{{#if is.cold_winters}} all winter{{/if}}. Our line:
   never below ______ (NWS, Winter Weather Safety, advises a tank near full in winter).
{{#if has.child}}4. **Put a spare hat, mittens and boots in each vehicle for every child, in the size that fits
   now.** Children get stranded in whatever they wore to school.
{{/if}}5. **Look under the cargo floor today:** is there a spare tyre, a jack and a wrench? Write it
   in the table below. Many newer vehicles, hybrids and EVs carry none.
6. **Check the kit on the go-bag dates** (→ 22-03).

{{photo vehicle-kit-stowed}}

## Our vehicles

| Vehicle | Fuel | Four-wheel drive | Can tow | Spare tyre? | Jack + wrench? | Payload (door sticker) | Kit checked |
|---|---|---|---|---|---|---|---|
{{#each vehicles as v}}| {{v.type_text}} | {{v.fuel_text}} | {{v.four_wheel_drive}} | {{v.can_tow}} | ____ | ____ | ______ lb | ______ |
{{else}}| No vehicle entered | | | | | | | |
{{/each}}

{{#if !has.vehicle}}No vehicle is entered in settings. Read this page anyway: a borrowed or rental vehicle in an
evacuation needs the same kit, and the rules for medicine and fuel do not change.
{{/if}}

## The three jobs of a vehicle kit

| Job | Example | What it demands |
|---|---|---|
| **Stranded** | Storm, ditch, breakdown, closed highway | **Warmth or cooling, water, light, being seen, patience** |
| **Getting yourself out** | Stuck in snow or mud, dead battery, flat tyre | Traction, tools, a way to jump-start |
| **Evacuation** | The Phase B drive (→ 01-03) | Fuel, water, food, navigation, the family's kit |

Most car-kit lists only cover the second job. In cold or hot country the first one is the one
that kills, and it is mostly a temperature-and-water problem.

## If you are stranded: the rules, in order

1. **Stay in the vehicle.** Walking in a whiteout or extreme heat is how people get lost
   (NWS; American Red Cross).
2. **Make yourself visible.** Bright cloth on the antenna or door handle; dome light on while
   the engine runs; hazard lights sparingly.
3. **Before running the engine: clear the exhaust pipe**, every time, and **crack a window on
   the side away from the wind.** Run it about **10 minutes an hour**, not continuously
   (American Red Cross, Winter Storm Safety; CDC; → 08-02).
4. **Insulate.** Blankets, sleeping bags, everyone in one space. Move arms and legs now and
   then to keep blood moving (OSHA, Cold Stress).
5. **Water first, food second.** Do not eat snow: it costs body heat; melt it (→ 03-06).
6. **Call or text your location** while you still have signal, then save the phone's battery
   (→ 00-10).
7. **Watch the children constantly.** Small bodies cool and overheat faster (→ 11-02, → 08-05).

## The kit: all year, every vehicle

| ✔ | Item | Why |
|---|---|---|
| [ ] | **Water**, rotated (it may freeze; leave room in the bottle) | The first shortage |
| [ ] | Shelf-stable food{{#if has.anaphylaxis}}, **safe for the person with the food allergy** (→ 02-04){{/if}}; extra snacks for children | |
{{#if has.condition.CL-01}}| [ ] | **Fast sugar**, clearly marked | For anyone with diabetes (→ 02-01) |
{{/if}}| [ ] | First-aid kit + trauma items (→ 12-01, → 12-02) | |
| [ ] | **Headlamp or flashlight + spare batteries** | Roadside work is night work |
| [ ] | Phone cables, 12 V adapter, **jump pack** (also charges devices) | → 09-11 |
| [ ] | Multi-tool, knife, duct tape, zip ties, work gloves | |
| [ ] | Tow strap, jumper cables | |
| [ ] | Spare tyre **checked**, jack, wheel wrench, **tyre plug kit, 12 V compressor**, tyre gauge | A flat you cannot fix is a stranding (→ 16-10) |
| [ ] | Fluids: oil, coolant, washer fluid{{#if is.cold_winters}} rated for winter{{/if}} | |
| [ ] | Fire extinguisher | → 29-12 |
| [ ] | **Paper maps** of home, destinations and the states between, + a compass | Phones and networks fail first (→ 25-04) |
| [ ] | **Printed contact and meeting-place card** (→ 15-03, → 25-08) | Phones die; paper does not |
| [ ] | Cash in small bills (→ 19-02) | |
| [ ] | Whistle, signal mirror, bright cloth | Being seen |
| [ ] | Trash bags, wipes, hand sanitiser{{#if has.infant}}, **diapers and wipes**{{/if}} | → 13-08 |
| [ ] | Rain gear, spare clothing for everyone who rides in it | |
| [ ] | Notebook and **pencil** | Pens fail in the cold |

## Winter add-on{{#if is.cold_winters}} (applies here: January mean low {{ region.home.jan_low_f }} °F){{/if}}

| ✔ | Item | Why |
|---|---|---|
| [ ] | **A sleeping bag or heavy wool blanket for every seat** | The single most life-saving item in a winter vehicle |
| [ ] | **Extra hats, mittens, wool socks, insulated boots**{{#if has.child}}, children's in the size that fits now{{/if}} | People get stranded dressed for the car, not the ditch |
| [ ] | Emergency blankets or bivvies, one per person | Cheap, tiny, effective |
| [ ] | Hand and body warmers | **Outside the inner layer** for anyone too young to tell you a warmer is burning them: the packets warn against direct skin contact |
{{#if has.young_child}}| [ ] | **A blanket or poncho that goes over the buckled car-seat harness** | No bulky coat under the harness; the top layer must come off easily so the child does not overheat once the cabin warms (AAP, Winter Car Seat Safety Tips; → 11-02) |
{{/if}}| [ ] | **Full-size shovel** (not a folding toy) | Digging out and clearing the exhaust |
| [ ] | Traction: sand, cat litter or traction boards; tyre chains if you carry them | |
| [ ] | Ice scraper and snow brush | |
| [ ] | Candle in a metal can + lighter | A little heat and light, with a window cracked. Open flame in a closed space is a household choice: {{choice DC-20}} → 30-21 |
| [ ] | Bright flagging cloth | Being found |
| [ ] | Snow pants for whoever will dig | |

## Heat add-on{{#if is.hot_summers}} (applies here: July mean high {{ region.home.jul_high_f }} °F){{/if}}

| ✔ | Item | Why |
|---|---|---|
| [ ] | Extra water, more than you think | Heat illness starts with dehydration (→ 17-04) |
| [ ] | Sunshade for the windshield, a light-coloured cover for children's seats | A closed car heats far past the outside temperature (NWS, Heat Safety) |
| [ ] | Wide hats, light long sleeves, sunscreen | |
| [ ] | A battery fan and a spray bottle | Moving air and evaporation |
| [ ] | Insulated medicine pouch | Medicine still leaves with a person (→ 29-07) |

{{#if is.wildfire_region}}**Wildfire country:** N95 masks for everyone, goggles, and the tank kept fuller in fire
season; know two ways out (→ 17-14).
{{/if}}{{#if is.hurricane_region}}**Hurricane country:** fill the tank when a storm is first forecast; stations close early
(→ 17-13).
{{/if}}{{#if is.flood_region}}**Flood risk:** never drive into water over the road; a small depth of moving water can float
a car (→ 17-03).
{{/if}}

## The evacuation load (waits in the house, loads in minutes)

Pre-stage it in one place so loading is not a decision (→ 01-06):

1. **First: the medical load-out from → 01-07.**{{#if has.refrigerated_meds}} This household has
   refrigerated medicine: the running cooler goes in first, in the cabin, thermometer in range.{{/if}}
   Medicine and the medical kit (→ 22-06) ride **in the cabin with a person**, never the trunk,
   a trailer or a roof box.
2. The go-bags and the household bag (→ 22-03).
3. Water containers (fill them on the way out if there is time).
4. Food bin, stove and fuel.
{{#if has.pets}}5. Pet carriers, food, litter (→ 20-09).
{{/if}}6. Sleeping bags, tarp or tent, ground pads; tools, cordage, tape.
7. **Documents, cash, drives** (→ 19-01).
8. **Fuel cans, filled and stabilised** (→ 06-06, → 06-08), outside the passenger space: on a
   hitch carrier or in a trailer. Whether cans may ever ride inside the vehicle, in the cargo
   area, for the shortest possible leg, is a household choice: {{choice DC-06}} → 30-07.
   **Fuel is never stored or transferred near an open flame or a running appliance.**

## The spare tyre

**Many newer vehicles, most EVs and many hybrids have no spare**; they carry a sealant and
inflator kit, which cannot fix a sidewall cut, a blowout or a hole larger than a nail.
{{#if has.hybrid}}A hybrid is in this household: check its cargo floor today.{{/if}}{{#if has.ev}}
An EV is in this household: check its cargo floor today.{{/if}}

The roadside ladder, cheapest first (→ 16-10 has the full procedure):

1. **A bad valve core** causes many slow leaks: a valve tool and spare cores fix it.
2. **A tyre plug kit with steel T-handles + a 12 V compressor + a pencil gauge.** Plugs fix most
   tread punctures and can be used again and again. They are a get-home repair; never plug a
   sidewall. **Practise one plug on a scrap tyre**: it takes real force the first time.
3. **One can of sealant** as the last layer: tread holes only, temporary, and it gums the tyre
   pressure sensor and the rim, so shops may refuse to patch afterwards.
4. **A real spare for long trips:** a used wheel and tyre matching the size on the door-jamb
   sticker, a jack, a breaker bar and a torque wrench, strapped in the cargo area. **Do one
   practice wheel change in the driveway.**

## How much the vehicle can really carry

{{photo door-jamb-sticker}}

- **Payload is the limit that binds.** The sticker on the driver's door frame gives the most
  the vehicle can carry: every pound of people, pets, cargo **and trailer tongue weight**
  counts against it. Write each vehicle's number in the table above.
- **Add up the people first.** Weigh everyone, add car seats and pet carriers, and subtract from
  payload. What is left is all the cargo you have. Water weighs about 8.3 lb a gallon (→ 25-02),
  which is why a moving family carries a day or two of water plus a way to treat more, never
  its storage tanks (→ 03-01).
- **A hitch carrier** (a tray or box on a rear hitch) carries heavy items outside the cabin:
  fuel cans, the spare, tools. Its weight is on the tongue; the vehicle's tongue limit, not the
  hitch's rating, decides. **One receiver holds one thing:** a tray or a trailer, not both.
- **A roof box** suits the light, bulky half of the load (sleeping bags, clothing, diapers). Read
  the roof load limit in the owner's manual: it is small. **Never medicine** (a roof box is a
  freezer in winter and an oven in summer), **never firearms or documents.** Expect worse fuel
  use and know your new height.
- **A trailer** is the biggest capacity multiplier. Load about **10 to 12 percent of the
  trailer's loaded weight on the tongue**, heavy items over the axle (NHTSA, Trailer Safety);
  never exceed the vehicle's towing and tongue limits from the owner's manual. Backing a trailer
  is a skill: practise before it matters (→ 16-11). **Nothing alive rides in a trailer**, and
  neither do medicines or documents.
- **Do one test pack:** load the real totes into the real vehicle, seats in family
  configuration. "If it does not fit, it does not go" (→ 01-03) is only knowable by loading.

```
VEHICLE: ________________  PAYLOAD (sticker): ______ lb
People + car seats + pets: ______ lb   Left for cargo: ______ lb
Tow limit (manual): ______ lb   Tongue limit (manual): ______ lb
Roof load limit (manual): ______ lb   Range on a full tank: ______ mi
```

**Loading rules, whatever the setup:** heaviest items low, forward and inside; bulky-light up
top; fuel outside the passenger space; medicine and the medical kit in the cabin with a person.
Firearms travel unloaded, cased and out of reach, so they cannot shift, fire or be grabbed at a
stop. Never load so heavily that the vehicle squats.

> **Before the collapse:** laws on carrying firearms in vehicles differ by state and change at
> state lines. Unloaded and cased is the usual baseline; check each state on the route
> (→ 14-11).

## Fuel discipline

- **Set a refuelling line and keep it.** Ours: ______ of a tank.
- **Each vehicle is a tank of fuel**, plus stabilised cans stored outside the living space,
  away from ignition (→ 06-06).
- **In an evacuation, fuel is the range limit and stations may be down** (→ 01-03). Range in
  the tanks plus what you carry is your true radius: write it on the map (→ 25-04).
- **When fuel is gone, the vehicle becomes shelter and storage.** Bicycles, a wagon{{#if is.snow_region}}
  and a sled{{/if}} are the transport plan after that (→ 16-09).

## Medicine and batteries ride in a vehicle; they never live in one

- **A parked car runs far below freezing in winter and far above most medicine labels in
  summer.** Freezing destroys insulin with no sign; heat degrades insulin and epinephrine
  (FDA, Insulin Storage in an Emergency; → 29-07). **A frozen-then-thawed insulin vial or pen
  is discarded.** Heat-exposed medicine: {{choice DC-08}} → 30-09.
- Medicine lives in an **insulated pouch that travels with the person**, in and out every time.
- **Fast sugar** can live in the car permanently: it is stable, and it is what you will want
  fastest.
- **A vehicle-stored rescue device is better than none**, but treat it as a backup that is
  replaced on schedule, never the primary.
- **Lithium batteries and power stations** have charge and storage temperature limits on their
  labels that a parked car exceeds for months each year (→ 29-02, → 09-03). Load them at
  departure; bring them in on arrival. Anything battery-shaped that must stay: cabin footwell,
  not trunk; checked monthly.
- **The car is a generator, not a battery.** A running engine charges phones and power stations
  through the 12 V socket or a USB-C car charger (→ 09-11), outdoors only.

## If you do not have it

- **Blankets, sleeping bags and heavy coats** from the house: the warmth layer is the part that
  must not be missing.
- **Floor mats** make traction boards; **cat litter or sand** works as grit.
- **Cardboard and newspaper** insulate people from cold surfaces.
- **A wagon{{#if is.snow_region}}, sled{{/if}} or cart** hauls children and gear when the
  vehicle stops being the answer.

## When it runs out

- **How long:** fuel is the vehicle's clock, and it is short: days of on-and-off heat, or one
  tank's driving range.
- **Ration:** heat in cycles (about 10 minutes an hour), water steadily, food last.
- **Resupply:** stabilised fuel cans. Siphoning has real limits (many tanks block it; the vapour
  is the hazard), and **never siphon by mouth** (→ 06-07).
- **After fuel:** the vehicle is still **shelter, storage and a windbreak**; transport becomes
  bicycle, wagon{{#if is.snow_region}} and sled{{/if}} (→ 16-09).

## Phase notes

- **A (shelter in place):** the kit is for local emergencies: the ditch, the closed road, the
  school run in a storm. This is the most likely use of anything in this binder.
- **B (moving):** the vehicle is the evacuation. Load the pre-staged pile, keep the medical kit
  in the cabin, and go early rather than perfectly (→ 01-02).
- **C (establish):** the vehicle becomes a **fixed asset**: battery and alternator (→ 09-11),
  storage, shelter, glass, wire, seats and mirrors. Do not scrap it thoughtlessly.

Related: → 22-03 go-bags · → 22-06 medical kit · → 01-07 medical load-out · → 17-01 blizzards ·
→ 08-02 carbon monoxide · → 08-05 hypothermia · → 11-02 keeping children warm · → 06-06 fuel
storage · → 06-08 fuel in transport · → 16-10 tyre failures · → 16-11 trailers · → 25-04 maps.

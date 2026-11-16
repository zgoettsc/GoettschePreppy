---
id: 09-16-outage-day-one
section: 09-power-and-energy
title: "Outage day one: the live grid-down procedure"
version: 2
revised: 2026-11-16
layer: core
danger_level: critical
phase: [A, C]
tags: [power, outage, procedure, day one, checklist, stations, solar, generator, refrigerated medicine, heat, carbon monoxide]
derived_from: [09-16-outage-day-one]
sources:
  - american-red-cross-power-outage-safety-6d07a8
  - us-consumer-product-safety-commission-cpsc-what-to-k-3390a4
  - cpsc-safety-alert-portable-generator-hazards-r8
  - usfa-battery-fire-safety-r14
  - foodsafety-gov-usda-hhs-food-safety-during-a-power-o-3894c1
  - us-fire-administration-fema-candle-fire-safety-use-f-6eeda1
  - us-fda-information-regarding-insulin-storage-and-swi-6448d3
  - southwire-spec-70065-sjeoow-r14
  - ecoflow-river-2-pro-user-manual
  - jackery-explorer-2000-plus-user-manual
  - anker-solix-c1000-gen-2-user-guide
related:
  - 09-01-power-priorities
  - 09-03-batteries-and-storage
  - 09-04-generators
  - 09-05-solar-in-winter
  - 09-06-charging-medical-devices
  - 09-10-power-for-medical
  - 00-06-first-60-minutes
  - 03-10-well-water-without-power
  - 04-17-food-safety-power-outage
  - 08-01-heating-one-room
  - 08-02-carbon-monoxide-safety
  - 08-04-emergency-heat-options
  - 14-03-opsec
  - 17-08-power-grid-failure
  - 30-01-the-floors
  - 30-02-dc01-unvented-heater-overnight
  - 30-03-dc02-propane-cylinder-indoors
  - 30-08-dc07-diy-cord-and-plug-conversion
  - 30-21-dc20-open-flame-indoors
cards: [DC-01, DC-02, DC-07, DC-20]
explainers: [EX-02, EX-03, EX-04, EX-07]
promote_when: []
photo_slots:
  - { id: breaker-panel, caption: "Our breaker panel: where it is, the main breaker marked, the circuit list readable" }
  - { id: fridge-breaker, caption: "The breakers for the fridge, the freezer and the furnace, marked" }
  - { id: station-ports, caption: "The back and front of each power station: solar input socket, 12 V port, AC outlets, the label with the input limits" }
  - { id: panel-bag, caption: "The panel bag packed: panels, cables, Y-branch, multimeter, this card" }
figures: [fig-series-vs-parallel, fig-generator-connection-options]
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: { date: "2026-11-16", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "Backfeed floor as 30-01; Red Cross surge advice checked on the live page (archive capture partial); unreadable FEMA gas page dropped; storage charge per manual; MC4 polarity worded as the figure; 12 AWG cord rating sourced" }
---

# Outage day one: the live grid-down procedure

**What this page is for.** The page you run, in order, when the grid drops. It defends the loads that
matter most (→ 09-01): medical devices, refrigerated medicine, phones, light and, in cold weather,
heat. It then sets up the next morning's charging. The last part is a hard-limits card for your
stations and panels: print it and keep it with the panels.

> **SAFETY.** **Never run a generator, charcoal, or any engine indoors, in a garage, or near an open
> window**: carbon monoxide kills in minutes with no warning; alarms fail (→ 30-01). Generator outdoors
> only, 20 feet or more from the house, exhaust away (CPSC, Portable Generator Safety).
> **Never connect a generator to house wiring except through a transfer switch, or an interlock kit
> with the main breaker off. Never backfeed through an outlet with a double-male ("suicide")
> cord.** It electrocutes line workers and neighbours (→ 30-01; CPSC, Portable Generator Hazards).
> A cord-and-plug conversion is not a connection to house wiring: the appliance is unplugged from
> the house outlet and plugged into the generator cord, so nothing reaches the panel (DC-07,
> → 30-08). A power station's AC output never goes into house wiring or a wall outlet either.
> **The one wiring mistake that destroys a station instantly** is a panel string whose voltage is over
> the station's solar input limit. Use only the configurations on the card at the bottom. When in
> doubt, stop and read the card.

## Do this now (the power just went out)
1. **Is it just us?** Look outside. If neighbours have power, check the main breaker and the panel
   ({{photo breaker-panel}}). Report the outage: {{ contacts.utility.electric.provider }},
   {{ contacts.utility.electric.phone }}.
2. **Medical devices first.** {{#if has.cpap}}CPAP onto its battery or a station tonight. {{/if}}{{#if has.oxygen}}Oxygen: switch to cylinders or the portable concentrator's battery now and start
   counting hours. {{/if}}Phones and medical devices onto power banks (→ 09-06).
3. **Keep the fridge and freezer shut.** A closed refrigerator keeps food safe for about 4 hours; a
   full freezer about 48 hours, a half-full one about 24 (USDA and HHS, Food Safety During a Power
   Outage; → 04-17).
4. {{#if has.refrigerated_meds}}**Refrigerated medicine: set up the cooler within the first hour**
   (step 3 below), and move the medicine once the cooler's thermometer reads within the label range.
   {{else}}Any refrigerated medicine: set up a cooler within the first hour (step 3 below).{{/if}}
5. **Switch off and unplug appliances and electronics** to avoid overloads and damage from power
   surges when the grid returns (American Red Cross, Power Outage Safety). Leave one light switched on so
   you know when power is back. Leave smoke and carbon monoxide alarms alone.
6. **Light: flashlights and lanterns, not candles** (US Fire Administration, Candle Fire Safety).
   Candles indoors are a decision: {{choice DC-20}} (→ 30-21).
7. **If you smell gas, leave first and call from outside** ({{ contacts.utility.gas.phone }}). Once
   gas has been shut off, only a qualified professional turns it back on (American Red Cross).
8. **Decide what kind of outage this is** (→ 17-08): hours, overnight, or unknown. Overnight or
   unknown: carry on down this page.

## Before any outage
- **Print this page and the card at the bottom; keep the card in the panel bag.** {{photo panel-bag}}
- **Photograph the breaker panel and mark the fridge, freezer and furnace breakers.**
  {{photo fridge-breaker}}
- **Know your posture for refrigerated medicine** (→ 09-10): either the cooler lives on a station in
  UPS mode, or the medicine lives in the kitchen fridge and the cooler, station and designated
  thermometer are staged. Ours: ________________________________.
- **Test the cooler for 24 hours on the station's 12 V port** with the designated thermometer inside;
  turn the station's power-saving ("ECO") setting off for that port (→ 09-03).
- **Stations:** stored at the charge level each manual gives (→ 09-03), charged to 100% when a storm
  is forecast. Power banks charged.
  Panel bag staged with cables, Y-branch and multimeter. {{photo station-ports}}
- **Carbon monoxide alarms installed** (we have {{ gear.co_alarms }}), tested, spare batteries.
- **Walk this sequence once on a calm day and time it.** The first real run should be the second run.

## The sequence

### T+0: the first hour
1. **Fridge and freezer shut** (above). Start the clock.
2. **Kill non-essential house loads.** Walk the house once: power strips off, unplug anything with a
   standby light. Five minutes; it stretches every stored watt-hour and protects against the surge when
   power returns.
3. **Set up the medicine cooler** (if anyone uses refrigerated medicine):
   - Cooler, station and the designated thermometer to the **warm room** (→ 08-01), away from any
     heater; never an unheated room in winter.
   - **Plug the cooler into the station's 12 V port, not the AC outlets.** The inverter's idle draw
     alone can be most of what the cooler uses. Switch the 12 V port on; **power-saving mode off.** If
     the cooler's display is ever dark, re-enable the port.
   - **Thermometer inside, lid shut.** Move the medicine in **only when the thermometer reads within
     the label range** (for insulin, 36 to 46 °F, 2 to 8 °C, never frozen: US FDA, Information
     Regarding Insulin Storage). Wrap the medicine so it never touches the cooler walls; if it reads
     too cold, raise the setting.
4. **Runtimes to plan on** (→ 09-10): each station's days for the cooler, worked out there. **The
   percentage on the screen is the truth.** Move the cooler to the next station at ______ %.
5. **Before dark:** every phone and power bank charging from the remaining station capacity; set out
   tomorrow's panel plan in your head.

{{#if has.well}}**Water:** the well pump stops with the power (→ 03-10).{{/if}}

### T+0 to T+6 hours: heat (any outage in cold weather, or when the house is cooling)
{{#if is.cold_winters}}**In a winter as cold as yours, heat is the clock right behind medicine.**{{else}}When it is cold, heat is
the clock right behind medicine.{{/if}} Start while the house still holds its warmth, not late at
night. In this order (→ 08-04):
1. **Furnace, only if gas still flows and a safe connection exists.** Our connection:
   **{{ gear.house_connection }}**. A station or generator can run the blower only through a transfer
   switch or interlock, or a cord-and-plug conversion ({{choice DC-07}}, → 30-08; how to use it:
   → 09-04). Run the blower in bursts, coast, repeat. **Never backfeed.** {{figure fig-generator-connection-options}}
2. **Close down to one warm room** (→ 08-01): blankets over doorways, everyone (and the medicine) in
   one room. The warm room must meet the heater's air rules.
3. **Carbon monoxide alarms on and tested BEFORE any heater is lit:** one in the warm room, one where
   people sleep (→ 08-02).
4. **One combustion heater at a time,** used exactly as its manual says for room size and fresh
   air. Kerosene: → 08-10. Propane: → 08-09; a cylinder larger than 1 lb
   indoors is a decision: {{choice DC-02}} (→ 30-03). Shared propane also feeds the generator and
   any cooking stove: count it (→ 06-05).
5. **Overnight:** an unvented heater running while people sleep is a decision card:
   {{choice DC-01}} (→ 30-02). Whatever you chose, heated blankets from a station for the sleepers
   help either way (→ 09-01). Anyone waking with a headache or nausea: everyone out to fresh air.

### The first morning: panel deployment
{{#if has.solar}}Our panels: {{ gear.solar_w_total }} W.{{/if}} Deploy in this order, unless the
station's manual says otherwise: **position the panels → chain them as the card says → lay the cable →
plug into a station that is switched off → switch on.**

**Decision rule: charge whichever station is lowest.** Use **only the standing configurations on the
card** (worked out on → 09-03). {{figure fig-series-vs-parallel}}
- **Before the first connection of any string, measure its voltage (Voc)** with the multimeter: red
  probe to the + lead (as marked on the panel label or cable). **A minus sign means a connector is
  reversed: swap it.**
- **Re-check the card every time you move panels between stations.**
- **Suitcase kits:** the panel's bare MC4 leads only. A separate controller box never joins a string
  or a station.
- **Wind:** stake or weight kickstand panels. **Concealment:** out at dawn, in at dusk, never left
  unattended (→ 14-03).

### Who runs on what

| Load | Runs on | Why |
|---|---|---|
| Medicine cooler | **A station's 12 V port, power-saving off, AC inverter off** | Tier 0; no inverter loss; give it a dedicated station if you have two (→ 09-10) |
| CPAP, oxygen concentrator | Its own battery pack or DC cord, then a station | Tier 0 (→ 09-06) |
| Phones, medical charging, power banks | Power banks and the smallest station | Keeps the pocket tier off the big stations |
| Kettle boils, heated-blanket sessions | **Whichever station is fullest** | Big optional draws come from surplus, never from the cooler's station |
| Furnace blower | A station or generator, **only through the safe connection** | Never backfed (→ 09-04); check the start surge first |
| Lights, radio, laptop | Power banks and the smallest station first | Tier 1 stays off the AC tier when it can |

### The daily rhythm
- **Charge at midday; run loads while the sun is up.** Every watt-hour used while the panels are
  producing is storage you did not need (→ 09-05).
- **Kettle and blanket sessions in the afternoon**, from the day's surplus, not at 10 p.m. from the
  night's reserve.
- **The cooler's station is topped up before dark, every day.** The one hard daily requirement.
- **Panels in at dusk**, folded, indoors: inspection, concealment and hail insurance in one habit.

{{#if is.cold_winters}}### Winter variant
- **Panels go out only in usable sun.** A grey whiteout day is not worth the cold exposure or the wind
  risk (→ 09-05).
- **Stations charge INDOORS, above 32 °F, always.** Station manuals give 32 °F (0 °C) as the lowest
  charging temperature (EcoFlow, Jackery, Anker; → 09-03). Run the panel cable in through a window or door gap with a towel seal.
- **Check winter's gift first:** below-freezing outdoor air may let the cooler's job move to passive
  cold, with freeze protection and a min/max thermometer (→ 09-10, → 04-09).
{{/if}}

### When solar fails for two days or more: the generator bridge
{{#if has.generator}}Our generator: {{ gear.generator_watts }} W, {{ gear.generator_fuel }}.{{/if}}
Outdoors, 20 feet or more, exhaust away, carbon monoxide alarms on (→ 09-04). Run it long enough to
refill a station at the station's **standard** charge rate on a 12 AWG cord (rated 20 A; Southwire),
then off. That cycle is
the storm plan, not continuous running. In deep cold, start it warm and bring it back in between
runs (→ 09-04). **If it has never been run, follow the first-start steps on → 09-04 (oil
first).**

### When the power comes back
1. Leave the generator running only until the house is back on the grid; then switch it off, outdoors.
2. If the furnace or a pump was on the generator cord, **unplug it from the cord, plug it back into its
   wall receptacle**, then switch the main breaker back on (→ 09-04).
3. Plug things back in one at a time.
4. Check the fridge and freezer and decide on food (→ 04-17). Medicine goes back to its normal
   storage.
5. Recharge everything, return stations to storage charge later, and write what happened in the log.

## Hard-limits card: print, cut out, keep with the panels
*(Fill in from the labels and the worksheet on → 09-03. Cold rule: a string's Voc × 1.20 must stay
below the station's maximum input voltage, with margin: → 09-02.)*

| Station | Solar input: max V · max A · max W · socket | OK to connect | **NEVER** |
|---|---|---|---|
{{#each stations as s}}| {{s.model}} ({{s.wh}} Wh) | ______ V · ______ A · ______ W · ______ | ______________ | ______________ |
{{else}}| ______ | ______ V · ______ A · ______ W · ______ | ______________ | ______________ |
{{/each}}

**Standing configurations:** (1) ______________ → ______ · (2) ______________ → ______ ·
(3) ______________ → ______.

**Never-rules for every station:**
- Measure Voc with the multimeter before any first-time connection; a **minus sign** means a reversed
  connector.
- The × 1.20 cold factor is never dropped on a "mild" morning.
- No series string whose cold voltage reaches a station's maximum input, in any season.
- No suitcase controller box, its clips or its adapter tips in a string or a station.
- No station's AC output into house wiring or a wall outlet, ever.
- No charging any lithium station below 32 °F.
- Power-saving mode off on any port running a medicine cooler.
- Generator outdoors only, 20 feet or more, exhaust away.

## When it runs out
- **Day three or later with no sun and no generator fuel:** shed to Tier 0 (→ 09-01), move the
  cooler's job to passive cold if the season allows (→ 09-10), and charge phones from a vehicle
  (→ 09-11, → 09-14).
- **If a station dies:** with two or more, the system is redundant: the cooler runs on any station's
  12 V port (power-saving off on whichever it moves to). One dead unit is a log entry, not a crisis.
- **If Tier 0 cannot be met**, that is a go/no-go input (→ 01-02), not something to endure.

## Phase notes
- **A (at home):** this page as written.
- **B (moving):** this page does not apply. Phase B power is power banks, the smallest station and the
  vehicle (→ 09-06, → 09-11).
- **C (settled somewhere new):** the same sequence; the generator bridge matters more until solar is
  set up (→ 09-04).

## Cross-references
→ 09-03 stations, panels and the wiring worksheet behind this card · → 09-10 the medicine cooler ·
→ 09-04 generator bridge and house connections · → 09-05 winter solar · → 09-06 medical devices ·
→ 09-01 load triage · → 08-04 the heat ladder · → 08-01 the warm room · → 08-02 carbon monoxide ·
→ 04-17 food safety in an outage · → 17-08 power grid failure · → 00-06 the first 60 minutes

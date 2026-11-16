---
id: 17-04-extreme-cold-and-heat
section: 17-weather-and-regional-hazards
title: "Extreme cold and extreme heat"
version: 1
revised: 2026-11-16
layer: region
danger_level: critical
phase: [A, B, C]
tags: [weather, extreme cold, extreme heat, wind chill, heat index, heat stroke, heat exhaustion, hypothermia, frostbite, children, elders]
derived_from: [17-04-extreme-cold-and-heat]
sources:
  - noaa-national-weather-service-during-extremely-cold-9c1973
  - noaa-national-weather-service-wind-chill-chart-frost-89f6d7
  - nws-cold-hazard-simplification-2024
  - noaa-national-weather-service-heat-safety-66fd15
  - noaa-national-weather-service-heat-index-categories-f3dbb9
  - nws-heat-hazard-renaming-2025
  - cdc-niosh-heat-related-illnesses-symptoms-and-first-0b89bb
  - cdc-about-heat-and-your-health-112caf
  - cdc-preventing-hypothermia-c53e0c
related: [17-01-blizzards-and-ice, 17-07-drought-and-water-scarcity, 17-08-power-grid-failure, 08-01-heating-one-room, 08-03-winterizing-the-home, 08-05-hypothermia-frostbite, 12-10-hypothermia-cross-ref, 11-01-cold-weather-layering, 11-02-keeping-kids-warm, 11-08-summer-heat-clothing, 03-01-daily-water-needs, 04-09-winter-cold-storage, 04-13-salt-sugar-vinegar, 06-04-wood-supply-and-depletion, 09-05-solar-in-winter, 09-10-power-for-medical, 12-05-common-illness-and-dehydration, 12-16-triage-and-hard-calls, 23-02-master-consumables-table, 29-07-ex07-refrigerated-medicines, 29-10-ex10-weather-alert-words, 30-01-the-floors, 30-09-dc08-heat-exposed-medication, 30-10-dc09-infant-bed-sharing]
cards: [DC-08, DC-09]
explainers: [EX-07, EX-10]
promote_when: [is.cold_winters, is.hot_summers]
photo_slots: []
figures: [fig-wind-chill-chart, fig-heat-index-chart]
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: null
---

# Extreme cold and extreme heat

**What this page is for.** Temperature extremes kill quietly, mostly the very young, the old and
the sick, and mostly indoors when the power is out. This page puts cold and heat side by side,
because they fail in opposite directions and one plan has to handle both.
Where you live: January nights average about **{{ region.home.jan_low_f }} °F** (record low
**{{ region.home.record_low_f }} °F**); July days average about **{{ region.home.jul_high_f }} °F**
(record high **{{ region.home.record_high_f }} °F**).
{{#if is.cold_winters}}**Your winters are cold enough that this page applies every year.**{{/if}}
{{#if is.hot_summers}}**Your summers are hot enough that this page applies every year.**{{/if}}

> **SAFETY.**
> - **Heat stroke is an emergency.** A hot person who is **confused**, slurring, or passing out
>   needs **cooling at once**, before anything else (CDC/NIOSH).
> - **Never leave anyone, especially a child, in a parked vehicle.** Not with windows cracked,
>   not for five minutes.
> - **Cold:** wind chill decides how fast bare skin freezes. Read the NWS chart, not a feeling.
> - **A frozen-then-thawed insulin vial or pen is discarded.** In cold, refrigerated medicine must
>   be kept from freezing (→ 29-07, → 30-01).
> - **Never run a generator, charcoal, or any engine indoors, in a garage, or near an open
>   window.** Heating in a cold outage is when carbon monoxide kills (→ 08-02).

## Do this now

1. **Look at the wind chill chart and the heat index chart** (below and → 29-10). Use them before
   anyone works outside.
2. **Pick a winter room and a summer room.** In winter it is the room you heat (→ 08-01); in summer
   it is the lowest, shadiest room. They are usually not the same room.
3. **Set the work rule for each season:** winter work in the warmest hours; **summer work at dawn
   and dusk, rest in the middle of the day.**
4. **Check the refrigerated medicine plan at both ends** (→ 29-07, → 09-10): summer is keeping it
   cool; winter is keeping it from freezing.
5. **Write down who checks on whom**, including neighbours who live alone (→ 18-01).

## The two ends, side by side

| | **Extreme cold** | **Extreme heat** |
|---|---|---|
| **What kills** | Hypothermia, frostbite, carbon monoxide from heating | Heat stroke, dehydration |
| **How fast** | Frostbite in minutes at the coldest wind chills | Heat stroke can build over hours, or come fast with work |
| **The multiplier** | **Wind** (wind chill) | **Humidity** (heat index) |
| **The household limit** | **Fuel** (→ 06-04) | **Water** (→ 03-01) |
| **Solar power** | At its worst (→ 09-05) | At its best |
| **Keeping food and medicine cold** | Free: outdoor cold (→ 04-09), with freezing risk | Hard: the biggest electrical load (→ 09-10) |
| **Room** | One heated room (→ 08-01) | The lowest, shadiest room |
| **Work** | Midday, warmest hours | Dawn and dusk |
| **Clothing** | Layers, wool, no cotton (→ 11-01) | Loose, light, covered; cotton is right (→ 11-08) |

The pairing is useful: the hardest electrical job, cooling medicine, is cheapest when solar is
best and free when solar is worst.

## Alert words

| NWS alert | What it means |
|---|---|
| **Cold Weather Advisory** | Cold enough to be dangerous without care |
| **Extreme Cold Watch / Warning** | Dangerously cold air temperature or wind chill possible / expected |
| **Heat Advisory** | Heat that can make people ill, especially with work or no cooling |
| **Extreme Heat Watch / Warning** | Dangerous, possibly deadly heat possible / expected |

**Name changes.** The NWS renamed the wind chill alerts to Extreme Cold and Cold Weather Advisory in
October 2024 (NWS, 2024), and renamed the Excessive Heat Watch and Warning to **Extreme Heat** in
March 2025 (NWS, 2025). The Heat Advisory kept its name. Old cards and radios may still use the old
words; treat them the same. Each office sets its own trigger numbers. Your office,
**{{ region.home.nws_office }}**, issues an Extreme Cold Warning at ______ °F and an Extreme Heat
Warning at a heat index of ______ °F.

## Extreme cold

- **Wind chill is the number that matters.** Find today's temperature and wind on the NWS chart
  and read the frostbite time (NWS, Wind Chill Chart).
- **No bare skin outside at the coldest wind chills.** Children stay in; outdoor work is essential
  minutes only.
- **Cold breaks equipment:** batteries lose capacity and lithium batteries must not be charged
  below freezing (→ 09-07); engines start hard; phones shut off; pipes freeze (→ 03-06).
- **The house is your main defence** (→ 08-01, → 08-03), and fuel is the limit (→ 06-04).
- **Check children and elders by touch**, not by asking: belly and back of the neck (→ 11-02).
- **Warning signs and treatment** of hypothermia and frostbite: → 08-05, → 12-10.

{{figure fig-wind-chill-chart}}

## Extreme heat

**The heat index** (temperature plus humidity) is how hot it feels, because damp air stops sweat
cooling you. The NWS categories (NWS, Heat Index):

| Heat index | Category | With long exposure or work |
|---|---|---|
| 80 to 90 °F | Caution | Tiredness |
| 90 to 103 °F | Extreme caution | Heat cramps and heat exhaustion possible |
| 103 to 124 °F | Danger | Cramps and exhaustion likely; heat stroke possible |
| 125 °F and up | Extreme danger | Heat stroke imminent |

**The published heat index assumes shade and a light wind. Full sun can add up to 15 °F** (NWS).

{{figure fig-heat-index-chart}}

**Heat illness gets worse in steps** (CDC/NIOSH, Heat-Related Illnesses):
- **Heat exhaustion:** heavy sweating, weakness, dizziness, nausea, headache, cool clammy skin, a
  fast weak pulse. **Move to a cool place, loosen clothing, cool wet cloths or a cool bath, sips of
  water.** If they vomit, get worse, or are not better within an hour, treat it as heat stroke.
- **Heat stroke:** hot skin (wet or dry), **confusion**, slurred speech, passing out, a body
  temperature around 104 °F or higher. **Cool hard and at once:** cold water immersion if you can,
  otherwise soak the skin and fan it, cold packs or ice at neck, armpits and groin. **Do not rely
  on the person to drink.** Call for help if help exists; cooling comes first. With no help, see
  → 12-16.

**Living through heat with no air conditioning** (NWS, Heat Safety; CDC):
- **Close up by day, open up at night**, live on the lowest floor, block sun **outside** the
  glass, move air with a fan (→ 11-08).
- **Fans alone do not prevent heat illness once it is very hot** (CDC). Cool the body: wet cloths,
  a cool shower or bath, wet clothing in moving air.
- **Water on a schedule, not on thirst**, and more with work. Over days of heavy sweating, salt
  and electrolytes matter (→ 04-13, → 12-05).
- **Shift the work:** heavy jobs at dawn and evening, rest through the worst of the day. Write your
  household's line: outdoor work stops when ______________.

## Who is hit hardest

- **Infants and young children** lose and gain heat fast and cannot tell you. A carried or seated
  child makes little heat in the cold and cannot move to shade in the heat. Check by touch.
  {{#if has.infant}}An infant in your household is at the highest risk at both ends.{{/if}}
- **Elders and people with heart, lung or kidney disease** may not feel heat or thirst, and some
  medicines change how the body handles heat (CDC, Heat and Your Health). Ask a pharmacist now
  which of the household's medicines do.
  {{#if has.elder}}Plan a check on each elder at least twice a day in a heat wave.{{/if}}
{{#if has.diabetes}}- **Diabetes:** heat and dehydration push blood sugar around and dehydration
  feeds itself; in cold, low blood sugar can look like cold (confusion, clumsiness). **Check the
  glucose before blaming the weather.** See your condition page in Section 02.{{/if}}
{{#if has.refrigerated_meds}}- **Refrigerated medicine** that has been too warm is a hard choice
  when no replacement exists. It is a decision card: {{choice DC-08}} → 30-09{{/if}}
{{#if has.pregnant}}- **Pregnancy** raises heat risk. Rest in the coolest place and drink
  steadily.{{/if}}

## By dwelling type

{{#if has.mobile_home}}- **Mobile or manufactured home:** heats fast in sun and loses heat fast in
  cold. In a long heat wave or a deep-cold outage, agree in advance on a sturdier, cooler or warmer
  place to go.{{/if}}
{{#if has.apartment}}- **Apartment:** upper floors are the hottest. In a heat wave with no power,
  spend the day on a lower floor, in a shared cool space, or with someone below.{{/if}}
{{#if has.basement}}- **Basement:** usually the coolest room in summer and a steady room in winter;
  it is often the right summer room.{{/if}}
- **Any building:** window coverings that block sun in summer and hold heat in winter help twice
  (→ 08-03).

## Gear

| Item | Why | Notes |
|---|---|---|
| **Wind chill and heat index charts** | Turn a feeling into a time limit | Printed on this page and → 29-10 |
| Indoor/outdoor min/max thermometer | Shows what the house is really doing | |
| Cold-weather clothing for everyone | → 11-01, → 11-02 | Layers, wool |
| Hot-weather clothing, hats, shade | → 11-08 | |
| Low-power fans (12 V or USB) | Comfort per watt in summer | → 09-01 |
| Shade cloth or tarps | Block sun outside the glass | |
| Extra stored water | Summer needs far exceed the average | → 03-02 |
| Oral rehydration salts, salt | Days of heavy sweating | → 12-05 |
| Medical thermometers | Both hypothermia and heat stroke | → 12-01 |

**If you do not have it:** layers from any source, newspaper as insulation, snow banked against the
house, body heat and shared sleeping in the cold (an infant sharing an adult bed is a separate
decision: {{choice DC-09}} → 30-10); wet cloths at neck and wrists, a damp sheet in a breezy
window, the lowest room, and night air in the heat. Deep ground is cool in summer and above
freezing in winter, which is why cellars and basements work.

## When it runs out

- **Winter runs out of fuel; summer runs out of water.** Work out each one separately on → 23-02.
  Do not average them: a plan sized for the average fails at both ends.
- **Stretch it** by behaviour first: when you work, where you sleep, what you expect. It costs
  nothing and does more than equipment.
- **Lasting fixes help twice:** insulation, shade trees, window coverings, a cellar.

## Phase notes

- **A (at home):** the house is the tool at both ends: heated room in winter, lowest room in
  summer.
- **B (moving):** both extremes make travel much more dangerous (→ 01-02). Winter risks
  stranding (→ 17-01); summer is a water problem, and water is heavy. Move in mild weather if you
  have any choice.
- **C (rural or new site):** more exposure, less shade, more wind, help further away. Build shade
  and windbreaks early and plan the work calendar around the extremes.

---
id: 29-10-ex10-weather-alert-words
section: 29-explainers
title: "Weather alert words: watch, warning, advisory, wind chill, heat index"
version: 1
revised: 2026-11-16
layer: explainer
danger_level: caution
phase: [A, B, C]
tags: [weather, watch, warning, advisory, wind chill, heat index, tornado, flood, red flag, hazard rating, explainer]
derived_from: [15-01-weather-alerts, 17-02-tornadoes, 17-04-extreme-cold-and-heat, 25-02-conversions-and-math]
sources: [noaa-national-weather-service-weather-ready-nation-b0a52f, noaa-national-weather-service-tornado-safety-ba75e0, noaa-national-weather-service-wind-chill-chart-frost-89f6d7, noaa-national-weather-service-heat-index-categories-f3dbb9, noaa-national-weather-service-during-extremely-cold-9c1973, noaa-national-weather-service-nws-glossary-red-flag-753d33, noaa-national-weather-service-turn-around-don-t-drow-a6f9ff, noaa-national-weather-service-noaa-weather-radio-all-5f13d8]
related: [15-01-weather-alerts, 17-01-blizzards-and-ice, 17-02-tornadoes, 17-03-floods, 17-04-extreme-cold-and-heat, 17-05-grassland-fire, 17-06-tornado-shelter, 08-05-hypothermia-frostbite, 29-09-ex09-radios]
cards: [DC-19]
explainers: [EX-09]
promote_when: [experience.new]
photo_slots: []
figures: [fig-wind-chill-chart, fig-heat-index-chart]
plates: []
condition: null
gear: null
explainer: EX-10
card: null
review_pass: null
---

# Weather alert words, explained from the beginning

**What this page is for.** A weather alert is only useful if everyone in the house knows what
the words mean and what to do at once. This page explains the three alert levels, the two
"feels like" numbers, and the hazard ratings printed for your region.

## Watch, warning, advisory

| Word | What it means | What you do |
|---|---|---|
| **Watch** | Conditions are right for the hazard to develop. It has not happened yet. Watches cover large areas and last hours | Get ready. Charge things, check the plan, know where everyone is, shoes on |
| **Warning** | The hazard is happening, or is about to, where you are | **Act now.** For a tornado warning: to the shelter spot, immediately |
| **Advisory** | Less serious, but still a hazard that can hurt people who ignore it | Take care; change plans for travel or outdoor work |

**Tornado warning** means a tornado has been seen or shown by radar: the warning time is minutes
(NWS, Tornado Safety). A **severe thunderstorm warning** means damaging wind or large hail, and
tornadoes can form from these storms with little extra warning. → 17-02, → 17-06

Other alerts you will hear:
- **Flood or flash flood warning** — water is rising or about to. Never drive or walk into
  moving water: 6 inches can knock an adult down and 12 inches can carry away most cars (NWS,
  Turn Around Don't Drown). → 17-03
- **Red flag warning** — warm, dry, windy weather in which any fire spreads fast. No outdoor
  burning (NWS Glossary). → 17-05
- **Winter storm, ice storm, blizzard warning** — travel becomes dangerous and power loss is
  likely. → 17-01
- **Extreme cold warning** and **extreme heat warning** — dangerous cold or heat. Older radios
  and pages may say "wind chill warning" or "excessive heat warning"; treat them the same.

Each NWS office sets its own trigger numbers for its area, so the same word can start at a
different temperature in different states. Your office: {{ region.home.nws_office }}.

## The two "feels like" numbers

**Wind chill** is how cold it feels on bare skin when wind is added to cold air, because wind
strips heat away faster. It is the number that predicts **frostbite**. The NWS wind chill chart
shows, for each air temperature and wind speed, whether bare skin freezes in 30, 10 or 5 minutes
(NWS, Wind Chill Chart). Use the chart, not a feeling. → 08-05

**Heat index** is how hot it feels when humidity is added to heat, because damp air stops sweat
from cooling you. The NWS categories (NWS, Heat Index):

| Heat index | Category | What can happen with long exposure or work |
|---|---|---|
| 80°F to 90°F | Caution | Tiredness |
| 90°F to 103°F | Extreme caution | Heat cramps and heat exhaustion possible |
| 103°F to 124°F | Danger | Cramps and exhaustion likely; heat stroke possible |
| 125°F and up | Extreme danger | Heat stroke imminent |

The published heat index assumes shade and a light wind. **Full sun can add up to 15°F** (NWS).
→ 17-04

{{figure fig-wind-chill-chart}}

{{figure fig-heat-index-chart}}

## The hazard ratings in your region pages

The region appendix rates each natural hazard for every county on a scale of **1 to 3**: 1 is
lower, 3 is higher, and each rating is printed with its words. The rating says how much a hazard
deserves planning where you live; it does not predict any single day. Your home county:

| Hazard | Rating | Meaning |
|---|---|---|
{{#each region.home.hazards as h}}| {{h.name}} | {{h.rating}} | {{h.rating_text}} |
{{/each}}

Pages for the hazards rated 2 or 3 are moved to the front of their sections in your binder.

## Hearing the alert

The alert only helps if it reaches you at 3 a.m. with the power and phones out: a NOAA Weather
Radio with SAME and fresh batteries (→ 29-09). When to leave home altogether is a decision your
household writes down in advance: {{choice DC-19}} → 30-20

---
id: 15-01-weather-alerts
section: 15-communications
title: "NOAA Weather Radio and weather alerts"
version: 1
revised: 2026-11-16
layer: region
danger_level: caution
phase: [A, B, C]
tags: [NOAA Weather Radio, SAME, weather alerts, watch, warning, tornado, blizzard, flood, batteries, hand-crank, barometer]
derived_from: [15-01-weather-alerts]
sources: [noaa-national-weather-service-noaa-weather-radio-all-5f13d8, noaa-national-weather-service-nwr-county-coverage-an-c6207f, nws-partial-county-alerting-technical, nws-cold-hazard-simplification-2024, nws-heat-hazard-renaming-2025, noaa-national-weather-service-weather-ready-nation-b0a52f, american-red-cross-winter-storm-preparedness-and-bli-4bb6c0]
related: [29-10-ex10-weather-alert-words, 29-09-ex09-radios, 15-02-radio-options, 15-03-family-comms-plan, 15-04-monitoring-and-info, 15-05-ham-and-licensing, 15-06-antennas-and-range, 15-09-corridor-comms, 00-04-family-emergency-plan, 17-01-blizzards-and-ice, 17-02-tornadoes, 17-03-floods, 17-04-extreme-cold-and-heat, 17-05-grassland-fire, 17-06-tornado-shelter, 17-10-reading-the-sky, 17-13-hurricanes-and-tropical-storms, 17-14-wildfire-smoke-and-evacuation, 09-05-solar-in-winter, 09-07-battery-chemistry, 09-11-hand-and-alt-generation, 24-02-drills, 25-03-regional-contacts, 25-08-quick-reference-cards, 01-03-phase-b-movement, 01-05-choosing-a-destination, 03-04-purifying-water, 08-05-hypothermia-frostbite, 11-08-summer-heat-clothing, 18-01-mutual-aid]
cards: []
explainers: [EX-09, EX-10]
promote_when: [is.tornado_region, is.hurricane_region, is.flood_region, is.snow_region]
photo_slots:
  - { id: weather-radio, caption: "Our weather radio, where it lives, with the SAME codes we programmed" }
figures: []
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: null
---

# NOAA Weather Radio and weather alerts

**What this page is for.** The cheapest, most valuable communications item in this binder: a
NOAA Weather Radio that wakes you for a warning at 3 a.m. and works when the power, the phones
and the internet are all down. This page gives your home transmitters and county codes, the
alerts that matter, and how to keep the radio working. The alert words are explained on → 29-10;
radio basics on → 29-09.

> **CAUTION.** Buy one with **SAME programming and battery backup**, program your county code,
> and test it. An unprogrammed radio alerts for a wide area, gets switched off out of annoyance,
> and that is exactly how people miss the one that mattered.

## Do this now

1. {{#if has.noaa_radio}}**You have a weather radio.** Write the model and the room it lives in:
   ____________________ / ____________________. Consider a second one for the storm shelter
   area (→ 17-06).{{else}}**Buy a NOAA Weather Radio with SAME and battery backup.** It is one of
   the cheapest life-saving purchases there is.{{/if}}
2. **Program your county's SAME code and the counties around you** (table below). Storms often
   arrive from a neighbouring county first; a warning there is your lead time. Confirm each code
   on the radio and tick it.
3. **Test it, and check the batteries every time the clocks change.**
4. **Keep the radio's batteries as a protected reserve**: not borrowed for flashlights, and
   replaced first (→ 09-07).
5. **Also get a hand-crank weather radio** (→ 09-11): no power needed, and many also charge a
   phone and give light.
6. **Write the family's alert plan** (→ 00-04): what happens on each kind of warning, who does
   what, where {{#if has.child}}the children go{{else}}everyone goes{{/if}}. Practise it once
   (→ 24-02).

## What NOAA Weather Radio is

A network of transmitters run by the National Weather Service (NWS), broadcasting forecasts and
warnings around the clock (NWS, NOAA Weather Radio All Hazards). **It does not depend on the
internet, the cell network, commercial stations or your power**, only on the transmitter and
your radio's batteries.

**SAME** (Specific Area Message Encoding) lets the radio filter alerts to the counties you choose.
Program your county and it stays silent until something matters to you, which is what makes it
something you will actually leave on. A SAME code is six digits. For a whole county the first
digit is 0; a different first digit means only part of a county, which a few large counties use
(NWS, Partial County Alerting). Copy the codes from the table below rather than working them out.

**Every NOAA Weather Radio transmitter in the country uses one of seven frequencies: 162.400,
162.425, 162.450, 162.475, 162.500, 162.525 and 162.550 MHz.** With no internet, any radio that
tunes those (a weather radio, a scanner, many amateur handhelds) finds the working transmitter by
stepping through seven channels.

## Your numbers

Home: {{ home.county }}, {{ region.home.state_name }}. NWS forecast office:
**{{ region.home.nws_office }}**.

Your home transmitters (from the region appendix; NWS, NOAA Weather Radio Coverage by County):

| Call sign | Frequency (MHz) | SAME code | Confirmed on our radio |
|---|---|---|---|
{{#each region.home.nwr as t}}| {{t.call}} | {{t.freq}} | {{t.same}} | ☐ |
{{/each}}

**Neighbouring counties to program too** (look them up in your state's page in the region appendix,
Section 32, and check each against the transmitter's county list):

| County | SAME code | Programmed |
|---|---|---|
| ______________ | ______ | ☐ |
| ______________ | ______ | ☐ |
| ______________ | ______ | ☐ |
| ______________ | ______ | ☐ |

{{#if has.destinations}}**Destinations and route counties:** program these on arrival, from the
local transmitter's county list, not from here (→ 15-09).
{{#each destinations as x}}- {{x.name}} ({{x.county}}, {{x.state_name}}): NWS office
  {{x.region.nws_office}}. SAME code: ______ ☐
{{/each}}{{/if}}

{{photo weather-radio}}

## Watch, warning, advisory

- **Watch:** conditions are right for it. **Be ready. Get the plan out.**
- **Warning:** it is happening or about to. **Act now.**
- **Advisory:** less severe, but still hazardous.

Full explanations, wind chill and heat index: → 29-10. Post a card with these three words where
everyone can see it (→ 25-08). The difference matters most at 3 a.m.

## The alerts that matter

Your home's hazard ratings, from the region data (1 low to 3 high):

{{#each region.home.hazards as h}}- **{{h.name}}**: {{h.rating_text}}
{{/each}}

| Alert | What it means for your household |
|---|---|
| **Tornado Warning** | **Act now.** {{#if has.shelter_room}}{{ dwelling.shelter_room }}{{else}}Lowest floor, interior room, away from windows{{/if}}, everyone, now (→ 17-02, → 17-06) |
| **Severe Thunderstorm Warning** | Hail (a real threat to solar panels), damaging wind, possible tornadoes |
| **Blizzard Warning** | Do not travel. Bring in wood and water, charge everything, expect almost no solar (→ 09-05, → 17-01) |
| **Winter Storm or Ice Storm Warning** | Power loss likely; same preparation. Ice is a classic cause of long outages |
| **Extreme Cold Warning** (the NWS replaced "Wind Chill Warning" with this name in 2024; an older radio or card may still say wind chill) | Frostbite can happen fast (→ 08-05, → 29-10). No unnecessary outdoor work; children stay in |
| **Flood Warning** | Rivers and streams rising; water contamination risk (→ 03-04, → 17-03) |
| **Red Flag Warning** (fire weather) | Grass and wildfire risk (→ 17-05, → 17-14) |
| **Extreme Heat Warning** (the NWS renamed these from "Excessive Heat" in March 2025; either wording means act) | No air conditioning in a summer outage (→ 11-08, → 17-04) |
| **Hurricane or Tropical Storm Warning** | Follow evacuation orders; secure the house (→ 17-13) |

{{#if is.tornado_region}}Your home is rated for tornadoes: tornadoes can come at night, so the
radio belongs where you sleep.{{/if}}{{#if is.hurricane_region}} Your home is rated for
hurricanes: NWR carries the local watches and warnings as the storm approaches.{{/if}}

## Getting information when the grid is down

The weather radio comes first, and it is the one that works. Layer the others behind it:

1. **NOAA Weather Radio**: battery and hand-crank models.
2. **AM and FM broadcast**: commercial stations often run on generators well into an outage, and
   AM travels a long way at night (→ 15-04).
3. **Shortwave**: regional and world news when local sources are gone (→ 15-04).
4. **Scanner and amateur radio**: what is actually happening locally (→ 15-02, → 15-05).
5. **Phone alerts** (Wireless Emergency Alerts): useful while the cell network works. Do not build
   the plan on them.
6. **A barometer and your own eyes**: a falling barometer and a dark, green-tinged sky are
   information (→ 17-10).

## Power for the radio

- **Batteries first.** A weather radio uses very little. Stock AA and AAA cells and rechargeables
  (→ 09-07), and keep the radio's own cells as a protected reserve.
- **Hand-crank** as the no-power backup (→ 09-11).
- **Leave it on through severe-weather season and every winter storm**, not just when you think
  of it. A SAME-muted weather radio uses little power and transmits nothing, so it is the one
  radio that stays on all the time. (The scheduled listening times on → 15-03 are for scanners and
  two-way radios.)

## How it fails

- **No batteries in it** when it matters. Check every season.
- **Not programmed**, so it alerts constantly and gets switched off.
- **In the wrong room.** Put it where you sleep.
- **Nobody knows what to do when it sounds.** That is → 00-04 and → 24-02: make the plan and
  practise it once.
- **Relying on a phone.** Cell networks fail and phones go flat{{#if has.condition.CL-01}}, and a
  phone may be doing a medical job in your household{{/if}}.
- **Out of range.** Reliable reception typically reaches about 40 miles from a transmitter over
  level ground, and less among hills and mountains (NWS, NOAA Weather Radio Coverage by County).
  Some places are at the edge of coverage; check before relying on it at a new site (→ 15-06).

## Gear

| Item | Why | Notes |
|---|---|---|
| **NOAA Weather Radio with SAME and battery backup** | Wakes you for the night-time warning | Program your county and its neighbours |
| A second weather radio for the shelter area | Where you will be during the warning | → 17-06 |
| **Hand-crank weather radio with USB output and light** | No power needed; charges a phone | → 09-11 |
| AA and AAA batteries, deep stock, plus rechargeables | The radio's only need | → 09-07 |
| A portable AM/FM radio | Broadcast backup | Battery or crank |
| **Frequencies and SAME codes written in this binder** | You cannot look them up later | This page; → 25-03 |
| A printed alert-words card | Watch versus warning at a glance | → 25-08 |
| A written family alert plan | Who does what, where everyone goes | → 00-04 |
| A barometer | Real information with no power at all | Cheap, durable |

**If you do not have it:**

- **Any radio that receives the seven weather frequencies**: many scanners, marine radios and
  amateur handhelds do (→ 15-02).
- **A car radio** for AM and FM; many vehicles also receive the weather band.
- **Neighbours**: someone on the block has a weather radio; knowing who is worth something
  (→ 18-01).
- **Your own observation**: sky, wind, temperature trend, barometer (→ 17-10). People watched the
  sky long before radios existed.
- **What you cannot replace:** the middle-of-the-night alarm. That is what the radio is for.

## When it runs out

- **Batteries are the consumable**, and a weather radio uses very few. A crank radio needs none.
- **The transmitter itself may eventually go off the air** in a very long collapse. Expect the
  information to degrade in steps: weather radio, then commercial broadcast, then shortwave, then
  amateur radio (→ 15-05), then neighbours and your own eyes.
- **Learn the sky and a barometer** now, so you can step down when you have to. A barometer, a
  thermometer and attention are a real forecasting tool, and they never run out (→ 17-10).
- **The habit that matters:** during severe-weather season and every winter storm, the radio is
  on. That habit turns the purchase into protection.

## By phase

- **A (at home):** radio in the bedroom, a second near the shelter, codes programmed, plan
  practised.
- **B (on the move):** the hand-crank radio travels, and a weather radio rides in the vehicle.
  Weather is often the main hazard on the road, and a warning in time changes the decision
  (→ 01-03, → 17-01).
- **C (rural or a new place):** more exposed, farther from help, sometimes at the edge of
  coverage. **Check coverage before committing to a site** (→ 01-05), and plan on a better antenna
  (→ 15-06) or amateur radio (→ 15-05).

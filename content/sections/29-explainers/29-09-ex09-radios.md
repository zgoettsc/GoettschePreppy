---
id: 29-09-ex09-radios
section: 29-explainers
title: "Radios: FRS, GMRS, CB, MURS, ham and NOAA Weather Radio"
version: 1
revised: 2026-11-16
layer: explainer
danger_level: none
phase: [A, B, C]
tags: [radio, FRS, GMRS, CB, MURS, ham, amateur radio, repeater, NOAA Weather Radio, SAME, licence, explainer]
derived_from: [15-01-weather-alerts, 15-02-radio-options, 15-05-ham-and-licensing, 15-06-antennas-and-range]
sources: [us-government-publishing-office-ecfr-47-cfr-part-95-c8b55a, us-government-publishing-office-ecfr-47-cfr-part-97-17b11d, arrl-the-national-association-for-amateur-radio-amat-0ae5a4, arrl-the-national-association-for-amateur-radio-what-5edded, noaa-national-weather-service-noaa-weather-radio-all-5f13d8, noaa-national-weather-service-nwr-county-coverage-an-c6207f]
related: [15-01-weather-alerts, 15-02-radio-options, 15-03-family-comms-plan, 15-04-monitoring-and-info, 15-05-ham-and-licensing, 15-06-antennas-and-range, 28-05-radios, 29-10-ex10-weather-alert-words]
cards: []
explainers: [EX-10]
promote_when: [experience.new]
photo_slots: []
figures: [fig-line-of-sight-and-repeater]
plates: []
condition: null
gear: null
explainer: EX-09
card: null
review_pass: { date: "2026-11-16", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "Part 95 power limits and GMRS licence re-read (Cornell LII copy of 47 CFR); seven NWR frequencies re-read; everyday ranges are labelled planning figures; 28-05 now points here for range." }
---

# Radios, explained from the beginning

**What this page is for.** When phones are down, radios are how a family stays in touch and how
you hear warnings. The radios on sale use different "services" with different rules, power and
reach. This page says what each one is, what range to honestly expect, what a repeater is, and
how NOAA Weather Radio works.

## Words first

- **Handheld** — a walkie-talkie. **Mobile** — mounted in a vehicle. **Base** — at home with an
  outside antenna.
- **Watts** — transmit power. More power helps a little; **antenna height helps far more**.
- **Line of sight** — the radios these services use travel roughly in straight lines. Hills,
  buildings and the curve of the earth block them. Two people on rooftops talk much farther than
  two people in basements.
- **Repeater** — a radio on a tall tower or building that receives you on one frequency and
  re-transmits on another at once, so two handhelds that cannot reach each other can both reach
  it. GMRS repeaters listen 5 MHz above the frequency they transmit on (47 CFR Part 95).
- **"Privacy codes"** (CTCSS/DCS tones) only stop **your** radio from playing other people's
  traffic. **Everyone can still hear you.** Nothing on these radios is private.
- **Simplex** — radio to radio directly, no repeater.

{{figure fig-line-of-sight-and-repeater}}

## The services

| Service | Licence | Power (47 CFR Parts 95 and 97) | Honest everyday range | Good for |
|---|---|---|---|---|
| **FRS** (Family Radio Service) | None | 2 W on channels 1–7 and 15–22; 0.5 W on 8–14; fixed antenna | A few hundred yards to about a mile in town | The yard, the block, a campsite |
| **GMRS** (General Mobile Radio Service) | Yes; **no exam**; one licence covers the family | Up to 5 W on 1–7, 50 W on 15–22; removable antennas; repeaters allowed | 1 to 5 miles handheld; more with a repeater or a roof antenna | Family coordination around a town |
| **MURS** | None | 2 W, 5 channels near 151–154 MHz; external antennas allowed | 1 to 3 miles | A quiet alternative to FRS |
| **CB** (Citizens Band) | None | 4 W AM, 12 W single-sideband; 40 channels near 27 MHz | 1 to 5 miles; occasionally very far | Road and traffic information from truckers |
| **Amateur ("ham")** | Yes; **exam** | Depends on licence class and band | Across town to across the world, depending on band and antenna | Real distance; organised emergency nets |
| **Scanner / receiver** | None to listen | — | — | Hearing what is going on without being heard |

FRS and GMRS share the same 22 channels, so FRS and GMRS radios can talk to each other on them.
The "35-mile" figure on a blister pack is a mountaintop-to-mountaintop number; expect the
everyday column. **Test your own:** one person walks or drives away calling every block until
contact is lost, and you write that distance down (→ 15-06).

> **Before the collapse:** transmitting on GMRS or amateur bands requires an FCC licence while
> the FCC operates; GMRS needs no exam, amateur radio does (47 CFR Parts 95 and 97). A licence
> you hold and a radio you have practised on now are worth far more than one you are guessing at
> later. Listening needs no licence. → 15-05

## NOAA Weather Radio

The National Weather Service runs a network of transmitters that broadcast forecasts and warnings
around the clock. It does not depend on the internet, cell towers or your house power, only on
the transmitter and your radio's batteries. **Every transmitter in the country uses one of seven
frequencies: 162.400, 162.425, 162.450, 162.475, 162.500, 162.525 and 162.550 MHz** (NWS). Any
radio that tunes those finds the local one by stepping through seven channels.

**SAME** (Specific Area Message Encoding) is a code for each county. A weather radio with SAME,
programmed with your county's code, stays silent until an alert for that county arrives, then
sounds an alarm. Program the counties around yours too: storms arrive from neighbouring counties
first. What the alerts mean: → 29-10.

Your home transmitters (from the region appendix):

| Call sign | Frequency (MHz) | SAME code |
|---|---|---|
{{#each region.home.nwr as t}}| {{t.call}} | {{t.freq}} | {{t.same}} |
{{/each}}

{{#if has.noaa_radio}}You have a weather radio: program the SAME code above and test it.{{else}}A weather radio with SAME and battery backup is one of the cheapest life-saving purchases there is. → 15-01{{/if}}
{{#if has.gmrs}} You have FRS or GMRS radios: agree a family channel and practise. → 15-03{{/if}}
{{#if has.ham}} Someone in the household is licensed or has a ham radio. → 15-05{{/if}}

---
id: 28-05-radios
section: 28-gear-reference
title: "Two-way and weather radios: what the specs mean, and common models"
version: 1
revised: 2026-11-16
layer: gear
danger_level: none
phase: [A, B, C]
tags: [radio, FRS, GMRS, CB, amateur, ham, MURS, NOAA Weather Radio, SAME, watts, licence, batteries, spec table]
derived_from: [15-02-radio-options, 15-05-ham-and-licensing, 15-06-antennas-and-range, 15-01-weather-alerts]
sources:
  - us-government-publishing-office-ecfr-47-cfr-part-95-c8b55a
  - midland-lxt600vp3-product-page
  - midland-gxt1000vp4-product-page
  - midland-mxt275-product-page
  - midland-wr120b-product-page
  - btech-gmrs-v2-product-page
  - baofeng-uv-5r-product-page
  - cobra-29-ltd-product-page
  - uniden-pro520xl-product-page
related: [15-01-weather-alerts, 15-02-radio-options, 15-03-family-comms-plan, 15-05-ham-and-licensing, 15-06-antennas-and-range, 28-07-reading-your-own-gear, 29-09-ex09-radios, 29-10-ex10-weather-alert-words]
cards: []
explainers: [EX-09, EX-10]
promote_when: [has.gmrs, has.ham, has.noaa_radio]
photo_slots:
  - { id: radio-labels, caption: "The label inside the battery compartment of each of our radios (model, FCC ID, service)" }
figures: []
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: null
---

# Two-way and weather radios: what the specs mean, and common models

**What this page is for.** When phones and the internet are down, radios are how a household
talks across the block and hears warnings. This page explains the numbers and words on a radio's
box and label, then lists common models with the makers' own figures. What each radio service is
for and how far it really reaches: → 29-09 and → 15-02. Family channel plan: → 15-03.

## What matters and why

1. **Service.** Which set of frequencies and rules the radio is built for. **FRS** (Family Radio
   Service) bubble-pack radios, **GMRS** (General Mobile Radio Service) handhelds and mobiles,
   **CB** (Citizens Band) for vehicles, **amateur ("ham")** radios, and receive-only **NOAA
   Weather Radio**. Radios on the same service talk to each other; across services, mostly not.
   FRS and GMRS share channel numbers 1 to 22, so FRS and GMRS radios can talk.
2. **Transmit power, in watts.** The federal limits are fixed by service: FRS up to 2 W on
   channels 1–7 and 15–22 and 0.5 W on 8–14; GMRS up to 5 W handheld on 1–7, 0.5 W on 8–14, and
   up to 50 W from a mobile or base on the main channels; CB 4 W AM or FM, 12 W single-sideband;
   MURS 2 W (47 CFR Part 95). More watts helps a little. **Antenna height helps far more**
   (→ 15-06).
3. **Range claims.** "Up to 30 miles" or "35 miles" on a box is mountain-top to valley in ideal
   conditions; makers say so in the small print. Plan on a mile or two between handhelds in town
   (→ 29-09).
4. **Licence (before the collapse).** See the box below.
5. **NOAA weather and SAME alert.** Many two-way radios can listen to the seven NOAA weather
   channels. A **SAME** radio sounds an alarm only for the counties you program (→ 15-01,
   → 29-10). {{#each region.home.nwr as t}}Our nearest transmitter: {{t.call}} on {{t.freq}} MHz,
   SAME code {{t.same}}. {{/each}}
6. **Power source.** Radios that also take ordinary AA or AAA cells keep working when the
   rechargeable pack is flat and you have no way to charge it. Mobiles run from 12 V.
7. **Repeater capable and removable antenna.** GMRS radios that work through a repeater (a relay
   on a tower or hill) reach much farther. A removable antenna lets you fit a better one; FRS
   antennas are fixed by rule.
8. **Privacy codes are not privacy.** They only stop you hearing other users; anyone on the
   channel without a code hears you.

> **Before the collapse:** transmitting on **GMRS** needs an FCC individual licence; the rule says
> one licence lets the holder's immediate family operate the holder's stations, and it normally
> runs ten years (47 CFR 95.1705). Midland gives the fee as $35. **Amateur** radio needs an exam
> and a licence. **FRS** radios are sold as licence-free. Listening needs no licence. The maker of
> one popular inexpensive dual-band handheld describes it as legal for use on amateur frequencies,
> which means transmitting needs an amateur licence. → 15-05, → 29-09.

## Common models, from the makers' own pages

"See label" means the maker's page read for this kit did not give it.

| Model | Service | Transmit power | Licence (pre-collapse) | NOAA weather | Power source | Other | Source |
|---|---|---|---|---|---|---|---|
| Midland LXT600VP3 | FRS handheld | HI/LO; watts: see label (FRS limit 2 W) | Licence-free (Midland) | Weather alert and scan | NiMH packs or AAA cells | 22 + 14 extra channels | Midland, LXT600VP3 page |
| Midland GXT1000VP4 | GMRS handheld (drops to FRS power on 8–14) | See label | GMRS licence required (Midland) | Weather alert and scan | Rechargeable packs; desktop, AC and DC chargers | 50 channels | Midland, GXT1000VP4 page |
| Midland MXT275 | GMRS mobile ("MicroMobile") | 15 W | GMRS licence | Weather scan and alert | 12 V vehicle power cord | 15 high-power channels; 8 repeater channels; external magnetic antenna | Midland, MXT275 page |
| BTECH GMRS-V2 | GMRS handheld, repeater compatible | 0.5 W / 5 W; low power only on 8–14 | GMRS licence (47 CFR 95.1705) | NOAA receiver and scan | 7.4 V Li-ion pack, USB-C charging | 200 programmable channels; IP54 splash resistant; −4 to 140 °F | BTECH, GMRS-V2 page |
| BaoFeng UV-5R | Amateur dual-band (136–174 and 400–520 MHz) | 5 W / 1 W (first-generation page text says 4 W / 1 W) | Amateur licence; "legal for use on amateur frequencies" (maker) | Not stated | 7.4 V 1,500 mAh Li-ion pack | 128 channels; also receives FM broadcast | BaoFeng Tech, UV-5R page |
| Cobra 29 LTD | CB, 40 channels, AM/FM | 4 W | See box above and → 15-05 | Not stated | Vehicle power; volts: see label | No single-sideband | Cobra, 29 LTD page |
| Uniden PRO520XL | CB, 40 channels | 4 W | See box above and → 15-05 | Not stated | See label | Emergency channel 9 key; PA function | Uniden, PRO520XL page |
| Midland WR120B | NOAA Weather Radio, receive only | Does not transmit | None | SAME; 25 programmable locations; 90 dB siren | AC adapter, 3 AA backup | Midland's page gives both 60 and 85+ alert types | Midland, WR120B page |

Motorola Talkabout and other models were looked for and left out because the kit could not read
their specifications on the maker's own page. The label inside a radio's battery compartment
carries its model and FCC ID; the manual carries its power and channel chart (→ 28-07).

## Our radios

{{#if has.gmrs}}We have FRS or GMRS radios.{{/if}} {{#if has.ham}}Someone in the household has a ham
radio or licence.{{/if}} {{#if has.noaa_radio}}We have a NOAA weather radio.{{/if}}

| Radio | Model | Service | Watts | Batteries (and spare type) | Our channel and code | Licence holder and call sign |
|---|---|---|---|---|---|---|
| ______ | ______ | ______ | ______ | ______ | ______ | ______ |
| ______ | ______ | ______ | ______ | ______ | ______ | ______ |
| ______ | ______ | ______ | ______ | ______ | ______ | ______ |
| Weather radio | ______ | NOAA (receive) | — | ______ | SAME code ______ | — |

{{photo radio-labels}}

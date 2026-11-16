---
id: 32-00-section-intro
section: 32-region-appendix
title: "Region appendix: how to read it"
version: 1
revised: 2026-11-16
layer: generated
danger_level: none
phase: [A, B, C]
tags: ["region", "section intro"]
derived_from: []
sources: ["census-gazetteer-2024", "usgs-3dep-epqs", "noaa-ncei-normals-1991-2020", "noaa-rcc-acis", "usda-phzm-2023", "nws-awips-counties-cwa", "noaa-national-weather-service-nwr-county-coverage-an-c6207f", "fema-nri-counties", "epa-ecoregions-level3", "nasa-power-climatology", "fema-state-ema-list", "hrsa-poison-help", "census-ct-planning-region-crosswalk", "nrel-solar-resource-api"]
related: ["15-01-weather-alerts", "17-01-blizzards-and-ice", "17-02-tornadoes", "17-03-floods", "17-04-extreme-cold-and-heat", "17-05-grassland-fire", "17-07-drought-and-water-scarcity", "05-01-a-small-high-yield-garden", "05-06-foraging-and-deadly-look-alikes", "05-17-wild-edibles-by-season", "09-05-solar-in-winter", "12-17-poisoning-and-ingestion"]
cards: []
explainers: []
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
## What this section is for

Section 32 carries the public reference data for every state and the District of Columbia, because a household may have to cross the country. Your home county is already filled into the subject pages (weather alerts, hazards, garden, solar, foraging). Use these pages for destinations, routes, and any place you end up.

## How to read the state pages

- **Climate** values are 30-year averages (1991 to 2020) from the National Weather Service cooperative and airport stations nearest each county, chosen with a penalty for a big difference in elevation. Real years swing well past them.
- **Frost dates** are medians: half of years have a later last spring frost, half an earlier first fall frost. → 05-01
- **Record low and high** are the extremes in the full record of the station used: a station with at least 30 years of record within 80 km where there is one (in remote Alaska, at least 20 years within 250 km).
- **Hardiness zone** is the 2023 USDA zone at the county centre: each zone is a 10 F band of the coldest night of a typical winter, split into a (colder half) and b.
- **Peak sun hours** are kilowatt-hours of sunlight per square metre per day on a panel tilted at your latitude and facing south. → 09-05
- **Weather radio:** program the six-digit SAME code of each county you care about, and tune the transmitter frequency listed. → 15-01
- **Ecoregion** is the US EPA Level III region at the county centre; plant and tree plates are grouped by ecoregion. → 05-06

## Hazard ratings

Each state page rates 13 natural hazards per county from 1 to 3, taken from the FEMA National Risk Index (FEMA, National Risk Index, December 2025 release). FEMA rates every county against all others in five classes. The kit maps them like this:

| FEMA class | Kit rating |
| --- | --- |
| Very High | 3 (High) |
| Relatively High | 3 (High) |
| Relatively Moderate | 2 (Moderate) |
| Relatively Low | 1 (Low) |
| Very Low | 1 (Low) |
| No Rating, Not Applicable, Insufficient Data | 1 (Low) |

| Kit hazard | FEMA hazard used |
| --- | --- |
| Tornado | Tornado |
| Blizzard and winter storm | Winter Weather |
| Ice storm | Ice Storm |
| Flood (river and coastal) | the higher of Inland Flooding and Coastal Flooding |
| Wildfire | Wildfire |
| Earthquake | Earthquake |
| Hurricane | Hurricane |
| Extreme heat | Heat Wave |
| Extreme cold | Cold Wave |
| Drought | Drought |
| Volcano | Volcanic Activity |
| Tsunami | Tsunami |
| Landslide | Landslide |

FEMA's rating weighs how often a hazard strikes, how much there is to damage, and how well the community recovers. A rural county can rate Low for a hazard that still happens there. Treat a 2 or 3 as "prepare for this", and a 1 as "less likely here than in most of the country", never as "cannot happen". → 17-01 → 17-02 → 17-03

## Limits

- Every value is for one point near the centre of the county. Large or mountainous counties vary a lot inside their borders.
- Weather stations are not in every county; the station used can be in the next county. Data files carry the station names and distances.
- Agency names and transmitter lists change. Before the collapse, check the state agency and the NWS county listing once a year.
- These pages were generated from public datasets and reviewed by AI, not by a person. South Dakota and Illinois were cross-checked against a second source first.

## Who to call anywhere

- Emergency: 911. Poison control: 1-800-222-1222 (HRSA, Poison Help, 2026). → 12-17
- Each state page names that state's emergency management agency.

## State pages

- → 32-01
- → 32-02
- → 32-03
- → 32-04
- → 32-05
- → 32-06
- → 32-07
- → 32-08
- → 32-09
- → 32-10
- → 32-11
- → 32-12
- → 32-13
- → 32-14
- → 32-15
- → 32-16
- → 32-17
- → 32-18
- → 32-19
- → 32-20
- → 32-21
- → 32-22
- → 32-23
- → 32-24
- → 32-25
- → 32-26
- → 32-27
- → 32-28
- → 32-29
- → 32-30
- → 32-31
- → 32-32
- → 32-33
- → 32-34
- → 32-35
- → 32-36
- → 32-37
- → 32-38
- → 32-39
- → 32-40
- → 32-41
- → 32-42
- → 32-43
- → 32-44
- → 32-45
- → 32-46
- → 32-47
- → 32-48
- → 32-49
- → 32-50
- → 32-51

## Sources

- 2024 Gazetteer Files: Counties (and ZIP Code Tabulation Areas). U.S. Census Bureau, 2024. Used for: county list, names, internal points, land area.
- Connecticut County to County Subdivision and Planning Region Crosswalk. U.S. Census Bureau, 2022. Used for: connecticut planning regions to the legacy counties nws radio still uses.
- Elevation Point Query Service (3D Elevation Program). U.S. Geological Survey, 2026. Used for: elevation at each county point.
- U.S. Climate Normals 1991-2020 (annual/seasonal and monthly normals by station, v1.0.1). NOAA National Centers for Environmental Information, 2021 (archive files 2023). Used for: january low, july high, precipitation, snowfall, frost dates, frost-free days.
- Applied Climate Information System (ACIS): station period-of-record daily temperature extremes. NOAA Regional Climate Centers, 2026-11-16 (data through 2025). Used for: record low and record high (and 4-km grid elevation where usgs did not answer).
- 2023 USDA Plant Hardiness Zone Map (GIS grids and ZIP code table). USDA Agricultural Research Service and Oregon State University PRISM Climate Group, 2023. Used for: hardiness zone.
- AWIPS Counties and County Warning Areas (shapefiles c_16ap26 and w_16ap26). NOAA National Weather Service, 2026-04-16. Used for: nws forecast office per county.
- NOAA Weather Radio Coverage by County. NOAA / National Weather Service, 2026-11-02. Used for: weather radio transmitters, frequencies and same codes.
- National Risk Index, county-level hazard ratings (December 2025 release). Federal Emergency Management Agency, 2025-12. Used for: hazard ratings.
- Level III Ecoregions of the Continental United States (revised 2013) and of Alaska. U.S. Environmental Protection Agency, 2013. Used for: ecoregion.
- NASA POWER Climatology: solar irradiance on south-facing tilted surfaces, 2001-2025. NASA Langley Research Center, Prediction Of Worldwide Energy Resources (POWER) project, 2026. Used for: peak sun hours, december and june.
- Solar Resource Data API: monthly average latitude-tilt irradiance (Perez-SUNY/NREL 2012). National Renewable Energy Laboratory (now National Laboratory of the Rockies), U.S. Department of Energy, 2012 data, queried 2026-11-16. Used for: cross-check of peak sun hours (verification only).
- Emergency Management Agencies (state offices and agencies of emergency management). Federal Emergency Management Agency, 2016-12 (archived copy). Used for: state emergency management agency names.
- Poison Help: 1-800-222-1222. Health Resources and Services Administration (HRSA), U.S. Department of Health and Human Services, 2026. Used for: poison control line (national).

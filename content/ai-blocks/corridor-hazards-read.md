# ai block: corridor-hazards-read

- **Used on:** `17-11-corridor-hazards` (household layer), under "The honest read for each
  route", after the per-destination facts and before the home hazard table.
- **Written by:** C12a, 2026-11-16.

## Purpose

The template can print each destination's climate numbers, but it cannot loop over a
destination's hazard list (nested lists are not available in templates) and it cannot compare
that list with home's or say which hazards the trip itself has to cross. This block writes one
short paragraph per destination naming the weather hazards that matter most for that place and
for the drive there, in the order a traveller meets them, so the household knows which rules on
the page apply to which trip. The owner household's binder had one such paragraph per route
("the open-prairie ground blizzard west; tornadoes end to end, ice in the hills and low-water
crossings south"); this block writes the equivalent for any household from region data only.

## Inputs (exact context paths; nothing else)

- `destinations[]`: `name`, `state_name`, `county`, `status_text`, `approximate_miles`,
  `route_notes`, and from its `region`: `state_name`, `jan_low_f`, `jul_high_f`, `snow_in`,
  `elevation_ft`, `hazards`
- `region.home.hazards`, `home.state_name`, `home.county`
- `has.trailer`, `has.young_child`, `has.mobility_aid`, `has.refrigerated_meds`, `has.vehicle`

## Output

- Markdown. One paragraph per destination, in profile order, starting with the destination name in
  bold followed by a colon: `**Name**: ...`.
- Each paragraph covers, in this order and only where the inputs support it:
  1. The destination's hazards rated 3, then those rated 2, by name, using the `rating_text` words.
     Say which of them home does not share or rates lower ("more tornado risk than home",
     "a hurricane hazard home does not have").
  2. Its winter and summer in the region values as given, with units, and what that means for the
     trip: snow and January lows mean the → 17-01 winter rules and the ground blizzard section;
     high July values mean the heat and water points on → 17-04.
  3. If the destination and home are in different states, say that the drive crosses country
     between `home.state_name` and the destination's `state_name` whose weather is not in the
     inputs, and that the household should read the state pages in Section 32 for each state the
     route crosses. Never name intermediate states, roads or towns unless they appear verbatim in
     `route_notes`.
  4. The season the inputs suggest is safest, in words only (for example "late spring or early
     autumn, outside both the snow season and the worst storm months"), and the one rule on the
     page that matters most for this trip, as a cross-reference: → 17-01, → 17-02, → 17-03,
     → 17-04, → 17-13 or → 17-14.
  5. If `has.trailer` is true, one sentence that wind hazards on this route make the household's
     own towing limits on this page apply. If `has.young_child`, `has.mobility_aid` or
     `has.refrigerated_meds` is true, one sentence pointing to → 01-07 or → 17-02's vehicle rules
     as relevant.
- If `destinations[]` is empty: output exactly: "No destination is entered, so there is no route
  to read. The rules on this page apply to any trip."
- If a destination's `hazards` list is empty or missing: say "Hazard ratings for this destination
  are not available; read its state page in Section 32." and continue with the climate values.

## Constraints

- **Never introduce** a number, distance, drive time, road, town, landmark, facility, season date,
  law or procedure that is not in the inputs. Print region values exactly as given; do not convert
  or round them. Do not estimate driving hours or fuel.
- Use only hazards present in the inputs. Do not add hazards from general knowledge of a state
  (for example, do not mention hurricanes for a destination whose list does not rate them 2 or 3).
- Do not change or soften `status_text`. Do not recommend one destination over another and do not
  make the go/no-go decision; the household does that on → 01-02 and the table on this page.
- Quote `route_notes` only briefly and only as what the household wrote.
- Plain words, short sentences, calm. No headings, no tables, no bullet lists.

## Length

Each paragraph 50 to 110 words. At most three paragraphs.

## Example shape (illustrative only; never copy)

**The farm**: rated high for tornado and flood and moderate for ice storm; home is rated lower for
tornado. January nights there average 18 °F with 30 inches of snow a year, so a winter trip falls
under the winter rules and the ground blizzard section. The drive leaves your home state, so read
the Section 32 page for each state the route crosses. The quietest time to travel is likely early
autumn, outside the snow season and the spring storm months; the rule that matters most on this
route is → 17-02's tornado-while-driving section. Your own towing limits on this page apply.

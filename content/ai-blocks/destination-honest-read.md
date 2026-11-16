# ai block: destination-honest-read

- **Used on:** `01-05-choosing-a-destination` (household layer), under "The honest read", after
  the destinations table and the status definitions.
- **Written by:** C01, 2026-11-16.

## Purpose

One short, honest paragraph per destination that pulls together what the template can only print
in separate cells: how its status, distance, climate and hazards, the people there, and this
household's needs fit together, and what remains to be done to make it real. The owner household's
binder had such a paragraph per destination ("the distance is the whole problem: a one-shot early
trip, never a reactive winter one"); this block writes the equivalent for any household from its
own answers and the region data.

## Inputs (exact context paths; nothing else)

- For each `destinations[]` entry, in profile order: `name`, `state_name`, `county`,
  `status_text` (agreed / unannounced / property only / undecided), `who_is_there`,
  `how_to_reach_them`, `route_notes`, `approximate_miles`, and from its `region`: `jan_low_f`,
  `jul_high_f`, `snow_in`, `zone`, `hazards` (name, rating, rating_text).
- Household: `household.size`, `home.county`, `home.state_name`, `region.home.hazards`.
- Flags: `has.refrigerated_meds`, `has.oxygen`, `has.cpap`, `has.mobility_aid`, `has.anaphylaxis`,
  `has.infant`, `has.young_child`, `has.elder`, `has.pregnant`, `has.pets`, `has.vehicle`,
  `has.trailer`, `has.condition.CL-NN`.

## Output

- Markdown. For each destination, one paragraph starting with the destination name in bold and its
  status in bold, e.g. `**Name** (**agreed**): ...`. Paragraphs in profile order.
- Each paragraph covers, in this order and only where the inputs support it:
  1. What the status means for this place in practice (expected or not; can supplies be cached).
  2. Distance in the household's own miles, and what that implies for timing: a long trip suits
     only an early, seen-it-coming departure in good weather; a short one can be a later move. Say
     "the fuel worksheet on → 01-03" rather than computing fuel.
  3. Winter and climate from the region values (state the values as given, with units), and the
     destination hazards rated 2 or 3 by name, compared with home's in words ("more", "fewer",
     "different").
  4. The household's needs that make this place harder or easier, in words (for example
     refrigerated medicine and an unknown power source; a wheelchair and an unknown house; a
     small child and a working farm), pointing to → 01-07 for medical needs.
  5. The one or two most important open items, chosen from: ask them; visit; place a cache;
     settle water, heat, storm shelter or medical distance; drive the route.
- If `destinations[]` is empty: output exactly: "No destination is entered. Until one is agreed,
  staying is strongly preferred, and the realistic move is toward town, family or medical help.
  Add destinations in settings and regenerate."

## Constraints

- **Never introduce** a number, distance, drive time, road, town, facility, phone number, law or
  procedure that is not in the inputs. Use `approximate_miles` exactly as given; do not convert it
  to hours or fuel. Do not name highways, hospitals or pharmacies unless they appear verbatim in
  `route_notes` or `who_is_there`.
- Do not change or soften the status. An unannounced or undecided destination is never described as
  safe, expected or reliable. Property only is never described as having anyone there.
- Do not recommend one destination over another, and do not make the go/no-go decision; the
  household does that on → 01-02.
- Quote the household's free text (`who_is_there`, `route_notes`) only briefly and only as fact
  about what they wrote; never invent relationships or agreements.
- Plain words, short sentences, calm. No headings, no tables, no bullet lists.

## Length

Each paragraph 50 to 110 words. At most three paragraphs (the profile allows three destinations).

## Example shape (illustrative only; never copy)

**The cabin** (**property only**): nobody lives there, so nothing has been kept warm or stocked
unless you did it, and someone may be there before you. At about 140 miles it is within reach of a
later departure, but check → 01-03's fuel worksheet. January lows of 4 °F and 60 inches of snow a
year make it a hard winter arrival. With refrigerated medicine in the household and no known power
source there, the cold chain has to ride with you (→ 01-07). Next: visit, and decide what can be
cached there safely.

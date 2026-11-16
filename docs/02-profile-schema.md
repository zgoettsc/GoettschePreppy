# Profile schema: every question the settings page asks

The settings page is a walkthrough in nine steps. Each step shows the never-stored notice. Every
field below maps to `schema/profile.schema.json`. Required fields are marked **req**. Everything
else may be skipped and the binder then prints a blank to fill by hand, never a guess.

Writing level: the person has never prepped. Each question carries a one-line "why we ask" that the
page shows beneath it, listed here in italics.

## Step 0. Access and privacy

| Field | Type | Notes |
|---|---|---|
| access_key **req** | string | Checked by hash at the relay; never stored on the page. |
| acknowledged_notice **req** | boolean | The never-stored and private-copy notice, read and ticked. |
| save_profile_locally | boolean | Offer to download `profile.json` to the user's device at the end. Default off. |

## Step 1. Home base

*Where you live decides your weather, your hazards, your plants, your radio frequencies and your
state's emergency contacts. We ask for the county, not your street.*

| Field | Type | Notes |
|---|---|---|
| state **req** | US state or DC | Promotes this state's region data to the front; all states stay in the appendix. |
| county **req** | string, validated against the state's county list | Drives SAME code, NWS office, hardiness zone and climate normals. Never ask for a street address. |
| nearest_town | string | Used only in prose ("the drive from <town> to ..."). Optional. |
| setting **req** | enum: urban, suburban, small-town, rural, remote | Changes defaults for water, security, light discipline, scavenging, neighbours. |
| elevation_band | enum: low (<2,000 ft), mid, high (>6,000 ft) | Altitude affects boiling, cooking times, cold and solar. Optional; derived from county if blank. |

## Step 2. The dwelling

*Your house decides how you heat one room, where you shelter from a tornado, where fuel can live,
and how you get water when the taps stop.*

| Field | Type | Notes |
|---|---|---|
| dwelling_type **req** | enum: detached house, townhouse/duplex, apartment, mobile/manufactured, farm/ranch, other | Apartments remove generator, fuel-storage and well pages from the front but keep them in the appendix. |
| stories | integer 1 to 4 | |
| basement | enum: none, full, walkout, crawlspace | Walkout basements change the warm-room and fallout advice. |
| windowless_interior_room | boolean + free text "which room" | Tornado shelter spot. |
| water_supply **req** | enum: municipal, private well, shared well, cistern/haul, other | Well selects the well gear module. |
| sewer **req** | enum: municipal sewer, septic, other | Septic selects the septic module. |
| primary_heat **req** | enum: natural-gas furnace, propane furnace, heating oil, electric resistance, heat pump, wood stove/insert, pellet stove, other | Decides which fuel explainers and heater modules lead. |
| gas_service | enum: none, natural gas, propane tank (size) | Gas shutoff page is included only when present. |
| cooking_fuel | enum: electric, natural gas, propane, other | |
| water_heater | enum: none, tank gas, tank electric, tankless, size in gallons | A tank heater is 40 to 50 gallons of stored water; the page says how to use it. |
| fireplace_or_firepit | multi: indoor fireplace, wood stove, outdoor fireplace, fire pit, none | Outdoor cooking page adapts. |
| pool_or_hot_tub | enum: none, chlorine pool, saltwater pool, hot tub + approximate gallons | Selects the pool water module. |
| garden_space | enum: none, containers/balcony, small yard, large yard, acreage | |
| attached_garage | boolean | Fuel-storage decision card DC-05 only shows when true. |
| vehicles | list: type (car, SUV, pickup, van), fuel (gasoline, diesel, hybrid, EV), four-wheel-drive, towing | Fuel-transport and route pages; EV changes the power section. |
| trailer | enum: none, open utility, enclosed cargo, camper | Selects the trailer module. |

## Step 3. Household members

*Ages and weights decide water and calorie math, children's warmth and clothing, infant feeding,
and which published medical tables apply. Weights are used only to pick a row in a published table;
the binder never computes a dose.*

Repeat for each person (1 to 12):

| Field | Type | Notes |
|---|---|---|
| label **req** | string | First name or a nickname. Appears in the binder. |
| role **req** | enum: adult, teen (13 to 17), child (2 to 12), infant/toddler (under 2), elder (over 70) | |
| age_years **req** | integer | Months for under 2. |
| weight | number + unit | Optional for adults; asked for children because the epinephrine and KI tables are by weight and age. |
| sex | enum: female, male, prefer not to say | Only to show the pregnancy and menstrual pages at the front. |
| pregnant_or_nursing | enum: no, pregnant, nursing, both | Adds water and calorie allowances and the infant-feeding module. |
| conditions | multi-select from the condition library (CL-01 to CL-26) + "other" free text | Selected modules are promoted to the front of the medical section. |
| medications | list: name, strength, how often, refrigerated?, "what happens if I miss doses" (free text from the household) | Fills the "my meds" table. Never interpreted by the model beyond storage class (refrigerated or not). |
| allergies | list: allergen, reaction severity (mild, severe, anaphylaxis), carries epinephrine? | Drives CL-03/CL-04 and the food plan. |
| mobility_or_sensory | multi: wheelchair/walker, oxygen, hearing aids, glasses/contacts, CPAP, none | Power and device-protection pages. |
| skills | multi: medical professional, nurse/EMT, electrician, mechanic, hunter, HAM licence (callsign), farmer/gardener, firearms trained, none | Roles table; sets how far the explainers assume nothing. |

## Step 4. Pets and livestock

| Field | Type | Notes |
|---|---|---|
| pets | list: type (dog, cat, other), count, medications, food per day | Pets module incl. decision card DC-10. |
| livestock | list: type (chickens, rabbits, goats, cattle, horses, bees, other), count | Husbandry pages promoted; feed math. |

## Step 5. Destinations and routes

*If you ever have to leave, the binder should already know where you would go, how far it is, and
whether anyone is expecting you.*

Up to three destinations:

| Field | Type | Notes |
|---|---|---|
| name **req** | string | "Dad's farm", "the cabin". |
| state, county **req** | | Promotes that region's data (plants, hazards, climate) into a destination appendix. |
| status **req** | enum: agreed with the people there, not asked (would arrive unannounced), nobody there (property only), undecided | Printed plainly on the destination page. |
| who_is_there | free text | |
| how_to_reach_them | free text: phone, radio, letter | No numbers are validated or looked up. |
| route_notes | free text | Preferred roads, bridges to avoid, fuel stops. The binder adds the hazard dataset for every county the straight-line path crosses; it does not compute a driving route. |
| approximate_miles | integer | Household's own estimate; used for fuel and days math. |

## Step 6. Contacts and meeting places

| Field | Type | Notes |
|---|---|---|
| out_of_area_contact | name, relationship, phone | The family emergency plan page. |
| meeting_place_near_home | free text | |
| meeting_place_in_town | free text | |
| meeting_place_out_of_town | free text | Usually destination 1. |
| utility_contacts | electric, gas, water: provider name and outage number, as the household reads them from their own bills | The kit does not look these up (see the household binder's gas-utility lesson). |
| local_contacts | free text list | Doctor, vet, pharmacy, neighbours. |

## Step 7. Gear owned

*Tick what you already have. For each item the binder adds the matching module, written for that
class of gear, with a spec row for your model if we know it and a blank row to fill from the label
if we do not.*

| Group | Fields |
|---|---|
| Power | power stations (model, Wh), solar panels (model, W, count), generator (fuel: gasoline, propane, dual, diesel, inverter?; watts), transfer switch or inlet (none, interlock, cord-and-plug conversion, transfer switch), car inverter |
| Heat | portable propane heater (model), wick kerosene heater (model), ducted diesel/kerosene heater, wood stove, pellet stove, electric space heaters only |
| Fuel on hand | gasoline (gal), diesel (gal), kerosene (gal), propane (1-lb count, 20-lb count, bulk tank gal), firewood (cords), charcoal (lb), lamp oil |
| Water | stored water (gal), filters (brand/type), bleach or pool shock, water barrels |
| Cooking | camp stove (fuel), rocket stove, Dutch oven, solar oven, electric kettle/hot plate |
| Comms | NOAA weather radio, FRS/GMRS radios, GMRS licence, HAM radio (callsign), CB, satellite messenger, Starlink |
| Medical | first-aid kit tier (none, basic, trauma, long-haul), CO alarm count, smoke alarm count, fire extinguishers (count, location), fire blankets |
| Security | firearms owned (yes/no); if yes: platforms and calibers (free text), safe (yes/no), suppressors (yes/no) |
| Food | shelf-stable pantry (days), bulk staples (lb), freeze-dried (servings), canning equipment (water bath, pressure canner with gauge type), dehydrator, garden seeds |
| Transport | bicycles, hand cart, snowshoes/skis |

## Step 8. Experience and risk tolerance

| Field | Type | Notes |
|---|---|---|
| experience **req** | enum: new to all of this, some camping and basic prep, experienced | Sets explainer depth: new = every explainer at the front; experienced = explainers in the appendix. |
| decision_cards **req** | one choice per card DC-01 to DC-24: an option id or "undecided" | Undecided prints the card open with the options and a box. |
| notes_for_the_binder | free text | Anything else the household wants on the family plan page. |

## What is never asked

Street address, exact coordinates, Social Security or account numbers, safe combinations, gun
serial numbers, the location of valuables, photographs (those are attached locally and never sent),
employer, income. The family plan page has blank lines for the household to write some of these by
hand after printing, with a note saying why they were not typed into a web page.

# Decision cards and floors

Owner decision G4. The household binder ended with about twenty risk acceptances that are one
family's choices. In the kit none of them is a default. Each becomes a decision card the household
reads and answers in settings (or leaves open and answers on paper). A card never pretends the safe
choice and the convenient choice are the same thing.

## Part A. Card format

Every card is one page, written for someone who has never heard of the subject.

1. **The thing, in plain words.** What a 20-lb propane cylinder is, what "unvented" means.
2. **The rule as the manufacturer or agency states it, and why they set it.** Named, with the
   mechanism: "Propane tanks over 1 lb are not allowed indoors by the fire code because a leaking
   valve fills a room with heavy gas that pools at floor level and ignites from a pilot light."
3. **How it actually hurts people.** The specific injury, the specific sequence.
4. **What makes it safer**, in order of how much each step helps. Marked "removes the risk",
   "reduces it a lot", "reduces it a little".
5. **The options.** Usually three: follow the rule; do it with every mitigation; do it anyway. Each
   option says what you give up and what you accept.
6. **Our choice** box, with the household's settings answer printed and space to change it by
   hand, and the date.

## Part B. Floors: things the card does not offer as a choice

These are not risk trade-offs. They are the handful of mechanisms where there is no mitigation
and the failure is death or permanent injury without warning. The binder states them as rules,
explains why in the same plain words, and does not print an options box.

| Floor | Why there is no card |
|---|---|
| Never run a generator, charcoal, or any engine indoors, in a garage, or near an open window. | Carbon monoxide kills in minutes with no warning; alarms fail; there is no mitigation that works every time. |
| Never connect a generator to house wiring without a transfer switch, interlock, or a cord-and-plug conversion with the main breaker locked off. Never backfeed through an outlet. | Electrocutes line workers and neighbours; fire. |
| Never loosen a tourniquet once placed; mark the time. | Re-bleeding and clot release kill. |
| Low-acid foods are pressure-canned to the published time and pressure, or not canned. | Botulism has no field treatment and the food looks and smells normal. |
| No wild plant or mushroom is eaten on a "test"; identification or nothing. | The deadly ones are not detectable by taste tests and the dose is small. |
| Fuel is never stored or transferred near an open flame or a running appliance. | Vapour ignition. |
| A frozen-then-thawed insulin vial or pen is discarded. | Loss of potency with no way to tell; the published guidance is unanimous. |
| Bleach or pool shock is never mixed with ammonia, acids or other cleaners. | Chlorine gas. |
| Children do not have access to firearms, fuel, medications or chlorine products. | Fixed in every source. |

## Part C. The cards

Options are listed with their id for the profile (`decision_cards.DC-xx`).

| Card | Trade-off | Options |
|---|---|---|
| DC-01 | **An unvented heater running while people sleep.** | `never` keep heat by other means overnight; `alarm-and-wake` lowest setting, tested CO alarm at pillow height, two vents open, barrier, someone wakes every 3 hours; `run-it` run it with alarms and vents. |
| DC-02 | **A propane cylinder larger than 1 lb inside the house.** | `never`; `last-resort` only with a hose through a window, cylinder outside; `indoors-with-rules` cylinder indoors, valve closed when not burning, no pilot appliances, alarm. |
| DC-03 | **Refilling 1-lb propane cylinders from a 20-lb tank.** | `never` (manufacturer position); `by-weight` refill only with a refillable-rated cylinder, weighed, outdoors, leak-checked. |
| DC-04 | **Using expired or heat-exposed epinephrine, or other expired medication, when no in-date supply exists.** | `discard`; `use-if-clear` use if the solution is clear and colourless, and keep seeking in-date stock. |
| DC-05 | **Storing gasoline, kerosene or propane in an attached garage.** | `outbuilding-only`; `garage-with-rules` approved cans, away from ignition sources, transfer outdoors, quantity cap written on the card. |
| DC-06 | **Carrying fuel inside a passenger vehicle.** | `never-inside` roof, hitch carrier or trailer only; `cargo-area-shortest-time` sealed cans, cargo area, windows cracked, shortest possible leg. |
| DC-07 | **Converting a furnace or well pump to cord-and-plug yourself so a generator can run it.** | `electrician-only`; `diy-with-write-up` follow the kit's write-up, main breaker off and locked, tested before it is needed. (Backfeeding is a floor, not an option.) |
| DC-08 | **Using insulin or other refrigerated medication after a heat excursion.** | `discard-after-window` follow the published unrefrigerated window exactly; `use-and-watch` use beyond the window if no alternative, with closer monitoring. (Frozen is a floor.) |
| DC-09 | **Infant or toddler sharing a bed with adults for warmth.** | `separate-sleep-surface`; `bed-share-with-rules` over 12 months, firm surface, no heavy covers over the child, sober adults. |
| DC-10 | **Pets when food, water or movement makes keeping them impossible.** | `keep-at-all-costs`; `release-with-food-out`; `humane-end` with the method page. |
| DC-11 | **Firing weapons on your own property for practice or zeroing.** | `never`; `with-backstop-rule` only against a known backstop, no one downrange, neighbours told. |
| DC-12 | **Defensive use of force.** | A worksheet, not a multiple choice: the household writes its rule in its own words after reading the page; the state law line is printed as a pre-collapse note. |
| DC-13 | **Drinking water from a pool, hot tub or untreated surface source.** | `distill-only`; `filter-and-chlorinate` for fresh pools; `drink-treated-surface-water` with the treatment ladder. |
| DC-14 | **Eating food past its date, dented or rusted cans, or food from a failed freezer.** | `label-strict`; `inspect-and-eat` with the rules for each case. (Bulging, leaking or spurting cans are a floor: discard.) |
| DC-15 | **Giving someone else's prescription medication.** | `never`; `same-drug-same-strength-only` with the page's cautions. |
| DC-16 | **Antibiotics without a prescription (veterinary or stockpiled).** | `never`; `last-resort` only with the infection-signs page and the published adult-dose table printed as published, children excluded. |
| DC-17 | **Old kerosene, diesel or gasoline in a heater or engine.** | `fresh-only` with the rotation schedule; `jar-test-and-use` with the test on the page. |
| DC-18 | **Feeding a food-allergic person unlabeled, traded or scavenged food.** | `never`; `single-ingredient-only`; `with-epinephrine-in-hand` and the household's own line. |
| DC-19 | **When to leave home.** | A worksheet: the triggers page, with the household's own thresholds written in. |
| DC-20 | **Open-flame cooking or candles indoors.** | `never-indoors`; `with-extinguisher-and-alarm`. |
| DC-21 | **Using a fireplace or wood stove that has not been inspected this year.** | `inspect-first` using the page's own inspection; `use-with-small-fires-and-watch`. |
| DC-22 | **Potassium iodide for adults over 40.** | `follow-fda-table` (not recommended over 40 unless very high exposure); `take-anyway`. |
| DC-23 | **Chlorinating water beyond label strength when the water is very dirty.** | `label-dose-and-filter-first`; `double-dose-and-wait`. |
| DC-24 | **Letting children do dangerous jobs (fire, fuel, tools, animals) because hands are short.** | A worksheet: age bands and the household's rule for each job. |

## Part D. How a card gets into the binder

Every card is a core page with one slot: the choice. The settings page shows the card's first five
parts, exactly as printed, before asking. The generation model copies the choice into the box and
nowhere else; it does not reword the card. The consistency review pass checks that every other page
that mentions the trade-off refers to the card and does not state a different rule.

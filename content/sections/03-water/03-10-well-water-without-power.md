---
id: 03-10-well-water-without-power
section: 03-water
title: "Well water without power"
version: 1
revised: 2026-11-16
layer: gear
danger_level: caution
phase: [A, C]
tags: [water, well, submersible pump, pressure tank, generator, well bucket, bailer, hand pump, shock chlorination]
derived_from: [03-10-well-water-without-power]
sources: [cdc-guidelines-for-testing-well-water-382a7a, cdc-how-to-disinfect-wells-after-an-emergency, university-of-nebraska-lincoln-extension-private-dri-332afd, university-of-arizona-cooperative-extension-private-f2355a, water-systems-council-wellcare-information-sheet-wha-7d070e, simple-pump-co-manufacturer-deep-well-hand-pumps-bac-bd4b3b]
related: [03-01-daily-water-needs, 03-02-storing-water, 03-04-purifying-water, 03-06-winter-water, 03-07-testing-water, 01-04-phase-c-establish, 01-05-choosing-a-destination, 09-04-generators, 09-08-wiring-and-safety, 13-11-disease-outbreak, 13-12-septic-off-grid, 18-01-mutual-aid, 28-03-generators, 29-04-ex04-electricity-in-the-house, 30-01-the-floors, 30-08-dc07-diy-cord-and-plug-conversion]
cards: [DC-07]
explainers: [EX-04, EX-05]
promote_when: [has.well]
photo_slots:
  - { id: wellhead, caption: "Our wellhead and cap, with the casing diameter visible" }
  - { id: well-breaker-and-tank, caption: "The well pump breaker in the panel, the pressure tank and the pressure switch" }
figures: [fig-drilled-well-parts]
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: null
---

# Well water without power

**What this page is for.** Getting water out of a drilled well when the grid is down, at your
own home or at any place you might go that has one. A drilled well's water really comes from
an **electric pump** at the bottom of a narrow pipe: no power, no pump, no water, unless you
have planned one of the four ways round it below.
{{#if has.well}}Your home is on a well: this page is for you now.{{else}}Your home is on
{{ dwelling.water_supply }}. Keep this page for a destination, a relative's farm, or a
neighbour's well.{{/if}}

> **CAUTION.** Two ways to get hurt here.
> - **Electricity.** Generator-to-pump wiring is dangerous (→ 09-04, → 09-08, → 29-04).
>   **Floor:** never connect a generator to house wiring without a transfer switch, an
>   interlock, or a cord-and-plug conversion with the main breaker locked off. Never backfeed
>   through an outlet. Backfeeding electrocutes line workers and neighbours and starts fires.
>   (→ 30-01)
> - **Floor:** never run a generator indoors, in a garage, or near an open window. Carbon
>   monoxide kills in minutes with no warning. (→ 30-01)
> - **Contamination.** One dirty rope lowered down the well can foul the water everyone
>   drinks. Everything that goes down the pipe is clean.

## Do this now

1. **Buy a well bucket (cylinder bailer) and enough rope to reach the water, with margin.** It
   fits in a tote, and it is the one option that works on any drilled well with no power and
   no information. An ordinary bucket will not fit down a well.
2. **Fill in the well survey below** for your well and any well you might use. Ten minutes at
   the wellhead with a flashlight and a phone camera answers every open question on this page.
   Pull a water sample the same visit (→ 03-07).
3. **At someone else's place, ask what already exists.** A working farm has often solved this
   before: a standby or tractor-driven generator, a windmill stock well, a spring. Plugging
   into their system may be the right first move. Arrive assuming nothing is there for you.
4. **Do not open a well cap casually.** Sealed is safe. Open it only with clean hands, cleaned
   gear and a reason.

## What a drilled well is

{{figure fig-drilled-well-parts}}

- **The casing:** a steel or plastic pipe, usually **4 to 6 inches across** for a home well,
  set down to the water-bearing rock or gravel, often 100 to 300 feet or more. A sanitary
  **well cap** seals the top. Below it is a narrow, dark, wet tube.
- **The submersible pump:** an electric pump hanging near the bottom on a **drop pipe**,
  pushing water up. Most home submersible pumps run on **240 volts**; smaller ones (1/2
  horsepower) are sometimes 120 volts. That one fact decides the generator question.
- **The pitless adapter:** the underground fitting where the water line leaves the casing
  **below the frost line** and runs to the house. It is why a well works in winter.
- **The pressure tank and switch:** inside the house or a well house, a tank (commonly
  labelled 20 to 80 gallons) holds water under pressure so the pump starts and stops instead
  of running at every tap. The pressure switch (often set at 30/50 or 40/60 psi) turns the
  pump on and off.

{{photo wellhead}}

## Four ways to get water with no grid, fastest first

### 1. What is left in the pressure tank (minutes of water, not days)

The tank keeps delivering until its pressure is gone. A tank delivers only about a quarter of
its labelled size before the pump would normally restart: a "30-gallon" tank gives perhaps
**5 to 10 usable gallons** (University of Nebraska-Lincoln Extension). Draw it into containers
from the lowest tap, on purpose, before it disappears into toilet flushes and hand washing.

### 2. A generator to run the pump (the fast fix, if the electrics match)

Check, in this order:

- **Pump voltage.** Find the well pump's breaker in the panel. **A double-width (2-pole)
  breaker means a 240-volt pump; a single breaker means 120 volts.** Confirm on the pump's
  control box or nameplate.
- **Generator voltage.** Read the generator's label. **A 120-volt-only generator cannot run a
  240-volt pump at any wattage.** Many small and inverter generators are 120 volts only.
  {{#if has.generator}}Your generator: {{ gear.generator_watts }} running watts. Its voltage
  (from the label): ______ V.{{/if}}
- **Starting surge.** Pump motors draw two to three times their running watts for a moment to
  start. A 1/2-horsepower pump runs on about 1,000 watts but may need 2,000 to 3,000 to start;
  a 1-horsepower pump may need 4,000 to 6,000 (Water Systems Council, What if the Power
  Fails?). **Size the generator to the start surge, not the running number.** A "soft-start"
  kit fitted to the pump circuit roughly halves the surge.
- **Connection.** Through a transfer switch or interlock, or by a proper connection at the
  pump's own disconnect: **never backfed through a wall outlet** (floor above; → 09-04,
  → 09-08). Rewiring a pump to a plug yourself is a decision with its own card: your choice
  {{choice DC-07}} (→ 30-08).
- **Run it hard and briefly.** Run the generator, refill the pressure tank and every
  container, shut down. A well pump is the textbook short, heavy job for a generator (→ 09-04).

{{photo well-breaker-and-tank}}

### 3. The well bucket (no power, no information needed: buy now)

A 4 to 6 inch casing takes no ordinary container. A **purpose-made well bucket** is a slim
cylinder, about **3 to 3.5 inches across and 3 to 6 feet long**, of galvanised steel or
plastic pipe with a one-way valve in the foot. It holds **1 to 2 gallons per pull**. Lower it
on rope past the drop pipe and the pump wires (go slowly; do not snag the wire), let it fill,
haul it up. Slow, honest work, and it works at any depth your rope reaches. This plus good rope
is the guaranteed floor under this whole page.

### 4. A deep-well hand pump (the permanent fix)

Purpose-built deep-well hand pumps (for example the Simple Pump or Bison types) fit **beside
the existing electric pump in the same casing**, under a two-hole well cap, and lift water
from around **200 feet down (some to 325 feet)** (Simple Pump Co., Deep Well Hand Pumps). The
cheap "pitcher pumps" sold for shallow wells stop working at about 25 feet of lift. **You
cannot choose one without the survey:** casing inside width, how far down the water stands,
and how much room the drop pipe leaves. Before the collapse, it is the project that turns a
well from grid-dependent to hand-powered for good.

## Keeping the wellhead from freezing

The buried line and pitless adapter are safe below the frost line. What freezes is the
**equipment above ground**: the pressure tank, the switch and exposed pipe in a well house or
basement. In a grid-down winter with the building unheated: insulate the tank and pipes, heat
a small well house if you safely can, or **drain the above-ground side between generator
runs** and treat each run as "fill everything, then drain" (→ 03-06). Never leave a full
pressure tank in a space going below freezing. The capped casing itself survives winter fine.

## Keeping the well clean

A well is the one water source that one careless draw can *ruin*, for everyone who drinks
from it.

- **Everything that goes down the casing is clean.** Wipe the bailer and the first several
  feet of rope with the container-cleaning solution on → 03-02 (1 teaspoon of 5 to 9 percent
  bleach per quart of water, 30 seconds), then rinse with treated water. The drinking-water
  dose on → 03-04 is far too weak to clean a surface. Keep the rope in a sealed bag, never
  coiled on the ground, and wash your hands first.
- **Keep the cap on** except during a draw. Rodents, insects and surface water running down the
  casing are the classic ways wells get contaminated.
- **Keep fuel, the generator and animals away from the wellhead** (20 feet or more), and check
  that the ground slopes *away* from the casing. Keep latrines and septic systems well away too
  (→ 13-07, → 13-12).
- **After anything gets in** (bailer work, pump repair, flood water over the wellhead):
  disinfect the well as below and re-test before trusting it (→ 03-07). Treat all water until
  then (→ 03-04).

> **Floor:** bleach or pool shock is never mixed with ammonia, acids or other cleaners. The
> mix gives off chlorine gas. (→ 30-01)

### Disinfecting ("shock-chlorinating") a well: the CDC method

Do this after flood water covers the wellhead, after any work down the casing, or after a
positive coliform test. It takes a day; everyone uses stored or treated water meanwhile.
Steps from the CDC (How to Disinfect Wells After an Emergency), in plain words:

1. **Bypass or close the valves to any water softener**, and take carbon filters and UV units
   out of the line: strong chlorine ruins them.
2. **Work out the depth of water in the well**: total well depth minus the depth down to the
   water (from the survey, the well record, or a weighted line).
3. **Find the bleach amount in the table below.** Use only unscented household bleach.
4. **Mix that bleach with 3 to 5 gallons of water** in a 5-gallon bucket.
5. **Remove the vent cap and pour the mixture into the well** through a funnel. Keep clear of
   all electrical connections.
6. **Circulate it:** attach a clean hose to the nearest outside tap and run water back down
   the well for thorough mixing (this needs the pump, so a generator; see above). Rinse the
   inside of the casing with the hose or a bucket for 5 to 10 minutes. If the pump cannot run,
   pour the mixture, then bail and pour back several bucketfuls to mix it.
7. **Open every tap in the house** and run each until you smell a **strong chlorine (bleach)
   smell** at it. Then close them all.
8. **Leave it at least 12 hours.** Nobody drinks, cooks with or bathes in the water.
9. **Drain it:** run a hose from an outside tap onto an area **with no plants**, such as a
   driveway, until the chlorine smell is gone. Do not drain it into streams or ponds, and do
   not send it into a septic system (it kills the bacteria a septic tank needs, → 13-12). Then
   run the indoor taps until the smell is gone.
10. **Until the water is tested, boil it** (rolling boil, 1 minute) or use another source.
    **Wait at least 7 to 10 days**, then have the water tested (→ 03-07). Testing cannot be
    done until all the chlorine is flushed out.

A second positive test means contamination is still getting in (a cracked casing, surface
water, a nearby septic system or latrine). Find the cause; do not keep re-shocking.

**Approximate amount of bleach for disinfecting a drilled or driven well** (CDC, printed as
published; bleach of 5 to 9 percent; amounts reach a chlorine level above 100 mg/L):

| Depth of water | 2 in casing | 4 in casing | 6 in casing | 8 in casing | 10 in casing | 24 in casing | 36 in casing |
|---|---|---|---|---|---|---|---|
| 10 feet | 3/4 tbsp | 3 1/4 tbsp | 1/2 cup | 3/4 cup | 1 1/4 cups | 7 cups | 1 gal |
| 20 feet | 1 1/2 tbsp | 6 1/2 tbsp | 1 cup | 1 1/2 cups | 2 1/2 cups | 14 cups | 2 gal |
| 30 feet | 2 1/4 tbsp | 9 3/4 tbsp | 1 1/2 cups | 2 1/4 cups | 3 1/4 cups | 1 1/4 gal | 3 gal |
| 40 feet | 3 tbsp | 13 tbsp | 2 cups | 3 cups | 5 cups | 1 3/4 gal | 4 gal |
| 50 feet | 3 3/4 tbsp | 1 cup | 2 1/2 cups | 3 3/4 cups | 6 1/4 cups | 2 1/4 gal | 5 gal |
| 100 feet | 7 1/2 tbsp | 2 cups | 5 cups | 7 1/2 cups | 12 1/2 cups | 4 1/2 gal | 10 gal |

1 cup = 8 fluid ounces = 16 tablespoons; 1 gallon = 16 cups. For water deeper than 100 feet,
the CDC table stops; the target is the same strong chlorine smell at every tap.

If you have only pool shock (calcium hypochlorite), dissolve it in a bucket of water first;
never pour dry granules down a well. The strong chlorine smell at every tap is still the
target (→ 29-05).

## Gear and supplies

| Item | Why | Notes |
|---|---|---|
| **Cylinder well bucket (bailer)** | Works with no power and no information | About 3 to 3.5 inches across, with a foot valve; must fit a 4-inch casing |
| Rope long enough to reach the water with margin, and a carabiner | Reaching the water | Braided rope; kept bagged and clean |
| Well-cleaning kit | Protects the well during draws; disinfects it | Fresh unscented bleach, gloves, eye protection, a sealed rope bag, a clean 5-gallon bucket, a funnel, a garden hose |
| Soft-start kit | Roughly halves the generator surge the pump needs | Fit after the survey: pump horsepower and voltage first |
| A spare pressure switch, and knowing how it works | The most common well electrical failure | Photograph the existing switch during the survey |
| Water test supplies | Same visit as the survey | → 03-07 |

**If you don't have it:**

- A bailer can be made from **3-inch plastic pipe, a foot check valve and an eye bolt**: farm
  store parts and one afternoon.
- A neighbour's larger generator that can supply 240 volts can run a pump yours cannot: a
  mutual-aid trade waiting to happen (→ 18-01).
- A windmill or solar stock well elsewhere on a farm is water already solved. Ask where the
  animals drink in winter.

## When it runs out

- **Runway:** the groundwater is effectively unlimited at household scale. The runway is
  **generator fuel**, or **arms and rope** with the bailer. At 1 to 2 gallons a pull, your
  {{ derived.water.plan_gal_day }} gallons a day (→ 03-01) is a manageable number of pulls by
  hand.
- **Ration:** the well changes none of the treat-and-test rules. Until test results are in,
  treat every gallon you draw (→ 03-04).
- **Resupply:** roof catchment, stock tanks, and snowmelt in winter (→ 03-06). A hand pump is
  the permanent way off the fuel treadmill.
- **The failure to fear** is not a dry well. It is a **fouled** one: a contaminated casing
  after careless draws or a flood. Discipline at the wellhead is the whole game.

## Phase notes

- **A (sheltering at home):** {{#if has.well}}fill in the survey now, buy the bailer and rope,
  and know your pump's voltage and your generator's.{{else}}you are on {{ dwelling.water_supply }}.
  If any place you might go has a well, buy the bailer and rope now and pack them with the
  survey sheet and test strips.{{/if}}
- **B (moving):** wells along a route are sealed and private. Carry water (→ 03-01).
- **C (rural or at a destination):** on arrival, water is job one (→ 01-04). Check what is left
  in the pressure tank, find out what the place already uses to run the pump, and fall back to
  the bailer the same afternoon if needed. Do not wait for a perfect generator answer before
  you start drawing and treating water.

### Well survey (photograph everything)

| Question | Answer |
|---|---|
| Which well (home or destination): | ________ |
| Casing diameter (measure the cap): | ________ in |
| Total well depth / depth down to the water (well record, owner, or a weighted line): | ________ / ________ ft |
| Pump voltage (breaker poles and control box): 120 V ☐ 240 V ☐ | Horsepower: ________ |
| Pump breaker location and amps: | ________ |
| Pressure tank location and size: | ________ |
| Well house? Heated how in winter? | ________ |
| Generator on site (watts; can it supply 240 V?): | ________ |
| Hand pump, windmill or stock wells nearby: | ________ |
| Well log or driller's record available? | ________ |
| Water sample taken (→ 03-07)? ☐ coliform ☐ nitrate | Date: ________ |

{{#if has.destinations}}Destinations to survey:
{{#each destinations as d}}- **{{ d.name }}** ({{ d.county }}, {{ d.state_name }}): well? ☐ yes ☐ no ☐ unknown
{{/each}}{{/if}}

## Cross-references

→ 03-07 testing water · → 09-04 generators · → 09-08 wiring and safety · → 28-03 generator
specifications · → 30-08 the cord-and-plug card · → 01-04 arrival · → 03-06 freezing ·
→ 03-04 treat until tested · → 13-12 septic

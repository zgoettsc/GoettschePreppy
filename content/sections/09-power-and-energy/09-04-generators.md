---
id: 09-04-generators
section: 09-power-and-energy
title: "Generators: fuel, siting, carbon monoxide and backfeed"
version: 2
revised: 2026-11-16
layer: core
danger_level: critical
phase: [A, C]
tags: [power, generator, carbon monoxide, fuel, backfeed, transfer switch, interlock, cord-and-plug, furnace, safety, noise]
derived_from: [09-04-generators]
sources:
  - us-consumer-product-safety-commission-cpsc-what-to-k-3390a4
  - cpsc-safety-alert-portable-generator-hazards-r8
  - cpsc-carbon-monoxide-information-center
  - cdc-carbon-monoxide-poisoning-basics-772153
  - american-red-cross-power-outage-safety-6d07a8
  - osha-quickcard-portable-generator-safety
  - osha-29-cfr-1910-333-r14
  - honda-eu2200i-owners-manual
  - honda-eu-generator-fuel-recommendations
  - generac-gp3500io-owners-manual
  - southwire-spec-10028-nm-b-r14
  - southwire-spec-70065-sjeoow-r14
  - hubbell-nema-configuration-chart-r14
related:
  - 09-03-batteries-and-storage
  - 09-08-wiring-and-safety
  - 09-14-car-batteries-in-practice
  - 09-15-generator-maintenance
  - 09-16-outage-day-one
  - 08-02-carbon-monoxide-safety
  - 08-04-emergency-heat-options
  - 06-05-alternative-fuels
  - 06-06-fuel-storage-safety
  - 06-07-moving-and-transferring-fuel
  - 14-03-opsec
  - 28-03-generators
  - 29-01-ex01-fuels
  - 29-03-ex03-carbon-monoxide
  - 29-04-ex04-electricity-in-the-house
  - 30-01-the-floors
  - 30-06-dc05-fuel-in-attached-garage
  - 30-07-dc06-fuel-in-passenger-vehicle
  - 30-08-dc07-diy-cord-and-plug-conversion
cards: [DC-05, DC-06, DC-07, DC-17]
explainers: [EX-01, EX-03, EX-04, EX-14]
promote_when: [has.generator]
photo_slots:
  - { id: generator-spot, caption: "Our generator spot: 20+ ft from the house, exhaust pointing away from every door, window and vent" }
  - { id: generator-panel, caption: "The generator's outlet panel and its label (running watts, outlets, breaker ratings)" }
  - { id: furnace-plug, caption: "The furnace plug, its wall receptacle and both labels (only if the cord-and-plug conversion was done)" }
figures: [fig-generator-siting, fig-generator-connection-options, fig-cord-and-plug-conversion]
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: { date: "2026-11-16", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "Backfeed floor reworded as 30-01; DC-07 write-up re-sourced (OSHA 1910.333 verify-dead, NEC 240.4(D) via Southwire, NEMA via Hubbell, cord ampacity via Southwire), grounding/strain relief added; motor start 3x (Generac); fuel months-not-years (Honda)" }
---

# Generators: fuel, siting, carbon monoxide and backfeed

**What this page is for.** How to use a portable generator without killing anyone, what it is
really for in a long outage (charging batteries fast, then off), how to start one that has never
been run, the ways it can safely connect to the house, and the cord-and-plug conversion for a
furnace or well pump if your household chooses to do it itself. Fuels are explained on → 29-01,
carbon monoxide on → 29-03, the breaker panel and transfer switches on → 29-04.

> **SAFETY. Generators kill people every year in two ways, and both are preventable.**
>
> **1. Carbon monoxide.** **Never run a generator, charcoal, or any engine indoors, in a garage,
> or near an open window.** Carbon monoxide kills in minutes with no warning; alarms fail; there
> is no mitigation that works every time (→ 30-01). One portable generator makes as much carbon
> monoxide as hundreds of cars (CPSC, Carbon Monoxide Information Center), and more than 80
> people die in the US every year from carbon monoxide from portable generators (CPSC, What to
> Know About Generators and Carbon Monoxide). Opening a door or window does **not** make an
> enclosed space safe. Run it **outdoors only, at least 20 feet from the house**, exhaust pointed
> away from your home and other buildings (CPSC; CDC, Carbon Monoxide Poisoning: Basics).
> Battery-powered carbon monoxide alarms on every level and outside sleeping areas (CPSC;
> → 08-02). Some generators shut themselves off when carbon monoxide builds up, and CPSC advises
> asking for that feature; many do not have it, and **a generator without one runs happily while
> it poisons a room.** Only distance protects you.
>
> **2. Backfeed.** **Never connect a generator to house wiring except through a transfer switch,
> or an interlock kit with the main breaker off. Never backfeed through an outlet with a
> double-male ("suicide") cord.** Backfeed electrocutes line workers and neighbours served by the
> same transformer, and the generator can burn or start a fire when grid power returns (→ 30-01;
> CPSC, Portable Generator Hazards; Honda, EU2200i Owner's Manual). A cord-and-plug conversion is
> not a connection to house wiring: the appliance is unplugged from the house outlet and plugged
> into the generator cord, so nothing reaches the panel (whether to do that conversion yourself
> is DC-07, → 30-08).
>
> **3. Fuel.** **Fuel is never stored or transferred near an open flame or a running appliance**
> (vapour ignition, → 30-01). Turn the generator off and let it cool before refuelling: gasoline
> spilled on hot engine parts can ignite (CPSC, Portable Generator Hazards).

## Do this now
- **Install carbon monoxide alarms now, before you own a generator.** Battery-powered, every
  level, outside sleeping areas. Test them; keep spare batteries. The single highest-value item on
  this page.
- **Choose the generator's exact outdoor spot today** and mark it: 20 feet or more from the house,
  exhaust aimed away from your house and the neighbours', not under a deck or overhang, on a dry,
  level, solid surface, under an open, canopy-like cover at most, where water cannot reach or
  pool under it (CPSC, Portable Generator Hazards). {{photo generator-spot}}
  {{figure fig-generator-siting}}
- **Decide how the generator will reach anything in the house** (section below): extension cords
  only, a transfer switch or interlock fitted by an electrician, or a cord-and-plug conversion.
  Our connection: **{{ gear.house_connection }}**. Cord-and-plug done yourself is a decision card:
  {{choice DC-07}} (→ 30-08).
- **Think of the generator as a battery charger, not a power supply.** For this plan it fills the
  battery bank fast, then shuts off.
- **Fuel plan:** which fuel first, where it is stored, how it is rotated (→ 06-06, → 09-15).
  Propane cylinders larger than 1 lb live outdoors or in an outbuilding, upright, valves closed,
  away from doors and vents. Keeping gasoline or propane in an attached garage is a decision card:
  {{choice DC-05}} (→ 30-06).
- **Copy these from your generator's manual onto this page now** (you will not have the internet):
  oil type and capacity ________ · break-in load and hours ________ · first oil change after
  ________ · lowest rated operating temperature ________ °F · fuel allowed (octane, maximum ethanol)
  ________ · starting-battery charging instructions ________. Model specs for common generators:
  → 28-03.
{{#if has.generator}}
**Our generator:** {{ gear.generator_watts }} W running, fuel: {{ gear.generator_fuel }}.
{{#if has.inverter_generator}}It is an inverter generator: clean power, suitable for charging
stations and for electronics.{{else}}It is a conventional generator: fine for tools and pumps;
charge electronics through a power station or a pure sine charger rather than directly where you
can.{{/if}} {{photo generator-panel}}
{{/if}}

## First start: a generator that has never been run

Many households own a generator that has sat in its box. **The first start should not happen in
an emergency, by someone who has never done it.** If it has to, follow this in order.

**Step 0: before you start (5 minutes).**
- **Carbon monoxide alarm on inside**, on the side of the house nearest the generator. Anyone
  inside who feels sick, dizzy or weak: everyone out to fresh air, then call for help.
- **Find the box parts:** the propane hose and regulator (dual-fuel models), the battery charger,
  the oil funnel, the spark-plug wrench, any remote. No propane hose means gasoline only.
- **Pick the spot** (above). It must not sit in rain or snow while running: an open-sided cover
  only, never an enclosure.

**Step 1: move it outside first, empty.** Most are heavy: two people, the wheels and handle. **Keep
it upright.** Fuel and oil go in **outdoors, at the spot**, never in the garage. If it has been
sitting in deep cold, below its rated operating temperature, warm it first.

**Step 2: oil first. Nothing else until this is done.** Many generators ship **without oil** (Honda
says so in capitals in its EU2200i manual), and starting one dry destroys the engine. On level
ground, open the oil cover, pull the dipstick, and pour the **4-stroke engine oil** grade your
manual names (never 2-stroke oil) slowly, checking the dipstick as you go. Small engines hold very
little. **Stop between the marks; do not overfill.** If oil has sat in it for years, change it
anyway. A **low-oil shutdown** that stops the engine means it was already running low: it is
there to stop the engine before damage, not to tell you the level (Honda).

**Step 3: battery (electric start).** On a new machine the battery plug may be held apart with a
tie: cut it and push the plugs together. A battery stored for years is probably flat. Charge it
with the supplied charger as the manual says, and unplug it after the manual's maximum time if the
charger is not a maintainer. A power station's AC outlet can run the charger in an outage. If
there is no charge, **plan on the pull cord, in gloves.**

**Step 4: propane hookup (dual-fuel).** Use **the hose and regulator that came with the
generator**, not a heater's hose.
1. Generator off. **Cylinder upright, valve on top, on the ground, on a flat surface, away from the
   exhaust side.**
2. Cylinder valve **fully closed** (turn clockwise). The cylinder needs an **in-date
   requalification date** on its collar or foot ring (how to read it: → 29-14).
3. Thread the hose on by hand, then snug it as the manual says. **Do not over-tighten.** Unless the
   manual says otherwise, no thread tape or sealant.
4. Open the cylinder valve. **Leak test:** brush **soapy water** on every joint. Bubbles that
   appear or grow mean a leak: close the valve, tighten, retest. Still leaking: **do not use
   propane.**
5. **If you ever smell propane, do not start it.** Close the cylinder valve first.

**Step 5: start.**
- **Propane:** nothing plugged in, any economy or idle-down switch off, fuel selector on propane,
  cylinder valve open, start as the manual says (button, remote or pull cord: pull slowly until you
  feel resistance, then fast). Wait for the ready light. A little roughness at first is normal.
- **Gasoline:** engine off and cool. **Read the can's label before you pour** (→ 29-01): colour
  is not proof of what is inside. Fresh gasoline only, the octane and ethanol your manual allows
  (Honda, for example, forbids fuel with more than 10% ethanol in its generators; Honda, Fuel
  Recommendations). Pour slowly to the fill mark, do not overfill, cap on, wipe spills and let
  them dry before starting.

**Step 6: break-in.** Follow the manual: usually a light, varied load at first and an early first
oil change (Honda's EU2200i schedule puts the first oil change at 20 hours). A power station on a
slow charge setting is a good break-in load.

**Step 7: connect loads with extension cords only** (unless a transfer switch, interlock or
cord-and-plug conversion exists, below). Heavy-duty cords made for outdoor use, with all three
prongs, undamaged, and rated for more watts than everything plugged into them (CPSC, Portable
Generator Hazards; OSHA, Portable Generator Safety). A cord's amps are printed on its jacket or
tag; a three-conductor 12 AWG cord is rated 20 A and a 14 AWG cord 15 A (Southwire, cord
specification, from the National Electrical Code's flexible-cord table). Unroll the cord fully.
**Biggest load first, one at a time.** **Never plug a cord into a house outlet.** Do not prop a
door or window open for the cord: openings let exhaust in; protect the cord where it passes a
door so it is not pinched (CPSC).
- **Medical devices run from a power station or battery that the generator charges, not straight
  from the generator.** Generator makers say the same: Generac's GP3500iO manual, for one, says it
  is not intended for critical life support.
- **Charging a power station:** amps = the station's AC charging watts ÷ 120 (1,200 W is 10 A;
  1,800 W is 15 A). Keep that under the generator outlet's breaker rating and under the cord's and
  plug's rating (an ordinary NEMA 5-15 household plug is rated 15 A; Hubbell, NEMA configuration
  chart). If the station has a slower "standard" charge setting, use it from an ordinary outlet.
  Faster rates need the generator's larger outlet with the matching heavy cord and adapter, or they
  trip the breaker and heat the plug.
- **Overload light?** Unplug everything, reset, reconnect fewer loads.

**Step 8: shut down in the manual's order.** Usually: unplug loads, let it run a few minutes with
no load, switch off, battery switch off, **close the propane valve fully** and disconnect the hose
when not in use. Let it cool (the manual gives the time) before moving or covering it.

**Step 9: write it down** on a label on the machine: date, run hours, fuel used. Maintenance and
the no-start sequence: → 09-15.

## Why it works this way

**A generator's role in a long outage is narrow.** It burns a finite, hard-to-store fuel to make
electricity. Run continuously, it exhausts the fuel you own within days, and it is **loud**,
audible a long way off in a silent, dark neighbourhood (→ 14-03). Its real job:

**Run it hard, briefly, to bulk-charge the batteries and run the big one-time loads, then shut it
off and live from the batteries.** A generator burns a lot of fuel even lightly loaded, so idling
one for a couple of lights is the worst use of it. Charge the bank, run the well pump, pull the
freezer down, do the laundry, then off.

**Generator types** (sizes and specs for common models: → 28-03):

| Type | Output | Notes |
|---|---|---|
| **Inverter generator** | Clean pure-sine power, quieter, sips fuel at low load | Best fit for battery charging and electronics |
| Conventional portable | Cheap watts, loud, rougher power | Fine for tools and pumps; questionable for sensitive electronics |
| Dual- or tri-fuel | Gasoline, propane, sometimes natural gas | **Propane stores for years without going stale** |
| Standby (whole-house, natural gas) | Automatic, powerful | Depends on the gas utility still flowing |

**Fuel is the real limit** (→ 29-01, → 06-06):
- **Gasoline** goes stale: **months, not years.** Stabiliser added when the fuel is fresh slows
  this, but it has its own shelf life and cannot fix fuel that has already gone off; Honda's advice
  is to drain the carburettor of a generator run less than once a month, and to put stabilised
  fuel that has sat a year in a can into a car instead (Honda, Fuel Recommendations; → 29-01). It
  is volatile and dangerous to store in quantity. Old fuel in an engine is a decision card:
  {{choice DC-17}} (→ 30-18).
- **Propane** does not go stale in a sealed cylinder; the cylinder itself has a requalification
  date (→ 29-01, → 29-14). Store cylinders outdoors.
- **Diesel:** follow the generator's manual for storage and winter fuel (→ 29-01).
- **Do the arithmetic honestly.** Run hours = fuel on hand ÷ fuel per hour at your usual load (the
  manual gives fuel use). Even a lot of stored fuel is **weeks of intermittent use, not months.**
  Build the plan on solar and batteries; use the generator to cover gaps.

**Sizing.** Match the generator to the largest thing you must start, not your average load. A
motor needs a burst of extra power to start: Generac's manual says to allow about 3 times the
listed running watts for starting motor loads such as a refrigerator or a pump (Generac, GP3500iO
Owner's Manual).

**The duty cycle that multiplies fuel:** run it about as long as it takes to refill the station or
bank (the station's manual gives the charge time at each rate), then shut it down. Do not charge a
station at its fastest rate and run another large load at the same time if together they approach
the generator's running watts.

## Connecting the generator to anything in the house

{{figure fig-generator-connection-options}}

| Way | What it is | Who does it |
|---|---|---|
| **Extension cords to individual appliances** | Cord from the generator outlet to the appliance's own plug | Anyone. Always allowed |
| **Transfer switch** | A switch, usually beside the panel, that connects chosen circuits to either the grid or the generator, never both | Licensed electrician; needs a generator its manual says is suitable |
| **Interlock and inlet** | A plate on the panel that physically prevents the main breaker and the generator breaker being on together, fed from an outdoor inlet | Licensed electrician; same generator requirement |
| **Cord-and-plug conversion** | A hard-wired appliance (furnace, well pump) is given a plug and a receptacle, so it can be unplugged from the house and plugged into a generator cord | Electrician, or yourself if your household chooses: {{choice DC-07}} (→ 30-08) |
| **Backfeed through an outlet** | A cord with two male ends from the generator into a wall outlet | **Never. Floor (→ 30-01)** |

**Why a transfer switch or interlock may not fit your generator.** A standard residential inlet and
interlock are 240 V (often a twist-lock four-prong inlet) and feed both halves of the panel. A
generator with only 120 V outlets cannot properly drive them; adapters that bridge both halves
from one 120 V outlet can overload shared neutral wires, and the generator's neutral arrangement
must match the transfer equipment. **Read your manual's specifications: if it says it is not
transfer-switch ready, or has no 240 V outlet, a transfer switch or interlock is not for it.** Ask
an electrician. Our connection: **{{ gear.house_connection }}**.

### If you choose the cord-and-plug conversion yourself (DC-07)

**The trade-off in one sentence:** a cord-and-plug furnace or pump is a hard-wired appliance made
unpluggable; the risk is the wiring work itself (a live wire while you work, a missing ground, a
loose terminal, a plug or cord too small, no strain relief), and doing it yourself instead of hiring
an electrician accepts that risk. Backfeeding is never part of it. Read the card first:
{{choice DC-07}} (→ 30-08). If you chose an electrician, give them this write-up. If you chose to do
it yourself, every step below is part of the choice. {{figure fig-cord-and-plug-conversion}}

**The conversion, in order:**
1. **Power off and verified dead.** Find the appliance's own breaker (a well pump on 240 V has a
   two-handle breaker). Switch it off, tape or lock it off, and hang a note on the panel. If you are
   not certain it is the right breaker, switch the **main breaker** off too. A service switch on the
   furnace cabinet is not enough on its own. **Then prove it dead where you will work:** check your
   meter on a known live outlet, test at the box hot to neutral, hot to ground and neutral to
   ground (every reading 0 V, or stop), then check the meter on the live outlet again. A
   non-contact tester is a second check, not a replacement for the meter. OSHA's rule for anyone
   working on electrical parts is the same: test them and verify they are de-energised before
   touching them, including for power arriving from an unexpected source (OSHA, 29 CFR 1910.333).
   The gas supply to a furnace can stay as it is: this is electrical work only.
2. **Find the appliance's disconnect or junction box.** Usually a switch in a box on or beside the
   furnace cabinet, or a junction box where the house cable enters.
3. **Read the circuit.** The breaker's amps and the house cable's size go together: 14 AWG copper
   is protected at 15 A and 12 AWG copper at 20 A (National Electrical Code 240.4(D), as printed in
   Southwire's NM-B cable specification). Read the appliance's nameplate amps and volts too.
4. **Choose parts rated for the circuit,** never smaller:
   - **15 A, 120 V circuit:** NEMA 5-15 plug and receptacle (rated 15 A, 125 V) and a
     three-conductor flexible cord of 14 AWG or heavier.
   - **20 A, 120 V circuit:** NEMA 5-20 plug and receptacle (rated 20 A, 125 V) and a
     three-conductor cord of 12 AWG or heavier.
   - **240 V appliance (many well pumps):** NEMA 6-series (250 V) parts of the circuit's amps, a
     cord rated for it, and a generator with a 240 V outlet. **If you are unsure, stop and call an
     electrician.**

   (Plug ratings: Hubbell, NEMA configuration chart. Cord ratings: a three-conductor 14 AWG
   flexible cord is rated 15 A and a 12 AWG cord 20 A; Southwire, cord specification, from the
   National Electrical Code's flexible-cord ampacity table. Use hard-usage cord such as type SJOOW.)
5. **Give the appliance a plug. Either:**
   - **(A) a male flanged inlet** of the right rating, mounted in a knockout on the cabinet or the
     disconnect box and wired to the appliance's hot, neutral and ground; the appliance is then fed
     by a cord with a female end; **or**
   - **(B) a cord with a male plug**, entering the junction box through a **strain-relief cord
     connector** tightened on the cord's outer jacket, so a pull on the cord never pulls on the
     terminals, and wired to the appliance's hot, neutral and ground.
6. **Wire it the same way at every end.** Black (hot) to the brass screw, white (neutral) to the
   silver screw, **green or bare (ground) to the green screw and to the appliance's grounding
   point.** **The ground is never left off:** no two-prong plug, no cut-off ground pin, no
   three-to-two adapter. A missing ground makes the cabinet live when a fault happens later.
7. **End the old hard-wired circuit in a receptacle.** The house cable that used to enter the
   appliance now ends in a receptacle of the same rating, in a box fastened in place, the cable
   clamped where it enters, within cord reach. **The appliance's neutral and ground travel with its
   cord;** nothing is left floating or re-bonded.
8. **Normal use: the appliance plugs into that wall receptacle.** Breakers back on; run it through
   a full cycle; afterwards feel the plug and receptacle: warm means a loose or undersized part
   (→ 09-08).
9. **Never a cord with two male ends. Never a connection into any house wiring** (no dryer-plug
   cords, no outlet-to-outlet cords). The only cord that touches the appliance has one male end and
   one female end.
10. **Label the plug** ("FURNACE: generator or station in an outage") and label the receptacle.
11. **Check the start surge before trusting a generator or station.** A blower or pump motor needs a
    burst of extra power for a moment at start; Generac's rule is to allow about 3 times the running
    watts. From the motor plate or cabinet label: running ______ W × 3 = ______ W at start. Compare
    with the generator's starting and running watts ({{ gear.generator_watts }} W running) and each
    station's continuous and surge figures (→ 09-03).
12. **Test it before you need it:** once on the generator (outdoors, 20+ ft), once on a station.
    Let the blower start and run a full cycle; watch for an overload light. Date it on the label:
    conversion done ☐ · tested on generator ☐ ______ · tested on station ☐ ______.
    {{photo furnace-plug}}

**Using it in an outage:**
1. Generator outdoors, 20+ ft, running and steady; carbon monoxide alarms on inside.
2. **Main breaker off, locked or taped**, as the figure shows. This is a second habit, not what makes the
   method safe: what keeps generator power out of the house wiring is that the appliance is
   unplugged from it (→ 30-08). With the main off, the house's appliances are also spared the surge
   when grid power returns (the Red Cross advises unplugging them for that reason).
3. Unplug the appliance from its wall receptacle. Plug it into the extension cord from the
   generator (or the station): one male end, one female end, rated for the appliance. Nothing else
   changes.
4. **A gas furnace also needs gas.** If the gas supply has stopped, the furnace gives no heat
   (→ 08-04).
5. **When the grid returns:** unplug the appliance from the generator cord, plug it back into its
   wall receptacle, then turn the main breaker back on.

## Cold weather and propane

Check your manual's lowest operating temperature. Below it, store the generator somewhere above
that temperature while it is off (if gasoline is in its tank, that is fuel storage: → 30-06), wheel
it out warm for the run, and bring it back between runs. **Never run it inside, not for a second.**

**What deep cold does to propane:**
- **A 20-lb cylinder's vapour supply weakens in deep cold.** Propane must boil off the liquid to
  feed the engine, and the colder the cylinder, the slower it boils. A small cylinder feeding a
  large load in sub-zero cold can starve the engine (surging, stumbling) while the cylinder frosts
  over and still reads "full".
- **The regulator can ice** below zero, choking the flow minutes into a run.

**Fixes, in order of value:**
1. **A larger cylinder**, or two 20-lb cylinders teed together: more liquid surface, more vapour.
2. **Keep the duty cylinder sheltered outdoors** (a shed or covered rack out of wind and snow).
   **Never indoors, never in a basement or living space** (→ 06-06).
3. **Swap warm cylinders:** move the sheltered spare onto the generator and put the frosted one
   back under cover to recover.
4. **Optional:** during the no-load idle at shutdown, close the cylinder valve for the last minute
   so the regulator runs dry, and switch off **before** it stalls. This adds to the manual's
   shutdown; it never replaces it.

Keep the starting battery charged and know the pull cord in gloves.

## Commissioning checklist (a generator that has sat for years)

```
[ ] READ THE MANUAL for your model. Copy its key numbers onto this page now.
[ ] OIL FIRST. Many ship dry. If old oil has sat in it for years, change it.
[ ] RODENTS. Look inside the shroud, air filter housing and exhaust for nests
    and chewed wiring.
[ ] AIR FILTER clean and present.   [ ] SPARK PLUG present, gapped, not corroded.
[ ] RUBBER: fuel lines, primer bulb, any propane hose and regulator. Cracked or
    hard = replace.
[ ] BATTERY (electric start): probably flat; plan to replace it (09-14).
[ ] DUAL-FUEL? First start on PROPANE: nothing goes stale, nothing varnishes.
[ ] FIRST RUN OUTDOORS, 20+ ft, exhaust away, CO alarms already installed.
    Then ONE load within the break-in limit until it is fully warm, not a bare idle.
[ ] Only then plug in anything you care about.
[ ] WRITE the date and run hours on a label on the machine.
```
A generator that was never fuelled usually starts fine once it has oil and a charged battery. Oil
and rodents are the two things most likely to be wrong, and both are visible in ten minutes.
Keeping it alive between uses: → 09-15.

## Taking it with you
- **A generator and its fuel travel outside the passenger cabin**: on a trailer or an external
  carrier. Fuel inside a passenger vehicle is a decision card: {{choice DC-06}} (→ 30-07). A
  propane cylinder in an enclosed cabin is a leak away from an explosive atmosphere.
- **At a destination, check what fuel exists.** A gasoline/propane generator cannot run on natural
  gas without a conversion kit, and a kit lowers its output; check the kit's figures. Until a kit is
  fitted, it runs on the fuel you brought.

## Noise and light discipline
A running generator in a dark, silent neighbourhood announces fuel, power and probably food
(→ 14-03). Run it in daytime when other noise exists, keep runs short, and break up the sound with
distance and barriers that **do not restrict airflow or trap exhaust**. Never let noise push it
toward an enclosed space: carbon monoxide kills faster than anything else here.

## Gear and items

**Have it now (buy toward this):**

| Item | Why | Notes |
|---|---|---|
| **Battery-powered carbon monoxide alarms**, every level and outside bedrooms | The real life-saver on this page | Buy before the generator; test monthly |
| Generator suited to charging batteries | Inverter type preferred | Specs by class: → 28-03 |
| Heavy outdoor extension cords (12 AWG, 50 to 100 ft) | Lets you site it 20+ ft away and still reach | Rated 20 A (Southwire); undersized cords overheat (→ 09-08) |
| Transfer switch or interlock (electrician), or cord-and-plug conversion parts | The only safe ways to run a hard-wired appliance | Decision card DC-07 (→ 30-08) |
| Propane cylinders and the generator's own hose and regulator | Fuel that does not go stale | Stored outdoors, upright (→ 06-06) |
| Stabilised gasoline in approved cans, labelled with fill date | Second fuel, shared with vehicles | → 06-06, → 09-15 |
| Spare oil of the manual's grade, air filter, spark plug | Small engines need oil on a schedule | Two changes' worth, stored with the machine |
| Open-sided cover | Rain and snow protection **without enclosing it** | Must not trap exhaust |
| Battery charger that runs from generator AC | Bulk-charging the bank is the whole point | Pair with → 09-03 |

**Scavenge or substitute:**
- **A running vehicle is a generator you already own** (→ 09-11). Same carbon monoxide rules:
  **never run an engine in an attached garage.**
- **An inverter on a car battery** runs small AC loads with no engine running (→ 09-14).
- **Fuel:** from vehicles and stored equipment (→ 06-07 for the technique and why a hose down a
  modern filler neck usually fails). Give the generator the freshest fuel you have.
- **Cords:** heavy appliance cords, welding leads.
- **What you cannot substitute: the carbon monoxide alarm.** Buy several now.

## When it runs out
- **Fuel is the whole story.** Work your runway in **hours of run time**: fuel on hand ÷ fuel per
  hour at your usual load. Write it on → 23-02. Most households find the honest answer is days to a
  few weeks.
- **Ration from day one.** Batch every run: charge the bank to full, run every big load together,
  then shut down. Never idle it for a light.
- **Shared fuel:** if the same propane also feeds a heater or a cooking stove, every hour of those
  comes out of the generator's runway (→ 06-05).
- **Resupply:** stored fuel, then fuel from vehicles, then nothing. There is **no renewable
  resupply** for a generator, which is why this section leads with solar.
- **Plan for the generator to be a memory by month two and be fine anyway.**
- **Maintenance parts are a consumable too:** a generator run hard without oil changes dies before
  the fuel does (→ 09-15).

## Phase notes
- **A (at home):** the generator's best week is the first: bulk-charging, pulling the freezer down,
  laundry, filling water containers. After that it is an occasional charging tool. Noise discipline
  starts at once.
- **B (moving):** heavy, loud, and it needs fuel you would rather put in the vehicle. It travels
  only outside the cabin, with its fuel, or it stays behind.
- **C (settled somewhere new):** the main electrical tool until solar is set up, then back to
  storm-bridge duty. Keep fuel for real emergencies.

## Cross-references
→ 08-02 carbon monoxide safety · → 06-06 fuel storage · → 06-07 moving fuel · → 08-04 the heat
ladder · → 09-03 batteries (what the generator charges) · → 09-08 wiring and cords · → 09-15
generator maintenance and no-start troubleshooting · → 09-16 outage day one · → 28-03 generators
by class · → 29-04 electricity in the house · → 30-01 the floors · → 30-08 cord-and-plug
conversion card

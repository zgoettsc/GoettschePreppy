---
id: 16-12-grid-down-house-repairs
section: 16-tools-and-repair
title: "Grid-down house repairs: gas, roof, window, burst pipe, sump"
version: 1
revised: 2026-11-16
layer: core
danger_level: critical
phase: [A, B, C]
tags: [house repair, gas leak, gas shutoff, meter, roof tarp, ladder safety, broken window, board-up, burst pipe, push-fit, frozen pipe, sump pump, ceiling leak]
derived_from: [16-12-grid-down-house-repairs]
sources:
  - fema-ready-gov-utility-shut-off-and-safety-natural-g-7965ad
  - osha-fall-protection-ladders-roofs-and-working-at-he-b15a02
  - us-army-corps-of-engineers-blue-roof-information-tem-162ca8
  - american-red-cross-fema-repairing-your-flooded-home-eafdda
  - american-red-cross-preventing-and-thawing-frozen-pip-003044
related: [16-05-basic-repairs, 16-03-knots-and-cordage, 16-07-fasteners-and-hardware, 16-11-trailer-maintenance-and-repair, 03-06-winter-water, 03-04-purifying-water, 03-05-rain-and-snow-water, 08-01-heating-one-room, 08-02-carbon-monoxide-safety, 08-03-winterizing-the-home, 00-04-family-emergency-plan, 09-04-generators, 09-08-wiring-and-safety, 17-02-tornadoes, 17-06-tornado-shelter, 17-08-power-grid-failure, 17-18-hail-and-damaging-wind, 12-02-bleeding-and-wounds, 19-01-document-grab-kit, 22-04-household-inventory, 24-01-skills-checklist, 25-10-annual-review, 30-01-the-floors, 29-04-ex04-electricity-in-the-house]
cards: []
explainers: [EX-03, EX-04]
promote_when: [has.gas_any, is.snow_region, is.cold_winters]
photo_slots:
  - { id: gas-shutoff, caption: "Our gas shutoff valve at the meter or tank, with the wrench hanging beside it" }
  - { id: water-main-shutoff, caption: "Our main water shutoff valve, and which way turns it off" }
  - { id: breaker-panel, caption: "Our breaker panel: where it is, and the main breaker" }
figures: [fig-gas-valve-on-off, fig-roof-tarp-over-ridge, fig-ladder-four-to-one, fig-push-fit-coupling]
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: null
---

# Grid-down house repairs: gas, roof, window, burst pipe, sump

**What this page is for.** The repairs that keep a house a shelter when no one can come: a gas
smell, a torn-open roof, a broken window, a burst pipe, and water rising in a basement. All are
within reach of a careful person who is not a tradesman, if the materials are already in the house.
None of the materials can be bought after the storm, because everyone else's roof is open too.

> **SAFETY. The danger is not the house. It is you.** With no emergency room, **a fall off a ladder
> is a worse outcome than any leak.** Every repair below starts with a safety gate, and the gates
> are the point of the page.
>
> **Gas comes before every repair.** If you smell gas, nothing else on this page happens until the
> gas block has been run.
>
> **Never connect a generator to house wiring except through a transfer switch, or an interlock kit
> with the main breaker off. Never backfeed through an outlet with a double-male ("suicide")
> cord.** It electrocutes line workers and neighbors and starts fires (floor, → 30-01; → 29-04).
> Run cords to single appliances instead.
>
> **Never run a generator, charcoal, or any engine indoors, in a garage, or near an open window**
> (floor, → 30-01). Carbon monoxide kills in minutes with no warning (→ 08-02).

## Do this now

1. **Find the gas shutoff and the main water shutoff.** Practice both in the dark. Photograph both
   (blocks below). Write their locations on the family plan (→ 00-04).
2. **Buy the roof kit before storm season:** two heavy tarps sized for your roof (rule below), a
   bundle of 1x2 furring strips (thin wooden strips), and a box of 2-inch exterior screws.
3. **Buy the plumbing kit:** two push-fit couplings in **each** pipe size in the house (measure now),
   a small tube cutter, and two screw-type pipe repair clamps. It fits in a shoebox.
4. **Measure plywood for the windows most likely to break** (the big ones facing your usual storm
   direction) and write the sizes where you store the plywood.
5. **Walk the house and write down what your water pipes are made of** (table under Repair 3):
   ______________________.
{{#if has.basement}}6. **You have a basement.** If it has a sump pit (a hole in the floor with a pump in it), buy a
   battery water alarm for the pit, and read Repair 4.{{/if}}

## Gas: the gate before every repair

{{#if has.gas_any}}**Your home has {{#if has.natural_gas}}natural gas{{else}}propane{{/if}} service.**
This block is for you now.{{else}}**Your home has no gas service recorded.** Read this anyway for
any house you shelter in.{{/if}} Each gas appliance (furnace, water heater, stove) has its own
small valve on the pipe feeding it. **Those are not the house shutoff.** The house shutoff is at the
meter (natural gas) or at the tank (propane).

{{figure fig-gas-valve-on-off}}

{{photo gas-shutoff}}

```
[ ] SMELL GAS (rotten eggs) or HEAR HISSING -> everyone OUT, now.
    Leave doors open behind you. No light switches, no lighters, no
    phone calls until you are outside and away from the house.
[ ] SHUT OFF AT THE METER ONLY IF IT IS SAFE: you can reach it from
    outside, you do not smell gas strongly there, and nothing is
    burning. If in doubt, stay away and keep everyone away.
    NATURAL GAS: the valve is on the pipe coming out of the ground,
    BEFORE the meter. With a 12-inch adjustable wrench or gas wrench,
    turn it ONE QUARTER TURN so the flat bar lies CROSSWISE to the
    pipe = OFF. Bar in line with the pipe = ON (FEMA, Utility
    Shut-off and Safety).
    PROPANE TANK: close the valve under the tank's dome lid, turning
    clockwise ("righty tighty").
[ ] THE WRENCH HANGS AT THE METER. That is the only place it is any
    use. Hung on: ____/____/____
[ ] DO NOT TURN IT BACK ON YOURSELF while the utility exists. Call
    from outside: gas emergency line {{ contacts.utility.gas.phone }}
    ({{ contacts.utility.gas.provider }}), or 911. Only the utility
    restores service and relights pilots (FEMA).
```

**If the utility is gone for good:** turn gas back on only after the leak is found and fixed, with
every appliance valve closed first, then relight one appliance at a time, windows open, with a
working carbon monoxide alarm in the room (→ 08-02).

A gas smell also changes where you shelter from a tornado: not in a room near the leak (→ 17-06).

## Repair 1: tarping a roof after hail or wind

**The safety gate. All five must pass, or the answer is buckets in the attic until conditions
change.**

{{figure fig-ladder-four-to-one}}

```
[ ] DRY ROOF. Never wet, never icy, never in wind. The leak can
    run another day; you cannot.
[ ] TWO PEOPLE minimum: one on the roof, one holding the ladder and
    watching. NEVER alone.
[ ] ONE STORY ONLY. Higher than one story, or a pitch you would not
    comfortably sit on: the job is off. Tarp from inside the attic
    under the hole, set buckets, wait for help. This is the honest
    limit for someone who is not a roofer (OSHA, Fall Protection).
[ ] SOUND STRUCTURE. Sagging roof deck, a gas smell (gas block
    first), or power lines down on the house = nobody goes up
    (Red Cross / FEMA).
[ ] LADDER (OSHA): base 1 foot out from the wall for every 4 feet
    of height; top at least 3 feet ABOVE the roof edge and TIED OFF;
    three points of contact always. Hands EMPTY: screws and strips go
    up in a bucket on a rope (16-03). Held by the second person,
    always.
```

**The over-the-ridge method.** This is how the US Army Corps of Engineers' temporary "Blue Roof"
crews do it: the tarp is fixed to solid wood, never held by weights (US Army Corps of Engineers,
Blue Roof Information).

{{figure fig-roof-tarp-over-ridge}}

1. **Size the tarp** so it reaches **from over the peak (ridge) and down past the damage by at least
   3 feet on every side**, and far enough down the slope that water runs off onto sound shingles,
   not under the tarp's bottom edge.
2. **Anchor on the far, undamaged side first.** Roll the tarp's top edge twice around a furring
   strip and screw through strip and tarp into the roof deck, at close, even spacing along the whole
   strip. Wind cannot get under an edge that comes over the ridge.
3. **Unroll** over the ridge and down across the damage. Pull it drum-tight. Flapping destroys a
   tarp in days.
4. **Screw furring strips down both side edges**, through the tarp into the deck, working down the
   slope. Strips run **up and down** the slope, so water that gets under an edge still runs out the
   bottom.
5. **Bottom edge:** roll it around a strip and screw it onto sound roof, or let it hang over the eave
   with the roll screwed at the sides.
6. **Never bricks, sandbags or tires alone.** The first gust turns them into missiles and the tarp
   into a sail. Weights are only for an hour while you fetch the screws.
7. **Yes, the screws make holes.** Each is under the tarp or through it into wood, and easy to seal
   later with roofing cement (→ 16-05). A peeled-off tarp is a flooded house now. Count the screws
   so you can seal every hole when the tarp comes off.

### Water coming through the ceiling

Until the roof is tarped, catch the water inside.

{{photo breaker-panel}}

1. **Electricity first.** If water is running near a ceiling light or fan, switch that circuit off
   at the breaker panel before working under it. **Never stand in water to reach a panel.** If the
   panel itself is wet, or there is water on the floor in front of it, leave it alone. The power
   stays off until someone who knows has looked (electric utility while it exists:
   {{ contacts.utility.electric.phone }}).
2. **Find the drip point.** If the ceiling is bulging with water, set a bucket under it and poke a
   small hole at the lowest point, so the water drains in one place instead of bringing the ceiling
   down.
3. **Hang a ceiling leak diverter** (a square of waterproof fabric with a drain fitting in the middle)
   or a plastic sheet under the drip, corners tied or taped up, so the middle sags lowest at the
   drain.
4. **Run a hose from the drain to a bucket, floor drain, sink or out a window**, lower than the
   diverter.
5. **Check every few hours.** Empty the bucket; check the hose. It buys time; the tarp is still the
   repair.

A leak diverter hung upside-down outdoors also works as a rain funnel into a barrel (→ 03-05). That
water is raw: treat it before drinking (→ 03-04).

## Repair 2: broken window

**Glass first:** leather gloves and eye protection before touching anything (→ 12-02). Work loose
pieces out of the frame from the top down. Sweep, then wipe the floor with a damp cloth: the tiny
pieces outlast the cleanup.{{#if has.young_child}} With a small child crawling or barefoot, wipe
twice and keep them out of the room until it is done.{{/if}}

**For now (minutes):** plastic sheeting, or a contractor bag cut open, taped to the **inside** of the
frame all the way round. Inside tape survives wind better. Good for days, not weeks. It stops
weather, not people.

**Board-up (the real fix):**
1. Measure the opening. Cut plywood (1/2 inch or thicker) slightly smaller than the opening, or cut
   it larger and screw it over the outside trim instead.
2. Screw through the plywood into the **frame** (not the moving window sash), evenly spaced all
   round, with screws 2 inches or longer. Screws, not nails, so it comes off later without wrecking
   the trim.
3. **Winter:** trapped air insulates. Plastic inside, plywood outside, and a blanket hung over the
   whole opening (→ 08-03). That room may still drop out of the warm part of the house (→ 08-01).

## Repair 3: burst pipe

**Step 0: turn off the main water shutoff, then open the lowest faucet in the house to drain the
pipes** (→ 03-06). Everything below is done on a drained line with no pressure.

{{photo water-main-shutoff}}

**What pipe do you have?**

| Look | It is | Notes |
|---|---|---|
| Dull orange-brown metal, soldered joints | **Copper** | Push-fit works |
| Cream or tan rigid plastic, printed "CPVC" | **CPVC** | Push-fit works; old CPVC is brittle, cut gently |
| Flexible tubing, often red, blue or white, printed "PEX" | **PEX** | Push-fit works; use the stiffener insert that comes with the fitting |
| Gray metal, threaded joints, a magnet sticks | **Galvanized steel** (older houses) | **Push-fit does not fit.** Cap or clamp the branch and live without it; the real repair is threaded fittings and two pipe wrenches |

**The non-plumber's repair: a push-fit coupling on a clean cut.** A push-fit coupling is a short
fitting that seals with rubber rings and grips with steel teeth. No torch, no glue.

{{figure fig-push-fit-coupling}}

1. **Cut out the split** with the tube cutter (or a hacksaw, square across), removing a short
   section centered on the damage. If the split is long, make two cuts and bridge the gap with a
   repair coupling, or a spare piece of pipe and two couplings.
2. **Smooth the cut ends** (remove the sharp lip, "deburr") and wipe clean. A scratch or burr will
   leak. **On copper, use emery cloth only if it is corroded, and lightly**: deep scratches spoil the
   seal (fitting makers' instructions).
3. **Mark the insertion depth** on the pipe (the package states it), so you can see it seated fully.
4. **Push the fitting on**, twisting slightly, until the mark meets the fitting on both sides. It
   takes real force and stops with a solid feel.
5. **Reopen the main slowly** with a dry paper towel wrapped round the joint. Any wet spot within ten
   minutes means it is not seated: release it (with the release tool) and redo it.

**The fast temporary (no cutting):** a screw-type pipe repair clamp, a rubber pad in a hinged steel
sleeve, clamped over the split. No clamp: a strip of inner-tube rubber wrapped tight over the split
and held with two hose clamps or tightly twisted wire (→ 16-05, → 16-07). Temporaries weep and fail;
they buy time for the real repair.

**Frozen pipe, one sequence** (Red Cross, Preventing and Thawing Frozen Pipes):
1. **Main water off** (→ 03-06).
2. **Open the faucet on the frozen line**, so melting ice has somewhere to go.
3. **Warm the pipe starting from the faucet end**, working back toward the frozen section, with a
   hair dryer, a heating pad, or towels soaked in hot water. **Never a torch, a fuel heater or any
   open flame.** That is how a pipe job becomes a house fire.
4. **When water flows, turn the main back on slowly and check the whole run.** A pipe that froze may
   have split without showing it (→ 08-03).

## Repair 4: water rising in a basement sump pit

{{#if has.basement}}**You have a basement.** {{/if}}In a house with a basement sump pump, the most
likely grid-down water problem is not a burst pipe: it is **the sump pump stopping when the power
does**, during snowmelt or a big storm.

1. **Power the pump another way** if you have one: a power station or generator, by cord to the
   pump only, never through house wiring (floor above; → 17-08, → 09-04). Read the pump's label for
   its running watts (→ 29-14) and check your power source can start it. **Test it now, with the pit
   dry**, so you know the cord reaches.
2. **No power, or the pump is dead:** a small 12-volt utility or bilge pump on a power station's
   12-volt port with a garden hose out a door or window; or a bucket line up the stairs. That works.
   A water-powered backup pump works only while town water pressure holds.
3. **Put a battery water alarm at the edge of the pit.** The pump fails silently; the alarm wakes
   you.
4. **Keep nothing that matters on a basement floor.** Power stations, medicine, food, chemicals,
   documents (→ 19-01) on shelves. **Pool shock (calcium hypochlorite) that gets wet gives off
   chlorine gas and can start a fire** with organic material (→ 03-04): store it high and dry.

## Gear

| Item | Why | Notes |
|---|---|---|
| **12-inch adjustable wrench or gas wrench, hung at the gas meter** | The gas gate | Useless anywhere else |
| **Heavy tarps, two, roof-sized** | Repair 1 | Heaviest weave sold |
| **Furring strips (1x2, a bundle) and 2-inch exterior screws** | The tarp anchors | Store flat with the tarps |
| Plywood, 1/2 inch or thicker | Board-up | Sizes written on it |
| Plastic sheeting and tape | Interim window | → 16-05 |
| **Push-fit couplings, two per pipe size, plus a repair coupling** | Repair 3 | Your sizes: ______ |
| **Small tube cutter** | Clean square cuts in tight spots | |
| **Pipe repair clamps, two**, inner-tube rubber, hose clamps | The temporary | |
| Push-fit release tool | Redoing a bad joint | Tape it to the fittings box |
| Ceiling leak diverter or plastic sheet and hose | Inside until the tarp is on | |
| Battery water alarm (if you have a sump) | Repair 4 | Test the battery yearly (→ 25-10) |
| 12-volt utility pump and garden hose (optional) | Repair 4 backup | |
| Leather gloves and eye protection | Glass and overhead work | One set kept with this kit |
| Ladder in good condition | The gate assumes it | |

**Substitutes:** tarps from billboards, pool covers and truck loads; plywood from fences and interior
doors; strips from pallet wood; a garden hose split lengthwise and clamped as a pipe patch. In a long
event, **capping a branch line you can live without** beats repairing it.

## When it runs out

- **Tarps die from sunlight and flapping.** A tight tarp lasts a year or more; a loose one, a month.
  Re-tighten after every wind. The second tarp is the replacement.
- **Push-fit fittings can be reused** with the release tool, and do not age.
- **Prevention is the deeper fix:** winterizing the house (→ 08-03) and draining the water system
  before a hard freeze with no heat (→ 03-06) make Repair 3 unnecessary.
- **Damage beyond tarp scale** (sagging roof, broken roof framing) is a reason to move within the
  house or leave, not to do carpentry (→ 17-02).

## By phase

- **A, at home:** buy the kits, measure pipes and windows, hang the gas wrench, and treat the first
  real tarp job as practice, with the full safety gate.
- **B, on the move:** a tarp, screws and a driver travel{{#if has.trailer}} in the trailer
  (→ 16-11){{/if}}, because the place you arrive may be damaged.
- **C, settled:** barn and outbuilding roofs make this a recurring job. **The one-story,
  two-person gate still applies to every person, every time.**

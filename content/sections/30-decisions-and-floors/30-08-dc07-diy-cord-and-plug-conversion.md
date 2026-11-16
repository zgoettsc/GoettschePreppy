---
id: 30-08-dc07-diy-cord-and-plug-conversion
section: 30-decisions-and-floors
title: "DC-07. Converting a furnace or well pump to cord-and-plug yourself"
version: 1
revised: 2026-11-16
layer: card
danger_level: critical
phase: [A]
tags: [decision card, generator, furnace, well pump, cord-and-plug, electrical work, wiring, shock, fire]
derived_from: [09-04-generators, 08-04-emergency-heat-options, 09-08-wiring-and-safety]
sources:
  - cdc-carbon-monoxide-poisoning-basics-772153
  - osha-29-cfr-1910-333-r16
  - cpsc-safety-alert-portable-generator-hazards-r8
  - osha-quickcard-portable-generator-safety
related: [09-04-generators, 08-04-emergency-heat-options, 03-10-well-water-without-power, 09-08-wiring-and-safety, 28-03-generators, 29-04-ex04-electricity-in-the-house, 30-01-the-floors]
cards: [DC-07]
explainers: [EX-04, EX-02]
promote_when: [has.generator, has.well]
card: DC-07
figures: [fig-cord-and-plug-conversion]
options:
  - id: electrician-only
    label: "Electrician only"
    summary: "The cord-and-plug conversion of the furnace or well pump is done by a licensed electrician, now, while one is available. If none did it in time, the appliance stays hard-wired."
  - id: diy-with-write-up
    label: "Do it ourselves with the write-up"
    summary: "A competent adult converts it following the kit's write-up: that circuit's breaker off and tested dead; cord and plug rated for the circuit; strain relief; ground kept; labelled; tested on the generator before it is needed."
settings_summary: "A gas furnace needs electricity for its blower and controls, and a well needs it for the pump, so neither runs in an outage even with a generator. They are wired directly into the house, with no plug. A cord-and-plug conversion gives the appliance its own plug and turns its old supply into an outlet: normally it plugs into that outlet; in an outage you unplug it and plug it into the generator's cord. Nothing reaches the house panel, so it is not backfeeding. The risk is the wiring work itself: working on a live circuit, a missing ground, a loose connection, a plug or cord too small for the load, no strain relief. Those cause shock and fire, sometimes long after the work. What helps most: a licensed electrician now (removes most of it); the circuit's breaker off and tested dead, the written steps, correct parts, a test run before winter (reduces it a lot)."
review_pass: null
---

# DC-07. Converting a furnace or well pump to cord-and-plug yourself

**What this page is for.** Many households buy a generator and then learn it cannot run the
furnace or the well pump, because those are wired straight into the house. One way to fix that
is to give the appliance its own plug. This card explains what that conversion is, why it is
normally an electrician's job, what goes wrong when it is done badly, and what the household
decides about doing it themselves.

> **SAFETY.** Never connect a generator to house wiring except through a transfer switch, or an
> interlock kit with the main breaker off. Never backfeed through an outlet with a double-male
> ("suicide") cord. Never run a generator, charcoal, or any engine indoors, in a garage, or near
> an open window. (Both are floors, → 30-01.) A cord-and-plug conversion is not a connection to
> house wiring, so it is not backfeeding; but a cord with two plug ends is never part of it.

## 1. The thing, in plain words

Read → 29-04 first if the words below are new.

- A **hard-wired** appliance has its wires connected inside a box, not a plug. Most furnaces
  and well pumps are hard-wired.
- A **cord-and-plug conversion** gives the appliance its own cord and plug (or a plug-in inlet
  on its cabinet), and ends the old house wire in an ordinary outlet next to it. Normally the
  appliance is plugged into that outlet. In an outage you **unplug it from the house outlet and
  plug it into the generator's extension cord**. Generator power goes only to that appliance;
  nothing reaches the house panel, and the main breaker can stay as it is.
- A **transfer switch** or **interlock kit** is the other way to run house circuits from a
  generator: installed at the panel, they feed chosen circuits while keeping the house and the
  grid apart. Those are covered by the floor and by the generator page (→ 09-04), not by this
  card.

{{#if has.generator}}Your generator runs about {{ gear.generator_watts }} running watts on
{{ gear.generator_fuel }}. House connection in your settings: {{ gear.house_connection }}.{{/if}}

## 2. The rule, and why it was set

- OSHA's workplace rule for working on fixed electrical equipment: the parts are de-energised,
  the circuit is locked or tagged out, and a qualified person **tests it dead** with test
  equipment before anyone treats it as safe to touch; only qualified persons may work on
  parts that are still live (OSHA, 29 CFR 1910.333).
- CPSC says connect appliances to the generator with heavy-duty outdoor extension cords rated
  above the total wattage of what is plugged in, with all three prongs, and never plug the
  generator into a wall outlet (CPSC, Safety Alert: Portable Generator Hazards). OSHA says plug
  appliances directly into the generator and never attach it to a building's wiring without a
  properly installed transfer switch (OSHA, Portable Generator Safety QuickCard).

**Why:** house wiring can electrocute. Mistakes inside a junction box (a
loose neutral, a missing ground, the wrong wire on the wrong screw, a plug or cord rated below
the circuit, no clamp to stop the cord pulling on its wires) do not show until someone touches
the cabinet or a connection overheats. The licence and the inspection exist to catch those
mistakes.

## 3. How it actually hurts people

- **While doing the work:** the wrong breaker is switched off, or a second circuit runs through
  the same box. The person touches a live wire: shock, burns, a fall from a ladder.
- **Missing ground:** the appliance's metal cabinet becomes live when a fault happens later, and
  the next person to touch it is shocked.
- **Undersized or loose parts:** a cord or plug too small for the motor, or a loose screw
  terminal, overheats behind the furnace and starts a fire, possibly months later.
- **No strain relief:** the cord is pulled each time it is unplugged, the wires loosen inside the
  box, and it arcs.
- **The shortcut that kills strangers:** someone cannot make the conversion work and grabs a
  cord with two plug ends to feed the circuit from an outlet. That is backfeeding, a floor
  (→ 30-01).
- **Running it:** the generator is moved into the garage "for a minute" because the cord is too
  short. That is the carbon monoxide floor.

{{figure fig-cord-and-plug-conversion}}

## 4. What makes it safer

**Removes most of the risk**
- **A licensed electrician does the conversion now**, while electricians, parts and inspections
  exist. Tell them the appliance's running and starting load and which generator or power
  station you own (→ 09-04, → 28-03).

**Reduces it a lot** (if you do it yourself)
- **Follow the written steps on → 09-04 exactly**, and nothing else.
- **That circuit's breaker off, taped or locked, and tested dead** at the appliance with a
  non-contact tester and a meter before any wire is touched (OSHA's lock-out-and-test rule).
- **Cord, plug and outlet rated for the circuit** (wire size and amps on the breaker), with a
  **strain-relief clamp** where the cord enters the box.
- **The ground and neutral stay connected** to the appliance through its own cord.
- **Label the plug and the outlet**, and write down what you did.
- **Test it once on the generator, outdoors, before it is needed**, watching for overload when
  the motor starts.

**Reduces it a little**
- A second competent adult checks the work before the breaker goes back on.
- Keep the old wiring diagram and photos of every connection.
- No cord with two plug ends exists in the house.

## 5. The options

**`electrician-only`: Electrician only.**
You give up: money now, and the job may not get done if you wait until after the grid is down.
You accept: that if no electrician did it in time, the furnace or pump does not run on the
generator.

**`diy-with-write-up`: Do it ourselves with the write-up.**
You give up: the electrician's training and an inspector's check. You accept: shock risk while
doing the work and shock or fire risk from any mistake afterwards, controlled by the
lock-out-and-test rule, correct parts, the written steps and a test run.

> **Before the collapse:** most places require a permit and an inspection for changes to
> permanent wiring, and rules on cord-connecting a furnace or well pump differ by area. Ask your
> local building department. Insurance may refuse a claim on unpermitted work.

## 6. Our choice

{{card DC-07}}

---
id: 30-08-dc07-diy-cord-and-plug-conversion
section: 30-decisions-and-floors
title: "DC-07. Converting a furnace or well pump to cord-and-plug yourself"
version: 1
revised: 2026-11-16
layer: card
danger_level: critical
phase: [A]
tags: [decision card, generator, furnace, well pump, cord-and-plug, transfer switch, interlock, backfeed, electrical]
derived_from: [09-04-generators, 08-04-emergency-heat-options, 09-08-wiring-and-safety]
sources:
  - us-consumer-product-safety-commission-cpsc-what-to-k-3390a4
  - osha-electrical-safety-and-health-topics-a7a68f
  - american-red-cross-power-outage-safety-6d07a8
  - cdc-carbon-monoxide-poisoning-basics-772153
related: [09-04-generators, 08-04-emergency-heat-options, 03-10-well-water-without-power, 09-08-wiring-and-safety, 28-03-generators, 29-04-ex04-electricity-in-the-house, 30-01-the-floors]
cards: [DC-07]
explainers: [EX-04, EX-02]
promote_when: [has.generator, has.well]
card: DC-07
figures: [fig-backfeed-path]
options:
  - id: electrician-only
    label: "Electrician only"
    summary: "Any change that lets a generator or power station run the furnace or well pump (transfer switch, interlock or cord-and-plug conversion) is done by a licensed electrician, now, while one is available."
  - id: diy-with-write-up
    label: "Do it ourselves with the write-up"
    summary: "A competent adult converts it following the kit's write-up: breaker off, locked and tested dead; plug and receptacle rated for the circuit; no cord with two plug ends; labelled; tested on the generator before it is needed."
settings_summary: "A gas furnace needs electricity for its blower and controls, and a well needs it for the pump, so neither works in a power outage even if you own a generator. They are wired directly into the house, with no plug. A transfer switch or interlock lets an installed generator inlet feed chosen circuits safely; a cord-and-plug conversion gives the appliance its own plug so it can be moved to a generator cord. Doing that work yourself means opening live house wiring: mistakes cause electric shock, fire, or a connection that pushes generator power back into the grid and can kill line workers. Backfeeding through an outlet is never an option (floor). What helps most: a licensed electrician now (removes most of it); breaker locked off and tested dead, the written steps, a test run before winter (reduces it a lot)."
review_pass: null
---

# DC-07. Converting a furnace or well pump to cord-and-plug yourself

**What this page is for.** Many households buy a generator and then learn it cannot run the
furnace or the well pump, because those are wired straight into the house. This card explains
the safe ways to connect them, why the work is normally done by an electrician, and what the
household decides about doing it themselves.

> **SAFETY.** Never connect a generator to house wiring without a transfer switch, interlock,
> or a cord-and-plug conversion with the main breaker locked off. Never backfeed through an
> outlet. Never run a generator, charcoal, or any engine indoors, in a garage, or near an open
> window. (Both are floors, → 30-01.) Backfeeding is not an option on this card.

## 1. The thing, in plain words

Read → 29-04 first if the words below are new.

- A **hard-wired** appliance has its wires connected inside a box, not a plug. Most furnaces
  and well pumps are hard-wired.
- A **transfer switch** is a switch next to the breaker panel that disconnects chosen circuits
  from the power company and connects them to a generator inlet. The house and the grid can
  never be connected at the same moment.
- An **interlock** is a sliding plate on the panel that makes it impossible to turn on the
  generator breaker unless the main breaker is off.
- A **cord-and-plug conversion** gives the hard-wired appliance its own plug and turns its old
  supply into a wall outlet. Normally it plugs into the wall; in an outage you unplug it and
  plug it into a cord from the generator or a power station. Nothing else in the house is fed.
- **Backfeeding** is pushing generator power into the house wiring through an outlet with a
  cord that has plugs on both ends. It is a floor, not an option.

{{#if has.generator}}Your generator runs about {{ gear.generator_watts }} running watts on
{{ gear.generator_fuel }}. House connection in your settings: {{ gear.house_connection }}.{{/if}}

## 2. The rule, and why it was set

- CPSC says never plug a generator into a wall outlet, and use a properly installed transfer
  switch to power household wiring, because backfeeding can electrocute utility workers and
  neighbours (CPSC, Portable Generator Safety). The American Red Cross says the same (Red
  Cross, Power Outage Safety).
- Electrical codes treat changes to permanent wiring as work for a qualified person, with
  inspection. OSHA's rule for anyone working on electrical equipment is to de-energise it,
  lock it off and test it dead before touching it (OSHA, Electrical Safety and Health Topics).

**Why:** house wiring at 120 or 240 volts can stop a heart. Mistakes inside a junction box (a
loose neutral, a missing ground, the wrong wire on the wrong screw, a plug rated below the
circuit) do not show until someone touches metal or a wire overheats in a wall. The
electrician's licence and the inspection exist to catch those mistakes before they hurt
someone.

## 3. How it actually hurts people

- **While doing the work:** the wrong breaker is switched off, or a second circuit runs
  through the same box. The person touches a live wire. Electric shock, burns, a fall from a
  ladder.
- **After the work:** a ground left unconnected makes the furnace cabinet live when a fault
  happens later. An undersized plug or cord overheats and starts a fire behind the furnace.
- **The shortcut that kills strangers:** someone cannot make the conversion work and grabs a
  cord with two plug ends to feed the circuit from an outlet. That backfeeds the house and the
  power line (→ 30-01, floor 2).
- **Running it:** the generator is moved into the garage "for a minute" because the cord is
  too short. That is the carbon monoxide floor.

{{figure fig-backfeed-path}}

## 4. What makes it safer

**Removes most of the risk**
- **A licensed electrician installs a transfer switch, an interlock or the cord-and-plug
  conversion now**, while electricians, parts and inspections exist. Tell them which generator
  or power station you own: some small generators cannot drive a standard house transfer
  switch, and the electrician needs to know (→ 09-04, → 28-03).

**Reduces it a lot** (if you do it yourself)
- **Follow the written steps on → 09-04 exactly**, and nothing else.
- **Breaker off, taped or locked, and tested dead** at the appliance with a non-contact tester
  and a meter before any wire is touched (OSHA's lock-off-and-test rule).
- **Plug, receptacle and cord rated for the circuit**, the appliance's own ground and neutral
  kept with its plug.
- **No cord with two plug ends exists in the house.**
- **Label the plug and the outlet**, and write down what you did.
- **Test it once on the generator, outdoors, before it is needed**, watching for overload at
  the motor's start.

**Reduces it a little**
- A second competent adult checks the work before power goes back on.
- Keep the old wiring diagram and photos of every connection.

## 5. The options

**`electrician-only`: Electrician only.**
You give up: money now, and the job may not get done if you wait until after the grid is down.
You accept: that if no electrician did it in time, the furnace or pump does not run on the
generator.

**`diy-with-write-up`: Do it ourselves with the write-up.**
You give up: the electrician's training and an inspector's check. You accept: shock and fire
risk while doing the work and from any mistake afterwards, controlled by the lock-off-and-test
rule, the written steps and a test run.

> **Before the collapse:** most places require a permit and an inspection for changes to
> permanent wiring, and rules on cord-connecting a furnace differ by area. Ask your local
> building department. Insurance may refuse a claim on unpermitted work.

## 6. Our choice

{{card DC-07}}

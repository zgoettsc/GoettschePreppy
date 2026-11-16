---
id: 29-04-ex04-electricity-in-the-house
section: 29-explainers
title: "Electricity in the house: the panel, breakers, transfer switches and backfeeding"
version: 2
revised: 2026-11-16
layer: explainer
danger_level: critical
phase: [A, C]
tags: [electricity, panel, breaker, main breaker, transfer switch, interlock, backfeed, extension cord, GFCI, generator, explainer]
derived_from: [09-04-generators, 09-08-wiring-and-safety, 09-12-ac-dc-cables-and-connectors]
sources: [osha-quickcard-portable-generator-safety, osha-electrical-safety-and-health-topics-a7a68f, us-consumer-product-safety-commission-cpsc-what-to-k-3390a4, fema-ready-gov-utility-shut-off-and-safety-natural-g-7965ad, cpsc-safety-alert-portable-generator-hazards-r8]
related: [09-04-generators, 09-08-wiring-and-safety, 09-12-ac-dc-cables-and-connectors, 09-16-outage-day-one, 28-03-generators, 29-02-ex02-batteries-and-power-stations, 30-01-the-floors, 30-08-dc07-diy-cord-and-plug-conversion]
cards: [DC-07]
explainers: [EX-02]
promote_when: [experience.new]
photo_slots:
  - { id: main-breaker, caption: "Our electrical panel with the main breaker marked" }
figures: [fig-panel-transfer-switch-interlock]
plates: []
condition: null
gear: null
explainer: EX-04
card: null
review_pass: { date: "2026-11-16", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "Floor 2 reworded to 30-01 (old wording required the main off for a cord-and-plug conversion); backfeed consequences now from the CPSC safety alert read (the OSHA card does not mention fire or generator damage); OSHA quick card transfer-switch and cord lines re-read." }
---

# Electricity in the house, explained from the beginning

**What this page is for.** In an outage you may want to shut the power off, run a generator, or
power the furnace. Each of those touches the house wiring, where mistakes kill. This page names
the parts, explains backfeeding (the mistake that kills line workers), and says what a safe
generator connection looks like.

> **SAFETY — the floor that applies (→ 30-01).** **Never connect a generator to house wiring
> except through a transfer switch, or an interlock kit with the main breaker off. Never
> backfeed through an outlet with a double-male ("suicide") cord.** Electrocutes line workers
> and neighbours; fire. A cord-and-plug conversion is not a connection to house wiring: the
> appliance is unplugged from the house outlet and plugged into the generator cord, so nothing
> reaches the panel.

## The parts

| Part | What it is |
|---|---|
| **Service** | The wires from the utility pole or underground line to your meter. They carry power **both ways**: whatever is on your side can flow out to the street |
| **Meter** | Measures what you use. Belongs to the utility |
| **Panel** (breaker box) | The metal box where the incoming power is split into **circuits**, each feeding a group of outlets, lights or one big appliance |
| **Main breaker** | The large switch at the top of the panel. Off = the whole house is cut off from the utility line. Learn where it is now (FEMA, Utility Shut-off and Safety) |
| **Breaker** | One switch per circuit. It trips (shuts off) by itself if the circuit draws too much current, which protects the wiring from overheating |
| **GFCI** | An outlet or breaker that shuts off in a fraction of a second if current leaks to ground, for example through a person. Required near water: kitchen, bathroom, outdoors |
| **Transfer switch** | A switch installed by an electrician next to the panel. It connects the chosen circuits **either** to the utility **or** to a generator inlet, never both at once |
| **Interlock** | A metal plate fitted to the panel so the main breaker and a generator breaker cannot both be on at the same time. Same job as a transfer switch, done inside the panel |
| **Inlet** | A recessed, outdoor-rated plug on the house wall that a generator cord plugs into. Used with a transfer switch or interlock |

Most US household outlets are 120 volts; large appliances such as dryers, ranges, central air
and many well pumps run on 240 volts. Your generator or power station label says which it can
supply. → 29-02, → 28-03

{{figure fig-panel-transfer-switch-interlock}}

## Backfeeding: why it kills

**Backfeeding** means pushing power from a generator into the house wiring in a way that lets it
flow out through the service to the street. The usual way people do it is a homemade cord with a
plug on both ends, pushed into a wall outlet. The power goes backward through your meter, up to
the transformer, which raises it to the high voltage of the street line, and **can electrocute a utility worker
repairing a line they believe is dead**, or a neighbour served by the same transformer. It also
bypasses some of the house's own circuit protection (CPSC, Safety Alert: Portable Generator
Hazards).

OSHA's rule: **never attach a generator directly to a building's electrical system unless it
has a properly installed transfer switch**, because of the electrocution risk to utility
workers. A cord with two plug ends is never used for anything.

## The safe ways to use a generator

1. **Extension cords to individual appliances.** Plug the appliance into a cord, the cord into
   the generator. Nothing touches the house wiring. This is always allowed.
2. **A transfer switch or interlock with an inlet**, installed by an electrician. You then power
   chosen circuits through the panel with no path to the street.
3. **A cord-and-plug conversion** of one hard-wired appliance (such as a furnace) so it can be
   unplugged from the house outlet and plugged into a generator cord. Nothing then reaches the
   panel. Whether you do this yourself or have an electrician do it is a choice:
   {{choice DC-07}} → 30-08

Generators run outdoors, at least 20 feet from the house (CPSC). → 29-03

## Extension cords

- **Gauge** is the thickness of the wire inside. **A lower gauge number means a thicker wire**
  that carries more current without overheating: 12-gauge is thicker than 16-gauge.
- Use **heavy-duty, outdoor-rated, grounded (3-prong) cords** with no damage (OSHA, Portable
  Generator Safety). The cord's tag gives its rating; it must be at least the total of what is
  plugged into it.
- **Unroll the whole cord.** A coiled cord under load heats up.
- **Never chain cords together or plug power strips into each other.**
- Do not run a cord through a door or window that then has to stay open: exhaust gets in.

## Shutting the power off

To switch off the whole house, turn the **main breaker** off (FEMA, Utility Shut-off and
Safety). Stand on a dry surface. If there is water near the panel, or you smell burning, or see
scorching, stay away and get help. Any work inside the panel, any permanent wiring, any
connection to house circuits: a qualified electrician (OSHA, Electrical).

## This household

{{#if has.generator}}Your generator connects to the house by: {{ gear.house_connection }}.
{{#if has.house_connection}}Before you ever use it, check that the transfer switch is set to
generator, or with an interlock that the main breaker is off, every single time. → 09-04{{else}}Use extension cords to
individual appliances only. → 09-04{{/if}}{{else}}No generator is listed. Extension cords from a
power station follow the same cord rules. → 09-03{{/if}}

{{photo main-breaker}}

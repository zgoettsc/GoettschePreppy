---
id: 30-29-dc28-relighting-gas-appliances
section: 30-decisions-and-floors
title: "DC-28. Relighting gas appliance pilots yourself when the gas company will not come"
version: 2
revised: 2026-11-16
layer: card
danger_level: critical
phase: [A, C]
tags: [decision card, natural gas, propane, pilot light, relighting, gas leak, water heater, furnace, carbon monoxide]
derived_from: [16-12-grid-down-house-repairs]
sources:
  - fema-ready-gov-utility-shut-off-and-safety-natural-g-7965ad
  - perc-important-propane-safety-information-2005
  - railroad-commission-of-texas-home-safe-home-propane
  - ao-smith-residential-gas-water-heater-manual-196293
  - cpsc-464-carbon-monoxide-invisible-killer
related: [16-12-grid-down-house-repairs, 08-03-winterizing-the-home, 08-02-carbon-monoxide-safety, 08-07-ducted-heater-operation, 07-05-propane-and-camp-stoves, 17-03-floods, 29-01-ex01-fuels, 29-03-ex03-carbon-monoxide, 29-14-ex14-reading-a-label, 30-01-the-floors]
cards: [DC-28]
explainers: [EX-01, EX-03, EX-14]
promote_when: [has.gas_any]
card: DC-28
options:
  - id: utility-only
    label: "Utility only: wait for the gas company or a technician"
    summary: "Once the gas is shut off or a pilot goes out, the household does not turn the gas back on or relight anything itself. It waits for the gas utility, the propane supplier or a qualified technician, however long that takes, and heats and cooks by other means meanwhile."
  - id: relight-with-rules
    label: "Relight ourselves, with rules"
    summary: "Only when no one qualified will come: every appliance valve closed before gas is restored, no gas smell anywhere (floor level too), nothing that has been under water, each appliance relit one at a time by its own lighting label, a working CO alarm, gas off at once if a smell returns."
settings_summary: "Gas appliances such as water heaters, furnaces and some stoves have a pilot: a small flame that lights the main burner. When the gas is shut off or runs out, every pilot goes out. FEMA says that once gas is turned off, only a qualified professional should turn it back on, and propane safety guidance strongly recommends that only a technician relight a pilot. The danger is gas that has leaked or pooled: propane is heavier than air and settles at the floor, and a flame or spark sets it off. A damaged appliance can also make carbon monoxide. With no gas company coming, waiting may mean no hot water, no furnace, no stove. What helps most: a technician or the utility does it (removes it); every appliance valve closed first, the appliance's own lighting label followed exactly, and a CO alarm (reduces it a lot)."
review_pass: { date: "2026-11-16", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "FEMA, PERC, Texas RRC, A. O. Smith label and CPSC 464 quotes verified; label paraphrase tightened; contact line reads right when blank." }
---

# DC-28. Relighting gas appliance pilots yourself when the gas company will not come

**What this page is for.** After the gas has been shut off at the meter or tank, or after a
propane tank runs dry, every pilot flame in the house goes out. Normally the gas company or the
propane supplier turns the gas back on, checks for leaks and relights everything. This card is
about what the household does when nobody will come.

> **SAFETY.** **If you smell gas, or hear hissing: everyone out, now.** No light switches, no
> lighters, no phone calls until you are outside and away from the house (→ 16-12). **Never light
> a pilot if you smell gas** (Railroad Commission of Texas). Never run a generator, charcoal, or
> any engine indoors, in a garage, or near an open window (floor, → 30-01).

## 1. The thing, in plain words

- **Natural gas** comes through a pipe and a meter. **Propane** comes from a tank or cylinder at
  the house (→ 29-01). Both have a smell added (it smells like rotten eggs) so you can notice a
  leak.
- A **pilot** is a small, steady flame inside an appliance that lights the main burner when heat
  is needed. Many water heaters, older furnaces, boilers and some stoves have one. Newer
  appliances may light electrically instead; the label says which.
- **Relighting** means turning the gas back on and lighting each pilot again, following the
  **lighting instructions label** on the appliance (→ 29-14). That label is usually on the
  appliance itself, near the gas control knob.
- A **leak check** is a test that the pipes and fittings hold gas without leaking before anything
  is lit.

## 2. The rule, and why it was set

- **FEMA:** "If you turn off the gas for any reason, only a qualified professional can turn it
  back on. NEVER attempt to turn the gas back on yourself." (Ready.gov, Safety Skills.)
- **Propane Education & Research Council:** "It is strongly recommended that only a QUALIFIED
  SERVICE TECHNICIAN light any pilot light that has gone out. YOU ARE TAKING THE RISK of starting
  a fire or an explosion if you light a pilot light yourself." If a tank runs out, "a leak check is
  required" in many states, by the retailer or a qualified technician, before the gas is turned on
  (Important Propane Safety Information).
- **Railroad Commission of Texas** (the state's propane regulator): "In most situations it is best
  to have a trained technician light the pilots on your appliances."
- **The appliance's own label** (example: an A. O. Smith gas water heater): "If you do not follow
  these instructions exactly, a fire or explosion may result causing property damage, personal
  injury or loss of life."

**Why:**
- If an appliance valve or a gas line is left open when the gas comes back, gas flows out into the
  room (Propane Education & Research Council).
- "Some gas is heavier than air and will settle on the floor", which is why the label says to
  smell next to the floor before lighting (A. O. Smith label). Propane is that kind of gas
  (→ 29-01).
- A gas control that has been under water, or damaged, may not shut properly and must be replaced,
  not relit (A. O. Smith label; Railroad Commission of Texas).
- A relit appliance with a hidden problem, such as a badly adjusted burner or a blocked chimney,
  can make carbon monoxide, and "only a trained service technician can detect hidden problems"
  (CPSC, The "Invisible" Killer).

## 3. How it actually hurts people

The gas comes back on. The kitchen stove's knob was bumped to "on" in the dark weeks ago, and gas
has been flowing into the room for half an hour. Someone goes to the basement to light the water
heater pilot. The gas has sunk to the floor around it. The match lights it all at once: a flash
fire or an explosion that burns the person and can take the house.

A quieter version: the furnace is relit and runs, but its flue is blocked by a bird's nest or ice.
It fills the house with carbon monoxide overnight (→ 08-02).

**The other side:** with no gas company coming, waiting may mean no hot water, no furnace and no
stove for months, in a house set up to run on gas.

## 4. What makes it safer

**Removes the risk**
- **The utility, the propane supplier or a technician does it.** While any of them exists, call
  them from outside. Gas company or supplier: {{ contacts.utility.gas.provider }}; phone:
  {{ contacts.utility.gas.phone }}.

**Reduces it a lot**
- **Close every appliance valve and set every control to "off"** before the gas is turned back on
  at the meter or tank, so nothing is left open (Propane Education & Research Council).
- **Follow the appliance's own lighting label exactly**, word for word, one appliance at a time.
  The A. O. Smith water heater label, for example: the tank must be **full of water** first;
  smell all around the appliance and **next to the floor** before lighting; turn the control to
  "OFF"; **wait five minutes** to clear any gas
  and smell again; if you smell gas, stop; turn the knob **by hand only, never with tools**; if
  the pilot will not stay lit, turn it off and call a technician. Other makers' labels give other
  times; use the one on your appliance.
- **Never relight an appliance that has been under water** (A. O. Smith label; → 17-03).
- **A working carbon monoxide alarm** on every level (Propane Education & Research Council) and
  near sleeping areas (CPSC), and watch for
  the signs CPSC lists of an appliance running badly: soot on the appliance or vent, an unfamiliar
  or burning smell, moisture on the inside of windows.

**Reduces it a little**
- A second person standing outside, ready to shut the gas off at the meter or tank.
- Daylight, so you are not using a flame to see.

## 5. The options

**`utility-only`: Utility only: wait for the gas company or a technician.**
You give up: hot water, furnace heat and gas cooking until someone qualified comes, which may be
never. You accept: heating and cooking by other means (→ 08-04) for as long as that takes.

**`relight-with-rules`: Relight ourselves, with rules.**
You give up: the professional leak check and inspection that the published guidance requires.
You accept: the fire, explosion and carbon monoxide risk described above, and that every rule in
the summary is followed every time, starting with no gas smell and every valve closed.

## 6. Our choice

{{card DC-28}}

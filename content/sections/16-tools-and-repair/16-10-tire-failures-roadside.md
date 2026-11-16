---
id: 16-10-tire-failures-roadside
section: 16-tools-and-repair
title: "Tire failures: roadside diagnosis and repair"
version: 1
revised: 2026-11-16
layer: core
danger_level: caution
phase: [A, B, C]
tags: [tires, flat tire, plug kit, tire sealant, inflator, jack, lug wrench, spare tire, blowout, valve core, roadside, winter, vehicle kit]
derived_from: [16-10-tire-failures-roadside]
sources:
  - nhtsa-us-department-of-transportation-tirewise-tire-ebb0d0
  - american-red-cross-winter-storm-preparedness-and-bli-4bb6c0
  - cdc-carbon-monoxide-poisoning-basics-772153
related: [22-05-kit-vehicle, 16-11-trailer-maintenance-and-repair, 16-09-bicycle-and-transport, 16-03-knots-and-cordage, 17-01-blizzards-and-ice, 08-02-carbon-monoxide-safety, 01-03-phase-b-movement, 23-04-resource-lifecycles, 26-08-expiry-and-rotation-tracker, 26-09-shopping-list-and-budget, 18-01-mutual-aid, 29-14-ex14-reading-a-label]
cards: []
explainers: [EX-03, EX-14]
promote_when: [has.vehicle]
photo_slots:
  - { id: jacking-points, caption: "Our vehicle's jacking points, marked with paint pen, from the owner's manual" }
  - { id: tire-kit, caption: "Our tire kit laid out: plug kit, inflator, sealant, jack, lug wrench, spare" }
figures: [fig-tire-plug-steps, fig-lug-star-pattern, fig-tread-vs-sidewall]
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: null
---

# Tire failures: roadside diagnosis and repair

**What this page is for.** What to do when a tyre goes soft, punctures, or fails on the road, with
a small kit you carry in the vehicle: a plug kit, a portable inflator, sealant, a jack, a lug wrench
and, ideally, a spare. Many newer vehicles carry no spare at all, only a sealant kit; for those,
this page is the replacement. In a long emergency there is no tyre shop and no tow truck, so these
repairs are how the vehicle keeps moving.

> **CAUTION. Three ways to get hurt at the roadside.**
> - **Traffic.** Get as far off the road as possible. A ruined rim is cheaper than a person.
> - **The jack.** **Everyone out of the vehicle before it is jacked up.** A person shifting in a
>   seat is the movement that rocks a jack over onto the hands of the person working. Never put
>   any part of your body under a vehicle held only by a jack.
> - **Carbon monoxide.** If the engine runs for heat while you wait, **the exhaust pipe must be
>   clear of snow** and a window cracked. A blocked tailpipe fills the cabin with carbon monoxide
>   (→ 08-02, → 29-03).
>
> **Your products' own instructions govern** where they differ from this page. Keep a copy of
> this page, and those instructions, in the kit.

**Your vehicles:**
{{#if has.vehicle}}{{#each vehicles as v}}- {{v.type_text}} ({{v.fuel_text}}; four-wheel drive: {{v.four_wheel_drive}}; can tow: {{v.can_tow}}). Spare tyre aboard: yes / no / compact only. Tyre size (from the sidewall): __________. Pressure from the door-jamb placard: front ____ rear ____. Lug nut torque from the manual: ____.
{{/each}}{{else}}None entered. Keep this page for any vehicle you ride in or borrow.{{/if}}

{{#if has.trailer}}**Trailer:** every procedure here works the same on your trailer's tyres, with
the same kit, **except** the pressure (a trailer uses the maximum pressure moulded on its own tyre
sidewall, not a door placard) and the trailer's own spare. That, plus wheel bearings and lights, is
→ 16-11.{{/if}}

## Do this now

1. **Find out whether each vehicle has a spare**, and what kind: full-size, compact ("donut"), or
   none. Write it above. If none, put a used full-size wheel and tyre for that vehicle on the
   shopping list (→ 26-09).
2. **Build the kit** in the table at the bottom (→ 22-05).
3. **Practise a plug once on a scrap tyre.** The insertion tool takes real force the first time,
   and the first time should not be on a freezing roadside.
4. **Do one driveway jack-and-swap.** Find the jacking points in the owner's manual and mark them
   with a paint pen. Add the photo:

{{photo jacking-points}}

5. **Charge the inflator** and put it on your regular charging rotation. Its 12-volt cord is the
   backup.
6. **Keep sealant bottles in the cabin**, not a cold cargo area. Sealant pours badly when cold.
7. **Check tyre pressures monthly and before any long trip**, cold, against the door-jamb placard
   (NHTSA, TireWise). Many roadside "flats" began as weeks of slow under-inflation.

{{photo tire-kit}}

## Step 0: every case starts the same way

```
[ ] OFF THE ROAD as far as possible. Flat, firm ground. Hazard
    lights ON. In winter, the stranded-vehicle rules (17-01) apply
    in full.
[ ] For plugging, sealing and inflating: children stay buckled in
    the vehicle. One adult works, one adult watches traffic and
    children. Work on the side away from traffic when you can.
    JACKING is different: everyone OUT first (Case 4).
[ ] Engine may run for heat ONLY with the exhaust pipe clear of
    snow and a window cracked (08-02).
[ ] LOOK BEFORE YOU TOUCH: what failed, and can you see why?
```

## Diagnose it

{{figure fig-tread-vs-sidewall}}

The **tread** is the thick part that touches the road. The **sidewall** is the thin, smooth side
with the writing on it. The **shoulder** is the curved edge between them.

| What you see | It is | Go to |
|---|---|---|
| Tyre soft or low, warning light, no visible damage | Slow leak | Case 1 |
| Nail or screw head in the **tread** | Puncture | Case 2 |
| Hissing you cannot find; a hole too ragged for a plug; or no time or too dangerous to plug | Sealant case | Case 3 |
| Cut or bulge in the **sidewall**, tread peeling, tyre shredded | Dead tyre | Case 4 |
| Loud bang and a pull while driving | Blowout | Case 5 first, then 4 |

## Case 1: slow leak or low tyre

1. **Inflate to the placard pressure** with the inflator. Check with a simple pencil gauge too;
   digital gauges are sometimes wrong.
2. **Find the leak:** sponge soapy water (a little soap in any bottle of water) over the tread, the
   valve and the edge where tyre meets rim. Bubbles mark it. No soap: listen, and feel with a wet
   finger.
3. **Bubbles at the valve:** use the valve-core tool (a small key, often in plug kits) to tighten the
   valve core a quarter turn. Still bubbling? Swap in a spare core (the tyre deflates; reinflate
   after). A 30-second fix few people know.
4. **Bubbles on the tread:** that is a puncture. Go to Case 2.
5. **Bubbles at the rim edge, or nothing found but it keeps dropping:** reinflate and drive on,
   checking about every 30 minutes. Rim leaks are shop work, or Case 3 if it will not hold.

## Case 2: puncture in the tread (the plug kit)

{{figure fig-tire-plug-steps}}

**Plugs are for the tread only. Never the sidewall, never the shoulder.**

```
1. Mark the spot, then PULL THE OBJECT out with pliers.
2. REAM: push the spiral reamer in and out several times for a
   clean, round hole. (A little of the kit's lubricant on the tools
   helps.)
3. THREAD a plug through the eye of the insertion needle, centred.
   A touch of lubricant or cement on the plug.
4. INSERT straight in with steady force until about 1/3 of the plug
   is still outside. This takes muscle; brace yourself and the tyre.
5. PULL STRAIGHT OUT quickly. The plug stays; the needle releases.
6. TRIM the plug flush with a knife.
7. REINFLATE to the placard pressure. Check the repair with soapy
   water.
8. Drive. Recheck pressure after 10 minutes, then at each stop.
```

A well-set plug often lasts the life of the tyre, but by the tyre industry's own standard it is a
temporary repair. In normal times, have a shop fit a patch from the inside soon. **Plugs are the
most renewable tyre resource you can carry:** a kit holds many, and each one fixes a puncture.
Prefer a plug to sealant whenever you can.

## Case 3: sealant

**When:** the hole is too ragged for a plug, there are several small punctures, you cannot find the
leak but must move, or plugging is unsafe (traffic, cold, dark).

```
1. Roll the vehicle so the VALVE IS AT THE TOP.
2. REMOVE THE VALVE CORE with the core tool. (The tyre deflates
   fully. That is expected.)
3. SQUEEZE IN the amount the bottle's label gives for your tyre size.
4. REFIT THE CORE, snug.
5. REINFLATE to the placard pressure.
6. DRIVE AT ONCE, a few miles at moderate speed, to spread the
   sealant. Recheck pressure after 10 minutes; top up.
```

(Some sealant kits pump in through the valve without removing the core. Follow the label.)

**What it costs you:** it is temporary; it gums up the rim and the tyre-pressure sensor; and the tyre
will need a real repair or replacement. **Each bottle fixes one tyre, once.** In a long emergency,
sealant is the scarce resource and plugs are the plentiful one, so sealant is the reserve, not the
default.

## Case 4: dead tyre (sidewall cut, bulge, shredded)

**Nothing in a bottle or a plug fixes a sidewall. Ever.** Sidewall damage means the tyre is
replaced (NHTSA, TireWise).

**With a spare aboard:**

{{figure fig-lug-star-pattern}}

```
1. EVERYONE OUT before the jack goes under. Children with the second
   adult, well off the road, never between the vehicle and traffic.
   If there is NO safe place to stand (whiteout, deep cold, no
   shoulder), that is the signal to plug or seal instead, or to wait
   for help (17-01). CHOCK the wheel diagonally opposite (a rock or
   block in front of and behind it). Parking brake ON. Shift to park
   (or first gear).
2. LOOSEN each lug nut half a turn WHILE THE WHEEL IS STILL ON THE
   GROUND. Counter-clockwise ("lefty loosey").
3. JACK at the marked jacking point until the tyre just clears the
   ground.
4. Lug nuts off, wheel off, SPARE ON. Lug nuts back on, hand-tight,
   in a STAR pattern (across, not round the circle).
5. LOWER the vehicle, then tighten firmly in the star pattern.
6. Tighten to the torque in your owner's manual at the first chance
   (auto parts stores often lend torque wrenches). Recheck the lug
   nuts after about 50 miles regardless.
```

- **A compact spare** has a speed and distance limit printed on it. Respect it.
{{#if has.4wd}}- **Your household has a four-wheel-drive vehicle.** Read its manual about spares and
  tyre replacement: many four-wheel and all-wheel-drive vehicles need all four tyres closely matched
  in size and wear, and a compact spare may require the vehicle to stay in two-wheel drive or stay
  slow until the tyre is replaced. Four-wheel drive does not help you drive on a flat.
{{/if}}- **Without a spare:** this is a stranding, not a repair. In normal times, call roadside help
  or a tow. With no help coming, drive on the flat **at walking speed, on flat ground, only if
  staying where you are is dangerous**. You will ruin the rim; a ruined rim is better than a family
  stranded in danger.
- **This case is why a spare wheel belongs on the shopping list** (→ 26-09).

## Case 5: blowout at speed

```
GRIP the wheel firmly. DO NOT BRAKE HARD. Ease OFF the accelerator,
hold the car straight, let the speed bleed off, signal, and roll
gently onto the shoulder. Then Case 4.
```

Braking hard or swerving with a blown front tyre is how a blowout becomes a rollover. Say this
sequence out loud once a year so it becomes reflex.

## Winter

- **The stranded-vehicle rules** (→ 17-01) run alongside the whole time: be visible, stay warm,
  keep the exhaust clear, watch the children.
- **Work in short bursts.** Bare fingers lose their skill within minutes in deep cold; warm your
  hands inside between steps. The plug job gets twice as hard. Sealant kept warm in the cabin may
  beat a plug in a whiteout, even for a pluggable hole. That is a reasonable call.
- **Cold lowers tyre pressure** by roughly 1 psi for every 10 °F drop (NHTSA, TireWise). A "low"
  tyre on a bitter morning may just be the cold; check against the placard before assuming a leak.

## Gear

| Item | Covers | Where it lives |
|---|---|---|
| **Tyre plug kit** (plugs, insertion tool, reamer, pliers, knife, pencil gauge, valve-core tool, spare valve cores) | Cases 1 and 2 | Vehicle, with this page in the lid |
| **Portable inflator** (battery and 12-volt cord) | Every case ends with "reinflate" | Vehicle; on the charging rotation |
| **Tyre sealant**, one bottle per tyre you want to cover | Case 3 | **Cabin**; date on each bottle |
| **Jack** rated for your vehicle, and its handle | Case 4 | Vehicle |
| **Long-handled lug wrench** in your lug-nut size | Case 4 | With the jack |
| Wheel chocks (or two solid blocks) | Case 4 | With the jack |
| **Spare wheel and tyre**, full-size if possible | Turns Case 4 from a stranding into a delay | Vehicle, for every trip beyond town |
| Work gloves, headlamp, reflective triangles | Every case | Vehicle |
| Factory sealant kit, if the vehicle came with one | A backup bottle; check its expiry | Where the maker put it |

**Substitutes:** any air source beats none: a gas-station hose, or a bicycle floor pump (→ 16-09),
slow but real. Plug strings and rubber cement are sold in any auto aisle and worth grabbing.

## When it runs out

- **Plugs:** the renewable workhorse. Restock while stores exist.
- **Sealant:** one use each, and it ages. Write the purchase date on each bottle and check the
  label's shelf life at the rotation check (→ 26-08).
- **Valve cores:** cheap by the card. Keep spares.
- **Tyres themselves:** in a long emergency, nobody can make them. Gentle driving, correct pressure
  (NHTSA, TireWise) and moving the least-worn tyres to where they matter most are the plan
  (→ 23-04).

## By phase

- **A, at home:** flats are an errand. Plug, then have a shop fix it properly. Keep the kit stocked.
  Practise now.
- **B, on the move:** the kit, a charged inflator, warm sealant and a spare ride along (→ 01-03). A
  flat is a 20-minute delay if, and only if, you practised.
- **C, settled:** gravel and field work eat tyres. A plug kit becomes something the whole community
  uses (→ 18-01). Save sealant for true emergencies.

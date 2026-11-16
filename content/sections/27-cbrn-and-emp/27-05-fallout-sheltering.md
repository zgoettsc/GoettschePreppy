---
id: 27-05-fallout-sheltering
section: 27-cbrn-and-emp
title: "Fallout: sheltering, time and decontamination"
version: 1
revised: 2026-11-16
layer: core
danger_level: critical
phase: [A, B]
tags: [fallout, shelter, protection factor, decontamination, radiation, decay, children, pets, water]
derived_from: [27-05-fallout-sheltering]
sources:
  - us-department-of-health-and-human-services-remm-nucl-652eb0
  - cdc-radiation-emergencies-62e24d
  - us-epa-radiation-protection-25aa78
  - us-epa-emergency-disinfection-of-drinking-water-6aa91f
  - ready-gov-fema-nuclear-explosion-dac8c3
  - cdc-pets-and-radiation-emergencies-ed2146
  - fema-planning-guidance-nuclear-detonation-2022
related: [27-04-nuclear-first-hour, 27-06-potassium-iodide, 27-07-chemical-and-biological, 08-01-heating-one-room, 03-02-storing-water, 03-04-purifying-water, 13-01-human-waste-no-plumbing, 20-08-kids-and-fear, 21-04-routine-and-structure, 22-06-kit-medical, 15-01-weather-alerts, 17-06-tornado-shelter, 30-01-the-floors, 30-02-dc01-unvented-heater-overnight, 30-03-dc02-propane-cylinder-indoors]
cards: [DC-01, DC-02, DC-22]
explainers: [EX-03, EX-06]
promote_when: []
photo_slots:
  - { id: fallout-shelter-spot, caption: "Our fallout shelter spot, and where the mass gets stacked" }
  - { id: decon-boundary, caption: "Our decontamination line: where outer clothes come off and where the bag goes" }
figures: [fig-shelter-by-dwelling, fig-fallout-decay-7-10]
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: null
---

# Fallout: sheltering, time and decontamination

**What this page is for.** How to shelter for the 24 to 48 hours after a nuclear explosion: where
in your home, how to add protection with what you own, how to get contamination off people and
pets, what to eat and drink, and when to come out. The first hour is → 27-04.

> **SAFETY.** The fact that makes sheltering work: **fallout fades fast.** HHS REMM: the level
> *"decays quickly, roughly by a factor of 10 for every 7-fold increase in time."* **Time inside
> is the most protective thing you can do, and the first day buys the most.** Stay inside at
> least 24 hours unless officials say otherwise (Ready.gov, Nuclear Explosion). **Never run a
> generator, charcoal, or any engine indoors, in a garage, or near an open window.** **Bleach or
> pool shock is never mixed with ammonia, acids or other cleaners.**

## Do this now (before anything happens)

1. **Choose the shelter spot** using the guide below, write it down, and photograph it. It may not
   be your tornado spot: a tornado spot is for twenty minutes; a fallout spot is for a day or two
   and needs room for water, a toilet, bedding and heat or cooling (→ 17-06).
2. **Keep stored, covered water near it** (→ 03-02). **Boiling and chemical disinfection do
   nothing to radioactive material** (→ 03-04). Covered water stored before the event{{#if has.water_heater_tank}}, then the
   water heater ({{ dwelling.water_heater_gallons }} gal){{/if}} and the water in the pipes, is the answer
   (CDC, Radiation Emergencies), not treatment.
3. **Put a bucket toilet and cover material there** (→ 13-01). Two days with
   {{ household.size }} people and no plan for waste is its own emergency.
4. {{#if has.child}}**Put something there for the children** (→ 20-08).{{else}}**Put something there to pass the time**: cards, books (→ 21-02).{{/if}}

## The decay rule, and why it decides everything

{{figure fig-fallout-decay-7-10}}

Because fallout fades **about tenfold for every sevenfold increase in time** (HHS REMM):

| Time after the explosion | Roughly |
|---|---|
| **1 hour** | The starting level |
| **7 hours** | About **1/10** of it |
| **2 days (49 hours)** | About **1/100** |
| **2 weeks** | About **1/1,000** |

**What it means:** going outside at hour 1 versus hour 24 is an enormous difference. Day 3 versus
day 4 is small. **That is why the advice is "at least 24 hours" and why the first day is not up
for debate.**

**It is also why the plan is achievable.** Nobody is asking you to live underground for months.
You are being asked to stay put for a day or two with supplies you should have anyway.

## The three protections, in order

1. **Time**: every hour inside counts, and the early ones count most.
2. **Distance**: from the fallout itself, which settles on the roof, the ground and the outside
   walls. Go to the middle of the building and below ground level.
3. **Shielding (mass)**: put heavy material between you and the outside. Earth is best;
   concrete, brick, water and books all work.

**Shelters are measured by protection factor.** A protection factor of 10 means a person inside
gets one-tenth of the dose they would get outside; higher is better (FEMA, Planning Guidance for
Response to a Nuclear Detonation). Below ground, and the centre of large brick or concrete
buildings, score far higher than the ground floor of a small wood-frame house.

## The best shelter for your home

{{figure fig-shelter-by-dwelling}}

Your home: {{ dwelling.type }}{{#if has.basement}}, basement: {{ dwelling.basement }}{{/if}}.

{{#if has.basement}}**You have a basement: use it.** Pick the corner most below ground, farthest from windows, window
wells and outside doors. Stack mass against any window well and, if there is living space above,
consider a sturdy table with heavy things on it to sit under.
{{#if has.walkout}}**Your basement is a walkout.** One side is at ground level with glass or a door, so that side
gives little protection. Shelter on the buried side or in the buried corner, and **stack mass
across the walkout glass and door**: it is the room's weak side. If the walkout area is where you
keep warm in winter, the trade is real: the buried corner shields better, the warm side is
heatable. Stack the mass and decide which matters more for your household this night.
{{/if}}{{/if}}{{#if has.shelter_room}}**Your named room**: {{ dwelling.shelter_room }}. An interior room with no outside walls, on the lowest
floor, is a reasonable shelter in a house without a basement. Stack mass on any wall that faces
outside and keep away from the ceiling under the roof if it is a one-storey house.
{{/if}}{{#if has.apartment}}**Apartment.** In a large building, the best places are **below ground** (a basement, an underground
garage) or **the centre of the middle floors**, away from the roof and the outside walls. The top
floor and the ground floor near glass are poor. If your own unit is on the top floor or has
mostly outside walls, a central stairwell or an interior corridor on a middle floor is often
better: agree it with neighbours now. Never use the lifts.
{{/if}}{{#if has.mobile_home}}**Mobile or manufactured home.** It gives very little protection. **The plan is to reach a sturdy
building within minutes**, before fallout arrives (→ 27-04): a school, church, store or a
neighbour's basement that you have agreed in advance. If you cannot reach one in time, go to the
centre of the home, the lowest point, and pile everything heavy you own around you, then move to a
sturdy building only when officials say it is safe.
{{/if}}{{#if !has.basement}}{{#if !has.apartment}}{{#if !has.mobile_home}}**No basement.** Use the most central room on the ground floor, with the fewest outside walls and
windows: often a bathroom, closet or hallway. Stack mass on every side that faces outside.
{{/if}}{{/if}}{{/if}}
Our spot: ______________. Second choice: ______________.

{{photo fallout-shelter-spot}}

### Building shielding from what you have

Stack mass between you and the outside, especially across windows, glass doors and window wells,
and overhead if there is living space or roof above:
- **Water containers**: filled, they are heavy and you need them anyway.
- **Books, full boxes, bags of soil or sand, bins of canned food.**
- **Furniture, mattresses, appliances** against window wells and glass.
- **Earth**, if you can bank it against a window well from inside.

**A smaller, denser space beats a large comfortable one.** You are trading room for mass, and for
a day or two it is the right trade.

## Heat and air in the shelter

- **A furnace that only recirculates indoor air may run if it has power.** Ready.gov's instruction
  is to turn off fans and units that **bring air in from outside** (Ready.gov, Nuclear Explosion).
- **With no furnace, heat the shelter the way you heat one room in any outage** (→ 08-01), with a
  carbon monoxide alarm working where people sleep. **Keep the heater's fresh-air openings open**,
  even here: a closed, heated room without them is a carbon monoxide risk that is immediate, while
  fallout through a cracked window is small and fading. Overnight: {{choice DC-01}} → 30-02. A
  propane cylinder over 1 lb indoors: {{choice DC-02}} → 30-03
{{#if is.hot_summers}}- **In summer heat**, a closed room gets dangerously hot. Water, wet cloths and rest; watch the
  young and old for heat illness (→ 11-08). Short, early-morning ventilation is a trade-off to make
  only after the first 24 hours, or when officials say so.
{{/if}}

## Decontamination: simple and effective

Most outside contamination is dust on the outside of you. Removing it is straightforward (HHS
REMM; CDC, Radiation Emergencies).

```
[ ] TAKE OFF OUTER CLOTHING before entering the shelter space. Peel it away
    from the face. CDC: removing your outer layer of clothing can remove up to
    90% of radioactive material. This one step is most of it.
[ ] BAG IT and put it outside the living space, well away from people.
[ ] WASH exposed skin and hair with soap and lukewarm water, gently.
    Do NOT scrub skin raw: broken skin lets contamination in.
    Do NOT use hair conditioner: it binds contamination to hair.
[ ] Blow your nose; wipe eyelids and ears with a clean damp cloth.
[ ] Put on clean clothing that was stored inside.
[ ] Wipe down pets that were outside before they come into the shelter space.
```

**Do it at the edge of the shelter space**, so contamination stays on one side of a line everyone
understands. Bagged clothing and gear go **outside the living space**: an outbuilding, a closed
garage, a trailer or a bin outside, away from doors and people.

{{photo decon-boundary}}

{{#if has.child}}**Decontaminating children: the order and the details matter.**
```
[ ] ADULT HANDS FIRST. Clean your own hands (and face if exposed) before you
    touch a child. Dirty hands put contamination back on everything.
[ ] CUT, DON'T PULL. Cut contaminated clothing off rather than pulling it
    over the head: pulling drags the dirty layer across mouth, nose and eyes.
    Keep blunt-tipped trauma shears in the medical kit (22-06).
[ ] EYES AND NOSE: wipe OUTWARD, from the inner corner of the eye out, from
    the nose out and down, with a clean damp part of the cloth for each wipe.
    Never wipe toward the eyes or mouth.
[ ] KEEP THEM WARM. Small children chill fast. Use warm water, wash gently
    and quickly, dry at once, dress in clothes stored inside (11-02).
[ ] TALK THE WHOLE WAY. Say what is happening in plain words, keep your voice
    level, and give an older child a job ("you hold the towel"). A drill
    voice, not an emergency voice (20-08).
```
{{#if has.infant}}**For a baby, warmth outranks speed.** A baby washed in a cold room can get dangerously cold faster
than outside contamination can plausibly hurt them. Warm the water first.
{{/if}}{{/if}}

{{#if has.pets}}**Pets** (CDC, Pets and Radiation Emergencies):
```
[ ] BRING PETS IN and CONFINE them (crate or small room) as soon as you can.
    An animal that grooms a contaminated coat swallows the contamination.
[ ] GLOVES ON. Gently wash or brush the coat out; with cats, wiping
    head-to-tail with damp cloths in or beside the crate is what two people
    can actually do. Change cloths often; bag used cloths with the clothing.
[ ] PAWS: do them thoroughly. Paws carry contamination into bedding and
    litter. Treat the first litter change as contaminated waste: bag it
    with the clothing.
[ ] Pets then stay inside the shelter space with you. Nobody goes outside
    to chase a pet that bolts: it is crated and wiped when it comes back.
```
{{/if}}

## Food and water in the shelter

- **Water: use stored, covered water** (→ 03-02). Anything sealed from before the event is fine;
  the water heater and the pipes hold pre-event water too (CDC). **Boiling and chlorine do nothing
  to radioactive material; a filter removes fallout particles but not what is dissolved**
  (EPA, Radiation Protection; → 03-04). Treating water is a last resort for settled, filtered
  water once stored water is gone, not a plan.
- **Food: sealed, packaged food is fine.** The packaging is what matters. Wipe the outside of a
  container before opening it.
- **Do not eat from the garden, collect rainwater or use open water** (→ 03-05) until officials
  say it is safe.
- **Local milk and fresh produce** are the usual way contamination enters the food chain;
  official advisories will cover them.

## 48 hours in one space: the list

This is the part nobody plans and everybody struggles with. It is a logistics and morale problem,
not a physics one.

```
[ ] WATER for {{ household.size }} people for 48 hours: at least 2 days at your
    planning figure of {{ derived.water.plan_gal_day }} gal a day (03-01)
[ ] MEDICAL KIT: every medicine, epinephrine, device and charger      (22-06)
[ ] Bucket toilet, liners, cover material, hand sanitiser             (13-01)
[ ] Food that needs no cooking, for everyone                          (04-01)
[ ] Bedding, and something each person will actually sleep on       (21-07)
[ ] LIGHT: headlamps and spare batteries; a lantern for the space     (10-01)
[ ] Battery radio and spare batteries: your only instruction channel (15-01)
[ ] Warm layers; the heat plan and its CO alarm                       (08-01)
[ ] Cards, books, paper, pencils                                       (21-06)
[ ] This binder, charged                                               (00-10)
```
{{#if has.infant}}- [ ] Diapers, wipes, a changing surface (→ 20-06), and the baby's feeding plan: nursing parent's
  extra water and food, or formula with **sealed bottled water** (→ 20-05, → 02-13).
{{/if}}{{#if has.young_child}}- [ ] Each young child's comfort item, and a few new small activities saved for this (→ 20-08).
{{/if}}{{#if has.food_allergy}}- [ ] Allergy-safe food, sealed and labelled (→ 02-04).
{{/if}}{{#if has.pets}}- [ ] Pet carriers, litter or waste bags, pet food and water (→ 20-09).
{{/if}}{{#if has.elder}}- [ ] For older members: medicines, glasses, hearing aids and batteries, a chair they can get up from,
  and a plan for the toilet (→ 02-21).
{{/if}}{{#if has.oxygen}}- [ ] Oxygen cylinders and the regulator (→ 02-08).
{{/if}}{{#if has.cpap}}- [ ] CPAP and its battery (→ 02-24).
{{/if}}{{#if has.refrigerated_meds}}- [ ] The medicine cooler and its thermometer (→ 29-07).
{{/if}}

> **Keep the routine.** Meals at meal times, sleep at bedtime{{#if has.child}}, a job for each
> child{{/if}}. It is the most effective thing you can do for people in a small space (→ 21-04,
> → 20-08).

## When can you come out?

**When officials say so.** That is the honest answer, and why the radio is on the list.

With no instruction at all:
- **Do not go out in the first 24 hours** if you can possibly avoid it (Ready.gov).
- **Brief, essential trips only** after that, and brief means minutes.
- **Every trip outside ends with the decontamination routine above.**
- **The longer you wait, the better**: the improvement is steep early and shallow later.

**A home radiation meter** is optional and mostly not useful: a meaningful one is expensive,
needs calibration, and needs interpretation you will not have. **The radio and the clock are the
instruments this plan runs on.**

Potassium iodide is a separate question, only on official direction (→ 27-06). Adults over 40:
{{choice DC-22}} → 30-23

## What you need

Everything on the 48-hour list, and **almost all of it is already in this binder for other
reasons**: stocking one warm room for a winter outage (→ 08-01) stocks it for this. The only
additions worth making are **pre-cut plastic sheeting and tape** for sealing a room (→ 27-07) and
a **second radio**.

No money? Mass from anything heavy; a bucket and bags for the toilet; blankets for warmth; the
water you already store. **There is no substitute for having stored water before the event**:
it is the thing this scenario forgives least.

## When it runs out

- **Runway:** stock the shelter for **48 hours**, and the aftermath for as long as → 23-02 says.
- **Ration:** never ration drinking water or children's food (→ 23-01). Ration light and
  battery.
- **Resupply:** only when officials say moving is safe.
- **Substitute:** after the acute phase this becomes an ordinary long outage (→ 01-01), with the
  whole binder behind it.

## By phase

- **A, at home:** this **is** sheltering at home, squeezed into one space for two days.
- **B, moving:** do not move during the acute phase (→ 27-04). Afterwards, → 01-02 applies
  as normal.
- **C, establishing:** a basement with earth around it shelters better than most above-ground
  construction: a small point in a site's favour, well below water and timber (→ 01-05).

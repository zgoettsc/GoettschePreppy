---
id: 25-08-quick-reference-cards
section: 25-reference-and-appendices
title: "Quick-reference cards"
version: 2
revised: 2026-11-16
layer: core
danger_level: critical
phase: [A, B, C]
tags: [quick reference, cards, emergency numbers, anaphylaxis, diabetes, carbon monoxide, bleeding, tornado, CPR, choking, heaters]
derived_from: [25-08-quick-reference-cards]
sources:
  - cdc-recognizing-and-responding-to-anaphylaxis-645825
  - american-academy-of-allergy-asthma-and-immunology-aa-7f3939
  - cdc-diabetic-ketoacidosis-55a7c2
  - cdc-low-blood-sugar-hypoglycemia
  - us-fda-information-regarding-insulin-storage-and-swi-6448d3
  - us-epa-emergency-disinfection-of-drinking-water-6aa91f
  - cdc-how-to-create-and-store-an-emergency-water-suppl-f0c412
  - cdc-carbon-monoxide-poisoning-basics-772153
  - american-college-of-surgeons-stop-the-bleed-stop-the-8d1b5b
  - noaa-national-weather-service-tornado-safety-ba75e0
  - noaa-storm-prediction-center-tornado-safety-faq-vehi-aba867
  - foodsafety-gov-usda-hhs-food-safety-during-a-power-o-3894c1
  - medlineplus-us-national-library-of-medicine-nih-chok-70112e
  - medlineplus-us-national-library-of-medicine-nih-cpr-3ea104
  - medlineplus-us-national-library-of-medicine-nih-cpr-a08739
  - american-heart-association-american-academy-of-pedia-d6c089
  - us-army-rigging-techniques-procedures-and-applicatio-404793
  - noaa-national-weather-service-flood-safety-c02f3a
  - noaa-national-weather-service-heat-safety-66fd15
  - noaa-national-weather-service-wildfire-safety-b17a66
  - noaa-national-weather-service-lightning-safety-when-455ad7
  - ready-gov-earthquakes
  - ready-gov-hurricanes
  - ready-gov-tsunamis
  - national-capital-poison-center-poison-control-1-800-e428c9
  - university-of-missouri-extension-unvented-portable-k-e850fe
  - american-academy-of-pediatrics-aap-allergy-and-anaph-3e6f49
  - cdc-treatment-of-low-blood-sugar-r7
  - usuhs-ncdmph-stop-the-bleed-apply-a-tourniquet-r7
  - noaa-national-weather-service-during-a-winter-storm-r7
  - medlineplus-us-national-library-of-medicine-nih-abdo-687213
  - american-heart-association-2020-aha-guidelines-pedia-c1bb66
  - 988-suicide-and-crisis-lifeline-samhsa-988-suicide-a-5f45b0
  - samhsa-disaster-distress-helpline-28957e
related: [00-02-emergency-quick-reference, 00-06-first-60-minutes, 25-03-regional-contacts, 25-09-family-medical-summary, 22-03-go-bags-and-kits, 02-03-cl03-anaphylaxis, 02-01-cl01-type-1-diabetes-injections, 03-04-purifying-water, 08-02-carbon-monoxide-safety, 12-02-bleeding-and-wounds, 12-18-choking-and-cpr, 17-02-tornadoes, 17-06-tornado-shelter, 15-03-family-comms-plan, 29-10-ex10-weather-alert-words, 30-01-the-floors]
cards: [DC-01, DC-02, DC-03, DC-04, DC-08, DC-17, DC-20, DC-25]
explainers: [EX-03, EX-05, EX-07, EX-10]
promote_when: []
photo_slots: []
figures: []
plates: []
condition: null
gear: null
explainer: null
card: null
review_pass: { date: "2026-11-16", passes: [source-trace, consistency, owner-residue, readability, rendering], notes: "Floors checked word for word against 30-01/docs 05; anaphylaxis card re-sourced to AAP plan; tourniquet, hypo, boil, winter-vehicle and lightning rows corrected and sourced." }
---

# Quick-reference cards

**What this page is for.** Short cards for the minute when you cannot read a whole page. Each
is a memory aid for something you have already read and practised (→ 24-01), not a substitute
for training. **The full page always governs**; each card names it. Print them, cut them out,
laminate them (or slip them into zip bags), and put a set wherever an emergency could start.

> **SAFETY — CRITICAL.**
> - **These cards are compressed.** When a card and its page differ, the page is right; reprint
>   the card.
> - **No card contains a calculated dose.** A medical card is replaced by the person's own
>   written plan from their prescriber before it goes in a bag.
> - The floors that appear on these cards are printed word for word from → 30-01.

## Do this now

1. **Print, cut and laminate.** One set on the fridge, one in each go-bag, one in each vehicle,
   one in the medical kit (→ 22-06), one at the shelter spot.
2. **Replace cards 2 and 3 with the prescriber's written plans** for anyone in the household who
   has one (→ 02-03, → 02-01).
3. **Fill in every blank.** A card with blanks is a card that fails. Numbers you typed in
   settings are already printed; everything else comes from → 25-03.
4. **Reprint any card whose page changes** and swap every copy.

## Card 1: Emergency numbers

| | |
|---|---|
| **Emergency (police, fire, ambulance)** | **911** |
| **Poison Help** | **1-800-222-1222** |
| **988 Suicide & Crisis Lifeline** | **988** |
| **Disaster Distress Helpline** | **1-800-985-5990** |
| **Out-of-area contact** (text first, then call) | {{ contacts.out_of_area.name }} · {{ contacts.out_of_area.phone }} |
| **Meeting place near home** | {{ contacts.meet.near_home }} |
| **Meeting place in town** | {{ contacts.meet.in_town }} |
| **Meeting place out of town** | {{ contacts.meet.out_of_town }} |
| **Gas leak** (leave the building first) | {{ contacts.utility.gas.provider }} · {{ contacts.utility.gas.phone }} |
| **Electric outage** | {{ contacts.utility.electric.provider }} · {{ contacts.utility.electric.phone }} |
| **Water** | {{ contacts.utility.water.provider }} · {{ contacts.utility.water.phone }} |
| **Doctor / pharmacy / vet** | ______________ / ______________ / ______________ |
| **Nearest emergency room** | ______________________ |
| **NWS office** | {{ region.home.nws_office }} |
| **Weather radio** | {{#each region.home.nwr as t}}{{t.call}} {{t.freq}} MHz, SAME {{t.same}} · {{else}}______ MHz, SAME ______{{/each}} |
| **If no phone works** | Medical: the cards and pages govern (poisoning → 12-17, CPR → 12-18). Nearest neighbour with medical skills: ______________ |

## Card 2: Anaphylaxis (replace with the person's signed plan, → 02-03)

{{#if has.anaphylaxis}}**In this household:** {{#each allergies as a}}{{a.member}}: {{a.allergen}} ({{a.severity}}) · {{/each}}
Epinephrine is kept: ______________________
{{else}}No anaphylaxis is entered. Keep the card: a reaction can happen to a guest, or a first time.
{{/if}}

| | |
|---|---|
| **Signs** | Any one severe sign: trouble breathing, wheeze or cough, tight or hoarse throat, trouble swallowing, swollen lips or tongue, pale or blue skin, weak pulse, faint or dizzy, many hives over the body, severe vomiting, confusion. Or more than one mild sign at once (AAP, Allergy and Anaphylaxis Emergency Plan) |
| **1. Epinephrine first** | Outer thigh, through clothing if needed. **Do not wait.** Note the time (AAP; CDC, Recognizing and Responding to Anaphylaxis) |
| **2. Call 911** | Or get to care |
| **3. Position** | Lie flat, legs raised. Vomiting: on the side. Struggling to breathe: sitting up. **Never stand or walk them** |
| **4. Second dose** | If symptoms get worse, continue, or do not get better in **5 minutes** (AAP, Allergy and Anaphylaxis Emergency Plan) |
| **5. Stay** | Reactions can return hours later. No 911: that watch is yours, epinephrine in reach |
| **Antihistamine** | **Not a treatment for anaphylaxis.** Never delay epinephrine for anything |
| **Expired or out-of-range device, nothing else available** | Household choice: {{choice DC-04}} → 30-05 |

## Card 3: Diabetes emergency (no dosing; replace with the prescriber's plan, → 02-01)

| | |
|---|---|
| **LOW (hypoglycaemia)** | Shaky, sweaty, confused, irritable, pale, slurred, unsteady (CDC, Low Blood Sugar) |
| **Awake and can swallow** | Fast sugar now; **recheck in about 15 minutes**; repeat until back in range, then a snack or meal (CDC, Treatment of Low Blood Sugar) |
| **Unconscious, seizing, or cannot swallow** | **Nothing by mouth. Give glucagon. Call 911.** On their side. Sugar by mouth only once awake and able to swallow |
| **HIGH with ketones (DKA risk)** | Thirst, peeing a lot, nausea or vomiting, belly pain, fruity breath, fast deep breathing, confusion (CDC, Diabetic Ketoacidosis) |
| **What to do** | **Check ketones.** Fluids. Follow the prescriber's sick-day plan. **DKA is an emergency: get help** |
| **Pump or sensor failure** | The prescriber's written fallback plan (→ 02-02) |
| **Insulin** | **A frozen-then-thawed insulin vial or pen is discarded.** Heat-exposed: {{choice DC-08}} → 30-09. Fridge range 36 to 46 °F (FDA, Insulin Storage in an Emergency). Never ration on your own judgement |
| **Days of insulin left** | ______ (update weekly) |

## Card 4: Water

| | |
|---|---|
| **This household, floor** | **{{ derived.water.floor_gal_day }} gal a day** (the rationing line) |
| **This household, plan** | **{{ derived.water.plan_gal_day }} gal a day**; two weeks = {{ derived.water.two_weeks_gal }} gal |
| **Days of water** | Stored gallons ÷ {{ derived.water.plan_gal_day }} |
| **1. Settle** | Let cloudy water settle, then pour it through cloth or a coffee filter |
| **2. Disinfect** | **Boil: a rolling boil for 1 minute** (3 minutes above 5,000 ft) (EPA, Emergency Disinfection of Drinking Water), **or** chemicals: **amounts are on → 03-04, not here**, because bleach strength varies by product and age |
| **3. Store** | Covered, cool, dark, labelled with the date |
| **Pool or salt water** | Filtering and boiling **do not remove salt or pool chemicals**. Distillation only (→ 03-03) |
| **Reserves in the house** | Water heater {{ dwelling.water_heater_gallons }} gal · pipes · toilet tanks (not bowls) |

## Card 5: Carbon monoxide

| | |
|---|---|
| **The floor** | **Never run a generator, charcoal, or any engine indoors, in a garage, or near an open window.** |
| **What it is** | A gas with **no colour, no smell, no taste** that kills silently (CDC, Carbon Monoxide Poisoning: Basics; → 29-03) |
| **Never indoors** | Generator, grill, charcoal, camp stove, any heater not rated for indoor use, a running vehicle (including in an attached garage, door open or not) |
| **Symptoms** | Headache, dizziness, nausea, weakness, confusion, sleepiness. **Several people sick at once, or better outside = suspect CO** |
| **Alarm sounds or you suspect it** | **1. Everyone outside into fresh air, now. 2. Call 911. 3. Nobody goes back in** until it is cleared. Count heads |
| **No 911** | Fresh air is the treatment: rest outside for hours; turn off the source; air the house fully; symptoms can return, so anyone affected takes it easy |
| **Alarms** | Battery CO alarm on every level and outside every sleeping area. Test monthly. We have {{ gear.co_alarms }} |

## Card 6: Severe bleeding

| | |
|---|---|
| **1. Pressure** | Hard, direct, both hands, and **hold** |
| **2. Limb bleeding that will not stop** | **Tourniquet** 2 to 3 inches above the wound, not over a joint. Tighten until the bleeding **stops**. It will hurt. If it still bleeds, a second one above the first (Stop the Bleed, USUHS) |
| **3. The floor** | **Never loosen a tourniquet once placed while help can still come; mark the time.** Write it on the strap or the skin, and say it aloud. If no help will ever come, the conversion decision is DC-25: {{choice DC-25}} → 30-26 |
| **4. Body or groin wound** | **Pack** the wound with gauze and press hard |
| **5. Keep them warm** | Cold makes bleeding worse |
| **6. Get help** | → 12-02 |
| **Tourniquets are kept** | ______________________ |

## Card 7: Tornado

| | |
|---|---|
| **Watch** | Conditions favourable: be ready, stay alert |
| **Warning** | Happening or imminent: **go now** |
| **Go to** | {{#if has.shelter_room}}**{{ dwelling.shelter_room }}**{{else}}the lowest floor, the innermost room with no windows: ______________{{/if}} |
| **Do** | Cover head and neck; helmets on children if you have them; shoes on |
| **Take** | Shoes, light, weather radio, phone, water, **rescue medicines and the medical kit** (the house may not be there afterwards) |
| **Not** | Not in a vehicle, not under an overpass (NOAA Storm Prediction Center, Tornado Safety FAQ). {{#if has.mobile_home}}**You live in a mobile home: it is not shelter. Go to a sturdy building before the warning** (→ 17-06).{{else}}A mobile home is not shelter.{{/if}} |
| **Gas smell after** | Get out; shut the gas off only if you know how; call from outside |

Full page: → 17-02, → 17-06 (NWS, Tornado Safety).

## Card 8: Stranded in a vehicle in winter

| | |
|---|---|
| **Stay with the vehicle** | It is shelter, and it is what searchers find (NWS, During a Winter Storm) |
| **Be seen** | Bright cloth on the antenna; dome light on at night when running; hazards sparingly |
| **Before running the engine** | **Clear the exhaust pipe** and **crack a window away from the wind**. About 10 minutes an hour (NWS, During a Winter Storm) |
| **Insulate** | Blankets, everyone together, move arms and legs now and then |
| **Water** | Do not eat snow: melt it |
| **Phone** | Text your location while you have signal, then save the battery |
| **Children** | Watch them constantly: they cool much faster |
| **Frostbite** | At extreme wind chill, minutes. Cover all skin (→ 08-05) |

## Card 9: Power cut and food safety

| | |
|---|---|
| **Keep the fridge and freezer closed** | Refrigerated food about **4 hours**; full freezer about **48 hours**, half full about **24** (USDA/HHS, Food Safety During a Power Outage) |
| **When in doubt, throw it out** | Never taste to test |
| **Power goes to, in order** | 1. Medical devices · 2. Light · 3. Communications · 4. Refrigeration · 5. Everything else (→ 09-01) |
| **Check** | CO alarms · water · the heat plan · the neighbours |
| **Eat down** | Fridge first, then freezer, then pantry |
| **Generator** | **Never connect a generator to house wiring except through a transfer switch, or an interlock kit with the main breaker off. Never backfeed through an outlet with a double-male ("suicide") cord.** |

## Card 10: Grab and go

| You have | You take |
|---|---|
| **60 seconds** | People{{#if has.pets}}, pets{{/if}}, **medical kit**, go-bags, phones, keys, wallets |
| **10 minutes** | + document kit, water, food bin, sleeping bags, coats and boots for everyone |
| **30 minutes** | + tools, stove and fuel, extra water, extra clothing (→ 22-05) |

Who carries or leads whom: {{#each children as c}}{{c.label}} → ______ · {{else}}______{{/each}}

Go-bags are at: ______________ · Medical kit is at: ______________{{#if has.pets}} · Pet carriers are at: ______________{{/if}}

## Card 11: Daily priorities when it has gone on a long time

| Every day, in this order |
|---|
| 1. **Medical**: medicines, supplies, rescue medicines in date and in reach |
| 2. **Water**: treated, stored, tomorrow's secured |
| 3. **Warmth or cooling**: the one room, fuel for tomorrow |
| 4. **Food**: cook it, ration it; children eat properly |
| 5. **Sanitation**: waste out, hands washed |
| 6. **Security**: doors, light discipline, awareness |
| 7. **People**: sleep, routine, children, each other |

**Never ration:** drinking water, handwashing, medicine, children's food, sleep. Log the day
(→ 25-05). Shortest clock: ______ days.

## Card 12: Choking and CPR (memory aid: the class governs, → 12-18)

| | |
|---|---|
| **Coughing hard** | Let them cough. Watch |
| **Silent, no air, turning blue** | **Act now** |
| **Under 1 year** | 5 back blows (face down along your forearm) + 5 chest thrusts (two fingers). Repeat. **Never abdominal thrusts on a baby** (MedlinePlus, Choking: infant under 1 year) |
| **Age 1 and up** | 5 back blows, then 5 abdominal thrusts (in and up, hard). Alternate until clear |
| **Goes limp** | Start CPR. Remove from the mouth only what you can see |
| **CPR** | Not breathing, or only gasping: **push hard, push fast, centre of the chest, 100 to 120 a minute; 30 pushes : 2 breaths** (MedlinePlus, CPR) |
| **Depth** | Baby about 1½ in (two fingers; cover mouth **and** nose for gentle puffs) · child about 2 in (one or two hands) · adult 2 to 2.4 in (two hands) |
| **Untrained or unwilling to give breaths** | Pushes only |
| **More than one rescuer** | Swap every 2 minutes |

## Card 13: Six knots (utility only: never for climbing or lifting people, → 16-03)

| Knot | Use | How |
|---|---|---|
| **Words** | | **Working end** = the short end you move. **Standing part** = the long rope to the load |
| **Bowline** | A fixed loop | Small loop in the standing part; working end up through it, behind the standing part, back down the loop; snug. The end finishes inside the loop |
| **Taut-line hitch** | An adjustable guy line | Round the anchor; two wraps round the standing part inside the loop; one wrap outside; tuck under itself. Slides by hand, holds under pull |
| **Clove hitch** | Onto a post | Over and around; cross over the standing part; around again; tuck under the second wrap. Add a half hitch: it slips under changing loads |
| **Two half hitches** | Tying off | Round the object, over, behind, up through; repeat in front |
| **Square knot** | Bundles, same-size rope | Right over left and under; left over right and under. It lies flat, or it is a granny: retie. **Not for joining ropes under load** |
| **Trucker's hitch** | Tightening a load | Fix the far end; a small loop in the standing part; pull a fold through it; working end round the anchor, up through the fold; haul; lock with two half hitches |

Text cannot draw a knot: the US Army rigging manual (FM 5-125) plates behind → 16-03 are the
pictures.

## Card 14: Communications (PACE; fill the blanks or this card fails, → 15-03)

PACE = **P**rimary, **A**lternate, **C**ontingency, **E**mergency: four ways to reach each other,
tried in that order.

| | Primary | Alternate | Contingency | Emergency |
|---|---|---|---|---|
| **Local** | Text, then call | Out-of-area contact relays | Radio channel ______ | Go to the meeting place; leave a note |
| **Regional** | Text (it queues) | Out-of-area contact at a set time: ______ | ______________ | ______________ |
| **At a destination** | Call or text home and the out-of-area contact | Destination phones | Radio window: ______ | ______________ |

**Out-of-area contact:** {{ contacts.out_of_area.name }} · {{ contacts.out_of_area.phone }} ·
backup ______________. **No bars:** 911 works on any carrier's tower; some phones can text by
satellite (clear sky). **Weather radio:** {{#each region.home.nwr as t}}{{t.freq}} MHz ({{t.call}}) · {{else}}______ MHz{{/each}}.
**Overdue rule:** no word by ______ hours after departure, the contact calls ______________.

## Card 15: Watch, warning, advisory (→ 29-10)

| Level | Meaning | Do |
|---|---|---|
| **Advisory** | Hazardous but lesser | Adjust plans; errands early; kit in the vehicle |
| **Watch** | Conditions **favourable** | **Get ready now:** water filled, everything charging, tank topped up, plan out. Prepare at the watch, not the warning |
| **Warning** | Happening or imminent | **Act** on the row below |

| Warning | Our action |
|---|---|
| **Tornado** | Shelter spot now, heads covered (Card 7) |
| **Severe thunderstorm** | Inside; away from windows; lightning means indoors (NWS, Lightning Safety) |
| **Blizzard, winter storm, ice storm** | No travel. One-room plan ready; everything charged; expect days without power |
| **Extreme cold** | Outside only for essential minutes; children stay in |
| **Flood or flash flood** | Higher ground. **Never drive into water over a road** (NWS, Flood Safety) |
| **Red flag, fire** | Leave early; do not wait to see (NWS, Wildfire Safety) |
| **Extreme heat** | Shade, fluids, the coolest room; watch children, elders and medicines (NWS, Heat Safety) |
| **Hurricane** | Leave when told to; if staying, the interior room above flood level (Ready.gov, Hurricanes) |

Home hazards rated 2 or 3 move to the top of this card:
{{#each region.home.hazards as z}}{{z.name}} {{z.rating_text}} · {{/each}}

## Card 16: Indoor heaters

| | |
|---|---|
| **Before any heater is lit** | **A battery CO alarm installed and tested** in that room and where people sleep |
| **Only heaters rated for indoor use** | Read the label (→ 29-14). Everything else stays outside |
| **One heater at a time** | Never unattended. Clearances and ventilation **as the manual states** |
| **Overnight while people sleep** | Household choice: {{choice DC-01}} → 30-02 |
| **Propane cylinder bigger than 1 lb indoors** | Household choice: {{choice DC-02}} → 30-03. Refilling 1-lb cylinders: {{choice DC-03}} → 30-04 |
| **Kerosene** | **1-K only**, clear, no water layer in a jar check. **Gasoline in a kerosene heater = fire or explosion** (University of Missouri Extension, Unvented Portable Kerosene Heaters). Old fuel: {{choice DC-17}} → 30-18 |
| **Filling** | **Fuel is never stored or transferred near an open flame or a running appliance.** Outdoors, heater off and cold |
| **Fuel cans** | Read the label aloud, smell, then pour. An unlabelled can is not poured (→ 29-01) |
| **Leak check (propane)** | Soapy water on every joint, every time. Gas smell: valve off, everyone out |
| **Children** | A barrier around the heater; nothing drying on top |
| **Alarm, headache, dizziness, nausea** | Heater off if in reach, **everyone out**, then air the room (Card 5) |

Open-flame cooking and candles indoors: {{choice DC-20}} → 30-21. Our heaters:
{{#each heaters as h}}{{h.kind_text}} ({{h.model}}) · {{else}}none entered{{/each}}.

## Card 17: Other hazards in one line each

| Hazard | First move | Page |
|---|---|---|
| **Earthquake** | **Drop, cover and hold on**; stay inside until the shaking stops; then check for gas and fire (Ready.gov, Earthquakes) | → 17-12 |
| **Hurricane** | Leave when officials say; if not, an interior room above flood level; **never in a flooded car** (Ready.gov, Hurricanes) | → 17-13 |
| **Wildfire or smoke** | Leave early; N95 masks; windows shut; a clean-air room (NWS, Wildfire Safety) | → 17-14 |
| **Extreme heat** | Shade, water, the coolest room; **never leave a child or pet in a car** (NWS, Heat Safety) | → 17-04 |
| **Lightning** | When thunder roars, go indoors; a hard-topped car is next best (NWS, Lightning Safety) | → 17-02 |
| **Flood** | Higher ground; **turn around, do not drown** (NWS, Flood Safety) | → 17-03 |
| **Poisoning** | **Poison Help 1-800-222-1222**; do not make the person vomit unless told to | → 12-17 |
{{#if is.coastal}}| **Tsunami (coast)** | Strong shaking or the sea pulling back: go to high ground or inland at once (Ready.gov, Tsunamis) | → 17-15 |
{{/if}}

## Printing and keeping them current

- **Print at full size, cut, laminate** (or a zip bag and tape). **Punch a corner and keep them
  on a ring** so a set stays together.
- **Where:** fridge · each go-bag · each vehicle · medical kit · shelter spot. **Card 16 goes
  with each heater** too.
- **Every card is a compressed page.** When the page changes, reprint and swap every copy: **a
  stale card in a bag is worse than none.**
- **Cards 2 and 3 are the ones a stranger may have to use.** Make them legible, complete, and
  in the outside pocket.

Related: → 00-02 emergency quick reference · → 00-06 the first 60 minutes · → 25-09 medical
summary · → 25-03 contacts · → 22-03 where the cards live · → 30-01 the floors.

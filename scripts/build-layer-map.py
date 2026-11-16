#!/usr/bin/env python3
"""Build the layer map for the kit from the household binder's manifest.json.

Usage: python3 scripts/build-layer-map.py /path/to/SHTF/manifest.json

Writes data/layer-map.json and docs/03-layer-map.md.

Layers
  core       L0: true everywhere; ships to every household after de-personalising
  region     L1: built from the national region datasets (climate, hazards, plants, codes)
  household  L2: written per household from a template + the profile
  condition  L2: a condition-library module (only if the condition is selected, but the
                 whole library is always present in the app)
  gear       L2: a gear module (heater, station, generator, trailer, well, pool, septic...)
  generated  built by scripts (indexes, intros, bibliography)
  drop       owner-only; does not go into the kit
Actions
  ship       de-personalise only (names, places, gear) and ship
  rewrite    substantive rewrite: household rule boxes -> decision cards, novice explainers
  template   keep structure, replace household facts with profile slots
  dataset    page body comes from the region datasets
  module     becomes (or seeds) a module in the condition/gear library
  drop       not carried over
"""
import json, sys, collections, pathlib

MANIFEST = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else None
ROOT = pathlib.Path(__file__).resolve().parents[1]

# section defaults: (layer, action)
SECTION_DEFAULT = {
    '00': ('core', 'rewrite'), '01': ('core', 'template'), '02': ('condition', 'module'),
    '03': ('core', 'ship'), '04': ('core', 'ship'), '05': ('core', 'ship'), '06': ('core', 'ship'),
    '07': ('core', 'ship'), '08': ('core', 'rewrite'), '09': ('core', 'rewrite'), '10': ('core', 'ship'),
    '11': ('core', 'ship'), '12': ('core', 'ship'), '13': ('core', 'ship'), '14': ('core', 'rewrite'),
    '15': ('core', 'ship'), '16': ('core', 'ship'), '17': ('region', 'dataset'), '18': ('core', 'ship'),
    '19': ('core', 'ship'), '20': ('core', 'template'), '21': ('core', 'ship'), '22': ('household', 'template'),
    '23': ('core', 'template'), '24': ('core', 'ship'), '25': ('core', 'template'), '26': ('core', 'template'),
    '27': ('core', 'ship'), '28': ('drop', 'drop'), '29': ('drop', 'drop'), '30': ('drop', 'drop'),
    '31': ('core', 'ship'),
}

# per-page overrides: id -> (layer, action, note)
OVERRIDE = {
 '00-01-how-to-use-this-binder': ('core','rewrite','App-first: offline install, charge discipline, PDF export button.'),
 '00-02-emergency-quick-reference': ('household','template','Numbers and names are slots; 911 and Poison Control constant.'),
 '00-03-master-index': ('generated','ship','Built from the generated page set.'),
 '00-04-family-emergency-plan': ('household','template','Contacts, meeting places, out-of-area contact from profile.'),
 '00-05-safety-disclaimer': ('core','rewrite','New disclaimer: AI-generated, AI-reviewed, not human-verified; household decides risk; private copy notice.'),
 '00-06-first-60-minutes': ('core','template','Gear slots (fridge, stations, heaters) from profile.'),
 '00-07-household-roles': ('household','template','Roles table built from members.'),
 '00-08-binder-map': ('generated','ship',''),
 '01-01-phase-a-shelter-in-place': ('core','template','House facts (water, heat, warm room) are slots.'),
 '01-02-go-no-go-decision': ('core','rewrite','Triggers generalised; destination names are slots; add decision card DC-19.'),
 '01-03-phase-b-movement': ('core','template','Route and winter travel generalised; kids/ages gated.'),
 '01-04-phase-c-establish': ('core','ship',''),
 '01-05-choosing-a-destination': ('household','template','Up to three destinations with status agreed/unannounced/none.'),
 '01-06-phase-transition-checklists': ('core','template',''),
 '02-01-t1d-overview-and-supply-math': ('condition','module','Seeds CL-01 Type 1 diabetes: dependency map + supply math worksheet (no derived doses).'),
 '02-02-insulin-without-the-grid': ('condition','module','CL-01/CL-02: insulin storage; FDA/manufacturer windows as published; frozen = discard rule as a floor.'),
 '02-03-pump-to-injection-fallback': ('condition','module','CL-01 pump/CGM variant: tech-failure ladder generalised; basal rule becomes "my prescriber-approved fallback" slot.'),
 '02-04-cgm-conservation-and-dka': ('condition','module','CL-01: sick-day and DKA warning signs at WebMD level.'),
 '02-05-sourcing-insulin-supplies': ('condition','module','CL-01: sourcing/scavenging insulin; decision card DC-08.'),
 '02-06-hugh-anaphylaxis-action-plan': ('condition','module','CL-03 anaphylaxis: action plan template with the published epinephrine weight bands.'),
 '02-07-epinephrine-storage-and-supply': ('condition','module','CL-03: storage, heat/cold, expired-use decision card DC-04.'),
 '02-08-allergen-safe-food-plan': ('condition','module','CL-03/CL-04 food allergy: allergen slots; traded/unlabeled food decision card DC-18.'),
 '02-09-pet-care-cats': ('household','module','Pets module (cats/dogs/other) incl. decision card DC-10.'),
 '02-10-evaporative-cooling-pouches': ('core','ship','Applies to any refrigerated medication; keep in core medical.'),
 '02-11-diabetes-rig-offline-docs-and-assistant': ('drop','drop','Owner-specific rig docs. Replaced by CL-01 pump/CGM module.'),
 '02-12-evacuation-medical-logistics': ('core','template','Generalised: evacuating with any medical dependency; patients and supply clocks are slots.'),
 '03-01-daily-water-needs': ('core','template','Household size and nursing/infant flags from profile.'),
 '03-03-pool-water-desalination': ('gear','module','GM pool module (saltwater/chlorine pool as a water source).'),
 '03-06-winter-water': ('core','ship','Region-gated: shown first in cold climates, present everywhere.'),
 '03-10-well-water-without-power': ('gear','module','GM well module; Kimball specifics removed.'),
 '04-01-calorie-and-stockpile-math': ('core','template','Household calorie table from members/ages.'),
 '04-09-winter-cold-storage': ('core','ship','Region-gated.'),
 '04-19-freeze-dried-stockpile': ('core','template','Calorie plan-of-record; owner brands removed; quantities from household size.'),
 '05-01-small-urban-garden': ('region','dataset','Hardiness zone, frost dates and crop list from region data.'),
 '05-04-backyard-chickens': ('core','rewrite','Ordinance paragraph becomes a pre-collapse note; husbandry stays core.'),
 '05-06-foraging-northern-plains': ('region','dataset','National plant appendix: killers and look-alikes per ecoregion; all regions always in the app.'),
 '05-07-hunting-sd': ('region','dataset','Game species, seasons as pre-collapse note, field methods core.'),
 '05-08-fishing-and-ice-fishing': ('core','ship','Ice-fishing part region-gated.'),
 '05-13-perennials-and-fruit': ('region','dataset','By hardiness zone.'),
 '05-17-wild-edibles-calendar': ('region','dataset','National plant appendix: safe starters per ecoregion with plates.'),
 '05-18-goshen-ozark-garden-calendar': ('household','template','Destination garden calendar generated per destination from region data.'),
 '05-19-ozark-foraging-and-hazards': ('household','template','Destination foraging/hazards generated per destination from region data.'),
 '05-20-kimball-ranch-food-plan': ('drop','drop','Owner destination. Pattern kept as the destination-food-system template.'),
 '06-03-firewood-basics': ('core','dataset','Species table and plates from the regional tree dataset.'),
 '06-05-alternative-fuels': ('core','rewrite','Add the fuels explainer EX-01 up front.'),
 '06-06-fuel-storage-safety': ('core','rewrite','Decision cards DC-05 garage storage, DC-17 kerosene age; label colours as a core rule.'),
 '06-07-moving-and-transferring-fuel': ('core','ship',''),
 '06-08-fuel-transport': ('core','rewrite','Decision card DC-06 fuel in a passenger vehicle; trailer facts are gear slots.'),
 '07-01-cooking-on-the-fireplace': ('core','rewrite','Generalised: open fire, fireplace, fire pit.'),
 '07-05-propane-and-camp-stoves': ('core','rewrite','CO explainer EX-03 reference; indoor use is a floor, not a card.'),
 '07-06-electric-kettle-cooking': ('core','template','Station slots.'),
 '07-07-freeze-dried-rehydration': ('core','ship',''),
 '08-01-heating-one-room': ('core','rewrite','Warm-room method; house slots; decision card DC-01 overnight heater.'),
 '08-02-carbon-monoxide-safety': ('core','rewrite','Floor page; EX-03 explainer embedded.'),
 '08-04-emergency-heat-options': ('core','rewrite','Options matrix with cards DC-01, DC-02.'),
 '08-07-ducted-heater-operation': ('gear','module','GM ducted diesel/kerosene heater.'),
 '08-09-mr-heater-buddy': ('gear','module','GM portable propane heater (Buddy family) incl. DC-01/DC-02/DC-03.'),
 '08-10-dyna-glo-kerosene-heater': ('gear','module','GM wick kerosene heater incl. DC-17.'),
 '09-03-batteries-and-storage': ('core','rewrite','Explainer EX-02 batteries/stations; owner stations become gear slots.'),
 '09-04-generators': ('core','rewrite','Backfeed is a floor; cord-and-plug conversion as a decision card DC-07 with the write-up.'),
 '09-05-winter-solar-reality': ('region','dataset','Sun hours by month from region data; the method is core.'),
 '09-06-charging-medical-devices': ('core','template','Devices from the condition modules selected.'),
 '09-10-power-for-medical': ('core','template','Refrigerated-medication power sizing; fridge/station slots.'),
 '09-16-outage-day-one': ('core','template','Live procedure with house and gear slots.'),
 '11-02-keeping-kids-warm': ('core','template','Age-gated; ages are slots.'),
 '11-09-kids-sizing-ledger': ('household','template',''),
 '12-07-meds-stockpile': ('core','template','Household "my meds" table from profile; OTC list core.'),
 '12-11-chronic-conditions': ('core','rewrite','Becomes the condition-library index page.'),
 '12-12-childbirth-and-womens-health': ('core','ship','Also seeds CL-12 pregnancy.'),
 '12-20-field-dentistry': ('core','rewrite','Remove the in-house dentist; keep layperson dental first aid.'),
 '13-12-septic-off-grid': ('gear','module','GM septic.'),
 '14-04-caliber-roles-and-inventory': ('household','template','Only if firearms selected.'),
 '14-06-spare-parts-and-armorer': ('gear','module','Only if firearms selected; platform slots.'),
 '14-10-suppressors-and-nfa': ('core','rewrite','Law content becomes a pre-collapse note.'),
 '14-11-defense-and-sd-law': ('core','rewrite','State law line from region dataset as pre-collapse note; household rule becomes DC-12.'),
 '14-14-safe-storage-and-child-access': ('core','ship','Age-gated emphasis.'),
 '15-01-weather-alerts': ('region','dataset','NWS office, transmitter frequencies, SAME codes from dataset.'),
 '15-03-family-comms-plan': ('household','template',''),
 '15-05-ham-and-licensing': ('core','ship','Licensing as pre-collapse note.'),
 '15-08-destination-comms': ('household','template','Per destination.'),
 '15-09-corridor-comms': ('household','template','Per route.'),
 '16-10-tire-failures-roadside': ('core','template','Vehicle kit slots.'),
 '16-11-trailer-maintenance-and-repair': ('gear','module','GM trailer; only if a trailer is owned.'),
 '17-08-power-grid-failure': ('core','ship',''),
 '17-09-pandemic-and-illness': ('core','ship',''),
 '17-10-reading-the-sky': ('core','ship',''),
 '17-11-corridor-hazards': ('household','template','Per route from region hazard data.'),
 '19-08-practice-continuity': ('core','rewrite','Generalised: income continuity for a self-employed adult.'),
 '20-01-toddler-and-infant-needs': ('core','template','Age-gated.'),
 '20-05-infant-feeding': ('core','template','Age-gated; nursing flag.'),
 '20-06-diapers-and-hygiene': ('core','template','Age-gated.'),
 '22-03-go-bags-and-kits': ('household','template','Per member.'),
 '22-06-kit-medical': ('condition','module','Built from selected condition modules.'),
 '23-02-master-consumables-table': ('household','template','Quantities from household size and gear.'),
 '25-01-planting-calendar': ('region','dataset',''),
 '25-02-conversions-and-math': ('core','ship',''),
 '25-03-regional-contacts': ('region','dataset','NWS, state EM, poison control, utilities (user enters their own); national appendix lists every state.'),
 '25-04-maps': ('household','template','Map list per home base, destinations and routes; the app embeds no map tiles (owner decision pending).'),
 '25-05-blank-logs': ('core','ship',''),
 '25-06-source-bibliography': ('generated','ship','Titles, publishers and dates only; no URLs printed.'),
 '25-07-glossary': ('core','rewrite','Expanded for novices; absorbs explainer vocabulary.'),
 '25-08-quick-reference-cards': ('core','template','Cards with household slots.'),
 '25-09-family-medical-summary': ('household','template',''),
 '27-03-protecting-electronics': ('core','template','Devices from condition modules.'),
 '27-06-potassium-iodide': ('core','ship','FDA table as published; DC-22 for adults over 40.'),
}

SECTION_NOTE = {
 '17': 'Hazard pages are generated from the region hazard dataset; the method text (what to do) is core and shared.',
 '28': 'Owner power-system reference (one house). Replaced by gear modules: solar + station, generator, panel wiring, with the owner pages as the worked example in the module author notes only.',
 '29': 'Owner diabetes rig (Trio/AAPS). Replaced by CL-01 pump/CGM variant written at WebMD level; no loop-build instructions.',
 '30': 'Reproduced third-party documentation (Juggluco guide: author forbids redistribution; AndroidAPS docs: AGPL). Not shipped. If a household selects CL-01 with a DIY loop, the AGPL docs are fetched into their private copy at download time.',
 '31': 'Public-domain Air Force survival handbook extraction. Ships unchanged in every binder; figures to be restored (see docs/08-pictures-plan.md).',
}

def main():
    m = json.load(open(MANIFEST))
    rows = []
    for p in m['pages']:
        pid = p['id']; sec = pid[:2]
        if pid.endswith('-section-intro'):
            layer, action, note = 'generated', 'ship', 'Section intro rebuilt by scripts.'
        elif pid in OVERRIDE:
            layer, action, note = OVERRIDE[pid]
        else:
            layer, action = SECTION_DEFAULT[sec]; note = ''
        rows.append({'id': pid, 'title': p['title'], 'section': p['section'], 'danger_level': p['danger_level'],
                     'layer': layer, 'action': action, 'note': note})
    (ROOT/'data').mkdir(exist_ok=True)
    json.dump({'source_manifest_pages': len(rows), 'pages': rows}, open(ROOT/'data/layer-map.json','w'), indent=1)

    by_layer = collections.Counter(r['layer'] for r in rows)
    by_action = collections.Counter(r['action'] for r in rows)
    by_sec = collections.defaultdict(list)
    for r in rows: by_sec[r['section']].append(r)

    out = []
    out.append('# Layer map: every page of the household binder, tagged for the kit\n')
    out.append('Generated by `scripts/build-layer-map.py` from the household binder manifest '
               f'({len(rows)} pages). Edit the tag tables in the script, not this file.\n')
    out.append('## Legend\n')
    out.append('| Layer | Meaning |\n|---|---|\n'
               '| core | L0. True everywhere. Ships to every household after de-personalising. |\n'
               '| region | L1. Body comes from the national region datasets (climate, hazards, plants, codes, offices). |\n'
               '| household | L2. Written per household from a template and the profile. |\n'
               '| condition | L2. Seeds a condition-library module. The whole library is always in the app; the household\'s selected conditions are promoted to the front. |\n'
               '| gear | L2. Seeds a gear module, included when the household owns that class of gear. |\n'
               '| generated | Built by scripts (indexes, intros, bibliography). |\n'
               '| drop | Owner-only. Does not go into the kit. |\n')
    out.append('| Action | Meaning |\n|---|---|\n'
               '| ship | De-personalise (names, places, gear models) and ship. |\n'
               '| rewrite | Substantive rewrite: household rule boxes become decision cards; novice explainers added. |\n'
               '| template | Keep the structure; household facts become profile slots. |\n'
               '| dataset | Body generated from the region datasets. |\n'
               '| module | Becomes, or seeds, a module in the condition or gear library. |\n'
               '| drop | Not carried over. |\n')
    out.append('## Totals\n')
    out.append('| Layer | Pages |\n|---|---|\n' + ''.join(f'| {k} | {v} |\n' for k, v in sorted(by_layer.items(), key=lambda kv: -kv[1])))
    out.append('| Action | Pages |\n|---|---|\n' + ''.join(f'| {k} | {v} |\n' for k, v in sorted(by_action.items(), key=lambda kv: -kv[1])))
    out.append('## Pages by section\n')
    for sec, rs in sorted(by_sec.items()):
        out.append(f'### {sec}\n')
        if sec[:2] in SECTION_NOTE: out.append(SECTION_NOTE[sec[:2]] + '\n')
        out.append('| Page | Title | Danger | Layer | Action | Note |\n|---|---|---|---|---|---|\n')
        for r in rs:
            t = r['title'].replace('|','/')
            out.append(f"| {r['id']} | {t} | {r['danger_level']} | {r['layer']} | {r['action']} | {r['note']} |\n")
        out.append('\n')
    (ROOT/'docs').mkdir(exist_ok=True)
    open(ROOT/'docs/03-layer-map.md','w').write('\n'.join(out))
    print(dict(by_layer)); print(dict(by_action))

if __name__ == '__main__':
    main()

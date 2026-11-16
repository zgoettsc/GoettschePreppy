"""Build data/plants/species.json, data/plants/county-distribution.json and
data/regions/ecoregion-plants.json from the authored species files, the USDA PLANTS distribution
download and worker D1's county -> ecoregion data.

  python3 scripts/plants/build_species.py

Ecoregion method (coarse, and the binder says so):
  1. For every county where USDA PLANTS records the species, the species is listed for every EPA
     Level III ecoregion that covers at least 10 percent of that county (D1's whole-county shares).
  2. For a state where PLANTS records the species but gives no county, the species is listed for
     every ecoregion covering at least 10 percent of any county in that state ("state-coarse").
  3. Fungi (no PLANTS records) and planted ornamentals use a hand-set state list from the
     literature, mapped as in 2.
PLANTS county records mean "documented here", not "common here"; absence of a record does not
mean the plant is absent.
"""
import json
from collections import defaultdict
from datetime import date
from common import ROOT, RAW, LOWER48, EAST, RISK_ORDER, HEAT_ORDER, merged_species
from distribution import parse
from common import plants_profile, plants_distribution

SHARE_MIN = 0.10
SRC = {  # authored alias -> key in sources/index.json or sources/additions/D2.json
    'plants': 'usda-nrcs-plants-database-plant-profiles-and-image-l-a7089c',
    'usfs-water-hemlock': 'usda-forest-service-water-hemlock-cicuta-maculata-c0a866',
    'ars-water-hemlock': 'usda-ars-poisonous-plant-research-laboratory-water-h-ab9a68',
    'ars-poison-hemlock': 'usda-ars-poisonous-plant-research-laboratory-poison-255ffb',
    'cdc-mmwr-water-hemlock': 'cdc-water-hemlock-poisoning-maine-1992-mmwr-43-13-bf58c2',
    'umn-hemlock': 'university-of-minnesota-extension-poison-and-water-h-680b86',
    'sdsu-hemlock': 'sdsu-extension-poisonous-plants-on-rangelands-hemloc-0c4ddd',
    'missouri-wood-fuel': 'university-of-missouri-extension-wood-fuel-for-heati-b63761',
    'epa-burnwise': 'us-epa-burn-wise-heating-with-wood-safe-operation-se-ba0e76',
    'ars-pprl': 'usda-ars-poisonous-plant-research-laboratory-poisono-d2a001',
    'cornell-poison': 'cornell-university-department-of-animal-science-plan-d2a002',
    'ncsu-toolbox': 'nc-state-extension-north-carolina-extension-gardener-d2a003',
    'niosh-plants': 'cdc-niosh-poisonous-plants-outdoor-workers-d2a004',
    'fda-badbug': 'us-fda-bad-bug-book-2nd-edition-natural-toxins-mushr-d2a005',
    'cdc-mmwr-amanita-2016': 'cdc-amanita-phalloides-mushroom-poisonings-northern-d2a006',
    'cdc-ricin': 'cdc-ricin-chemical-fact-sheet-d2a007',
    'fpl-wood-handbook': 'usda-forest-service-fpl-wood-handbook-wood-as-an-engi-d2a008',
    'silvics': 'usda-forest-service-silvics-of-north-america-agricul-d2a009',
    'feis': 'usda-forest-service-fire-effects-information-system-d2a010',
    'epa-ecoregions': 'us-epa-level-iii-and-iv-ecoregions-of-the-continenta-d2a011',
    'umaine-fiddleheads': 'university-of-maine-cooperative-extension-facts-on-f-d2a012',
}

# Hand-set state lists (literature, coarse) for fungi and for where planted ornamentals are met.
ALL = LOWER48 + ['AK']
SOUTH = ['VA', 'NC', 'SC', 'GA', 'FL', 'AL', 'MS', 'LA', 'TX', 'AR', 'TN', 'KY', 'OK']
WARM = ['FL', 'GA', 'SC', 'AL', 'MS', 'LA', 'TX', 'AZ', 'CA', 'NV', 'NM', 'HI']
NORTH_MTN = ['AK', 'WA', 'OR', 'ID', 'MT', 'WY', 'CO', 'UT', 'CA', 'NM', 'MN', 'WI', 'MI', 'ME', 'NH', 'VT', 'NY', 'PA', 'MA']
FUNGUS_STATES = {
    'eastern-destroying-angel': EAST, 'fly-agaric': ALL, 'deadly-galerina': ALL, 'deadly-dapperling': ALL,
    'deadly-conocybe': ALL, 'false-morel': NORTH_MTN, 'green-spored-parasol': EAST + ['CA', 'AZ', 'NM', 'HI'],
    'jack-o-lantern': EAST, 'sweating-mushroom': ALL,
}
PLANTED = {  # where people meet these in yards and parks (in addition to PLANTS records of escapes)
    'english-yew': LOWER48, 'japanese-yew': LOWER48, 'oleander': WARM, 'yellow-oleander': ['FL', 'TX', 'HI'],
    'sago-palm': WARM, 'nandina': SOUTH + ['CA'], 'lantana': WARM, 'castor-bean': LOWER48,
    'foxglove': LOWER48, 'lily-of-the-valley': LOWER48, 'daffodil': LOWER48, 'japanese-pieris':
    ['ME', 'NH', 'VT', 'MA', 'RI', 'CT', 'NY', 'NJ', 'PA', 'DE', 'MD', 'VA', 'NC', 'OH', 'MI', 'WA', 'OR'],
    'golden-chain': ['WA', 'OR', 'NY', 'MA', 'CT', 'RI', 'NJ', 'PA', 'MI', 'WI', 'MN'], 'autumn-crocus': LOWER48,
    'chinese-wisteria': LOWER48, 'horse-chestnut': LOWER48, 'english-holly': LOWER48,
    'february-daphne': ['ME', 'NH', 'VT', 'MA', 'NY', 'PA', 'MI', 'WI', 'MN', 'OH', 'WA', 'OR'],
    'crown-flower': ['HI', 'FL'], 'brazilian-pepper': ['FL', 'TX', 'CA', 'HI'],
}


def load_d1():
    eco = json.load(open(ROOT / 'data' / 'regions' / 'ecoregions.json'))
    code2name = {v['code']: k for k, v in eco.items()}
    detail = json.load(open(ROOT / 'data' / 'regions' / 'counties-detail.json'))
    fips_eco, state_eco = {}, defaultdict(set)
    for fips, c in detail.items():
        names = {code2name[e['code']] for e in c.get('ecoregions_present', []) if e.get('share', 0) >= SHARE_MIN
                 and e['code'] in code2name}
        if not names and c.get('ecoregions_present'):
            top = max(c['ecoregions_present'], key=lambda e: e.get('share', 0))
            if top['code'] in code2name:
                names = {code2name[top['code']]}
        if not names and fips.startswith('15'):   # Hawaii: no EPA Level III layer; D1's placeholder region
            names = {code2name['HI']}
        fips_eco[fips] = names
    fips_idx = json.load(open(ROOT / 'data' / 'regions' / 'fips-index.json'))
    for fips, names in fips_eco.items():
        st = fips_idx.get(fips, [None])[0]
        if st:
            state_eco[st] |= names
    return eco, fips_eco, state_eco, fips_idx


def text_note(s):
    main = s.get('harm') or s.get('use') or (s.get('burn') or {}).get('notes', '')
    return f"{main} Where: {s['habitat']}".strip() if s.get('habitat') else main


def main():
    by = merged_species()
    res = json.load(open(RAW / 'resolved.json'))
    eco, fips_eco, state_eco, fips_idx = load_d1()
    plates = {p['key']: p for p in json.load(open(ROOT / 'images' / 'index.json'))['plants']}
    county_dist, species_out = {}, []
    eco_lists = {name: dict(deadly=[], edible=[], firewood=[]) for name in eco}
    unmapped_counties = 0

    for key, s in by.items():
        r = res.get(key)
        states, counties, basis = [], [], None
        if r:
            pid = plants_profile(r['symbol'])['Id']
            states, counties = parse(plants_distribution(pid))
            basis = 'usda-plants-county'
        if s['kind'] == 'fungus':
            states = sorted(s.get('states') or FUNGUS_STATES.get(key, ALL))
            basis = 'literature-coarse'
        planted = sorted(PLANTED.get(key, []))
        ecos, coarse_states = set(), []
        for f in counties:
            if f in fips_eco:
                ecos |= fips_eco[f]
            else:
                unmapped_counties += 1
        county_states = {fips_idx[f][0] for f in counties if f in fips_idx}
        for st in sorted(set(states) | set(planted)):
            if st not in county_states and st in state_eco:
                ecos |= state_eco[st]; coarse_states.append(st)
        if counties:
            county_dist[key] = counties
        ecos = sorted(ecos)
        for g in s['groups']:
            for e in ecos:
                eco_lists[e][g].append(key)
        look = [dict(key=k, how_to_tell=t) for k, t in sorted(s['look'].items())]
        out = dict(
            key=key, group=s['group'], groups=s['groups'], kind=s['kind'],
            scientific=s['sci'], plants_name=(r or {}).get('accepted'), symbol=(r or {}).get('symbol'),
            family=(r or {}).get('family'), common_names=s['common'], risk=s.get('risk'),
            id_features=s['id'],
        )
        if s.get('harm'):
            out['harm'] = s['harm']
        if s.get('use'):
            out['use'] = s['use']
        if s.get('burn'):
            out['burn'] = s['burn']
        out.update(habitat=s.get('habitat', ''), mistaken_for=s.get('mistaken_for', ''), lookalikes=look,
                   distribution=dict(basis=basis, states=sorted(states), county_records=len(counties),
                                     state_coarse=coarse_states, planted_states=planted,
                                     range_note=s.get('range_note')),
                   ecoregions=ecos,
                   plates=len(plates.get(key, {}).get('plates', [])),
                   sources=[SRC[a] for a in s['src']])
        species_out.append(out)

    order = {'deadly': 0, 'edible': 1, 'firewood': 2}
    species_out.sort(key=lambda x: (order[x['group']], x['key']))
    rank = {x['key']: x for x in species_out}

    def sort_list(g, keys):
        if g == 'firewood':
            return sorted(keys, key=lambda k: (HEAT_ORDER[rank[k]['burn']['heat']], k))
        return sorted(keys, key=lambda k: (RISK_ORDER.get(rank[k]['risk'], 3) if rank[k]['group'] == g else 1, k))

    eco_out = {}
    for name, lists in eco_lists.items():
        eco_out[name] = dict(code=eco[name].get('code'), states=eco[name].get('states', []),
                             **{g: sort_list(g, v) for g, v in lists.items()})
    counts = dict(species=len(species_out),
                  by_group={g: sum(1 for x in species_out if g in x['groups']) for g in ('deadly', 'edible', 'firewood')},
                  fungi=sum(1 for x in species_out if x['kind'] == 'fungus'),
                  with_plates=sum(1 for x in species_out if x['plates']),
                  plates=sum(x['plates'] for x in species_out),
                  lookalike_links=sum(len(x['lookalikes']) for x in species_out) // 2)
    method = (
        'Species, identification features, harm, use, burn class and look-alike links were written by worker D2 '
        'from the named sources (USDA PLANTS, USDA ARS Poisonous Plant Research Laboratory, USDA Forest Service, '
        'CDC/NIOSH, FDA, university Extension). Scientific names and symbols are checked against the USDA PLANTS '
        'checklist (plants_name is the PLANTS accepted name where it differs). Distribution is the USDA PLANTS '
        'county and state distribution download; ecoregions are EPA Level III, assigned COARSELY: a species is '
        f'listed for every ecoregion covering at least {int(SHARE_MIN*100)} percent of a county where PLANTS records it, '
        'and, for states where PLANTS gives no county, for every ecoregion in that state (state_coarse). Fungi and '
        'planted ornamentals use hand-set state lists from the literature. A record means documented there, not '
        'common there; no record does not mean absent.')
    (ROOT / 'data' / 'plants').mkdir(parents=True, exist_ok=True)
    json.dump(dict(note=method, generated=str(date.today()), counts=counts,
                   fields={
                       'group': 'deadly | edible | firewood (primary list); groups lists every list the species is in',
                       'risk': 'deadly: lethal | serious | contact; edible: starter | caution | do-not-eat; firewood: null',
                       'burn': '{heat: high|medium|low, season_months, notes}; Extension heat-per-cord class',
                       'lookalikes': 'two-way links: [{key, how_to_tell}]',
                       'plates': 'number of plates in images/index.json (0 = no licence-clear photograph yet)',
                       'sources': 'keys in sources/index.json or sources/additions/D2.json'},
                   species=species_out),
              open(ROOT / 'data' / 'plants' / 'species.json', 'w'), indent=1, ensure_ascii=False)
    json.dump(dict(note='USDA PLANTS county records (5-digit FIPS) per species key; build input for county overrides.',
                   generated=str(date.today()), counties=county_dist),
              open(ROOT / 'data' / 'plants' / 'county-distribution.json', 'w'), separators=(',', ':'))
    json.dump(dict(note=('EPA Level III ecoregion -> plant and tree keys (data/plants/species.json; plates in '
                         'images/index.json). Lists are ordered deadliest / safest / hottest first. ' + method),
                   generated=str(date.today()), sources=[SRC['plants'], SRC['epa-ecoregions']], ecoregions=eco_out),
              open(ROOT / 'data' / 'regions' / 'ecoregion-plants.json', 'w'), indent=1, ensure_ascii=False)
    print(json.dumps(counts))
    print('unmapped county records:', unmapped_counties)
    return species_out, eco_out


if __name__ == '__main__':
    main()

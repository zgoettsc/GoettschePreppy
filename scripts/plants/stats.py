"""Coverage statistics for notes/workers/D2.md."""
import json
from common import ROOT
sp = {s['key']: s for s in json.load(open(ROOT / 'data/plants/species.json'))['species']}
eco = json.load(open(ROOT / 'data/regions/ecoregion-plants.json'))['ecoregions']
d1 = json.load(open(ROOT / 'data/regions/ecoregions.json'))
pilot = [n for n, v in d1.items() if set(v.get('states', [])) & {'SD', 'IL'}]
def row(n):
    v = eco[n]; keys = set(v['deadly']) | set(v['edible']) | set(v['firewood'])
    withp = sum(1 for k in keys if sp[k]['plates'])
    return f"| {n} ({v['code']}) | {len(v['deadly'])} | {len(v['edible'])} | {len(v['firewood'])} | {withp}/{len(keys)} |"
print('PILOT'); [print(row(n)) for n in pilot]
print('ALL'); [print(row(n)) for n in eco if n not in pilot]
miss = [k for k, s in sp.items() if not s['plates']]
print('MISSING', len(miss)); print(', '.join(f"{k}" for k in miss))
from collections import Counter
print(Counter(s['plates'] for s in sp.values()))
idx = json.load(open(ROOT / 'images/index.json'))
print(Counter(p['collection'] for s in idx['plants'] for p in s['plates']))
print(Counter(p['feature'] for s in idx['plants'] for p in s['plates']))

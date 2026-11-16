"""Resolve every authored scientific name to its USDA PLANTS accepted symbol.
Writes build/plants-raw/resolved.json and prints problems."""
import json
from common import load_sources, load_checklist, RAW

D, E, F = load_sources()
by_name, accepted = load_checklist()
# PLANTS still files these under older names; resolve with the PLANTS name, keep the modern name for display.
OVERRIDE = {'meadow-death-camas': 'Zigadenus venenosus', 'mountain-death-camas': 'Zigadenus elegans',
            'fremonts-death-camas': 'Zigadenus fremontii', 'deadly-nightshade': 'Atropa bella-donna',
            'mescal-bean': 'Sophora secundiflora', 'spotted-spurge': 'Chamaesyce maculata',
            'foothill-death-camas': 'Zigadenus paniculatus', 'nuttalls-death-camas': 'Zigadenus nuttallii'}
out, bad = {}, []
for s in D + E + F:
    if s.get('kind') == 'fungus' or s.get('alias_of'):
        continue
    name = OVERRIDE.get(s['key'], s['sci'])
    hits = by_name.get(name.lower())
    if not hits:
        bad.append((s['key'], s['sci'], 'NOT FOUND')); continue
    accs = sorted({h['acc'] for h in hits})
    if len(accs) > 1:
        # prefer the row where the name itself is accepted
        own = [h['acc'] for h in hits if not h['syn']]
        accs = own or accs
    acc = accs[0]
    a = accepted.get(acc, {})
    out[s['key']] = dict(sci_authored=s['sci'], symbol=acc, accepted=a.get('name'), full=a.get('full'),
                         plants_common=a.get('common'), family=a.get('family'),
                         synonym=any(h['syn'] for h in hits if h['acc'] == acc), ambiguous=accs if len(accs) > 1 else None)
    if a.get('name', '').lower() != name.lower() or len(accs) > 1:
        bad.append((s['key'], s['sci'], f"-> {acc} {a.get('name')} ({a.get('common')}) {'AMBIG '+str(accs) if len(accs)>1 else ''}"))
json.dump(out, open(RAW / 'resolved.json', 'w'), indent=1)
print(len(out), 'resolved')
for b in bad: print(*b)

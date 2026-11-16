"""Parse PLANTS distribution CSVs -> states and county FIPS per species key."""
import csv, io, json
from common import RAW, STATE_ABBR, plants_profile, plants_distribution

def parse(csv_text):
    lines = csv_text.splitlines()
    i = next(n for n, l in enumerate(lines) if l.startswith('Symbol,'))
    states, counties = set(), set()
    for r in csv.DictReader(io.StringIO('\n'.join(lines[i:]))):
        if r['Country'] != 'United States':
            continue
        st = STATE_ABBR.get(r['State'])
        if not st:
            continue
        states.add(st)
        if r['County'] and r['County FIP']:
            counties.add(r['State FIP'].zfill(2) + r['County FIP'].zfill(3))
    return sorted(states), sorted(counties)

def all_distributions():
    res = json.load(open(RAW / 'resolved.json'))
    out = {}
    for k, v in res.items():
        pid = plants_profile(v['symbol'])['Id']
        st, co = parse(plants_distribution(pid))
        out[k] = dict(symbol=v['symbol'], plant_id=pid, states=st, counties=co)
    return out

if __name__ == '__main__':
    d = all_distributions()
    json.dump(d, open(RAW / 'distribution.json', 'w'))
    unknown = set()
    print(len(d), 'species;', sum(len(v['counties']) for v in d.values()), 'county records')
    print('no US states:', [k for k, v in d.items() if not v['states']])
    pilot = [k for k, v in d.items() if 'SD' in v['states'] or 'IL' in v['states']]
    print('pilot (SD or IL):', len(pilot))

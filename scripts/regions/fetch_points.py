#!/usr/bin/env python3
"""Per-county point queries, cached under build/regions-raw/api/ (re-runs only fill gaps).

    python3 scripts/regions/fetch_points.py [epqs] [power] [acis] [gridelev]

- epqs:  USGS 3D Elevation Program, Elevation Point Query Service: ground elevation (ft) at each
         county's Census internal point.
- power: NASA POWER climatology (2001-2025), solar irradiance on a south-facing panel tilted at
         the site latitude and on a horizontal surface, kWh/m2/day (= peak sun hours), one query
         per 1-degree cell (the native resolution of the source) containing a county point.
- gridelev: fallback elevation where USGS has not answered: the PRISM 4-km grid-cell elevation
         served by ACIS GridData (contiguous states only).
- acis:  NOAA Regional Climate Centers' ACIS: period-of-record extreme daily low and high for every
         climate station that build.py selected (reads build/regions-raw/api/acis_wanted.json).
"""
import json, os, sys, subprocess, math, time, zipfile
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
RAW = os.path.join(ROOT, 'build', 'regions-raw')
API = os.path.join(RAW, 'api')
EPQS = 'https://epqs.nationalmap.gov/v1/json?x={lon}&y={lat}&units=Feet&wkid=4326&includeDate=false'
POWER = ('https://power.larc.nasa.gov/api/temporal/climatology/point?parameters=SI_EF_TILTED_SURFACE'
         '&community=RE&longitude={lon}&latitude={lat}&format=JSON')
ACIS = 'https://data.rcc-acis.org/MultiStnData'


def get(url, data=None, timeout=120):
    cmd = ['curl', '-sS', '--fail', '-m', str(timeout), url]
    if data is not None:
        cmd += ['-X', 'POST', '-H', 'Content-Type: application/json', '-d', json.dumps(data)]
    for i in range(4):
        r = subprocess.run(cmd, capture_output=True)
        if r.returncode == 0:
            try:
                return json.loads(r.stdout)
            except ValueError:
                pass
        time.sleep(2 * (i + 1))
    return None


def counties():
    z = zipfile.ZipFile(os.path.join(RAW, 'gaz_counties.zip'))
    lines = z.read(z.namelist()[0]).decode('latin1').splitlines()
    head = [h.strip() for h in lines[0].split('\t')]
    out = []
    for line in lines[1:]:
        r = dict(zip(head, [c.strip() for c in line.split('\t')]))
        if r['GEOID'][:2] in ('60', '66', '69', '72', '78'):
            continue
        out.append((r['GEOID'], float(r['INTPTLAT']), float(r['INTPTLONG'])))
    return out


class Cache:
    def __init__(self, name):
        self.path = os.path.join(API, name)
        self.d = json.load(open(self.path)) if os.path.exists(self.path) else {}

    def save(self):
        tmp = self.path + '.tmp'
        json.dump(self.d, open(tmp, 'w'), indent=0, sort_keys=True)
        os.replace(tmp, self.path)


def run_epqs():
    c = Cache('epqs.json')
    todo = [(f, la, lo) for f, la, lo in counties() if f not in c.d or c.d[f] is None]

    def one(t):
        f, la, lo = t
        j = get(EPQS.format(lat=la, lon=lo), timeout=60)
        try:
            v = float(j['value'])
            return f, (None if v < -1000 else round(v, 1))
        except Exception:
            return f, None
    with ThreadPoolExecutor(16) as ex:
        for i, (f, v) in enumerate(ex.map(one, todo)):
            c.d[f] = v
            if i % 200 == 0:
                c.save(); print('epqs', i, '/', len(todo), flush=True)
    c.save()
    print('epqs done; missing', sum(1 for v in c.d.values() if v is None))


def run_gridelev():
    """Fallback elevation (ft): PRISM 4-km grid-cell elevation from ACIS GridData (CONUS only)."""
    c = Cache('gridelev.json')
    todo = [(f, la, lo) for f, la, lo in counties() if f not in c.d and f[:2] not in ('02', '15')]

    def one(t):
        f, la, lo = t
        j = get('https://data.rcc-acis.org/GridData', {'loc': f'{lo},{la}', 'grid': '21', 'sdate': '2020-01-01',
                                                      'edate': '2020-01-01', 'elems': 'maxt', 'meta': 'll,elev'}, timeout=60)
        try:
            return f, float(j['meta']['elev'])
        except Exception:
            return f, None
    with ThreadPoolExecutor(8) as ex:
        for i, (f, v) in enumerate(ex.map(one, todo)):
            c.d[f] = v
            if i % 500 == 0:
                c.save(); print('gridelev', i, '/', len(todo), flush=True)
    c.save()


def cell(la, lo):
    return math.floor(la) + 0.5, math.floor(lo) + 0.5


def run_power():
    c = Cache('power.json')
    cells = sorted({cell(la, lo) for _, la, lo in counties()})
    todo = [x for x in cells if f'{x[0]},{x[1]}' not in c.d]

    def one(x):
        j = get(POWER.format(lat=x[0], lon=x[1]))
        try:
            p = j['properties']['parameter']
            keep = {k: {m: p[k][m] for m in ('DEC', 'JUN', 'ANN')} for k in
                    ('SI_TILTED_AVG_LATITUDE', 'SI_TILTED_AVG_HORIZONTAL', 'SI_TILTED_AVG_OPTIMAL')}
            return x, keep
        except Exception:
            return x, None
    with ThreadPoolExecutor(4) as ex:
        for i, (x, v) in enumerate(ex.map(one, todo)):
            if v is not None:
                c.d[f'{x[0]},{x[1]}'] = v
            if i % 100 == 0:
                c.save(); print('power', i, '/', len(todo), flush=True)
    c.save()
    print('power done', len(c.d), 'of', len(cells))


def run_acis():
    c = Cache('acis.json')
    wanted = json.load(open(os.path.join(API, 'acis_wanted.json')))
    todo = [s for s in wanted if s not in c.d]
    elems = [{'name': 'mint', 'interval': 'dly', 'duration': 'dly', 'smry': {'reduce': 'min', 'add': 'date'}, 'smry_only': 1},
             {'name': 'maxt', 'interval': 'dly', 'duration': 'dly', 'smry': {'reduce': 'max', 'add': 'date'}, 'smry_only': 1}]
    batches = [todo[i:i + 40] for i in range(0, len(todo), 40)]

    def one(b):
        j = get(ACIS, {'sids': ','.join(b), 'sdate': '1850-01-01', 'edate': '2025-12-31', 'elems': elems,
                       'meta': 'sids,name,valid_daterange'}, timeout=300)
        res = {}
        for row in (j or {}).get('data', []):
            sids = [s.split()[0] for s in row['meta'].get('sids', [])]
            hit = next((s for s in b if s in sids), None)
            if hit:
                res[hit] = {'name': row['meta'].get('name'), 'por': row['meta'].get('valid_daterange'),
                            'min': row.get('smry', [None, None])[0], 'max': row.get('smry', [None, None])[1]}
        return b, res, j is not None
    with ThreadPoolExecutor(3) as ex:
        for i, (b, res, ok) in enumerate(ex.map(one, batches)):
            for s in b:
                if s in res:
                    c.d[s] = res[s]
                elif ok:
                    c.d[s] = None  # ACIS answered but does not know this station
            if i % 10 == 0:
                c.save(); print('acis', i, '/', len(batches), flush=True)
    c.save()
    print('acis done', sum(1 for v in c.d.values() if v), 'stations with extremes')


if __name__ == '__main__':
    os.makedirs(API, exist_ok=True)
    what = sys.argv[1:] or ['epqs', 'power', 'acis']
    for w in what:
        {'epqs': run_epqs, 'power': run_power, 'acis': run_acis, 'gridelev': run_gridelev}[w]()

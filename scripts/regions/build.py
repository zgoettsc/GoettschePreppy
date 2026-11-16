#!/usr/bin/env python3
"""Build data/regions/ for every county of the 50 states and DC (decision G1).

    python3 scripts/regions/fetch.py          # raw files into build/regions-raw/ (cached)
    python3 scripts/regions/build.py          # runs the per-county API pulls it needs, then writes data/regions/
    python3 scripts/regions/build.py --skip=epqs   # use cached answers only for the named pulls

Outputs (all JSON, keyed by 5-digit county FIPS or 2-letter state code; formats in notes/workers/D1.md):
    data/regions/counties.json         context-ready region object per county (schema/context.json region.*)
    data/regions/counties-detail.json  provenance per county: stations, distances, raw NRI classes, all CWAs
    data/regions/states.json           per state: name, EM agency, counties, NWS offices, ecoregions, climate by area
    data/regions/nws-offices.json      per NWS forecast office (CWA code)
    data/regions/ecoregions.json       per EPA Level III ecoregion present in the data
    data/regions/national.json         national constants (poison control) and method notes
    data/regions/sources.json          datasets used (title, publisher, date, licence class; no URLs)

Python 3 standard library plus numpy. No other dependencies.
"""
import csv, io, json, math, os, re, sys, tarfile, zipfile
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import geo  # noqa: E402
import fetch_points  # noqa: E402

ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
RAW = os.path.join(ROOT, 'build', 'regions-raw')
API = os.path.join(RAW, 'api')
OUT = os.path.join(ROOT, 'data', 'regions')

STATES = {
    '01': ('AL', 'Alabama'), '02': ('AK', 'Alaska'), '04': ('AZ', 'Arizona'), '05': ('AR', 'Arkansas'),
    '06': ('CA', 'California'), '08': ('CO', 'Colorado'), '09': ('CT', 'Connecticut'), '10': ('DE', 'Delaware'),
    '11': ('DC', 'District of Columbia'), '12': ('FL', 'Florida'), '13': ('GA', 'Georgia'), '15': ('HI', 'Hawaii'),
    '16': ('ID', 'Idaho'), '17': ('IL', 'Illinois'), '18': ('IN', 'Indiana'), '19': ('IA', 'Iowa'),
    '20': ('KS', 'Kansas'), '21': ('KY', 'Kentucky'), '22': ('LA', 'Louisiana'), '23': ('ME', 'Maine'),
    '24': ('MD', 'Maryland'), '25': ('MA', 'Massachusetts'), '26': ('MI', 'Michigan'), '27': ('MN', 'Minnesota'),
    '28': ('MS', 'Mississippi'), '29': ('MO', 'Missouri'), '30': ('MT', 'Montana'), '31': ('NE', 'Nebraska'),
    '32': ('NV', 'Nevada'), '33': ('NH', 'New Hampshire'), '34': ('NJ', 'New Jersey'), '35': ('NM', 'New Mexico'),
    '36': ('NY', 'New York'), '37': ('NC', 'North Carolina'), '38': ('ND', 'North Dakota'), '39': ('OH', 'Ohio'),
    '40': ('OK', 'Oklahoma'), '41': ('OR', 'Oregon'), '42': ('PA', 'Pennsylvania'), '44': ('RI', 'Rhode Island'),
    '45': ('SC', 'South Carolina'), '46': ('SD', 'South Dakota'), '47': ('TN', 'Tennessee'), '48': ('TX', 'Texas'),
    '49': ('UT', 'Utah'), '50': ('VT', 'Vermont'), '51': ('VA', 'Virginia'), '53': ('WA', 'Washington'),
    '54': ('WV', 'West Virginia'), '55': ('WI', 'Wisconsin'), '56': ('WY', 'Wyoming'),
}
ST_NAME = {a: n for a, n in STATES.values()}

# Kit hazard -> NRI hazard prefix(es). Where two NRI hazards feed one kit hazard, the higher rating wins.
HAZARDS = [
    ('tornado', 'Tornado', ['TRND']),
    ('blizzard', 'Blizzard and winter storm', ['WNTW']),
    ('ice_storm', 'Ice storm', ['ISTM']),
    ('flood', 'Flood (river and coastal)', ['IFLD', 'CFLD']),
    ('wildfire', 'Wildfire', ['WFIR']),
    ('earthquake', 'Earthquake', ['ERQK']),
    ('hurricane', 'Hurricane', ['HRCN']),
    ('extreme_heat', 'Extreme heat', ['HWAV']),
    ('extreme_cold', 'Extreme cold', ['CWAV']),
    ('drought', 'Drought', ['DRGT']),
    ('volcano', 'Volcano', ['VLCN']),
    ('tsunami', 'Tsunami', ['TSUN']),
    ('landslide', 'Landslide', ['LNDS']),
]
# NRI hazard-type Risk Index rating class -> kit 1..3 (documented in national.json and notes/workers/D1.md)
NRI_MAP = {
    'Very High': 3, 'Relatively High': 3,
    'Relatively Moderate': 2,
    'Relatively Low': 1, 'Very Low': 1,
    'No Rating': 1, 'Not Applicable': 1, 'Insufficient Data': 1, 'No Expected Annual Losses': 1,
}
RATING_TEXT = {3: 'High', 2: 'Moderate', 1: 'Low'}
MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


def jdump(name, obj):
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, name), 'w') as f:
        json.dump(obj, f, indent=1, sort_keys=False, ensure_ascii=False)
        f.write('\n')


def load_counties():
    z = zipfile.ZipFile(os.path.join(RAW, 'gaz_counties.zip'))
    lines = z.read(z.namelist()[0]).decode('latin1').splitlines()
    head = [h.strip() for h in lines[0].split('\t')]
    out = {}
    for line in lines[1:]:
        r = dict(zip(head, [c.strip() for c in line.split('\t')]))
        if r['GEOID'][:2] not in STATES:
            continue
        out[r['GEOID']] = {'fips': r['GEOID'], 'state': r['USPS'], 'name': r['NAME'],
                           'lat': float(r['INTPTLAT']), 'lon': float(r['INTPTLONG']),
                           'land_sqmi': float(r['ALAND_SQMI'])}
    return out


def num(v):
    v = (v or '').strip()
    if not v:
        return None
    try:
        x = float(v)
    except ValueError:
        return v
    return x


def load_normals():
    cache = os.path.join(RAW, 'normals_parsed.json')
    if os.path.exists(cache):
        return json.load(open(cache))
    st = {}
    with tarfile.open(os.path.join(RAW, 'normals_ann.tar.gz')) as tf:
        for m in tf:
            if not m.isfile():
                continue
            rows = list(csv.DictReader(io.StringIO(tf.extractfile(m).read().decode('latin1'))))
            if not rows:
                continue
            r = rows[0]
            sid = r['STATION'].strip()
            st[sid] = {'name': r['NAME'].strip(), 'lat': float(r['LATITUDE']), 'lon': float(r['LONGITUDE']),
                       'elev_m': num(r['ELEVATION']),
                       'prcp': num(r.get('ANN-PRCP-NORMAL')), 'snow': num(r.get('ANN-SNOW-NORMAL')),
                       'lst': (r.get('ANN-TMIN-PRBLST-T32FP50') or '').strip(),
                       'fst': (r.get('ANN-TMIN-PRBFST-T32FP50') or '').strip(),
                       'gsl': num(r.get('ANN-TMIN-PRBGSL-T32FP50'))}
    with tarfile.open(os.path.join(RAW, 'normals_mly.tar.gz')) as tf:
        for m in tf:
            if not m.isfile():
                continue
            rows = list(csv.DictReader(io.StringIO(tf.extractfile(m).read().decode('latin1'))))
            if not rows:
                continue
            sid = rows[0]['STATION'].strip()
            s = st.setdefault(sid, {'name': rows[0]['NAME'].strip(), 'lat': float(rows[0]['LATITUDE']),
                                    'lon': float(rows[0]['LONGITUDE']), 'elev_m': num(rows[0]['ELEVATION'])})
            for r in rows:
                mo = r['month'].strip()
                if mo == '01':
                    s['jan_tmin'] = num(r.get('MLY-TMIN-NORMAL'))
                elif mo == '07':
                    s['jul_tmax'] = num(r.get('MLY-TMAX-NORMAL'))
    for s in st.values():
        for k in ('prcp', 'snow', 'jan_tmin', 'jul_tmax', 'gsl', 'elev_m'):
            v = s.get(k)
            if isinstance(v, float) and v <= -7000:
                s[k] = 0.0 if (v == -7777 and k in ('prcp', 'snow')) else None
            elif not isinstance(v, float):
                s[k] = None
    json.dump(st, open(cache, 'w'))
    return st


def frost_text(v):
    m = re.match(r'^(\d\d)/(\d\d)$', v or '')
    return f'{MONTHS[int(m.group(1)) - 1]} {int(m.group(2))}' if m else None


def has(s, kind):
    if kind == 'temp':
        return s.get('jan_tmin') is not None and s.get('jul_tmax') is not None
    if kind == 'frost':
        return s.get('gsl') is not None and (frost_text(s.get('lst')) or s.get('lst', '').startswith('-9999'))
    return s.get(kind) is not None


class StationPicker:
    """Nearest station with the needed normals, distance penalised by elevation difference."""
    def __init__(self, stations):
        import numpy as np
        self.np = np
        self.ids = list(stations)
        self.st = stations
        self.lat = np.radians(np.array([stations[k]['lat'] for k in self.ids]))
        self.lon = np.radians(np.array([stations[k]['lon'] for k in self.ids]))
        self.elev = np.array([stations[k]['elev_m'] if stations[k]['elev_m'] is not None else np.nan for k in self.ids])
        self.mask = {k: np.array([bool(has(stations[i], k)) for i in self.ids]) for k in ('temp', 'frost', 'prcp', 'snow')}

    def pick(self, lat, lon, elev_m, kind, n=1, max_km=None):
        np = self.np
        p1, l1 = math.radians(lat), math.radians(lon)
        h = np.sin((self.lat - p1) / 2) ** 2 + math.cos(p1) * np.cos(self.lat) * np.sin((self.lon - l1) / 2) ** 2
        d = 6371.0 * 2 * np.arcsin(np.sqrt(h))
        pen = np.where(np.isnan(self.elev) | (elev_m is None), 0.0, np.abs(self.elev - (elev_m or 0)) / 10.0)
        score = np.where(self.mask[kind], d + pen, np.inf)
        if max_km is not None:
            score = np.where(d <= max_km, score, np.inf)
        idx = np.argsort(score)[:n]
        return [(self.ids[i], float(d[i]), float(score[i])) for i in idx if np.isfinite(score[i])]


def zone_of(t):
    if t is None:
        return None
    k = (t + 60) / 10.0
    n = math.floor(k) + 1
    half = 'a' if (k - math.floor(k)) < 0.5 else 'b'
    return f'{n}{half}'


def zone_key(z):
    return int(z[:-1]) * 2 + (0 if z[-1] == 'a' else 1)


def lattice(bbox, rings_test, target=60):
    """Sample points on a regular lattice inside a polygon (rings_test(x, y) -> bool)."""
    x0, y0, x1, y1 = bbox
    area = max((x1 - x0) * (y1 - y0), 1e-6)
    step = max(math.sqrt(area / (target * 1.6)), 0.004)
    pts, y = [], y0 + step / 2
    while y < y1:
        x = x0 + step / 2
        while x < x1:
            if rings_test(x, y):
                pts.append((x, y))
            x += step
        y += step
    return pts


def main():
    counties = load_counties()
    print('counties', len(counties))

    # --- per-county point pulls (cached) -------------------------------------------------------
    os.makedirs(API, exist_ok=True)
    skip = set(','.join(a[7:] for a in sys.argv[1:] if a.startswith('--skip=')).split(','))
    if 'epqs' not in skip:
        fetch_points.run_epqs()
    if 'gridelev' not in skip:
        fetch_points.run_gridelev()
    if 'power' not in skip:
        fetch_points.run_power()
    epqs_raw = json.load(open(os.path.join(API, 'epqs.json')))
    gridelev = json.load(open(os.path.join(API, 'gridelev.json')))
    epqs, elev_src = {}, {}
    for f in counties:
        if epqs_raw.get(f) is not None:
            epqs[f], elev_src[f] = epqs_raw[f], 'USGS 3DEP point'
        elif gridelev.get(f) is not None:
            epqs[f], elev_src[f] = gridelev[f], 'PRISM 4-km grid cell (ACIS)'
    power = json.load(open(os.path.join(API, 'power.json')))

    # --- normals and station choice --------------------------------------------------------------
    stations = load_normals()
    picker = StationPicker(stations)
    pick = {}
    wanted = set()
    for f, c in counties.items():
        el_ft = epqs.get(f)
        el_m = el_ft * 0.3048 if el_ft is not None else None
        p = {k: picker.pick(c['lat'], c['lon'], el_m, k, n=(4 if k == 'temp' else 1),
                            max_km=(150 if k == 'snow' else None)) for k in ('temp', 'frost', 'prcp', 'snow')}
        pick[f] = p
        wanted.update(s for s, _, _ in p['temp'])
    json.dump(sorted(wanted), open(os.path.join(API, 'acis_wanted.json'), 'w'))
    if 'acis' not in skip:
        fetch_points.run_acis()
    acis = json.load(open(os.path.join(API, 'acis.json')))

    # --- hardiness zone grids --------------------------------------------------------------------
    grids = {'us': geo.BilGrid(os.path.join(RAW, 'phzm_us_grid_2023.zip'), 'phzm_us_grid_2023'),
             'AK': geo.BilGrid(os.path.join(RAW, 'phzm_ak_grid_2023.zip'), 'phzm_ak_grid_2023'),
             'HI': geo.BilGrid(os.path.join(RAW, 'phzm_hi_grid_2023.zip'), 'phzm_hi_grid_2023')}

    # --- NWS counties / CWA ---------------------------------------------------------------------
    nws_layer = geo.read_layer(os.path.join(RAW, 'nws_counties.zip'), 'c_16ap26')
    nws_idx = geo.PolyIndex(nws_layer)
    nws_by_fips = defaultdict(list)
    for i, row in enumerate(nws_idx.rows):
        nws_by_fips[row['FIPS']].append(i)
    cwa_rows = {r['CWA']: r for r, _ in geo.read_layer(os.path.join(RAW, 'nws_cwa.zip'), 'w_16ap26')}

    # CT planning regions (09110..09190) -> legacy counties (09001..09015) for NWS/NWR, from the
    # Census crosswalk of county subdivisions.
    ct = defaultdict(set)
    with open(os.path.join(RAW, 'ct_crosswalk.txt'), encoding='utf-8-sig') as fh:
        rows = list(csv.reader(fh, delimiter='|'))
    for r in rows[1:]:
        if len(r) > 4 and r[1].strip().isdigit():
            ct['09' + r[3].strip()].add('09' + r[1].strip())

    # --- NWR county coverage ----------------------------------------------------------------------
    js = open(os.path.join(RAW, 'nwr_ccl.js'), encoding='latin1').read()
    arrays = defaultdict(dict)
    for name, i, val in re.findall(r'^(\w+)\[(\d+)\] = "(.*)";\s*$', js, re.M):
        arrays[name][int(i)] = val
    nwr = defaultdict(list)
    for i in sorted(arrays['SAME']):
        g = lambda k: arrays[k].get(i, '')
        nwr[g('SAME')[1:]].append({'call': g('CALLSIGN'), 'freq': g('FREQ'), 'same': g('SAME'),
                                   'site': g('SITENAME'), 'site_state': g('SITESTATE'), 'power_w': g('PWR'),
                                   'status': g('STATUS'), 'wfo': g('WFO').replace('|', ', '),
                                   'remarks': g('REMARKS')})

    # --- NRI ----------------------------------------------------------------------------------------
    nri = {r['STCOFIPS']: r for r in json.load(open(os.path.join(RAW, 'nri_counties.json')))}
    nri_ver = Counter(r.get('NRI_VER') for r in nri.values()).most_common(1)[0][0]

    # --- EPA Level III ecoregions -----------------------------------------------------------------
    alb_us = geo.Albers(23.0, -96.0, 29.5, 45.5)
    alb_ak = geo.Albers(50.0, -154.0, 55.0, 65.0)
    eco_us = geo.PolyIndex(geo.read_layer(os.path.join(RAW, 'us_eco_l3.zip'), 'us_eco_l3'))
    eco_ak = geo.PolyIndex(geo.read_layer(os.path.join(RAW, 'ak_eco_l3.zip'), 'ak_eco_l3'))

    def eco_at(state, lon, lat):
        if state == 'HI':
            return None
        idx, alb = (eco_ak, alb_ak) if state == 'AK' else (eco_us, alb_us)
        x, y = alb.fwd(lon, lat)
        i = idx.locate(x, y)
        if i is None:
            i = idx.nearest(x, y, 15000)
        return None if i is None else idx.rows[i]

    ecoregions = {}

    def eco_key(row):
        code = row['US_L3CODE']
        if code not in ecoregions:
            ecoregions[code] = {'code': code, 'name': row['US_L3NAME'], 'na_code': row.get('NA_L3CODE'),
                                'level2': (row.get('NA_L2NAME') or '').title(),
                                'level1': (row.get('NA_L1NAME') or '').title(), 'states': set()}
        return code

    # --- assemble -------------------------------------------------------------------------------------
    out, detail = {}, {}
    for n, (f, c) in enumerate(sorted(counties.items())):
        st = c['state']
        lat, lon = c['lat'], c['lon']
        el_ft = epqs.get(f)
        d = {'fips': f, 'state': st, 'lat': lat, 'lon': lon, 'point': 'Census 2024 internal point',
             'elevation_source': elev_src.get(f)}

        # climate
        p = pick[f]
        temp = p['temp'][0] if p['temp'] else None
        rec = None
        for sid, dist, _ in p['temp']:
            a = acis.get(sid)
            if not a or not a.get('min') or not a.get('max') or a['min'][0] in ('M', '') or a['max'][0] in ('M', ''):
                continue
            try:
                yrs = int(a['por'][0][1][:4]) - int(a['por'][0][0][:4])
            except Exception:
                yrs = 0
            if yrs >= 30 and dist <= 80:
                rec = (sid, dist, a, yrs); break
        fr = p['frost'][0] if p['frost'] else None
        pr = p['prcp'][0] if p['prcp'] else None
        sn = p['snow'][0] if p['snow'] else None
        # Keep one coherent station where it is nearly as good: use the temperature station's own
        # frost, precipitation and snow normals when its score is within 25 of the best station's.
        if temp:
            tst = stations[temp[0]]
            if fr and has(tst, 'frost') and temp[2] <= fr[2] + 25:
                fr = temp
            if pr and tst.get('prcp') is not None and temp[2] <= pr[2] + 25:
                pr = temp
            if sn and tst.get('snow') is not None and temp[2] <= sn[2] + 25:
                sn = temp
        S = lambda t: stations[t[0]] if t else {}
        ts, fs, ps, ss = S(temp), S(fr), S(pr), S(sn)
        lst, fst = frost_text(fs.get('lst')), frost_text(fs.get('fst'))
        frost_free = bool(fs) and not lst
        clim = {
            'jan_low_f': round(ts['jan_tmin']) if ts else None,
            'jul_high_f': round(ts['jul_tmax']) if ts else None,
            'record_low_f': int(float(rec[2]['min'][0])) if rec else None,
            'record_high_f': int(float(rec[2]['max'][0])) if rec else None,
            'precip_in': round(ps['prcp'], 1) if ps else None,
            'snow_in': (round(ss['snow']) if ss else (0 if lat < 31 or st == 'HI' else None)),
            'last_frost': ('None in most years' if frost_free else lst),
            'first_frost': ('None in most years' if frost_free else fst),
            'growing_days': (int(fs['gsl']) if fs and fs.get('gsl') is not None else None),
        }
        stn = lambda t: None if not t else {'id': t[0], 'name': stations[t[0]]['name'], 'km': round(t[1], 1),
                                            'elev_ft': None if stations[t[0]]['elev_m'] is None else round(stations[t[0]]['elev_m'] / 0.3048)}
        d['stations'] = {'temperature': stn(temp), 'frost': stn(fr), 'precip': stn(pr), 'snow': stn(sn),
                         'records': None if not rec else {**stn(rec[:2]), 'por_years': rec[3],
                                                          'record_low_date': rec[2]['min'][1], 'record_high_date': rec[2]['max'][1]}}

        # hardiness zone
        grid = grids['AK'] if st == 'AK' else grids['HI'] if st == 'HI' else grids['us']
        t = grid.value_near(lon, lat)
        zone = zone_of(t)
        # zone range over the county polygon (AWIPS county shape); CT planning regions use the point only
        zr = []
        polys = nws_by_fips.get(f, [])
        for i in polys:
            x0, y0, x1, y1 = nws_idx.bbox[i]
            for (x, y) in lattice((x0, y0, x1, y1), lambda x, y, i=i: nws_idx.contains(i, x, y)):
                z = zone_of(grid.value(x, y))
                if z:
                    zr.append(z)
        zr = sorted(set(zr + ([zone] if zone else [])), key=zone_key)
        d['zone_temp_f'] = None if t is None else round(t, 1)
        d['zone_range'] = [zr[0], zr[-1]] if zr else None

        # NWS office(s)
        legacy = sorted(ct[f]) if f in ct else [f]
        cwas = []
        for lf in legacy:
            for i in nws_by_fips.get(lf, []):
                cwas.append(nws_idx.rows[i]['CWA'])
        hit = nws_idx.locate(lon, lat)
        primary = nws_idx.rows[hit]['CWA'] if hit is not None and nws_idx.rows[hit]['STATE'] == st else (Counter(cwas).most_common(1)[0][0] if cwas else None)
        cwas = [primary] + sorted(set(cwas) - {primary}) if primary else sorted(set(cwas))
        d['cwa'] = cwas
        office = lambda w: f"NWS {cwa_rows[w]['CITY']}, {cwa_rows[w]['ST']}" if w in cwa_rows else f'NWS {w}'

        # NOAA Weather Radio
        tx, seen = [], set()
        for lf in legacy:
            for r in nwr.get(lf, []):
                k = (r['call'], r['same'])
                if k in seen:
                    continue
                seen.add(k); tx.append(r)
        d['nwr_full'] = tx

        # hazards
        h = nri.get(f, {})
        hz, hz_raw = [], {}
        for key, label, pre in HAZARDS:
            best, cls = 1, []
            for pfx in pre:
                v = h.get(f'{pfx}_RISKR')
                cls.append(f'{pfx}:{v}')
                best = max(best, NRI_MAP.get(v, 1))
            hz.append({'name': label, 'rating': best, 'rating_text': RATING_TEXT[best]})
            hz_raw[key] = {p_: {'risk': h.get(f'{p_}_RISKR'), 'eal': h.get(f'{p_}_EALR'),
                                'hlr': h.get(f'{p_}_HLRR'), 'afreq': h.get(f'{p_}_AFREQ')} for p_ in pre}
        d['nri'] = hz_raw
        d['nri_overall'] = h.get('RISK_RATNG')

        # ecoregion
        er = eco_at(st, lon, lat)
        eco_code = eco_key(er) if er else None
        present = Counter()
        for i in polys:
            x0, y0, x1, y1 = nws_idx.bbox[i]
            for (x, y) in lattice((x0, y0, x1, y1), lambda x, y, i=i: nws_idx.contains(i, x, y), target=25):
                r2 = eco_at(st, x, y)
                if r2:
                    present[eco_key(r2)] += 1
        if eco_code:
            present[eco_code] += 0
        tot = sum(present.values()) or 1
        d['ecoregions_present'] = [{'code': k, 'share': round(v / tot, 2)} for k, v in present.most_common()]
        for k in present:
            ecoregions[k]['states'].add(st)

        # sun hours (NASA POWER, 1-degree cell)
        cl = fetch_points.cell(lat, lon)
        pw = power.get(f'{cl[0]},{cl[1]}')
        sun = None
        if pw:
            lt, hzn = pw['SI_TILTED_AVG_LATITUDE'], pw['SI_TILTED_AVG_HORIZONTAL']
            sun = {'dec': round(lt['DEC'], 1), 'jun': round(lt['JUN'], 1),
                   'dec_flat': round(hzn['DEC'], 1), 'jun_flat': round(hzn['JUN'], 1)}
        d['sun'] = sun
        d['sun_cell'] = list(cl)

        name_full = c['name']
        out[f] = {
            'fips': f, 'state': st, 'state_name': ST_NAME[st], 'county': name_full,
            'lat': round(lat, 4), 'lon': round(lon, 4),
            'elevation_ft': None if el_ft is None else int(round(el_ft, -1)),
            'zone': zone,
            **clim,
            'ecoregion': ecoregions[eco_code]['name'] if eco_code else ('Hawaiian Islands (not mapped at EPA Level III)' if st == 'HI' else None),
            'ecoregion_code': eco_code if eco_code else ('HI' if st == 'HI' else None),
            'nws_office': office(cwas[0]) if cwas else None,
            'nws_cwa': cwas[0] if cwas else None,
            'nwr': [{'call': r['call'], 'freq': r['freq'], 'same': r['same']} for r in tx],
            'state_em': None,  # filled below
            'hazards': hz,
            'sun_hours_dec': sun['dec'] if sun else None,
            'sun_hours_jun': sun['jun'] if sun else None,
            'plants': {'deadly': [], 'edible': []},
            'trees': {'firewood': []},
        }
        detail[f] = d
        if n % 250 == 0:
            print('assembled', n, flush=True)

    # --- states ---------------------------------------------------------------------------------------
    em = json.load(open(os.path.join(HERE, 'state_em.json')))
    states = {}
    for code, (ab, name) in sorted(STATES.items(), key=lambda kv: kv[1][1]):
        fs = sorted(k for k, v in out.items() if v['state'] == ab)
        for k in fs:
            out[k]['state_em'] = em[ab]['name']
        states[ab] = {'code': ab, 'fips': code, 'name': name, 'state_em': em[ab]['name'],
                      'state_em_basis': em[ab]['basis'], 'counties': fs,
                      'nws_offices': sorted({w for k in fs for w in detail[k]['cwa']}),
                      'ecoregions': sorted({e['code'] for k in fs for e in detail[k]['ecoregions_present']}, key=lambda s: (len(s), s))}

    offices = {}
    for w in sorted({w for d in detail.values() for w in d['cwa']}):
        r = cwa_rows.get(w, {})
        offices[w] = {'code': w, 'name': f"NWS {r.get('CITY', w)}, {r.get('ST', '')}".rstrip(', '),
                      'city': r.get('CITY'), 'state': r.get('ST'), 'region': r.get('REGION'),
                      'counties': sorted(k for k, d in detail.items() if w in d['cwa'])}

    for e in ecoregions.values():
        e['states'] = sorted(e['states'])

    national = {
        'poison_control': {'name': 'Poison Help line (America\'s Poison Centers)', 'phone': '1-800-222-1222',
                           'note': 'Free, confidential, 24 hours, anywhere in the United States; connects to the local poison center.'},
        'built': '2026-11-16',
        'counts': {'counties': len(out), 'states': len(states)},
        'nri_version': nri_ver,
        'methods': {
            'point': 'Each county is represented by its Census 2024 Gazetteer internal point (a point inside the county near its centre), not the county seat.',
            'elevation': 'USGS 3DEP ground elevation at the internal point, rounded to 10 ft.',
            'climate': 'NOAA NCEI U.S. Climate Normals 1991-2020. For each value the station chosen is the one with that normal whose score (distance in km + elevation difference in m / 10) is lowest; station ids and distances are in counties-detail.json.',
            'frost': 'Median (50 percent probability) last spring and first fall dates of 32 F, and the median 32 F freeze-free period, from the same normals. "None in most years" where the station records no 32 F freeze in most years.',
            'records': 'Lowest and highest daily temperature in the period of record of the nearest of the four best temperature stations that has at least 30 years of record and lies within 80 km, from NOAA RCC ACIS; record dates in counties-detail.json.',
            'zone': 'USDA 2023 Plant Hardiness Zone at the internal point from the official PRISM grid (mean annual extreme minimum temperature, 1991-2020); zone_range in counties-detail.json samples the whole county.',
            'hazards': 'FEMA National Risk Index, hazard-type Risk Index rating per county. Very High and Relatively High -> 3 (High); Relatively Moderate -> 2 (Moderate); Relatively Low, Very Low, No Rating, Not Applicable, Insufficient Data -> 1 (Low). Blizzard uses Winter Weather; flood takes the higher of Inland (riverine) Flooding and Coastal Flooding; extreme heat uses Heat Wave; extreme cold uses Cold Wave; volcano uses Volcanic Activity.',
            'nws': 'NWS county warning area (AWIPS counties, 16 April 2026). The office whose area contains the internal point is listed first; counties split between offices list both in counties-detail.json.',
            'nwr': 'NOAA Weather Radio county coverage listing; every transmitter NWS lists for the county, with the county SAME code. Connecticut planning regions list the transmitters of the legacy counties they overlap, with the legacy SAME codes the radios still use.',
            'ecoregion': 'EPA Level III ecoregion containing the internal point; ecoregions_present samples the whole county. Hawaii is not mapped at Level III by EPA.',
            'sun': 'Peak sun hours = mean daily solar energy in kWh per square metre per day on a south-facing panel tilted at the local latitude (NASA POWER climatology 2001-2025, 1-degree cell). Flat (horizontal) values in counties-detail.json.',
        },
        'hazard_rating_map': NRI_MAP,
        'hazard_order': [label for _, label, _ in HAZARDS],
    }

    jdump('counties.json', out)
    jdump('counties-detail.json', detail)
    jdump('states.json', states)
    jdump('nws-offices.json', offices)
    jdump('ecoregions.json', dict(sorted(ecoregions.items(), key=lambda kv: (len(kv[0]), kv[0]))))
    jdump('national.json', national)

    # --- coverage report ---------------------------------------------------------------------------
    keys = ['elevation_ft', 'zone', 'jan_low_f', 'jul_high_f', 'record_low_f', 'record_high_f', 'precip_in',
            'snow_in', 'last_frost', 'first_frost', 'growing_days', 'ecoregion', 'nws_office', 'sun_hours_dec']
    miss = {k: [f for f, v in out.items() if v.get(k) is None] for k in keys}
    miss['nwr'] = [f for f, v in out.items() if not v['nwr']]
    miss['nri'] = [f for f in out if f not in nri]
    rep = {k: {'missing': len(v), 'examples': v[:12]} for k, v in miss.items()}
    json.dump(rep, open(os.path.join(RAW, 'coverage.json'), 'w'), indent=1)
    for k, v in rep.items():
        print(f'{k:15s} missing {v["missing"]:5d} {v["examples"][:6]}')


if __name__ == '__main__':
    main()

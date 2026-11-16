#!/usr/bin/env python3
"""Cross-check data/regions against a second source for pilot counties (decision G20: SD and IL).

    python3 scripts/regions/verify.py            # prints a Markdown report (pasted into notes/workers/D1.md)

Second sources:
- climate: 1991-2020 means computed by ACIS from the raw daily observations of the same station
  (independent of NCEI's normals processing, which also fills gaps and adjusts for station changes);
- hardiness zone: the PHZM 2023 ZIP-code table, ZIP whose centre is nearest the county point;
- NWS office: the WFO field of the NOAA Weather Radio county coverage listing (a different NWS product);
- SAME code: NWS SameCode.txt county list (name must match);
- elevation: USGS 3DEP point vs the PRISM 4-km grid-cell elevation (ACIS);
- sun hours: NREL Solar Resource Data API latitude-tilt monthly means vs NASA POWER.
"""
import csv, io, json, math, os, sys, zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import fetch_points  # noqa: E402
import geo  # noqa: E402

ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
RAW = os.path.join(ROOT, 'build', 'regions-raw')
DATA = os.path.join(ROOT, 'data', 'regions')
PILOT = ['46099', '46103', '46013', '46065', '46081', '17031', '17167', '17019', '17077', '17143']


def acis_means(sid):
    cache = os.path.join(RAW, 'api', 'verify_acis.json')
    c = json.load(open(cache)) if os.path.exists(cache) else {}
    if sid not in c:
        el = lambda n, red: {'name': n, 'interval': 'mly', 'duration': 'mly', 'reduce': red, 'maxmissing': 3}
        j = fetch_points.get('https://data.rcc-acis.org/StnData',
                             {'sid': sid, 'sdate': '1991-01', 'edate': '2020-12',
                              'elems': [el('mint', 'mean'), el('maxt', 'mean'), el('pcpn', 'sum'), el('snow', 'sum')]})
        c[sid] = j
        json.dump(c, open(cache, 'w'))
    j = c[sid]
    if not j or 'data' not in j:
        return None
    jan, jul, yp, ys = [], [], {}, {}
    for row in j['data']:
        ym, mn, mx, pc, sn = row
        y, m = ym.split('-')
        f = lambda x: None if x in ('M', '', None) else (0.0 if x == 'T' else float(x))
        if m == '01' and f(mn) is not None: jan.append(f(mn))
        if m == '07' and f(mx) is not None: jul.append(f(mx))
        yp.setdefault(y, []).append(f(pc)); ys.setdefault(y, []).append(f(sn))
    full = lambda d: [sum(v) for v in d.values() if len(v) == 12 and None not in v]
    P, S = full(yp), full(ys)
    avg = lambda a: round(sum(a) / len(a), 1) if a else None
    return {'jan_low': avg(jan), 'jul_high': avg(jul), 'precip': avg(P), 'snow': avg(S), 'years_p': len(P), 'years_s': len(S)}


def main():
    detail = json.load(open(os.path.join(DATA, 'counties-detail.json')))
    fidx = json.load(open(os.path.join(DATA, 'fips-index.json')))
    states = {}
    for f in PILOT:
        st = fidx[f][0]
        if st not in states:
            states[st] = json.load(open(os.path.join(DATA, 'states', f'{st}.json')))
    county = lambda f: states[fidx[f][0]]['counties'][fidx[f][1]]
    # zip zones
    zz = {r['zipcode']: r['zone'] for r in csv.DictReader(open(os.path.join(RAW, 'phzm_us_zipcode_2023.csv')))}
    z = zipfile.ZipFile(os.path.join(RAW, 'gaz_zcta.zip'))
    lines = z.read(z.namelist()[0]).decode('latin1').splitlines()
    zc = []
    for line in lines[1:]:
        p = [x.strip() for x in line.split('\t')]
        zc.append((p[0], float(p[-2]), float(p[-1])))
    # NWR WFO + SameCode
    import re
    js = open(os.path.join(RAW, 'nwr_ccl.js'), encoding='latin1').read()
    arr = {}
    for name, i, val in re.findall(r'^(\w+)\[(\d+)\] = "(.*)";\s*$', js, re.M):
        arr.setdefault(name, {})[int(i)] = val
    wfo = {}
    for i, s in arr['SAME'].items():
        wfo.setdefault(s[1:], set()).add(arr['WFO'].get(i, '').replace('|', ', '))
    same = {l.split(',')[0]: l.split(',', 1)[1].strip() for l in open(os.path.join(RAW, 'nwr_samecode.txt'), encoding='latin1') if ',' in l}
    gridelev = json.load(open(os.path.join(RAW, 'api', 'gridelev.json')))
    nrel = json.load(open(os.path.join(RAW, 'api', 'nrel_verify.json')))

    out = []
    out.append('| County | Check | Kit value | Second source | Result |')
    out.append('|---|---|---|---|---|')
    tally = {'agree': 0, 'close': 0, 'differs': 0}

    def row(name, check, kit, other, ok):
        tally[ok] += 1
        out.append(f'| {name} | {check} | {kit} | {other} | {ok} |')

    for f in PILOT:
        c, d = county(f), detail[f]
        name = f'{fidx[f][1]}, {fidx[f][0]}'
        ts = d['stations']['temperature']
        m = acis_means(ts['id'])
        if m:
            for k, kk, tol in (('jan_low_f', 'jan_low', 2), ('jul_high_f', 'jul_high', 2)):
                diff = abs(c[k] - m[kk])
                row(name, f'{k} ({ts["id"]})', c[k], f'{m[kk]} (ACIS 1991-2020 raw mean)', 'agree' if diff <= tol else 'close' if diff <= 4 else 'differs')
        ps = d['stations']['precip']
        mp = acis_means(ps['id'])
        if mp and mp['precip']:
            diff = abs(c['precip_in'] - mp['precip']) / max(c['precip_in'], 1)
            row(name, f'precip_in ({ps["id"]})', c['precip_in'], f'{mp["precip"]} ({mp["years_p"]} complete yrs)', 'agree' if diff <= 0.08 else 'close' if diff <= 0.15 else 'differs')
        ss = d['stations']['snow']
        if ss:
            ms = acis_means(ss['id'])
            if ms and ms['snow'] is not None and ms['years_s'] >= 10:
                diff = abs(c['snow_in'] - ms['snow']) / max(c['snow_in'], 1)
                row(name, f'snow_in ({ss["id"]})', c['snow_in'], f'{ms["snow"]} ({ms["years_s"]} complete yrs)', 'agree' if diff <= 0.12 else 'close' if diff <= 0.25 else 'differs')
        # zone
        la, lo = d['lat'], d['lon']
        best = min(zc, key=lambda t: geo.haversine_km(la, lo, t[1], t[2]))
        zk = zz.get(best[0])
        row(name, 'zone', c['zone'], f'{zk} (ZIP {best[0]}, PHZM ZIP table)', 'agree' if zk == c['zone'] else 'close')
        # NWS
        w = sorted(wfo.get(f, []))
        city = c['nws_office'].split(',')[0]
        row(name, 'nws_office', c['nws_office'], '; '.join(w) + ' (NWR listing WFO)', 'agree' if any(city in x for x in w) else 'differs')
        # SAME
        sc = '0' + f
        nm = same.get(sc, '?')
        row(name, 'SAME code', ', '.join(sorted({t['same'] for t in c['nwr']})) or sc, f'{sc} = {nm} (SameCode.txt)', 'agree' if fidx[f][1].startswith(nm.split(',')[0]) else 'differs')
        # elevation
        g = gridelev.get(f)
        if g is not None and c['elevation_ft'] is not None:
            diff = abs(c['elevation_ft'] - g)
            row(name, 'elevation_ft', c['elevation_ft'], f'{round(g)} (PRISM 4-km cell)', 'agree' if diff <= 150 else 'close' if diff <= 400 else 'differs')
        # sun
        n = nrel.get(f)
        if n and 'lat_tilt_dec' in n:
            dd = abs(c['sun_hours_dec'] - n['lat_tilt_dec']); dj = abs(c['sun_hours_jun'] - n['lat_tilt_jun'])
            row(name, 'sun hours Dec / Jun', f"{c['sun_hours_dec']} / {c['sun_hours_jun']}", f"{n['lat_tilt_dec']} / {n['lat_tilt_jun']} (NREL)",
                'agree' if dd <= 0.4 and dj <= 0.4 else 'close' if dd <= 0.7 and dj <= 0.7 else 'differs')
    print('\n'.join(out))
    print()
    print(f"Totals: {tally}")


if __name__ == '__main__':
    main()

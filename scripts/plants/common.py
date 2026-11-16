"""Shared helpers for the national plant dataset pipeline (worker D2).

Raw downloads live in build/plants-raw/ (git-ignored). Nothing here invents data: names and
symbols come from the USDA PLANTS checklist, distribution from the PLANTS distribution download,
image licence flags from the PLANTS image records.
"""
import json, os, re, sys, time, urllib.request, urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / 'build' / 'plants-raw'
API = 'https://plantsservices.sc.egov.usda.gov/api'
IMG_BASE = 'https://plants.usda.gov'
UA = {'User-Agent': 'Mozilla/5.0 (compatible; offline-binder-kit/1.0; plant dataset build)'}

sys.path.insert(0, str(Path(__file__).resolve().parent / 'src'))


def http(url, data=None, headers=None, timeout=60, tries=4):
    h = dict(UA)
    if headers:
        h.update(headers)
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, data=data, headers=h)
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except Exception as e:  # network or HTTP error: retry with back-off
            last = e
            time.sleep(1.5 * (i + 1))
    raise last


def cached(path, fetch):
    path = Path(path)
    if path.exists() and path.stat().st_size > 0:
        return path.read_bytes()
    b = fetch()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(b)
    return b


def plants_profile(symbol):
    b = cached(RAW / 'api' / f'profile-{symbol}.json', lambda: http(f'{API}/PlantProfile?symbol={symbol}'))
    return json.loads(b)


def plants_images(plant_id):
    b = cached(RAW / 'api' / f'images-{plant_id}.json', lambda: http(f'{API}/PlantImages?plantId={plant_id}'))
    return json.loads(b)


def plants_distribution(plant_id):
    body = json.dumps({'MasterId': plant_id}).encode()
    b = cached(RAW / 'api' / f'dist-{plant_id}.csv',
               lambda: http(f'{API}/PlantProfile/getDownloadDistributionDocumentation', data=body,
                            headers={'Content-Type': 'application/json', 'Accept': 'text/csv'}))
    return b.decode('utf-8-sig')


def load_sources():
    from deadly import D
    from edible import E
    from firewood import F
    return D, E, F


STATE_ABBR = {
    'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA', 'Colorado': 'CO',
    'Connecticut': 'CT', 'Delaware': 'DE', 'District of Columbia': 'DC', 'Florida': 'FL', 'Georgia': 'GA',
    'Hawaii': 'HI', 'Idaho': 'ID', 'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA', 'Kansas': 'KS',
    'Kentucky': 'KY', 'Louisiana': 'LA', 'Maine': 'ME', 'Maryland': 'MD', 'Massachusetts': 'MA',
    'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS', 'Missouri': 'MO', 'Montana': 'MT',
    'Nebraska': 'NE', 'Nevada': 'NV', 'New Hampshire': 'NH', 'New Jersey': 'NJ', 'New Mexico': 'NM',
    'New York': 'NY', 'North Carolina': 'NC', 'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK',
    'Oregon': 'OR', 'Pennsylvania': 'PA', 'Rhode Island': 'RI', 'South Carolina': 'SC', 'South Dakota': 'SD',
    'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA',
    'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY', 'Puerto Rico': 'PR',
    'Virgin Islands': 'VI', 'U.S. Virgin Islands': 'VI', 'Guam': 'GU', 'American Samoa': 'AS',
    'Northern Mariana Islands': 'MP',
}
LOWER48 = [s for s in STATE_ABBR.values() if s not in ('AK', 'HI', 'PR', 'VI', 'GU', 'AS', 'MP')]
EAST = ['AL', 'AR', 'CT', 'DE', 'DC', 'FL', 'GA', 'IL', 'IN', 'IA', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN',
        'MS', 'MO', 'NH', 'NJ', 'NY', 'NC', 'OH', 'OK', 'PA', 'RI', 'SC', 'TN', 'TX', 'VT', 'VA', 'WV', 'WI']


def strip_author(name):
    """'Sambucus nigra L. ssp. canadensis (L.) Bolli' -> 'Sambucus nigra ssp. canadensis'."""
    t = name.replace('×', 'x ').split()
    if not t:
        return ''
    out = [t[0]]
    i = 1
    if i < len(t) and t[i] == 'x':
        out.append('x'); i += 1
    if i < len(t) and re.match(r'^[a-z][a-z-]+$', t[i]):
        out.append(t[i]); i += 1
    while i < len(t):
        if t[i] in ('ssp.', 'var.', 'subsp.', 'f.') and i + 1 < len(t) and re.match(r'^[a-z][a-z-]+$', t[i + 1]):
            out += ['ssp.' if t[i] == 'subsp.' else t[i], t[i + 1]]; i += 2
        else:
            i += 1
    return ' '.join(out)


def load_checklist():
    import csv
    rows = list(csv.DictReader(open(RAW / 'plantlst.txt', encoding='utf-8', errors='replace')))
    by_name, accepted = {}, {}
    for r in rows:
        nm = strip_author(r['Scientific Name with Author'])
        acc = r['Symbol']
        syn = r['Synonym Symbol']
        if not syn:
            accepted[acc] = dict(name=nm, full=r['Scientific Name with Author'], common=r['Common Name'], family=r['Family'])
        by_name.setdefault(nm.lower(), []).append(dict(acc=acc, syn=syn or None))
    return by_name, accepted

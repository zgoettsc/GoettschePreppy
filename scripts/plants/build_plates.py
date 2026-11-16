"""Download, licence-check and compress the plant plates; write images/plants.json and images/index.json.

  python3 scripts/plants/build_plates.py            # fetch anything missing
  python3 scripts/plants/build_plates.py --force    # re-fetch and re-compress everything

Inputs (all written by a person after looking at the image):
  scripts/plants/selections.tsv       plates chosen on the review contact sheets, with captions
  scripts/plants/household_reuse.tsv  plates already checked for the household binder
Rules enforced here, not by hand:
  - A USDA PLANTS image is refused unless its PLANTS record says Copyright=false.
  - Credits known to carry a copyright notice in the frame are refused even if the record says
    Copyright=false (see EXCLUDED_CREDITS).
  - Every download must be a real JPEG/PNG/GIF (magic bytes) before it is kept.
  - Plates are resized to at most 900 px on the longest side and saved as JPEG of about 40-80 KB.
No image is generated or altered beyond resizing and recompression. No AI imagery, ever.
"""
import hashlib, io, json, sys
from datetime import date
from PIL import Image
from common import ROOT, RAW, IMG_BASE, http, cached, plants_profile, plants_images, load_sources, merged_species

FORCE = '--force' in sys.argv
OUT = ROOT / 'images' / 'plates'
EXCLUDED_CREDITS = ('Patrick J. Alexander', 'Smithsonian', 'Norman Melvin')
MAX_SIDE, LO, HI = 900, 40_000, 80_000

COLLECTIONS = {
    'usda-plants': {
        'org': 'USDA NRCS PLANTS Database',
        'source_key': 'usda-nrcs-plants-database-plant-profiles-and-image-l-a7089c',
        'license': ('Public domain: the PLANTS image record carries Copyright=false (US Government work or '
                    'contributed to the public domain). Checked per image at build time; an image whose record '
                    'turns to Copyright=true is refused. Photographer or illustrator credit recorded per image.'),
        'tier': 1},
    'usda-ars-pprl': {
        'org': 'USDA ARS Poisonous Plant Research Laboratory (Logan, Utah)',
        'source_key': 'usda-ars-poisonous-plant-research-laboratory-water-h-ab9a68',
        'license': 'Public domain: US Government work (USDA Agricultural Research Service).',
        'tier': 1},
}
COLLECTIONS['wikimedia-commons'] = {
    'org': 'Wikimedia Commons (files tagged public domain or CC0 only)',
    'source_key': None,
    'license': ('Public domain or CC0 as tagged on the Wikimedia Commons file page; the tag and the author '
                'credit are recorded per image and re-checked at build time. Anything else is refused.'),
    'tier': 2}


def commons_rows():
    import hashlib as _h, re as _re, time as _t, urllib.parse as _u
    rows = []
    for line in open(ROOT / 'scripts' / 'plants' / 'commons_selections.tsv', encoding='utf-8'):
        if not line.strip() or line.startswith('#'):
            continue
        k, title, feat, cap = line.rstrip('\n').split('\t')
        q = dict(action='query', format='json', titles=title, prop='imageinfo',
                 iiprop='extmetadata|url|mime', iiurlwidth='960')
        url = 'https://commons.wikimedia.org/w/api.php?' + _u.urlencode(q)
        def f():
            for i in range(6):
                _t.sleep(3.0 + 10 * i)
                try:
                    return http(url, tries=1)
                except Exception as e:
                    last = e
            raise last
        info = json.loads(cached(RAW / 'commons' / 'info' / (_h.sha1(title.encode()).hexdigest() + '.json'), f))
        page = next(iter(info['query']['pages'].values()))
        ii = page['imageinfo'][0]; md = ii.get('extmetadata', {})
        lic = (md.get('License', {}) or {}).get('value', '').lower()
        strip = lambda v: _re.sub(r'\s+', ' ', _re.sub(r'<[^>]+>', '', v or '')).strip()
        rows.append(dict(key=k, imageId=None, feature=feat, caption=cap, collection='wikimedia-commons',
                         lic=lic, url=ii.get('thumburl') or ii['url'], page=ii.get('descriptionurl'),
                         credit=strip((md.get('Artist') or {}).get('value'))[:200] or None,
                         provider='Wikimedia Commons: ' + strip((md.get('LicenseShortName') or {}).get('value')),
                         fname=_re.sub(r'[^A-Za-z0-9]+', '-', title[5:].rsplit('.', 1)[0]).strip('-').lower()[:60] + '.jpg'))
    return rows


EXTRA = [  # non-PLANTS plates (each licence-checked by hand)
    dict(key='western-water-hemlock', collection='usda-ars-pprl', imageId=None, feature='root',
         url='https://www.ars.usda.gov/ARSUserFiles/20801500/Images/whemlock3.gif',
         credit='USDA ARS Poisonous Plant Research Laboratory', provider=None,
         caption=('CONFIRMATION ONLY, NOT A FIELD TEST: the rootstalk of western water hemlock split lengthwise, '
                  'showing the chambers that hold the poisonous liquid. Do not cut one open to check: the liquid '
                  'poisons skin too. Identify by leaf, stem and wet habitat instead.')),
]


def read_tsv(name):
    rows = []
    for line in open(ROOT / 'scripts' / 'plants' / name, encoding='utf-8'):
        if not line.strip() or line.startswith('#'):
            continue
        k, iid, feat, cap = line.rstrip('\n').split('\t')
        rows.append(dict(key=k, imageId=int(iid), feature=feat, caption=cap.replace('CHECK-LARGE ', '')))
    return rows


def sniff(b):
    if b[:2] == b'\xff\xd8':
        return 'jpeg'
    if b[:8] == b'\x89PNG\r\n\x1a\n':
        return 'png'
    if b[:3] == b'GIF':
        return 'gif'
    return None


def compress(raw):
    im = Image.open(io.BytesIO(raw))
    im = im.convert('RGB')
    # Line drawings and black-and-white photographs: store as one-channel greyscale (smaller, same look).
    small = im.copy(); small.thumbnail((200, 200))
    px = list(small.getdata())
    if max(max(r, g, b) - min(r, g, b) for r, g, b in px) <= 24:
        im = im.convert('L')
    if max(im.size) > MAX_SIDE:
        im.thumbnail((MAX_SIDE, MAX_SIDE), Image.LANCZOS)
    best = None
    # Resize and recompress only. Grainy film scans step down in size (never below 560 px) rather
    # than fall below quality 45.
    base = im
    for side in (900, 800, 720, 640, 560):
        im = base.copy()
        if max(im.size) > side:
            im.thumbnail((side, side), Image.LANCZOS)
        for q in (82, 75, 68, 60, 52, 45):
            buf = io.BytesIO()
            im.save(buf, 'JPEG', quality=q, optimize=True, progressive=True)
            b = buf.getvalue()
            best = (b, q)
            if len(b) <= HI:
                return b, im.size, q
    return best[0], im.size, best[1]


def main():
    D, E, F = load_sources()
    meta = merged_species()
    res = json.load(open(RAW / 'resolved.json'))
    rows = read_tsv('household_reuse.tsv') + read_tsv('selections.tsv')
    seen, plates_by_key, refused, failed = set(), {}, [], []
    for r in rows:
        if (r['key'], r['imageId']) in seen:
            continue
        seen.add((r['key'], r['imageId']))
        plates_by_key.setdefault(r['key'], []).append(dict(r, collection='usda-plants'))
    for x in EXTRA:
        plates_by_key.setdefault(x['key'], []).append(x)
    for x in commons_rows():
        if x['lic'] not in ('cc0', 'pd'):
            refused.append((x['key'], x['page'], 'commons licence ' + x['lic'])); continue
        plates_by_key.setdefault(x['key'], []).append(x)

    manifest_plants, index_plants = [], []
    total_bytes = 0
    for key in [s['key'] for s in D + E + F if s['key'] in plates_by_key and not s.get('alias_of')]:
        s = meta[key]
        sym = res.get(key, {}).get('symbol')
        main_txt = s.get('harm') or s.get('use') or (s.get('burn') or {}).get('notes', '')
        entry_m = dict(key=key, common=s['common'][0], scientific=s['sci'], symbol=sym, **{'class': s['group']},
                       groups=s.get('groups', [s['group']]), risk=s.get('risk'),
                       note=f"{main_txt} Where: {s.get('habitat', '')}".strip(),
                       lookalikes=sorted(s['look']), plates=[])
        entry_i = dict(entry_m, plates=[])
        recs = {}
        if sym:
            recs = {i['ImageID']: i for i in plants_images(plants_profile(sym)['Id'])}
        for p in plates_by_key[key][:3]:
            if p['collection'] == 'usda-plants':
                rec = recs.get(p['imageId'])
                if not rec:
                    failed.append((key, p['imageId'], 'not in PLANTS record')); continue
                who = f"{rec.get('CommonName') or ''} | {rec.get('ProvidedBy') or ''}"
                if rec['Copyright'] or any(c in who for c in EXCLUDED_CREDITS):
                    refused.append((key, p['imageId'], 'copyright')); continue
                path = rec.get('LargeSizeImageLibraryPath') or rec.get('StandardSizeImageLibraryPath')
                url = IMG_BASE + path
                credit = rec.get('CommonName') or None
                provider = rec.get('ProvidedBy') or rec.get('InstitutionName') or None
                if rec.get('LiteratureTitle'):
                    provider = f"{provider + ' - ' if provider else ''}{rec['LiteratureTitle']}" + \
                               (f" ({rec['LiteratureYear']})" if rec.get('LiteratureYear') else '')
                fname = path.rsplit('/', 1)[-1].rsplit('.', 1)[0] + '.jpg'
            elif p['collection'] == 'wikimedia-commons':
                url, credit, provider, fname = p['url'], p['credit'], p['provider'], p['fname']
            else:
                url, credit, provider = p['url'], p['credit'], p['provider']
                fname = url.rsplit('/', 1)[-1].rsplit('.', 1)[0] + '.jpg'
            try:
                cache_name = (p['fname'] if p['collection'] == 'wikimedia-commons' else url.rsplit('/', 1)[-1])
                def _get(u=url, c=p['collection']):
                    if c != 'wikimedia-commons':
                        return http(u)
                    import time as _t
                    for i in range(6):
                        _t.sleep(3.0 + 10 * i)
                        try:
                            return http(u, tries=1)
                        except Exception as e:
                            last = e
                    raise last
                raw = cached(RAW / 'large' / cache_name, _get)
            except Exception as e:
                failed.append((key, p.get('imageId'), f'download: {e}')); continue
            if not sniff(raw):
                failed.append((key, p.get('imageId'), 'not an image')); continue
            dest = OUT / key / fname
            if FORCE or not dest.exists():
                b, size, q = compress(raw)
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_bytes(b)
            b = dest.read_bytes()
            w, h = Image.open(io.BytesIO(b)).size
            total_bytes += len(b)
            rel = str(dest.relative_to(ROOT))
            entry_m['plates'].append(dict(collection=p['collection'], imageId=p.get('imageId'), file=rel,
                                          feature=p['feature'], shows=p['caption']))
            entry_i['plates'].append(dict(file=rel, shows=p['caption'], feature=p['feature'],
                                          collection=p['collection'], url=p.get('page') or url, credit=credit, provider=provider,
                                          license=COLLECTIONS[p['collection']]['license'],
                                          imageId=p.get('imageId'), width=w, height=h, bytes=len(b),
                                          sha256=hashlib.sha256(b).hexdigest()))
        if entry_m['plates']:
            manifest_plants.append(entry_m); index_plants.append(entry_i)

    note = ('National plant-identification plates for GoettschePreppy. Every image is a real photograph or a '
            'published botanical line drawing from a US Government source (USDA NRCS PLANTS, USDA Forest '
            'Service, USDA ARS); no AI-generated imagery is ever acceptable for identification. Each image was '
            'looked at before selection: the "shows" text describes what is actually in the frame, and images '
            'with a copyright notice in the frame were refused even when the source record says public domain. '
            'Plates help you recognise danger; they do not make a photograph an identification for eating.')
    coll = {k: {kk: vv for kk, vv in v.items()} for k, v in COLLECTIONS.items()}
    (ROOT / 'images').mkdir(exist_ok=True)
    json.dump(dict(note=note, collections=coll, plants=manifest_plants),
              open(ROOT / 'images' / 'plants.json', 'w'), indent=1, ensure_ascii=False)
    json.dump(dict(note=note, generated=str(date.today()), collections=coll, plants=index_plants),
              open(ROOT / 'images' / 'index.json', 'w'), indent=1, ensure_ascii=False)
    n = sum(len(p['plates']) for p in index_plants)
    print(f'{n} plates for {len(index_plants)} species, {total_bytes/1e6:.1f} MB; refused {len(refused)}; failed {len(failed)}')
    for f in refused + failed:
        print('  !', *f)


if __name__ == '__main__':
    main()

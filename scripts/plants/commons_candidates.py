"""Find public-domain / CC0 candidates on Wikimedia Commons for species with no PLANTS plate.
Only files whose Commons licence is CC0 or public domain are kept; everything else is ignored."""
import json, urllib.parse, sys
from common import RAW, http, cached, merged_species
API = 'https://commons.wikimedia.org/w/api.php'
by = merged_species()
idx = {p['key'] for p in json.load(open(RAW.parent.parent / 'images' / 'index.json'))['plants']}
miss = [k for k, s in by.items() if k not in idx and s['kind'] == 'plant']
out = {}
for k in miss:
    sci = by[k]['sci']
    q = dict(action='query', format='json', generator='categorymembers', gcmtitle=f'Category:{sci}', gcmtype='file',
             gcmlimit='200', prop='imageinfo', iiprop='extmetadata|url|size|mime', iiurlwidth='330')
    url = API + '?' + urllib.parse.urlencode(q)
    try:
        d = json.loads(cached(RAW / 'commons' / f'cat-{k}.json', lambda: http(url)))
    except Exception as e:
        print(k, 'ERR', e); continue
    cands = []
    for p in (d.get('query', {}).get('pages', {}) or {}).values():
        ii = (p.get('imageinfo') or [{}])[0]
        md = ii.get('extmetadata', {})
        lic = (md.get('License', {}) or {}).get('value', '').lower()
        short = (md.get('LicenseShortName', {}) or {}).get('value', '')
        if ii.get('mime') != 'image/jpeg' or lic not in ('cc0', 'pd'):
            continue
        cands.append(dict(title=p['title'], lic=lic, short=short, thumb=ii.get('thumburl'), url=ii.get('url'),
                          w=ii.get('width'), h=ii.get('height'),
                          artist=(md.get('Artist', {}) or {}).get('value', ''), credit=(md.get('Credit', {}) or {}).get('value', ''),
                          usage=(md.get('UsageTerms', {}) or {}).get('value', '')))
    out[k] = cands
    print(k, len(cands), [c['short'] for c in cands[:4]])
json.dump(out, open(RAW / 'commons' / 'candidates.json', 'w'), indent=1)

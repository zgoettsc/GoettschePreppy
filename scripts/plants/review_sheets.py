"""Build contact sheets of public-domain PLANTS image candidates for visual review.

Every image that reaches the kit is looked at by a person (or the reviewing worker) on these
sheets: species match, what part it shows, no watermark or copyright notice in the frame.
Output: build/plants-raw/sheets/sheet-NNN.jpg and sheets.json (tile id -> image record).
"""
import json, io, sys
from concurrent.futures import ThreadPoolExecutor
from PIL import Image, ImageDraw, ImageFont
from common import RAW, IMG_BASE, http, cached, plants_profile, plants_images, load_sources

HOUSEHOLD_DONE = set(json.load(open(RAW / 'household-reuse.json')).keys()) if (RAW / 'household-reuse.json').exists() else set()
res = json.load(open(RAW / 'resolved.json'))
dist = json.load(open(RAW / 'distribution.json'))
D, E, F = load_sources()
order = [s['key'] for s in D + E + F if s['key'] in res and not s.get('alias_of')]
pilot = [k for k in order if set(dist[k]['states']) & {'SD', 'IL'}]
rest = [k for k in order if k not in pilot]
MAXC = 5
DONE = set()
import csv as _csv
for f in ('selections.tsv', 'rejected.tsv'):
    for line in open(f):
        if line.strip() and not line.startswith('#'):
            DONE.add(line.split('\t')[0])

def excluded(i):
    # Credits whose every sampled image carried a copyright notice in the frame although the PLANTS
    # record says Copyright=false, and seed-laboratory photographs (not useful for field identification).
    who = (i.get('CommonName') or '') + ' | ' + (i.get('ProvidedBy') or '')
    return ('Patrick J. Alexander' in who or 'Smithsonian' in who or 'Norman Melvin' in who
            or 'Systematic Botany and Mycology' in who)

def candidates(key):
    p = plants_profile(res[key]['symbol'])
    imgs = [i for i in plants_images(p['Id']) if not i['Copyright'] and i.get('StandardSizeImageLibraryPath')
            and not excluded(i)]
    photos = [i for i in imgs if i['StandardSizeImageLibraryPath'][-5:-4] == 'p']
    draws = [i for i in imgs if i['StandardSizeImageLibraryPath'][-5:-4] == 'd']
    return (photos[:MAXC - min(1, len(draws))] + draws[:1])[:MAXC]

def std(i):
    path = i['StandardSizeImageLibraryPath']
    return cached(RAW / 'std' / path.rsplit('/', 1)[-1], lambda: http(IMG_BASE + path))

keys = [k for k in pilot + rest if k not in HOUSEHOLD_DONE and k not in DONE]
plan = [(k, candidates(k)) for k in keys]
plan = [(k, c) for k, c in plan if c]
with ThreadPoolExecutor(8) as ex:
    list(ex.map(lambda ic: std(ic), [i for _, c in plan for i in c]))

font = ImageFont.load_default(size=15)
TW, TH, LH = 264, 176, 20
sheets, tiles = [], {}
PER = 4
(RAW / 'sheets2').mkdir(exist_ok=True)
for n in range(0, len(plan), PER):
    chunk = plan[n:n + PER]
    sheet = Image.new('RGB', (TW * MAXC, (TH + LH * 2) * len(chunk)), 'white')
    dr = ImageDraw.Draw(sheet)
    sid = n // PER + 1
    for r, (k, cands) in enumerate(chunk):
        y = r * (TH + LH * 2)
        row = 'ABCD'[r]
        dr.text((4, y + 2), f"{row}: {k}  ({res[k]['accepted']})", fill='black', font=font)
        for c, i in enumerate(cands):
            im = Image.open(io.BytesIO(std(i))).convert('RGB')
            im.thumbnail((TW - 4, TH))
            x = c * TW
            sheet.paste(im, (x + 2, y + LH))
            dr.text((x + 4, y + LH + TH), f"{row}{c+1} {i['ImageID']}", fill='red', font=font)
            tiles[f"{sid}:{row}{c+1}"] = dict(key=k, imageId=i['ImageID'])
    sheet.save(RAW / 'sheets2' / f'sheet-{sid:03d}.jpg', quality=80)
    sheets.append(dict(sheet=sid, keys=[k for k, _ in chunk]))
json.dump(dict(sheets=sheets, tiles=tiles, pilot=pilot), open(RAW / 'sheets2.json', 'w'), indent=0)
print(len(plan), 'species with candidates;', len(sheets), 'sheets;', len(tiles), 'tiles; pilot species', len(pilot))
print('pilot sheets end at', max(s['sheet'] for s in sheets if any(k in pilot for k in s['keys'])))

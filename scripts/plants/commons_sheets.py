import json, io, re, time
from PIL import Image, ImageDraw, ImageFont
from common import RAW, http, cached, merged_species
by = merged_species()
c = json.load(open(RAW / 'commons' / 'candidates.json'))
order = [k for k in c if by[k]['group'] == 'deadly'] + [k for k in c if by[k]['group'] != 'deadly']
plan = [(k, c[k][:4]) for k in order if c[k]]
font = ImageFont.load_default(size=15)
TW, TH, LH, PER = 300, 200, 20, 4
tiles = {}
(RAW / 'commons' / 'sheets').mkdir(exist_ok=True)
def thumb(cd):
    name = re.sub(r'[^A-Za-z0-9._-]', '_', cd['title'])[:120]
    def f():
        time.sleep(0.7); return http(cd['thumb'])
    return cached(RAW / 'commons' / 'thumbs' / name, f)
for n in range(0, len(plan), PER):
    chunk = plan[n:n + PER]; sid = n // PER + 1
    sheet = Image.new('RGB', (TW * 4, (TH + LH * 2) * len(chunk)), 'white'); dr = ImageDraw.Draw(sheet)
    for r, (k, cands) in enumerate(chunk):
        y = r * (TH + LH * 2); row = 'ABCD'[r]
        dr.text((4, y + 2), f"{row}: {k}  ({by[k]['sci']})", fill='black', font=font)
        for j, cd in enumerate(cands):
            try:
                im = Image.open(io.BytesIO(thumb(cd))).convert('RGB'); im.thumbnail((TW - 4, TH))
                sheet.paste(im, (j * TW + 2, y + LH))
            except Exception as e:
                dr.text((j * TW + 4, y + LH + 40), f'ERR {e}'[:40], fill='red', font=font)
            dr.text((j * TW + 4, y + LH + TH), f"{row}{j+1} {cd['lic']}", fill='red', font=font)
            tiles[f'{sid}:{row}{j+1}'] = dict(key=k, **cd)
    sheet.save(RAW / 'commons' / 'sheets' / f'c-{sid:02d}.jpg', quality=80)
json.dump(tiles, open(RAW / 'commons' / 'tiles.json', 'w'), indent=1)
print(len(plan), 'species;', -(-len(plan) // PER), 'sheets')

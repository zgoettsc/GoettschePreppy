"""Fetch PLANTS profile, county distribution and image list for every resolved symbol (cached)."""
import json, sys
from concurrent.futures import ThreadPoolExecutor
from common import RAW, plants_profile, plants_images, plants_distribution

res = json.load(open(RAW / 'resolved.json'))
syms = sorted({v['symbol'] for v in res.values()})

def one(sym):
    try:
        p = plants_profile(sym)
        pid = p['Id']
        plants_images(pid)
        csv = plants_distribution(pid)
        return sym, pid, csv.count('\n'), None
    except Exception as e:
        return sym, None, 0, repr(e)

with ThreadPoolExecutor(6) as ex:
    for sym, pid, n, err in ex.map(one, syms):
        print(sym, pid, n, err or '', flush=True)

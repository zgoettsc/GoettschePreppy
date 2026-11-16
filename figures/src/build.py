"""Write every drawn diagram to figures/svg/<id>.svg and print a JSON list of their metadata.

Run:  python3 figures/src/build.py [fig-id ...]
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import importlib, glob as _glob
import fig_power, fig_heat, fig_medical, fig_knots, fig_misc  # noqa: E401

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'svg')
ALL = {}
for m in (fig_power, fig_heat, fig_medical, fig_knots, fig_misc):
    ALL.update(m.FIGS)
# F2's modules (fig_f2_*.py) are picked up automatically; they only add new ids.
for _f in sorted(_glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fig_f2_*.py'))):
    _m = importlib.import_module(os.path.basename(_f)[:-3])
    assert not (set(_m.FIGS) & set(ALL)), _f
    ALL.update(_m.FIGS)

if __name__ == '__main__':
    want = sys.argv[1:] or list(ALL)
    os.makedirs(OUT, exist_ok=True)
    meta = {}
    for fid in want:
        f = ALL[fid]
        s = f['fn']()
        bare = s.replace('xmlns="http://www.w3.org/2000/svg"', '')
        assert 'http' not in bare and 'www.' not in bare, fid
        with open(os.path.join(OUT, fid + '.svg'), 'w') as fh:
            fh.write(s)
        meta[fid] = {k: f[k] for k in ('caption', 'alt', 'pages')}
        print(fid, len(s), 'bytes', file=sys.stderr)
    with open(os.path.join(OUT, '..', 'src', 'meta.json'), 'w') as fh:
        json.dump({k: {kk: vv for kk, vv in ALL[k].items() if kk != 'fn'} for k in ALL}, fh, indent=1)

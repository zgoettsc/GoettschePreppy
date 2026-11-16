"""Write figures/REQUESTS.md: every figure id requested by a content page, the pages, the
description the requesting worker wrote, the plan and the status.

Run:  python3 figures/src/make_requests.py   (after make_index.py)
"""
import glob, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..', '..'))

pages = {}
for f in sorted(glob.glob(os.path.join(ROOT, 'content/sections/*/*.md'))):
    txt = open(f).read()
    m = re.search(r'^figures:\s*\[(.*?)\]', txt, re.M)
    pid = os.path.basename(f)[:5]
    for fid in re.findall(r'fig-[a-z0-9-]+', m.group(1) if m else ''):
        pages.setdefault(fid, []).append(pid)
    for fid in re.findall(r'\{\{\s*figure\s+(fig-[a-z0-9-]+)', txt):
        if pid not in pages.setdefault(fid, []):
            pages[fid].append(pid)

desc = {}
for f in sorted(glob.glob(os.path.join(ROOT, 'notes/workers/*.md'))):
    w = os.path.basename(f)[:-3]
    if w == 'F1':
        continue
    lines = open(f).read().split('\n')
    i = 0
    while i < len(lines):
        m = re.match(r'^\s*-\s+`?(fig-[a-z0-9-]+)`?\s*[:—-]\s*(.*)$', lines[i])
        if m:
            fid, d = m.group(1), m.group(2)
            j = i + 1
            while j < len(lines) and lines[j].startswith('  ') and not re.match(r'^\s*-\s', lines[j]):
                d += ' ' + lines[j].strip()
                j += 1
            d = d.replace('|', '/').strip()
            if fid not in desc or len(d) > len(desc[fid][1]):
                desc[fid] = (w, d)
            i = j
        else:
            i += 1

index = json.load(open(os.path.join(ROOT, 'figures/index.json')))

MERGE = {
    'fig-generator-distance': ('fig-generator-siting', '30-01, 17-08'),
    'fig-panel-transfer-switch-interlock': ('fig-backfeed-path', '29-04'),
    'fig-chopping-block-height': ('fig-splitting-stance', '16-06'),
}
PD_WANTED = {
    'fig-hemlock-leaf-veins': 'pd-plate only (USDA ARS / Forest Service line drawing or photo). Plant identification: never drawn.',
    'fig-squash-male-female-flowers': 'pd-plate (USDA / Extension PD photo); not drawn (plant imagery).',
    'fig-tick-removal': 'pd-plate: CDC tick-removal illustration (PD); fetch blocked here.',
    'fig-shelter-by-dwelling': 'pd-plate: FEMA Planning Guidance for a Nuclear Detonation protection-factor figure; else svg.',
    'fig-tornado-shelter-choices': 'pd-plate: FEMA P-320 figure (fema.gov returned 403 here); else svg.',
    'fig-avma-gunshot-sites-dog-cat': 'hold: AVMA 2020 figures are copyrighted; a drawn animal-anatomy schematic needs an owner decision.',
    'fig-hail-sizes': 'svg (or NWS PD hail-size graphic).',
    'fig-drop-cover-hold-on': 'svg (Earthquake Country Alliance art is not PD).',
}


def plan_status(fid):
    if fid in MERGE:
        tgt, pg = MERGE[fid]
        st = f'merged into {tgt}; alias in index.json' if fid in index else f'merged into {tgt} (not drawn yet)'
        return f'drop/merge → {tgt} (page edit: {pg})', st
    e = index.get(fid)
    if e:
        kind = 'pd-plate' if not e['file'].endswith('.svg') else 'svg'
        return kind, 'done: ' + e['file']
    if fid in PD_WANTED:
        return PD_WANTED[fid], 'open'
    return 'svg', 'open'


rows = []
for fid in sorted(set(pages) | set(desc)):
    plan, st = plan_status(fid)
    w, d = desc.get(fid, ('', ''))
    rows.append((fid, ', '.join(sorted(pages.get(fid, []))) or '(no page)', f'{d} ({w})' if d else '(no description in notes)', plan, st))
new = [f for f in index if f not in pages]

done = sum(1 for r in rows if r[4].startswith('done') or 'alias' in r[4])
out = ['# Figure requests (F1)', '',
       'Every `fig-*` id in a content page (frontmatter `figures:` and `{{figure}}` tags), the pages that use it, '
       'the description the requesting worker wrote in `notes/workers/*.md`, the plan and the status. '
       'Regenerate with `python3 figures/src/make_requests.py`.', '',
       f'{len(rows)} ids requested; {done} have a figure in `figures/index.json` (including merged aliases); '
       f'{len(rows) - done} open.', '',
       'Plans: **pd-plate** = public-domain figure cropped from a federal document (`figures/pd/`); '
       '**svg** = line diagram drawn here (`figures/svg/`, source in `figures/src/`), labelled "Diagram, not to scale"; '
       '**drop/merge** = same picture as another id. Plant, fungus and animal identification images are never drawn.', '',
       '| id | pages | what it must show (requester) | plan | status |', '|---|---|---|---|---|']
for r in rows:
    out.append('| ' + ' | '.join(r) + ' |')
if new:
    out += ['', '## Drawn without a page reference yet', '',
            'These figures exist in `figures/index.json` but no page lists them; the page edits are in `notes/workers/F1.md`.', '']
    for f in new:
        out.append(f'- `{f}`: {index[f]["caption"]}')
open(os.path.join(ROOT, 'figures/REQUESTS.md'), 'w').write('\n'.join(out) + '\n')
print(len(rows), 'requests,', done, 'done')

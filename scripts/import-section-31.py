#!/usr/bin/env python3
"""Import Section 31 (AFH 10-644, public domain) from the household binder.

Usage: python3 scripts/import-section-31.py /path/to/SHTF

Copies the verbatim chapter text, converts frontmatter to the kit schema, replaces the
household banner with the kit banner (plus chapter-specific cautions written for any
household), and removes web addresses from the handbook's reference lists (no links
anywhere). Section intro 31-00 is generated elsewhere.
"""
import sys, re, pathlib, json
SHTF = pathlib.Path(sys.argv[1]); ROOT = pathlib.Path(__file__).resolve().parents[1]
SRC = SHTF / 'sections/31-sere-field-reference'
DST = ROOT / 'content/sections/31-sere-field-reference'; DST.mkdir(parents=True, exist_ok=True)
KEY = 'afh-10-644'
REVISED = '2026-11-16'

BANNER = """> **Verbatim U.S. Air Force doctrine** (Air Force Handbook 10-644, Survival Evasion
> Resistance Escape Operations, 27 March 2017, public domain). Reproduced word for word for offline
> use. Figures and photographs are not in this text; the handbook's figures are being restored
> into this section (→ 31-00). `[p. N]` markers give the handbook's PDF page. "IP" means isolated
> person: a service member on their own."""

CAUTION = {
 '31-05': """> **SAFETY for households:** this is military field medicine, and some of it is decades
> old. The binder's own first-aid pages (Section 12) come first; read this chapter as depth behind
> them. **Tourniquet: ignore 5.5.1.1.2's "loosen after 15 to 20 minutes".** Once a tourniquet is on,
> it stays on; write the time (→ 12-02, → 30-01). **Snakebite: no extractor or suction kits**, no
> cutting, no ice. **Wound closure and maggot therapy:** → 12-14 decides. **5.10 "Medical Plants for
> SERE Scenarios"** identifies plants by text without the photographs: never use it to identify a
> plant (→ 30-01).""",
 '31-16': """> **SAFETY for households: treat all water.** The binder's water pages (Section 03) decide
> how much water and how to make it safe (→ 03-04). The "no purification needed" statements in this
> chapter are about tropical vines and bamboo and do not apply to a household. The chapter's boil
> rule (1 minute at a rolling boil, 3 minutes at high altitude) agrees with the CDC.""",
 '31-17': """> **SAFETY for households: plant identification and the "edibility test".** The
> identification photographs this chapter depends on are not in this text. **Never decide a plant,
> mushroom or animal is edible from this text alone**; use the identification plates in the region
> appendix (→ 32-00) and the foraging page (→ 05-06). **The "universal edibility test" in 17.4.3.1
> is not used in this binder** (→ 30-01): it does not protect against the plants that actually kill,
> and for anyone with a severe allergy it is dangerous by design. **Insects (17.3.9)** can trigger
> reactions in people allergic to shellfish; anyone with a shellfish or other severe food allergy
> follows their own allergy plan (→ 02-04).""",
}

def split(text):
    m = re.match(r'^---\n(.*?)\n---\n(.*)$', text, re.S); return m.group(1), m.group(2)

n = 0
for f in sorted(SRC.glob('31-*.md')):
    if f.name.startswith('31-00'): continue
    fm, body = split(f.read_text())
    pid = re.search(r'^id:\s*(\S+)', fm, re.M).group(1)
    title = re.search(r'^title:\s*"?(.*?)"?\s*$', fm, re.M).group(1)
    tags = re.search(r'^tags:\s*\[(.*?)\]', fm, re.M)
    tags = [t.strip() for t in tags.group(1).split(',')] if tags else []
    lines = body.split('\n')
    # body: '# Title', blank, banner (> lines), rest
    i = 0
    while i < len(lines) and not lines[i].startswith('# '): i += 1
    h1 = lines[i]; j = i + 1
    while j < len(lines) and lines[j].strip() == '': j += 1
    while j < len(lines) and lines[j].startswith('>'): j += 1
    rest = '\n'.join(lines[j:])
    rest = re.sub(r'https?://\S+|www\.\S+', '[web address omitted]', rest)
    banner = BANNER + ('\n>\n' + CAUTION[pid[:5]] if pid[:5] in CAUTION else '')
    danger = 'critical' if pid[:5] in CAUTION else 'none'
    new_fm = {
        'id': pid, 'section': '31-sere-field-reference', 'title': title, 'version': 1, 'revised': REVISED,
        'layer': 'core', 'danger_level': danger, 'phase': ['A', 'B', 'C'], 'tags': tags,
        'derived_from': [pid], 'sources': [KEY], 'related': ['31-00-section-intro'],
    }
    head = '---\n' + '\n'.join(f'{k}: {json.dumps(v, ensure_ascii=False)}' for k, v in new_fm.items()) + '\n---\n\n'
    (DST / f.name).write_text(head + h1 + '\n\n' + banner + '\n\n' + rest.lstrip('\n'))
    n += 1
print(f'imported {n} pages')

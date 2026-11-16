from figlib import *
from fig_power import fig as _f
FIGS = {}


def fig(fid, caption, alt, pages):
    def deco(fn):
        FIGS[fid] = dict(fn=fn, caption=caption, alt=alt, pages=pages)
        return fn
    return deco


def leg(dx=0, dy=0, s=1.0):
    """Leg lying flat, seen from the side: hip at left, knee near x=180, foot up at right."""
    P = lambda x, y: f'{round(dx + x * s, 1)},{round(dy + y * s, 1)}'
    d = (f'M{P(10, 56)} C{P(80, 58)} {P(150, 68)} {P(178, 74)} C{P(200, 78)} {P(260, 84)} {P(300, 88)} '
         f'L{P(312, 52)} C{P(318, 44)} {P(330, 46)} {P(332, 54)} L{P(328, 112)} C{P(320, 120)} {P(304, 116)} {P(298, 112)} '
         f'C{P(260, 116)} {P(210, 118)} {P(180, 122)} C{P(150, 126)} {P(80, 132)} {P(10, 134)}')
    return path(d, INK, INK, 1.8, 0.05) + path(f'M{P(172, 80)} q{8 * s},{-6 * s} {16 * s},0', INK, sw=1.2, op=0.6)


def band(x, y1, y2, color=INK, dashed=False, s=1.0):
    """Windlass tourniquet across the limb at x, from y1 to y2 (limb edges)."""
    dash = '4 3' if dashed else None
    b = rect(x - 6 * s, y1 - 4, 12 * s, y2 - y1 + 8, color, color, 1.6, 2, 0.0 if dashed else 0.25, dash)
    if not dashed:
        my = (y1 + y2) / 2
        b += line(x - 14 * s, my - 14 * s, x + 14 * s, my + 14 * s, color, 4)  # windlass rod
        b += rect(x + 8 * s, y1 - 14 * s, 10 * s, 12 * s, color, 'none', 1.4, 2)  # clip
    return b


def wound(x, y, r=7):
    return path(f'M{x - r},{y} q{r * 0.5},{-r * 0.8} {r},{-0.2 * r} q{r * 0.6},{-0.9 * r} {r},{0.3 * r} q{0.2 * r},{r * 0.9} {-r},{r * 0.8} q{-0.8 * r},{0.4 * r} {-r},{-0.9 * r} Z',
                RED, RED, 1.4, 0.75)


@fig('fig-tourniquet-placement',
     'Tourniquet: 2 to 3 inches above the wound, on the limb, never over a joint. Tighten until the bleeding stops and there is no pulse below, lock the windlass, write the time on it, never loosen it. Still bleeding: a second tourniquet above the first.',
     'Two legs drawn lying flat. Top: a wound on the thigh; a windlass tourniquet sits 2 to 3 inches above it, between the wound and the body, with the windlass rod locked in its clip and TIME written on the strap; a dashed second tourniquet is shown above the first for when bleeding continues. Bottom: a wound just below the knee; a tourniquet over the knee is crossed out in red, and the correct one is above the knee on the thigh.',
     ['12-02'])
def tourniquet():
    b = [t(8, 16, 'Leg lying flat, seen from the side', 11.5, italic=True)]
    oy = 20
    b.append(leg(0, oy))
    b.append(wound(150, oy + 98))
    b.append(t(150, oy + 152, 'wound', 11, 'middle', fill=RED))
    tx = 104
    b.append(band(tx, oy + 63, oy + 130))
    b.append(rect(tx - 5, oy + 108, 10, 18, AMBER, AMBER, 1, 1, 0.5))
    b.append(band(68, oy + 60, oy + 132, GREEN, dashed=True))
    b.append(arrow(124, oy + 40, 112, oy + 40, INK, 1.4, 5) + arrow(126, oy + 40, 148, oy + 40, INK, 1.4, 5))
    b.append(line(150, oy + 44, 150, oy + 88, INK, 1, '2 2') + line(110, oy + 44, 110, oy + 56, INK, 1, '2 2'))
    b.append(t(130, oy + 32, '2 to 3 in', 11.5, 'middle', 'bold'))
    b.append(tl(4, oy + 150, [('2nd tourniquet', False)], 10.5, fill=GREEN))
    b.append(t(4, oy + 162, 'if still bleeding', 10.5, fill=GREEN))
    b.append(tl(204, oy + 34, ['knee'], 11) + arrow(206, oy + 38, 190, oy + 66, INK, 1, 5))
    b.append(t(96, oy + 182, 'TIME written on the strap', 11, 'start', 'bold', AMBER))
    b.append(t(8, oy + 14, '← hip end (toward the body)', 10.5, italic=True))
    # second leg: wound below knee
    oy2 = 228
    b.append(line(4, oy2 - 14, 356, oy2 - 14, INK, 0.8, op=0.4))
    b.append(t(8, oy2 + 4, 'Wound at or just below a joint: go above the joint', 12, weight='bold'))
    b.append(leg(0, oy2 + 10))
    b.append(wound(206, oy2 + 110))
    b.append(band(182, oy2 + 82, oy2 + 134, RED))
    b.append(cross(164, oy2 + 70, 38, 74, RED, 3.5))
    b.append(t(182, oy2 + 168, 'never over the knee or elbow', 11, 'middle', 'bold', RED))
    b.append(band(140, oy2 + 76, oy2 + 138))
    b.append(check(132, oy2 + 44, 14))
    # rules
    y = oy2 + 196
    rules = [('Tighten until the bleeding stops AND there is no', True), ('pulse below it. Lock the windlass in its clip.', True),
             ('It will hurt a great deal. That is expected.', False), ('Write the time on it. Never loosen it.', True)]
    b.append(tl(8, y, rules, 12, 15))
    return svg('fig-tourniquet-placement', y + 76, '\n'.join(b), 'Where a tourniquet goes')


def body_front(cx, top, s=1.0, sw=1.6):
    """Very simple front-view body outline; returns (svg, landmarks)."""
    S = lambda v: round(v * s, 1)
    b = circle(cx, top + S(14), S(13), INK, INK, sw, 0.05)
    b += path(f'M{cx - S(6)},{top + S(27)} v{S(6)} M{cx + S(6)},{top + S(27)} v{S(6)}', INK, sw=sw)
    b += path(f'M{cx - S(28)},{top + S(36)} Q{cx},{top + S(30)} {cx + S(28)},{top + S(36)} L{cx + S(24)},{top + S(110)} '
              f'L{cx - S(24)},{top + S(110)} Z', INK, INK, sw, 0.05)
    b += path(f'M{cx - S(28)},{top + S(38)} L{cx - S(40)},{top + S(104)} M{cx + S(28)},{top + S(38)} L{cx + S(40)},{top + S(104)}', INK, sw=sw * 2.2)
    b += path(f'M{cx - S(16)},{top + S(110)} L{cx - S(18)},{top + S(196)} M{cx + S(16)},{top + S(110)} L{cx + S(18)},{top + S(196)}', INK, sw=sw * 3.2)
    lm = dict(neck=(cx, top + S(31)), armpit=(cx - S(26), top + S(44)), chest=(cx, top + S(56)), belly=(cx, top + S(88)),
              groin=(cx - S(12), top + S(116)))
    return b, lm


@fig('fig-wound-packing',
     'Wound packing for the groin, armpit or neck, where a tourniquet cannot go: push gauze in until the wound is full, then press hard on top and keep pressing. Never pack the chest or belly: cover and press.',
     'Left: a simple body outline. The groin, armpit and neck are marked in green as places to pack; the chest and belly are shaded red with "do not pack: cover and press". Right, two cross-sections of a wound below the skin: first, fingers push a long strip of gauze into the wound until it is filled; second, two hands stacked on top press straight down hard.',
     ['12-02'])
def wound_packing():
    b = []
    bb, lm = body_front(64, 28, 1.0)
    b.append(bb)
    b.append(rect(42, 66, 44, 68, RED, RED, 1.2, 4, 0.18))
    for k in ('neck', 'armpit', 'groin'):
        x, y = lm[k]
        b.append(circle(x, y, 6, GREEN, GREEN, 2, 0.35))
    b.append(tl(4, 248, [('PACK: groin,', True), ('armpit, neck', True)], 11.5, 14, fill=GREEN))
    b.append(tl(4, 286, [('NEVER pack chest', True), ('or belly: cover', True), ('and press.', True)], 11.5, 14, fill=RED))
    # cross-section 1
    x0 = 150

    def section(y):
        return (path(f'M{x0},{y} L{x0 + 50},{y} C{x0 + 56},{y + 56} {x0 + 108},{y + 56} {x0 + 114},{y} L{x0 + 200},{y}', INK, sw=2) +
                path(f'M{x0 + 50},{y} C{x0 + 56},{y + 56} {x0 + 108},{y + 56} {x0 + 114},{y} Z', RED, RED, 0, 0.15) +
                t(x0 + 176, y - 6, 'skin', 10.5, 'middle'))
    y1 = 104
    b.append(t(x0, 18, '1. Push gauze in with your', 12.5, weight='bold') + t(x0 + 15, 33, 'fingers until it is full.', 12.5, weight='bold'))
    b.append(section(y1))
    b.append(path(f'M{x0 + 62},{y1 + 6} l40,0 l-36,10 l32,0 l-28,10 l24,0 l-18,8 l10,0', INK, sw=2.2))
    b.append(path(f'M{x0 + 102},{y1 + 6} C{x0 + 120},{y1 - 20} {x0 + 140},{y1 - 34} {x0 + 170},{y1 - 34}', INK, sw=2.2))
    b.append(circle(x0 + 182, y1 - 34, 12, INK, INK, 1.6, 0.1) + t(x0 + 182, y1 - 52, 'gauze', 10.5, 'middle'))
    b.append(path(f'M{x0 + 70},{y1 - 46} L{x0 + 80},{y1 + 2} M{x0 + 84},{y1 - 48} L{x0 + 90},{y1 + 2}', INK, sw=7, op=0.35))
    b.append(t(x0 + 64, y1 - 52, 'fingers', 10.5, 'end'))
    # cross-section 2
    y2 = 270
    b.append(t(x0, y2 - 102, '2. Press hard on top. Keep', 12.5, weight='bold'))
    b.append(t(x0 + 15, y2 - 87, 'pressing; do not lift to check.', 12.5, weight='bold'))
    b.append(section(y2))
    b.append(path(f'M{x0 + 56},{y2 + 4} C{x0 + 64},{y2 + 44} {x0 + 100},{y2 + 44} {x0 + 108},{y2 + 4} Z', INK, INK, 1.4, 0.35))
    b.append(rect(x0 + 50, y2 - 24, 64, 20, INK, INK, 1.6, 8, 0.12) + rect(x0 + 54, y2 - 40, 56, 16, INK, INK, 1.6, 7, 0.12))
    b.append(t(x0 + 82, y2 - 10, 'hand', 9.5, 'middle') + t(x0 + 82, y2 - 28, 'hand', 9.5, 'middle'))
    for dx in (62, 102):
        b.append(arrow(x0 + dx, y2 - 66, x0 + dx, y2 - 44, RED, 2.2, 7))
    b.append(t(x0 + 120, y2 - 34, 'stacked,', 10.5) + t(x0 + 120, y2 - 22, 'arms straight', 10.5))
    b.append(tl(x0, y2 + 64, ['Hemostatic gauze or plain gauze.', 'Keep them warm and lying flat.'], 11.5, 14))
    return svg('fig-wound-packing', 380, '\n'.join(b), 'Packing a wound where a tourniquet cannot go')


SKIN = INK


def figure_g(parts, color=INK, op=0.32, w=14):
    """Body as thick round strokes in one group, so overlaps do not darken.
    parts: list of ('l', [(x,y),...], width) polylines or ('c', (x,y), r) heads."""
    out = []
    for p in parts:
        if p[0] == 'c':
            (x, y), r = p[1], p[2]
            out.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{color}"/>')
        else:
            pts, ww = p[1], (p[2] if len(p) > 2 else w)
            d = 'M' + ' L'.join(f'{x},{y}' for x, y in pts)
            out.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{ww}" stroke-linecap="round" stroke-linejoin="round"/>')
    return f'<g opacity="{op}">' + ''.join(out) + '</g>'


def floor(y, x1=0, x2=360):
    return line(x1, y, x2, y, INK, 1.6, op=0.6)


def supine(x, y, scale=1.0, child=False):
    """Person lying on the back, head at left; returns (svg, chest point)."""
    s = scale
    hr = 13 * s if not child else 13 * s
    parts = [('c', (x + 14 * s, y - 14 * s), hr),
             ('l', [(x + 32 * s, y - 13 * s), (x + 120 * s, y - 13 * s)], 26 * s),
             ('l', [(x + 118 * s, y - 10 * s), (x + 196 * s, y - 8 * s), (x + 230 * s, y - 14 * s)], 16 * s),
             ('l', [(x + 40 * s, y - 6 * s), (x + 100 * s, y - 4 * s)], 9 * s)]
    return figure_g(parts), (x + 62 * s, y - 27 * s)


def kneeler(hx, hy, color=BLUE, s=1.0, hands='stack'):
    """Rescuer kneeling, arms straight down to hands at (hx, hy)."""
    sh = (hx + 6 * s, hy - 66 * s)
    hip = (hx + 40 * s, hy - 20 * s)
    knee = (hx + 44 * s, hy + 26 * s)
    foot = (hx + 92 * s, hy + 28 * s)
    parts = [('c', (sh[0] - 6 * s, sh[1] - 22 * s), 12 * s),
             ('l', [sh, hip], 22 * s), ('l', [hip, knee, foot], 15 * s),
             ('l', [sh, (hx, hy - 4 * s)], 9 * s)]
    return figure_g(parts, color, 0.55)


@fig('fig-cpr-adult',
     'Adult CPR: heel of one hand on the centre of the chest, other hand on top, fingers interlaced, arms straight, shoulders over the hands. Push about 2 inches (5 cm) deep, 100 to 120 a minute, let the chest come fully back up. 30 compressions to 2 breaths.',
     'Side view of a person lying on their back on the floor and a rescuer kneeling beside them, arms straight, shoulders directly above two stacked hands on the centre of the chest. An arrow shows the push of about 2 inches. An inset shows the heel of one hand on the chest with the other hand on top, fingers laced and lifted.',
     ['12-18'])
def cpr_adult():
    b = [floor(204)]
    body, chest = supine(10, 204)
    b.append(kneeler(chest[0], chest[1] - 2))
    b.append(body)
    b.append(rect(chest[0] - 9, chest[1] - 12, 18, 10, BLUE, BLUE, 1.4, 4, 0.5))
    b.append(arrow(chest[0] - 26, chest[1] - 40, chest[0] - 26, chest[1] - 4, RED, 2.4, 8))
    b.append(t(8, chest[1] - 50, 'about 2 in', 11.5, 'start', 'bold', RED))
    b.append(tl(4, 28, [('ADULT', True)], 15))
    # inset hands
    ix, iy = 252, 40
    b.append(rect(ix - 10, iy - 22, 112, 96, INK, 'none', 1, 6, op=0.5))
    b.append(t(ix + 46, iy - 8, 'hands', 10.5, 'middle'))
    b.append(path(f'M{ix},{iy + 40} q40,-10 90,0', INK, sw=1.4, op=0.6) + t(ix + 46, iy + 66, 'centre of chest', 10, 'middle'))
    b.append(rect(ix + 22, iy + 22, 48, 16, BLUE, BLUE, 1.6, 7, 0.25) + rect(ix + 18, iy + 8, 56, 16, BLUE, BLUE, 1.6, 7, 0.4))
    b.append(t(ix + 46, iy + 20, 'fingers laced', 9, 'middle'))
    y = 232
    rows = [('Hands', 'heel of 1 hand, other on top'), ('Depth', 'about 2 in (5 cm)'),
            ('Rate', '100 to 120 a minute (Stayin\' Alive)'), ('Rhythm', '30 : 2, one or two rescuers'),
            ('Recoil', 'let the chest come fully back up')]
    for k, v in rows:
        b.append(t(8, y, k, 12, weight='bold') + t(74, y, v, 12))
        y += 17
    b.append(t(8, y + 6, 'Pulled from water: breaths first. Never hands-only.', 11.5, weight='bold', fill=RED))
    return svg('fig-cpr-adult', y + 30, '\n'.join(b), 'Adult CPR hand position')


@fig('fig-cpr-child',
     'Child CPR (1 year to puberty): heel of one hand on the centre of the chest, other hand on top, about 2 inches (5 cm) deep, 100 to 120 a minute. Head tilt and chin lift for breaths. 30:2 with one rescuer, 15:2 with two.',
     'Side view of a child lying on their back and a kneeling rescuer pressing with the heel of one hand, other hand on top, on the centre of the chest, arms straight. An arrow shows a push of about 2 inches. A second small drawing shows the head tilted back with two fingers lifting the chin.',
     ['12-18'])
def cpr_child():
    b = [floor(204)]
    body, chest = supine(30, 204, 0.72, child=True)
    b.append(kneeler(chest[0], chest[1] - 2, s=1.0))
    b.append(body)
    b.append(rect(chest[0] - 7, chest[1] - 10, 14, 9, BLUE, BLUE, 1.4, 4, 0.5))
    b.append(arrow(chest[0] - 24, chest[1] - 40, chest[0] - 24, chest[1] - 4, RED, 2.4, 8))
    b.append(t(8, chest[1] - 48, 'about 2 in', 11.5, 'start', 'bold', RED))
    b.append(t(4, 28, 'CHILD', 15, weight='bold') + t(4, 44, '1 year to puberty', 11))
    # head tilt inset
    ix, iy = 256, 100
    b.append(rect(ix - 14, iy - 70, 110, 104, INK, 'none', 1, 6, op=0.5))
    b.append(figure_g([('c', (ix + 30, iy - 18), 18), ('l', [(ix + 46, iy - 6), (ix + 92, iy + 4)], 22)], INK, 0.32))
    b.append(path(f'M{ix + 14},{iy - 30} q-8,8 -4,18', INK, sw=1.4) + arrow(ix + 16, iy - 50, ix + 8, iy - 34, INK, 1.4, 5))
    b.append(path(f'M{ix + 22},{iy + 4} l-10,12', BLUE, sw=5) + t(ix + 40, iy + 28, 'tilt head, lift chin', 10, 'middle'))
    y = 232
    rows = [('Hands', 'heel of 1 hand, other on top'), ('Depth', 'about 2 in (5 cm)'),
            ('Rate', '100 to 120 a minute'), ('Rhythm', '30 : 2 alone; 15 : 2 with two rescuers'),
            ('Breaths', 'pinch nose, seal mouth, 1 second')]
    for k, v in rows:
        b.append(t(8, y, k, 12, weight='bold') + t(74, y, v, 12))
        y += 17
    b.append(t(8, y + 6, 'Alone: about 2 minutes of CPR before going for help.', 11.5, weight='bold'))
    return svg('fig-cpr-child', y + 30, '\n'.join(b), 'Child CPR hand position')


def infant(x, y, s=1.0, face='up'):
    parts = [('c', (x, y - 11 * s), 11 * s), ('l', [(x + 14 * s, y - 10 * s), (x + 50 * s, y - 10 * s)], 20 * s),
             ('l', [(x + 50 * s, y - 8 * s), (x + 78 * s, y - 8 * s)], 11 * s)]
    return figure_g(parts, INK, 0.32)


@fig('fig-cpr-infant',
     'Infant CPR (under 1 year): two thumbs side by side on the centre of the chest just below the nipple line, hands wrapped round the chest; or the heel of one hand if you cannot press deep enough. About 1½ inches (4 cm) deep, 100 to 120 a minute. No two-finger compressions. Cover mouth and nose with your mouth.',
     'Left: an infant on its back on a firm surface, head in a neutral sniffing position, with the heel of one hand pressing the breastbone just below the nipples and an arrow showing about 1½ inches. Right: seen from above, two hands wrap around the infant\'s chest with both thumbs side by side on the breastbone, the first choice.',
     ['12-18'])
def cpr_infant():
    b = [t(4, 24, 'INFANT', 15, weight='bold') + t(4, 40, 'under 1 year', 11)]
    b.append(rect(14, 130, 150, 8, INK, INK, 1.2, 2, 0.2) + t(88, 154, 'firm, flat surface', 10.5, 'middle'))
    b.append(infant(36, 130, 1.3))
    cx = 36 + 36
    b.append(path(f'M{cx - 3},{106} L{cx - 3},{60} M{cx + 3},{106} L{cx + 3},{60}', BLUE, sw=13, op=0.55))
    b.append(rect(cx - 12, 46, 24, 16, BLUE, BLUE, 1.2, 6, 0.35))
    b.append(t(cx + 14, 64, 'or heel of', 10.5, fill=BLUE) + t(cx + 14, 76, '1 hand', 10.5, fill=BLUE))
    b.append(t(cx + 14, 88, 'just below', 10.5) + t(cx + 14, 100, 'nipple line', 10.5))
    b.append(arrow(cx - 22, 70, cx - 22, 104, RED, 2.2, 7) + tl(cx - 28, 64, [('about', True), ('1½ in', True)], 11, 12.5, 'end', fill=RED))
    # two-thumb technique, top view
    ox, oy = 250, 86
    b.append(t(ox + 6, 28, 'First choice:', 11.5, 'middle', 'bold') + t(ox + 6, 42, 'two thumbs, hands', 10.5, 'middle') + t(ox + 6, 54, 'encircling the chest', 10.5, 'middle'))
    b.append(circle(ox + 6, oy - 4, 14, INK, INK, 1.4, 0.2))
    b.append(rect(ox - 20, oy + 10, 52, 66, INK, INK, 1.4, 20, 0.15))
    b.append(path(f'M{ox - 22},{oy + 30} q-14,20 2,38 M{ox + 34},{oy + 30} q14,20 -2,38', BLUE, sw=8, op=0.45))
    b.append(rect(ox - 3, oy + 34, 8, 18, BLUE, BLUE, 1.4, 4, 0.6) + rect(ox + 7, oy + 34, 8, 18, BLUE, BLUE, 1.4, 4, 0.6))
    b.append(t(ox + 6, oy + 92, 'seen from above', 10, 'middle', italic=True))
    y = 204
    rows = [('Depth', 'about 1½ in (4 cm)'), ('Rate', '100 to 120 a minute'),
            ('Rhythm', '30 : 2 alone; 15 : 2 with two rescuers'), ('Breaths', 'mouth over mouth AND nose'),
            ('Head', 'neutral "sniffing" position, not')]
    for k, v in rows:
        b.append(t(8, y, k, 12, weight='bold') + t(74, y, v, 12))
        y += 17
    b.append(t(74, y - 2, 'tipped far back', 12))
    return svg('fig-cpr-infant', y + 26, '\n'.join(b), 'Infant CPR thumb and hand positions')


@fig('fig-choking-infant',
     'Choking infant under 1: five firm back blows with the baby face-down along your forearm, head lower than chest, jaw supported; then turn face-up for five chest thrusts with the heel of one hand on the middle of the breastbone, just below the nipples. Never abdominal thrusts under 1.',
     'Two panels. Left: a seated adult rests a forearm on the thigh with the infant lying face-down along it, head lower than the chest and the jaw held in the hand; the palm of the other hand strikes between the shoulder blades, marked 5 back blows. Right: the infant face-up along the forearm, head lower, with the heel of one hand on the middle of the breastbone just below the nipples, marked 5 chest thrusts.',
     ['12-18'])
def choking_infant():
    b = []

    def panel(x0, face):
        out = []
        # thigh and forearm sloping down to the left (head end)
        out.append(figure_g([('l', [(x0 + 150, 160), (x0 + 30, 172)], 30)], BLUE, 0.3))
        out.append(t(x0 + 120, 196, 'your thigh', 10, 'middle'))
        out.append(figure_g([('l', [(x0 + 150, 128), (x0 + 22, 146)], 12), ('c', (x0 + 18, 147), 9)], BLUE, 0.55))
        out.append(t(x0 + 120, 118, 'forearm', 10, 'middle', fill=BLUE))
        # infant along forearm, head at left lower
        out.append(figure_g([('c', (x0 + 26, 128), 12), ('l', [(x0 + 42, 124), (x0 + 82, 118)], 20), ('l', [(x0 + 82, 118), (x0 + 112, 112)], 11)], INK, 0.38))
        return ''.join(out)
    b.append(t(8, 18, '1. Face-down, head lower', 12.5, weight='bold'))
    b.append(panel(0, 'down'))
    b.append(figure_g([('l', [(96, 56), (72, 100)], 11)], BLUE, 0.55))
    b.append(arrow(96, 60, 70, 104, RED, 2.4, 8))
    b.append(tl(8, 220, [('5 back blows,', True), 'palm of your hand, between', 'the shoulder blades.', 'Hold the jaw, not the throat.'], 11.5, 14))
    b.append(line(180, 6, 180, 280, INK, 0.8, op=0.4))
    b.append(t(188, 18, '2. Turn face-up, head lower', 12.5, weight='bold'))
    b.append(panel(180, 'up'))
    b.append(path('M241,62 L241,106 M247,62 L247,106', BLUE, sw=12, op=0.55))
    b.append(arrow(226, 66, 226, 104, RED, 2.2, 7))
    b.append(tl(188, 220, [('5 chest thrusts,', True), 'heel of 1 hand, middle', 'of the breastbone, just', 'below the nipples.'], 11.5, 14))
    b.append(rect(6, 288, 348, 52, RED, RED, 1.6, 5, 0.06))
    b.append(tl(14, 306, [('Repeat 5 and 5. NEVER abdominal thrusts under 1.', True), ('Never hold an infant upside down by the feet.', True),
                          'Remove only what you can see. Limp: start CPR.'], 11, 13.5, fill=RED))
    return svg('fig-choking-infant', 362, '\n'.join(b), 'Choking infant: back blows and chest thrusts')


@fig('fig-choking-child-adult',
     'Choking, age 1 to adult: bend them forward and give five back blows between the shoulder blades, then five abdominal thrusts from behind, fist just above the navel, in and up. Kneel behind a small child. Pregnant or too big to reach round: chest thrusts.',
     'Three panels. Left: a standing person bent forward at the waist, a rescuer beside them supporting the chest with one arm and striking between the shoulder blades with the heel of the other hand, marked 5 back blows. Middle: the rescuer standing behind with arms around, a fist just above the navel, arrow in and up, marked 5 abdominal thrusts. Right: the rescuer kneeling behind a small child doing the same.',
     ['12-18'])
def choking_adult():
    b = []
    gy = 228
    b.append(floor(gy))
    # 1. back blows: patient bent forward
    b.append(t(6, 18, '1. 5 back blows', 12.5, weight='bold'))
    b.append(figure_g([('c', (36, 88), 12), ('l', [(50, 90), (96, 76)], 22), ('l', [(98, 80), (100, 150), (96, gy - 6)], 15),
                       ('l', [(56, 92), (50, 128)], 8)], INK, 0.32))
    b.append(figure_g([('c', (110, 36), 12), ('l', [(110, 50), (114, 124)], 20), ('l', [(114, 126), (120, 176), (118, gy - 6)], 14),
                       ('l', [(108, 58), (84, 64)], 8), ('l', [(106, 58), (64, 100)], 8)], BLUE, 0.5))
    b.append(arrow(94, 58, 78, 72, RED, 2.4, 7))
    b.append(t(60, gy + 16, 'heel of the hand,', 10.5, 'middle') + t(60, gy + 28, 'between shoulder blades', 10.5, 'middle'))
    # 2. abdominal thrusts standing
    x = 146
    b.append(line(x - 6, 6, x - 6, gy + 34, INK, 0.8, op=0.4))
    b.append(t(x, 18, '2. 5 abdominal thrusts', 12.5, weight='bold'))
    b.append(figure_g([('c', (x + 74, 40), 12), ('l', [(x + 76, 54), (x + 80, 130)], 22), ('l', [(x + 80, 130), (x + 82, gy - 6)], 15)], BLUE, 0.5))
    b.append(figure_g([('c', (x + 40, 44), 12), ('l', [(x + 40, 58), (x + 42, 132)], 24), ('l', [(x + 42, 132), (x + 40, gy - 6)], 16)], INK, 0.32))
    b.append(line(x + 34, 110, x + 80, 94, BLUE, 6, op=0.5) + circle(x + 30, 112, 7, BLUE, BLUE, 1.6, 0.7))
    b.append(arrow(x + 14, 126, x + 28, 104, RED, 2.4, 7))
    b.append(t(x + 104, 64, 'fist just', 10.5) + t(x + 104, 76, 'above the', 10.5) + t(x + 104, 88, 'navel:', 10.5) + t(x + 104, 100, 'IN and UP', 10.5, weight='bold', fill=RED))
    # 3. kneel behind small child
    x3 = 270
    b.append(line(x3 - 8, 120, x3 - 8, gy + 34, INK, 0.8, op=0.4))
    b.append(t(x3 - 2, 134, '3. Small child:', 11.5, weight='bold') + t(x3 - 2, 148, 'kneel behind', 11.5, weight='bold'))
    b.append(figure_g([('c', (x3 + 66, 168), 11), ('l', [(x3 + 66, 182), (x3 + 70, 206)], 18), ('l', [(x3 + 70, 206), (x3 + 60, gy - 4), (x3 + 88, gy - 4)], 13)], BLUE, 0.5))
    b.append(figure_g([('c', (x3 + 36, 186), 9), ('l', [(x3 + 36, 196), (x3 + 38, 212)], 16), ('l', [(x3 + 38, 212), (x3 + 38, gy - 4)], 10)], INK, 0.32))
    y = gy + 50
    b.append(tl(6, y, [('Alternate 5 and 5 until it clears or they go limp.', True), 'Pregnant, or too big to reach round: CHEST thrusts.',
                       'Limp: lower them to the ground and start CPR.', 'Coughing hard, speaking or crying: do not hit or thrust.'], 11.5, 14.5))
    return svg('fig-choking-child-adult', y + 72, '\n'.join(b), 'Choking age 1 and up: back blows and abdominal thrusts')


@fig('fig-recovery-position',
     'Recovery position: on their side, top knee bent forward to stop them rolling, head tilted back and mouth pointing down so vomit drains and the airway stays open. Check breathing.',
     'Seen from above, a person lying on their side. The lower arm is out in front, the upper hand is under the cheek, the head is tilted back with the mouth pointing toward the ground, and the upper leg is bent forward at hip and knee so the knee rests on the ground in front of the body.',
     ['12-17', '02-01', '02-11', '02-17'])
def recovery_position():
    b = [t(8, 16, 'Seen from above, lying on the left side', 11.5, italic=True)]
    parts = [('c', (60, 96), 16),
             ('l', [(78, 98), (190, 100)], 34),
             ('l', [(190, 104), (300, 108), (340, 104)], 15),   # lower leg straight
             ('l', [(192, 94), (236, 142), (292, 146)], 16),    # upper leg bent forward
             ('l', [(84, 86), (50, 56), (20, 50)], 10),         # lower arm out in front (up on screen = in front? keep)
             ('l', [(96, 110), (66, 120), (56, 108)], 10)]       # upper hand under cheek
    b.append(figure_g(parts, INK, 0.33))
    b.append(arrow(30, 112, 38, 104, RED, 2, 6) + tl(8, 138, [('mouth points', True), ('down', True)], 11, 13, fill=RED))
    b.append(t(100, 66, 'head tilted back', 10.5))
    b.append(t(96, 140, 'hand under cheek', 10.5))
    b.append(tl(236, 172, [('top knee bent', True), ('forward', True)], 11.5, 14, 'middle', fill=GREEN))
    b.append(tl(8, 214, [('Check breathing again and again.', True), 'Stops breathing: on the back, start CPR (→ 12-18).'], 11.5, 14.5))
    return svg('fig-recovery-position', 252, '\n'.join(b), 'Recovery position')

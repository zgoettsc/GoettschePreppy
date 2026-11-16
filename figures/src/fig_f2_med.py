"""F2: first-aid and medical-condition diagrams (new ids only; F1's figures stay in fig_medical.py)."""
from figlib import *
from fig_medical import figure_g, floor, supine
FIGS = {}


def fig(fid, caption, alt, pages):
    def deco(fn):
        FIGS[fid] = dict(fn=fn, caption=caption, alt=alt, pages=pages)
        return fn
    return deco


def rule(y, x1=4, x2=356):
    return line(x1, y, x2, y, INK, 0.8, op=0.4)


def box(x, y, w, h, color=RED, op=0.06):
    return rect(x, y, w, h, color, color, 1.6, 5, op)


def hand_top(x, y, s=1.0, color=INK, op=0.3, fingers=True):
    """A hand seen palm-up, wrist at the bottom, (x, y) = centre of the wrist."""
    S = lambda v: round(v * s, 1)
    out = [f'<path d="M{x - S(11)},{y} L{x - S(15)},{y - S(18)} L{x - S(18)},{y - S(50)} L{x + S(18)},{y - S(50)} L{x + S(16)},{y - S(22)} L{x + S(11)},{y} Z" fill="{color}" stroke="{color}" stroke-width="{S(6)}" stroke-linejoin="round"/>']
    if fingers:
        for dx, ln in ((-14, 30), (-4.5, 36), (5, 34), (14, 26)):
            out.append(f'<path d="M{x + S(dx)},{y - S(46)} L{x + S(dx * 1.05)},{y - S(50 + ln)}" stroke="{color}" stroke-width="{S(8.5)}" stroke-linecap="round" fill="none"/>')
        out.append(f'<path d="M{x + S(16)},{y - S(18)} L{x + S(28)},{y - S(32)} L{x + S(34)},{y - S(46)}" stroke="{color}" stroke-width="{S(9)}" stroke-linecap="round" stroke-linejoin="round" fill="none"/>')
    return f'<g opacity="{op}">' + ''.join(out) + '</g>'


def head_side(x, y, r=26, color=INK, op=0.3, nose='up'):
    """Head lying on its back, seen from the side; nose points up."""
    b = figure_g([('c', (x, y), r)], color, op)
    b += path(f'M{x + r * 0.15},{y - r * 0.96} l{r * 0.12},{-r * 0.3} l{r * 0.2},{r * 0.28}', color, sw=2, op=0.6)
    return b


# ---------------------------------------------------------------- anaphylaxis

@fig('fig-anaphylaxis-positions',
     'Anaphylaxis positions (AAP Allergy and Anaphylaxis Emergency Plan, as on 02-03): keep them lying on their back; if they vomit or have trouble breathing, keep them lying on their side. Keep them lying down: do not stand them up or walk them.',
     'Two panels. Top: a person lying flat on their back on the floor, labelled usual position. Bottom: seen from above, a person lying on their side with the knees bent forward and the mouth pointing down, labelled if vomiting or having trouble breathing. Below, a red bar: keep them lying down, do not stand them up or walk them.',
     ['02-03'])
def anaphylaxis_positions():
    b = [t(6, 18, '1. Lying on their back', 13, weight='bold'), t(6, 34, 'the usual position', 11)]
    b.append(floor(118))
    body, _ = supine(40, 118, 1.15)
    b.append(body + path('M62,84 l4,-8 l5,7', INK, sw=2, op=0.7))
    b.append(t(70, 74, 'face up', 10.5, italic=True))
    b.append(rule(134))
    b.append(t(6, 156, '2. Vomiting or trouble breathing:', 13, weight='bold'))
    b.append(t(6, 172, 'lying on their SIDE (seen from above)', 11))
    parts = [('c', (62, 232), 15), ('l', [(80, 234), (180, 236)], 30),
             ('l', [(182, 230), (232, 272), (290, 276)], 14), ('l', [(184, 242), (290, 246), (330, 244)], 14),
             ('l', [(90, 222), (64, 196), (40, 194)], 9)]
    b.append(figure_g(parts, INK, 0.33))
    b.append(arrow(44, 244, 36, 254, RED, 2, 6) + tl(6, 276, ['mouth', 'points down'], 10.5, 12.5, fill=RED))
    b.append(t(236, 302, 'knees bent', 10.5, 'middle'))
    y = 320
    b.append(box(6, y, 348, 46))
    b.append(tl(16, y + 19, [('Keep them lying down.', True), ('Do NOT stand them up or walk them.', True)], 12, 15, fill=RED))
    b.append(tl(8, y + 68, ['Second dose if symptoms get worse, continue, or do', 'not get better in 5 minutes (AAP plan; → 02-03).'], 11, 13.5))
    return svg('fig-anaphylaxis-positions', y + 104, '\n'.join(b), 'Anaphylaxis: lying positions')


@fig('fig-auto-injector-outer-thigh',
     'Epinephrine auto-injector: into the outer thigh, through clothing if needed, following the device\'s own instructions. For one common pen the label says hold it in place for 3 seconds, then massage the area for 10 seconds. Note the time.',
     'Front view of two legs from the hips to the knees. A shaded oval on the outside of the middle of the right thigh marks where the auto-injector goes; the pen is drawn pressed straight against the outer thigh from the side, through a trouser leg. Notes beside it: through clothing if needed; follow your device\'s own instructions; one common pen, hold 3 seconds then massage 10 seconds; note the time.',
     ['02-03'])
def auto_injector():
    b = [t(6, 18, 'Front view, hips to knees', 11.5, italic=True)]
    # legs (trousers)
    b.append(path('M60,40 L176,40 L172,96 L162,236 L124,236 L118,120 L112,236 L74,236 L64,96 Z', INK, INK, 1.8, 0.07))
    b.append(line(118, 52, 118, 120, INK, 1.2, op=0.5))
    # target on outer right thigh
    b.append(f'<ellipse cx="164" cy="140" rx="9" ry="26" fill="{AMBER}" fill-opacity="0.45" stroke="{AMBER}" stroke-width="1.6"/>')
    # pen from the side, perpendicular
    b.append(rect(176, 132, 62, 16, INK, INK, 1.8, 5, 0.15) + rect(238, 134, 14, 12, INK, INK, 1.4, 3, 0.3))
    b.append(rect(170, 135, 8, 10, AMBER, AMBER, 1.4, 2, 0.8))
    b.append(arrow(268, 140, 254, 140, RED, 2.4, 7))
    b.append(t(212, 124, 'pen', 10.5, 'middle'))
    b.append(tl(176, 176, [('OUTER thigh,', True), ('through clothing', False), ('if needed', False)], 11.5, 14, fill=INK))
    b.append(rule(270))
    y = 290
    rows = [('1', 'Follow your own device\'s instructions.'),
            ('2', 'One common pen (FDA label): hold it in place'),
            ('', '3 seconds (count 1, 2, 3), then massage 10 s.'),
            ('3', 'Note the time. Say it aloud or write it.'),
            ('4', 'Lie them down (→ positions figure).')]
    for n, s in rows:
        b.append((t(10, y, n, 12.5, weight='bold', fill=AMBER) if n else '') + t(28, y, s, 12))
        y += 17
    return svg('fig-auto-injector-outer-thigh', y + 16, '\n'.join(b), 'Where an epinephrine auto-injector goes')


# ---------------------------------------------------------------- splints

@fig('fig-splint-joint-above-below',
     'Splinting: splint it as you found it, holding still the joint above and the joint below the break, with padding in every gap. Leave fingers and toes showing so you can check colour, warmth, pulse, feeling and wiggle before and after; if they get worse, loosen it at once. A broken finger can be taped to its neighbour.',
     'Three drawings. Forearm: a rigid splint runs from the palm past the elbow, padding fills the gaps, three ties hold it, and the fingertips are left showing; the elbow and wrist are labelled joint above and joint below. Lower leg: splints on both sides run from above the knee to past the foot, padded, tied in several places, toes showing; knee and ankle labelled. Finger: the injured finger taped to the finger beside it with two bands of tape and padding between them. Below: check before and after, loosen at once if worse, re-check often.',
     ['12-09'])
def splint():
    b = [t(6, 18, '1. Forearm: wrist AND elbow held still', 12.5, weight='bold')]
    # forearm: elbow left, hand right
    y = 60
    b.append(figure_g([('l', [(20, y), (60, y)], 26), ('l', [(60, y), (232, y + 2)], 22), ('l', [(232, y + 2), (262, y + 2)], 24),
                       ('l', [(262, y), (300, y - 2)], 10), ('l', [(262, y + 6), (298, y + 7)], 9)], INK, 0.3))
    b.append(shade(44, y + 13, 228, 8, AMBER, 0.45) + rect(40, y + 21, 236, 7, INK, INK, 1.6, 2, 0.3))
    for x in (78, 150, 222):
        b.append(rect(x, y - 15, 9, 44, BLUE, BLUE, 1.4, 2, 0.35))
    b.append(path(f'M140,{y - 6} l6,8 l-4,4 l6,8', RED, sw=2))
    b.append(t(143, y - 22, 'break', 10, 'middle', fill=RED))
    b.append(t(60, y + 46, 'elbow', 10.5, 'middle', 'bold') + t(60, y + 58, '(joint above)', 10, 'middle'))
    b.append(t(244, y + 46, 'wrist', 10.5, 'middle', 'bold') + t(244, y + 58, '(joint below)', 10, 'middle'))
    b.append(tl(304, y - 10, ['fingers', 'showing'], 10, 12, fill=GREEN, weight='bold'))
    b.append(t(158, y + 40, 'padding', 10, 'middle', fill=AMBER) + t(186, y - 22, 'ties', 10, fill=BLUE))
    b.append(rule(134))
    b.append(t(6, 154, '2. Lower leg: knee AND ankle held still', 12.5, weight='bold'))
    y2 = 196
    b.append(figure_g([('l', [(14, y2), (110, y2 + 2)], 30), ('l', [(110, y2 + 2), (262, y2 + 4)], 22), ('l', [(262, y2 + 4), (290, y2 + 4), (300, y2 - 22)], 14)], INK, 0.3))
    b.append(shade(46, y2 - 22, 262, 7, AMBER, 0.45) + shade(46, y2 + 16, 262, 7, AMBER, 0.45))
    b.append(rect(42, y2 - 29, 270, 7, INK, INK, 1.6, 2, 0.3) + rect(42, y2 + 23, 270, 7, INK, INK, 1.6, 2, 0.3))
    for x in (64, 140, 214, 286):
        b.append(rect(x, y2 - 33, 9, 67, BLUE, BLUE, 1.4, 2, 0.35))
    b.append(path(f'M176,{y2 - 8} l6,8 l-4,4 l6,8', RED, sw=2))
    b.append(t(110, y2 + 50, 'knee (joint above)', 10, 'middle') + t(262, y2 + 50, 'ankle (joint below)', 10, 'middle'))
    b.append(tl(312, y2 - 40, ['toes', 'showing'], 10, 12, fill=GREEN, weight='bold'))
    b.append(rule(262))
    b.append(t(6, 282, '3. Finger: tape it to its neighbour', 12.5, weight='bold'))
    fx = 70
    b.append(figure_g([('l', [(fx, 400), (fx, 330)], 18), ('l', [(fx + 20, 400), (fx + 20, 322)], 18)], INK, 0.3))
    b.append(shade(fx + 7, 326, 6, 70, AMBER, 0.6))
    b.append(rect(fx - 12, 338, 44, 10, BLUE, BLUE, 1.4, 2, 0.4) + rect(fx - 12, 370, 44, 10, BLUE, BLUE, 1.4, 2, 0.4))
    b.append(tl(fx + 46, 330, [('Two bands of tape,', False), ('padding between the', False), ('fingers, joints left free', False), ('to bend.', False)], 11, 13.5))
    b.append(t(fx - 4, 418, 'injured + neighbour', 10, 'start', italic=True))
    y = 446
    b.append(box(6, y - 16, 348, 82, INK, 0.05))
    b.append(tl(14, y, [('Splint it as found: do not straighten it.', True), 'Check colour, warmth, pulse, feeling and wiggle',
                       'BEFORE and AFTER. Worse? Loosen it at once.', ('Re-check often: swelling builds for hours.', True)], 11.5, 15))
    return svg('fig-splint-joint-above-below', y + 84, '\n'.join(b), 'Splints: the joint above and the joint below')


# ---------------------------------------------------------------- stroke

@fig('fig-stroke-fast',
     'Stroke, F.A.S.T. (American Stroke Association): Face drooping, Arm weakness, Speech difficulty, Time to call 911 and note when it started. Any one sign means act. If the person has diabetes and a meter is at hand, check blood sugar first: a low can look exactly like a stroke. No aspirin for a possible stroke.',
     'An amber bar across the top reads: diabetes and a meter or sensor, check blood sugar first, a low looks like a stroke. Below it, four tiles. F: a face with one side of the mouth drooping, ask for a smile. A: a person with both arms raised and one drifting down. S: a speech bubble with jumbled words, slurred or wrong words. T: a clock, note the time it started and go. At the bottom: any one sign means act; no aspirin for a possible stroke.',
     ['02-09', '12-16'])
def stroke_fast():
    b = [rect(4, 4, 352, 50, AMBER, AMBER, 1.8, 6, 0.14)]
    b.append(tl(14, 24, [('FIRST, if they have diabetes and a meter or sensor:', True), 'check blood sugar. A low looks exactly like a stroke.'], 11.5, 15))
    tiles = [('F', 'Face drooping', ['Ask for a smile:', 'one side sags.']),
             ('A', 'Arm weakness', ['Raise both arms:', 'one drifts down.']),
             ('S', 'Speech difficulty', ['Slurred, wrong words,', 'cannot repeat a', 'simple sentence.']),
             ('T', 'Time', ['Note the time it', 'started. Call 911', 'or go now.'])]
    for i, (L, title, sub) in enumerate(tiles):
        x = 4 + (i % 2) * 178
        y = 66 + (i // 2) * 164
        b.append(rect(x, y, 174, 156, INK, 'none', 1.4, 6))
        b.append(t(x + 10, y + 30, L, 28, weight='bold', fill=RED) + t(x + 36, y + 26, title, 12.5, weight='bold'))
        cx, cy = x + 112, y + 74
        if L == 'F':
            b.append(circle(cx, cy, 26, INK, INK, 1.8, 0.06) + circle(cx - 9, cy - 7, 2.5, INK, INK) + circle(cx + 9, cy - 5, 2.5, INK, INK))
            b.append(path(f'M{cx - 12},{cy + 8} Q{cx - 2},{cy + 14} {cx + 4},{cy + 13} Q{cx + 10},{cy + 14} {cx + 13},{cy + 19}', INK, sw=2))
            b.append(arrow(cx + 32, cy + 6, cx + 32, cy + 20, RED, 1.8, 6))
        elif L == 'A':
            b.append(figure_g([('c', (cx, cy - 24), 9), ('l', [(cx, cy - 12), (cx, cy + 26)], 14),
                               ('l', [(cx - 5, cy - 8), (cx - 32, cy - 22)], 7), ('l', [(cx + 5, cy - 8), (cx + 30, cy + 4)], 7)], INK, 0.35))
            b.append(path(f'M{cx + 34},{cy - 30} A40,40 0 0 1 {cx + 38},{cy - 4}', RED, sw=1.8) + arrow(cx + 38, cy - 10, cx + 37, cy - 2, RED, 1.8, 6))
        elif L == 'S':
            b.append(path(f'M{cx - 34},{cy - 22} h66 a6,6 0 0 1 6,6 v26 a6,6 0 0 1 -6,6 h-40 l-12,12 v-12 h-14 a6,6 0 0 1 -6,-6 v-26 a6,6 0 0 1 6,-6 Z', INK, INK, 1.6, 0.06))
            b.append(t(cx + 4, cy, 'wh..t? ma', 11, 'middle', italic=True) + t(cx + 4, cy + 13, 'tt..er', 11, 'middle', italic=True))
        else:
            b.append(circle(cx, cy - 2, 24, INK, INK, 1.8, 0.06) + line(cx, cy - 2, cx, cy - 18, INK, 2.2) + line(cx, cy - 2, cx + 12, cy + 4, INK, 2.2))
        b.append(tl(x + 10, y + 118, sub, 11, 13))
    y = 66 + 2 * 164 + 18
    b.append(box(4, y - 8, 352, 46))
    b.append(tl(14, y + 10, [('Any ONE sign means act. Sudden and one-sided.', True), ('No aspirin for a possible stroke.', True)], 12, 15, fill=RED))
    return svg('fig-stroke-fast', y + 64, '\n'.join(b), 'F.A.S.T. stroke check')


# ---------------------------------------------------------------- burns

@fig('fig-burn-palm-rule',
     'The palm rule: the burned person\'s own palm is about 1% of their body surface (palm and fingers together about 0.8 to 1%). Count with their palm, not yours: an adult\'s palm on a toddler gives the wrong answer. Count blistered or worse skin; redness alone does not count.',
     'Left: an open hand, palm up, with the palm and fingers shaded and the label: their own palm, about 1 percent of their body. Right: a large adult hand beside a small toddler hand, with the adult hand crossed out for measuring a toddler: use the burned person\'s own palm. Below: count blistered or worse, not redness; an adult with about 10 of their own palms or more of blistered burn needs care; any child\'s burn bigger than a few of their own palms is serious.',
     ['12-03'])
def burn_palm():
    b = [t(6, 18, 'THEIR OWN palm', 13, weight='bold')]
    b.append(hand_top(84, 196, 1.45, AMBER, 0.45))
    b.append(tl(6, 222, [('palm ≈ 1% of their body', True), 'palm + fingers ≈ 0.8 to 1%'], 11.5, 14))
    b.append(line(178, 8, 178, 250, INK, 0.8, op=0.4))
    b.append(t(188, 18, 'Measure a toddler with', 12, weight='bold') + t(188, 33, 'the toddler\'s palm', 12, weight='bold'))
    b.append(hand_top(232, 196, 1.15, INK, 0.25))
    b.append(cross(206, 98, 52, 60, RED, 3))
    b.append(t(232, 214, 'adult', 10.5, 'middle', fill=RED))
    b.append(hand_top(312, 196, 0.62, AMBER, 0.5))
    b.append(check(302, 120, 16))
    b.append(t(312, 214, 'toddler', 10.5, 'middle', fill=GREEN))
    b.append(rule(256))
    y = 278
    b.append(tl(8, y, [('Count blistered or worse. Redness alone does not count.', True),
                       'Adult: about 10 of their own palms or more (10%)',
                       '   → move toward whatever care exists (→ 12-03).',
                       'Child: a burn bigger than a few of their own palms',
                       '   is serious. Any burn on an infant counts.'], 11.5, 15.5))
    return svg('fig-burn-palm-rule', y + 94, '\n'.join(b), 'Sizing a burn with the palm rule')


# ---------------------------------------------------------------- wound closure

@fig('fig-closure-strips',
     'Closure strips are only for the narrow case: a clean, fresh, well-flushed, shallow cut with straight edges that meet without pulling. Lay the strips across the cut with gaps between them. Most wounds (dirty, punctures, bites, hours old, deep, crushed, over a joint) stay open: pack loosely and dress. Unsure? Leave it open.',
     'Two panels. Top, marked with a green tick: a straight shallow cut on the skin closed with five thin strips laid across it, gaps between the strips, the edges meeting without pulling. Bottom, marked leave open: a ragged wound with loose gauze packing in it and a dressing beside it, and a list of wounds never to close: dirty, puncture, bite, more than several hours old, infected, deep, crushed, over a joint, face hands or genitals.',
     ['12-14'])
def closure_strips():
    b = [t(6, 18, 'The narrow case: CLOSE with strips', 12.5, weight='bold', fill=GREEN)]
    b.append(tl(6, 34, ['clean, fresh, flushed, not deep, straight edges that', 'meet without pulling, sure what is underneath'], 11, 13.5))
    b.append(rect(30, 66, 300, 70, INK, INK, 1.2, 10, 0.05))
    b.append(line(70, 101, 290, 101, RED, 2))
    for i in range(6):
        x = 82 + i * 38
        b.append(rect(x, 76, 14, 50, INK, 'white', 1.4, 2) + shade(x, 76, 14, 50, INK, 0.06))
    b.append(t(180, 152, 'strips ACROSS the cut, gaps between them', 11, 'middle'))
    b.append(t(180, 168, 'Glue (if used): on the surface only, never inside.', 10.5, 'middle', italic=True))
    b.append(rule(182))
    b.append(t(6, 204, 'Most wounds: LEAVE OPEN, pack loosely', 12.5, weight='bold', fill=RED))
    b.append(rect(30, 218, 150, 80, INK, INK, 1.2, 10, 0.05))
    b.append(path('M56,258 q12,-20 30,-10 q14,-16 30,-4 q18,-8 34,6 q-10,18 -32,12 q-16,14 -34,4 q-20,8 -28,-8 Z', RED, RED, 1.6, 0.3))
    b.append(path('M70,256 q10,-6 18,0 q8,6 16,-2 q10,-6 18,2 q8,4 14,0', 'white', sw=5) + path('M70,256 q10,-6 18,0 q8,6 16,-2 q10,-6 18,2 q8,4 14,0', INK, sw=1.2))
    b.append(t(105, 314, 'gauze in loosely; dress over', 10.5, 'middle'))
    b.append(tl(194, 226, [('Never close:', True), 'dirty; a puncture; a bite;', 'hours old; infected; deep;', 'crushed; over a joint;', 'edges will not meet;', 'face, hands, genitals.'], 11, 13.5, fill=INK))
    b.append(box(4, 326, 352, 28, RED, 0.06))
    b.append(t(180, 345, 'Unsure? Leave it open.', 13, 'middle', 'bold', RED))
    return svg('fig-closure-strips', 378, '\n'.join(b), 'Closure strips, and the wounds to leave open')


# ---------------------------------------------------------------- naloxone

@fig('fig-naloxone-nasal-spray',
     'Naloxone nasal spray (Narcan 4 mg Drug Facts, as on 02-17): thumb on the bottom of the plunger, nozzle into either nostril, press firmly; each device sprays once. Not awake after 2 to 3 minutes: another dose with a new device, and keep going every 2 to 3 minutes until they wake. Then on their side; not breathing normally, start CPR. Stay with them.',
     'A person lying on their back, seen from the side, with the head tipped slightly back. A hand holds a nasal spray device with the nozzle in one nostril and the thumb on the bottom of the plunger. A box to the right reads: no wake-up in 2 to 3 minutes, next dose with a new device, either nostril, keep going until they wake. Below, numbered steps: spray, call 911, watch and repeat, on their side or CPR, stay.',
     ['02-17'])
def naloxone():
    b = [t(6, 18, 'Lying on their back, seen from the side', 11.5, italic=True)]
    b.append(floor(180, 0, 228))
    b.append(figure_g([('c', (60, 146), 24), ('l', [(84, 154), (210, 156)], 36)], INK, 0.3))
    b.append(path('M48,124 l-3,-10 l10,6', INK, sw=2, op=0.7))
    nx, ny = 50, 114
    b.append(rect(nx - 4, ny - 18, 8, 20, BLUE, BLUE, 1.4, 3, 0.5))
    b.append(rect(nx - 16, ny - 26, 32, 8, BLUE, BLUE, 1.4, 3, 0.4))
    b.append(rect(nx - 7, ny - 58, 14, 32, BLUE, BLUE, 1.4, 3, 0.4))
    b.append(figure_g([('l', [(nx - 12, ny - 34), (nx - 28, ny - 56)], 9), ('l', [(nx + 12, ny - 34), (nx + 28, ny - 56)], 9),
                       ('l', [(nx, ny - 66), (nx + 18, ny - 84)], 11)], INK, 0.35))
    b.append(arrow(nx - 22, ny - 90, nx - 6, ny - 68, RED, 2, 6))
    b.append(t(nx + 34, ny - 72, 'thumb on the bottom', 10.5) + t(nx + 34, ny - 60, 'of the plunger', 10.5))
    b.append(t(nx + 34, ny - 38, 'two fingers either', 10.5) + t(nx + 34, ny - 26, 'side of the nozzle', 10.5))
    b.append(t(nx + 34, ny - 6, 'nozzle in either', 10.5) + t(nx + 34, ny + 6, 'nostril, press firmly', 10.5))
    b.append(rect(238, 30, 118, 120, AMBER, AMBER, 1.6, 6, 0.12))
    b.append(tl(246, 50, [('No wake-up in', True), ('2 to 3 minutes:', True), 'next dose with a', ('NEW device,', True), 'either nostril.', 'Keep going until', 'they wake.'], 11, 13.5))
    y = 204
    steps = [('1', 'Spray: press firmly. Each device sprays once.'), ('2', 'Call 911 if any phone works.'),
             ('3', 'Wait 2 to 3 minutes; repeat as in the box.'), ('4', 'On their side (→ recovery position).'),
             ('', 'Not breathing normally: start CPR (→ 12-18).'), ('5', 'Stay, even if they wake. Very sleepy again:'), ('', 'another dose.')]
    for n, s in steps:
        b.append((t(10, y, n, 12.5, weight='bold', fill=AMBER) if n else '') + t(28, y, s, 12))
        y += 17
    return svg('fig-naloxone-nasal-spray', y + 16, '\n'.join(b), 'Giving naloxone nasal spray')


# ---------------------------------------------------------------- inhaler

@fig('fig-inhaler-with-spacer',
     'Rescue inhaler with a spacer: sit upright, leaning slightly forward; the inhaler fits into the back of the spacer and the mouthpiece goes in the mouth. How many puffs, and when, comes from the person\'s written action plan, not from this picture.',
     'Left: a person sitting upright on a chair, leaning slightly forward, holding a tube-shaped spacer to the mouth with the inhaler fitted into its far end. Right: a close-up of the spacer: the inhaler canister in its plastic boot pushed into the back end, the tube, and the mouthpiece at the front. A box below says the number of puffs comes from the written action plan.',
     ['02-07'])
def inhaler():
    b = [t(6, 18, 'Sit upright, leaning slightly forward', 12, weight='bold')]
    gy = 214
    b.append(floor(gy, 0, 170))
    b.append(path(f'M40,{gy} L40,148 L96,148 L96,{gy} M40,148 L34,70', INK, sw=2.2, op=0.6))
    b.append(figure_g([('c', (78, 58), 13), ('l', [(72, 74), (64, 142)], 22), ('l', [(64, 142), (116, 142), (118, gy - 4)], 14),
                       ('l', [(74, 84), (100, 104), (110, 76)], 8)], INK, 0.32))
    b.append(rect(92, 56, 46, 14, BLUE, BLUE, 1.4, 6, 0.4) + rect(136, 42, 10, 26, BLUE, BLUE, 1.4, 2, 0.55))
    b.append(t(116, 40, 'spacer', 10.5, 'middle', fill=BLUE))
    # close-up
    b.append(line(178, 30, 178, 214, INK, 0.8, op=0.4))
    cx = 190
    b.append(t(cx, 50, 'close-up', 11, italic=True))
    b.append(rect(cx + 24, 96, 96, 40, BLUE, BLUE, 1.6, 12, 0.15))
    b.append(rect(cx + 4, 106, 22, 20, BLUE, BLUE, 1.6, 4, 0.25))
    b.append(rect(cx + 118, 104, 22, 24, INK, INK, 1.6, 4, 0.2))
    b.append(rect(cx + 124, 72, 12, 34, INK, INK, 1.6, 3, 0.35))
    b.append(arrow(cx + 130, 60, cx + 130, 70, RED, 1.8, 6))
    b.append(t(cx + 14, 150, 'mouthpiece', 10, 'middle') + t(cx + 70, 150, 'spacer', 10, 'middle') + t(cx + 134, 150, 'inhaler', 10, 'middle'))
    b.append(t(cx + 70, 92, 'fits into the back', 10, 'middle'))
    b.append(box(4, 232, 352, 48, AMBER, 0.12))
    b.append(tl(14, 252, [('How many puffs, and when: from the person\'s', True), ('written action plan. This picture sets no dose.', True)], 11.5, 15))
    b.append(t(6, 300, 'Danger signs (blue lips, cannot talk): help and CPR, → 12-18.', 11))
    return svg('fig-inhaler-with-spacer', 322, '\n'.join(b), 'Inhaler with a spacer')


# ---------------------------------------------------------------- pressure sores

@fig('fig-pressure-points',
     'Where pressure sores form (MedlinePlus): where bone presses skin against a mattress or seat: back of the head, shoulder blades, elbows, tailbone, hips, knees, ankles, heels and ears. In bed, change position every 1 to 2 hours; in a wheelchair, shift weight every 15 to 20 minutes. Pillows between knees and ankles, under the calves to lift the heels; none under the knees; no donut cushions.',
     'Three outlines. Lying on the back: red dots on the back of the head, shoulder blades, elbow, tailbone and heels, with a pillow under the calves so the heels float. Lying on the side: red dots on the ear, shoulder, hip, knee and ankle, with a pillow between the knees and ankles. Sitting in a wheelchair: red dots on the tailbone and shoulder blades, with the note shift weight every 15 to 20 minutes.',
     ['02-22'])
def pressure_points():
    def dot(x, y):
        return circle(x, y, 5.5, RED, RED, 1.4, 0.6)
    b = [t(6, 18, 'On the back: turn every 1 to 2 hours', 12, weight='bold')]
    gy = 96
    b.append(rect(6, gy, 348, 8, INK, INK, 1.2, 2, 0.12))
    b.append(figure_g([('c', (28, gy - 14), 13), ('l', [(46, gy - 14), (150, gy - 14)], 26), ('l', [(150, gy - 12), (240, gy - 14), (300, gy - 26), (330, gy - 26)], 15),
                       ('l', [(56, gy - 6), (118, gy - 4)], 9)], INK, 0.3))
    b.append(rect(240, gy - 18, 52, 14, BLUE, BLUE, 1.4, 6, 0.3) + t(266, gy + 22, 'pillow under calves:', 10, 'middle', fill=BLUE) + t(266, gy + 34, 'heels float', 10, 'middle', fill=BLUE))
    for x, y in ((18, gy - 4), (60, gy - 3), (100, gy - 2), (150, gy - 3), (334, gy - 18)):
        b.append(dot(x, y))
    b.append(t(18, gy + 22, 'head', 10, 'middle') + t(62, gy + 22, 'shoulder', 10, 'middle') + t(62, gy + 34, 'blades', 10, 'middle'))
    b.append(t(102, gy + 22, 'elbow', 10, 'middle') + t(152, gy + 22, 'tailbone', 10, 'middle') + t(334, gy - 30, 'heel', 10, 'middle'))
    b.append(rule(144))
    b.append(t(6, 164, 'On the side', 12, weight='bold'))
    gy2 = 236
    b.append(rect(6, gy2, 348, 8, INK, INK, 1.2, 2, 0.12))
    b.append(figure_g([('c', (30, gy2 - 16), 15), ('l', [(48, gy2 - 18), (150, gy2 - 20)], 32), ('l', [(150, gy2 - 16), (230, gy2 - 12), (320, gy2 - 10)], 15)], INK, 0.3))
    b.append(rect(220, gy2 - 30, 60, 10, BLUE, BLUE, 1.4, 5, 0.3) + t(250, gy2 - 36, 'pillow between knees and ankles', 10, 'middle', fill=BLUE))
    for x, y in ((24, gy2 - 4), (60, gy2 - 4), (148, gy2 - 4), (226, gy2 - 4), (312, gy2 - 4)):
        b.append(dot(x, y))
    b.append(t(24, gy2 + 22, 'ear', 10, 'middle') + t(60, gy2 + 22, 'shoulder', 10, 'middle') + t(148, gy2 + 22, 'hip', 10, 'middle'))
    b.append(t(226, gy2 + 22, 'knee', 10, 'middle') + t(312, gy2 + 22, 'ankle', 10, 'middle'))
    b.append(rule(270))
    b.append(t(6, 290, 'In a wheelchair', 12, weight='bold'))
    wx, wy = 124, 440
    b.append(circle(wx, wy - 26, 26, INK, 'none', 2.2) + path(f'M{wx - 40},{wy - 58} L{wx + 18},{wy - 58} M{wx - 40},{wy - 58} L{wx - 46},{wy - 116}', INK, sw=2.4, op=0.6))
    b.append(figure_g([('c', (wx - 30, wy - 132), 12), ('l', [(wx - 34, wy - 116), (wx - 36, wy - 64)], 22),
                       ('l', [(wx - 36, wy - 64), (wx + 14, wy - 64), (wx + 18, wy - 14)], 14)], INK, 0.3))
    b.append(dot(wx - 46, wy - 102) + dot(wx - 40, wy - 64))
    b.append(t(wx - 54, wy - 104, 'shoulder', 10, 'end') + t(wx - 54, wy - 92, 'blades', 10, 'end') + t(wx - 50, wy - 60, 'tailbone', 10, 'end'))
    b.append(tl(184, 320, [('Shift weight every', True), ('15 to 20 minutes:', True), 'lean forward, left, right,', 'or have someone help.', '', 'Foam or gel seat cushion.', ('No donut cushions.', True), ('No pillow under the knees.', True)], 11.5, 14.5))
    b.append(t(6, 466, 'Check the skin every day. Never drag: lift or use a draw sheet.', 11))
    return svg('fig-pressure-points', 490, '\n'.join(b), 'Where pressure sores form')


# ---------------------------------------------------------------- birth

@fig('fig-cord-tie-and-cut',
     'The cord can wait: WHO recommends clamping late, about 1 to 3 minutes after birth. When it has stopped pulsing, tie it tightly with clean (boiled) string in two places a few finger-widths apart and cut between the ties with a boiled blade. Never pull on the cord.',
     'A length of umbilical cord running from the baby\'s side on the left to the mother\'s side on the right. Two tight string ties sit a few finger-widths apart, and a blade cuts between them. Labels: wait 1 to 3 minutes, until it stops pulsing; boiled string; boiled blade; never pull on the cord.',
     ['02-12'])
def cord_tie():
    b = [t(6, 18, 'First wait: 1 to 3 minutes, until it stops', 12, weight='bold'), t(6, 34, 'pulsing. There is no hurry to cut.', 12, weight='bold')]
    cy = 104
    b.append(path(f'M20,{cy} C80,{cy - 16} 140,{cy + 14} 200,{cy} S300,{cy - 10} 340,{cy + 4}', INK, sw=14, op=0.2))
    b.append(path(f'M20,{cy} C80,{cy - 16} 140,{cy + 14} 200,{cy} S300,{cy - 10} 340,{cy + 4}', INK, sw=1.4, op=0.6))
    b.append(t(20, cy + 32, '← baby', 11, weight='bold') + t(340, cy + 32, 'mother →', 11, 'end', 'bold'))
    for x in (148, 212):
        b.append(rect(x - 4, cy - 12, 8, 24, AMBER, AMBER, 1.6, 2, 0.7))
    b.append(t(148, cy - 22, 'tie', 10.5, 'middle', 'bold', AMBER) + t(212, cy - 22, 'tie', 10.5, 'middle', 'bold', AMBER))
    b.append(arrow(158, cy + 24, 202, cy + 24, INK, 1.2, 5) + arrow(202, cy + 24, 158, cy + 24, INK, 1.2, 5))
    b.append(t(180, cy + 40, 'a few finger-widths', 10.5, 'middle'))
    b.append(line(180, cy - 40, 180, cy + 12, RED, 2, '4 3') + t(180, cy - 46, 'cut here', 10.5, 'middle', 'bold', RED))
    y = 176
    b.append(tl(8, y, ['String: clean, BOILED, tied tightly.', 'Blade: BOILED.', ('Never pull on the cord.', True), 'The afterbirth comes by itself; keep it in a bowl.'], 12, 16))
    return svg('fig-cord-tie-and-cut', y + 82, '\n'.join(b), 'Tying and cutting the cord')


@fig('fig-newborn-skin-to-skin',
     'Dry the baby at once with a clean cloth and lay it skin to skin on the mother\'s bare chest, both covered, the baby\'s head covered. A wet baby loses heat fast.',
     'A mother half sitting up against pillows with a newborn lying on its front on her bare chest. A blanket covers both of them up to the baby\'s shoulders, and the baby wears a cap. Labels: dried at once, skin to skin, both covered, head covered.',
     ['02-12'])
def skin_to_skin():
    b = []
    gy = 196
    b.append(floor(gy))
    b.append(path(f'M14,{gy} L14,92 Q14,80 30,82 L74,96 L74,{gy}', INK, INK, 1.6, 0.08))
    b.append(figure_g([('c', (62, 74), 17), ('l', [(66, 96), (110, 150), (150, 166)], 40), ('l', [(150, 168), (300, 172), (330, 176)], 22)], INK, 0.3))
    # baby on chest
    b.append(figure_g([('c', (112, 104), 11), ('l', [(122, 114), (150, 138)], 18)], AMBER, 0.6))
    b.append(path('M101,100 a11,11 0 0 1 20,-4', BLUE, sw=6, op=0.7))
    # blanket
    b.append(path(f'M106,126 Q150,118 210,148 L330,156 L336,{gy - 2} L90,{gy - 2} Q86,150 106,126 Z', BLUE, BLUE, 1.8, 0.18))
    b.append(t(120, 66, 'cap: head covered', 10.5, fill=BLUE) + line(118, 70, 116, 92, BLUE, 1))
    b.append(t(170, 106, 'baby dried at once,', 10.5) + t(170, 118, 'on its front, skin to skin', 10.5))
    b.append(t(250, 182, 'blanket over BOTH', 10.5, 'middle', 'bold', BLUE))
    b.append(tl(8, gy + 24, [('A wet baby loses heat fast.', True), 'Warm room; put the baby to the breast; it helps the', 'womb tighten (→ 02-12).'], 11.5, 14.5))
    return svg('fig-newborn-skin-to-skin', gy + 74, '\n'.join(b), 'Newborn skin to skin')


# ---------------------------------------------------------------- oxygen

@fig('fig-oxygen-no-flame-zone',
     'Medical oxygen: at least 5 feet between the oxygen and any heat source, open flame or electrical device; never a candle, match, lighter, oil lamp or wood stove near it; no smoking by anyone, with No Smoking and No Open Flames signs. Best: a room with no flame at all.',
     'Room plan. In the middle, a chair with an oxygen concentrator beside it and a dashed circle around them marked at least 5 feet. Inside the circle, nothing. Outside the circle, crossed out for inside it: a candle, an oil lamp, a space heater, a gas stove and a wood stove, which is in a different room. A No Smoking and No Open Flames sign is on the door. Notes: no aerosol sprays, vapour rub, petroleum jelly or oil-based lotions; turn the oxygen off when not in use.',
     ['02-08'])
def oxygen():
    b = [rect(6, 8, 230, 250, INK, 'none', 2.4)]
    cx, cy = 116, 130
    b.append(circle(cx, cy, 86, GREEN, GREEN, 2, 0.06, '6 4'))
    b.append(rect(cx - 16, cy - 10, 32, 30, INK, INK, 1.6, 4, 0.15) + t(cx, cy + 34, 'chair', 10, 'middle'))
    b.append(rect(cx + 22, cy - 6, 18, 24, BLUE, BLUE, 1.6, 3, 0.35) + t(cx + 46, cy + 4, 'O₂', 11, 'start', 'bold', BLUE))
    b.append(arrow(cx, cy, cx - 84, cy, GREEN, 1.4, 6) + t(cx - 44, cy - 6, 'at least 5 ft', 10.5, 'middle', 'bold', GREEN))
    b.append(t(cx, cy - 60, 'no flame, no heater,', 10.5, 'middle', fill=GREEN) + t(cx, cy - 47, 'no electrical device', 10.5, 'middle', fill=GREEN))
    # door with sign
    b.append(line(236, 200, 236, 244, 'white', 5) + path('M236,200 A44,44 0 0 1 280,244', INK, sw=1, dash='3 3'))
    b.append(rect(170, 208, 60, 38, RED, RED, 1.4, 3, 0.12) + tl(200, 223, ['NO SMOKING', 'NO FLAMES'], 8, 11, 'middle', 'bold', RED))
    # outside items list
    items = ['candle', 'oil lamp', 'match, lighter', 'space heater', 'gas stove', 'wood stove']
    b.append(t(248, 26, 'Keep OUT:', 12, weight='bold', fill=RED))
    for i, s in enumerate(items):
        y = 44 + i * 18
        b.append(xmark(248, y - 9, 9, RED, 2) + t(262, y, s, 11))
    b.append(tl(248, 170, ['Best: a room', 'with NO flame', 'at all.'], 11, 13.5, weight='bold'))
    y = 284
    b.append(tl(8, y, [('No smoking near them, by anyone.', True), 'No aerosol sprays, vapour rubs, petroleum jelly or',
                       'oil-based lotions: use water-based products.', 'Turn the oxygen off when not in use; tanks secured.'], 11.5, 15))
    return svg('fig-oxygen-no-flame-zone', y + 72, '\n'.join(b), 'Oxygen: the no-flame zone')


# ---------------------------------------------------------------- cooling pouch

@fig('fig-evaporative-pouch',
     'Evaporative cooling pouch: soak for exactly the time your instructions give, drain and towel until only semi-dry, put the medicine in, and keep it open to the air. Water evaporating through the fabric carries heat away; anything that stops evaporation (a zip bag, an airtight box) stops the cooling. It is not a refrigerator.',
     'Four small panels: a pouch soaking in a bowl of cold water beside a timer; the pouch being patted with a towel; an insulin pen going into the pouch; the pouch clipped open to the air on a belt with wavy lines leaving it. Below, crossed out in red: the pouch sealed in a zip bag, and the pouch in an airtight box.',
     ['12-21'])
def evaporative_pouch():
    b = []

    def pouch(x, y, w=56, h=34, op=0.25):
        return rect(x, y, w, h, BLUE, BLUE, 1.6, 6, op) + path(f'M{x + 6},{y + 8} h{w - 12} M{x + 6},{y + 17} h{w - 12} M{x + 6},{y + 26} h{w - 12}', BLUE, sw=1, op=0.6)
    panels = ['1. SOAK, timed', '2. Drain, towel', '3. Medicine in', '4. OPEN to air']
    for i, s in enumerate(panels):
        x = 4 + i * 89
        b.append(rect(x, 6, 85, 150, INK, 'none', 1.2, 6, op=0.6) + t(x + 42, 24, s, 11, 'middle', 'bold'))
    # 1 bowl
    b.append(path('M12,80 h70 q-4,40 -35,40 q-31,0 -35,-40 Z', INK, BLUE, 1.6, 0.15) + pouch(20, 72, 54, 26))
    b.append(circle(66, 50, 9, INK, 'none', 1.4) + line(66, 50, 66, 44, INK, 1.4) + line(66, 50, 70, 52, INK, 1.4))
    b.append(tl(46, 140, ['your leaflet\'s', 'exact time'], 9.5, 11.5, 'middle'))
    # 2 towel
    b.append(pouch(110, 70) + path('M104,100 q30,-24 66,0 l0,12 q-34,-20 -66,0 Z', AMBER, AMBER, 1.4, 0.35))
    b.append(tl(136, 140, ['semi-dry,', 'not dripping'], 9.5, 11.5, 'middle'))
    # 3 pen in
    b.append(pouch(198, 82) + rect(214, 46, 12, 50, INK, INK, 1.4, 4, 0.25) + arrow(240, 50, 240, 76, INK, 1.4, 5))
    b.append(tl(226, 140, ['in its own', 'packaging'], 9.5, 11.5, 'middle'))
    # 4 on belt, waves
    b.append(rect(270, 104, 82, 10, INK, INK, 1.2, 2, 0.3) + pouch(282, 74))
    for dx in (0, 16, 32):
        b.append(path(f'M{290 + dx},68 q-4,-6 0,-12 q4,-6 0,-12', BLUE, sw=1.4))
    b.append(tl(312, 132, ['belt, pocket,', 'open bag'], 9.5, 11.5, 'middle'))
    # failures
    b.append(t(6, 182, 'Stops the cooling completely:', 12.5, weight='bold', fill=RED))
    b.append(rect(14, 196, 120, 64, INK, INK, 1.6, 6, 0.06) + line(14, 206, 134, 206, INK, 2) + pouch(40, 216))
    b.append(cross(14, 196, 120, 64, RED, 3) + t(74, 278, 'sealed in a zip bag', 10.5, 'middle', 'bold', RED))
    b.append(rect(176, 196, 120, 64, INK, INK, 2.4, 2, 0.12) + pouch(208, 214))
    b.append(cross(176, 196, 120, 64, RED, 3) + t(236, 278, 'airtight or waterproof box', 10.5, 'middle', 'bold', RED))
    b.append(tl(8, 304, [('Not a refrigerator. No protection against freezing.', True), 'Re-soak on your product\'s schedule; check it with a', 'thermometer. Your own leaflet sets the numbers.'], 11.5, 15))
    return svg('fig-evaporative-pouch', 360, '\n'.join(b), 'Using an evaporative cooling pouch')


# ---------------------------------------------------------------- insulin

@fig('fig-insulin-cooler-barrier',
     'Ice or cold packs with a barrier: a towel or a box between the ice and the insulin so it cannot freeze, and a min/max thermometer beside the insulin. Aim for the label\'s 36 to 46 °F and never let it freeze: frozen insulin is discarded.',
     'Cut-away of an insulated cooler. Cold packs stand against both sides and lie on the bottom. A folded towel lines the space between the packs and a small box in the middle, which holds the insulin. A min/max thermometer probe sits beside the insulin box, its display outside the lid. A red label: insulin never touches ice. Notes: aim for 36 to 46 °F; never let it freeze; frozen insulin is discarded.',
     ['02-01', '02-06'])
def insulin_cooler():
    b = [t(6, 18, 'Insulated cooler, cut away', 11.5, italic=True)]
    x0, y0, w, h = 40, 40, 230, 170
    b.append(rect(x0, y0, w, h, INK, INK, 2.4, 10, 0.08) + rect(x0 + 10, y0 + 10, w - 20, h - 20, INK, 'white', 1.4, 6))
    b.append(rect(x0 - 4, y0 - 14, w + 8, 16, INK, INK, 2, 5, 0.18) + t(x0 + w / 2, y0 - 3, 'lid', 9.5, 'middle'))
    for xx in (x0 + 14, x0 + w - 40):
        b.append(rect(xx, y0 + 16, 26, h - 34, BLUE, BLUE, 1.6, 4, 0.35))
    b.append(rect(x0 + 44, y0 + h - 40, w - 88, 24, BLUE, BLUE, 1.6, 4, 0.35))
    b.append(t(x0 + 27, y0 + 90, 'ice', 10, 'middle', 'bold', BLUE) + t(x0 + w - 27, y0 + 90, 'ice', 10, 'middle', 'bold', BLUE))
    # towel barrier U
    b.append(path(f'M{x0 + 46},{y0 + 24} L{x0 + 46},{y0 + h - 46} L{x0 + w - 46},{y0 + h - 46} L{x0 + w - 46},{y0 + 24}', AMBER, sw=8, op=0.6))
    b.append(t(x0 + w / 2, y0 + h - 48 + 0, '', 1))
    # insulin box
    b.append(rect(x0 + 74, y0 + 56, 60, 50, INK, INK, 1.6, 4, 0.15) + t(x0 + 104, y0 + 86, 'insulin', 10.5, 'middle', 'bold'))
    # thermometer probe
    b.append(path(f'M{x0 + 160},{y0 + 80} L{x0 + 160},{y0 - 20} L{x0 + 210},{y0 - 20}', INK, sw=1.4))
    b.append(circle(x0 + 160, y0 + 82, 4, RED, RED, 1.2, 0.8))
    b.append(rect(x0 + 210, y0 - 34, 46, 26, INK, INK, 1.4, 3, 0.1) + t(x0 + 233, y0 - 17, 'min/max', 9, 'middle', 'bold'))
    b.append(t(x0 + 166, y0 + 70, 'probe', 9.5))
    # labels on right
    b.append(tl(284, 112, [('towel or', True), ('box =', True), ('barrier', True)], 11, 13.5, fill=AMBER))
    b.append(box(6, 226, 348, 30))
    b.append(t(180, 246, 'Insulin NEVER touches ice.', 13, 'middle', 'bold', RED))
    b.append(tl(8, 278, ['Aim for the label\'s 36 to 46 °F. Read the min/max often.', ('Never let it freeze. Frozen insulin: discard.', True),
                         'Winter: never against ice or a frozen wall (→ 29-07).'], 11.5, 15))
    return svg('fig-insulin-cooler-barrier', 336, '\n'.join(b), 'Insulin in a cooler with a barrier')


@fig('fig-device-fallback-ladder',
     'The pump and sensor fallback ladder (02-02): six rungs from full automation down to fast-acting insulin only. Each step down trades convenience for reliability. Never jump further down than the failure forces; never stay above a step that has stopped working. Rungs 4 and 5 need no electricity.',
     'A ladder of six rungs, top to bottom: 1 full automation, needs pump, sensor, controller, power; 2 backup controller or reader, needs the spare already set up; 3 pump without automation, needs settings copy and sugar readings; 4 injections with a sensor, needs long- and fast-acting insulin and the prescriber\'s plan; 5 injections with a fingerstick meter, needs meter, strips, lancets, night alarm; 6 fast-acting insulin only, a bridge on a prescriber\'s plan. Rungs 4 and 5 are bracketed: no electricity needed.',
     ['02-02'])
def device_ladder():
    rungs = [('1', 'Full automation', 'pump + sensor + controller, power'),
             ('2', 'Backup controller or reader', 'the spare, charged, already set up'),
             ('3', 'Pump without automation', 'settings copy; sugar readings'),
             ('4', 'Injections with a sensor', 'long- AND fast-acting; written plan'),
             ('5', 'Injections, fingerstick meter', 'meter, many strips, night alarm'),
             ('6', 'Fast-acting insulin only', 'frequent doses, prescriber\'s plan only')]
    b = [t(6, 18, 'more convenience', 11, italic=True)]
    x1, x2 = 14, 30
    y0, step = 30, 50
    b.append(line(x1, y0, x1, y0 + step * 6, INK, 3) + line(x2, y0, x2, y0 + step * 6, INK, 3))
    for i, (n, name, need) in enumerate(rungs):
        y = y0 + 20 + i * step
        b.append(line(x1, y, x2, y, INK, 3))
        col = GREEN if n in '45' else INK
        b.append(rect(40, y - 18, 262, 40, col, col, 1.4, 5, 0.08))
        b.append(t(50, y - 1, n + '. ' + name, 12.5, weight='bold') + t(50, y + 15, 'needs: ' + need, 10.5))
    b.append(t(6, y0 + step * 6 + 18, 'more reliability', 11, italic=True))
    b.append(path(f'M306,{y0 + 2 + 3 * step} h8 v{2 * step - 4} h-8', GREEN, sw=2))
    b.append(tl(318, y0 + 4 * step - 6, [('no', True), ('power', True)], 10.5, 12.5, fill=GREEN))
    y = y0 + step * 6 + 44
    b.append(tl(8, y, [('Never jump further down than the failure forces.', True), ('Never stay above a rung that has stopped working.', True)], 11.5, 15))
    return svg('fig-device-fallback-ladder', y + 44, '\n'.join(b), 'Pump and sensor fallback ladder')

"""F2: fire, firewood, chimney and wood-cutting diagrams (new ids only)."""
from figlib import *
from fig_medical import figure_g
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


@fig('fig-fuel-ladder',
     'The fuel ladder (06-01): four sizes, all ready before you strike anything: tinder that catches a spark; kindling from pencil-lead to pencil thickness; small fuel from finger to wrist thickness; fuel wood, the real logs. Have three times more kindling than you think you need.',
     'Four piles laid out from left to right with thickness labels: tinder (a cotton ball, bark shavings, lint); kindling, thin twigs from pencil-lead to pencil thick; small fuel, sticks from finger to wrist thick; fuel wood, split logs. Under the kindling pile, a note: three times more than you think.',
     ['06-01'])
def fuel_ladder():
    b = [t(6, 18, 'All four ready BEFORE you strike anything', 12.5, weight='bold')]
    gy = 150
    b.append(line(0, gy, 360, gy, INK, 1.6, op=0.6))
    # tinder
    b.append(circle(30, gy - 14, 12, INK, 'white', 1.4) + path(f'M14,{gy - 4} q8,-14 18,-2 q8,-12 16,0', AMBER, sw=1.4) + path(f'M40,{gy - 34} q6,-6 12,0 q6,6 12,0', AMBER, sw=1.2))
    # kindling
    for k in range(9):
        b.append(line(86 + k * 1.5, gy - 4 - k * 3, 150 + k * 1.5, gy - 10 - k * 3, AMBER, 1 + (k % 3) * 0.7))
    # small fuel
    for k in range(5):
        b.append(line(178, gy - 6 - k * 9, 252, gy - 12 - k * 9, AMBER, 5 + k % 2 * 3, op=0.85))
    # fuel wood
    for k, (x, y) in enumerate(((290, gy - 16), (326, gy - 16), (308, gy - 46))):
        b.append(circle(x, y, 16, INK, AMBER, 1.8, 0.4) + circle(x, y, 6, INK, 'none', 0.8))
    labs = [(42, '1. Tinder', 'catches a spark'), (120, '2. Kindling', 'pencil-lead to pencil'),
            (214, '3. Small fuel', 'finger to wrist'), (308, '4. Fuel wood', 'the real logs')]
    for x, a, c in labs:
        b.append(t(x, gy + 20, a, 11.5, 'middle', 'bold') + t(x, gy + 34, c, 9, 'middle'))
    b.append(t(120, gy + 52, '× 3 what you think', 10.5, 'middle', 'bold', RED))
    y = gy + 82
    b.append(tl(8, y, ['Tinder: petroleum-jelly cotton ball, birch bark, dryer lint,', 'fatwood shavings, char cloth, a commercial starter.',
                       ('Running back for more kindling while a weak flame dies', True), ('is the most common failure.', True)], 11, 14.5))
    return svg('fig-fuel-ladder', y + 66, '\n'.join(b), 'The fuel ladder')


@fig('fig-banked-fire',
     'Banking a fire (06-02): let it burn down to a good bed of coals, rake the coals into a compact pile, put one or two large, dense logs on top, and cover the edges with ash. In the morning, rake the ash off, add fine kindling and blow gently.',
     'Side section of a fire bed: a compact mound of glowing coals in the middle, two large dense logs lying on top of it, and a layer of grey ash drawn over the edges of the mound, labelled ash insulates and slows it to a smoulder.',
     ['06-02'])
def banked_fire():
    b = [t(6, 18, 'Side section', 11.5, italic=True)]
    gy = 170
    b.append(line(0, gy, 360, gy, INK, 2) + shade(0, gy, 360, 10, INK, 0.12))
    b.append(path(f'M90,{gy} Q180,{gy - 90} 270,{gy} Z', RED, RED, 1.6, 0.35))
    for (x, y) in ((150, gy - 20), (180, gy - 34), (210, gy - 22), (166, gy - 10), (196, gy - 12)):
        b.append(circle(x, y, 6, AMBER, AMBER, 0, 0.8))
    b.append(t(180, gy - 4, 'compact coal mound', 10, 'middle', 'bold'))
    b.append(path(f'M60,{gy} Q100,{gy - 30} 130,{gy - 44} L140,{gy - 34} Q110,{gy - 18} 96,{gy} Z', INK, INK, 1.4, 0.35))
    b.append(path(f'M300,{gy} Q260,{gy - 30} 230,{gy - 44} L220,{gy - 34} Q250,{gy - 18} 264,{gy} Z', INK, INK, 1.4, 0.35))
    for (x, y) in ((156, gy - 64), (206, gy - 60)):
        b.append(f'<ellipse cx="{x}" cy="{y}" rx="40" ry="15" fill="{AMBER}" fill-opacity="0.5" stroke="{INK}" stroke-width="1.8"/>')
    b.append(t(180, gy - 92, '1 or 2 large, dense logs on top', 11, 'middle', 'bold'))
    b.append(tl(4, gy - 70, [('ash over', True), ('the edges', True)], 10.5, 12.5) + arrow(46, gy - 52, 86, gy - 26, INK, 1.2, 5))
    y = gy + 34
    steps = ['1. Burn down to a good bed of coals.', '2. Rake the coals into a compact pile.', '3. One or two large, dense logs on top.',
             '4. Cover the edges with ash.', '5. Morning: rake off the ash, fine kindling, blow gently.']
    b.append(tl(8, y, steps, 11.5, 15))
    b.append(t(8, y + 82, 'Indoors: bank with dry wood; smouldering makes creosote.', 11, weight='bold'))
    return svg('fig-banked-fire', y + 102, '\n'.join(b), 'Banking a fire overnight')


def stack(x, y, w, h, d, label=None):
    """Isometric-ish woodpile: front face w x h, depth offset d."""
    dx, dy = d * 0.6, -d * 0.4
    b = path(f'M{x},{y} L{x + w},{y} L{x + w},{y - h} L{x},{y - h} Z', INK, AMBER, 1.8, 0.3)
    b += path(f'M{x},{y - h} L{x + dx},{y - h + dy} L{x + w + dx},{y - h + dy} L{x + w},{y - h} Z', INK, AMBER, 1.4, 0.18)
    b += path(f'M{x + w},{y} L{x + w + dx},{y + dy} L{x + w + dx},{y - h + dy} L{x + w},{y - h} Z', INK, AMBER, 1.4, 0.12)
    for i in range(int(w // 14)):
        for j in range(int(h // 14)):
            b += circle(x + 7 + i * 14, y - 7 - j * 14, 5.5, INK, 'none', 0.7)
    return b


@fig('fig-cord-measure',
     'A full cord is 128 cubic feet: a stack 4 ft high, 4 ft deep and 8 ft long. A face cord (rick) is one row 4 ft high and 8 ft long but only 16 to 24 inches deep: a third to a half of a cord, and often sold as a "cord" (MU Extension).',
     'Two woodpiles drawn the same height and length. The top one is a full cord, 4 feet high, 8 feet long and 4 feet deep, labelled 128 cubic feet. The bottom one is a face cord, the same 4 by 8 feet face but only 16 to 24 inches deep, labelled a third to a half of a cord.',
     ['06-03'])
def cord_measure():
    b = [t(6, 18, 'FULL CORD = 128 cu ft', 13, weight='bold')]
    b.append(stack(30, 176, 196, 98, 100))
    b.append(t(128, 192, '8 ft long', 11, 'middle', 'bold') + t(22, 130, '4 ft', 11, 'end', 'bold'))
    b.append(t(270, 102, '4 ft deep', 11, 'start', 'bold'))
    b.append(rule(210))
    b.append(t(6, 232, 'FACE CORD (rick): same face, one row', 13, weight='bold'))
    b.append(stack(30, 356, 196, 98, 30))
    b.append(t(128, 372, '8 ft long', 11, 'middle', 'bold') + t(22, 310, '4 ft', 11, 'end', 'bold'))
    b.append(tl(250, 256, [('16 to 24 in', True), 'deep'], 11, 13.5))
    b.append(tl(250, 316, [('= a third to', True), ('a half of a cord', True)], 11, 13.5, fill=RED))
    y = 402
    b.append(tl(8, y, ['Often sold as a "cord". Measure your stack honestly.', 'Stack off the ground, covered on top, open on the sides.'], 11.5, 15))
    return svg('fig-cord-measure', y + 40, '\n'.join(b), 'A cord and a face cord')


def splitter(x, gy, block_h, tip, color=INK):
    """Person splitting: feet apart at x, axe/maul head ending at tip."""
    hip = (x, gy - 70)
    sh = (x + 6, gy - 120)
    parts = [('c', (x + 10, gy - 136), 11), ('l', [sh, hip], 18), ('l', [hip, (x - 18, gy - 2)], 11), ('l', [hip, (x + 22, gy - 2)], 11),
             ('l', [sh, (x + 34, gy - 92)], 8)]
    return figure_g(parts, color, 0.32)


@fig('fig-splitting-stance',
     'Splitting safely (06-03): chopping block at about knee height, never on the ground; feet apart and out of the swing line, so a glancing blade hits the block or the dirt, not your shin; nobody near you while you split, especially children.',
     'Side view of a person splitting a round on a knee-high chopping block. The feet are apart and back from the block; the maul\'s arc is drawn ending in the round and, if it glances, in the block and the ground, never the shin. A dashed circle around the scene is labelled keep everyone well clear.',
     ['06-03'])
def splitting_stance():
    b = []
    gy = 230
    b.append(line(0, gy, 360, gy, INK, 2))
    bx = 200
    b.append(rect(bx, gy - 52, 54, 52, INK, AMBER, 1.8, 3, 0.35) + rect(bx + 6, gy - 86, 42, 34, INK, AMBER, 1.6, 3, 0.2))
    b.append(t(bx + 27, gy - 28, 'block', 10, 'middle') + t(bx + 27, gy - 66, 'round', 10, 'middle'))
    b.append(tl(bx + 62, gy - 50, [('about knee', True), ('height', True)], 10.5, 12.5))
    b.append(splitter(140, gy, 52, None))
    b.append(line(174, gy - 92, 222, gy - 88, AMBER, 4) + rect(214, gy - 98, 16, 18, INK, INK, 1.4, 2, 0.6))
    b.append(path(f'M150,{gy - 200} A100,100 0 0 1 226,{gy - 96}', INK, sw=1.4, dash='4 3') + arrow(222, gy - 104, 226, gy - 92, INK, 1.4, 6))
    b.append(path(f'M226,{gy - 80} L240,{gy - 10}', RED, sw=1.6, dash='3 3') + t(244, gy - 4, 'glance: block or dirt', 9.5, fill=RED))
    b.append(t(120, gy + 16, 'feet apart, back from the block', 10, 'middle', 'bold'))
    b.append(tl(6, 30, [('Nobody near you', True), ('while you split,', True), ('especially children.', True)], 10.5, 12.5, fill=RED))
    y = gy + 48
    b.append(tl(8, y, ['Maul for splitting. Wedges and a sledge for knotty wood.', ('Stop when you are tired: most injuries come on a tired swing.', True)], 11, 14.5))
    return svg('fig-splitting-stance', y + 40, '\n'.join(b), 'Splitting stance and block height')


@fig('fig-chopping-block-height',
     'Chopping block height (16-06): for splitting, a low block, knee height or less, so the head arrives near the bottom of its swing with the handle about level and a miss hits the block or the ground. A waist-high splitting block sends a glancing blow forward and down into your legs. The higher block is only for hatchet and kindling work.',
     'Three side-view panels. Left, ticked: a person splitting on a block at knee height or less, the maul handle about level at impact, a miss going into the block or the ground. Middle, crossed out: the same swing on a waist-high block, with a red arrow showing a glancing blow travelling forward and down into the legs. Right: a higher block used only for a hatchet splitting kindling, hands clear.',
     ['16-06'])
def chopping_block():
    b = []
    gy = 220
    b.append(line(0, gy, 360, gy, INK, 2))
    panels = [(0, 'SPLITTING', 'knee height or less', GREEN, 44), (120, 'NOT for splitting', 'waist high', RED, 96), (240, 'KINDLING only', 'higher block, hatchet', AMBER, 96)]
    for x0, title, sub, col, bh in panels:
        b.append(t(x0 + 58, 18, title, 11.5, 'middle', 'bold', col) + t(x0 + 58, 32, sub, 10, 'middle'))
        b.append(rect(x0 + 64, gy - bh, 40, bh, INK, AMBER, 1.6, 3, 0.3))
        if x0:
            b.append(line(x0 - 2, 10, x0 - 2, gy + 50, INK, 0.8, op=0.4))
    # panel 1
    b.append(figure_g([('c', (34, gy - 132), 10), ('l', [(38, gy - 118), (36, gy - 66)], 16), ('l', [(36, gy - 66), (20, gy - 2)], 10), ('l', [(36, gy - 66), (52, gy - 2)], 10), ('l', [(40, gy - 110), (60, gy - 70)], 7)], INK, 0.32))
    b.append(line(58, gy - 66, 92, gy - 62, AMBER, 4) + rect(86, gy - 72, 12, 16, INK, INK, 1.2, 2, 0.6))
    b.append(t(60, gy - 80, 'handle level', 9, 'middle'))
    b.append(check(92, 46, 16))
    # panel 2
    b.append(figure_g([('c', (154, gy - 132), 10), ('l', [(158, gy - 118), (156, gy - 66)], 16), ('l', [(156, gy - 66), (140, gy - 2)], 10), ('l', [(156, gy - 66), (172, gy - 2)], 10), ('l', [(160, gy - 110), (184, gy - 104)], 7)], INK, 0.32))
    b.append(line(182, gy - 104, 206, gy - 112, AMBER, 4))
    b.append(arrow(204, gy - 92, 168, gy - 30, RED, 2.2, 7) + t(158, gy + 16, 'glance into legs', 9.5, 'middle', 'bold', RED))
    b.append(cross(130, 50, 100, 150, RED, 2.5))
    # panel 3
    b.append(rect(298, gy - 112, 10, 16, AMBER, AMBER, 1.2, 1, 0.6) + line(280, gy - 124, 300, gy - 112, INK, 3) + rect(274, gy - 130, 10, 8, INK, INK, 1, 1, 0.6))
    b.append(t(298, gy + 16, 'hands stay clear', 9.5, 'middle'))
    y = gy + 44
    b.append(tl(8, y, ['Feet apart, out of the swing. Nothing behind or overhead.', ('Never hold wood with your hand while striking it.', True)], 11, 14.5))
    return svg('fig-chopping-block-height', y + 38, '\n'.join(b), 'Chopping block height')


@fig('fig-creosote-stages',
     'Creosote, as sweeps grade it (CSIA, as on 06-09): stage 1, light, flaky, sooty dust that an ordinary brush takes off; stage 2, crusty, tar-like flakes a brush struggles with; stage 3, glaze, hard, shiny or tacky black, like poured tar that set, which brushing will not remove. All of it is highly combustible. Never reach stage 3.',
     'Three square swatches of flue wall. Stage 1: a light grey dusting of loose soot flakes, labelled brush takes it off. Stage 2: darker, crusty, curled tar-like flakes, labelled brush struggles. Stage 3: a smooth, shiny black glaze with highlights, labelled glaze, brushing will not remove it, stop using the flue.',
     ['06-09'])
def creosote():
    b = []
    import random
    random.seed(7)
    for i, (title, sub, col) in enumerate([('STAGE 1', ['flaky, sooty dust', 'brush takes it off'], INK),
                                           ('STAGE 2', ['crusty, tar-like', 'flakes; brush struggles'], AMBER),
                                           ('STAGE 3: GLAZE', ['hard, shiny, tacky;', 'brushing will NOT', 'remove it'], RED)]):
        x = 6 + i * 118
        b.append(t(x + 53, 20, title, 11.5, 'middle', 'bold', col))
        b.append(rect(x, 30, 106, 106, INK, '#b8a99a', 1.6, 2, 0.5))
        if i == 0:
            for k in range(40):
                b.append(circle(round(x + 8 + random.random() * 90, 1), round(38 + random.random() * 90, 1), round(1.5 + random.random() * 2, 1), '#555', '#555', 0, 0.45))
        elif i == 1:
            for k in range(14):
                cx, cy = x + 12 + random.random() * 80, 40 + random.random() * 84
                b.append(path(f'M{cx:.1f},{cy:.1f} q8,-6 16,0 q-2,8 -14,6 Z', '#222', '#333', 1, 0.8))
        else:
            b.append(rect(x + 3, 33, 100, 100, '#111', '#111', 0, 2, 0.92))
            b.append(path(f'M{x + 16},{60} q30,-14 60,4', 'white', sw=3, op=0.6) + path(f'M{x + 30},{100} q20,-8 40,2', 'white', sw=2, op=0.4))
        b.append(tl(x + 53, 154, sub, 10, 12, 'middle', fill=col if i == 2 else INK))
    y = 214
    b.append(box(4, y - 16, 352, 52))
    b.append(tl(12, y + 2, [('All three are highly combustible. Never reach stage 3.', True), 'Stage 3 with no professional: a flue you may have to give up.'], 11, 15, fill=RED))
    b.append(t(8, y + 60, 'Prevention: hot fires and dry wood.', 11.5, weight='bold'))
    return svg('fig-creosote-stages', y + 82, '\n'.join(b), 'Creosote stages 1 to 3')


@fig('fig-flue-inspection-mirror',
     'Inspecting the flue (06-09): cold flue, damper open; from the firebox or the cleanout door, angle a mirror to see up the flue and shine a strong flashlight on it. Scrape test: drag a screwdriver along the flue wall; about 1/8 inch of sooty buildup means sweep before the next fire. Shiny, tarry glaze: stop using the flue.',
     'Cut-away of a cold fireplace and flue. A hand holds a mirror tilted inside the firebox below the open damper, and a flashlight beam bounces off the mirror up the flue lining. An inset shows a screwdriver dragged along the flue wall, scraping a layer marked about 1/8 inch: sweep before the next fire.',
     ['06-09'])
def flue_mirror():
    b = []
    gy = 290
    b.append(line(0, gy, 220, gy, INK, 2))
    b.append(rect(40, 10, 140, gy - 10, INK, INK, 1.6, 0, 0.12))
    b.append(rect(80, 10, 60, 170, INK, 'white', 1.6))
    b.append(shade(80, 10, 6, 170, INK, 0.5) + shade(134, 10, 6, 170, INK, 0.5))
    b.append(t(114, 90, 'flue', 11, 'start', 'bold'))
    b.append(path('M60,180 L80,180 M140,180 L160,180 L160,' + str(gy) + ' M60,180 L60,' + str(gy), INK, sw=2))
    b.append(line(86, 186, 110, 176, INK, 3) + t(170, 176, 'damper OPEN', 10, 'start', 'bold'))
    b.append(t(110, gy - 8, 'firebox (cold)', 10, 'middle'))
    # mirror
    b.append(line(92, 250, 122, 228, BLUE, 4) + t(126, 252, 'mirror', 10, fill=BLUE))
    b.append(figure_g([('l', [(64, 278), (92, 252)], 9)], INK, 0.35))
    # flashlight
    b.append(rect(140, 254, 30, 12, INK, INK, 1.4, 3, 0.4) + t(176, 270, 'flashlight', 10))
    b.append(path('M140,260 L108,240 L108,30', AMBER, sw=1.6, dash='4 3') + arrow(108, 60, 108, 30, AMBER, 1.6, 6))
    # scrape inset
    ix = 232
    b.append(rect(ix, 20, 122, 150, INK, 'none', 1, 6, op=0.6) + t(ix + 61, 38, 'Scrape test', 11.5, 'middle', 'bold'))
    b.append(rect(ix + 14, 50, 24, 106, INK, '#b8a99a', 1.4, 0, 0.5) + rect(ix + 38, 50, 8, 106, '#333', '#333', 0, 0, 0.8))
    b.append(line(ix + 54, 70, ix + 94, 120, INK, 4) + rect(ix + 90, 116, 14, 28, AMBER, AMBER, 1.2, 3, 0.6))
    b.append(t(ix + 50, 160, '≈ 1/8 in', 10, 'start', 'bold', RED))
    y = gy + 28
    b.append(tl(8, y, [('About 1/8 in of sooty buildup: sweep before the next fire.', True), 'Shiny, tarry glaze: stop using the flue.',
                       'Also look for: cracked tiles, daylight, nests, blockages.'], 11, 14.5))
    return svg('fig-flue-inspection-mirror', y + 56, '\n'.join(b), 'Inspecting a flue with a mirror')


@fig('fig-chainsaw-kickback-zone',
     'Chainsaw kickback (16-06): when the upper tip of the bar touches wood or anything else, or the wood pinches the chain, the bar is thrown up and back toward you in a fraction of a second. Never let the nose of the bar touch anything; both hands on the saw, left on the front handle, right on the rear.',
     'Side view of a chainsaw. The upper quarter of the rounded bar tip is shaded red and labelled kickback zone. A curved red arrow shows the bar flying up and back toward the operator\'s position. The front and rear handles are labelled left hand and right hand.',
     ['16-06'])
def chainsaw():
    b = []
    cy = 150
    # body
    b.append(rect(20, cy - 40, 90, 60, INK, INK, 1.8, 10, 0.2) + t(65, cy - 6, 'saw', 11, 'middle', 'bold'))
    b.append(path(f'M10,{cy - 10} q-8,-30 20,-40 l10,10 q-18,6 -14,30', INK, sw=5, op=0.6) + t(4, cy + 36, 'rear handle:', 10) + t(4, cy + 48, 'RIGHT hand', 10, weight='bold'))
    b.append(path(f'M60,{cy - 40} q10,-34 50,-30', INK, sw=5, op=0.6) + t(116, cy - 52, 'front handle: LEFT hand', 10, weight='bold'))
    # bar
    bx1, bx2 = 110, 320
    b.append(path(f'M{bx1},{cy - 24} L{bx2},{cy - 18} A16,16 0 0 1 {bx2},{cy + 14} L{bx1},{cy + 10} Z', INK, INK, 1.8, 0.1))
    b.append(path(f'M{bx2},{cy - 18} A16,16 0 0 1 {bx2 + 16},{cy - 2} L{bx2},{cy - 2} Z', RED, RED, 1.6, 0.6))
    b.append(t(342, cy - 28, 'KICKBACK', 11, 'end', 'bold', RED) + t(bx2 + 6, cy - 22 - 0, '', 1))
    b.append(t(bx2 - 6, cy + 40, 'upper tip of the bar', 10, 'middle', 'bold', RED))
    b.append(path(f'M{bx2 - 20},{cy - 40} Q{bx2 - 120},{cy - 170} 60,{cy - 100}', RED, sw=2.2) + arrow(80, cy - 102, 60, cy - 100, RED, 2.2, 8))
    b.append(t(170, cy - 78, 'bar thrown UP and BACK', 11, 'middle', 'bold', RED))
    y = cy + 76
    b.append(tl(8, y, [('Never let the nose of the bar touch anything.', True), 'Never cut above shoulder height; never on a ladder.',
                       'Chain brake on whenever you walk with the saw.', 'Chaps, helmet with face shield and muffs, glasses, gloves.'], 11, 14.5))
    return svg('fig-chainsaw-kickback-zone', y + 70, '\n'.join(b), 'Chainsaw kickback zone')


@fig('fig-sawbuck',
     'A sawbuck (16-06): an X-shaped stand that holds wood at working height while sawing. Build one; it prevents many injuries.',
     'Side view of a sawbuck: two X-shaped leg frames joined by a rail, with a log lying in the upper V of the crosses at about hip height. A bow saw cuts the log between the two frames, and a person stands upright beside it.',
     ['16-06'])
def sawbuck():
    b = []
    gy = 220
    b.append(line(0, gy, 360, gy, INK, 2))
    for x in (130, 250):
        b.append(line(x - 40, gy, x + 30, gy - 130, AMBER, 7) + line(x + 40, gy, x - 30, gy - 130, AMBER, 7))
    b.append(line(110, gy - 60, 270, gy - 60, AMBER, 5))
    b.append(rect(60, gy - 110, 260, 30, INK, AMBER, 1.8, 14, 0.25) + t(300, gy - 118, 'log', 10.5, 'middle'))
    b.append(path(f'M178,{gy - 150} L232,{gy - 150} L222,{gy - 100} L188,{gy - 100} Z', INK, sw=2.4) + t(205, gy - 158, 'bow saw', 10, 'middle'))
    b.append(figure_g([('c', (40, gy - 168), 11), ('l', [(40, gy - 154), (40, gy - 80)], 18), ('l', [(40, gy - 80), (32, gy - 2)], 11), ('l', [(40, gy - 80), (50, gy - 2)], 11),
                       ('l', [(44, gy - 140), (80, gy - 120)], 8)], INK, 0.32))
    b.append(tl(232, 22, [('Working height:', True), 'you stand upright,', 'the wood cannot roll.'], 11, 13.5))
    b.append(t(190, gy + 18, 'X-shaped legs, joined by a rail', 10.5, 'middle'))
    y = gy + 44
    b.append(tl(8, y, [('Build one: it prevents many injuries.', True), 'A bow saw cuts logs to length (bucking).'], 11, 14.5))
    return svg('fig-sawbuck', y + 40, '\n'.join(b), 'A sawbuck')

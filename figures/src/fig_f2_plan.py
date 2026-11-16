"""F2: planning and cycle diagrams (new ids only)."""
import math
from figlib import *
FIGS = {}


def fig(fid, caption, alt, pages):
    def deco(fn):
        FIGS[fid] = dict(fn=fn, caption=caption, alt=alt, pages=pages)
        return fn
    return deco


def rule(y, x1=4, x2=356):
    return line(x1, y, x2, y, INK, 0.8, op=0.4)


def ring(cx, cy, r, items, colors=None, box_w=118, box_h=44):
    """Boxes evenly around a circle, with arrows between them clockwise."""
    b = []
    n = len(items)
    pos = []
    for k in range(n):
        a = -math.pi / 2 + k * 2 * math.pi / n
        pos.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    for k in range(n):
        a1 = -math.pi / 2 + (k + 0.28) * 2 * math.pi / n
        a2 = -math.pi / 2 + (k + 0.72) * 2 * math.pi / n
        p1 = (round(cx + r * math.cos(a1), 1), round(cy + r * math.sin(a1), 1))
        p2 = (round(cx + r * math.cos(a2), 1), round(cy + r * math.sin(a2), 1))
        b.append(path(f'M{p1[0]},{p1[1]} A{r},{r} 0 0 1 {p2[0]},{p2[1]}', INK, sw=1.8))
        a3 = a2 - 0.05
        b.append(arrow(round(cx + r * math.cos(a3), 1), round(cy + r * math.sin(a3), 1), p2[0], p2[1], INK, 1.8, 7))
    for k, (x, y) in enumerate(pos):
        col = (colors or [INK] * n)[k]
        lines = items[k]
        b.append(rect(round(x - box_w / 2, 1), round(y - box_h / 2, 1), box_w, box_h, col, col, 1.6, 6, 0.1))
        b.append(tl(round(x, 1), round(y - box_h / 2 + 17, 1), lines, 11, 13, 'middle'))
    return '\n'.join(b)


@fig('fig-power-bank-rotation',
     'Power-bank rotation (00-10): number your power banks. At any moment one is in use, one is charging (from a power station, a solar panel, or a vehicle that is running anyway) and one is full and set aside as the reserve. Empty goes to charging; charged becomes the reserve; the reserve goes into use. Tape the number and the fill date on each.',
     'Three numbered power banks in a clockwise cycle: in use, in a pocket charging a phone; charging, from a power station, solar panel or running vehicle; full reserve, set aside, with a tape strip showing number and date. Arrows run from in use to charging to reserve and back to in use.',
     ['00-10'])
def power_bank():
    b = [ring(180, 150, 96, [[('IN USE', True), 'pocket, phone'], [('CHARGING', True), 'station, solar,', 'running vehicle'], [('FULL RESERVE', True), 'set aside']],
              [BLUE, AMBER, GREEN], 124, 54)]
    b.append(tl(180, 140, [('empty → charging', False), ('full → reserve', False), ('reserve → use', False)], 10.5, 14, 'middle', italic=True))
    y = 288
    b.append(tl(8, y, [('Number each bank. Tape: number + date filled.', True), 'Only one bank? Keep it full; use it only for the binder', 'device and medical devices.'], 11.5, 15))
    return svg('fig-power-bank-rotation', y + 56, '\n'.join(b), 'Power-bank rotation')


@fig('fig-wood-year-lag',
     'The wood calendar (24-03): fell and cut to length in late winter to early spring; split in spring; stack off the ground, covered on top and open on the sides, through summer; move a winter\'s worth close to the house in autumn; in winter, burn last year\'s wood. Wood cut this year is next year\'s fuel.',
     'A year drawn as a wheel of five steps: late winter to early spring, fell and cut; spring, split; summer, stack and dry; autumn, move near the house; winter, burn last year\'s wood. A separate arrow leaves the cut step and jumps a full turn ahead to next winter, labelled this year\'s wood burns next winter.',
     ['24-03'])
def wood_lag():
    items = [[('Late winter-spring', True), 'fell, cut to length'], [('Spring', True), 'split'], [('Summer', True), 'stack off ground;', 'cover the top only'],
             [('Autumn', True), 'move near house'], [('Winter', True), 'burn LAST', 'year\'s wood']]
    b = [ring(180, 176, 124, items, [BLUE, GREEN, AMBER, AMBER, RED], 116, 52)]
    b.append(tl(180, 196, [('This year\'s wood', True), ('burns NEXT winter', True)], 12, 15, 'middle', fill=RED))
    y = 356
    b.append(tl(8, y, ['"We will cut wood when we need it" fails: start the', 'cycle now (→ 23-04).'], 11.5, 15))
    return svg('fig-wood-year-lag', y + 40, '\n'.join(b), 'The one-year wood lag')


@fig('fig-three-classes-of-consumable',
     'Three classes of supply (23-01): A, renewable, you can make or gather more (water, wood, garden food): build the ability to produce it. B, substitutable, it runs out but something else does the job (batteries to daylight, gauze to boiled cloth): stock deeply and learn the substitute. C, irreplaceable, no way to make it and nothing replaces it (prescription medicines the body depends on): class C is short, and it decides everything.',
     'Three columns. A, renewable, in green, with examples water, wood, garden food, soap and the plan: build the ability to produce it. B, substitutable, in amber, with examples batteries to daylight, gauze to boiled cloth, tape to wire, and the plan: stock deeply and learn the substitute. C, irreplaceable, in red, with examples insulin, epinephrine, seizure and heart medicines, and the line: class C is short, and it decides everything.',
     ['23-01'])
def three_classes():
    cols = [('A', 'RENEWABLE', GREEN, ['water', 'wood', 'garden food', 'soap, cordage'], ['Build the ability', 'to produce it.']),
            ('B', 'SUBSTITUTABLE', AMBER, ['batteries → daylight', 'gauze → boiled cloth', 'tape → wire', 'screws → lashings'], ['Stock deeply AND', 'learn the substitute.']),
            ('C', 'IRREPLACEABLE', RED, ['insulin', 'epinephrine', 'seizure and heart', 'medicines'], ['Short list. It sets', 'the whole timeline.'])]
    b = []
    for i, (L, name, col, ex, plan) in enumerate(cols):
        x = 4 + i * 119
        b.append(rect(x, 6, 113, 250, col, col, 1.6, 6, 0.08))
        b.append(t(x + 56, 40, L, 28, 'middle', 'bold', col) + t(x + 56, 60, name, 10.5, 'middle', 'bold', col))
        b.append(tl(x + 8, 86, ex, 10, 14))
        b.append(line(x + 8, 162, x + 105, 162, col, 1))
        b.append(tl(x + 8, 182, plan, 10.5, 14, weight='bold'))
    y = 284
    b.append(tl(8, y, [('Class C is short, and it decides everything.', True), 'Well prepared in A and B, the timeline is still set by', 'one item in C.'], 11.5, 15))
    return svg('fig-three-classes-of-consumable', y + 56, '\n'.join(b), 'Three classes of supply')


@fig('fig-four-stages-of-a-resource',
     'The four stages every supply passes through (23-04): 1 stock, a pile that only shrinks; 2 extend, ration, recover, reuse, repair, so it shrinks more slowly; 3 substitute, something else does the job, usually worse; 4 produce, you make or gather it on and on. A supply is only really solved at stage 4; a supply with no stage 4 has a deadline.',
     'Four steps from left to right: a pile labelled 1 stock, only shrinks; a smaller pile shrinking slowly labelled 2 extend; a different object labelled 3 substitute, usually worse; a growing plant labelled 4 produce, on and on. A bracket under stages 2 and 3 reads buys time.',
     ['23-04'])
def four_stages():
    b = []
    names = [('1. STOCK', 'only shrinks'), ('2. EXTEND', 'shrinks slower'), ('3. SUBSTITUTE', 'usually worse'), ('4. PRODUCE', 'on and on')]
    for i, (a, c) in enumerate(names):
        x = 4 + i * 89
        cx = x + 42
        b.append(t(cx, 22, a, 10.5, 'middle', 'bold', GREEN if i == 3 else INK) + t(cx, 36, c, 9.5, 'middle'))
        if i < 3:
            b.append(arrow(x + 76, 100, x + 92, 100, INK, 1.4, 5))
    # piles
    b.append(path('M14,130 L46,70 L78,130 Z', AMBER, AMBER, 1.6, 0.5))
    b.append(path('M106,130 L132,92 L158,130 Z', AMBER, AMBER, 1.6, 0.5))
    b.append(rect(200, 96, 30, 34, BLUE, BLUE, 1.6, 4, 0.3) + path('M196,90 q19,-14 38,0', BLUE, sw=1.6))
    b.append(path('M314,130 L314,74', GREEN, sw=3) + path('M314,96 q-20,-6 -24,-22 q18,2 24,16 M314,86 q18,-8 22,-24 q-18,2 -22,18', GREEN, GREEN, 1.6, 0.3))
    b.append(line(4, 132, 356, 132, INK, 1.6))
    b.append(path('M98,146 v8 h168 v-8', INK, sw=1.4) + t(182, 170, 'stages 2 and 3 buy time', 10.5, 'middle', italic=True))
    y = 200
    b.append(tl(8, y, [('A supply is only really solved at stage 4.', True), 'No stage 4: it has a deadline, and the deadline sets', 'the plan. Class C items stop at stage 1 (→ 23-01).'], 11.5, 15))
    return svg('fig-four-stages-of-a-resource', y + 56, '\n'.join(b), 'Four stages of a resource')


@fig('fig-layer-system',
     'The layer system (11-01): base layer against the skin moves sweat away (wool or synthetic, never cotton); mid layer traps air, which is the warmth (fleece, wool, down, synthetic fill); outer shell blocks wind and water; extremities, head, hands, feet and face, are where frostbite happens. Several thin layers beat one thick one.',
     'A cut-away of layers over skin, from the inside out: base, a thin band with sweat arrows moving outward, never cotton; mid, a thick band of trapped air dots, the warmth; outer shell, a thin band with wind and rain arrows bouncing off. Beside it, small icons of a hat, gloves, boots and face cover labelled extremities.',
     ['11-01'])
def layer_system():
    b = []
    x0 = 40
    layers = [('skin', 16, INK, 0.25), ('BASE', 22, BLUE, 0.25), ('MID', 70, AMBER, 0.2), ('SHELL', 18, GREEN, 0.3)]
    x = x0
    for name, w, col, op in layers:
        b.append(rect(x, 40, w, 200, col, col, 1.4, 0, op))
        b.append(t(x + w / 2, 260 if name != 'skin' else 274, name, 10, 'middle', 'bold', col if name != 'skin' else INK))
        x += w
    import random
    random.seed(3)
    for k in range(40):
        b.append(circle(round(x0 + 40 + random.random() * 66, 1), round(48 + random.random() * 184, 1), 2.2, AMBER, 'none', 1))
    for y in (80, 140, 200):
        b.append(arrow(x0 + 4, y, x0 + 34, y, BLUE, 1.4, 5))
    for y in (70, 150, 220):
        b.append(arrow(x + 50, y, x + 6, y, INK, 1.6, 6) + path(f'M{x + 4},{y + 6} l14,14', INK, sw=1.2))
    b.append(t(x + 20, 34, 'wind, water', 10.5))
    b.append(tl(x + 66, 70, [('EXTREMITIES', True), 'head, hands,', 'feet, face:', 'where frostbite', 'happens'], 10.5, 13.5, fill=RED))
    notes = [('BASE: moves sweat off the skin. Cotton holds sweat, chills you.', True), 'MID: traps air. That IS the warmth. Squashed or wet: none.',
             'SHELL: blocks wind and water.', ('Several thin layers beat one thick one; shed heat', True), ('before you sweat.', True)]
    y = 290
    b.append(tl(8, y, notes, 11, 15))
    return svg('fig-layer-system', y + 88, '\n'.join(b), 'The cold-weather layer system')

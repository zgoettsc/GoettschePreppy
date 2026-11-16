"""F2: food storage, preserving and cooking diagrams (new ids only)."""
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


def egg(cx, cy, rx=34, ry=46, air=10, kind='good'):
    b = f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{AMBER}" fill-opacity="0.18" stroke="{INK}" stroke-width="1.8"/>'
    # air cell at the wide (top) end
    b += path(f'M{cx - rx * 0.62},{cy - ry + air * 1.6} Q{cx},{cy - ry + air * 2.6} {cx + rx * 0.62},{cy - ry + air * 1.6}', INK, sw=1.4)
    if kind == 'good':
        b += circle(cx, cy + 6, 14, AMBER, AMBER, 0, 0.35)
    else:
        b += path(f'M{cx - 12},{cy + 4} q8,-12 18,-4 q10,8 0,18 q-12,10 -20,0 Z', INK, INK, 1, 0.6)
        b += circle(cx + 14, cy + 22, 4, INK, INK, 0, 0.5) + circle(cx - 16, cy + 26, 3, INK, INK, 0, 0.5)
    return b


@fig('fig-candling-an-egg',
     'Candling an egg (04-15): in a dark room, hold the egg against a bright flashlight. A sound egg shows a small air pocket at the wide end and a faint yolk shadow. A large air pocket, a dark or moving mass, blotches, cracks, or a bad smell on opening: throw it out. Crack every egg into a separate bowl first.',
     'Left: a hand-held flashlight shining up into an egg in a dark room. Middle: a sound egg lit from behind, with a small air pocket at the wide end and a faint yolk shadow, marked keep. Right: a bad egg with a large air pocket and a dark mass and blotches, marked throw out.',
     ['04-15'])
def candling():
    b = [shade(0, 0, 360, 200, '#333', 1)]
    b.append(t(8, 18, 'Dark room', 11.5, 'start', 'bold', 'white'))
    # flashlight + egg
    b.append(rect(40, 150, 24, 44, INK, '#888', 1.6, 4, 1) + path('M34,150 L70,150 L64,136 L40,136 Z', '#ddd', '#ddd', 1.4, 1))
    b.append(egg(52, 92, 26, 36, 6))
    b.append(path('M40,136 L28,70 M64,136 L76,70', '#ffd36b', sw=1.2, dash='3 3'))
    b.append(t(6, 214, 'egg held on a bright flashlight', 10.5, fill=INK))
    b.append(t(170, 30, 'SOUND', 12, 'middle', 'bold', '#9be29f'))
    b.append(egg(170, 104, 34, 46, 6, 'good'))
    b.append(t(290, 30, 'BAD', 12, 'middle', 'bold', '#ff8a80'))
    b.append(egg(290, 104, 34, 46, 18, 'bad'))
    b.append(t(170, 176, 'small air pocket,', 10, 'middle', fill='white') + t(170, 189, 'faint yolk shadow', 10, 'middle', fill='white'))
    b.append(t(290, 176, 'large air pocket,', 10, 'middle', fill='white') + t(290, 189, 'dark mass, blotches', 10, 'middle', fill='white'))
    y = 238
    b.append(tl(8, y, [('Large air pocket, dark or moving mass, blotches,', True), ('cracks, or a bad smell: throw it out.', True),
                       'Float test: one that floats is old: throw it out.', 'Crack each egg into a separate bowl first.'], 11.5, 15))
    return svg('fig-candling-an-egg', y + 70, '\n'.join(b), 'Candling an egg')


@fig('fig-mylar-bucket-pack',
     'The container system (04-03): a food-grade bucket, a Mylar liner bag, dry food (about 10 percent moisture or less), oxygen absorbers sized to the container and opened last, the Mylar sealed with a clothes iron or hair straightener, then the lid, and a label on the outside: contents, weight, date packed and the ingredient label.',
     'Cut-away of a 5-gallon bucket. Inside, a Mylar bag full of dry grain with oxygen absorbers on top; the top of the bag is folded over and sealed with a hot iron. A lid sits above. A label on the outside lists contents, weight, date packed and ingredients. A small jar beside it holds the unused absorbers, resealed at once.',
     ['04-03'])
def mylar():
    b = []
    bx, by, bw, bh = 70, 80, 150, 190
    b.append(path(f'M{bx},{by} L{bx + 10},{by + bh} L{bx + bw - 10},{by + bh} L{bx + bw},{by}', INK, INK, 2.2, 0.06))
    b.append(t(bx + bw / 2, by + bh + 18, '1. food-grade bucket', 10.5, 'middle', 'bold'))
    # mylar bag
    b.append(path(f'M{bx + 8},{by + 6} L{bx + 16},{by + bh - 6} L{bx + bw - 16},{by + bh - 6} L{bx + bw - 8},{by + 6}', '#8a8a8a', '#bbb', 2, 0.3))
    b.append(shade(bx + 18, by + 50, bw - 36, bh - 58, AMBER, 0.45) + t(bx + bw / 2, by + 140, 'DRY food', 11, 'middle', 'bold'))
    b.append(t(bx + bw / 2, by + 154, '(about 10% moisture', 9.5, 'middle') + t(bx + bw / 2, by + 166, 'or less)', 9.5, 'middle'))
    for dx in (40, 66, 92):
        b.append(rect(bx + dx, by + 36, 18, 12, BLUE, BLUE, 1.4, 2, 0.4))
    b.append(t(bx + bw + 8, by + 46, '3. oxygen absorbers,', 10.5, weight='bold') + t(bx + bw + 8, by + 59, 'sized to the bucket,', 10) + t(bx + bw + 8, by + 72, 'opened LAST', 10, weight='bold'))
    # sealed top
    b.append(path(f'M{bx + 20},{by - 6} L{bx + bw - 20},{by - 6}', '#8a8a8a', sw=6))
    b.append(rect(bx + 40, by - 26, 46, 14, RED, RED, 1.4, 3, 0.35) + t(bx + 92, by - 15, 'iron', 9.5))
    b.append(t(bx + bw + 8, by - 4, '4. seal the Mylar', 10.5, 'start', 'bold'))
    b.append(t(bx - 6, by + 32, '2. Mylar bag', 10.5, 'end', 'bold'))
    b.append(rect(bx - 6, by - 56, bw + 12, 14, INK, INK, 1.8, 3, 0.25) + t(bx + bw / 2, by - 64, 'then the lid', 10.5, 'middle'))
    # label
    b.append(rect(bx + 30, by + 92, 90, 36, INK, 'white', 1.2, 2) + tl(bx + 36, by + 104, ['contents · weight', 'date packed', 'ingredient label'], 8.5, 10.5))
    b.append(t(bx - 6, by + 112, '5. label', 10.5, 'end', 'bold'))
    # jar for spare absorbers
    jx = 290
    b.append(rect(jx, by + 120, 40, 50, INK, 'none', 1.6, 6) + rect(jx - 2, by + 112, 44, 10, INK, INK, 1.4, 2, 0.3))
    for k in range(3):
        b.append(rect(jx + 8, by + 158 - k * 13, 24, 10, BLUE, BLUE, 1.2, 2, 0.4))
    b.append(tl(jx + 20, by + 186, ['unused absorbers:', 'reseal in a jar', 'AT ONCE'], 9.5, 11.5, 'middle'))
    y = by + bh + 48
    b.append(tl(8, y, ['Absorbers are not desiccants: moist food sealed without', 'oxygen can grow botulism.',
                       ('No absorbers with sugar, salt, or anything moist or oily.', True)], 11.5, 15))
    return svg('fig-mylar-bucket-pack', y + 56, '\n'.join(b), 'Packing a bucket with Mylar and oxygen absorbers')


@fig('fig-sprouting-jar',
     'Sprouting in a jar (04-16): soak the seed overnight, drain completely, then rinse and drain twice a day, morning and evening, with the jar tilted mouth-down so it drains, at room temperature, out of direct sun. Ready in 2 to 6 days, when the sprout is about as long as the seed. Musty, sour, slimy or mouldy: throw it out.',
     'A glass jar with a mesh lid tilted mouth-down in a bowl so water drains out. Beside it, a row of four seeds showing the stages: soaked seed, a seed just splitting, a short sprout, and a sprout about as long as the seed marked ready.',
     ['04-16'])
def sprouting():
    b = []
    # bowl and tilted jar
    b.append(path('M20,170 Q90,220 160,170 Z', INK, INK, 1.8, 0.08))
    b.append(f'<g transform="rotate(35 90 120)">' + rect(60, 60, 60, 100, INK, BLUE, 1.8, 10, 0.08) +
             shade(64, 120, 52, 36, AMBER, 0.45) + rect(58, 156, 64, 12, INK, INK, 1.6, 2, 0.25) +
             ''.join(line(60 + k * 8, 158, 60 + k * 8, 166, INK, 0.8) for k in range(1, 8)) + '</g>')
    b.append(t(150, 70, 'tilted mouth-DOWN', 10.5, weight='bold') + t(150, 83, 'mesh lid', 10.5) + t(150, 96, 'drains into a bowl', 10.5))
    b.append(t(20, 230, 'room temperature, out of direct sun', 10.5))
    b.append(rule(244))
    b.append(t(6, 264, 'Rinse and drain twice a day:', 12, weight='bold'))
    stages = [('soaked', 0), ('day 1', 6), ('day 2-3', 14), ('READY', 26)]
    for i, (lab, ln) in enumerate(stages):
        x = 40 + i * 84
        b.append(f'<ellipse cx="{x}" cy="300" rx="12" ry="8" fill="{AMBER}" fill-opacity="0.45" stroke="{INK}" stroke-width="1.4"/>')
        if ln:
            b.append(path(f'M{x + 10},302 q{ln * 0.6},4 {ln},-2', GREEN, sw=2.6))
        b.append(t(x + 6, 330, lab, 10.5, 'middle', 'bold' if lab == 'READY' else None, GREEN if lab == 'READY' else INK))
    b.append(t(354, 346, 'sprout about as long as the seed', 9.5, 'end'))
    y = 372
    b.append(tl(8, y, ['Ready in 2 to 6 days. Keep finished sprouts cold.', ('Musty, sour, slimy or mouldy: throw the batch out.', True)], 11.5, 15))
    return svg('fig-sprouting-jar', y + 40, '\n'.join(b), 'Sprouting in a jar')


@fig('fig-drying-rack-over-stove',
     'Drying with heat you already have (04-06): a screen rack above a wood stove, with a thermometer at rack level, is good for plant food, and for meat only if the thermometer at the rack reads 140 °F the whole time. A covered solar-drying screen is for fruit, vegetables and herbs only: never meat.',
     'Two panels. Left: a wood stove with a screen rack hung above it holding sliced fruit, and a thermometer clipped at rack level; label: meat only if the rack reads 140 °F the whole time. Right: a screen in the sun on blocks, covered with a fine cloth, holding fruit and herbs, with air moving under it; a crossed-out piece of meat says never meat.',
     ['04-06'])
def drying_rack():
    b = [t(6, 18, 'Above a wood stove', 12.5, weight='bold')]
    gy = 230
    b.append(line(0, gy, 170, gy, INK, 2))
    b.append(rect(30, 150, 100, 70, INK, INK, 2, 4, 0.2) + rect(40, 220, 10, 10, INK, INK, 1, 0, 0.4) + rect(110, 220, 10, 10, INK, INK, 1, 0, 0.4))
    b.append(rect(66, 30, 20, 120, INK, INK, 1.6, 0, 0.15) + flame(80, 210, 1.1))
    for dy in (0, 12):
        b.append(path(f'M54,{126 - dy} q4,-8 0,-14', AMBER, sw=1.4) + path(f'M106,{126 - dy} q4,-8 0,-14', AMBER, sw=1.4))
    b.append(rect(14, 84, 140, 6, INK, 'none', 1.4, 0, dash='2 2') + line(14, 30, 14, 84, INK, 1) + line(154, 30, 154, 84, INK, 1))
    for x in (24, 44, 110, 130):
        b.append(f'<ellipse cx="{x}" cy="82" rx="8" ry="4" fill="{AMBER}" fill-opacity="0.6"/>')
    b.append(rect(136, 60, 8, 22, RED, 'white', 1.4, 3) + t(150, 56, 'thermometer', 9.5, 'end'))
    b.append(t(150, 104, 'at rack level', 9.5, 'end'))
    b.append(tl(4, gy + 22, [('Plant food: yes.', True), ('Meat: only if the rack', True), ('reads 140 °F the', True), ('WHOLE time.', True)], 11, 13.5, fill=AMBER))
    b.append(line(180, 6, 180, gy + 76, INK, 0.8, op=0.4))
    b.append(t(190, 18, 'Solar drying screen', 12.5, weight='bold'))
    b.append(circle(330, 46, 14, AMBER, AMBER, 1.6, 0.4))
    b.append(line(186, gy, 360, gy, INK, 2))
    b.append(rect(196, 170, 150, 6, INK, 'none', 1.4, 0, dash='2 2') + rect(196, 176, 14, gy - 176, INK, INK, 1, 0, 0.3) + rect(332, 176, 14, gy - 176, INK, INK, 1, 0, 0.3))
    for x in (214, 238, 262, 286):
        b.append(f'<ellipse cx="{x}" cy="168" rx="9" ry="4" fill="{AMBER}" fill-opacity="0.6"/>')
    b.append(path('M300,166 q6,-10 12,-2 q6,-10 12,0', GREEN, sw=2))
    b.append(path('M192,158 Q270,138 350,158', INK, sw=1.4, dash='3 2') + t(270, 132, 'fine cloth cover', 10, 'middle'))
    b.append(arrow(220, 204, 300, 204, BLUE, 1.4, 6) + t(260, 222, 'air under it', 9.5, 'middle', fill=BLUE))
    b.append(tl(190, gy + 22, [('Fruit, vegetables,', True), ('herbs only.', True)], 11, 13.5, fill=GREEN))
    b.append(rect(300, gy + 30, 30, 16, RED, RED, 1.4, 6, 0.3) + cross(296, gy + 24, 38, 28, RED, 2.6))
    b.append(t(315, gy + 66, 'NEVER meat', 10.5, 'middle', 'bold', RED))
    y = gy + 98
    b.append(tl(8, y, ['Whenever a fire is lit for cooking or heat, something', 'should be drying near it.'], 11.5, 15))
    return svg('fig-drying-rack-over-stove', y + 40, '\n'.join(b), 'Drying racks: stove and sun')


@fig('fig-haybox',
     'The haybox (07-02): bring the food to a full rolling boil right through the pot, then move the covered pot into a heavily insulated box. Check with a thermometer before serving: still above 140 °F is fine; just dropped below 140 °F, reheat to 165 °F; below 140 °F for more than 2 hours, throw it out (CDC). Dry beans: soak, discard the water and boil 30 minutes first.',
     'Two steps. Left: a lidded pot on a fire at a full rolling boil, bubbles right through. Right: the same covered pot packed inside a cooler stuffed with towels, with a thermometer. A table of three outcomes: above 140 °F fine; just below 140 °F reheat to 165 °F; below 140 °F for more than 2 hours throw out.',
     ['07-02'])
def haybox():
    b = [t(6, 18, '1. Full rolling boil,', 12, weight='bold') + t(6, 33, 'right through the pot', 12, weight='bold')]
    gy = 170
    b.append(line(0, gy, 150, gy, INK, 2) + flame(50, gy - 2, 1.2) + flame(74, gy - 2, 1.4) + flame(98, gy - 2, 1.1))
    b.append(rect(30, 70, 90, 74, INK, INK, 2, 6, 0.1) + rect(26, 62, 98, 10, INK, INK, 1.6, 3, 0.35))
    for (x, y) in ((50, 120), (74, 100), (98, 124), (62, 132), (88, 86), (104, 104), (44, 96)):
        b.append(circle(x, y, 4, BLUE, 'none', 1.4))
    b.append(arrow(146, 100, 176, 100, INK, 2, 8))
    b.append(t(186, 18, '2. Covered pot into a', 12, weight='bold') + t(186, 33, 'heavily insulated box', 12, weight='bold'))
    b.append(rect(186, 52, 164, 118, BLUE, BLUE, 2, 8, 0.12) + rect(200, 64, 136, 96, AMBER, AMBER, 1.2, 14, 0.35))
    b.append(rect(232, 84, 72, 56, INK, INK, 2, 6, 0.15) + rect(228, 78, 80, 8, INK, INK, 1.4, 3, 0.35))
    b.append(t(268, 154, 'towels, blankets, straw', 9.5, 'middle'))
    b.append(line(296, 66, 296, 110, RED, 2) + circle(296, 112, 3, RED, RED) + rect(290, 50, 30, 16, INK, 'white', 1.2, 2) + t(305, 62, '°F', 9.5, 'middle', 'bold'))
    y = 196
    b.append(t(6, y, 'Check with a thermometer before serving:', 12, weight='bold'))
    rows = [('above 140 °F', 'fine', GREEN), ('just dropped below 140 °F', 'reheat to 165 °F', AMBER), ('below 140 °F for over 2 hours', 'THROW OUT', RED)]
    for i, (a, c, col) in enumerate(rows):
        yy = y + 22 + i * 22
        b.append(rect(6, yy - 14, 348, 20, col, col, 1.2, 3, 0.1) + t(12, yy, a, 11.5) + t(348, yy, c, 11.5, 'end', 'bold', col))
    y2 = y + 96
    b.append(tl(8, y2, [('Dry beans: soak 5+ hours, THROW AWAY the soak water,', True), ('boil 30+ minutes in fresh water, THEN the box.', True),
                        'An overnight haybox is not breakfast.'], 11.5, 15))
    return svg('fig-haybox', y2 + 56, '\n'.join(b), 'Haybox cooking')


@fig('fig-dutch-oven-coals',
     'Dutch oven coals (Missouri Department of Conservation, as on 07-04): total briquettes = 2 × the diameter in inches for about 325 °F; a 12-inch oven takes 24, with two-thirds (16) on the lid and one-third (8) underneath for baking. Add or remove 2 briquettes for about 25 °F. Every 15 minutes, turn the oven a quarter turn and the lid a quarter turn the other way. Check with a thermometer.',
     'Side view of a three-legged camp Dutch oven with a rimmed lid. Sixteen briquettes sit on the lid in a ring and eight sit underneath between the legs. Labels: 12-inch oven, about 325 °F, 24 briquettes, 16 on the lid, 8 underneath; add or remove 2 for about 25 °F. A top view shows curved arrows: oven a quarter turn one way, lid a quarter turn the other way, every 15 minutes.',
     ['07-04'])
def dutch_oven():
    b = [t(6, 18, '12-inch oven, about 325 °F = 24 briquettes', 12, weight='bold')]
    gy = 200
    b.append(line(0, gy, 230, gy, INK, 2))
    ox, oy, ow = 40, 110, 150
    b.append(path(f'M{ox},{oy} L{ox},{oy + 50} Q{ox},{oy + 66} {ox + 16},{oy + 66} L{ox + ow - 16},{oy + 66} Q{ox + ow},{oy + 66} {ox + ow},{oy + 50} L{ox + ow},{oy} Z', INK, INK, 2.2, 0.25))
    b.append(rect(ox - 6, oy - 10, ow + 12, 10, INK, INK, 2, 2, 0.4) + rect(ox - 6, oy - 18, 8, 8, INK, INK, 1.4) + rect(ox + ow - 2, oy - 18, 8, 8, INK, INK, 1.4))
    for lx in (ox + 20, ox + ow / 2, ox + ow - 20):
        b.append(line(lx, oy + 66, lx, gy, INK, 3))
    for k in range(8):
        b.append(rect(ox + 6 + k * 18, oy - 28, 13, 10, AMBER, AMBER, 1, 3, 0.85))
    for k in range(8):
        b.append(rect(ox + 6 + k * 18, oy - 42, 13, 10, AMBER, AMBER, 1, 3, 0.85))
    for k in range(4):
        b.append(rect(ox + 30 + k * 12, gy - 10, 10, 9, AMBER, AMBER, 1, 3, 0.85))
        b.append(rect(ox + 92 + k * 12, gy - 10, 10, 9, AMBER, AMBER, 1, 3, 0.85))
    b.append(t(ox + ow / 2, oy - 50, '16 on the lid (two-thirds)', 11, 'middle', 'bold', AMBER))
    b.append(t(ox + ow / 2, gy + 18, '8 underneath (one-third)', 11, 'middle', 'bold', AMBER))
    b.append(tl(4, gy + 44, ['Rule: briquettes = 2 × diameter', '(10-inch oven: 20).', ('±2 briquettes ≈ ±25 °F', True), '(about 350 °F: 26).'], 11, 14))
    # top view turn
    cx, cy = 296, 110
    b.append(t(cx, 40, 'Every 15 min', 11.5, 'middle', 'bold'))
    b.append(circle(cx, cy, 40, INK, INK, 2, 0.08) + circle(cx, cy, 30, INK, 'none', 1.2, dash='3 2'))
    b.append(path(f'M{cx - 50},{cy + 10} A52,52 0 0 0 {cx - 10},{cy + 52}', INK, sw=1.8) + arrow(cx - 18, cy + 50, cx - 8, cy + 52, INK, 1.8, 6))
    b.append(path(f'M{cx + 20},{cy - 18} A26,26 0 0 0 {cx - 18},{cy - 20}', RED, sw=1.8) + arrow(cx - 10, cy - 24, cx - 20, cy - 18, RED, 1.8, 6))
    b.append(tl(cx, cy + 70, ['oven: ¼ turn', 'one way'], 10, 12, 'middle'))
    b.append(tl(cx, cy - 52 + 0, [''], 1))
    b.append(tl(cx, cy + 102, ['lid: ¼ turn', 'the other way'], 10, 12, 'middle', fill=RED))
    y = gy + 116
    b.append(tl(8, y, ['Cold or wind: expect more. Briquettes last about 30', 'minutes. Check with a thermometer inside the pot.'], 11.5, 15))
    return svg('fig-dutch-oven-coals', y + 40, '\n'.join(b), 'Dutch oven coal placement')


@fig('fig-rocket-stove-cutaway',
     'Rocket stove (07-02): an insulated L-shaped burn chamber; fuel feeds in sideways on a shelf while air passes underneath; the short vertical chimney makes a strong draft; the pot sits on supports with a gap so the hot gases reach it. Level, non-combustible ground; never indoors, in a tent or in a garage.',
     'Cut-away of an L-shaped rocket stove. Sticks lie on a shelf in the horizontal feed tube, with an air arrow passing under the shelf. The burn chamber turns upward into a short vertical chimney surrounded by insulation such as wood ash or vermiculite inside an outer can. A pot sits on small supports above the chimney top, with a gap for the hot gases to flow out around the pot.',
     ['07-02'])
def rocket():
    b = []
    gy = 260
    b.append(line(0, gy, 360, gy, INK, 2))
    # outer can
    ox, ow = 120, 150
    b.append(rect(ox, 100, ow, gy - 100, INK, INK, 2.2, 4, 0.06))
    b.append(shade(ox + 2, 102, ow - 4, gy - 104, AMBER, 0.25) + t(ox + ow + 4, 150, 'insulation', 10, 'start', 'bold', AMBER) + t(ox + ow + 4, 162, '(ash or', 9) + t(ox + ow + 4, 173, 'vermiculite)', 9))
    # L chamber
    cx1, cx2 = 170, 220
    b.append(path(f'M30,{gy - 70} L{cx1},{gy - 70} L{cx1},100 L{cx2},100 L{cx2},{gy - 20} L30,{gy - 20} Z', INK, 'white', 2.2))
    # shelf
    b.append(line(30, gy - 42, 170, gy - 42, INK, 2.4))
    for k in range(4):
        b.append(line(20, gy - 48 - k * 5, 150, gy - 52 - k * 5, AMBER, 4))
    b.append(t(20, gy - 80, 'fuel on the shelf', 10.5, 'start', 'bold'))
    b.append(arrow(10, gy - 30, 140, gy - 30, BLUE, 1.8, 7) + t(14, gy - 4, 'air under the shelf', 10.5, fill=BLUE))
    b.append(flame(190, gy - 50, 1.6) + flame(196, 170, 1.4) + flame(194, 130, 1.2))
    b.append(t(195, 214, 'burn', 9.5, 'middle') + t(195, 225, 'chamber', 9.5, 'middle'))
    b.append(arrow(195, 120, 195, 80, RED, 1.8, 6))
    # supports and pot
    b.append(rect(150, 86, 10, 14, INK, INK, 1.4, 0, 0.5) + rect(230, 86, 10, 14, INK, INK, 1.4, 0, 0.5))
    b.append(rect(130, 30, 130, 56, INK, INK, 2.2, 6, 0.15) + t(195, 62, 'pot', 11, 'middle', 'bold'))
    b.append(arrow(150, 92, 112, 70, RED, 1.4, 5) + arrow(240, 92, 278, 70, RED, 1.4, 5))
    b.append(tl(276, 50, ['supports:', 'a gap for the', 'hot gases'], 10, 12))
    b.append(tl(4, 110, [('short vertical', True), ('chimney:', True), 'strong draft'], 10.5, 12.5) + arrow(80, 118, 162, 140, INK, 1.2, 5))
    y = gy + 28
    b.append(tl(8, y, [('Level, non-combustible ground. Chimney very hot.', True), ('Never indoors, in a tent or in a garage.', True)], 11.5, 15))
    return svg('fig-rocket-stove-cutaway', y + 42, '\n'.join(b), 'Rocket stove cutaway')


@fig('fig-solar-box-cooker',
     'Box solar cooker (07-03): a cardboard box inside a larger box, the gap packed with crumpled newspaper or wool; the inside lined with aluminium foil; a dark pot with a lid inside; a clear plastic or glass lid; foil-covered flaps as reflectors. An oven thermometer inside; do not open it to look.',
     'Cut-away of two nested cardboard boxes with crumpled paper insulation in the gap. The inner box is lined with foil and holds a dark lidded pot and an oven thermometer. A clear lid covers the top, and a foil-covered reflector flap is propped up behind, bouncing sunlight down through the clear lid.',
     ['07-03'])
def solar_box():
    b = []
    gy = 250
    b.append(line(0, gy, 360, gy, INK, 2))
    ox, oy, ow, oh = 40, 130, 260, 120
    b.append(rect(ox, oy, ow, oh, AMBER, AMBER, 2, 2, 0.15))
    for k in range(10):
        b.append(circle(ox + 12 + k * 26, oy + oh - 10, 6, INK, 'none', 0.8))
    b.append(rect(ox + 22, oy + 8, ow - 44, oh - 30, '#8a8a8a', '#ddd', 2.6, 1, 0.5))
    b.append(t(ox + 6, oy + 24, '', 1))
    b.append(rect(ox + 16, oy - 6, ow - 32, 6, BLUE, BLUE, 1.6, 1, 0.25) + t(ox + ow - 16, oy - 12, 'clear lid', 10.5, 'end', 'bold', BLUE))
    b.append(rect(ox + 90, oy + 40, 70, 52, INK, INK, 2, 6, 0.85) + rect(ox + 86, oy + 34, 78, 8, INK, INK, 1.4, 3, 0.9))
    b.append(t(ox + 125, gy + 16, 'dark pot, lid on', 10.5, 'middle', 'bold'))
    b.append(rect(ox + 182, oy + 50, 22, 30, INK, 'white', 1.4, 3) + t(ox + 193, oy + 36, 'oven', 8.5, 'middle') + t(ox + 193, oy + 46, 'thermom.', 8.5, 'middle'))
    # reflector flap
    b.append(line(ox + 16, oy - 6, ox - 20, 20, '#8a8a8a', 5) + t(4, 14, 'foil reflector flap', 10.5, weight='bold'))
    b.append(circle(320, 34, 16, AMBER, AMBER, 1.6, 0.5))
    b.append(arrow(300, 44, 200, 120, AMBER, 1.6, 6) + arrow(298, 40, 60, 80, AMBER, 1.6, 6) + arrow(60, 82, 120, 166, AMBER, 1.6, 6))
    b.append(tl(ox + ow + 6, oy + 30, ['foil', 'lining'], 10, 12) + tl(ox + ow + 6, oy + 90, ['paper or', 'wool in', 'the gap'], 10, 12, fill=AMBER))
    y = gy + 42
    b.append(tl(8, y, ['Slow-oven heat on a clear day: two to four times the', 'usual cooking time. Do not open it to look.',
                       'Water: if not boiled, use a WAPI indicator (→ 03-04).'], 11.5, 15))
    return svg('fig-solar-box-cooker', y + 58, '\n'.join(b), 'Box solar cooker')


@fig('fig-coal-heat-zones',
     'Heat zones (07-01): let the fire burn down to a glowing bed of coals, then rake them into a hot zone (deep coals) for searing and boiling, a medium zone (thinner coals) for most cooking, and a cool zone (few or no coals) to move food to when it is getting ahead of you. Move the food, not the fire.',
     'Top view of a ring of stones around a fire pit with a grate across it. The coals are raked into three zones: on the left a deep pile marked hot, searing and boiling; in the middle a thinner layer marked medium, most cooking; on the right a few scattered coals marked cool, move food here. A pot and a pan sit on the grate.',
     ['07-01'])
def coal_zones():
    b = [t(6, 18, 'Seen from above', 11.5, italic=True)]
    cx, cy, r = 180, 140, 110
    for k in range(16):
        import math
        a = k / 16 * 2 * math.pi
        b.append(f'<ellipse cx="{round(cx + r * 1.42 * math.cos(a), 1)}" cy="{round(cy + r * 0.95 * math.sin(a), 1)}" rx="16" ry="11" fill="{INK}" fill-opacity="0.18" stroke="{INK}" stroke-width="1.4"/>')
    zones = [(cx - 90, RED, 0.75, 14, 'HOT'), (cx, AMBER, 0.55, 7, 'MEDIUM'), (cx + 90, AMBER, 0.25, 3, 'COOL')]
    import random
    random.seed(4)
    for zx, col, op, n, lab in zones:
        for i in range(n * 2):
            dx, dy = random.uniform(-30, 30), random.uniform(-50, 50)
            b.append(circle(round(zx + dx, 1), round(cy + dy, 1), 6, col, col, 0.8, op))
        b.append(t(zx, cy + 136, lab, 12, 'middle', 'bold', RED if lab == 'HOT' else AMBER))
    for k in range(9):
        b.append(line(cx - 120 + k * 30, cy - 66, cx - 120 + k * 30, cy + 66, INK, 1.2, op=0.5))
    b.append(line(cx - 124, cy - 66, cx + 124, cy - 66, INK, 2) + line(cx - 124, cy + 66, cx + 124, cy + 66, INK, 2))
    b.append(circle(cx - 90, cy - 20, 26, INK, INK, 2, 0.2) + t(cx - 90, cy - 16, 'pot', 10, 'middle', 'bold'))
    b.append(circle(cx + 4, cy + 20, 22, INK, INK, 2, 0.2) + t(cx + 4, cy + 24, 'pan', 10, 'middle', 'bold'))
    y = cy + 166
    b.append(tl(8, y, ['Hot: searing, boiling. Medium: most cooking.', 'Cool: move food there when it gets ahead of you.',
                       ('Move the FOOD, not the fire. Cook on coals, not flames.', True)], 11.5, 15))
    return svg('fig-coal-heat-zones', y + 58, '\n'.join(b), 'Coal heat zones')

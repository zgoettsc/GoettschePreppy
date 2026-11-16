"""F2: sanitation, hygiene and laundry diagrams (new ids only)."""
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


@fig('fig-two-bin-humanure',
     'Two-bin composting (13-06): bin one receives, every addition covered at once with a thick layer of straw, leaves or sawdust; when it is full it rests, closed and undisturbed for as long as you can possibly manage, while bin two receives. Then swap. Bins closed on all sides, rodent- and child-proof, on soil, placed by 13-07.',
     'Two closed bins side by side on soil, each with a lid and hardware-cloth sides. The left bin is labelled 1, receiving: waste covered at once with a thick carbon layer. The right is labelled 2, resting: lid closed, undisturbed as long as possible. A curved arrow says swap when bin 1 is full. Notes: on soil, downhill and far from water, the edible garden and the kitchen.',
     ['13-06'])
def two_bin():
    b = []
    gy = 200
    b.append(line(0, gy, 360, gy, INK, 2) + shade(0, gy, 360, 14, AMBER, 0.3) + t(352, gy + 12, 'soil', 10, 'end'))
    for i, (title, sub, col) in enumerate([('1. RECEIVING', 'cover every addition', GREEN), ('2. RESTING', 'closed, undisturbed', BLUE)]):
        x = 20 + i * 176
        b.append(rect(x, 70, 140, gy - 70, INK, 'none', 2.2))
        for k in range(1, 7):
            b.append(line(x + k * 20, 70, x + k * 20, gy, INK, 0.6, op=0.4))
        for k in range(1, 6):
            b.append(line(x, 70 + k * 22, x + 140, 70 + k * 22, INK, 0.6, op=0.4))
        b.append(rect(x - 6, 58, 152, 12, INK, INK, 1.8, 2, 0.3))
        b.append(t(x + 70, 22, title, 12.5, 'middle', 'bold', col) + t(x + 70, 38, sub, 10.5, 'middle'))
        if i == 0:
            b.append(shade(x + 2, 150, 136, 48, AMBER, 0.45) + shade(x + 2, 136, 136, 14, AMBER, 0.8))
            b.append(t(x + 70, 147, 'thick carbon cover', 9.5, 'middle', 'bold'))
        else:
            b.append(shade(x + 2, 90, 136, 108, AMBER, 0.45) + t(x + 70, 150, 'as long as you', 10, 'middle') + t(x + 70, 162, 'possibly can', 10, 'middle'))
    b.append(t(90, 52, 'lid', 9.5, 'middle'))
    b.append(t(90, 216, 'hardware cloth all round', 9.5, 'middle'))
    b.append(path('M120,236 Q180,262 266,236', INK, sw=1.6) + arrow(250, 241, 266, 236, INK, 1.6, 6) + t(180, 270, 'full? swap', 11, 'middle', 'bold'))
    y = 296
    b.append(tl(8, y, [('Only waste, toilet paper and cover material.', True), 'Gloves and boots; hands washed with soap straight after.',
                       'Children never near it. Placed by → 13-07: downhill', 'and far from water, the edible garden and the kitchen.'], 11.5, 15))
    return svg('fig-two-bin-humanure', y + 72, '\n'.join(b), 'Two-bin composting')


@fig('fig-tippy-tap',
     'Tippy-tap (13-02): a jug hung from a frame with a small hole near the cap, tipped by a string tied to a foot pedal; soap hangs on a string beside it. Hands-free and uses very little water. Built from a jug, cord, two sticks and a nail.',
     'Two upright sticks with a crossbar. A jug hangs from the crossbar by its handle; a string runs from the jug\'s cap down to a stick lying on the ground as a foot pedal. A foot presses the pedal and the jug tips, pouring a thin stream from a small hole near the cap onto hands. A bar of soap hangs on a string from the crossbar. The rinse water runs off and away from the station.',
     ['13-02'])
def tippy_tap():
    b = []
    gy = 260
    b.append(line(0, gy, 360, gy, INK, 2))
    b.append(line(60, 40, 60, gy, AMBER, 6) + line(260, 40, 260, gy, AMBER, 6) + line(48, 50, 272, 50, AMBER, 6))
    b.append(t(266, 140, 'two sticks', 10.5))
    # jug tipped
    jx, jy = 140, 64
    b.append(f'<g transform="rotate(-28 {jx} {jy + 30})">' + rect(jx - 24, jy + 10, 48, 62, INK, BLUE, 1.8, 10, 0.18) +
             rect(jx - 8, jy + 72, 16, 10, INK, INK, 1.4, 2, 0.4) + '</g>')
    b.append(line(jx, 50, jx, jy + 10, INK, 1.4))
    b.append(path(f'M{jx + 36},{jy + 74} q10,30 6,70', BLUE, sw=2))
    b.append(t(jx + 50, jy + 62, 'small hole', 10) + t(jx + 50, jy + 74, 'near the cap', 10))
    # string to pedal
    b.append(line(jx + 20, jy + 76, 196, gy - 12, INK, 1.2, '4 2'))
    b.append(line(150, gy - 8, 240, gy - 16, AMBER, 5) + t(238, gy + 16, 'foot pedal', 10.5, 'middle'))
    b.append(path(f'M200,{gy - 24} l26,-4 l4,8 l-30,6 Z', INK, INK, 1.4, 0.3) + arrow(214, gy - 50, 214, gy - 30, RED, 1.8, 6))
    # hands under stream
    b.append(figure_g([('l', [(150, 196), (184, 214)], 12), ('l', [(206, 196), (186, 214)], 12)], INK, 0.35))
    # soap
    b.append(line(90, 50, 90, 120, INK, 1.2) + rect(80, 120, 20, 14, AMBER, AMBER, 1.4, 4, 0.5) + t(90, 150, 'soap on', 10, 'middle') + t(90, 162, 'a string', 10, 'middle'))
    b.append(path(f'M120,{gy} q4,-6 8,0 q4,-6 8,0 q4,-6 8,0 q4,-6 8,0 q4,-6 8,0 q4,-6 8,0', INK, sw=1.2, op=0.6) + t(112, gy + 16, 'rinse water runs off and away', 10))
    y = gy + 42
    b.append(tl(8, y, [('Hands never touch the jug.', True), 'Jug, cord, two sticks and a nail. One at the toilet,', 'one at the kitchen.'], 11.5, 15))
    return svg('fig-tippy-tap', y + 56, '\n'.join(b), 'Tippy-tap handwashing station')


@fig('fig-three-tub-dishwashing',
     'Three-tub dishwashing (13-10): scrape first; tub 1 WASH, hot water and soap, cleanest to dirtiest; tub 2 RINSE, clean warm water; tub 3 SANITIZE, 1 tablespoon of unscented 5 to 9 percent bleach in 1 gallon of clean water, dishes fully under; then air dry on a rack, no towel. The sanitize tub is not drinkable. Wash and rinse water become greywater.',
     'A row of steps from left to right: a plate being scraped into a waste bin; three tubs labelled 1 wash, hot water and soap; 2 rinse, clean warm water; 3 sanitize, 1 tablespoon bleach per gallon, dishes fully under, not drinkable; then a drying rack labelled air dry, no towel. Arrows from tubs 1 and 2 to a greywater bucket.',
     ['13-10'])
def three_tub():
    b = []
    # scrape
    b.append(t(6, 18, '0. SCRAPE', 11.5, weight='bold'))
    b.append(f'<ellipse cx="44" cy="52" rx="30" ry="8" fill="{INK}" fill-opacity="0.1" stroke="{INK}" stroke-width="1.6"/>')
    b.append(arrow(40, 62, 40, 88, INK, 1.4, 6) + rect(24, 90, 32, 26, INK, INK, 1.4, 2, 0.15) + t(40, 130, 'waste', 9.5, 'middle'))
    tubs = [('1. WASH', ['hot water', 'and soap'], BLUE, 0.15), ('2. RINSE', ['clean', 'warm water'], BLUE, 0.08), ('3. SANITIZE', ['1 Tbsp bleach', 'per 1 gal'], AMBER, 0.25)]
    for i, (title, sub, col, op) in enumerate(tubs):
        x = 86 + i * 92
        b.append(t(x + 40, 18, title, 11.5, 'middle', 'bold', AMBER if i == 2 else INK))
        b.append(path(f'M{x},{40} L{x + 8},{110} L{x + 72},{110} L{x + 80},{40}', INK, col, 2, op))
        b.append(tl(x + 40, 70, sub, 10, 12, 'middle'))
        if i < 2:
            b.append(arrow(x + 82, 76, x + 90, 76, INK, 1.4, 5))
    b.append(tl(270, 128, [('fully under;', True), ('NOT drinkable', True)], 10, 12, 'middle', fill=RED))
    b.append(t(130, 128, 'cleanest to dirtiest', 9.5, 'middle', italic=True))
    # rack
    b.append(rule(160))
    rx = 200
    b.append(t(rx, 182, '4. AIR DRY on a rack', 11.5, weight='bold', fill=GREEN))
    b.append(rect(rx, 240, 140, 8, INK, INK, 1.4, 2, 0.2))
    for k in range(6):
        b.append(f'<ellipse cx="{rx + 20 + k * 20}" cy="218" rx="6" ry="22" fill="{INK}" fill-opacity="0.08" stroke="{INK}" stroke-width="1.4"/>')
    b.append(t(rx + 70, 266, 'no towel', 10.5, 'middle', 'bold', RED))
    # greywater
    b.append(path('M126,112 Q120,170 74,200 M218,112 Q200,180 90,206', BLUE, sw=1.4, dash='4 3'))
    b.append(rect(46, 200, 52, 46, INK, BLUE, 1.6, 4, 0.15) + tl(72, 262, ['greywater:', 'flush or', 'non-food plants'], 9.5, 11.5, 'middle'))
    y = 312
    b.append(tl(8, y, ['Unscented 5 to 9 percent household bleach. Mix fresh', 'daily; label the tub; children away. No bleach: dishes',
                       'into boiling water (tongs). Clean first, then sanitize.'], 11.5, 15))
    return svg('fig-three-tub-dishwashing', y + 58, '\n'.join(b), 'Three-tub dishwashing')


@fig('fig-septic-system',
     'How a septic system works (EPA, as on 13-12): waste water runs down one main drain into a buried, watertight tank; solids sink as sludge, fats and grease float as scum, and the cleared liquid in the middle (effluent) flows out to the drain field, shallow covered trenches in dry soil, where the soil does the treatment.',
     'Cut-away of the ground beside a house. A main drain pipe slopes from the house into a buried tank showing three layers: scum floating at the top, clear effluent in the middle and sludge on the bottom. Tank lids or risers show at the surface. An outlet pipe leads to a drain field of shallow covered trenches with perforated pipes, and arrows show the liquid soaking down through the soil, which treats it before it reaches groundwater.',
     ['13-12'])
def septic():
    b = []
    gy = 70
    b.append(rect(4, 10, 64, gy - 10, INK, INK, 1.8, 0, 0.08) + t(36, 44, 'house', 10.5, 'middle'))
    b.append(line(0, gy, 360, gy, INK, 2) + shade(0, gy, 360, 230, AMBER, 0.12))
    b.append(path(f'M40,{gy} L40,{gy + 24} L92,{gy + 40}', INK, sw=5, op=0.45) + t(6, gy + 64, 'main drain', 10))
    tx, ty, tw, th = 92, gy + 30, 110, 90
    b.append(rect(tx, ty, tw, th, INK, 'white', 2.2, 4))
    b.append(shade(tx + 2, ty + 2, tw - 4, 14, AMBER, 0.6) + t(tx + tw / 2, ty + 13, 'scum', 10, 'middle', 'bold'))
    b.append(shade(tx + 2, ty + 16, tw - 4, 46, BLUE, 0.15) + t(tx + tw / 2, ty + 44, 'effluent', 10, 'middle', 'bold', BLUE))
    b.append(shade(tx + 2, ty + 62, tw - 4, 26, INK, 0.35) + t(tx + tw / 2, ty + 80, 'sludge', 10, 'middle', 'bold'))
    for lx in (tx + 18, tx + tw - 30):
        b.append(rect(lx, gy - 4, 14, 34, INK, INK, 1.4, 2, 0.25))
    b.append(t(tx + tw / 2, gy - 10, 'lids / risers', 10, 'middle'))
    b.append(path(f'M{tx + tw},{ty + 30} L{tx + tw + 30},{ty + 34}', INK, sw=5, op=0.45))
    # drain field
    fx = tx + tw + 30
    for k in range(3):
        y = gy + 26 + k * 0
        x = fx + k * 44
        b.append(rect(x, gy + 16, 34, 26, INK, INK, 1.2, 2, 0.12) + line(x + 4, gy + 30, x + 30, gy + 30, INK, 3, '3 2'))
        for dx in (10, 24):
            b.append(arrow(x + dx, gy + 46, x + dx, gy + 76, BLUE, 1.4, 5))
    b.append(line(fx - 4, gy + 30, fx + 128, gy + 30, INK, 1.2, op=0.5))
    b.append(t(fx + 60, gy - 8, 'drain field', 11, 'middle', 'bold'))
    b.append(tl(fx + 60, gy + 94, ['soil filters it;', 'its organisms eat', 'the germs'], 10, 12, 'middle', fill=GREEN))
    b.append(line(0, gy + 196, 360, gy + 196, BLUE, 1.4, '6 4') + t(356, gy + 190, 'groundwater', 10, 'end', fill=BLUE))
    y = gy + 226
    b.append(tl(8, y, [('The tank is alive: no chemicals, no heavy bleach.', True), ('The field can only soak up so much: less water.', True),
                       'Know where the lids and field are; no driving over them.'], 11.5, 15))
    return svg('fig-septic-system', y + 58, '\n'.join(b), 'How a septic tank and drain field work')


@fig('fig-ash-hopper',
     'The traditional ash hopper (13-09, an outline, not a procedure): a barrel with a false bottom and a spout; dry, sieved hardwood ash on top; soft water such as rainwater trickled slowly through; the liquid collected underneath is caustic lye. Goggles, gloves, ventilation; never boil it down.',
     'Cut-away of a barrel on blocks. Inside, a perforated false bottom holds a thick layer of hardwood ash; rainwater trickles in from a can at the top; liquid drips through the false bottom and runs out of a spout near the base into a bucket. Red warning labels: caustic, treat as lye; goggles and gloves; boiling it down spatters, this is where people get hurt.',
     ['13-09'])
def ash_hopper():
    b = []
    gy = 250
    b.append(line(0, gy, 360, gy, INK, 2))
    bx, by, bw, bh = 70, 70, 120, 150
    b.append(rect(bx - 6, by + bh, 20, gy - by - bh, INK, INK, 1.4, 0, 0.3) + rect(bx + bw - 14, by + bh, 20, gy - by - bh, INK, INK, 1.4, 0, 0.3))
    b.append(rect(bx, by, bw, bh, INK, 'white', 2.2, 6))
    b.append(line(bx + 2, by + 116, bx + bw - 2, by + 116, INK, 3, '6 3') + t(bx + bw + 10, by + 120, 'false bottom', 10))
    b.append(shade(bx + 2, by + 24, bw - 4, 90, INK, 0.25) + t(bx + bw / 2, by + 70, 'hardwood ash', 11, 'middle', 'bold'))
    b.append(t(bx + bw / 2, by + 84, 'dry, sieved', 9.5, 'middle'))
    b.append(shade(bx + 2, by + 118, bw - 4, 30, AMBER, 0.45) + t(bx + bw / 2, by + 138, 'lye', 10, 'middle', 'bold', RED))
    # water can
    b.append(path(f'M{bx + 70},{by - 50} l40,0 l0,26 l-40,0 Z M{bx + 70},{by - 40} l-24,14', BLUE, BLUE, 1.6, 0.2))
    for dy in (0, 12, 24):
        b.append(circle(bx + 44, by - 14 + dy, 2, BLUE, BLUE))
    b.append(tl(bx + 118, by - 40, [('soft water (rain),', True), 'trickled SLOWLY'], 10.5, 12.5, fill=BLUE))
    # spout + bucket
    b.append(path(f'M{bx + bw},{by + bh - 10} l26,6', INK, sw=4) + circle(bx + bw + 28, by + bh + 4, 2, AMBER, AMBER))
    b.append(path(f'M{bx + bw + 10},{by + bh + 12} L{bx + bw + 14},{gy} L{bx + bw + 44},{gy} L{bx + bw + 48},{by + bh + 12} Z', INK, AMBER, 1.6, 0.2))
    b.append(t(bx + bw + 52, by + bh - 12, 'spout', 10))
    y = gy + 26
    b.append(box(4, y - 16, 352, 74))
    b.append(tl(12, y, [('CAUSTIC: treat it exactly like bought lye.', True), 'Goggles, gloves, ventilation, children away.',
                        ('Never boil it down: boiling caustic spatters.', True), 'This is where people get hurt.'], 11.5, 15, fill=RED))
    return svg('fig-ash-hopper', y + 80, '\n'.join(b), 'Ash hopper for leaching lye')


@fig('fig-plunger-agitator',
     'Hand laundry (13-04): agitate with a plunger in a bucket (movement, not temperature, removes most dirt); wring hard and rinse once or twice; wring again, then roll the item in a dry towel and stand on it; dry on a high line in the warm room or outdoors.',
     'Four panels. 1: a plunger pumped up and down in a bucket of soapy laundry. 2: hands twisting a wet item to wring it. 3: an item rolled up inside a dry towel on the floor with a foot standing on it. 4: clothes hanging on a high line.',
     ['13-04'])
def plunger():
    b = []
    titles = ['1. Agitate', '2. Wring, rinse', '3. Towel-press', '4. High line']
    for i, s in enumerate(titles):
        x = 4 + i * 89
        b.append(rect(x, 6, 85, 170, INK, 'none', 1.2, 6, op=0.6) + t(x + 42, 24, s, 11, 'middle', 'bold'))
    # 1 bucket + plunger
    b.append(path('M14,90 L20,160 L72,160 L78,90 Z', INK, BLUE, 1.8, 0.15) + shade(16, 104, 60, 50, BLUE, 0.2))
    b.append(line(46, 36, 46, 110, AMBER, 5) + path('M30,124 Q46,104 62,124 Z', INK, INK, 1.6, 0.4))
    b.append(arrow(64, 50, 64, 74, INK, 1.4, 5) + arrow(64, 74, 64, 50, INK, 1.4, 5))
    # 2 wring
    cx = 136
    b.append(path(f'M{cx - 30},96 C{cx - 10},86 {cx + 10},106 {cx + 30},96', BLUE, sw=14, op=0.35))
    for dx in (-14, 0, 14):
        b.append(path(f'M{cx + dx - 4},88 l8,16', INK, sw=1.2))
    b.append(figure_g([('l', [(cx - 40, 96), (cx - 26, 96)], 14), ('l', [(cx + 26, 96), (cx + 40, 96)], 14)], INK, 0.4))
    b.append(path(f'M{cx - 34},70 a10,10 0 1 1 6,-8', INK, sw=1.4) + path(f'M{cx + 34},122 a10,10 0 1 1 -6,8', INK, sw=1.4))
    b.append(tl(cx, 150, ['rinse once', 'or twice'], 10, 12, 'middle'))
    # 3 towel press
    cx = 226
    b.append(rect(cx - 36, 132, 72, 18, AMBER, AMBER, 1.6, 9, 0.35) + line(cx - 36, 152, cx + 36, 152, INK, 1.6))
    b.append(figure_g([('l', [(cx - 4, 60), (cx - 6, 126)], 12), ('l', [(cx - 8, 128), (cx + 14, 128)], 9)], INK, 0.35))
    b.append(arrow(cx + 26, 96, cx + 26, 124, RED, 1.6, 6) + tl(cx, 40, ['rolled in a', 'dry towel'], 9.5, 11.5, 'middle'))
    # 4 line
    cx = 316
    b.append(line(cx - 38, 46, cx + 38, 46, INK, 1.6))
    for dx, w in ((-30, 22), (0, 26), (28, 14)):
        b.append(rect(cx + dx - w / 2, 46, w, 40, BLUE, BLUE, 1.4, 2, 0.25))
    b.append(tl(cx, 120, ['warm room,', 'or outdoors'], 10, 12, 'middle'))
    y = 200
    b.append(tl(8, y, [('Movement, not temperature, removes most dirt.', True), 'Soak first: an overnight soak beats hard scrubbing.',
                       'Wash and rinse water becomes greywater (→ 13-03).'], 11.5, 15))
    return svg('fig-plunger-agitator', y + 58, '\n'.join(b), 'Hand laundry: agitate, wring, press, dry')


@fig('fig-flat-diaper-fold',
     'Cloth diapering with a flat (13-08): a single large square of cotton folded into a pad and laid in a waterproof cover, closed with snap-style fasteners or safety pins. Flats dry fastest. Scrape solids into the toilet system first; store in a lidded dry pail until wash day.',
     'Three steps left to right: a large square of cotton; the square folded into a long pad of several layers; the pad laid inside a waterproof cover with its tabs and a safety pin or snap fastener. Below: solids into the toilet system, then a lidded dry pail.',
     ['13-08'])
def flat_diaper():
    b = []
    b.append(t(6, 18, '1. A flat:', 12, weight='bold') + t(6, 32, 'one big square', 10.5))
    b.append(rect(12, 44, 84, 84, INK, INK, 1.6, 2, 0.06))
    b.append(arrow(104, 86, 122, 86, INK, 1.6, 6))
    b.append(t(124, 18, '2. Fold a pad', 12, weight='bold') + t(124, 32, '(several layers)', 10.5))
    for k in range(3):
        b.append(rect(148 + k * 3, 48 - k * 3, 34, 80, INK, 'white' if k < 2 else INK, 1.4, 2, 0.06 if k == 2 else None))
    b.append(arrow(200, 86, 218, 86, INK, 1.6, 6))
    b.append(t(236, 18, '3. In the cover', 12, weight='bold'))
    b.append(path('M230,48 L346,48 L330,86 Q288,140 246,86 Z', BLUE, BLUE, 1.8, 0.18))
    b.append(rect(274, 52, 28, 60, INK, INK, 1.4, 2, 0.08))
    b.append(rect(226, 44, 18, 14, BLUE, BLUE, 1.4, 3, 0.4) + rect(332, 44, 18, 14, BLUE, BLUE, 1.4, 3, 0.4))
    b.append(tl(288, 140, ['waterproof cover;', 'snaps or safety pins'], 10, 12, 'middle', fill=BLUE))
    b.append(rule(172))
    y = 194
    b.append(tl(8, y, [('Solids into the toilet system; never into the wash.', True), 'Lidded DRY pail until wash day (no pail of water:',
                       'a drowning risk). Hot water and soap; rinse well.', ('Never bleach a pail of soiled diapers.', True)], 11.5, 15))
    return svg('fig-flat-diaper-fold', y + 72, '\n'.join(b), 'Flat cloth diaper and cover')

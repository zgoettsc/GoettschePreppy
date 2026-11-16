"""F2: water diagrams (new ids only)."""
import math
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


@fig('fig-first-flush-diverter',
     'Rain barrel set-up (03-05): the first rain off the roof carries the most dirt, germs and chemicals, so send it away from the barrel and collect what comes after. Screen and lid on the barrel, level solid base, draw from a spigot above the sediment. Then filter, boil or disinfect, and store clean. Never mix rain into treated water.',
     'A roof edge, gutter and downspout. The downspout feeds a capped side pipe first, labelled first flush, the dirtiest runoff, kept out of the barrel; once it is full, water carries on through a screen into a lidded barrel standing on a level platform. A spigot sits above the sediment layer at the bottom. An arrow leads from the spigot to three steps: filter, boil or disinfect, store clean as treated.',
     ['03-05'])
def first_flush():
    b = []
    b.append(poly([(4, 60), (120, 20)], INK, sw=3) + t(30, 30, 'roof', 10.5))
    b.append(path('M110,24 L134,24 L134,36 L110,36', INK, sw=2) + t(140, 30, 'gutter: screen out leaves', 10))
    # downspout
    b.append(path('M122,36 L122,84 L170,84', BLUE, sw=10, op=0.35))
    # first flush pipe
    b.append(rect(112, 84, 20, 150, INK, BLUE, 1.8, 2, 0.12) + rect(108, 234, 28, 8, INK, INK, 1.4, 2, 0.4))
    b.append(shade(114, 150, 16, 82, BLUE, 0.35))
    b.append(tl(4, 130, [('first flush:', True), 'fills first;', 'the dirtiest', 'rain stays', 'OUT of the', 'barrel'], 10.5, 12.5, fill=RED))
    # pipe to barrel
    b.append(path('M132,84 L214,84 L214,106', BLUE, sw=8, op=0.35))
    bx, by, bw, bh = 176, 112, 92, 140
    b.append(rect(bx, by, bw, bh, INK, BLUE, 2, 8, 0.1) + rect(bx - 4, by - 8, bw + 8, 10, INK, INK, 1.6, 3, 0.25))
    b.append(path(f'M{bx + 24},{by - 4} h40', INK, sw=1, dash='2 2') + t(bx + bw + 8, by, 'lid + screen', 10))
    b.append(shade(bx + 2, by + bh - 18, bw - 4, 16, AMBER, 0.45) + t(bx + bw / 2, by + bh - 6, 'sediment', 9, 'middle'))
    b.append(rect(bx + bw, by + bh - 34, 18, 8, INK, INK, 1.4, 2, 0.4) + t(bx + bw + 22, by + bh - 26, 'spigot above', 10) + t(bx + bw + 22, by + bh - 14, 'the sediment', 10))
    b.append(rect(bx - 14, by + bh, bw + 28, 14, INK, INK, 1.6, 2, 0.25) + t(bx + bw / 2, by + bh + 30, 'level, solid platform', 10, 'middle'))
    b.append(t(bx + bw / 2, by + 60, 'RAW', 13, 'middle', 'bold', BLUE))
    y = 312
    b.append(rule(y - 14))
    steps = [('filter', INK), ('boil or disinfect', INK), ('store clean', GREEN)]
    x = 8
    for i, (s, col) in enumerate(steps):
        w = len(s) * 7 + 18
        b.append(badge(x, y, s, col, w, 11))
        if i < 2:
            b.append(arrow(x + w + 4, y + 10, x + w + 20, y + 10, INK, 1.4, 5))
        x += w + 24
    b.append(tl(8, y + 46, [('Never mix rainwater into treated water.', True), 'Barrel full: about 460 lb. Freeze coming: drain it.'], 11.5, 15))
    return svg('fig-first-flush-diverter', y + 84, '\n'.join(b), 'Rain barrel with a first-flush pipe')


@fig('fig-tube-condenser-still',
     'Tube-condenser still (03-03): pot half full of pre-filtered water at a low rolling boil, lid sealed around 10 to 20 ft of soft copper tube that slopes downhill the whole way through a bucket of cold water or snow to the collection jar. Never vinyl or PVC tube; never let the pot boil dry; throw away the salty liquid left in the pot.',
     'A pot on a fire with its lid sealed around a copper tube. The tube leaves the lid, coils downward through a bucket of cold water and snow, and comes out near the bottom to drip into a jar. Arrows show steam going up the tube and water dripping into the jar. Labels: half full, low rolling boil; sealed lid; copper coil slopes downhill all the way; keep the bath cold; never boil dry.',
     ['03-03'])
def tube_still():
    b = []
    gy = 236
    b.append(line(0, gy, 360, gy, INK, 2))
    # fire + pot
    b.append(flame(54, gy - 2, 1.2) + flame(76, gy - 2, 1.0) + flame(34, gy - 2, 0.9))
    b.append(rect(14, 130, 84, 76, INK, INK, 2, 6, 0.08) + shade(16, 168, 80, 36, BLUE, 0.3))
    b.append(t(56, 196, 'half full', 10, 'middle') + rect(10, 122, 92, 10, AMBER, AMBER, 1.6, 2, 0.45))
    b.append(tl(4, 40, [('lid SEALED', True), 'around the tube'], 10.5, 12.5, fill=AMBER))
    for dx in (34, 56, 78):
        b.append(path(f'M{dx},164 q-4,-8 0,-16 q4,-8 0,-16', INK, sw=1.2, op=0.5))
    # tube up and over to bucket
    b.append(path('M70,122 L70,70 L160,92', AMBER, sw=4))
    b.append(arrow(86, 64, 140, 78, INK, 1.2, 5) + t(110, 58, 'steam', 10, 'middle'))
    # bucket
    bx, by, bw, bh = 150, 90, 110, 130
    b.append(path(f'M{bx},{by} L{bx + 8},{by + bh} L{bx + bw - 8},{by + bh} L{bx + bw},{by}', INK, BLUE, 2, 0.15))
    for i in range(4):
        y1 = by + 16 + i * 26
        b.append(path(f'M{bx + 14},{y1 - 4} C{bx + 40},{y1 + 6} {bx + 70},{y1 + 10} {bx + 96},{y1 + 10} C{bx + 70},{y1 + 14} {bx + 40},{y1 + 16} {bx + 14},{y1 + 22}', AMBER, sw=3))
    b.append(path(f'M{bx + 14},{by + 120} L{bx + bw + 30},{by + 128}', AMBER, sw=4))
    b.append(tl(bx + 10, by - 26, [('cold water or snow;', True), 'keep it cold'], 10.5, 12.5, fill=BLUE))
    # jar
    jx = 296
    b.append(rect(jx, gy - 56, 40, 56, INK, BLUE, 1.8, 6, 0.08) + shade(jx + 2, gy - 22, 36, 20, BLUE, 0.35))
    b.append(path(f'M{jx + 20},{gy - 76} v8', BLUE, sw=2) + circle(jx + 20, gy - 62, 2.5, BLUE, BLUE))
    b.append(t(jx + 20, gy + 16, 'jar', 10.5, 'middle'))
    b.append(tl(bx + 36, gy + 16, [('copper coil slopes', True), ('DOWNHILL all the way', True)], 10.5, 12.5, 'middle', fill=AMBER))
    y = gy + 56
    b.append(tl(8, y, ['Soft copper, 3/8 or 1/2 in, 10 to 20 ft. Lead-free fittings.', ('Never vinyl or PVC tube.', True),
                       ('Never let the pot boil dry.', True), 'Throw away the salty liquid left in the pot.', 'Check with a TDS meter: near zero.'], 11.5, 15))
    return svg('fig-tube-condenser-still', y + 86, '\n'.join(b), 'Tube-condenser still')


@fig('fig-micron-scale-germs',
     'Germ sizes against filter pore sizes (29-06): parasites such as Giardia and Cryptosporidium are removed by a filter of 1 micron or finer; bacteria by 0.3 micron or finer; viruses are far smaller, and most portable filters do not remove them, so filtered water still needs chlorine or boiling unless the box says viruses.',
     'A horizontal scale in microns, with each step ten times the last, from 0.01 to 100. Bars show viruses at the small end, bacteria around one micron, and Giardia and Cryptosporidium larger. Vertical lines mark filter pore sizes of 0.3 and 1 micron; parasites are to the right of both, bacteria are to the right of 0.3, and viruses are to the left of both, labelled most portable filters do not stop these.',
     ['29-06'])
def micron_scale():
    b = [t(6, 18, 'Size in microns (each step is 10 times the last)', 11.5, weight='bold')]
    x0, x1 = 20, 340
    lo, hi = -2, 2

    def X(v):
        return round(x0 + (math.log10(v) - lo) / (hi - lo) * (x1 - x0), 1)
    ay = 200
    b.append(line(x0, ay, x1, ay, INK, 1.8))
    for v, lab in ((0.01, '0.01'), (0.1, '0.1'), (1, '1'), (10, '10'), (100, '100')):
        b.append(line(X(v), ay, X(v), ay + 6, INK, 1.4) + t(X(v), ay + 20, lab, 10.5, 'middle'))
    bars = [('viruses', 0.02, 0.25, RED, 100), ('bacteria', 0.4, 4, AMBER, 130), ('Giardia, Cryptosporidium', 3, 15, BLUE, 166)]
    for name, a, c, col, y in bars:
        b.append(rect(X(a), y, X(c) - X(a), 18, col, col, 1.4, 9, 0.3))
        b.append(t(X(a), y - 6, name, 11, weight='bold', fill=col))
    for v, lab in ((0.3, '0.3'), (1, '1')):
        b.append(line(X(v), 40, X(v), ay, INK, 1.6, '5 3'))
    b.append(t(X(0.3) - 3, 50, '0.3 micron filter', 10, 'end', 'bold') + t(X(0.3) - 3, 62, 'stops bacteria', 9.5, 'end'))
    b.append(t(X(1) + 3, 50, '1 micron filter', 10, weight='bold') + t(X(1) + 3, 62, 'stops parasites', 9.5))
    b.append(t(X(0.3) - 4, 136, 'most portable filters', 10, 'end', 'bold', RED) + t(X(0.3) - 4, 148, 'do NOT stop these', 10, 'end', 'bold', RED))
    b.append(t(x1, ay + 36, 'germ sizes approximate', 9.5, 'end', italic=True))
    y = ay + 60
    b.append(tl(8, y, [('Unless the box says viruses, filtered water', True), ('still needs chlorine or boiling.', True),
                       'Chlorine works poorly on parasites; iodine does not', 'kill Cryptosporidium. Boiling kills all three.',
                       'Check whether the pore size is "absolute" or "nominal".'], 11.5, 15))
    return svg('fig-micron-scale-germs', y + 88, '\n'.join(b), 'Germ sizes and filter pore sizes')


@fig('fig-water-cascade',
     'Cascade your water (13-03): clean water, then rinsing, then washing, then dishwater, then flushing or non-food plants. Each drop is used two or three times. Greywater is used the same day, poured on the soil, never on anything eaten raw.',
     'Five basins stepping down from left to right like stairs, joined by arrows: clean water, rinse, wash, dishwater, and at the bottom a toilet bowl and a non-food plant. Notes under them: greywater the same day, on the soil not the leaves, never for drinking, cooking, food or hands.',
     ['13-03', '17-07'])
def water_cascade():
    b = []
    steps = [('clean', 'water', BLUE), ('rinsing', '', BLUE), ('washing', '', INK), ('dishwater', '', INK)]
    for i, (a, c, col) in enumerate(steps):
        x, y = 8 + i * 70, 30 + i * 40
        b.append(path(f'M{x},{y} L{x + 6},{y + 30} L{x + 54},{y + 30} L{x + 60},{y}', INK, col, 1.8, 0.12 + 0.1 * (i > 1)))
        b.append(t(x + 30, y - 6, a, 11, 'middle', 'bold') + (t(x + 30, y + 46, c, 10, 'middle') if c else ''))
        b.append(arrow(x + 58, y + 18, x + 80, y + 46, BLUE, 1.8, 6))
    # final: toilet and plant
    x, y = 290, 190
    b.append(path(f'M{x},{y} q0,30 26,30 q26,0 26,-30 Z', INK, INK, 1.8, 0.1) + rect(x + 14, y + 30, 24, 14, INK, INK, 1.4, 2, 0.1))
    b.append(t(x + 26, y - 8, 'flush', 11, 'middle', 'bold'))
    b.append(path('M226,238 q-2,-18 6,-30 M232,212 q8,-10 18,-6 M230,222 q-10,-10 -18,-4', GREEN, sw=2.4))
    b.append(rect(218, 238, 26, 16, INK, INK, 1.4, 2, 0.2) + tl(231, 270, ['non-food', 'plants'], 10, 12, 'middle', 'bold', GREEN))
    b.append(t(268, 232, 'or', 11, 'middle', italic=True))
    y = 302
    b.append(rule(y - 14))
    b.append(tl(8, y, [('Each drop used two or three times.', True), 'Greywater: use it the same day; on the soil, not the leaves.',
                       ('Never for drinking, cooking, washing food or hands,', True), ('or on the edible parts of food plants.', True)], 11.5, 15))
    return svg('fig-water-cascade', y + 72, '\n'.join(b), 'Water cascade')


@fig('fig-drilled-well-parts',
     'A drilled well (03-10): the sanitary well cap on the casing; the submersible pump hanging near the bottom on its drop pipe; the pitless adapter, where the water line leaves the casing below the frost line; the pressure tank and pressure switch in the house. A purpose-made well bucket (cylinder bailer) is slim enough to go down the casing; an ordinary bucket is not.',
     'Cut-away of the ground with a well casing going down from a capped top to water-bearing rock. Inside, a drop pipe hangs from the top to a submersible pump near the bottom, with its electric cable. Below a dashed frost line, a pitless adapter joins the drop pipe to a buried water line that runs sideways to a house wall, where a pressure tank and pressure switch stand. Beside the casing at the top, a slim well bucket on a rope, next to a crossed-out ordinary bucket.',
     ['03-10'])
def drilled_well():
    b = []
    gy = 60
    b.append(line(0, gy, 360, gy, INK, 2.2) + shade(0, gy, 360, 330, INK, 0.05))
    b.append(line(0, gy + 50, 260, gy + 50, BLUE, 1.4, '6 4') + t(4, gy + 44, 'frost line', 10, fill=BLUE))
    cx = 150
    b.append(rect(cx - 12, gy - 16, 24, 360, INK, 'white', 2))
    b.append(rect(cx - 16, gy - 24, 32, 10, INK, INK, 1.6, 3, 0.35) + t(cx + 20, gy - 16, 'well cap', 10.5, 'start', 'bold'))
    b.append(t(cx + 18, gy + 20, 'casing', 10.5, 'start', 'bold'))
    b.append(line(cx, gy - 14, cx, 352, BLUE, 3))
    b.append(line(cx + 6, gy - 14, cx + 6, 352, AMBER, 1.2, '3 2'))
    b.append(rect(cx - 7, 352, 14, 40, INK, INK, 1.6, 4, 0.4) + t(cx + 14, 372, 'submersible pump', 10.5, 'start', 'bold'))
    b.append(t(cx + 14, 386, '240 V or 120 V: check', 10) + t(cx + 14, 248, 'drop pipe', 10.5) + t(cx + 14, 262, '+ pump cable', 10, fill=AMBER))
    b.append(shade(cx - 11, 300, 22, 100, BLUE, 0.25) + t(cx - 18, 320, 'water', 10, 'end', fill=BLUE))
    # pitless adapter
    py = gy + 80
    b.append(rect(cx - 10, py - 6, 20, 12, INK, INK, 1.6, 2, 0.5) + line(cx + 12, py, 300, py, BLUE, 3))
    b.append(t(cx - 18, py - 6, 'pitless adapter,', 10.5, 'end', 'bold') + t(cx - 18, py + 8, 'below frost line', 10, 'end'))
    # house with tank
    hx = 290
    b.append(rect(hx, 10, 66, gy + 140, INK, INK, 1.8, 0, 0.06) + t(hx + 33, 26, 'house', 10.5, 'middle'))
    b.append(rect(hx + 12, py - 50, 30, 46, INK, INK, 1.6, 12, 0.15) + line(hx, py, hx + 27, py, BLUE, 3) + line(hx + 27, py, hx + 27, py - 4, BLUE, 3))
    b.append(tl(hx + 4, py - 72, ['pressure', 'tank'], 10, 12))
    b.append(rect(hx + 46, py - 34, 14, 14, AMBER, AMBER, 1.4, 2, 0.45) + tl(hx + 4, py + 26, ['switch: on at', '30 or 40 psi,', 'off ~20 higher'], 9.5, 11.5))
    # well bucket
    wx = 40
    b.append(line(wx, 6, wx, gy - 40, INK, 1.2) + rect(wx - 5, gy - 40, 10, 34, BLUE, BLUE, 1.6, 3, 0.35))
    b.append(tl(wx + 10, 16, ['well bucket', '(bailer): fits'], 9.5, 11.5, weight='bold', fill=GREEN))
    b.append(path(f'M236,{gy - 2} L240,{gy - 26} L268,{gy - 26} L272,{gy - 2} Z', INK, INK, 1.4, 0.1) + xmark(245, gy - 24, 18, RED, 2.4) + t(254, gy - 32, 'ordinary', 9.5, 'middle', fill=RED))
    y = 418
    b.append(tl(8, y, ['The casing is a few inches across: measure yours at the cap.', 'Pump voltage is on the breaker and control box (→ 03-10).'], 11, 14))
    return svg('fig-drilled-well-parts', y + 44, '\n'.join(b), 'Parts of a drilled well')

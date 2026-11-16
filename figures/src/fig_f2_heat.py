"""F2: heating, CO, fuel-vapour and smoke diagrams (new ids only)."""
from figlib import *
from fig_heat import heater, co
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


@fig('fig-ducted-heater-window-board',
     'Ducted diesel heater window board: a snug board in the window with two holes, combustion intake and exhaust, both opening outdoors; the warm-air duct stays entirely indoors. Every exhaust joint sealed; the exhaust slopes slightly down and away and ends away from any window, door or vent. Battery CO alarm in the heated room, every run.',
     'Cross-section of a wall with a window. A board fills the bottom of the window opening, with the window closed down onto it. Inside, the heater sits on the floor; a warm-air duct leaves it and stays inside the room. Two pipes pass through the board: the combustion intake and the exhaust, which slopes slightly downward outside and ends away from the window. Labels: seal every exhaust joint, very hot, keep off siding and combustibles. A CO alarm is drawn on the room wall.',
     ['08-07'])
def ducted_board():
    b = [t(6, 18, 'INSIDE', 12, weight='bold') + t(354, 18, 'OUTSIDE', 12, 'end', 'bold')]
    wx = 200
    gy = 290
    b.append(line(0, gy, 360, gy, INK, 2) + shade(wx, gy, 160, 10, INK, 0.15))
    # wall with window opening between y 80 and 200
    b.append(rect(wx - 10, 30, 20, 50, INK, INK, 1.6, 0, 0.25) + rect(wx - 10, 200, 20, gy - 200, INK, INK, 1.6, 0, 0.25))
    b.append(rect(wx - 6, 80, 12, 60, BLUE, BLUE, 1.4, 0, 0.2) + t(wx + 14, 104, 'window,', 10, fill=BLUE) + t(wx + 14, 116, 'closed down', 10, fill=BLUE) + t(wx + 14, 128, 'onto board', 10, fill=BLUE))
    b.append(rect(wx - 8, 140, 16, 60, AMBER, AMBER, 1.6, 1, 0.45) + t(wx - 14, 150, 'board', 10.5, 'end', 'bold', AMBER))
    # heater
    hx, hy = 40, 236
    b.append(rect(hx, hy, 80, 44, INK, INK, 1.8, 6, 0.12) + t(hx + 40, hy + 26, 'heater', 11, 'middle', 'bold'))
    b.append(rect(hx + 10, hy + 44, 60, 10, INK, INK, 1.2, 2, 0.2))
    # warm air duct indoors
    b.append(path(f'M{hx + 20},{hy} L{hx + 20},{hy - 80} Q{hx + 20},{hy - 96} {hx + 4},{hy - 96} L{hx - 2},{hy - 96}', AMBER, sw=10, op=0.35))
    for i in range(3):
        b.append(path(f'M{hx - 10},{hy - 104 + i * 9} q-6,-3 -12,0', AMBER, sw=1.6))
    b.append(tl(hx - 34, hy - 126, [('warm-air duct: stays INSIDE', True)], 10.5, 12.5, fill=AMBER))
    # intake
    b.append(path(f'M{hx + 80},{hy + 12} L{wx - 30},{hy + 12} L{wx - 30},160 L{wx + 40},160', INK, sw=5, op=0.35))
    b.append(arrow(wx + 60, 160, wx + 44, 160, BLUE, 1.8, 6) + t(wx + 64, 164, 'intake', 10.5, fill=BLUE))
    # exhaust sloping down and away
    b.append(path(f'M{hx + 80},{hy + 28} L{wx - 46},{hy + 28} L{wx - 46},182 L{wx + 20},182 L{wx + 120},204', RED, sw=5, op=0.5))
    for x, y in ((wx - 46, hy + 28), (wx - 46, 182), (wx + 20, 182)):
        b.append(circle(x, y, 5, RED, 'white', 1.6))
    b.append(arrow(wx + 124, 205, wx + 150, 211, RED, 1.8, 6))
    b.append(tl(wx + 40, 228, [('exhaust: slopes', True), ('slightly DOWN', True), ('and away', True)], 10.5, 12.5, fill=RED))
    b.append(tl(wx + 40, 270, ['very hot: off siding,', 'cord, combustibles'], 10, 12))
    b.append(tl(hx + 34, 196, [('seal every', True), ('exhaust joint', True)], 10, 12, fill=RED))
    b.append(co(24, 52) + tl(52, 50, ['CO alarm in the room,', 'every run'], 10, 12, fill=GREEN))
    y = 320
    b.append(tl(8, y, [('Board edges: comfort. Exhaust joints: life.', True), 'End the exhaust away from any window, door or vent;',
                       'clear snow from it after every storm. Never run it', 'indoors, not even "temporarily".'], 11.5, 15))
    return svg('fig-ducted-heater-window-board', y + 76, '\n'.join(b), 'Ducted heater window board')


@fig('fig-kerosene-flame-height',
     'Wick kerosene heater flame, seen through the glass: correct is a ½-inch flame above the flame spreader, even all round. Too high gives smoke and soot (lower the wick); too low gives smell and carbon monoxide (never run below the wick stop). Check at 5 to 7 minutes, then every 30 minutes.',
     'Three side-by-side drawings of a heater burner seen through its glass. Left, marked correct: an even flame about half an inch above the flame spreader. Middle, too high: tall uneven flames with smoke and soot above. Right, too low: a flame barely above the wick, marked smell and carbon monoxide.',
     ['08-10'])
def kerosene_flame():
    b = []
    panels = [('CORRECT', GREEN, 'ok'), ('TOO HIGH', RED, 'high'), ('TOO LOW', RED, 'low')]
    for i, (title, col, kind) in enumerate(panels):
        x = 6 + i * 118
        cx = x + 54
        b.append(t(cx, 20, title, 13, 'middle', 'bold', col))
        b.append(rect(x + 14, 40, 80, 130, INK, BLUE, 1.6, 6, 0.06))
        b.append(rect(x + 20, 150, 68, 20, INK, INK, 1.4, 2, 0.2) + t(cx, 164, 'wick', 9, 'middle'))
        b.append(rect(x + 24, 118, 60, 6, INK, INK, 1.4, 1, 0.45))
        if kind == 'ok':
            b.append(path(f'M{x + 26},{118} q14,-14 28,0 q14,-14 28,0', AMBER, AMBER, 1.6, 0.4))
            b.append(line(x + 100, 118, x + 100, 104, INK, 1.2) + line(x + 96, 104, x + 104, 104, INK, 1.2) + line(x + 96, 118, x + 104, 118, INK, 1.2))
            b.append(t(x + 97, 98, '½ in', 10.5, 'start', 'bold'))
        elif kind == 'high':
            b.append(path(f'M{x + 26},118 q4,-50 14,-60 q4,30 10,0 q6,-30 12,8 q6,-20 10,0 q8,30 10,52 Z', AMBER, AMBER, 1.6, 0.45))
            for dx in (34, 52, 70):
                b.append(path(f'M{x + dx},56 q-6,-6 0,-12 q6,-6 0,-12', INK, sw=2.4, op=0.55))
        else:
            b.append(path(f'M{x + 30},118 q8,-5 12,0 M{x + 60},118 q6,-4 10,0', AMBER, sw=2))
        b.append(t(cx, 132, 'flame spreader', 8.5, 'middle'))
    notes = [(['½ in above the', 'spreader, even', 'all round'], GREEN),
             (['smoke and soot:', 'lower the wick'], RED),
             (['smell and CO:', 'never below', 'the wick stop'], RED)]
    for i, (ls, col) in enumerate(notes):
        b.append(tl(6 + i * 118 + 54, 190, ls, 11, 13.5, 'middle', 'bold', col))
    b.append(rule(236))
    b.append(tl(8, 256, [('Check at 5 to 7 minutes, then every 30 minutes:', True), 'as the room and tank warm, the flame climbs.',
                         'Strong or continuing smell is not normal.'], 11.5, 15))
    return svg('fig-kerosene-flame-height', 314, '\n'.join(b), 'Kerosene heater flame height')


@fig('fig-box-fan-filter',
     'The clean room in wildfire smoke: windows and door shut, a portable air cleaner on its highest setting, or, if you have none, a box fan with a furnace filter taped to it (a temporary substitute EPA describes). No smoke made inside.',
     'Plan of a closed room with its window and door shut. In the middle, a box fan seen from the side with a furnace filter taped flat against one face; arrows show room air passing through the filter and then the fan. Crossed-out icons: candle, frying pan, aerosol spray. A note: a portable air cleaner sized for the room, that makes no ozone, is better.',
     ['17-14'])
def box_fan():
    b = [rect(6, 8, 348, 240, INK, 'none', 2.4)]
    b.append(line(120, 8, 220, 8, BLUE, 5) + t(170, 26, 'window SHUT', 10.5, 'middle', 'bold', BLUE))
    b.append(line(354, 150, 354, 210, INK, 6) + t(346, 184, 'door', 10.5, 'end') + t(346, 197, 'SHUT', 10.5, 'end', 'bold'))
    # fan side view
    fx, fy = 150, 90
    b.append(rect(fx, fy, 30, 100, INK, INK, 2, 3, 0.15) + t(fx + 15, fy + 116, 'box fan', 10.5, 'middle'))
    b.append(rect(fx - 12, fy - 4, 12, 108, AMBER, AMBER, 1.6, 1, 0.4))
    for yy in (fy + 6, fy + 94):
        b.append(rect(fx - 16, yy - 3, 50, 6, INK, INK, 1, 1, 0.4))
    b.append(tl(fx - 20, fy + 130, ['furnace filter,', 'taped on'], 10.5, 12.5, 'end', fill=AMBER))
    for yy in (fy + 25, fy + 50, fy + 75):
        b.append(arrow(fx - 70, yy, fx - 18, yy, INK, 1.6, 6) + arrow(fx + 34, yy, fx + 80, yy, BLUE, 1.6, 6))
    b.append(t(fx - 70, fy - 8, 'smoky room air', 10) + t(fx + 40, fy - 8, 'filtered air', 10, fill=BLUE))
    # no smoke inside
    b.append(t(244, 206, 'make no smoke:', 10.5, weight='bold', fill=RED))
    for i, s in enumerate(['candles', 'frying', 'sprays']):
        b.append(xmark(244 + i * 36, 214, 8, RED, 2) + t(248 + i * 36, 238, s, 9, 'middle'))
    y = 272
    b.append(tl(8, y, [('Better: a portable air cleaner sized for the room,', True), 'highest setting, a type that makes no ozone.',
                       'The box fan and filter is a temporary substitute.', 'Fresh-air settings off; recirculate.'], 11.5, 15))
    return svg('fig-box-fan-filter', y + 70, '\n'.join(b), 'Box fan with a furnace filter in a clean room')


@fig('fig-propane-pools-low',
     'How an indoor propane cylinder hurts people (30-03): a slow leak overnight spreads along the floor, where nobody smells it at standing height; the heater, lit in the morning, or a water-heater pilot across the room catches the edge of the cloud and it burns all at once.',
     'Cut-away of a room. A propane cylinder stands beside a heater; a shaded layer of gas flows from a loose connection along the floor across the room, under a standing person whose nose is well above it, to a water heater with a pilot flame at floor level. Labels: slow leak overnight, spreads along the floor, nobody smells it at standing height, pilot or heater lights the edge of the cloud.',
     ['30-03'])
def propane_pools():
    b = []
    gy = 220
    b.append(rect(6, 20, 348, gy - 20, INK, 'none', 2) + line(6, gy, 354, gy, INK, 2.4))
    # cylinder + heater
    b.append(rect(24, gy - 70, 36, 70, INK, INK, 1.8, 10, 0.15) + rect(34, gy - 80, 16, 10, INK, INK, 1.4, 2, 0.3))
    b.append(t(42, gy - 34, '20 lb', 9.5, 'middle'))
    b.append(heater(70, gy - 30) + t(87, gy - 36, 'heater', 9.5, 'middle'))
    b.append(circle(52, gy - 76, 5, RED, 'none', 1.8) + t(6, 12, '', 1))
    # gas layer
    b.append(path(f'M56,{gy - 76} q20,20 10,50 Q40,{gy - 14} 90,{gy - 16} Q200,{gy - 26} 340,{gy - 18} L340,{gy} L8,{gy} L8,{gy - 10} Q30,{gy - 20} 56,{gy - 30}', RED, RED, 0, 0.18))
    for x in (120, 180, 240):
        b.append(arrow(x, gy - 10, x + 30, gy - 10, RED, 1.6, 6))
    # person
    b.append(figure_g([('c', (170, 70), 11), ('l', [(170, 84), (170, 150)], 16), ('l', [(170, 150), (164, gy - 4)], 10), ('l', [(170, 150), (178, gy - 4)], 10)], INK, 0.3))
    b.append(t(186, 74, 'nose up here:', 10) + t(186, 86, 'smells nothing', 10))
    # water heater
    b.append(rect(286, 80, 50, gy - 80, INK, INK, 1.8, 6, 0.12) + t(311, 120, 'water', 10, 'middle') + t(311, 132, 'heater', 10, 'middle'))
    b.append(flame(311, gy - 6, 0.7) + t(311, gy - 26, 'pilot', 9.5, 'middle', 'bold', AMBER))
    b.append(tl(70, 44, [('slow leak overnight', True)], 10.5, fill=RED) + arrow(86, 50, 58, gy - 80, RED, 1.2, 5))
    y = gy + 26
    b.append(tl(8, y, [('Propane is heavier than air: it spreads along the floor.', True), 'The heater lit in the morning, or a pilot across the room,',
                       'catches the edge of the cloud: flash fire or explosion.', 'Never in a basement.'], 11.5, 15))
    return svg('fig-propane-pools-low', y + 72, '\n'.join(b), 'Propane leaks pool low')


@fig('fig-vapour-flow',
     'Gasoline vapour is heavier than air: it flows along the floor and can be lit by a water heater\'s pilot light across the room (Maryland Department of the Environment). Never pour or transfer fuel inside the garage.',
     'Cut-away of an attached garage. A gasoline can sits at one side; a shaded layer of vapour flows from it along the floor, past a car, to a gas water heater with a pilot flame at floor level on the far wall. The shared wall and door to the house are on the right. Labels: vapour is heavier than air, flows along the floor; pilot light across the room.',
     ['06-06'])
def vapour_flow():
    b = [t(6, 16, 'Attached garage, cut away', 11.5, italic=True)]
    gy = 210
    b.append(rect(6, 26, 300, gy - 26, INK, 'none', 2) + line(6, gy, 354, gy, INK, 2.4))
    b.append(rect(306, 26, 48, gy - 26, INK, INK, 1.2, 0, 0.06) + t(330, 60, 'house', 10.5, 'middle'))
    b.append(rect(300, 120, 12, gy - 120, INK, 'white', 1.4) + t(316, 114, 'door', 9.5))
    # can
    b.append(rect(24, gy - 40, 32, 40, RED, RED, 1.8, 4, 0.35) + rect(28, gy - 48, 10, 8, RED, RED, 1.2, 1, 0.5) + t(40, gy - 54, 'gasoline', 9.5, 'middle', 'bold', RED))
    # car
    b.append(path(f'M90,{gy - 12} L90,{gy - 40} L114,{gy - 66} L184,{gy - 66} L208,{gy - 40} L226,{gy - 36} L226,{gy - 12} Z', INK, INK, 1.6, 0.08))
    b.append(circle(118, gy - 10, 11, INK, 'white', 1.8) + circle(200, gy - 10, 11, INK, 'white', 1.8))
    # water heater with pilot
    b.append(rect(246, 70, 46, gy - 70, INK, INK, 1.8, 6, 0.12) + t(269, 110, 'water', 10, 'middle') + t(269, 122, 'heater', 10, 'middle'))
    b.append(flame(269, gy - 6, 0.7) + t(269, gy - 26, 'pilot', 9.5, 'middle', 'bold', AMBER))
    b.append(path(f'M56,{gy - 30} Q70,{gy - 18} 90,{gy - 14} Q170,{gy - 4} 260,{gy - 10} L262,{gy} L56,{gy} Z', RED, RED, 0, 0.2))
    for x in (66, 150, 216):
        b.append(arrow(x, gy - 4, x + 22, gy - 4, RED, 1.6, 5))
    b.append(tl(64, 50, [('vapour is heavier than air:', True), 'it flows along the floor', 'to the pilot light'], 10.5, 13, fill=RED))
    y = gy + 26
    b.append(tl(8, y, [('Never pour or transfer fuel inside the garage,', True), ('power on or off.', True),
                       'A fuel-fired appliance that cannot light in an outage', 'lights again the moment power returns.'], 11.5, 15))
    return svg('fig-vapour-flow', y + 72, '\n'.join(b), 'Gasoline vapour flows along the floor')


@fig('fig-heat-ladder-house-to-bag',
     'Why small is warm (08-06): as fuel gets short, step down to smaller spaces with the same heat source, you: house, one room, a tent inside the room, sleeping bags inside the tent, layers inside the bags.',
     'Five nested outlines, each inside the last: a house, one room inside it, a tent inside the room, a sleeping bag inside the tent, and a person in layers inside the bag. Each is labelled, with an arrow showing the steps from house to layers.',
     ['08-06'])
def heat_ladder():
    b = []
    # house
    b.append(poly([(10, 80), (180, 14), (350, 80)], INK, sw=2.2) + rect(16, 80, 328, 240, INK, 'none', 2.2))
    b.append(t(26, 100, '1. House', 12, weight='bold'))
    b.append(rect(40, 112, 280, 196, INK, INK, 2, 2, 0.04) + t(52, 132, '2. One room (→ 08-01)', 12, weight='bold'))
    b.append(poly([(70, 290), (180, 150), (290, 290)], AMBER, AMBER, 2, 0.12, closed=True) + t(180, 204, '3. Tent', 12, 'middle', 'bold', AMBER))
    b.append(rect(118, 214, 124, 64, BLUE, BLUE, 2, 26, 0.15) + t(180, 232, '4. Sleeping bag', 11, 'middle', 'bold', BLUE))
    b.append(figure_g([('c', (140, 256), 9), ('l', [(152, 256), (220, 258)], 16)], INK, 0.35))
    b.append(t(186, 274, '5. layers', 10, 'middle', 'bold'))
    y = 346
    b.append(tl(8, y, [('Each step: a smaller space, the same heat source: you.', True), 'Step down as fuel gets short (→ 08-06).'], 11.5, 15))
    return svg('fig-heat-ladder-house-to-bag', y + 40, '\n'.join(b), 'Smaller is warmer: house to bag')

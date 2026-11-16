from figlib import *
from fig_power import fig as _f
FIGS = {}


def fig(fid, caption, alt, pages):
    def deco(fn):
        FIGS[fid] = dict(fn=fn, caption=caption, alt=alt, pages=pages)
        return fn
    return deco


def heater(x, y, w=34, h=26, color=INK):
    return rect(x, y, w, h, color, color, 1.6, 3, 0.12) + flame(x + w / 2, y + h - 4, 0.8)


def co(x, y, ok=True, label='CO'):
    col = GREEN if ok else RED
    b = rect(x - 12, y - 8, 24, 16, col, col, 1.6, 4, 0.15) + t(x, y + 4, label, 9.5, 'middle', 'bold', col)
    return b + (check(x + 14, y - 14, 10, GREEN, 2.4) if ok else xmark(x + 13, y - 13, 9, RED, 2.4))


def mattress(x, y, w, h):
    return (rect(x, y, w, h, INK, INK, 1.4, 4, 0.08) + rect(x + 4, y + h - 16, w - 8, 12, INK, INK, 1.2, 4, 0.12) +
            (t(x + w / 2, y + h - 7, 'pillow', 8.5, 'middle') if h > 40 else ''))


@fig('fig-warm-room-layout',
     'The warm room: heater behind a barrier at its label clearances, the heater\'s air openings, the door closed and hung with a blanket, everyone sleeping in the room, the CO alarm on the wall opposite the heater at pillow height.',
     'Plan view of one room. The heater stands near the outside wall with the window, inside a barrier drawn at the clearances on its label. The door is closed with a blanket hung over it. Mattresses and a small tent are at the far side, pillows toward the wall opposite the heater, where the CO alarm is mounted at pillow height. An inset shows the window wall from inside: a 3 by 3 inch opening at ceiling level and another at floor level for a propane heater, or the window cracked at least 1 inch for a wick kerosene heater when the room is smaller than its manual requires.',
     ['08-01'])
def warm_room():
    b = [t(8, 16, 'Seen from above', 11.5, italic=True), t(352, 16, 'OUTSIDE WALL', 10.5, 'end', 'bold')]
    x0, y0, x1, y1 = 14, 28, 346, 300
    b.append(rect(x0, y0, x1 - x0, y1 - y0, INK, 'none', 3))
    b.append(line(x0, y0, x1, y0, INK, 6, op=0.5))
    b.append(line(150, y0, 214, y0, BLUE, 6) + t(182, y0 + 15, 'window', 10.5, 'middle', fill=BLUE))
    # heater and barrier
    b.append(rect(132, 50, 100, 78, GREEN, GREEN, 2, 4, 0.06, '6 4'))
    b.append(heater(165, 74))
    b.append(t(182, 118, 'heater', 10.5, 'middle'))
    b.append(tl(240, 62, ['barrier at the', 'clearances on', 'the heater label;', 'floor inside =', 'hot zone'], 10.5, 12.5, fill=GREEN))
    # door
    b.append(line(270, y1, 318, y1, x1 and '#ffffff00', 6))
    b.append(path(f'M270,{y1} A48,48 0 0 1 318,{y1 - 48}', INK, sw=1, dash='3 3', op=0.6))
    b.append(path(f'M268,{y1 - 4} q6,-6 12,0 t12,0 t12,0 t12,0', AMBER, sw=2.2))
    b.append(tl(340, y1 - 92, ['door shut,', 'blanket', 'over it'], 10.5, 12, 'end', fill=AMBER))
    # sleeping
    b.append(mattress(30, 176, 70, 112) + mattress(108, 176, 70, 112))
    b.append(path('M30,250 L64,186 L100,250', INK, sw=1.6, dash='5 3') + t(64, 172, 'tent', 10.5, 'middle'))
    b.append(t(144, 172, 'beds', 10.5, 'middle'))
    # CO alarm opposite wall
    b.append(co(214, y1 - 12))
    b.append(tl(184, y1 - 52, [('CO alarm:', True), 'opposite wall,', 'pillow height'], 10.5, 12.5, fill=GREEN))
    b.append(tl(24, 70, ['smallest room', 'that fits', 'everyone', 'sleeping'], 10.5, 12.5))
    # inset elevation
    yi = 330
    b.append(t(8, yi - 8, 'The window wall, seen from inside', 11.5, italic=True))
    b.append(rect(14, yi, 150, 120, INK, INK, 2, 0, 0.05))
    b.append(rect(50, yi + 34, 78, 52, BLUE, 'none', 2))
    b.append(t(89, yi + 64, 'window', 10, 'middle', fill=BLUE))
    b.append(rect(140, yi + 6, 14, 14, GREEN, GREEN, 1.6, 1, 0.25))
    b.append(rect(140, yi + 100, 14, 14, GREEN, GREEN, 1.6, 1, 0.25))
    b.append(t(14, yi + 134, 'floor', 10, italic=True) + line(14, yi + 120, 164, yi + 120, INK, 2.4))
    b.append(tl(176, yi + 10, [('Propane heater:', True), '3 × 3 in (9 sq in) opening at', 'ceiling level AND at floor', 'level (green squares).'], 11, 13.5))
    b.append(tl(176, yi + 74, [('Wick kerosene heater', True), ('in a small room:', True), 'window open at least 1 in.'], 11, 13.5))
    b.append(t(176, yi + 128, 'Your manual governs.', 11, italic=True))
    return svg('fig-warm-room-layout', yi + 152, '\n'.join(b), 'Warm room layout')


@fig('fig-co-alarm-placement',
     'Carbon monoxide alarms: one on every level and one outside each sleeping area; in the warm room, on the wall opposite the heater at pillow height. Never above the heater, in a ceiling corner, beside a window, door, vent or fan, or in a bathroom.',
     'Cutaway of a two-storey house with a basement. Green alarms: in the upstairs hall outside the bedrooms, on the main floor, in the basement, and in the warm room on the wall opposite the heater at the height of a sleeping person\'s head. Red crossed-out alarms: directly above the heater, in the corner where wall meets ceiling, beside the cracked window, and in the bathroom.',
     ['08-02'])
def co_alarm_placement():
    b = []
    L, R = 14, 346
    yR, y2, y1, yB, yG = 70, 82, 176, 272, 344
    b.append(poly([(L - 4, yR + 14), (180, 16), (R + 4, yR + 14)], INK, sw=2))
    b.append(rect(L, y2, R - L, yG - y2, INK, 'none', 2.4))
    b.append(line(L, y1, R, y1, INK, 2.4) + line(L, yB, R, yB, INK, 2.4))
    b.append(line(0, yB, L, yB, INK, 1, op=0.5) + line(R, yB, 360, yB, INK, 1, op=0.5))
    b.append(shade(L, yB, R - L, yG - yB, INK, 0.06))
    # upstairs: bedroom | hall | bathroom
    b.append(line(124, y2, 124, y1, INK, 2) + line(232, y2, 232, y1, INK, 2))
    b.append(t(69, y2 + 18, 'bedroom', 11, 'middle') + mattress(30, y1 - 34, 76, 30))
    b.append(t(178, y2 + 18, 'hall', 11, 'middle') + co(172, y2 + 52) + tl(178, y2 + 78, ['outside the', 'bedrooms'], 10.5, 12.5, 'middle', fill=GREEN))
    b.append(t(289, y2 + 18, 'bathroom', 11, 'middle') + co(280, y2 + 50, False) + tl(289, y2 + 76, ['not in a', 'bathroom'], 10.5, 12.5, 'middle', fill=RED))
    # main floor: warm room
    b.append(t(22, y1 + 16, 'WARM ROOM', 11, weight='bold'))
    b.append(line(L, y1 + 30, L, y1 + 60, BLUE, 5) + t(22, y1 + 46, 'window', 10, fill=BLUE))
    b.append(co(40, y1 + 74, False) + t(24, y1 + 96, 'by a window', 10, fill=RED))
    b.append(heater(96, yB - 28) + co(110, y1 + 40, False) + t(113, y1 + 64, 'above heater', 10, 'middle', fill=RED))
    b.append(co(222, y1 + 14, False) + t(206, y1 + 18, 'ceiling corner', 10, 'end', fill=RED))
    b.append(line(250, y1, 250, yB, INK, 2))
    b.append(mattress(156, yB - 20, 66, 16))
    b.append(co(232, yB - 36) + tl(180, y1 + 42, ['opposite wall,', 'pillow height'], 10, 12, 'middle', fill=GREEN))
    b.append(t(298, y1 + 18, 'main floor', 10.5, 'middle') + co(292, y1 + 52) + t(298, y1 + 78, 'every level', 10.5, 'middle', fill=GREEN))
    # basement
    b.append(t(24, yB + 18, 'basement', 10.5) + rect(40, yB + 28, 30, 40, INK, INK, 1.4, 2, 0.1) + t(55, yB + 52, 'furn.', 9, 'middle'))
    b.append(co(170, yB + 38) + t(176, yB + 62, 'every level', 10.5, 'middle', fill=GREEN))
    b.append(tl(8, yG + 18, ['Only battery (or battery-backup) alarms work in an outage.',
                             'Height and mounting: follow the alarm\'s own manual.'], 11, 14))
    return svg('fig-co-alarm-placement', yG + 50, '\n'.join(b), 'Where carbon monoxide alarms go')


@fig('fig-propane-heater-hose-route',
     'Portable propane heater on a 20-lb tank: the tank outdoors on a board, the maker\'s hose through a cracked ground-level window or door with a towel at the gap, the fuel filter at the heater\'s regulator, both air openings open, and the CO alarm on the opposite wall at pillow height.',
     'Cutaway of a room at ground level and the yard outside. Outside, a 20-lb propane tank stands upright on a board. The maker\'s hose runs from the tank valve through a window cracked at ground level, with a towel round the gap, to the heater on the floor inside. The fuel filter sits between the hose and the heater regulator. The heater has its clearances marked, 30 inches above, 24 inches in front, 6 inches each side. A 3 by 3 inch opening at ceiling level and another at floor level are open. The CO alarm is on the far wall at pillow height.',
     ['08-09'])
def propane_hose():
    b = []
    W_, gy = 236, 262
    b.append(t(8, 18, 'INSIDE (ground-level room)', 11.5, weight='bold') + t(352, 18, 'OUTDOORS', 11.5, 'end', 'bold'))
    b.append(line(0, gy, 360, gy, INK, 2.4) + shade(W_, gy, 124, 10, INK, 0.15))
    b.append(line(8, 28, 228, 28, INK, 2) + line(8, 28, 8, gy, INK, 2))
    b.append(line(W_, 28, W_, 168, INK, 8, op=0.4) + line(W_, 232, W_, gy, INK, 8, op=0.4))
    b.append(rect(W_ - 5, 168, 10, 46, BLUE, 'none', 2) + tl(W_ - 12, 180, ['window', 'cracked'], 10, 12, 'end', fill=BLUE))
    b.append(rect(W_ - 7, 214, 14, 18, AMBER, AMBER, 1.2, 4, 0.4) + tl(W_ - 12, 210, ['towel at', 'the gap'], 10, 12, 'end', fill=AMBER))
    # openings
    b.append(rect(W_ - 6, 40, 12, 12, GREEN, GREEN, 1.6, 1, 0.3) + rect(W_ - 6, 238, 12, 12, GREEN, GREEN, 1.6, 1, 0.3))
    b.append(tl(W_ - 12, 46, ['3 × 3 in opening', 'at ceiling level'], 10, 12, 'end', fill=GREEN))
    b.append(t(W_ + 10, 252, 'and at floor', 10, fill=GREEN))
    # tank on board
    tx = 286
    b.append(rect(tx - 8, gy - 6, 64, 6, INK, INK, 1.2, 1, 0.4) + t(tx + 24, gy + 22, 'board', 10, 'middle'))
    b.append(rect(tx, gy - 76, 48, 70, INK, INK, 1.8, 14, 0.1) + rect(tx + 10, gy - 92, 28, 16, INK, 'none', 1.6, 3))
    b.append(t(tx + 24, gy - 36, '20 lb', 11, 'middle', 'bold') + t(tx + 24, gy - 23, 'upright', 9.5, 'middle'))
    b.append(t(tx + 24, gy - 98, 'valve', 10, 'middle'))
    # hose
    b.append(path(f'M{tx + 20},{gy - 84} C{tx + 4},{gy - 120} {W_ + 30},{gy - 60} {W_},{gy - 39} C{W_ - 40},{gy - 18} 190,{gy - 4} 152,{gy - 18}', INK, sw=3))
    b.append(t(268, 140, "maker's hose", 10.5, 'middle'))
    # heater with filter and regulator
    hx = 92
    b.append(rect(hx, gy - 52, 50, 52, INK, INK, 1.8, 4, 0.1) + flame(hx + 25, gy - 14, 0.9))
    b.append(rect(hx + 50, gy - 26, 8, 14, INK, INK, 1.4, 2, 0.3))
    b.append(rect(hx + 58, gy - 24, 14, 10, AMBER, AMBER, 1.4, 3, 0.4))
    b.append(tl(hx + 64, gy + 14, ['fuel filter', 'on regulator'], 10, 12, 'start', fill=AMBER))
    b.append(arrow(hx + 25, gy - 56, hx + 25, gy - 104, INK, 1.2, 5) + t(hx + 25, gy - 108, '30 in above', 10, 'middle'))
    b.append(arrow(hx, gy - 30, hx - 40, gy - 30, INK, 1.2, 5) + t(hx - 42, gy - 36, '24 in front', 10, 'middle'))
    b.append(t(hx + 25, gy + 14, '6 in each side', 10, 'middle'))
    # CO alarm
    b.append(rect(8, 196, 26, 16, GREEN, GREEN, 1.6, 4, 0.15) + t(21, 208, 'CO', 9.5, 'middle', 'bold', GREEN))
    b.append(tl(14, 120, ['CO alarm:', 'opposite wall,', 'pillow height'], 10, 12, fill=GREEN) + arrow(26, 154, 22, 192, GREEN, 1.2, 5))
    b.append(tl(8, gy + 50, [('Never bring the 20-lb tank inside. Never a fully', True), ('below-ground room with propane.', True),
                             'Only the maker\'s hoses; no second regulator.', 'Clearances from one common model: check your label.'], 11.5, 14.5))
    return svg('fig-propane-heater-hose-route', gy + 122, '\n'.join(b), 'Propane heater with the tank outdoors')


@fig('fig-heater-barrier-clearances',
     'A fixed, anchored barrier around the heater at the clearances on its label, the hot-zone line taped on the floor, the play area on the far side from the heater and its air openings, and the CO alarm at pillow height.',
     'Plan view of a room. The heater stands inside a ring of play-yard panels anchored to the wall, set back by the clearances printed on its label, with blanks to write the above, front and side distances. A taped line on the floor marks the hot zone that children do not cross. The play area and crib are on the far side of the room from the heater and the air openings. The CO alarm is on the far wall at pillow height.',
     ['20-02'])
def heater_barrier():
    b = [t(8, 16, 'Seen from above', 11.5, italic=True)]
    x0, y0, x1, y1 = 14, 28, 346, 300
    b.append(rect(x0, y0, x1 - x0, y1 - y0, INK, 'none', 3) + line(x0, y0, x1, y0, INK, 6, op=0.5))
    b.append(line(250, y0, 300, y0, BLUE, 6) + t(275, y0 + 14, 'air openings', 10, 'middle', fill=BLUE))
    b.append(heater(78, 50))
    # play-yard barrier: panels
    pts = [(30, y0), (30, 128), (166, 128), (166, y0)]
    b.append(poly(pts, GREEN, sw=4))
    for i in range(30, 167, 17):
        b.append(line(i, 124, i, 132, GREEN, 2))
    b.append(circle(30, y0 + 4, 4, GREEN, GREEN) + circle(166, y0 + 4, 4, GREEN, GREEN))
    b.append(t(186, 52, 'anchored to', 10, fill=GREEN) + t(186, 64, 'the wall', 10, fill=GREEN))
    # clearance dims
    b.append(arrow(95, 80, 95, 122, INK, 1.2, 5) + t(100, 106, 'front ___ in', 10.5))
    b.append(arrow(76, 72, 34, 72, INK, 1.2, 5) + t(36, 88, 'side ___ in', 10))
    b.append(t(98, 44, 'above ___ in', 10.5))
    b.append(tl(186, 90, ['clearances from', 'YOUR heater\'s label', 'and manual'], 10.5, 12.5, fill=GREEN))
    # hot zone tape
    b.append(poly([(22, y0), (22, 140), (176, 140), (176, y0)], AMBER, sw=3, dash='8 5'))
    b.append(t(22, 156, 'tape line: hot zone, children never cross', 10.5, 'start', 'bold', AMBER))
    # play area far side
    b.append(rect(180, 190, 150, 96, INK, INK, 1.4, 6, 0.06) + t(255, 210, 'play area', 11, 'middle'))
    b.append(rect(198, 222, 70, 50, INK, 'none', 1.6, 2) + t(233, 252, 'crib', 10.5, 'middle'))
    b.append(t(255, 284, 'far from heater and vents', 10, 'middle', italic=True))
    b.append(co(60, y1 - 12) + tl(40, y1 - 48, [('CO alarm,', True), 'pillow height'], 10.5, 12.5, fill=GREEN))
    b.append(tl(8, y1 + 22, [('Lit only with an adult in the room and awake.', True), 'Write your label clearances in the blanks on this page.'], 11.5, 14.5))
    return svg('fig-heater-barrier-clearances', y1 + 62, '\n'.join(b), 'Heater barrier and hot zone')

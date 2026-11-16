"""Power diagrams: panels, generator connection, backfeed, siting, cord-and-plug, MC4."""
from figlib import *

FIGS = {}


def fig(fid, caption, alt, pages):
    def deco(fn):
        FIGS[fid] = dict(fn=fn, caption=caption, alt=alt, pages=pages)
        return fn
    return deco


def panel(x, y, w=84, h=56, label='about 20 V'):
    b = [rect(x, y, w, h, INK, INK, 1.6, 2, 0.07)]
    for i in (1, 2):
        b.append(line(x + w * i / 3, y, x + w * i / 3, y + h, INK, 0.8, op=0.4))
    b.append(line(x, y + h / 2, x + w, y + h / 2, INK, 0.8, op=0.4))
    b.append(t(x + w / 2, y + h / 2 + 4.5, label, 12, 'middle', 'bold'))
    return ''.join(b)


def term(x, y, sign, side='right'):
    col = RED if sign == '+' else INK
    dx = 7 if side == 'right' else -7
    return circle(x, y, 3.2, col, col, 1.2) + t(x + dx, y + 5, sign, 14, 'start' if side == 'right' else 'end', 'bold', col)


@fig('fig-series-vs-parallel',
     'Series adds voltage, parallel adds current. Do the cold-voltage check before any series string, and never put a series string into a station with a low input-voltage ceiling.',
     'Top: three panels of about 20 V wired plus to minus in a chain make about 60 V. A box says add the label Voc of every panel, multiply by 1.20, and the result must be below the station maximum PV input voltage. A station with a high voltage ceiling is ticked; a station with a low ceiling is crossed out. Bottom: two panels joined plus to plus and minus to minus with Y-branch connectors make about 20 V with the currents added.',
     ['09-02', '09-03', '09-09', '09-16'])
def series_vs_parallel():
    b = []
    b.append(t(10, 20, 'SERIES: + of one panel to − of the next', 14, weight='bold'))
    xs = [12, 138, 264]
    for x in xs:
        b.append(panel(x, 32))
        b.append(line(x + 18, 88, x + 18, 100) + line(x + 66, 88, x + 66, 100, RED))
    # links: + of panel n to - of panel n+1
    for a, c in ((xs[0], xs[1]), (xs[1], xs[2])):
        b.append(poly([(a + 66, 100), (a + 66, 110), (c + 18, 110), (c + 18, 100)], INK, sw=1.8))
    for x in xs:
        b.append(term(x + 18, 100, '−', 'left') + term(x + 66, 100, '+', 'right'))
    # free ends
    b.append(poly([(30, 100), (30, 124), (150, 124)], INK, sw=1.8))
    b.append(poly([(330, 100), (330, 124), (210, 124)], RED, sw=1.8))
    b.append(rect(150, 116, 60, 16, INK, INK, 1.2, 3, 0.1) + t(180, 128, 'to station', 11, 'middle'))
    b.append(t(180, 152, 'String: about 60 V (20 + 20 + 20)', 13, 'middle', 'bold'))
    b.append(t(180, 168, "Current stays at the weakest panel's level.", 12, 'middle'))
    # cold check
    b.append(rect(10, 180, 340, 74, INK, INK, 1.4, 6, 0.05))
    b.append(tl(20, 198, [('COLD-VOLTAGE CHECK, every series string', True),
                          'Add the label Voc of every panel in the string,',
                          'then × 1.20. The result must be BELOW the station\'s',
                          'max PV input voltage, with a margin.'], 12.5, 15))
    b.append(arrow(95, 254, 95, 272) + arrow(265, 254, 265, 272))
    b.append(rect(10, 274, 164, 76, GREEN, GREEN, 1.8, 6, 0.08))
    b.append(check(18, 282, 16))
    b.append(tl(40, 293, [('HIGH input-voltage', True), ('ceiling station', True)], 12.5, 15, fill=GREEN))
    b.append(tl(18, 328, ['Series string OK, if the', 'cold check passes.'], 12, 14))
    b.append(rect(186, 274, 164, 76, RED, RED, 1.8, 6, 0.08))
    b.append(xmark(194, 282, 15))
    b.append(tl(216, 293, [('LOW input-voltage', True), ('ceiling station', True)], 12.5, 15, fill=RED))
    b.append(tl(194, 328, [('NEVER a series string.', True), 'Kills the input for good.'], 12, 14, fill=RED))

    y0 = 378
    b.append(line(10, y0 - 12, 350, y0 - 12, INK, 0.8, op=0.4))
    b.append(t(10, y0 + 8, 'PARALLEL: all + together, all − together', 14, weight='bold'))
    p1, p2 = 60, 216
    for x in (p1, p2):
        b.append(panel(x, y0 + 20))
        b.append(line(x + 18, y0 + 76, x + 18, y0 + 86) + line(x + 66, y0 + 76, x + 66, y0 + 86, RED))
    ny = y0 + 128
    b.append(poly([(p1 + 18, y0 + 86), (p1 + 18, y0 + 100), (152, ny)], INK, sw=1.8))
    b.append(poly([(p2 + 18, y0 + 86), (p2 + 18, y0 + 100), (152, ny)], INK, sw=1.8))
    b.append(poly([(p1 + 66, y0 + 86), (p1 + 66, y0 + 100), (208, ny)], RED, sw=1.8))
    b.append(poly([(p2 + 66, y0 + 86), (p2 + 66, y0 + 100), (208, ny)], RED, sw=1.8))
    for x in (p1, p2):
        b.append(term(x + 18, y0 + 86, '−', 'left') + term(x + 66, y0 + 86, '+', 'right'))
    b.append(rect(140, ny - 4, 24, 16, INK, INK, 1.4, 3, 0.15) + t(152, ny + 8, 'Y−', 10.5, 'middle', 'bold'))
    b.append(rect(196, ny - 4, 24, 16, RED, RED, 1.4, 3, 0.15) + t(208, ny + 8, 'Y+', 10.5, 'middle', 'bold', RED))
    b.append(t(108, ny + 8, 'Y-branch', 11.5, 'end') + t(232, ny + 8, 'Y-branch', 11.5))
    b.append(line(152, ny + 12, 152, ny + 26) + line(208, ny + 12, 208, ny + 26, RED))
    b.append(rect(150, ny + 26, 60, 16, INK, INK, 1.2, 3, 0.1) + t(180, ny + 38, 'to station', 11, 'middle'))
    b.append(t(180, ny + 64, 'Pair: about 20 V; the currents add.', 13, 'middle', 'bold'))
    b.append(tl(180, ny + 82, ['Cold raises voltage, never current: winter cannot',
                               'push a parallel pair over a voltage ceiling.',
                               'Too much current is normally just clipped (stay under',
                               "a max current if the station's manual lists one)."], 12, 15, 'middle'))
    b.append(t(10, ny + 150, 'Voltages are examples: use your own panel labels.', 11, italic=True))
    return svg('fig-series-vs-parallel', ny + 168, '\n'.join(b), 'Series versus parallel panel wiring')


def gen(x, y, label='GEN', color=INK):
    """Portable generator icon, top-left (x, y), about 46 x 32."""
    return (rect(x, y, 46, 26, color, color, 1.6, 3, 0.1) + t(x + 23, y + 17, label, 11, 'middle', 'bold', color) +
            circle(x + 9, y + 29, 4, color) + circle(x + 37, y + 29, 4, color) +
            line(x + 46, y + 6, x + 52, y + 6, color, 2.2))


def plug_m(x, y, color=INK, d=1):
    """Male plug at the end of a cord pointing in direction d (+1 right, -1 left)."""
    return (rect(x - (0 if d > 0 else 10), y - 6, 10, 12, color, color, 1.4, 2, 0.25) +
            line(x + 10 * d, y - 3, x + 15 * d, y - 3, color, 1.6) + line(x + 10 * d, y + 3, x + 15 * d, y + 3, color, 1.6))


def socket(x, y, color=INK):
    """Wall receptacle face centred on (x, y)."""
    return (rect(x - 9, y - 12, 18, 24, color, color, 1.4, 3, 0.08) +
            line(x - 3, y - 6, x - 3, y - 1, color, 1.6) + line(x + 3, y - 6, x + 3, y - 1, color, 1.6) +
            circle(x, y + 5, 1.6, color, color, 1))


def panelbox(x, y, w=30, h=46, main='on', color=INK, label=True):
    b = [rect(x, y, w, h, color, color, 1.6, 2, 0.08)]
    b.append(rect(x + 5, y + 5, w - 10, 8, RED if main == 'off' else color, 'none', 1.2))
    for i in range(3):
        b.append(line(x + 6, y + 20 + i * 8, x + w - 6, y + 20 + i * 8, color, 2.4, op=0.7))
    if label:
        b.append(t(x + w / 2, y + h + 12, 'panel', 11, 'middle'))
    return ''.join(b)


def wall(x, y1, y2):
    return line(x, y1, x, y2, INK, 5, op=0.35)


@fig('fig-generator-connection-options',
     'Five ways a generator can reach something in the house. Four are allowed with the right person doing the work; backfeeding through an outlet is never allowed.',
     'Five rows, each with a generator outdoors on the left and the house wall: (a) an extension cord to one appliance, always allowed; (b) a cord to an inlet on the wall and a transfer switch beside the panel, licensed electrician; (c) a cord to an inlet and an interlock plate on the panel so the main breaker and the generator breaker are never on together, licensed electrician; (d) a furnace unplugged from its wall receptacle and plugged into the generator cord, a cord-and-plug conversion, decision card DC-07; (e) a cord with two male ends pushed into a wall outlet, crossed out in red: backfeed, never.',
     ['09-04', '09-16'])
def generator_connection_options():
    b = []
    rh = 92
    y0 = 34
    b.append(t(8, 16, 'OUTDOORS', 11.5, weight='bold') + t(8, 28, '20 ft or more', 11))
    b.append(t(106, 16, 'INSIDE THE HOUSE', 11.5, weight='bold'))
    b.append(wall(98, 6, y0 + rh * 5 - 6))
    rows = []
    # (a)
    y = y0
    b.append(gen(8, y + 26))
    b.append(path(f'M60,{y + 38} C80,{y + 38} 90,{y + 56} 120,{y + 56}', INK, sw=2) + plug_m(120, y + 56))
    b.append(rect(142, y + 18, 34, 58, INK, INK, 1.6, 4, 0.06) + line(142, y + 40, 176, y + 40, INK, 1.2) +
             t(159, y + 14, 'fridge', 11, 'middle'))
    rows.append((y, '(a) Extension cord', ["to one appliance's own", 'plug. Anyone. Always', 'allowed.'], GREEN, 'ok'))
    # (b) transfer switch
    y = y0 + rh
    b.append(gen(8, y + 26))
    b.append(path(f'M60,{y + 38} C80,{y + 38} 82,{y + 46} 92,{y + 46}', INK, sw=2))
    b.append(rect(92, y + 39, 12, 14, INK, INK, 1.4, 2, 0.3) + t(98, y + 66, 'inlet', 10.5, 'middle'))
    b.append(line(104, y + 46, 122, y + 46, INK, 2) + rect(122, y + 30, 22, 32, INK, INK, 1.6, 2, 0.15) +
             t(133, y + 50, 'TS', 10.5, 'middle', 'bold'))
    b.append(line(144, y + 46, 150, y + 46, INK, 2) + panelbox(150, y + 22, label=False) + t(165, y + 82, 'panel', 11, 'middle'))
    b.append(t(133, y + 13, 'transfer', 10, 'middle') + t(133, y + 24, 'switch', 10, 'middle'))
    rows.append((y, '(b) Transfer switch:', ['circuits on grid OR', 'generator, never both.', 'Licensed electrician.'], INK, None))
    # (c) interlock
    y = y0 + rh * 2
    b.append(gen(8, y + 26))
    b.append(path(f'M60,{y + 38} C80,{y + 38} 82,{y + 46} 92,{y + 46}', INK, sw=2))
    b.append(rect(92, y + 39, 12, 14, INK, INK, 1.4, 2, 0.3) + t(98, y + 66, 'inlet', 10.5, 'middle'))
    b.append(line(104, y + 46, 128, y + 46, INK, 2))
    px, py = 128, y + 8
    b.append(rect(px, py, 48, 64, INK, INK, 1.6, 2, 0.08))
    b.append(rect(px + 5, py + 6, 17, 10, RED, RED, 1.2, 1, 0.15) + t(px + 13.5, py + 26, 'MAIN', 8.5, 'middle', 'bold', RED) +
             t(px + 13.5, py + 35, 'OFF', 8.5, 'middle', 'bold', RED))
    b.append(rect(px + 26, py + 6, 17, 10, GREEN, GREEN, 1.2, 1, 0.3) + t(px + 34.5, py + 26, 'GEN', 8.5, 'middle', 'bold', GREEN) +
             t(px + 34.5, py + 35, 'ON', 8.5, 'middle', 'bold', GREEN))
    b.append(rect(px + 3, py + 2, 21, 4, INK, INK, 1, 1, 0.6))
    for i in range(2):
        b.append(line(px + 8, py + 46 + i * 8, px + 40, py + 46 + i * 8, INK, 2.4, op=0.7))
    b.append(t(px + 24, y + 84, 'panel + interlock plate', 10, 'middle'))
    rows.append((y, '(c) Interlock + inlet:', ['main and generator', 'breakers never on', 'together. Electrician.'], INK, None))
    # (d) cord-and-plug
    y = y0 + rh * 3
    b.append(gen(8, y + 26))
    b.append(path(f'M60,{y + 38} C80,{y + 38} 92,{y + 60} 118,{y + 60}', INK, sw=2))
    b.append(rect(118, y + 54, 9, 12, INK, INK, 1.4, 2, 0.25))  # female end
    b.append(plug_m(141, y + 60, INK, -1) + path(f'M141,{y + 60} C150,{y + 60} 152,{y + 50} 152,{y + 42}', INK, sw=2))
    b.append(rect(140, y + 6, 40, 36, INK, INK, 1.6, 3, 0.08) + t(160, y + 28, 'furnace', 10.5, 'middle'))
    b.append(socket(116, y + 22) + arrow(126, y + 24, 136, y + 40, INK, 1.2, 5, '2 2'))
    b.append(t(116, y + 46, 'wall', 9.5, 'middle'))
    rows.append((y, '(d) Cord-and-plug:', ['furnace unplugged from', 'its wall receptacle, into', 'the generator cord. DC-07'], INK, None))
    # (e) backfeed
    y = y0 + rh * 4
    b.append(gen(8, y + 26, color=RED))
    b.append(path(f'M60,{y + 38} C80,{y + 38} 92,{y + 46} 112,{y + 46}', RED, sw=2) + plug_m(112, y + 46, RED))
    b.append(plug_m(66, y + 38, RED, -1))
    b.append(socket(142, y + 46, RED))
    b.append(cross(60, y + 14, 106, 56, RED, 4))
    b.append(t(8, y + 84, 'cord with two male ends', 10.5, 'start', None, RED))
    rows.append((y, '(e) Into a wall outlet:', [('BACKFEED. NEVER.', True), 'Kills line workers and', 'neighbours (floor 30-01).'], RED, 'no'))
    for (y, head, lines, col, mark) in rows:
        tx = 196
        if mark == 'ok':
            b.append(check(tx, y + 18, 14))
        if mark == 'no':
            b.append(xmark(tx, y + 18, 13))
        hx = tx + (20 if mark else 0)
        b.append(t(hx, y + 30, head, 12.5, weight='bold', fill=col))
        b.append(tl(tx, y + 47, lines, 12, 15, fill=col if col == RED else INK))
        b.append(line(4, y + rh - 2, 356, y + rh - 2, INK, 0.6, op=0.3))
    b.append(tl(8, y0 + rh * 5 + 14, ['(b) and (c) need a generator whose manual says it suits', 'transfer equipment (240 V). See your manual.'], 11, 14, italic=True))
    return svg('fig-generator-connection-options', y0 + rh * 5 + 46, '\n'.join(b), 'Generator connection options')


def house_scene(y0, mode):
    b = []
    gy = y0 + 178
    b.append(line(0, gy, 360, gy, INK, 1.2, op=0.5))
    # poles and street line
    for px in (262, 338):
        b.append(line(px, y0 + 22, px, gy, INK, 3) + line(px - 18, y0 + 30, px + 18, y0 + 30, INK, 2))
    sl = RED if mode == 'bad' else INK
    b.append(line(240, y0 + 30, 358, y0 + 30, sl, 2.2 if mode == 'bad' else 1.6))
    b.append(rect(268, y0 + 44, 18, 26, sl, sl, 1.6, 4, 0.15) + line(277, y0 + 44, 277, y0 + 30, sl, 1.4))
    # line worker on pole 2
    wc = RED if mode == 'bad' else INK
    b.append(circle(326, y0 + 42, 5, wc, 'none', 1.8) + line(326, y0 + 47, 328, y0 + 72, wc, 1.8) +
             line(327, y0 + 53, 338, y0 + 36, wc, 1.8) + line(328, y0 + 72, 336, y0 + 88, wc, 1.8) +
             line(328, y0 + 72, 322, y0 + 90, wc, 1.8))
    # house
    b.append(poly([(70, gy), (70, y0 + 92), (180, y0 + 92), (180, gy)], INK, sw=1.8))
    b.append(poly([(62, y0 + 96), (125, y0 + 52), (188, y0 + 96)], INK, sw=1.8))
    # service drop and meter
    b.append(line(180, y0 + 78, 180, y0 + 92, INK, 2))
    b.append(path(f'M277,{y0 + 70} Q230,{y0 + 90} 180,{y0 + 78}', sl, sw=1.8))
    b.append(line(180, y0 + 92, 186, y0 + 116, sl, 1.6))
    b.append(circle(188, y0 + 124, 8, sl, sl, 1.6, 0.12))
    b.append(t(200, y0 + 128, 'meter', 11))
    b.append(t(212, y0 + 98, 'service', 11))
    # panel inside on right wall
    main = 'off' if mode == 'good' else 'on'
    b.append(panelbox(146, y0 + 104, 26, 40, main, label=False) + t(159, y0 + 100, 'panel', 11, 'middle'))
    b.append(line(172, y0 + 122, 180, y0 + 124, INK, 1.4) + line(180, y0 + 124, 180, y0 + 124))
    return b, gy


@fig('fig-backfeed-path',
     'Backfeeding: generator power pushed into an outlet flows out through the panel and meter to the pole transformer, which raises it to the street line\'s voltage and kills a line worker who believes the line is dead. The safe path: an inlet and a transfer switch or interlock, with the main breaker off.',
     'Two house cutaways with the service wires, the meter, the panel, a pole transformer and a line worker on the next pole. Top, crossed out: a generator outside with a cord that has two male ends pushed into a wall outlet; red arrows run from the outlet to the panel, out through the meter and the service wires to the transformer and along the street line to the worker. Bottom, ticked: the generator cord goes to an outdoor inlet and a transfer switch or interlock; the main breaker is off and nothing reaches the street.',
     ['30-01', '17-08', '29-04'])
def backfeed_path():
    b = []
    # --- bad ---
    y0 = 26
    b.append(badge(8, 4, 'BACKFEED THROUGH AN OUTLET: NEVER', RED, 262))
    s, gy = house_scene(y0, 'bad')
    b += s
    b.append(gen(6, gy - 32, color=RED))
    b.append(path(f'M58,{gy - 26} C66,{gy - 26} 68,{gy - 36} 78,{gy - 36}', RED, sw=2) + socket(84, gy - 36, RED))
    b.append(tl(6, gy - 52, ['two-male', 'cord'], 10.5, 12, fill=RED))
    # red flow path
    b.append(arrowpath([(92, gy - 40), (112, gy - 50), (146, y0 + 140)], RED, 2.4, 8))
    b.append(arrowpath([(172, y0 + 120), (186, y0 + 116), (184, y0 + 96)], RED, 2.4, 7))
    b.append(arrow(200, y0 + 80, 262, y0 + 70, RED, 2.4, 8))
    b.append(arrow(292, y0 + 24, 318, y0 + 24, RED, 2.4, 8))
    b.append(tl(8, gy + 15, ['It flows out through the meter to the pole transformer, which raises', 'it to the street line\'s voltage. The worker believes the line is dead.'], 11, 14, fill=RED))
    b.append(tl(300, y0 + 104, ['line', 'worker'], 11, 13, 'middle', fill=RED))
    # --- good ---
    y1 = gy + 52
    b.append(line(4, y1 - 12, 356, y1 - 12, INK, 0.8, op=0.4))
    b.append(check(8, y1 - 2, 14))
    b.append(t(28, y1 + 10, 'SAFE: INLET + TRANSFER SWITCH OR INTERLOCK', 12, weight='bold', fill=GREEN))
    s, gy2 = house_scene(y1 + 6, 'good')
    b += s
    b.append(gen(6, gy2 - 32, color=GREEN))
    b.append(path(f'M58,{gy2 - 26} C64,{gy2 - 26} 64,{gy2 - 30} 66,{gy2 - 30}', GREEN, sw=2))
    b.append(rect(66, gy2 - 37, 10, 14, GREEN, GREEN, 1.4, 2, 0.3) + tl(6, gy2 - 52, ['to inlet', 'on wall'], 10.5, 12, fill=GREEN))
    b.append(rect(106, y1 + 6 + 112, 22, 30, GREEN, GREEN, 1.6, 2, 0.15) + t(117, y1 + 6 + 131, 'TS', 10, 'middle', 'bold', GREEN))
    b.append(arrowpath([(76, gy2 - 30), (96, gy2 - 30), (106, y1 + 6 + 140)], GREEN, 2.2, 7))
    b.append(arrow(128, y1 + 6 + 128, 145, y1 + 6 + 128, GREEN, 2.2, 7))
    b.append(t(159, y1 + 6 + 158, 'MAIN OFF', 10.5, 'middle', 'bold', RED))
    b.append(tl(8, gy2 + 15, ['The main breaker is off whenever the generator feeds the panel:', 'nothing reaches the meter or the street.'], 11, 14, fill=GREEN))
    b.append(tl(8, gy2 + 50, ['TS = transfer switch beside the panel, or an interlock plate on', 'the panel. Both installed by a licensed electrician.'], 11, 14))
    return svg('fig-backfeed-path', gy2 + 80, '\n'.join(b), 'How backfeeding kills, and the safe path')


@fig('fig-generator-siting',
     'Where the generator runs: outdoors, 20 feet or more from any window, door or vent, exhaust pointed away from every house, never in a garage or under a deck or overhang.',
     'Plan view from above. A house with windows, a door and a vent, an attached garage and a deck. Inside the garage and under the deck a generator is crossed out in red. Out in the yard a generator sits 20 feet or more from the nearest window, its exhaust arrow pointing away from the house and away from the neighbour\'s house. A checklist below repeats the rules and says to keep battery carbon monoxide alarms on inside.',
     ['09-04', '09-15', '30-01', '17-08'])
def generator_siting():
    b = [t(8, 16, 'Seen from above', 11.5, italic=True)]
    # house
    b.append(rect(14, 28, 170, 150, INK, INK, 2, 0, 0.05) + t(99, 108, 'HOUSE', 13, 'middle', 'bold'))
    for wy in (48, 128):  # windows on right wall
        b.append(line(184, wy, 184, wy + 22, BLUE, 5) + t(178, wy + 15, 'window', 10.5, 'end', fill=BLUE))
    b.append(line(120, 178, 146, 178, BLUE, 5) + t(133, 170, 'door', 10.5, 'middle', fill=BLUE))
    b.append(line(14, 60, 14, 74, BLUE, 5) + t(20, 71, 'vent', 10.5, fill=BLUE))
    # garage
    b.append(rect(14, 178, 92, 78, INK, INK, 2, 0, 0.05) + line(30, 256, 90, 256, INK, 4, op=0.15))
    b.append(t(60, 194, 'garage', 11, 'middle') + t(60, 270, 'door open', 10, 'middle'))
    b.append(gen(36, 212, color=RED) + cross(30, 204, 64, 44, RED, 3.5))
    # deck
    b.append(rect(184, 34, 46, 60, INK, 'none', 1.4, dash='3 3') + t(207, 30, 'deck', 10.5, 'middle'))
    b.append(gen(186, 50, color=RED) + cross(186, 44, 44, 44, RED, 3.5))
    # neighbour
    b.append(rect(292, 20, 64, 84, INK, INK, 1.6, 0, 0.05) + t(324, 64, 'neigh-', 10.5, 'middle') + t(324, 76, 'bour', 10.5, 'middle'))
    # good generator
    gx, gy = 236, 214
    b.append(rect(gx - 8, gy - 8, 64, 48, GREEN, GREEN, 1.4, 4, 0.08))
    b.append(gen(gx, gy, color=GREEN))
    b.append(arrow(gx + 54, gy + 6, gx + 104, gy + 48, AMBER, 2.4, 9))
    b.append(tl(gx + 40, gy + 64, ['exhaust away', 'from every house'], 10.5, 12, 'start', fill=AMBER))
    # dimension
    b.append(arrow(203, 172, 186, 152, GREEN, 1.6, 6) + arrow(203, 172, 226, 204, GREEN, 1.6, 6))
    b.append(tl(212, 168, ['20 ft', 'or more'], 11.5, 13, weight='bold', fill=GREEN))
    # checklist
    y = 304
    items = [
        ('ok', '20 ft or more from any window, door or vent'),
        ('ok', 'Exhaust pointed away from every house'),
        ('ok', 'Dry, level, solid ground; open to air'),
        ('no', 'Never in a garage (door open or not), a'),
        (None, 'basement or shed, or under a deck or overhang'),
        ('ok', 'Battery CO alarms on inside, every level'),
    ]
    for k, s in items:
        if k == 'ok':
            b.append(check(10, y - 11, 12))
        elif k == 'no':
            b.append(xmark(10, y - 10, 11))
        b.append(t(30, y, s, 12, fill=RED if k == 'no' or (k is None) else INK))
        y += 17
    return svg('fig-generator-siting', y + 12, '\n'.join(b), 'Generator siting outdoors')


@fig('fig-cord-and-plug-conversion',
     'Cord-and-plug conversion (DC-07): the furnace gets its own plug. Normal: it plugs into the receptacle where its old house circuit now ends. Outage: main breaker off and locked, furnace unplugged from the wall and plugged into the generator cord, which has one male and one female end.',
     'Two rows. Normal: the panel with breakers on feeds a wall receptacle; the furnace cord and plug are plugged into it; plug and receptacle are labelled. Outage: the main breaker is off with a lock; the wall receptacle is empty; the furnace plug goes into the female end of an extension cord whose male end is in the generator outdoors. A red note says never a cord with two male ends and never into house wiring.',
     ['09-04', '30-08'])
def cord_and_plug():
    b = []

    def furnace(x, y):
        return (rect(x, y, 70, 92, INK, INK, 1.8, 3, 0.06) + t(x + 35, y + 22, 'FURNACE', 11.5, 'middle', 'bold') +
                rect(x + 8, y + 34, 54, 30, INK, 'none', 1, op=0.5) + t(x + 35, y + 53, 'junction box', 9.5, 'middle'))

    def tag(x, y, s):
        return rect(x, y, 84, 15, AMBER, AMBER, 1.2, 3, 0.15) + t(x + 42, y + 11, s, 9.5, 'middle', 'bold')

    # NORMAL
    b.append(t(8, 18, 'NORMAL DAYS', 13, weight='bold'))
    b.append(panelbox(14, 38, 34, 54, 'on', label=False) + t(31, 106, 'panel', 11, 'middle') + t(31, 32, 'all ON', 10, 'middle'))
    b.append(path('M48,70 L150,70', INK, sw=2) + t(98, 64, 'old house cable', 10, 'middle'))
    b.append(socket(162, 70) + t(162, 98, 'receptacle', 10.5, 'middle') + t(162, 110, 'same rating', 10, 'middle'))
    b.append(tag(120, 120, 'RECEPTACLE'))
    b.append(furnace(266, 26))
    b.append(path('M290,90 C290,110 220,112 196,96 C188,90 182,76 174,72', INK, sw=2.2) + plug_m(184, 72, INK, -1))
    b.append(tag(214, 124, 'FURNACE PLUG'))
    b.append(line(4, 150, 356, 150, INK, 0.8, op=0.4))
    # OUTAGE
    y0 = 158
    b.append(t(8, y0 + 12, 'IN AN OUTAGE', 13, weight='bold'))
    b.append(panelbox(14, y0 + 38, 34, 54, 'off', label=False) + t(31, y0 + 106, 'panel', 11, 'middle'))
    b.append(t(54, y0 + 32, 'MAIN OFF,', 10.5, weight='bold', fill=RED) + t(54, y0 + 44, 'locked or taped', 10.5, fill=RED))
    b.append(rect(24, y0 + 26, 14, 10, RED, RED, 1.4, 2, 0.2) + path(f'M27,{y0 + 26} v-5 a4,4 0 0 1 8,0 v5', RED, sw=1.6))
    b.append(path(f'M48,{y0 + 70} L150,{y0 + 70}', INK, sw=2, op=0.5))
    b.append(socket(162, y0 + 70) + t(162, y0 + 98, 'empty', 10.5, 'middle'))
    b.append(furnace(266, y0 + 26))
    b.append(path(f'M290,{y0 + 118} C290,{y0 + 140} 250,{y0 + 150} 226,{y0 + 150}', INK, sw=2.2) + plug_m(226, y0 + 150, INK, -1))
    b.append(rect(202, y0 + 144, 9, 12, INK, INK, 1.4, 2, 0.25))
    b.append(path(f'M202,{y0 + 150} C160,{y0 + 150} 120,{y0 + 168} 74,{y0 + 168}', INK, sw=2.2))
    b.append(wall(60, y0 + 120, y0 + 196) + t(56, y0 + 132, 'outside', 10, 'end') + t(64, y0 + 132, 'inside', 10))
    b.append(gen(6, y0 + 156) + plug_m(66, y0 + 168, INK, -1))
    b.append(tl(6, y0 + 206, ['generator outdoors,', '20 ft or more'], 10.5, 12))
    b.append(tl(110, y0 + 186, ['extension cord: one male end,', 'one female end'], 11, 13))
    y = y0 + 236
    b.append(rect(8, y, 344, 40, RED, RED, 1.6, 5, 0.06) + xmark(16, y + 13, 13))
    b.append(tl(38, y + 16, [('Never a cord with two male ends.', True), ('Never a connection into any house wiring.', True)], 12, 15, fill=RED))
    b.append(tl(8, y + 60, ['The plug: (A) a flanged male inlet on the cabinet, fed by a', 'cord with a female end, or (B) a cord with a male plug through',
                            'a strain relief. Ratings match the circuit (→ 09-04, steps 3 to 5).'], 11, 14))
    return svg('fig-cord-and-plug-conversion', y + 112, '\n'.join(b), 'Cord-and-plug conversion, normal and outage')


@fig('fig-mc4-polarity-check',
     'Check a panel string before plugging it in: meter on DC volts, red probe to the + lead, black to the − lead. A minus sign on the display means a connector is reversed: swap it.',
     'A multimeter set to DC volts with its red probe touching the panel lead marked plus and its black probe on the minus lead. One display shows a plain number labelled correct; a second display shows the same number with a minus sign, labelled reversed, swap it before anything is plugged in.',
     ['09-03', '09-12', '09-16'])
def mc4_check():
    b = []

    def mc4(x, y, sign):
        col = RED if sign == '+' else INK
        return (path(f'M{x},{y - 9} L{x + 46},{y - 9} L{x + 54},{y - 4} L{x + 54},{y + 4} L{x + 46},{y + 9} L{x},{y + 9} Z', col, col, 1.6, 0.12) +
                t(x + 24, y + 5, sign, 15, 'middle', 'bold', col))

    b.append(rect(8, 10, 70, 40, INK, INK, 1.6, 3, 0.07) + t(43, 34, 'panel', 11, 'middle'))
    b.append(path('M30,50 C30,80 60,82 120,82', INK, sw=2.2) + mc4(120, 82, '+'))
    b.append(path('M56,50 C56,66 80,124 120,128', INK, sw=2.2) + mc4(120, 128, '−'))
    b.append(tl(184, 74, [('+ lead', True), '(as marked on the', 'panel label or cable)'], 10.5, 12, fill=RED))
    b.append(t(184, 134, '− lead', 10.5, weight='bold'))
    # meter
    mx, my = 222, 150
    b.append(rect(mx, my, 110, 150, INK, INK, 1.8, 10, 0.06))
    b.append(rect(mx + 12, my + 12, 86, 36, INK, 'none', 1.4, 3))
    b.append(t(mx + 55, my + 38, '61.3', 20, 'middle', 'bold'))
    b.append(t(mx + 55, my + 66, 'DC volts (V ⎓)', 10.5, 'middle'))
    b.append(circle(mx + 55, my + 92, 16, INK, 'none', 1.4) + line(mx + 55, my + 92, mx + 66, my + 81, INK, 2))
    b.append(circle(mx + 30, my + 132, 5, INK, INK, 1.2, 0.8) + t(mx + 30, my + 122, 'COM', 9, 'middle'))
    b.append(circle(mx + 80, my + 132, 5, RED, RED, 1.2, 0.8) + t(mx + 80, my + 122, 'V', 9, 'middle', fill=RED))
    # probes
    b.append(path(f'M{mx + 80},{my + 137} C{mx + 80},{my + 170} 196,{my + 30} 178,82', RED, sw=2.2) + circle(176, 82, 3, RED, RED))
    b.append(path(f'M{mx + 30},{my + 137} C{mx + 30},{my + 160} 190,{my + 20} 178,128', INK, sw=2.2) + circle(176, 128, 3, INK, INK))
    b.append(check(14, 168, 14) + tl(34, 180, [('No minus sign:', True), 'polarity correct.'], 12, 15, fill=GREEN))
    # reversed display
    b.append(rect(14, 222, 98, 34, RED, 'none', 1.6, 3) + t(63, 246, '−61.3', 19, 'middle', 'bold', RED))
    b.append(tl(14, 274, [('Minus sign: a connector', True), ('is reversed. Swap it', True), ('before plugging in.', True)], 12, 15, fill=RED))
    b.append(t(8, 334, 'Numbers are an example: read your own string.', 11, italic=True))
    return svg('fig-mc4-polarity-check', 352, '\n'.join(b), 'Checking panel polarity with a multimeter')

from figlib import *
from fig_power import fig as _f
FIGS = {}


def fig(fid, caption, alt, pages):
    def deco(fn):
        FIGS[fid] = dict(fn=fn, caption=caption, alt=alt, pages=pages)
        return fn
    return deco


def _gas_panel(cx, mode):
    b = []
    gy = 236
    b.append(line(cx - 70, gy, cx + 70, gy, INK, 2) + shade(cx - 70, gy, 140, 10, INK, 0.12))
    # meter
    b.append(rect(cx - 6, 56, 64, 48, INK, INK, 1.8, 6, 0.08) + t(cx + 26, 84, 'meter', 11, 'middle'))
    # riser pipe
    b.append(path(f'M{cx},{gy} L{cx},{114} Q{cx},{106} {cx + 8},{104}', INK, sw=9, op=0.25))
    b.append(path(f'M{cx},{gy} L{cx},{114} Q{cx},{106} {cx + 8},{104}', INK, sw=1.4))
    # valve body
    vy = 170
    b.append(rect(cx - 13, vy - 15, 26, 30, INK, INK, 1.8, 4, 0.18))
    col = GREEN if mode == 'on' else RED
    if mode == 'on':
        b.append(rect(cx - 5, vy - 26, 10, 52, col, col, 2, 2, 0.45))
        b.append(circle(cx, vy - 18, 2.5, col, 'none', 1.4))
    else:
        b.append(rect(cx - 30, vy - 5, 60, 10, col, col, 2, 2, 0.45))
        b.append(circle(cx - 22, vy, 2.5, col, 'none', 1.4))
        # wrench
        b.append(path(f'M{cx + 34},{vy - 8} l8,-4 l4,8 l-8,4 Z M{cx + 42},{vy - 6} L{cx + 64},{vy + 40}', INK, sw=5, op=0.5))
        b.append(path(f'M{cx + 22},{vy - 34} A30,30 0 0 1 {cx + 34},{vy - 14}', INK, sw=1.6) + arrow(cx + 32, vy - 18, cx + 35, vy - 11, INK, 1.6, 6))
        b.append(t(cx + 26, vy - 38, '¼ turn', 10.5, 'start', 'bold'))
    b.append(t(cx - 18, vy + 46, 'pipe from', 10, 'end') + t(cx - 18, vy + 58, 'the ground', 10, 'end'))
    head = 'ON' if mode == 'on' else 'OFF'
    sub = ['bar IN LINE', 'with the pipe'] if mode == 'on' else ['bar CROSSWISE', 'to the pipe']
    b.append(t(cx, 16, head, 16, 'middle', 'bold', col))
    b.append(tl(cx, 34, sub, 11, 13, 'middle', fill=col, weight='bold'))
    return b


@fig('fig-gas-valve-on-off',
     'Natural gas shutoff at the meter: the valve is on the pipe coming out of the ground, before the meter. Bar in line with the pipe = ON; a quarter turn with a wrench so the bar lies crosswise = OFF. Propane: close the valve under the tank\'s dome, clockwise.',
     'Two drawings of a gas meter on its riser pipe. Left, ON: the flat bar on the valve body points along the pipe. Right, OFF: the bar is turned a quarter turn so it lies across the pipe, with an adjustable wrench on it and a curved arrow. Below, a propane tank with the dome lid open and the valve marked clockwise to close.',
     ['16-12'])
def gas_valve():
    b = []
    b += _gas_panel(90, 'on')
    b += _gas_panel(270, 'off')
    b.append(line(180, 8, 180, 240, INK, 0.8, op=0.4))
    y = 266
    b.append(tl(8, y, [('Natural gas: the valve on the pipe coming out of', True), ('the ground, BEFORE the meter. 12-inch adjustable', True),
                       ('or gas wrench. Hang the wrench at the meter.', True)], 12, 15))
    # propane tank inset
    y2 = y + 60
    b.append(path(f'M40,{y2 + 90} L40,{y2 + 40} Q40,{y2 + 16} 70,{y2 + 16} L190,{y2 + 16} Q220,{y2 + 16} 220,{y2 + 40} L220,{y2 + 90} Z', INK, INK, 1.8, 0.06))
    b.append(path(f'M100,{y2 + 16} Q130,{y2 - 6} 160,{y2 + 16}', INK, sw=1.6, dash='4 3') + t(130, y2 - 2, 'dome lid', 10, 'middle'))
    b.append(circle(130, y2 + 30, 9, INK, INK, 1.6, 0.2) + path(f'M118,{y2 + 46} A14,14 0 0 0 142,{y2 + 46}', RED, sw=1.8) +
             arrow(139, y2 + 49, 143, y2 + 44, RED, 1.6, 6))
    b.append(t(130, y2 + 74, 'PROPANE TANK', 11, 'middle', 'bold'))
    b.append(tl(232, y2 + 28, [('Propane: close', True), ('the valve under', True), ('the dome,', True), ('clockwise', True), '("righty tighty").'], 11.5, 14, fill=RED))
    b.append(tl(8, y2 + 116, ['Do not turn gas back on yourself while the utility', 'exists: only the utility restores service and relights pilots.'], 11, 14))
    return svg('fig-gas-valve-on-off', y2 + 150, '\n'.join(b), 'Gas shutoff valve on and off')


@fig('fig-water-heater-valves',
     'Getting water out of a tank water heater: heat off (gas control to OFF, or the breaker off), close the cold-water inlet valve on top, open a hot tap higher in the house, then open the drain valve at the base slowly into a hose or bucket. The water can be scalding.',
     'A tank water heater seen from the front. On top, the cold-water inlet pipe with its valve, marked close, and the hot outlet pipe. Low on the front, the gas control knob marked OFF, not pilot, or for an electric heater the breaker off. At the base, the drain valve with a hose running to a bucket, marked open slowly, scalding. A note shows a hot tap upstairs left open to let air in. Numbers 1 to 4 follow the draining steps.',
     ['03-02', '08-03'])
def water_heater():
    b = []
    tx, ty, tw, th = 150, 70, 80, 220
    b.append(rect(tx, ty, tw, th, INK, INK, 2, 14, 0.06))
    b.append(t(tx + tw / 2, ty + 100, 'TANK', 13, 'middle', 'bold'))
    # pipes on top
    b.append(line(tx + 22, ty, tx + 22, 20, BLUE, 8, op=0.5) + line(tx + 58, ty, tx + 58, 20, RED, 8, op=0.5))
    b.append(t(tx + 18, 14, 'cold in', 10.5, 'end', 'bold', BLUE) + t(tx + 62, 14, 'hot out', 10.5, 'start', 'bold', RED))
    b.append(rect(tx + 14, 36, 16, 14, INK, INK, 1.6, 2, 0.3) + line(tx + 6, 43, tx + 38, 43, INK, 3.4))
    b.append(circle(18, 52, 10, INK, INK, 1.6, 0.12) + t(18, 56, '2', 12, 'middle', 'bold'))
    b.append(tl(34, 48, [('Close the cold', True), ('inlet valve', True)], 11, 13) + line(124, 46, tx + 4, 44, INK, 1, '2 2'))
    # gas control
    b.append(rect(tx + 19, ty + 150, 42, 26, INK, INK, 1.6, 3, 0.15) + circle(tx + 40, ty + 163, 8, INK, 'none', 1.6) + line(tx + 40, ty + 163, tx + 40, ty + 155, INK, 2.4))
    b.append(circle(18, ty + 130, 10, INK, INK, 1.6, 0.12) + t(18, ty + 134, '1', 12, 'middle', 'bold'))
    b.append(tl(34, ty + 126, [('Heat OFF', True), 'gas: knob to OFF', '(not pilot);', 'electric: its', 'breaker off'], 11, 13) + line(132, ty + 163, tx + 19, ty + 163, INK, 1, '2 2'))
    # drain valve, hose, bucket
    fy = ty + th
    b.append(line(0, fy + 44, 360, fy + 44, INK, 1.2, op=0.5))
    b.append(rect(tx + tw - 4, fy - 26, 18, 12, INK, INK, 1.6, 2, 0.3))
    b.append(path(f'M{tx + tw + 14},{fy - 20} C{tx + tw + 40},{fy - 20} {tx + tw + 30},{fy + 4} {tx + tw + 40},{fy + 6}', INK, sw=3))
    bx = tx + tw + 26
    b.append(path(f'M{bx},{fy + 2} L{bx + 5},{fy + 42} L{bx + 43},{fy + 42} L{bx + 48},{fy + 2}', INK, sw=1.8) + t(bx + 24, fy + 34, 'bucket', 10, 'middle'))
    b.append(circle(254, ty + 130, 10, INK, INK, 1.6, 0.12) + t(254, ty + 134, '4', 12, 'middle', 'bold'))
    b.append(tl(268, ty + 126, [('Drain valve', True), 'at the base:', 'hose or bucket,', 'open SLOWLY.'], 11, 13))
    b.append(tl(268, ty + 178, [('SCALDING.', True), 'Gloves, long', 'sleeves,', 'children out.'], 11, 13, fill=RED))
    # hot tap upstairs
    b.append(circle(254, 52, 10, INK, INK, 1.6, 0.12) + t(254, 56, '3', 12, 'middle', 'bold'))
    b.append(tl(268, 48, [('Open a hot tap', True), 'higher in the', 'house (lets', 'air in)'], 11, 13))
    b.append(path('M300,108 l0,-6 l20,0 l0,10', INK, sw=2.4) + path('M320,116 q-2,6 0,10 M326,116 q-2,6 0,10', BLUE, sw=1.4))
    y = fy + 68
    b.append(tl(8, y, [('First gallon or two: sediment. Let it settle.', False), ('Heat back on only when the tank is full again:', True),
                       ('inlet open, hot tap running with no air.', True)], 11.5, 14.5))
    return svg('fig-water-heater-valves', y + 58, '\n'.join(b), 'Water heater valves for draining')

YEL = '#e0a800'


@fig('fig-fuel-can-colours',
     'US fuel can colours: red gasoline, yellow diesel, blue kerosene. Propane comes only in pressure cylinders. Trust the label, not the colour: every can is labelled with its fuel.',
     'Three portable fuel cans side by side, red labelled GASOLINE, yellow labelled DIESEL, blue labelled KEROSENE, each with a hand-written label, then a grey propane cylinder and a printed metal camp-fuel can. Below: the label, not the colour.',
     ['06-06', '29-01'])
def fuel_cans():
    b = []

    def can(x, col, name, sub):
        out = path(f'M{x},{150} L{x},{70} L{x + 10},{58} L{x + 44},{58} L{x + 50},{50} L{x + 60},{50} L{x + 60},{150} Z', col, col, 2, 0.28)
        out += path(f'M{x + 50},{50} L{x + 58},{34} L{x + 64},{36}', col, sw=4)
        out += rect(x + 8, 64, 22, 8, col, 'none', 2, 3)
        out += rect(x + 3, 92, 54, 30, INK, INK, 1.2, 2, 0.04) + t(x + 30, 106, name, 8, 'middle', 'bold') + t(x + 30, 117, sub, 8, 'middle', italic=True)
        return out
    b.append(can(8, RED, 'GASOLINE', 'stabilised'))
    b.append(t(38, 170, 'red', 11, 'middle', 'bold', RED))
    b.append(can(78, YEL, 'DIESEL', 'date: ___'))
    b.append(t(108, 170, 'yellow', 11, 'middle', 'bold', YEL))
    b.append(can(148, BLUE, 'KEROSENE', 'K-1 only'))
    b.append(t(178, 170, 'blue', 11, 'middle', 'bold', BLUE))
    # propane cylinder
    b.append(rect(224, 64, 52, 86, INK, INK, 1.8, 18, 0.12) + rect(236, 46, 28, 18, INK, 'none', 1.6, 4) + t(250, 112, 'PROPANE', 8.5, 'middle', 'bold'))
    b.append(t(250, 170, 'cylinder', 11, 'middle'))
    # camp fuel
    b.append(rect(290, 70, 52, 80, INK, INK, 1.6, 3, 0.06) + rect(306, 58, 14, 12, INK, 'none', 1.4, 2) + t(316, 104, 'CAMP', 8.5, 'middle', 'bold') + t(316, 115, 'FUEL', 8.5, 'middle', 'bold'))
    b.append(t(316, 170, 'printed can', 11, 'middle'))
    b.append(rect(8, 188, 344, 50, AMBER, AMBER, 1.6, 6, 0.08))
    b.append(tl(18, 207, [('THE LABEL, NOT THE COLOUR.', True), 'No label: do not pour. Read aloud, smell, then pour.'], 12, 16))
    b.append(t(8, 258, 'Gasoline in a kerosene heater: flare-up, fire or explosion.', 11, weight='bold', fill=RED))
    return svg('fig-fuel-can-colours', 280, '\n'.join(b), 'Fuel can colours and labels')


@fig('fig-three-phases',
     'The binder\'s spine: A, shelter in place at home for as long as home works; the go or no-go decision; B, movement; C, establish at a destination or wherever you end up. You can turn back from B to A, and move again from C.',
     'Three boxes left to right, A shelter in place, B movement, C establish. Between A and B a diamond reads go or no-go. A curved arrow from B back to A is labelled turn back; a curved arrow from C back to B is labelled move again.',
     ['00-01'])
def three_phases():
    b = []
    y = 70

    def box(x, letter, name, sub):
        return (rect(x, y, 84, 70, INK, INK, 2, 8, 0.07) + t(x + 42, y + 28, letter, 22, 'middle', 'bold') +
                t(x + 42, y + 48, name, 11.5, 'middle', 'bold') + t(x + 42, y + 62, sub, 10, 'middle'))
    b.append(box(6, 'A', 'Shelter', 'in place at home'))
    b.append(path(f'M136,{y + 35} l22,-22 l22,22 l-22,22 Z', AMBER, AMBER, 2, 0.2) + t(158, y + 32, 'go /', 9.5, 'middle', 'bold') + t(158, y + 43, 'no-go', 9.5, 'middle', 'bold'))
    b.append(arrow(90, y + 35, 136, y + 35, INK, 2, 8) + arrow(180, y + 35, 196, y + 35, INK, 2, 8))
    b.append(box(196, 'B', 'Movement', 'leave, route, trip'))
    b.append(arrow(280, y + 35, 290, y + 35, INK, 2, 6))
    b.append(rect(290, y, 66, 70, INK, INK, 2, 8, 0.07) + t(323, y + 28, 'C', 22, 'middle', 'bold') + t(323, y + 48, 'Establish', 11, 'middle', 'bold') + t(323, y + 62, 'at destination', 9, 'middle'))
    b.append(path(f'M238,{y} C230,{y - 50} 60,{y - 50} 48,{y - 4}', INK, sw=1.8, dash='5 4') + arrow(50, y - 12, 48, y - 2, INK, 1.8, 7))
    b.append(t(144, y - 46, 'turn back', 11, 'middle', italic=True))
    b.append(path(f'M323,{y + 70} C318,{y + 112} 250,{y + 112} 240,{y + 74}', INK, sw=1.8, dash='5 4') + arrow(241, y + 82, 239, y + 72, INK, 1.8, 7))
    b.append(t(284, y + 114, 'move again', 11, 'middle', italic=True))
    b.append(tl(8, y + 140, ['Checklists for moving between phases: 01-06.'], 11, 14, italic=True))
    return svg('fig-three-phases', y + 160, '\n'.join(b), 'The three phases')


@fig('fig-jar-headspace-and-seal',
     'Canning jar: headspace is the empty space between the food and the lid, set by the recipe. Sealed: the lid is pulled down (concave) and does not flex. Unsealed: fridge and eat now, or reprocess with a new lid. Bulging lid: throw away without tasting.',
     'Left: cross-section of a canning jar with band and flat lid, the food level, and the headspace between food and lid marked as the recipe says. Right, three lids side by side: sealed, dipped in the centre, ticked; unsealed, flexing up and down when pressed, marked fridge and eat now or reprocess; bulging, domed up, crossed out and marked throw away, do not taste.',
     ['04-04', '29-08'])
def jar():
    b = []
    x, y = 20, 40
    b.append(path(f'M{x + 10},{y + 30} L{x + 10},{y + 12} L{x + 90},{y + 12} L{x + 90},{y + 30} C{x + 110},{y + 40} {x + 110},{y + 50} {x + 110},{y + 70} '
                  f'L{x + 110},{y + 200} Q{x + 110},{y + 214} {x + 96},{y + 214} L{x + 4},{y + 214} Q{x - 10},{y + 214} {x - 10},{y + 200} '
                  f'L{x - 10},{y + 70} C{x - 10},{y + 50} {x - 10},{y + 40} {x + 10},{y + 30}', INK, INK, 2, 0.04))
    b.append(rect(x + 4, y + 2, 92, 14, INK, INK, 1.6, 2, 0.25) + t(x + 120, y + 8, 'band', 10.5) + line(x + 100, y + 6, x + 116, y + 4, INK, 1))
    b.append(line(x + 8, y + 12, x + 92, y + 12, AMBER, 3) + t(x + 120, y + 24, 'flat lid', 10.5) + line(x + 96, y + 14, x + 116, y + 20, INK, 1))
    b.append(shade(x - 9, y + 52, 118, 160, GREEN, 0.18) + line(x - 8, y + 52, x + 108, y + 52, GREEN, 1.6))
    b.append(t(x + 50, y + 140, 'food and', 11, 'middle') + t(x + 50, y + 154, 'liquid', 11, 'middle'))
    b.append(arrow(x + 50, y + 34, x + 50, y + 16, RED, 1.4, 5) + arrow(x + 50, y + 34, x + 50, y + 50, RED, 1.4, 5))
    b.append(tl(x + 120, y + 44, [('headspace', True), 'as the recipe', 'says'], 11, 13, fill=RED))
    # lids
    lx = 200
    rows = [('SEALED', 'pulled down,', 'does not flex', GREEN, 'M0,0 Q50,10 100,0', 'ok'),
            ('UNSEALED', 'flexes when', 'pressed: fridge', AMBER, 'M0,0 Q50,-6 100,0', 'mid'),
            ('BULGING', 'throw away,', 'do not taste', RED, 'M0,0 Q50,-22 100,0', 'no')]
    for i, (head, a, c, col, d, mark) in enumerate(rows):
        yy = 52 + i * 78
        b.append(f'<g transform="translate({lx},{yy}) scale(0.62,1)">' + path(d, col, sw=4) + rect(0, 0, 100, 12, INK, INK, 1.4, 2, 0.2) + '</g>')
        b.append(t(lx + 72, yy - 16, head, 11.5, weight='bold', fill=col))
        if mark == 'ok':
            b.append(check(lx + 74, yy - 8, 11))
        elif mark == 'no':
            b.append(xmark(lx + 74, yy - 6, 10))
        b.append(tl(lx + 72 + (0 if mark == 'mid' else 18), yy + 4, [a, c], 10.5, 12.5))
        if mark == 'mid':
            b.append(tl(lx + 72, yy + 29, ['and eat now, or', 'reprocess, new lid'], 10.5, 12.5))
    b.append(tl(8, 290, ['Check seals 12 to 24 hours after canning.', 'Remove bands, wipe, label with contents and date.'], 11.5, 14.5))
    return svg('fig-jar-headspace-and-seal', 330, '\n'.join(b), 'Jar headspace and seal check')


@fig('fig-fallout-decay-7-10',
     'The 7-10 rule (HHS REMM): fallout radiation falls about tenfold for every sevenfold increase in time. 1 hour: the starting level; 7 hours: about 1/10; 2 days: about 1/100; 2 weeks: about 1/1,000.',
     'Four bars on a logarithmic scale. 1 hour after the explosion, a full bar labelled the starting level; 7 hours, a bar one step lower labelled about 1/10; 2 days (49 hours), another step lower, about 1/100; 2 weeks, the lowest, about 1/1,000.',
     ['27-05'])
def fallout():
    b = [t(8, 18, 'Fallout level: each 7 times longer, 10 times less', 11.5, italic=True)]
    data = [('1 hour', 'starting level', 4), ('7 hours', 'about 1/10', 3), ('2 days (49 h)', 'about 1/100', 2), ('2 weeks', 'about 1/1,000', 1)]
    base = 230
    for i, (tm, lab, h) in enumerate(data):
        x = 20 + i * 84
        hh = h * 46
        b.append(rect(x, base - hh, 60, hh, RED, RED, 1.6, 2, 0.12 + 0.08 * h))
        b.append(t(x + 30, base - hh - 8, lab, 10.5, 'middle', 'bold'))
        b.append(t(x + 30, base + 16, tm, 11, 'middle', 'bold'))
    b.append(line(10, base, 350, base, INK, 1.6))
    b.append(tl(8, base + 44, [('The first hours are the most dangerous, and', True), ('they fade fastest.', True), 'Rule of thumb from HHS REMM; your area\'s officials govern.'], 11.5, 14.5))
    return svg('fig-fallout-decay-7-10', base + 98, '\n'.join(b), 'Fallout decay, the 7-10 rule')


@fig('fig-cup-on-lid-still',
     'Cup-on-lid still (CDC): pot half full of filtered water, lid upside down, cup tied to the lid handle so it hangs upright and does not touch the water. Boil 20 minutes; the water in the cup is distilled.',
     'Cutaway of a pot on a flame, half full of water. The lid sits upside down so its handle points into the pot; a cup is tied to the handle and hangs upright above the water. Steam rises, condenses on the lid, runs to the low middle point and drips into the cup.',
     ['03-03'])
def cup_still():
    b = []
    px, py, pw, ph = 70, 70, 220, 150
    b.append(path(f'M{px},{py} L{px},{py + ph} Q{px},{py + ph + 10} {px + 10},{py + ph + 10} L{px + pw - 10},{py + ph + 10} Q{px + pw},{py + ph + 10} {px + pw},{py + ph} L{px + pw},{py}', INK, sw=2.4))
    b.append(shade(px + 2, py + 80, pw - 4, 78, BLUE, 0.25) + t(px + pw / 2, py + 140, 'pot half full of filtered water', 10.5, 'middle'))
    b.append(path(f'M{px - 10},{py - 4} Q{px + pw / 2},{py + 34} {px + pw + 10},{py - 4}', INK, sw=3))
    b.append(t(px - 10, py - 16, 'lid upside down (handle pointing down)', 10.5))
    b.append(rect(px + pw / 2 - 6, py + 15, 12, 10, INK, INK, 1.4, 2, 0.4))
    b.append(line(px + pw / 2, py + 25, px + pw / 2, py + 40, INK, 1.2) + t(px + pw / 2 + 10, py + 38, 'tied', 10))
    b.append(path(f'M{px + pw / 2 - 18},{py + 40} L{px + pw / 2 - 14},{py + 72} L{px + pw / 2 + 14},{py + 72} L{px + pw / 2 + 18},{py + 40}', GREEN, sw=2.2))
    b.append(shade(px + pw / 2 - 15, py + 56, 30, 15, BLUE, 0.4))
    b.append(tl(px + pw / 2 - 24, py + 46, ['cup, upright,', 'not touching', 'the water'], 10.5, 12.5, 'end', fill=GREEN))
    for sx in (px + pw - 70, px + pw - 45, px + pw - 20):
        b.append(path(f'M{sx},{py + 76} q-6,-10 0,-20 q6,-10 0,-20', INK, sw=1.4, op=0.6))
    for dx in (-4, 4):
        b.append(circle(px + pw / 2 + dx, py + 32 + abs(dx) * 2, 2, BLUE, BLUE))
    b.append(flame(px + pw / 2 - 30, py + ph + 40, 1.2) + flame(px + pw / 2, py + ph + 40, 1.2) + flame(px + pw / 2 + 30, py + ph + 40, 1.2))
    b.append(tl(8, py + ph + 70, [('Boil 20 minutes. Let it cool before drinking.', True), 'Removes germs, salt, heavy metals and most chemicals (CDC).'], 11.5, 14.5))
    return svg('fig-cup-on-lid-still', py + ph + 110, '\n'.join(b), 'Cup-on-lid still')


@fig('fig-bucket-toilet',
     'Bucket toilet: two 5-gallon buckets (one in use, one being emptied), a snap-on seat with lid, a bag liner, cover material and a scoop beside it, a separate urine jug, and handwashing right next to it.',
     'Side by side: a 5-gallon bucket with a snap-on toilet seat and lid and a bag liner, labelled in use; a second bucket labelled spare, being emptied and cleaned; a bin of cover material such as sawdust with a scoop; a jug for urine; and a handwashing station with soap.',
     ['13-01'])
def bucket_toilet():
    b = []
    gy = 200

    def bucket(x, label):
        return (path(f'M{x},{gy - 110} L{x + 8},{gy} L{x + 62},{gy} L{x + 70},{gy - 110}', INK, INK, 2, 0.06) +
                path(f'M{x - 2},{gy - 106} q37,-8 74,0', INK, sw=1.2, op=0.5) + t(x + 35, gy + 16, label, 10.5, 'middle', 'bold'))
    b.append(bucket(10, 'IN USE'))
    b.append(rect(2, gy - 124, 86, 12, INK, INK, 1.6, 6, 0.25) + path(f'M6,{gy - 124} L22,{gy - 170} L72,{gy - 170} L84,{gy - 124}', INK, INK, 1.6, 0.1))
    b.append(t(46, gy - 176, 'seat + lid', 10.5, 'middle'))
    b.append(path(f'M14,{gy - 108} q-6,30 4,60', AMBER, sw=2) + t(22, gy - 60, 'bag', 10, fill=AMBER))
    b.append(t(46, gy + 30, '5 gal', 10, 'middle'))
    b.append(bucket(100, 'SPARE'))
    b.append(t(135, gy + 30, 'emptied, cleaned', 10, 'middle'))
    # cover bin
    b.append(rect(186, gy - 70, 70, 70, INK, INK, 1.8, 3, 0.06) + shade(188, gy - 50, 66, 48, AMBER, 0.3))
    b.append(t(221, gy + 16, 'COVER', 10.5, 'middle', 'bold') + t(221, gy + 30, 'sawdust, ash...', 10, 'middle'))
    b.append(path(f'M236,{gy - 58} l22,-36 M228,{gy - 62} q8,10 18,4 l-6,-10 Z', INK, sw=2))
    b.append(t(258, gy - 98, 'scoop', 10))
    # urine jug
    b.append(path(f'M270,{gy} L270,{gy - 54} Q270,{gy - 64} 280,{gy - 66} L280,{gy - 76} L292,{gy - 76} L292,{gy - 66} Q304,{gy - 64} 304,{gy - 54} L304,{gy} Z', YEL, YEL, 1.8, 0.2))
    b.append(t(287, gy + 16, 'URINE', 10.5, 'middle', 'bold') + t(287, gy + 30, 'separate', 10, 'middle'))
    # handwash
    b.append(rect(316, gy - 110, 34, 26, BLUE, BLUE, 1.6, 4, 0.2) + line(333, gy - 84, 333, gy - 70, BLUE, 2) + rect(318, gy - 40, 30, 40, INK, 'none', 1.4, 2))
    b.append(t(333, gy + 16, 'WASH', 10.5, 'middle', 'bold') + t(333, gy + 30, 'soap', 10, 'middle'))
    b.append(line(0, gy, 360, gy, INK, 1.2, op=0.5))
    b.append(tl(8, gy + 60, [('Layer of cover in the bottom first. Cover every deposit', True), ('completely. Keep the lid closed. Wash hands every time.', True),
                             'Never empty into a storm drain, creek, ditch or flowing water.'], 11.5, 14.5))
    return svg('fig-bucket-toilet', gy + 118, '\n'.join(b), 'Bucket toilet setup')


@fig('fig-latrine-setbacks',
     'Latrine siting: downhill of the well and at least 100 ft from it and from any surface water, 50 ft or more from the house, never in a drainage path or floodplain; at least 5 ft of dry soil under the bottom of the pit.',
     'Top, plan view on a slope with an arrow pointing downhill. The well is uphill; the house is between; the latrine is downhill, at least 100 ft from the well and at least 100 ft from a creek, and 50 ft or more from the house. Bottom, side view of the pit with at least 5 ft of dry soil between its bottom and the water table.',
     ['13-07'])
def latrine():
    b = [t(8, 16, 'Seen from above', 11.5, italic=True)]
    b.append(arrow(330, 30, 330, 230, INK, 2, 10) + tl(322, 120, ['down', 'hill'], 10.5, 13, 'end', italic=True))
    b.append(circle(70, 50, 14, BLUE, BLUE, 2, 0.2) + t(70, 55, 'well', 10, 'middle', 'bold', BLUE) + t(70, 78, 'UPHILL', 10, 'middle', 'bold', BLUE))
    b.append(rect(170, 60, 70, 46, INK, INK, 1.8, 0, 0.08) + t(205, 88, 'house', 11, 'middle', 'bold'))
    b.append(rect(110, 196, 34, 30, AMBER, AMBER, 2, 3, 0.25) + t(104, 216, 'latrine', 11, 'end', 'bold', AMBER))
    b.append(path('M10,270 C80,262 200,280 300,268', BLUE, sw=6, op=0.5) + t(20, 290, 'creek or any surface water', 10.5, fill=BLUE))
    b.append(line(76, 64, 120, 194, GREEN, 1.6, '5 3') + tl(30, 132, [('100 ft', True), ('or more', True)], 11, 13, fill=GREEN))
    b.append(line(140, 196, 192, 108, GREEN, 1.6, '5 3') + tl(176, 156, [('50 ft', True), ('or more', True)], 11, 13, fill=GREEN))
    b.append(line(127, 228, 140, 266, GREEN, 1.6, '5 3') + t(150, 254, '100 ft or more', 11, weight='bold', fill=GREEN))
    # side view
    y0 = 316
    b.append(t(8, y0, 'Side view of the pit', 11.5, italic=True))
    gy = y0 + 20
    b.append(line(0, gy, 360, gy, INK, 2) + shade(0, gy, 360, 120, AMBER, 0.08))
    b.append(rect(130, gy, 60, 50, INK, INK, 1.8, 0, 0.12) + t(160, gy + 30, 'pit', 11, 'middle'))
    wt = gy + 110
    b.append(path(f'M0,{wt} q30,-4 60,0 t60,0 t60,0 t60,0 t60,0 t60,0', BLUE, sw=2.4) + shade(0, wt, 360, 18, BLUE, 0.25))
    b.append(t(8, wt + 14, 'water table', 10.5, fill=BLUE))
    b.append(arrow(220, gy + 80, 220, gy + 52, GREEN, 1.6, 6) + arrow(220, gy + 80, 220, wt - 2, GREEN, 1.6, 6))
    b.append(tl(230, gy + 74, [('at least 5 ft', True), ('of dry soil', True)], 11, 13, fill=GREEN))
    b.append(tl(8, wt + 44, ['Dig a test hole and wait a day: water or soggy soil = wrong site.', 'Sandy soil or cracked rock: increase every distance a lot.'], 11, 14))
    return svg('fig-latrine-setbacks', wt + 86, '\n'.join(b), 'Latrine setback distances')


@fig('fig-cal-hypo-two-step',
     'Pool shock (calcium hypochlorite), the EPA two-step method: 1, one heaping teaspoon (about 1/4 oz) of granules into 2 gallons of water makes the stock, labelled DO NOT DRINK; 2, one part stock to 100 parts water (1 pint per 12.5 gallons), stir, wait 30 minutes, expect a slight chlorine smell.',
     'Step 1: a heaping teaspoon of granules going into a 2-gallon bucket of water, the bucket labelled CHLORINE STOCK: DO NOT DRINK. Step 2: a pint of stock poured into 12.5 gallons of water, with the equivalents per gallon and per 5 gallons, a 30-minute clock, and a check for a slight chlorine smell. A label panel shows 65 to 73 percent calcium hypochlorite with no algaecides, clarifiers or stabilizers.',
     ['03-04'])
def cal_hypo():
    b = []
    b.append(t(8, 18, '1. MAKE THE STOCK', 13, weight='bold'))
    b.append(path('M60,40 l30,0 l-4,10 l-22,0 Z', INK, INK, 1.6, 0.2) + line(90, 44, 120, 38, INK, 2.4))
    for dx, dy in ((70, 58), (76, 66), (68, 72), (80, 76)):
        b.append(circle(dx, dy, 1.6, INK, INK))
    b.append(tl(130, 44, [('1 heaping teaspoon', True), '(about 1/4 oz) granules'], 11, 13))
    b.append(path('M40,90 L48,190 L132,190 L140,90 Z', BLUE, BLUE, 2, 0.15))
    b.append(t(90, 210, '2 gallons of water', 11, 'middle', 'bold'))
    b.append(rect(46, 120, 88, 40, RED, RED, 1.6, 3, 0.12) + tl(90, 135, [('CHLORINE STOCK', True), ('DO NOT DRINK', True)], 8, 11, 'middle', fill=RED))
    b.append(tl(160, 100, ['Granules INTO water,', 'never water onto', 'granules. Plastic or', 'glass, never metal.', 'Fresh air, eye', 'protection. Mix fresh;', 'do not store it.'], 10.5, 13))
    b.append(line(4, 230, 356, 230, INK, 0.8, op=0.4))
    y = 252
    b.append(t(8, y, '2. TREAT THE WATER: 1 part stock to 100 parts', 13, weight='bold'))
    b.append(path(f'M30,{y + 20} L34,{y + 60} L62,{y + 60} L66,{y + 20} Z', RED, RED, 1.6, 0.15) + t(48, y + 76, '1 pint', 10.5, 'middle', 'bold'))
    b.append(arrow(72, y + 40, 110, y + 40, INK, 2, 8))
    b.append(path(f'M116,{y + 14} L124,{y + 92} L206,{y + 92} L214,{y + 14} Z', BLUE, BLUE, 2, 0.15) + t(165, y + 108, '12.5 gallons', 10.5, 'middle', 'bold'))
    b.append(tl(228, y + 26, ['= 1.3 fl oz', '(2½ Tbsp)', 'per gallon', '= 6.4 oz per', '5 gallons'], 10.5, 13))
    b.append(circle(30, y + 136, 14, INK, 'none', 1.6) + line(30, y + 136, 30, y + 126, INK, 1.8) + line(30, y + 136, 38, y + 136, INK, 1.8))
    b.append(tl(54, y + 132, [('Stir, wait 30 minutes.', True), 'Slight chlorine smell = done. No smell: add', 'more and wait again.'], 11, 13.5))
    y2 = y + 180
    b.append(rect(8, y2, 344, 50, AMBER, AMBER, 1.6, 5, 0.08))
    b.append(tl(16, y2 + 18, [('LABEL: 65 to 73% calcium hypochlorite, with NO', True), ('algaecides, clarifiers or stabilizers.', True), "Never dry granules in drinking water; never dosed like bleach drops."], 10.5, 13))
    return svg('fig-cal-hypo-two-step', y2 + 78, '\n'.join(b), 'Pool shock two-step method')

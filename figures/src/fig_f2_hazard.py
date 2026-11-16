"""F2: hazards, power, vehicle and fire-safety diagrams (new ids only)."""
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


def car(x, gy, w=90, color=INK, op=0.12):
    h = w * 0.38
    b = path(f'M{x},{gy - 10} L{x},{gy - h * 0.55} L{x + w * 0.2},{gy - h} L{x + w * 0.72},{gy - h} L{x + w * 0.88},{gy - h * 0.55} L{x + w},{gy - h * 0.5} L{x + w},{gy - 10} Z', color, color, 1.6, op)
    b += circle(x + w * 0.22, gy - 8, w * 0.1, color, 'white', 1.6) + circle(x + w * 0.8, gy - 8, w * 0.1, color, 'white', 1.6)
    return b


@fig('fig-flood-water-depths',
     'Turn Around, Don\'t Drown (NWS): moving water 6 inches deep knocks an adult off their feet; 12 inches carries away most cars; 2 feet carries away SUVs and trucks. No depth of flowing water across a road is safe to drive, and the road under it may be gone.',
     'Three panels side by side, each with moving water shown by arrows. 6 inches: water at an adult\'s ankles and shins, the person falling. 12 inches: a car floating off the road. 2 feet: an SUV or pickup being carried away. Below: the road under the water may be gone; never drive or walk into moving water.',
     ['17-03', '17-11'])
def flood_depths():
    b = []
    gy = 190
    panels = [('6 in', 'knocks an adult', 'off their feet', 20), ('12 in', 'carries away', 'most cars', 40), ('2 ft', 'carries away', 'SUVs and trucks', 80)]
    for i, (d, a, c, wd) in enumerate(panels):
        x = 4 + i * 119
        b.append(t(x + 56, 22, d, 18, 'middle', 'bold', BLUE))
        b.append(line(x, gy, x + 112, gy, INK, 2))
        if i == 0:
            b.append(figure_g([('c', (x + 66, gy - 104), 10), ('l', [(x + 62, gy - 90), (x + 50, gy - 44)], 16), ('l', [(x + 50, gy - 44), (x + 40, gy - 2)], 10), ('l', [(x + 50, gy - 44), (x + 70, gy - 8)], 10),
                               ('l', [(x + 60, gy - 82), (x + 84, gy - 98)], 7)], INK, 0.32))
        elif i == 1:
            b.append(f'<g transform="rotate(-6 {x + 56} {gy - 40})">' + car(x + 12, gy - 26, 88) + '</g>')
        else:
            b.append(f'<g transform="rotate(-10 {x + 56} {gy - 50})">' + car(x + 6, gy - 46, 100) + '</g>')
        b.append(shade(x, gy - wd, 112, wd, BLUE, 0.3))
        for k in range(2):
            b.append(arrow(x + 14 + k * 44, gy - wd / 2, x + 46 + k * 44, gy - wd / 2, BLUE, 1.6, 6))
        b.append(t(x + 56, gy + 20, a, 11, 'middle', 'bold') + t(x + 56, gy + 34, c, 11, 'middle', 'bold'))
    y = gy + 64
    b.append(box(4, y - 16, 352, 70))
    b.append(tl(12, y, [('Never drive or walk into moving water.', True), 'No depth of flowing water across a road is safe to drive:',
                        'you cannot judge depth or current, and the road under', 'the water may be gone.'], 11, 14.5, fill=RED))
    return svg('fig-flood-water-depths', y + 78, '\n'.join(b), 'Moving water depths that kill')


@fig('fig-defensible-space-zones',
     'Defensible space (USFA, as on 17-05): 0 to 5 feet, nothing that burns (no mulch, dead plants, leaves, needles, firewood or stored items against the walls); 5 to 30 feet, lean, clean and green; woodpiles at least 30 feet from the house; 30 to 100 feet, fuel reduced by thinning, spacing and limbing up. The house: clean gutters, screened vents, nothing under or on decks, propane cylinders moved away.',
     'Plan view of a house in the middle of three rings: 0 to 5 feet shaded grey, gravel or bare soil; 5 to 30 feet with spaced, watered plants; 30 to 100 feet with thinned, spaced trees. A woodpile sits beyond the 30-foot ring. Callouts on the house: clean gutters, screened vents, nothing under the deck, propane moved away.',
     ['17-05'])
def defensible_space():
    b = []
    cx, cy = 180, 190
    b.append(circle(cx, cy, 170, GREEN, GREEN, 1.4, 0.05, '6 4'))
    b.append(circle(cx, cy, 112, GREEN, GREEN, 1.4, 0.08, '6 4'))
    b.append(circle(cx, cy, 58, INK, INK, 1.4, 0.15))
    b.append(rect(cx - 38, cy - 30, 76, 60, INK, 'white', 2.2) + t(cx, cy + 4, 'house', 11, 'middle', 'bold'))
    b.append(t(cx, cy - 44, '0-5 ft: nothing', 9.5, 'middle', 'bold') + t(cx, cy + 50, 'that burns', 9.5, 'middle', 'bold'))
    b.append(t(cx, cy - 92, '5-30 ft: lean, clean, green', 10, 'middle', 'bold', GREEN))
    b.append(t(cx, cy - 136, '30-100 ft: thin, space,', 10, 'middle', 'bold', GREEN) + t(cx, cy - 124, 'limb up trees', 10, 'middle', 'bold', GREEN))
    for (dx, dy) in ((-80, 50), (80, 40), (-70, -60), (60, -70)):
        b.append(circle(cx + dx, cy + dy, 9, GREEN, GREEN, 1.4, 0.35))
    for (dx, dy) in ((-140, 60), (130, 90), (-120, -100), (140, -60), (20, 150), (-150, -10)):
        b.append(circle(cx + dx, cy + dy, 13, GREEN, GREEN, 1.4, 0.3))
    # woodpile beyond 30 ft
    b.append(rect(cx + 118, cy + 18, 30, 16, AMBER, AMBER, 1.4, 2, 0.6) + tl(cx + 112, cy + 48, ['woodpile:', '30 ft +'], 9.5, 11.5, weight='bold'))
    y = cy + 196
    b.append(tl(8, y, [('The house: clean gutters, screened vents, nothing', True), ('under or on decks, propane cylinders moved away.', True),
                       'Your state or county distances: use the larger number.'], 11, 14.5))
    return svg('fig-defensible-space-zones', y + 54, '\n'.join(b), 'Defensible space zones')


@fig('fig-ice-thickness',
     'New clear ice (Minnesota DNR, as on 05-08): under 4 inches, stay off; 4 inches, walking and ice fishing on foot; 5 to 7 inches, snowmobile or small ATV; 7 to 8 inches, side-by-side ATV; 9 to 10 inches, small car or SUV; 11 to 12 inches, medium SUV or small truck; 13 inches, medium truck. White ice is about half as strong: double every figure. No ice is ever "safe" ice.',
     'A stacked bar chart of clear-ice thickness from under 4 inches to 13 inches, each band labelled with the load it carries: stay off; on foot; snowmobile or small ATV; side-by-side ATV; small car or SUV; medium SUV or small truck; medium truck. A note: white ice, double every figure.',
     ['05-08'])
def ice_thickness():
    rows = [('under 4 in', 'STAY OFF', RED), ('4 in', 'walking, ice fishing on foot', BLUE), ('5 to 7 in', 'snowmobile or small ATV', BLUE),
            ('7 to 8 in', 'side-by-side ATV', BLUE), ('9 to 10 in', 'small car or SUV', BLUE), ('11 to 12 in', 'medium SUV or small truck', BLUE),
            ('13 in', 'medium truck', BLUE)]
    b = [t(6, 18, 'NEW CLEAR ICE (Minnesota DNR)', 12.5, weight='bold')]
    y0 = 32
    for i, (th, load, col) in enumerate(rows):
        y = y0 + i * 32
        w = 40 + i * 12
        b.append(rect(6, y, w, 26, col, col, 1.4, 2, 0.2 + i * 0.06))
        b.append(t(14 + w, y + 17, th, 11.5, 'start', 'bold'))
        b.append(t(204, y + 17, load, 11.5, 'start', 'bold' if col == RED else None, col if col == RED else INK))
    y = y0 + 7 * 32 + 22
    b.append(box(4, y - 16, 352, 50, AMBER, 0.12))
    b.append(tl(12, y + 2, [('White ice (snow melted and refrozen on top):', True), ('about half as strong. DOUBLE every figure.', True)], 11.5, 15))
    b.append(tl(8, y + 58, [('No ice is ever "safe" ice.', True), 'Check with a spud bar or auger again and again as you go.'], 11.5, 15))
    return svg('fig-ice-thickness', y + 104, '\n'.join(b), 'Ice thickness and loads')


def extinguisher(x, y, s=1.0):
    S = lambda v: round(v * s, 1)
    b = rect(x, y, S(28), S(70), RED, RED, 1.8, S(8), 0.35)
    b += rect(x + S(6), y - S(10), S(16), S(10), INK, INK, 1.4, 2, 0.4)
    b += path(f'M{x + S(22)},{y - S(8)} l{S(16)},{S(-6)}', INK, sw=2.4)
    return b


@fig('fig-extinguisher-pass',
     'Using an extinguisher, PASS (USFA, as on 29-12): Pull the pin, nozzle pointing away from you; Aim low, at the base of the fire; Squeeze the lever slowly and evenly; Sweep side to side across the base until it is out. Only with your back to a clear exit. Label "1A:10B:C": 1A matches 1.25 gallons of water on a class A fire; 10B covers a liquid fire of about 10 square feet; C is for plugged-in electrical equipment.',
     'Four panels: P, a hand pulling the pin from the handle; A, the hose aimed low at the base of the flames; S, a hand squeezing the lever; S, the hose sweeping side to side across the base of the fire. Below, a sample label reading 1A:10B:C with each part explained, and a note: back to a clear exit; if it is not out when the extinguisher is empty, leave.',
     ['29-12'])
def extinguisher_pass():
    b = []
    titles = [('P', 'Pull pin'), ('A', 'Aim LOW'), ('S', 'Squeeze'), ('S', 'Sweep')]
    for i, (L, s) in enumerate(titles):
        x = 4 + i * 89
        b.append(rect(x, 6, 85, 150, INK, 'none', 1.2, 6, op=0.6))
        b.append(t(x + 10, 34, L, 24, weight='bold', fill=RED) + t(x + 30, 30, s, 10.5, weight='bold'))
    # P
    b.append(extinguisher(30, 70) + circle(52, 56, 6, AMBER, 'none', 2.4) + arrow(56, 54, 78, 46, INK, 1.6, 6))
    b.append(t(46, 150, 'nozzle away', 9.5, 'middle'))
    # A
    x = 93
    b.append(extinguisher(x + 8, 70) + path(f'M{x + 34},{64} Q{x + 60},{60} {x + 62},{120}', INK, sw=2.4))
    b.append(flame(x + 72, 148, 1.2) + arrow(x + 62, 120, x + 70, 138, RED, 1.6, 6) + t(x + 44, 150, 'base of the fire', 9, 'middle'))
    # S squeeze
    x = 182
    b.append(extinguisher(x + 26, 74) + path(f'M{x + 26},{58} l30,0', INK, sw=3) + path(f'M{x + 26},{66} l30,-4', INK, sw=3))
    b.append(arrow(x + 50, 44, x + 50, 58, RED, 1.6, 6) + t(x + 42, 150, 'slowly, evenly', 9.5, 'middle'))
    # S sweep
    x = 271
    b.append(flame(x + 20, 140, 1.0) + flame(x + 42, 140, 1.2) + flame(x + 64, 140, 1.0))
    b.append(path(f'M{x + 12},{110} Q{x + 42},{126} {x + 72},{110}', RED, sw=1.8) + arrow(x + 66, 113, x + 74, 109, RED, 1.8, 6) + arrow(x + 18, 113, x + 10, 109, RED, 1.8, 6))
    b.append(t(x + 42, 76, 'side to side', 9.5, 'middle') + t(x + 42, 88, 'across the base', 9.5, 'middle'))
    # label
    y = 178
    b.append(rect(6, y, 140, 34, INK, 'white', 1.6, 3) + t(76, y + 23, '1A:10B:C', 16, 'middle', 'bold'))
    b.append(tl(156, y + 4, [('1A', True), ('10B', True), ('C', True)], 10.5, 15, fill=RED))
    b.append(tl(186, y + 4, ['= 1.25 gal of water, class A', '= liquid fire about 10 sq ft', '= plugged-in electrical'], 10.5, 15))
    y2 = y + 66
    b.append(box(4, y2 - 16, 352, 52))
    b.append(tl(12, y2 + 2, [('Only with your back to a clear exit.', True), 'Not out when it is empty: leave. Watch for re-lighting.'], 11, 15, fill=RED))
    return svg('fig-extinguisher-pass', y2 + 60, '\n'.join(b), 'PASS: using a fire extinguisher')


@fig('fig-watts-and-watt-hours',
     'The four words as water in a hose (29-02): volts are pressure, amps are how much water flows, watts are pressure × flow (watts = volts × amps), and watt-hours are the water in the bucket (watt-hours = watts × hours). A 1,000 Wh battery runs a 100 W load for roughly 10 hours, less losses.',
     'A tap feeds a hose that fills a bucket. Labels: volts, the pressure pushing; amps, how much water flows; watts, pressure times flow, how fast it is being used; watt-hours, the water collected in the bucket. Below, a worked example: 1,000 watt-hours divided by 100 watts is about 10 hours, less losses.',
     ['29-02'])
def watts():
    b = []
    b.append(rect(10, 30, 40, 60, INK, INK, 1.8, 4, 0.12) + t(30, 104, 'tap', 10, 'middle'))
    b.append(path('M50,60 C110,60 120,130 190,130 L250,130', BLUE, sw=12, op=0.35))
    for x in (100, 160, 210):
        b.append(arrow(x - 16, 60 + (x - 100) * 0.7 if x < 190 else 130, x, 60 + (x - 100) * 0.7 if x < 190 else 130, BLUE, 1.4, 5))
    b.append(path('M250,130 q16,0 16,24', BLUE, sw=6, op=0.5))
    b.append(path('M236,170 L246,250 L310,250 L320,170 Z', INK, BLUE, 2, 0.08) + shade(240, 206, 76, 44, BLUE, 0.35))
    labels = [(56, 24, 'VOLTS (V)', '= pressure: how hard it pushes'), (130, 166, 'AMPS (A)', '= how much is flowing'),
              (10, 210, 'WATTS (W) = V × A', '= how fast it is used'), (196, 280, 'WATT-HOURS (Wh)', '= water in the bucket')]
    for x, y, a, c in labels:
        b.append(t(x, y, a, 12, weight='bold', fill=AMBER) + t(x, y + 14, c, 10.5))
    y = 330
    b.append(rule(y - 18))
    b.append(tl(8, y, [('1,000 Wh ÷ 100 W ≈ 10 hours', True), 'less the losses. Watt-hours = watts × hours.',
                       'Amp-hours × volts = watt-hours: 100 Ah at 12 V = 1,200 Wh.'], 11.5, 15))
    return svg('fig-watts-and-watt-hours', y + 58, '\n'.join(b), 'Volts, amps, watts and watt-hours')


@fig('fig-lug-star-pattern',
     'Lug nuts go on in a star pattern, across the wheel, not round the circle (16-10): hand-tight in a star, lower the vehicle, tighten firmly in the star, then torque to the owner\'s manual at the first chance and recheck after a short drive.',
     'Two wheels seen face-on. A five-lug wheel with the nuts numbered 1 to 5 in a star order, each number across from the last, joined by a star-shaped line. A six-lug wheel numbered 1 to 6 in a criss-cross order, each nut followed by the one opposite.',
     ['16-10'])
def lug_star():
    b = []

    def wheel(cx, cy, n, order):
        out = circle(cx, cy, 70, INK, INK, 2.2, 0.08) + circle(cx, cy, 18, INK, INK, 1.6, 0.2)
        pts = []
        for k in range(n):
            a = -math.pi / 2 + k * 2 * math.pi / n
            pts.append((round(cx + 44 * math.cos(a), 1), round(cy + 44 * math.sin(a), 1)))
        seq = [pts[i] for i in order]
        out += poly(seq + [seq[0]], AMBER, sw=1.8)
        for num, i in enumerate(order, 1):
            x, y = pts[i]
            out += circle(x, y, 11, INK, 'white', 1.8) + t(x, y + 4.5, str(num), 12, 'middle', 'bold')
        return out
    b.append(t(90, 22, '5 lugs', 13, 'middle', 'bold') + wheel(90, 112, 5, [0, 2, 4, 1, 3]))
    b.append(t(270, 22, '6 lugs', 13, 'middle', 'bold') + wheel(270, 112, 6, [0, 3, 1, 4, 2, 5]))
    y = 210
    b.append(tl(8, y, [('Across the wheel, not round the circle.', True), '1. Hand-tight in the star.  2. Lower the vehicle.',
                       '3. Tighten firmly in the star.  4. Torque from the manual', 'at the first chance; recheck after a short drive.'], 11.5, 15))
    return svg('fig-lug-star-pattern', y + 70, '\n'.join(b), 'Lug nut star pattern')


@fig('fig-four-pin-connector',
     'Trailer lights (16-11): in a common 4-pin plug, the white wire and the light housings\' mounting screws carry the return (ground) path; a bad ground causes most trailer light faults. Unbolt the white wire where it meets the frame, wire-brush the frame and terminal to bright metal, bolt it back tight. Pack both plug halves with dielectric grease.',
     'A flat 4-pin trailer plug with four wires leaving it; the white wire is highlighted and runs to a ring terminal bolted to the trailer frame, where a wire brush cleans the metal bright. The other three wires run to the lights. Labels: white wire, ground; bolt to bright metal; dielectric grease in both halves.',
     ['16-11'])
def four_pin():
    b = []
    b.append(rect(14, 40, 60, 90, INK, INK, 2, 6, 0.15) + t(44, 30, '4-pin plug', 10.5, 'middle', 'bold'))
    cols = ['white', INK, INK, INK]
    for k in range(4):
        y = 56 + k * 20
        b.append(circle(44, y, 6, INK, 'white' if k == 0 else INK, 1.6, None if k == 0 else 0.4))
        if k == 0:
            b.append(path(f'M74,{y} C120,{y} 120,200 170,200', INK, sw=5) + path(f'M74,{y} C120,{y} 120,200 170,200', 'white', sw=3))
        else:
            b.append(path(f'M74,{y} L300,{y}', INK, sw=2.4, op=0.5))
    b.append(t(304, 80, 'to the', 10) + t(304, 92, 'lights', 10))
    b.append(t(130, 150, 'WHITE wire: ground', 11, 'start', 'bold'))
    # frame and bolt
    b.append(rect(150, 212, 200, 22, INK, INK, 2, 0, 0.25) + t(330, 250, 'trailer frame', 10, 'end'))
    b.append(circle(176, 204, 8, INK, 'white', 1.8) + circle(176, 204, 3, INK, INK))
    b.append(shade(160, 212, 40, 6, AMBER, 0.8) + tl(196, 186, ['ring terminal bolted', 'to BRIGHT metal'], 10.5, 13, weight='bold', fill=AMBER))
    y = 280
    b.append(tl(8, y, [('Bad ground: dim lights, signals that flash everything,', True), ('lights that work only at an angle.', True),
                       'Wire-brush, bolt back tight; same for each light\'s', 'mounting screws. Dielectric grease in both plug halves', 'at every hitch-up.'], 11, 14.5))
    return svg('fig-four-pin-connector', y + 84, '\n'.join(b), 'Trailer 4-pin plug and ground')


@fig('fig-tornado-vehicle-choices',
     'Tornado while in a vehicle (NWS, SPC, as on 17-02): a sturdy building always wins. If the tornado is far off and roads are open, drive at right angles to its path. Caught by extreme wind or debris: park out of traffic lanes, stay in with the seat belt on, head below the windows, covered. Leave the car only for ground noticeably lower than the road. Never shelter under an overpass.',
     'Four panels. 1: a map view with a tornado track and a car turning to drive away at a right angle to it. 2: a car parked off the lane, the driver belted with head down below the windows, covered by a coat. 3: a person lying flat in a ditch that is noticeably lower than the road, head covered. 4: a car stopped under an overpass, crossed out in red.',
     ['17-02', '17-11'])
def tornado_vehicle():
    b = []
    panels = [('1. Far off: drive at', 'RIGHT ANGLES to its path', GREEN), ('2. Caught: park, belt ON,', 'head below windows, covered', AMBER),
              ('3. Only if noticeably', 'lower than the road', AMBER), ('4. NEVER under', 'an overpass', RED)]
    for i, (a, c, col) in enumerate(panels):
        x = 4 + (i % 2) * 178
        y = 6 + (i // 2) * 172
        b.append(rect(x, y, 174, 164, INK, 'none', 1.2, 6, op=0.6))
        b.append(t(x + 8, y + 18, a, 11, weight='bold', fill=col) + t(x + 8, y + 32, c, 11, weight='bold', fill=col))
    # 1 map: tornado track arrow + car path
    b.append(path('M20,150 L150,60', INK, sw=12, op=0.15) + arrow(30, 143, 150, 60, INK, 1.6, 8) + t(126, 100, 'its path', 9.5))
    b.append(rect(70, 112, 16, 10, BLUE, BLUE, 1.4, 2, 0.6) + arrowpath([(78, 117), (100, 140), (122, 160)], BLUE, 2, 7))
    # 2 car belted
    x = 182
    b.append(car(x + 30, 150, 116))
    b.append(figure_g([('c', (x + 76, 116), 7), ('l', [(x + 80, 124), (x + 96, 138)], 10)], INK, 0.4))
    b.append(path(f'M{x + 64},{108} q14,-8 28,4', AMBER, sw=4) + line(x + 52, 108, x + 132, 108, INK, 1, '3 2'))
    b.append(t(x + 160, 106, 'window line', 8.5, 'end'))
    # 3 ditch
    y3 = 178
    b.append(path(f'M8,{y3 + 92} L60,{y3 + 92} L80,{y3 + 130} L120,{y3 + 130} L140,{y3 + 92} L176,{y3 + 92}', INK, sw=2))
    b.append(figure_g([('c', (88, y3 + 122), 6), ('l', [(96, y3 + 124), (118, y3 + 124)], 9)], INK, 0.4))
    b.append(t(20, y3 + 86, 'road', 9.5) + t(100, y3 + 148, 'flat, head covered', 9.5, 'middle'))
    # 4 overpass
    x = 182
    b.append(rect(x + 10, y3 + 66, 156, 16, INK, INK, 1.6, 0, 0.3) + rect(x + 20, y3 + 82, 12, 60, INK, INK, 1.4, 0, 0.3) + rect(x + 144, y3 + 82, 12, 60, INK, INK, 1.4, 0, 0.3))
    b.append(car(x + 48, y3 + 142, 80) + line(x, y3 + 142, x + 174, y3 + 142, INK, 1.6))
    b.append(cross(x + 40, y3 + 60, 96, 86, RED, 3))
    y = 360
    b.append(tl(8, y, [('A sturdy building always wins: drive to the closest shelter.', True), 'In the open with no vehicle: lowest spot, flat, head covered.'], 11, 14.5))
    return svg('fig-tornado-vehicle-choices', y + 40, '\n'.join(b), 'Tornado: choices in a vehicle')


@fig('fig-tsunami-natural-warnings',
     'Tsunami natural warnings (NWS, as on 17-15): a strong or long earthquake; the ocean suddenly rising like a fast flood or a wall of water, or draining away; a loud roar from the ocean. Any one means go now, to high ground or as far inland as you can. Do not wait for an official warning. The first wave may not be the last or the largest.',
     'Three icons in a row: a shaking ground line labelled strong or long earthquake; a shoreline with the sea drawn rising or draining away; an ear with a roar from the ocean. A large arrow points from all three up a hill to high ground, labelled go now.',
     ['17-15'])
def tsunami():
    b = []
    items = [('Strong or LONG', 'earthquake'), ('Sea rising fast', 'or draining away'), ('Loud roar from', 'the ocean')]
    for i, (a, c) in enumerate(items):
        x = 4 + i * 119
        b.append(rect(x, 6, 113, 140, INK, 'none', 1.2, 6, op=0.6))
        b.append(t(x + 56, 116, a, 11, 'middle', 'bold') + t(x + 56, 130, c, 11, 'middle', 'bold'))
    b.append(path('M14,70 l12,-14 l10,24 l12,-26 l10,28 l12,-24 l10,20 l12,-12 l12,6', INK, sw=2.2) + line(10, 90, 112, 90, INK, 2, '4 3'))
    x = 123
    b.append(path(f'M{x + 6},90 L{x + 50},90 L{x + 106},60', INK, sw=2) + shade(x + 6, 60, 100, 30, BLUE, 0.15))
    b.append(path(f'M{x + 6},74 L{x + 70},74', BLUE, sw=3) + arrow(x + 30, 82, x + 30, 52, BLUE, 1.6, 6) + arrow(x + 70, 64, x + 70, 88, BLUE, 1.6, 6))
    x = 242
    b.append(path(f'M{x + 76},48 q-24,0 -24,26 q0,14 10,20 q6,4 4,12', INK, sw=2.4))
    for k in range(3):
        b.append(path(f'M{x + 12 + k * 10},{60 + k * 2} q-6,10 0,20', BLUE, sw=1.8))
    gy = 260
    b.append(path(f'M0,{gy} L120,{gy} Q240,{gy - 10} 356,{gy - 80} L356,{gy + 10} L0,{gy + 10} Z', INK, GREEN, 1.6, 0.12))
    b.append(shade(0, gy - 6, 120, 16, BLUE, 0.35))
    b.append(arrowpath([(40, gy - 20), (180, gy - 40), (320, gy - 96)], RED, 4, 14))
    b.append(t(130, 172, 'GO NOW: high ground or', 13, 'middle', 'bold', RED) + t(130, 188, 'as far inland as you can', 13, 'middle', 'bold', RED))
    y = gy + 34
    b.append(tl(8, y, [('Any ONE sign: go. Do not wait for an official warning.', True), 'The first wave may not be the last or the largest.'], 11.5, 15))
    return svg('fig-tsunami-natural-warnings', y + 40, '\n'.join(b), 'Tsunami natural warnings')

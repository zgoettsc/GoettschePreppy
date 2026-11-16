from figlib import *
from fig_power import fig as _f
FIGS = {}


def fig(fid, caption, alt, pages):
    def deco(fn):
        FIGS[fid] = dict(fn=fn, caption=caption, alt=alt, pages=pages)
        return fn
    return deco

ROPE = 7  # rope stroke width


def rope(d, col=INK, w=ROPE):
    """A rope drawn as a light core with dark edges, so crossings read."""
    return path(d, col, 'none', w + 2.4) + path(d, '#ffffff', 'none', w - 1.6, op=0.0) + path(d, col, 'none', w, op=0.35)


def wrap(cx, cy, rx=7, ry=13, col=INK):
    """One turn of a cord around a horizontal line: front stroke only."""
    return path(f'M{cx - rx},{cy - ry} C{cx + rx},{cy - ry} {cx + rx},{cy + ry} {cx - rx + 2},{cy + ry}', col, sw=5) + \
        path(f'M{cx - rx},{cy - ry} C{cx + rx},{cy - ry} {cx + rx},{cy + ry} {cx - rx + 2},{cy + ry}', col, sw=2.4, op=0.4)


@fig('fig-knot-parts-of-a-rope',
     'The words used in every knot step: working end, standing part, bight, loop.',
     'One rope drawn across the frame. The short free end on the right is labelled working end; the long rest on the left is labelled standing part. Below, a U-shaped fold with no crossing is labelled bight, and a circle where the rope crosses itself is labelled loop.',
     ['16-03'])
def parts_of_rope():
    b = []
    b.append(path('M10,60 C80,60 160,40 230,52 S320,64 336,60', INK, sw=8, op=0.35) + path('M10,60 C80,60 160,40 230,52 S320,64 336,60', INK, sw=2))
    b.append(t(80, 36, 'standing part', 13, 'middle', 'bold') + t(10, 92, '(the long part, to the load)', 11))
    b.append(t(300, 36, 'working end', 13, 'middle', 'bold') + t(300, 92, '(the end you move)', 11, 'middle'))
    b.append(line(250, 70, 250, 80, INK, 1, '2 2'))
    # bight
    d = 'M20,130 L120,130 C160,130 160,180 120,180 L20,180'
    b.append(path(d, INK, sw=8, op=0.35) + path(d, INK, sw=2))
    b.append(t(70, 210, 'BIGHT', 13, 'middle', 'bold') + t(70, 225, 'a U-fold, no crossing', 11, 'middle'))
    # loop
    d2 = 'M200,190 C230,190 300,180 300,150 C300,120 250,115 245,140 C240,165 280,190 340,190'
    b.append(path(d2, INK, sw=8, op=0.35) + path(d2, INK, sw=2))
    b.append(t(272, 210, 'LOOP', 13, 'middle', 'bold') + t(272, 225, 'the rope crosses itself', 11, 'middle'))
    return svg('fig-knot-parts-of-a-rope', 246, '\n'.join(b), 'Parts of a rope')


@fig('fig-knot-taut-line-hitch',
     'Taut-line hitch on a guy line: around the anchor, then two wraps around the standing part inside the loop, one wrap outside it, tucked. It slides by hand and holds under load.',
     'A stake at the left and a tarp at the right. The line runs from the tarp to the stake, around it and back toward the tarp. The working end makes wraps 1 and 2 around the standing part inside the big loop, then wrap 3 on the tarp side outside the loop, and is tucked under that last wrap. Arrows show the knot sliding along the standing part to tighten.',
     ['16-03'])
def taut_line():
    b = []
    b.append(rect(14, 40, 12, 130, INK, INK, 1.6, 2, 0.25) + t(20, 190, 'stake', 11, 'middle'))
    b.append(path('M336,40 L352,30 L352,160 L336,150 Z', AMBER, AMBER, 1.6, 0.25) + t(344, 180, 'tarp', 11, 'middle'))
    # standing part: tarp to stake (upper)
    sp = 'M336,80 L36,80 C24,80 22,88 22,92'
    b.append(path(sp, INK, sw=3))
    # back from stake (lower) toward tarp then wraps
    wp = 'M22,92 C22,98 24,108 36,110 L150,110 C170,110 172,100 176,86'
    b.append(path(wp, INK, sw=3))
    b.append(t(100, 72, 'standing part', 11, 'middle'))
    b.append(t(90, 128, 'the big loop', 11, 'middle', italic=True))
    for i, x in enumerate((182, 198)):
        b.append(wrap(x, 80))
        b.append(t(x, 112, str(i + 1), 12, 'middle', 'bold'))
    b.append(path('M204,92 C220,96 222,70 234,68', INK, sw=2.6, dash='3 2'))
    b.append(wrap(240, 80, col=GREEN))
    b.append(t(240, 112, '3', 12, 'middle', 'bold', GREEN))
    b.append(path('M243,93 C252,98 254,104 262,104', GREEN, sw=3))
    b.append(t(270, 108, 'tuck under', 10.5, fill=GREEN) + t(270, 120, 'wrap 3', 10.5, fill=GREEN))
    b.append(tl(140, 150, [('1 and 2: inside the loop,', True), 'turning back toward the stake.', ('3: outside the loop', True), 'on the tarp side, then tuck.'], 11.5, 14))
    b.append(arrow(178, 52, 140, 52, INK, 1.4, 6) + arrow(210, 52, 250, 52, INK, 1.4, 6) + t(194, 46, 'slides', 10.5, 'middle'))
    return svg('fig-knot-taut-line-hitch', 222, '\n'.join(b), 'Taut-line hitch')


@fig('fig-knot-truckers-hitch',
     'Trucker\'s hitch: far end tied off, a pulley loop in the standing part, the working end around the anchor and back up through the loop, pulled tight, locked with two half hitches.',
     'Side view of a load on a trailer bed. The rope is tied to a fixed point on the far side, runs over the load and down toward the anchor hook. About two feet above the anchor a hanging loop is formed in the standing part. The working end goes down around the anchor, back up through the loop, and is pulled down; two half hitches lock it around both strands below the loop.',
     ['16-03'])
def truckers():
    b = []
    b.append(rect(10, 170, 300, 10, INK, INK, 1.6, 2, 0.2) + t(160, 196, 'trailer bed or rail', 11, 'middle'))
    b.append(rect(60, 80, 160, 90, INK, INK, 1.6, 6, 0.08) + t(140, 130, 'LOAD', 13, 'middle', 'bold'))
    b.append(circle(30, 166, 5, INK, INK, 1.6, 0.4) + tl(14, 210, ['1. far end tied off', '(bowline or two half hitches)'], 10.5, 12.5))
    b.append(path('M300,170 q-10,-2 -10,-12 q0,-8 10,-8', INK, sw=3.4) + t(312, 160, 'anchor', 10.5))
    # rope: far end over load to pulley loop
    b.append(path('M30,162 L60,80 L220,80 L262,104', INK, sw=3))
    # pulley loop hanging from standing part at (262,104)
    b.append(path('M262,104 C250,110 250,128 262,132 C274,128 274,110 262,104', GREEN, sw=3))
    b.append(t(208, 118, '2-3. pulley', 10.5, 'end', fill=GREEN) + t(208, 130, 'loop', 10.5, 'end', fill=GREEN))
    # standing continues: from loop region down to anchor? (the standing part ends at loop; working end continues)
    b.append(path('M262,104 C272,100 282,110 282,124', INK, sw=3))
    b.append(path('M282,124 L292,152', INK, sw=3))
    b.append(t(300, 130, '4. around', 10.5) + t(300, 142, 'the anchor', 10.5))
    b.append(path('M298,152 C300,140 270,140 264,130', AMBER, sw=3) + path('M264,130 C258,124 260,114 268,110 L290,60', AMBER, sw=3))
    b.append(arrow(292, 56, 300, 36, AMBER, 2.4, 8))
    b.append(tl(306, 30, ['5-6. up', 'through', 'the loop,', 'pull'], 10.5, 12.5, fill=AMBER))
    b.append(tl(14, 252, [('7. Pinch the tight strands; lock the working end with', True), ('two half hitches around both strands below the loop.', True),
                         'Undo the hitches and the whole thing falls apart at once.'], 11.5, 14.5))
    return svg('fig-knot-truckers-hitch', 310, '\n'.join(b), "Trucker's hitch")


@fig('fig-knot-prusik',
     'Prusik: a closed loop of thinner cord wrapped three times around a thicker rope. It slides when you push the wraps and grips when the loop is pulled. Not for holding a person.',
     'A thick horizontal ridge line. A closed loop of thin cord is passed around it three times, each wrap inside the last, so three neat turns sit side by side; the loop hangs down below with an arrow showing the pull that makes it grip.',
     ['16-03'])
def prusik():
    b = []
    b.append(path('M8,70 L352,70', INK, sw=14, op=0.3) + line(8, 63, 352, 63, INK, 1.6) + line(8, 77, 352, 77, INK, 1.6))
    b.append(t(60, 50, 'thick rope (ridge line)', 11.5, 'middle'))
    for x in (156, 170, 184, 198, 212, 226):
        b.append(path(f'M{x - 5},{56} C{x + 6},{56} {x + 6},{84} {x - 3},{84}', GREEN, sw=4.2))
    b.append(path('M182,84 C170,110 176,140 190,150 C204,140 210,110 200,84', GREEN, sw=4.2))
    b.append(arrow(190, 152, 190, 182, INK, 1.8, 7) + t(198, 178, 'pull: grips', 11.5))
    b.append(t(190, 44, '3 wraps, side by side', 11.5, 'middle', 'bold', GREEN))
    b.append(arrow(240, 100, 290, 100, INK, 1.4, 6) + t(266, 116, 'push the wraps:', 10.5, 'middle') + t(266, 128, 'slides', 10.5, 'middle'))
    b.append(tl(8, 212, [('Thin cord, tied into a closed loop first.', True), 'Not for holding a person.'], 11.5, 14.5))
    return svg('fig-knot-prusik', 248, '\n'.join(b), 'Prusik knot')


@fig('fig-vehicle-recovery-setup',
     'Pulling a stuck vehicle: a rated strap with no metal hooks, attached to rated recovery points or the hitch receiver with a rated shackle, never the hitch ball; a blanket or mat over the middle of the strap; everyone else farther away than the strap is long and out of line with the pull.',
     'Two vehicles nose to tail, seen from the side and from above. A recovery strap runs between them from the receiver of the pulling vehicle, through a shackle, to a rated recovery point on the stuck one; a hitch ball is crossed out. A blanket hangs over the middle of the strap. From above, a shaded no-standing zone covers the line of pull and extends past both vehicles; people stand to the side, farther away than the strap is long.',
     ['16-03'])
def vehicle_recovery():
    b = [t(8, 16, 'Side view', 11.5, italic=True)]
    gy = 110
    b.append(line(0, gy, 360, gy, INK, 1.2, op=0.5))

    def car(x, label):
        return (path(f'M{x},{gy - 14} L{x},{gy - 44} L{x + 20},{gy - 44} L{x + 34},{gy - 64} L{x + 84},{gy - 64} L{x + 96},{gy - 44} L{x + 110},{gy - 40} L{x + 110},{gy - 14} Z', INK, INK, 1.8, 0.07) +
                circle(x + 24, gy - 12, 12, INK, INK, 1.6, 0.2) + circle(x + 88, gy - 12, 12, INK, INK, 1.6, 0.2) + t(x + 55, gy - 26, label, 10.5, 'middle'))
    b.append(car(8, 'pulling'))
    b.append(car(242, 'stuck'))
    b.append(rect(118, gy - 26, 12, 8, INK, INK, 1.4, 1, 0.5) + t(124, gy - 34, 'receiver', 9.5, 'middle'))
    b.append(path(f'M130,{gy - 26} a5,5 0 1 1 0,8', GREEN, sw=2.6) + t(150, gy + 14, 'rated shackle', 10, 'middle', fill=GREEN))
    b.append(path(f'M136,{gy - 22} C170,{gy - 18} 200,{gy - 18} 238,{gy - 22}', GREEN, sw=4))
    b.append(path(f'M164,{gy - 28} q20,-6 40,0 l-4,22 q-16,6 -32,0 Z', AMBER, AMBER, 1.4, 0.35) + t(186, gy - 40, 'blanket on the strap', 10, 'middle', fill=AMBER))
    b.append(rect(236, gy - 26, 6, 10, GREEN, GREEN, 1.4, 1, 0.5))
    b.append(t(214, gy + 14, 'rated point', 10, 'middle', fill=GREEN))
    # crossed hitch ball inset
    b.append(circle(36, gy + 40, 7, RED, RED, 1.6, 0.2) + line(36, gy + 47, 36, gy + 56, RED, 3) + xmark(26, gy + 30, 20, RED, 2.6))
    b.append(tl(54, gy + 40, [('never the hitch ball,', True), 'a bumper or a tie-down'], 10.5, 12.5, fill=RED))
    # plan view zone
    y0 = gy + 80
    b.append(t(8, y0, 'From above', 11.5, italic=True))
    zy = y0 - 4
    b.append(rect(0, zy + 18, 360, 50, RED, RED, 1.2, 0, 0.1, '5 4'))
    b.append(rect(30, zy + 28, 90, 30, INK, INK, 1.6, 4, 0.1) + rect(240, zy + 28, 90, 30, INK, INK, 1.6, 4, 0.1))
    b.append(line(120, zy + 43, 240, zy + 43, GREEN, 4))
    b.append(t(180, zy + 82, 'NO ONE IN LINE WITH THE PULL', 11, 'middle', 'bold', RED))
    for x in (40, 110, 180):
        b.append(circle(x, zy + 128, 5, INK, 'none', 1.8) + line(x, zy + 133, x, zy + 146, INK, 1.8))
    b.append(arrow(320, zy + 96, 320, zy + 118, INK, 1.2, 5) + arrow(320, zy + 96, 320, zy + 68, INK, 1.2, 5))
    b.append(tl(352, zy + 132, ['bystanders: farther', 'away than the strap', 'is long, out of line'], 10.5, 12.5, 'end'))
    y = zy + 186
    b.append(tl(8, y, [('Dig and add traction first. Only a rated strap with no', True), ('metal hooks: never rope, chain or a ratchet strap.', True),
                       "Your strap's own printed instructions govern."], 11.5, 14.5))
    return svg('fig-vehicle-recovery-setup', y + 56, '\n'.join(b), 'Vehicle recovery strap setup')

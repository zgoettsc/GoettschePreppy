"""Small helpers for GoettschePreppy line diagrams.

Every diagram is drawn on a 360-unit-wide viewBox (a phone column), in currentColor with a few
fixed accent colours that read on white and on a dark page. The root <svg> carries color="#1b1b1b"
as a presentation attribute: the binder shows figures on a white card today, and any CSS rule
(for example `figure.fig svg{color:var(--ink)}`) overrides it if the card ever follows the theme.

Ids inside a diagram are prefixed with the figure id, because many diagrams can be inlined into
one HTML file. No external references, no scripts, no URLs.
"""
from html import escape

INK = 'currentColor'
RED = '#c62828'
GREEN = '#2e7d32'
BLUE = '#1e6fc0'
AMBER = '#d97a00'
W = 360
FONT = 'font-family="Helvetica, Arial, sans-serif"'


def esc(s):
    return escape(str(s), quote=True)


def svg(fid, h, body, title, w=W):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
            f'color="#1b1b1b" {FONT} font-size="13" class="gpfig {fid}" aria-label="{esc(title)}">\n'
            f'<title>{esc(title)}</title>\n{body}\n'
            f'<text x="{w - 6}" y="{h - 6}" font-size="10.5" text-anchor="end" fill="{INK}" opacity="0.75">'
            f'Diagram, not to scale</text>\n</svg>\n')


def t(x, y, s, size=13, anchor='start', weight=None, fill=INK, italic=False, extra=''):
    a = f' text-anchor="{anchor}"' if anchor != 'start' else ''
    wgt = f' font-weight="{weight}"' if weight else ''
    it = ' font-style="italic"' if italic else ''
    sz = f' font-size="{size}"' if size != 13 else ''
    return f'<text x="{x}" y="{y}"{sz}{a}{wgt}{it} fill="{fill}"{extra}>{esc(s)}</text>'


def tl(x, y, lines, size=13, lh=None, anchor='start', weight=None, fill=INK, italic=False):
    """Multi-line text. A line given as ('bold text', True) is bold."""
    lh = lh or round(size * 1.25, 1)
    out = []
    for i, ln in enumerate(lines):
        w = weight
        if isinstance(ln, tuple):
            ln, b = ln
            w = 'bold' if b else weight
        out.append(t(x, round(y + i * lh, 1), ln, size, anchor, w, fill, italic))
    return '\n'.join(out)


def line(x1, y1, x2, y2, stroke=INK, w=1.6, dash=None, cap='round', op=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    o = f' opacity="{op}"' if op else ''
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{w}" stroke-linecap="{cap}"{d}{o}/>'


def rect(x, y, w, h, stroke=INK, fill='none', sw=1.6, rx=0, fop=None, dash=None, op=None):
    fo = f' fill-opacity="{fop}"' if fop is not None else ''
    d = f' stroke-dasharray="{dash}"' if dash else ''
    o = f' opacity="{op}"' if op else ''
    r = f' rx="{rx}"' if rx else ''
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}"{r} fill="{fill}"{fo} stroke="{stroke}" stroke-width="{sw}"{d}{o}/>'


def shade(x, y, w, h, fill=INK, op=0.08, rx=0):
    r = f' rx="{rx}"' if rx else ''
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}"{r} fill="{fill}" fill-opacity="{op}" stroke="none"/>'


def circle(cx, cy, r, stroke=INK, fill='none', sw=1.6, fop=None, dash=None):
    fo = f' fill-opacity="{fop}"' if fop is not None else ''
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}"{fo} stroke="{stroke}" stroke-width="{sw}"{d}/>'


def path(d, stroke=INK, fill='none', sw=1.6, fop=None, dash=None, join='round', op=None):
    fo = f' fill-opacity="{fop}"' if fop is not None else ''
    da = f' stroke-dasharray="{dash}"' if dash else ''
    o = f' opacity="{op}"' if op else ''
    return (f'<path d="{d}" fill="{fill}"{fo} stroke="{stroke}" stroke-width="{sw}" '
            f'stroke-linejoin="{join}" stroke-linecap="round"{da}{o}/>')


def poly(pts, stroke=INK, fill='none', sw=1.6, fop=None, closed=False, dash=None):
    d = 'M' + ' L'.join(f'{x},{y}' for x, y in pts) + (' Z' if closed else '')
    return path(d, stroke, fill, sw, fop, dash)


def arrow(x1, y1, x2, y2, color=INK, w=1.8, head=7, dash=None):
    """Straight arrow with a filled head at (x2, y2)."""
    import math
    a = math.atan2(y2 - y1, x2 - x1)
    bx, by = x2 - head * math.cos(a), y2 - head * math.sin(a)
    p1 = (round(bx + head * 0.5 * math.sin(a), 1), round(by - head * 0.5 * math.cos(a), 1))
    p2 = (round(bx - head * 0.5 * math.sin(a), 1), round(by + head * 0.5 * math.cos(a), 1))
    return (line(x1, y1, round(bx, 1), round(by, 1), color, w, dash) +
            f'<path d="M{x2},{y2} L{p1[0]},{p1[1]} L{p2[0]},{p2[1]} Z" fill="{color}" stroke="none"/>')


def arrowpath(pts, color=INK, w=1.8, head=7, dash=None):
    """Polyline arrow, head at the last point."""
    body = poly(pts[:-1] + [pts[-1]], color, 'none', w, dash=dash) if len(pts) > 2 else ''
    (x1, y1), (x2, y2) = pts[-2], pts[-1]
    return body + arrow(x1, y1, x2, y2, color, w, head, dash)


def cross(x, y, w, h, color=RED, sw=4):
    return line(x, y, x + w, y + h, color, sw) + line(x, y + h, x + w, y, color, sw)


def check(x, y, s=14, color=GREEN, sw=3):
    return path(f'M{x},{y + s * 0.55} L{x + s * 0.38},{y + s} L{x + s},{y}', color, 'none', sw)


def xmark(x, y, s=14, color=RED, sw=3):
    return line(x, y, x + s, y + s, color, sw) + line(x, y + s, x + s, y, color, sw)


def badge(x, y, s, color, w=None, size=12, fill_op=0.12):
    """Rounded label box with coloured outline."""
    w = w or (len(s) * size * 0.6 + 14)
    return (rect(x, y, w, size + 9, color, color, 1.4, 4, fill_op) +
            t(x + w / 2, y + size + 2.5, s, size, 'middle', 'bold', color))


def flame(cx, by, s=1.0, color=AMBER):
    return path(f'M{cx},{by} c{-8 * s},{-3 * s} {-9 * s},{-12 * s} {-3 * s},{-20 * s} '
                f'c{0},{6 * s} {4 * s},{6 * s} {4 * s},{2 * s} c{4 * s},{6 * s} {6 * s},{15 * s} {-1 * s},{18 * s} Z',
                color, color, 1.2, 0.35)


def person_stand(x, y, s=1.0, color=INK, sw=2):
    """Simple standing stick person; (x, y) = feet centre."""
    h = 60 * s
    return (circle(x, y - h + 6 * s, 6 * s, color, 'none', sw) +
            line(x, y - h + 12 * s, x, y - h * 0.45, color, sw) +
            line(x, y - h * 0.45, x - 7 * s, y, color, sw) + line(x, y - h * 0.45, x + 7 * s, y, color, sw) +
            line(x, y - h + 18 * s, x - 10 * s, y - h * 0.5, color, sw) +
            line(x, y - h + 18 * s, x + 10 * s, y - h * 0.5, color, sw))


def g(body, transform=None, op=None):
    tr = f' transform="{transform}"' if transform else ''
    o = f' opacity="{op}"' if op else ''
    return f'<g{tr}{o}>{body}</g>'

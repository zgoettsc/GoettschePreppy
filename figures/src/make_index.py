"""Write figures/index.json (A3's format) from the drawn SVGs (meta.json, written by build.py),
the public-domain plates listed below, and the alias ids kept until pages are edited.

Run after build.py:  python3 figures/src/make_index.py
"""
import json, os
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..', '..'))
SVG_CREDIT = 'GoettschePreppy (diagram, not to scale)'

AFH = ('US Air Force, AFH 10-644, Survival Evasion Resistance Escape (SERE) Operations, 27 March 2017, '
       'Figure {fig} (printed page {page}). Photo by SSgt Justin Watters, USAF. Public domain (US Government work).')

# id -> (file, caption, alt, credit, source key, provenance)
PD = {
    'fig-knot-overhand': ('figures/pd/afh-knot-overhand.jpg',
        'Overhand knot: a loop, the working end pushed through from behind, both ends pulled.',
        'Photograph of a red and black rope tied in a single overhand knot on a wooden table.',
        AFH.format(fig='15-25', page=253), 'afh-10-644', 'PDF page 261'),
    'fig-knot-bowline': ('figures/pd/afh-knot-bowline.jpg',
        'Bowline in four steps: the small loop, the working end up through it, around behind the standing part, back down the loop, tightened. The tail finishes inside the big loop.',
        'Four photographs of a rope on a table: 1, a small loop made in the standing part with the working end lying beside it; 2, the working end passed up through the small loop; 3, the end taken around behind the standing part; 4, the finished bowline with a fixed loop.',
        AFH.format(fig='15-31', page=257), 'afh-10-644', 'PDF page 265'),
    'fig-knot-clove-hitch': ('figures/pd/afh-knot-clove-hitch.jpg',
        'Clove hitch. Top row: tied in the hand as two loops laid one over the other and dropped over a post or clip. Bottom row: tied around a pole, two wraps side by side with the crossing pinned between them.',
        'Six photographs. Top: two loops in a rope, the loops overlapped, then dropped over a carabiner and pulled snug. Bottom: a rope wrapped around a green pole, crossed over itself, and tucked under the second wrap to form a clove hitch.',
        AFH.format(fig='15-36', page=261), 'afh-10-644', 'PDF page 269'),
    'fig-knot-round-turn-two-half-hitches': ('figures/pd/afh-knot-round-turn-two-half-hitches.jpg',
        'Round turn and two half hitches: two turns around the pole, then two half hitches around the standing part, slid down against the pole.',
        'Three photographs of a rope tied to a green pole: the round turn, the first half hitch around the standing part, and the finished knot with two half hitches.',
        AFH.format(fig='15-37', page=261), 'afh-10-644', 'PDF page 269'),
    'fig-knot-square-knot': ('figures/pd/afh-knot-square-vs-granny.jpg',
        'Square knot: right over left, then left over right; each rope\'s two strands leave the knot on the same side and it lies flat. Below, crossed out: the granny knot, which slips.',
        'Top: three photographs of a red rope and a blue rope tied into a square knot step by step. Bottom: two photographs of a granny knot, crossed out in red with the words granny knot slips, untie and start again.',
        AFH.format(fig='15-27 and 15-28 (granny knot panels)', page='255') + ' Titles and red cross added by GoettschePreppy.',
        'afh-10-644', 'PDF page 263'),
    'fig-knot-sheet-bend': ('figures/pd/afh-knot-single-sheet-bend.jpg',
        'Sheet bend: a bight in the thicker rope, the thin end up through it, around behind both legs, tucked under itself. Both short ends finish on the same side.',
        'Three photographs: a white thick rope folded into a U with a thinner red rope coming up through it, the red rope wrapped behind the U, and the finished sheet bend.',
        AFH.format(fig='15-29', page=256), 'afh-10-644', 'PDF page 264'),
    'fig-lashing-square': ('figures/pd/afh-lashing-square.jpg',
        'Square lashing: clove hitch on the upright, three or four wraps around the joint, frapping turns between the poles, clove hitch to finish.',
        'Four photographs of a cord lashing a horizontal yellow pole across an upright wooden pole: the starting hitch, the wraps, the frapping turns, and the finished lashing.',
        AFH.format(fig='15-40', page=263), 'afh-10-644', 'PDF page 271'),
    'fig-lashing-diagonal': ('figures/pd/afh-lashing-diagonal.jpg',
        'Diagonal lashing: a clove hitch around both poles where they cross (some guides use a timber hitch), three turns along one diagonal, three along the other, frapping turns, clove hitch to finish.',
        'Three photographs of a cord lashing two crossed poles: the starting hitch and first diagonal wraps, the wraps on the other diagonal, and the finished lashing with frapping turns.',
        AFH.format(fig='15-41', page=264), 'afh-10-644', 'PDF page 272'),
    'fig-wind-chill-chart': ('figures/pd/nws-wind-chill-chart.png',
        'NWS wind chill chart: find the air temperature across the top and the wind speed down the side. Shaded bands show frostbite in 30, 10 and 5 minutes.',
        'The National Weather Service wind chill table, temperatures 40 to minus 45 degrees F across, wind 5 to 60 mph down, with wind chill values in each cell and three shaded frostbite-time bands, plus the wind chill formula.',
        'NOAA National Weather Service, Wind Chill Chart (effective 1 November 2001). Public domain (US Government work).',
        'noaa-national-weather-service-wind-chill-chart-frost-89f6d7', 'NWS chart PDF, logos cropped'),
    'fig-heat-index-chart': ('figures/pd/nws-heat-index-chart.jpg',
        'NWS heat index chart: air temperature across the top, relative humidity down the side. Colours: Caution, Extreme Caution, Danger, Extreme Danger. Full sun can add up to 15 °F.',
        'The National Weather Service heat index table, 80 to 110 degrees F across and 40 to 100 percent relative humidity down, coloured in four bands from Caution to Extreme Danger.',
        'NOAA National Weather Service, Heat Index chart. Public domain (US Government work).',
        'noaa-national-weather-service-heat-index-categories-f3dbb9', 'NWS heat index chart image'),
    'fig-pressure-canner-parts': ('figures/pd/usda-pressure-canner-parts.jpg',
        'Pressure canner parts: weighted gauge or dial gauge, vent port (petcock), safety fuse, gasket, vent/cover lock, jar rack.',
        'Labelled cutaway drawing of a pressure canner holding jars of green beans on a rack, with the weighted gauge, dial gauge, one-piece safety counterweight, vent port, safety fuse, gasket and vent and cover lock called out.',
        'USDA National Institute of Food and Agriculture, Complete Guide to Home Canning (2015 revision), Guide 1: Principles of Home Canning, page 1-19. Public domain (US Government work).',
        'usda-nchfp-usda-complete-guide-to-home-canning-2015-452df1', 'PDF page 19'),
}

# Ids that pages still use but that are merged into another figure (see notes/workers/F1.md).
ALIASES = {
    'fig-generator-distance': 'fig-generator-siting',
    'fig-panel-transfer-switch-interlock': 'fig-backfeed-path',
}


def main():
    meta = json.load(open(os.path.join(HERE, 'meta.json')))
    out = {}
    for fid, m in sorted(meta.items()):
        f = f'figures/svg/{fid}.svg'
        if not os.path.exists(os.path.join(ROOT, f)):
            continue
        out[fid] = {'file': f, 'caption': m['caption'], 'alt': m['alt'], 'credit': SVG_CREDIT, 'source': None}
    for fid, (f, cap, alt, credit, src, where) in PD.items():
        im = Image.open(os.path.join(ROOT, f))
        out[fid] = {'file': f, 'caption': cap, 'alt': alt, 'credit': credit, 'source': src,
                    'licence': 'Public domain (US Government work, 17 U.S.C. 105)', 'provenance': where,
                    'width': im.width, 'height': im.height}
    for a, target in ALIASES.items():
        if target in out:
            out[a] = dict(out[target], alias_of=target)
    out = dict(sorted(out.items()))
    s = json.dumps(out, indent=1, ensure_ascii=False)
    assert 'http' not in s and 'www.' not in s
    open(os.path.join(ROOT, 'figures', 'index.json'), 'w').write(s + '\n')
    print(len(out), 'figures in index.json')


if __name__ == '__main__':
    main()

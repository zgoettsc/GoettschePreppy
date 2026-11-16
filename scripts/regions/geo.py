"""Minimal, dependency-free readers for the formats the region build uses.

- dBASE (.dbf) tables and ESRI polygon shapefiles (.shp), read straight from the zip.
- Albers equal-area conic (forward, GRS80 ellipsoid) for the EPA ecoregion layers.
- Point-in-polygon (even-odd rule over every ring, so holes work).
- ESRI BIL float rasters (the PRISM hardiness-zone grids).
- Great-circle distance.
"""
import io, math, struct, zipfile


def read_dbf(data):
    n = struct.unpack('<I', data[4:8])[0]
    hlen, rlen = struct.unpack('<HH', data[8:12])
    fields, pos = [], 32
    while data[pos] != 0x0D:
        name = data[pos:pos + 11].split(b'\0')[0].decode('latin1')
        ftype = chr(data[pos + 11]); flen = data[pos + 16]
        fields.append((name, ftype, flen)); pos += 32
    rows = []
    for i in range(n):
        off = hlen + i * rlen
        rec = data[off:off + rlen]
        if rec[:1] == b'*':
            rows.append(None); continue
        p, row = 1, {}
        for name, ftype, flen in fields:
            raw = rec[p:p + flen].decode('latin1').strip(); p += flen
            row[name] = raw
        rows.append(row)
    return rows


def read_shp(data):
    """Yield (bbox, rings) per record; rings are lists of (x, y). Polygon and PolygonZ/M only."""
    pos, out = 100, []
    while pos < len(data):
        _, clen = struct.unpack('>ii', data[pos:pos + 8]); pos += 8
        rec = data[pos:pos + clen * 2]; pos += clen * 2
        st = struct.unpack('<i', rec[:4])[0]
        if st == 0:
            out.append(None); continue
        if st not in (5, 15, 25):
            raise ValueError(f'shape type {st} not supported')
        bbox = struct.unpack('<4d', rec[4:36])
        nparts, npts = struct.unpack('<ii', rec[36:44])
        parts = list(struct.unpack(f'<{nparts}i', rec[44:44 + 4 * nparts]))
        p0 = 44 + 4 * nparts
        flat = struct.unpack(f'<{2 * npts}d', rec[p0:p0 + 16 * npts])
        pts = list(zip(flat[0::2], flat[1::2]))
        rings = [pts[parts[i]:(parts[i + 1] if i + 1 < nparts else npts)] for i in range(nparts)]
        out.append((bbox, rings))
    return out


def read_layer(zpath, stem):
    z = zipfile.ZipFile(zpath)
    names = {n.split('/')[-1]: n for n in z.namelist()}
    dbf = read_dbf(z.read(names[stem + '.dbf']))
    shp = read_shp(z.read(names[stem + '.shp']))
    return [(r, s) for r, s in zip(dbf, shp) if r is not None and s is not None]


def in_rings(x, y, rings):
    inside = False
    for ring in rings:
        n = len(ring)
        j = n - 1
        for i in range(n):
            xi, yi = ring[i]; xj, yj = ring[j]
            if (yi > y) != (yj > y) and x < (xj - xi) * (y - yi) / (yj - yi) + xi:
                inside = not inside
            j = i
    return inside


def locate(x, y, layer):
    """Return the attribute row of the first polygon containing (x, y), else None."""
    for row, (bbox, rings) in layer:
        if bbox[0] <= x <= bbox[2] and bbox[1] <= y <= bbox[3] and in_rings(x, y, rings):
            return row
    return None


def nearest_poly(x, y, layer, maxd):
    """Fallback for points just outside every polygon (coast, lake): nearest vertex within maxd."""
    best, bd = None, maxd * maxd
    for row, (bbox, rings) in layer:
        if x < bbox[0] - maxd or x > bbox[2] + maxd or y < bbox[1] - maxd or y > bbox[3] + maxd:
            continue
        for ring in rings:
            for px, py in ring[::4]:
                d = (px - x) ** 2 + (py - y) ** 2
                if d < bd:
                    bd, best = d, row
    return best


class Albers:
    """Albers equal-area conic on GRS80 (Snyder, Map Projections: A Working Manual, eq. 14-3 ff.)."""
    def __init__(self, lat0, lon0, lat1, lat2, a=6378137.0, f=1 / 298.257222101):
        self.a = a; e2 = 2 * f - f * f; self.e = math.sqrt(e2); self.lon0 = math.radians(lon0)
        m = lambda p: math.cos(p) / math.sqrt(1 - e2 * math.sin(p) ** 2)
        def q(p):
            s = math.sin(p); e = self.e
            return (1 - e2) * (s / (1 - e2 * s * s) - (1 / (2 * e)) * math.log((1 - e * s) / (1 + e * s)))
        self.q = q
        p0, p1, p2 = map(math.radians, (lat0, lat1, lat2))
        m1, m2 = m(p1), m(p2); q0, q1, q2 = q(p0), q(p1), q(p2)
        self.n = (m1 * m1 - m2 * m2) / (q2 - q1)
        self.C = m1 * m1 + self.n * q1
        self.rho0 = a * math.sqrt(self.C - self.n * q0) / self.n

    def fwd(self, lon, lat):
        rho = self.a * math.sqrt(self.C - self.n * self.q(math.radians(lat))) / self.n
        th = self.n * (math.radians(lon) - self.lon0)
        return rho * math.sin(th), self.rho0 - rho * math.cos(th)


class BilGrid:
    def __init__(self, zpath, stem):
        z = zipfile.ZipFile(zpath)
        names = {n.split('/')[-1]: n for n in z.namelist()}
        hdr = {}
        for line in z.read(names[stem + '.hdr']).decode().splitlines():
            k, *v = line.split()
            if v: hdr[k] = v[0]
        self.nr, self.nc = int(hdr['NROWS']), int(hdr['NCOLS'])
        self.x0, self.y0 = float(hdr['ULXMAP']), float(hdr['ULYMAP'])
        self.dx, self.dy = float(hdr['XDIM']), float(hdr['YDIM'])
        self.nodata = float(hdr.get('NODATA', -9999))
        self.raw = z.read(names[stem + '.bil'])

    def value(self, lon, lat):
        # ULXMAP/ULYMAP are the centre of the upper-left cell.
        c = round((lon - self.x0) / self.dx); r = round((self.y0 - lat) / self.dy)
        if not (0 <= r < self.nr and 0 <= c < self.nc):
            return None
        v = struct.unpack('<f', self.raw[(r * self.nc + c) * 4:(r * self.nc + c) * 4 + 4])[0]
        return None if v <= self.nodata + 1 else v

    def value_near(self, lon, lat, radius_cells=6):
        v = self.value(lon, lat)
        if v is not None:
            return v
        for k in range(1, radius_cells + 1):
            for dr in range(-k, k + 1):
                for dc in range(-k, k + 1):
                    v = self.value(lon + dc * self.dx, lat + dr * self.dy)
                    if v is not None:
                        return v
        return None


def haversine_km(lat1, lon1, lat2, lon2):
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dp, dl = p2 - p1, math.radians(lon2 - lon1)
    h = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 6371.0 * 2 * math.asin(math.sqrt(h))


class PolyIndex:
    """Vectorised point-in-polygon over a layer (numpy). rows[i] is the attribute row of polygon i."""
    def __init__(self, layer, project=None):
        import numpy as np
        self.np = np
        self.rows, self.bbox, self.edges = [], [], []
        for row, (bbox, rings) in layer:
            xs1, ys1, xs2, ys2 = [], [], [], []
            bx = [math.inf, math.inf, -math.inf, -math.inf]
            for ring in rings:
                pts = [project(*p) for p in ring] if project else ring
                for (a, b), (c, d) in zip(pts, pts[1:] + pts[:1]):
                    xs1.append(a); ys1.append(b); xs2.append(c); ys2.append(d)
                    bx = [min(bx[0], a), min(bx[1], b), max(bx[2], a), max(bx[3], b)]
            self.rows.append(row); self.bbox.append(bx)
            self.edges.append(tuple(np.array(v) for v in (xs1, ys1, xs2, ys2)))
        self.bb = np.array(self.bbox)

    def contains(self, i, x, y):
        np = self.np
        x1, y1, x2, y2 = self.edges[i]
        m = (y1 > y) != (y2 > y)
        if not m.any():
            return False
        with np.errstate(divide='ignore', invalid='ignore'):
            xc = (x2[m] - x1[m]) * (y - y1[m]) / (y2[m] - y1[m]) + x1[m]
        return bool((x < xc).sum() % 2)

    def candidates(self, x, y):
        b = self.bb
        return self.np.nonzero((b[:, 0] <= x) & (x <= b[:, 2]) & (b[:, 1] <= y) & (y <= b[:, 3]))[0]

    def locate(self, x, y):
        for i in self.candidates(x, y):
            if self.contains(i, x, y):
                return i
        return None

    def nearest(self, x, y, maxd):
        """Index of the polygon with the nearest vertex within maxd (for points just off a coast)."""
        np = self.np
        best, bd = None, maxd
        b = self.bb
        near = np.nonzero((b[:, 0] - maxd <= x) & (x <= b[:, 2] + maxd) & (b[:, 1] - maxd <= y) & (y <= b[:, 3] + maxd))[0]
        for i in near:
            x1, y1, _, _ = self.edges[i]
            d = np.sqrt((x1 - x) ** 2 + (y1 - y) ** 2).min()
            if d < bd:
                bd, best = d, i
        return best

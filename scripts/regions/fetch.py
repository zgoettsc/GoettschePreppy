#!/usr/bin/env python3
"""Download every raw dataset the region build needs into build/regions-raw/ (gitignored).

    python3 scripts/regions/fetch.py            # fetch what is missing
    python3 scripts/regions/fetch.py --force    # refetch everything

Uses curl (it honours the HTTPS proxy and CA bundle of the build machine). Every file is cached;
re-running is cheap. The per-county API pulls (NASA POWER, ACIS records, USGS elevation) run
in build steps that cache their own answers under build/regions-raw/api/ because they need the
county list first; see build.py.

URLs live only here, in build.py and in sources/additions/D1.json (decision G8).
"""
import os, subprocess, sys, json, time, urllib.parse

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
RAW = os.path.join(ROOT, 'build', 'regions-raw')

FILES = {
    # Census Bureau, 2024 Gazetteer files (public domain)
    'gaz_counties.zip': 'https://www2.census.gov/geo/docs/maps-data/data/gazetteer/2024_Gazetteer/2024_Gaz_counties_national.zip',
    'gaz_zcta.zip': 'https://www2.census.gov/geo/docs/maps-data/data/gazetteer/2024_Gazetteer/2024_Gaz_zcta_national.zip',
    # NOAA NCEI, U.S. Climate Normals 1991-2020 (public domain)
    'normals_ann.tar.gz': 'https://www.ncei.noaa.gov/data/normals-annualseasonal/1991-2020/archive/us-climate-normals_1991-2020_v1.0.1_annualseasonal_multivariate_by-station_c20230404.tar.gz',
    'normals_mly.tar.gz': 'https://www.ncei.noaa.gov/data/normals-monthly/1991-2020/archive/us-climate-normals_1991-2020_v1.0.1_monthly_multivariate_by-station_c20230404.tar.gz',
    # USDA ARS / Oregon State PRISM, 2023 Plant Hardiness Zone Map (public domain, USDA)
    'phzm_us_grid_2023.zip': 'https://prism.oregonstate.edu/phzm/data/2023/phzm_us_grid_2023.zip',
    'phzm_ak_grid_2023.zip': 'https://prism.oregonstate.edu/phzm/data/2023/phzm_ak_grid_2023.zip',
    'phzm_hi_grid_2023.zip': 'https://prism.oregonstate.edu/phzm/data/2023/phzm_hi_grid_2023.zip',
    'phzm_us_zipcode_2023.csv': 'https://prism.oregonstate.edu/phzm/data/2023/phzm_us_zipcode_2023.csv',
    'phzm_ak_zipcode_2023.csv': 'https://prism.oregonstate.edu/phzm/data/2023/phzm_ak_zipcode_2023.csv',
    'phzm_hi_zipcode_2023.csv': 'https://prism.oregonstate.edu/phzm/data/2023/phzm_hi_zipcode_2023.csv',
    # NOAA NWS, AWIPS counties with county warning area (16 April 2026) and CWA boundaries
    'nws_counties.zip': 'https://www.weather.gov/source/gis/Shapefiles/County/c_16ap26.zip',
    'nws_cwa.zip': 'https://www.weather.gov/source/gis/Shapefiles/WSOM/w_16ap26.zip',
    # NOAA NWS, NOAA Weather Radio county coverage listing (data behind the county coverage pages)
    'nwr_ccl.js': 'https://www.weather.gov/source/nwr/JS/CCL.js',
    'nwr_samecode.txt': 'https://www.weather.gov/source/nwr/SameCode.txt',
    # US EPA, Level III ecoregions (CONUS and Alaska), shapefiles
    'us_eco_l3.zip': 'https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/us/us_eco_l3.zip',
    'ak_eco_l3.zip': 'https://dmap-prod-oms-edc.s3.us-east-1.amazonaws.com/ORD/Ecoregions/ak/ak_eco_l3.zip',
}

# FEMA National Risk Index, counties table. The hazards.fema.gov download now redirects to a page
# that refuses automated clients, so the same table is read from FEMA's public ArcGIS feature
# service (layer NRI_Counties_Prod) in pages of 2000 rows.
NRI_SERVICE = 'https://services.arcgis.com/XG15cJAlne2vxtgt/arcgis/rest/services/National_Risk_Index_Counties/FeatureServer/0/query'
NRI_HAZ = ['AVLN', 'CFLD', 'CWAV', 'DRGT', 'ERQK', 'HAIL', 'HWAV', 'HRCN', 'ISTM', 'LNDS', 'LTNG',
           'IFLD', 'SWND', 'TRND', 'TSUN', 'VLCN', 'WFIR', 'WNTW']


def curl(url, dest, retries=4):
    tmp = dest + '.part'
    for i in range(retries):
        r = subprocess.run(['curl', '-sS', '-L', '--fail', '-m', '900', '-o', tmp, url])
        if r.returncode == 0 and os.path.getsize(tmp) > 0:
            os.replace(tmp, dest)
            return True
        time.sleep(3 * (i + 1))
    print(f'FAILED {url}', file=sys.stderr)
    return False


def fetch_nri(force):
    dest = os.path.join(RAW, 'nri_counties.json')
    if os.path.exists(dest) and not force:
        return
    fields = ['STCOFIPS', 'STATEABBRV', 'COUNTY', 'COUNTYTYPE', 'POPULATION', 'RISK_RATNG', 'NRI_VER']
    for h in NRI_HAZ:
        fields += [f'{h}_RISKR', f'{h}_EALR', f'{h}_HLRR', f'{h}_AFREQ']
    rows, offset = [], 0
    while True:
        q = urllib.parse.urlencode({'where': '1=1', 'outFields': ','.join(fields), 'returnGeometry': 'false',
                                    'orderByFields': 'STCOFIPS', 'resultOffset': offset,
                                    'resultRecordCount': 2000, 'f': 'json'})
        part = os.path.join(RAW, f'nri_page_{offset}.json')
        if not curl(NRI_SERVICE + '?' + q, part):
            sys.exit('NRI fetch failed')
        d = json.load(open(part))
        os.remove(part)
        feats = d.get('features', [])
        rows += [f['attributes'] for f in feats]
        if not d.get('exceededTransferLimit') and len(feats) < 2000:
            break
        offset += len(feats)
    json.dump(rows, open(dest, 'w'))
    print(f'NRI: {len(rows)} counties')


def main():
    force = '--force' in sys.argv
    os.makedirs(RAW, exist_ok=True)
    for name, url in FILES.items():
        dest = os.path.join(RAW, name)
        if os.path.exists(dest) and not force:
            continue
        print('fetch', name)
        curl(url, dest)
    fetch_nri(force)
    missing = [n for n in list(FILES) + ['nri_counties.json'] if not os.path.exists(os.path.join(RAW, n))]
    print('missing:', missing or 'none')


if __name__ == '__main__':
    main()

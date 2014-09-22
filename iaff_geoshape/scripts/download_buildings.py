import requests
import os

building_params = 'http://gis.arlingtonva.us/arlgis/rest/services/public/Buildings/MapServer/0/query?geometry=%27%3E&f=json&spatialRel=esriSpatialRelIntersects&outSR=4326&outFields=*&where=OBJECTID%3E{0}&orderByFields=OBJECTID'
buildings_count = 50000
ROOT = os.path.abspath(os.path.dirname(__file__))

for n, r in enumerate(range(0, buildings_count, 10000)):

    response = requests.get(building_params.format(r))
    open(os.path.normpath(os.path.join(ROOT, '../data/arlington/source/buildings_{0}.geojson'.format(n))), 'w').write(response.content)
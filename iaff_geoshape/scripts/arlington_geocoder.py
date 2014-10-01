import os
from csv import DictReader
import requests
import json

ROOT = os.path.abspath(os.path.dirname(__file__))

path = os.path.normpath(os.path.join(ROOT, '../data/arlington/high_rises/high_rises.csv'))
dr = DictReader(open(path, 'rU'))
url = 'http://gis.arlingtonva.us/arlgis/rest/services/geoproc/Addpnt_loc/GeocodeServer/findAddressCandidates?Street={0}&Single+Line+Input=&outFields=&maxLocations=&outSR=4326&searchExtent=&f=json'

output = {"type": "FeatureCollection", "features": []}

for n, row in enumerate(dr):
    row_data = dict([(k, v) for k, v in row.items() if k])
    row_data['Street'] = row_data.get('ADDRESS')
    row_data['OBJECTID'] = n
    geom = {"type": "Point", "coordinates":[]}
    geocode_address = url.format(row_data.get('Street').replace(' ', '+'))
    response = requests.get(geocode_address)

    if response.status_code == 200:
        address = json.loads(response.content)
        if address['candidates']:
            candidate = address['candidates'][0]
            geom['coordinates'].append(candidate['location']['x'])
            geom['coordinates'].append(candidate['location']['y'])
        else:
            print 'No candidates found for: {0}'.format(row_data.get('Street'))

    output['features'].append({'properties': row_data, 'geometry': geom})

with open(os.path.normpath(os.path.join(ROOT, '../data/arlington/high_rises/high_rises.geojson')), 'wb') as f:
    f.write(json.dumps(output))

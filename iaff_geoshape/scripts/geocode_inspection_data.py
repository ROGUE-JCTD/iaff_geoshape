import os
from csv import DictReader
import requests
import json
import psycopg2
ROOT = os.path.abspath(os.path.dirname(__file__))

path = os.path.normpath(os.path.join(ROOT, '../data/arlington/inspections/inspections.csv'))
dr = DictReader(open(path, 'rU'))
url = 'http://gis.arlingtonva.us/arlgis/rest/services/geoproc/Addpnt_loc/GeocodeServer/findAddressCandidates?Street={0}&Single+Line+Input=&outFields=&maxLocations=&outSR=4326&searchExtent=&f=json'

output = {"type": "FeatureCollection", "features": []}

from psycopg2.extras import DictCursor

RECORDS_TO_UPDATE = 40000
PROXY = ''
conn = psycopg2.connect("dbname='geonode_imports' user='tyler' host='localhost' ")
cur = conn.cursor(cursor_factory=DictCursor)


for n, row in enumerate(dr):
    row_data = dict([(k, v) for k, v in row.items() if k])
    address = ' '.join(row_data.get(n) for n in ['AddressNumber', 'Direction', 'Address', 'Suffix'] if row_data.get(n))

    row_data['Street'] = address
    row_data['OBJECTID'] = n
    geocode_address = url.format(row_data.get('Street').replace(' ', '+'))
    response = requests.get(geocode_address)

    sql = 'insert into arlington_inspections (inspection_type, address, subaddress, zip, city, inspection_date, ' \
          'next_inspection_date, inspection_cause, activity_type, region, property_use, occupancy, geom, error) values ' \
          '(\'{inspection_type}\', \'{address}\', \'{subaddress}\', {zip}, \'{city}\', \'{inspection_date}\', \'{next_inspection_date}\', ' \
          '\'{inspection_cause}\', \'{activity_type}\', \'{region}\', \'{property_use}\', \'{occupancy}\', {geom_sql}, {error});'


    vars = dict(inspection_type=row_data.get('InspectionType', 'null'),
             address=row_data.get('Street'),
             subaddress=row_data.get('SubAddress').replace("'", ''),
             zip=row_data.get('Zip').strip() or 'null',
             city=row_data.get('City', 'null'),
             inspection_date=row_data.get('InspectionDate', 'null').strip() or '1/1/1970',
             next_inspection_date=row_data.get('NextInspectionDate', 'null').strip() or '1/1/1970',
             inspection_cause=row_data.get('InspectionCause', 'null'),
             activity_type=row_data.get('ActivityType', 'null'),
             region=row_data.get('Region', 'null'),
             property_use=row_data.get('PropertyUseType', 'null'),
             occupancy=row_data.get('OccupancyType','null'),
             geom_sql='null',
             error=False
             )

    if response.status_code == 200:
        print 'Found candidates found for: {0}'.format(row_data.get('Street'))
        address = json.loads(response.content)
        if address['candidates']:
            candidate = address['candidates'][0]
            row_data['x'] = candidate['location']['x']
            row_data['y'] = candidate['location']['y']
            vars['geom_sql'] = '(SELECT ST_GeomFromText(\'Point({x} {y})\', 4326))'.format(x=row_data.get('x'),
                                                                                           y=row_data.get('y'))

        else:
            print 'No candidates found for: {0}'.format(row_data.get('Street'))
            vars['error'] = True

    output = sql.format(**vars)
    cur.execute(output)
    conn.commit()

del conn

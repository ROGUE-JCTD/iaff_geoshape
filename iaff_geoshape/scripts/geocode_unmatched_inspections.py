import os
from csv import DictReader
import requests
import json
import psycopg2
ROOT = os.path.abspath(os.path.dirname(__file__))

from psycopg2.extras import DictCursor

conn = psycopg2.connect("dbname='geonode_imports' user='tyler' host='localhost' ")
cur = conn.cursor(cursor_factory=DictCursor)
cur.execute('SELECT * from arlington_inspections where geom is null;')
cur2 = conn.cursor()
geocode_url = 'https://maps.googleapis.com/maps/api/geocode/json?address='
for record in cur:
    response = requests.get(geocode_url + record.get('address').replace('+', ' '))
    if response.status_code == 200:
        js = json.loads(response.content)
        if js.get('results'):
            candidate = js.get('results')[0]
            x = candidate['geometry']['location']['lng']
            y = candidate['geometry']['location']['lat']
            geom_sql = '(SELECT ST_GeomFromText(\'Point({x} {y})\', 4326))'.format(x=x,
                                                                                   y=y)
            cur2.execute('UPDATE arlington_inspections set geom={geom_sql} where id={id}'.format(id=record.get('id'),
                                                                                                 geom_sql=geom_sql))
            conn.commit()
        else:
            print 'No candidate found for: {address}'.format(address=record.get('address'))

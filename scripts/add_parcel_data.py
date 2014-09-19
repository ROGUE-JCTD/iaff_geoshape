import psycopg2
import requests
import time
import random
import sys

from BeautifulSoup import BeautifulSoup
from urlparse import urlparse
from psycopg2.extras import DictCursor

RECORDS_TO_UPDATE = 40000
PROXY = ''
conn = psycopg2.connect("dbname='test' user='tyler' host='localhost' ")
cur = conn.cursor(cursor_factory=DictCursor)
cur2 = conn.cursor()
cur.execute('SELECT * FROM parcels where year is NULL and error is NULL')


def get_assessment_url(content):
    c = BeautifulSoup(content)
    return PROXY + c.find(title='CAMA Data').get('href')


def parse_parcel_data(content):
    c = BeautifulSoup(content)
    year = c.find(text='Year Built').parent.parent.text.replace('Year Built', '').replace('N/A', '1000')
    property_class = c.find(text='Property Class Code').parent.parent.text.replace('Property Class Code', '')
    return dict(year=year, property_class=property_class)


def get_parcel_data(rpcmstr):
    url = PROXY + 'http://gis.arlingtonva.us/gis_apps/camadata.asp?rpcmstr={0}'.format(rpcmstr)
    response = requests.get(url)
    assessment_url = get_assessment_url(response.content)
    response = requests.get(assessment_url)
    parcel_data = parse_parcel_data(response.content)
    query = urlparse(assessment_url).query
    parcel_data['lrsn'] = query[query.index('lrsn'):].replace('lrsn=','')
    return parcel_data

n=0
while n < RECORDS_TO_UPDATE:
    try:
        record = cur.fetchone()
        rpcmstr = record.get('rpcmstr')
        if not record:
            break
        data = get_parcel_data(rpcmstr)
        print data
        cur2.execute("update parcels set lrsn=\'{lrsn}\', property_class=\'{property_class}\', "
                     "year={year} where rpcmstr='{rpcmstr}'"
        .format(rpcmstr=rpcmstr, **data))
        conn.commit()
        n += 1
        time.sleep(random.uniform(.00001, .5))
    except:
        print sys.exc_info()
        cur2.execute("update parcels set error={error} where rpcmstr='{rpcmstr}'".format(error=1,
                                                                                         rpcmstr=rpcmstr))
        conn.commit()

import os
from distutils.spawn import find_executable


def query_iterator(count, query, step=10000):
    """
    Returns a list of queries with the object_id incremented by the step value.
    """
    path = lambda obj_id: query.format(obj_id)
    return map(path, range(0, count, step))


ROOT = os.path.abspath(os.path.dirname(__file__))
QUERIES = {
    'fireboxes': 'http://gis.arlingtonva.us/arlgis/rest/services/public/Fireboxes/MapServer/1/query?where=1%3D1&text=&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&relationParam=&outFields=*&returnGeometry=true&maxAllowableOffset=&geometryPrecision=&outSR=4326&returnIdsOnly=false&returnCountOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&gdbVersion=&returnDistinctValues=false&f=json',
    'hydrants': '../source/hydrants.json', #http://gis.arlingtonva.us/arlgis/rest/services/public/Fireboxes/MapServer/0/query?where=1%3D1&text=&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&relationParam=&outFields=*&returnGeometry=true&maxAllowableOffset=&geometryPrecision=&outSR=4326&returnIdsOnly=false&returnCountOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&gdbVersion=&returnDistinctValues=false&f=json
    'buildings': query_iterator(count=50000, query='http://gis.arlingtonva.us/arlgis/rest/services/public/Buildings/MapServer/0/query?geometry=%27%3E&f=json&spatialRel=esriSpatialRelIntersects&outSR=4326&outFields=*&where=OBJECTID%3E{0}&orderByFields=OBJECTID'),
    'buildings_elevation': query_iterator(count=100152, query='http://gis.arlingtonva.us/arlgis/rest/services/public/Buildings/MapServer/1/query?geometry=%27%3E&f=json&spatialRel=esriSpatialRelIntersects&outSR=4326&outFields=*&where=OBJECTID%3E{0}&orderByFields=OBJECTID'),
    'fire_stations': 'http://gis.arlingtonva.us/arlgis/rest/services/public/County_Facility/MapServer/2/query?where=&text=&objectIds=&time=&geometry=%27&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&relationParam=&outFields=*&returnGeometry=true&maxAllowableOffset=&geometryPrecision=&outSR=4326&returnIdsOnly=false&returnCountOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&gdbVersion=&returnDistinctValues=false&f=json',
    'county_boundary': 'http://gis.arlingtonva.us/arlgis/rest/services/public/County_Boundary/MapServer/0/query?where=&text=&objectIds=&time=&geometry=%27&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&relationParam=&outFields=&returnGeometry=true&maxAllowableOffset=&geometryPrecision=&outSR=4326&returnIdsOnly=false&returnCountOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&gdbVersion=&returnDistinctValues=false&f=json',
    'addresses': query_iterator(count=42988, step=1000, query='http://gis.arlingtonva.us/arlgis/rest/services/public/Addresses/MapServer/0/query?geometry=%27%3E&f=json&spatialRel=esriSpatialRelIntersects&outSR=4326&outFields=*&where=OBJECTID%3E{0}&orderByFields=OBJECTID'),
    'parcels': query_iterator(count=38291, query='http://gis.arlingtonva.us/arlgis/rest/services/public/Parcels/MapServer/0/query?geometry=%27%3E&f=json&spatialRel=esriSpatialRelIntersects&outSR=4326&outFields=*&where=OBJECTID%3E{0}&orderByFields=OBJECTID'),
}

ogr2ogr = find_executable('ogr2ogr') or '/Applications/Postgres.app/Contents/MacOS/bin/ogr2ogr'

# Load the GDAL_DATA variable
os.environ['GDAL_DATA'] ='/Library/Frameworks/GDAL.framework/Versions/1.11/Resources/gdal/'

geojson_formatters = dict(extension='geojson', driver='GeoJSON')
shp_formatters = dict(extension='shp', driver='"ESRI Shapefile"')

def main():
    for service, query in QUERIES.items():
        path = os.path.normpath(os.path.join(ROOT, '../data/arlington/{0}'.format(service)))

        if not os.path.exists(path):
            os.mkdir(path)
            os.chdir(path)
            file_path = os.path.join(path, service)
            command_params = dict(file_path=file_path, query=query, ogr2ogr=ogr2ogr, service=service)

            ogr_command = '{ogr2ogr} -f {driver} {service}.{extension} \"{query}\" OGRGeoJSON -skipFailures'

            if hasattr(query, '__iter__'):
                for n, q in enumerate(query):
                    command_params['query'] = q
                    if n != 0:
                        ogr_command += ' -append'
                    os.system(ogr_command.format(**dict(command_params.items() + shp_formatters.items())))

            else:
                #os.system(ogr_command.format(**dict(command_params.items() + geojson_formatters.items())))
                os.system(ogr_command.format(**dict(command_params.items() + shp_formatters.items())))

        else:
            print 'path: {0} already exists'.format(path)

if __name__ == '__main__':
    main()
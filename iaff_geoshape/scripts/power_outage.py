import json
import requests

DOMINION_OUTAGE_SERVICE = 'http://outagemap.dom.com/ArcGIS/rest/services/DOMCOM_OUTAGE_VIEWER/MapServer/0/'


def get_json_response(url):
    """
    Makes a GET request to the URL and returns a dict of the response.
    """
    response = requests.get(url)
    return json.loads(response.content)


def get_query_url():
    """
    Returns a query url by getting the full extent of the service data.
    """

    full_extent = get_json_response(DOMINION_OUTAGE_SERVICE + '?f=json').get('extent')
    spatial_reference = full_extent.get('spatialReference').get('wkid')
    extent = [full_extent.get('xmin'), full_extent.get('ymin'), full_extent.get('xmax'), full_extent.get('ymax')]
    envelope = '%2C'.join(map(str, extent))
    return 'http://outagemap.dom.com/ArcGIS/rest/services/DOMCOM_OUTAGE_VIEWER/MapServer/0/query?text=&geometry={envelope}&geometryType=esriGeometryEnvelope&inSR={spatial_reference}&spatialRel=esriSpatialRelEnvelopeIntersects&where=&returnGeometry=true&outSR=&outFields=*&f=pjson'.format(envelope=envelope, spatial_reference=spatial_reference)


if __name__ == '__main__':
    url = get_query_url()
    data = get_json_response(url)

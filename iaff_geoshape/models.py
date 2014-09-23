from datetime import datetime
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from .utils import get_json_response


class PowerOutage(models.Model):
    """
    Power Outages model based on the Dominion Power schema.
    """

    SERVICE = 'http://outagemap.dom.com/ArcGIS/rest/services/DOMCOM_OUTAGE_VIEWER/MapServer/0/'
    SERVICE_SRID = 2284

    OUTAGE_TIME = models.DateTimeField(blank=True, null=True)
    ETR_MIN_DATE_EXT = models.DateTimeField(blank=True, null=True)
    ETR_MAX_DATE_EXT = models.DateTimeField(blank=True, null=True)
    OBJECTID = models.IntegerField(null=True, blank=True)
    WORK_REQUEST_NUMBER = models.IntegerField(null=True, blank=True)
    WORK_REQUEST_NUMBER = models.CharField(max_length=255, null=True, blank=True)
    WR_CC_IDENTIFIER = models.CharField(max_length=255, null=True, blank=True)
    CUSTOMERS_OUT = models.IntegerField(null=True, blank=True)
    SPEC_COND_YN = models.CharField(max_length=1, choices=(('Y', 'Y'), ('N', 'N')))
    CUST_CATEGORY = models.CharField(max_length=255, null=True, blank=True)
    CUST_DESC = models.CharField(max_length=255, null=True, blank=True)
    NUM_SC_CUST_OUT = models.IntegerField(null=True, blank=True)
    objects = models.GeoManager()
    geom = models.PointField()


    @staticmethod
    def get_query_url(service=SERVICE):
        """
        Generates a URL that returns features from the service.
        """
        full_extent = get_json_response(service + '?f=json').get('extent')
        spatial_reference = full_extent.get('spatialReference').get('wkid')
        extent = [full_extent.get('xmin'), full_extent.get('ymin'), full_extent.get('xmax'), full_extent.get('ymax')]
        envelope = '%2C'.join(map(str, extent))
        return 'http://outagemap.dom.com/ArcGIS/rest/services/DOMCOM_OUTAGE_VIEWER/MapServer/0/query?text=&geometry={envelope}&geometryType=esriGeometryEnvelope&inSR={spatial_reference}&spatialRel=esriSpatialRelEnvelopeIntersects&where=&returnGeometry=true&outSR=&outFields=*&f=pjson'.format(envelope=envelope, spatial_reference=spatial_reference)

    @staticmethod
    def fetch_data():
        """
        Fetches data from the service.
        """
        data = get_json_response(PowerOutage.get_query_url())
        return data.get('features')

    @staticmethod
    def parse_OUTAGE_TIME(value):
        """
        Parse the outage time format (Sep. 23 07:27 AM) into a datetime object.
        """
        return datetime.strptime(value, '%b. %d %I:%M %p')

    @staticmethod
    def parse_ETR_MIN_DATE_EXT(value):
        """
        Parse the etr_min_date_ext time format (9/23/2014 1:00:00 PM) into a datetime object.
        """
        return datetime.strptime(value, '%m/%d/%Y %I:%M:%S %p')

    @staticmethod
    def parse_ETR_MAX_DATE_EXT(value):
        """
        Parse the etr_max_date_ext time format (9/23/2014 1:00:00 PM) into a datetime object.
        """
        return datetime.strptime(value, '%m/%d/%Y %I:%M:%S %p')

    @classmethod
    def update_data(cls):
        """
        Updates the PowerOutage class with new features.
        """

        features = cls.fetch_data()
        cls.objects.all().delete()
        field_names = cls._meta.get_all_field_names()

        for feature in features:
            matching_attributes = filter(lambda attr: attr[0] in field_names, feature.get('attributes', {}).items())
            outage = PowerOutage()

            for key, value in matching_attributes:
                parse_function = getattr(cls, 'parse_{0}'.format(key), None)

                if parse_function:
                    value = parse_function(value)

                setattr(outage, key, value)

            geometry = feature.get('geometry')
            outage.geom = Point(geometry.get('x', 0), geometry.get('y', 0), srid=cls.SERVICE_SRID)
            outage.save()











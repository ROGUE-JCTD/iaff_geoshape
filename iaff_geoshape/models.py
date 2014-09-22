from django.contrib.gis.db import models


class PowerOutage(models.Model):
    """
    Power Outages model based on the Dominion Power schema.
    """

    SERVICE = 'http://outagemap.dom.com/ArcGIS/rest/services/DOMCOM_OUTAGE_VIEWER/MapServer/0/'

    outage_time = models.DateTimeField(blank=True, null=True)
    etr_min_date_ext = models.DateTimeField(blank=True, null=True)
    etr_max_date_ext = models.DateTimeField(blank=True, null=True)
    object_id = models.IntegerField(null=True, blank=True)
    work_request_number = models.IntegerField(null=True, blank=True)
    wr_order_type = models.CharField(max_length=255, null=True, blank=True)
    wr_cc_identifier = models.CharField(max_length=255, null=True, blank=True)
    customers_out = models.IntegerField(null=True, blank=True)
    spec_cond_yn = models.CharField(max_length=1, choices=(('Y', 'Y'), ('N', 'N')))
    cust_category = models.CharField(max_length=255, null=True, blank=True)
    cust_dest = models.CharField(max_length=255, null=True, blank=True)
    num_sc_cust_out = models.IntegerField(null=True, blank=True)
    objects = models.GeoManager()
    geom = models.PointField()

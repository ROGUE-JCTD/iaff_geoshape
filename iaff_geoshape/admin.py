from .models import PowerOutage
from django.contrib.gis import admin


class PowerOutageAdmin(admin.OSMGeoAdmin):
    list_display = ['CUSTOMERS_OUT', 'OUTAGE_TIME', 'ETR_MIN_DATE_EXT', 'ETR_MAX_DATE_EXT']
    list_filter = ['OUTAGE_TIME', 'SPEC_COND_YN', 'CUST_CATEGORY']

admin.site.register(PowerOutage, PowerOutageAdmin)

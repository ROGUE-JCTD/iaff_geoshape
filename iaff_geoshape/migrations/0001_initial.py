# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PowerOutage'
        db.create_table(u'iaff_geoshape_poweroutage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('outage_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('etr_min_date_ext', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('etr_max_date_ext', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('object_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('work_request_number', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('wr_order_type', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('wr_cc_identifier', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('customers_out', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('spec_cond_yn', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('cust_category', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('cust_dest', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('num_sc_cust_out', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.PointField')()),
        ))
        db.send_create_signal(u'iaff_geoshape', ['PowerOutage'])


    def backwards(self, orm):
        # Deleting model 'PowerOutage'
        db.delete_table(u'iaff_geoshape_poweroutage')


    models = {
        u'iaff_geoshape.poweroutage': {
            'Meta': {'object_name': 'PowerOutage'},
            'cust_category': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'cust_dest': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'customers_out': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'etr_max_date_ext': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'etr_min_date_ext': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'geom': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num_sc_cust_out': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'outage_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'spec_cond_yn': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'work_request_number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'wr_cc_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'wr_order_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['iaff_geoshape']
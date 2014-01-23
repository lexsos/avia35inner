# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Phone'
        db.create_table(u'mobile_phone', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'mobile', ['Phone'])

        # Adding model 'MonthlyLimit'
        db.create_table(u'mobile_monthlylimit', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('limit_sum', self.gf('django.db.models.fields.FloatField')()),
            ('phone', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mobile.Phone'])),
            ('deleted_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'mobile', ['MonthlyLimit'])

        # Adding unique constraint on 'MonthlyLimit', fields ['user', 'phone', 'deleted_at']
        db.create_unique(u'mobile_monthlylimit', ['user_id', 'phone_id', 'deleted_at'])

        # Adding model 'Month'
        db.create_table(u'mobile_month', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('consumption_file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('month_number', self.gf('django.db.models.fields.DateField')()),
            ('year_number', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'mobile', ['Month'])

        # Adding unique constraint on 'Month', fields ['year_number', 'month_number']
        db.create_unique(u'mobile_month', ['year_number', 'month_number'])

        # Adding model 'Consumption'
        db.create_table(u'mobile_consumption', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('month', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mobile.Month'])),
            ('monthly_limit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mobile.MonthlyLimit'])),
            ('consumption_sum', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'mobile', ['Consumption'])

        # Adding unique constraint on 'Consumption', fields ['month', 'monthly_limit']
        db.create_unique(u'mobile_consumption', ['month_id', 'monthly_limit_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Consumption', fields ['month', 'monthly_limit']
        db.delete_unique(u'mobile_consumption', ['month_id', 'monthly_limit_id'])

        # Removing unique constraint on 'Month', fields ['year_number', 'month_number']
        db.delete_unique(u'mobile_month', ['year_number', 'month_number'])

        # Removing unique constraint on 'MonthlyLimit', fields ['user', 'phone', 'deleted_at']
        db.delete_unique(u'mobile_monthlylimit', ['user_id', 'phone_id', 'deleted_at'])

        # Deleting model 'Phone'
        db.delete_table(u'mobile_phone')

        # Deleting model 'MonthlyLimit'
        db.delete_table(u'mobile_monthlylimit')

        # Deleting model 'Month'
        db.delete_table(u'mobile_month')

        # Deleting model 'Consumption'
        db.delete_table(u'mobile_consumption')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'mobile.consumption': {
            'Meta': {'ordering': "['month', 'monthly_limit']", 'unique_together': "(('month', 'monthly_limit'),)", 'object_name': 'Consumption'},
            'consumption_sum': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'month': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mobile.Month']"}),
            'monthly_limit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mobile.MonthlyLimit']"})
        },
        u'mobile.month': {
            'Meta': {'ordering': "['year_number', 'month_number']", 'unique_together': "(('year_number', 'month_number'),)", 'object_name': 'Month'},
            'consumption_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'month_number': ('django.db.models.fields.DateField', [], {}),
            'year_number': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'mobile.monthlylimit': {
            'Meta': {'ordering': "['user', 'phone']", 'unique_together': "(('user', 'phone', 'deleted_at'),)", 'object_name': 'MonthlyLimit'},
            'deleted_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'limit_sum': ('django.db.models.fields.FloatField', [], {}),
            'phone': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mobile.Phone']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'mobile.phone': {
            'Meta': {'ordering': "['phone_number']", 'object_name': 'Phone'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['mobile']
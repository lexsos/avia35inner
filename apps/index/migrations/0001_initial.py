# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Content'
        db.create_table(u'index_content', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('enabled', self.gf('django.db.models.fields.BooleanField')(default=True, db_index=True)),
            ('pub_date_start', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, db_index=True)),
            ('pub_date_end', self.gf('django.db.models.fields.DateTimeField')(db_index=True, null=True, blank=True)),
            ('weight', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, db_index=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('content_rich', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('content_plane', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'index', ['Content'])


    def backwards(self, orm):
        # Deleting model 'Content'
        db.delete_table(u'index_content')


    models = {
        u'index.content': {
            'Meta': {'ordering': "['-weight', '-pub_date_start']", 'object_name': 'Content'},
            'content_plane': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'content_rich': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date_end': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'pub_date_start': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'weight': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'db_index': 'True'})
        }
    }

    complete_apps = ['index']
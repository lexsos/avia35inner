# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Document'
        db.create_table(u'documents_document', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('enabled', self.gf('django.db.models.fields.BooleanField')(default=True, db_index=True)),
            ('pub_date_start', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, db_index=True)),
            ('pub_date_end', self.gf('django.db.models.fields.DateTimeField')(db_index=True, null=True, blank=True)),
            ('weight', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, db_index=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('document', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'documents', ['Document'])

        # Adding model 'Page'
        db.create_table(u'documents_page', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('document', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['documents.Document'])),
            ('page_file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('page_number', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'documents', ['Page'])

        # Adding unique constraint on 'Page', fields ['document', 'page_number']
        db.create_unique(u'documents_page', ['document_id', 'page_number'])


    def backwards(self, orm):
        # Removing unique constraint on 'Page', fields ['document', 'page_number']
        db.delete_unique(u'documents_page', ['document_id', 'page_number'])

        # Deleting model 'Document'
        db.delete_table(u'documents_document')

        # Deleting model 'Page'
        db.delete_table(u'documents_page')


    models = {
        u'documents.document': {
            'Meta': {'ordering': "['-weight', 'pub_date_start']", 'object_name': 'Document'},
            'document': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date_end': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'pub_date_start': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'weight': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'db_index': 'True'})
        },
        u'documents.page': {
            'Meta': {'ordering': "('document', 'page_number')", 'unique_together': "(('document', 'page_number'),)", 'object_name': 'Page'},
            'document': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['documents.Document']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'page_number': ('django.db.models.fields.PositiveIntegerField', [], {})
        }
    }

    complete_apps = ['documents']
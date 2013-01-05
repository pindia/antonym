# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Word.status'
        db.add_column('antonym_word', 'status',
                      self.gf('django.db.models.fields.IntegerField')(default=0, db_index=True),
                      keep_default=False)

        # Adding field 'Word.created'
        db.add_column('antonym_word', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 1, 5, 0, 0), blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Word.status'
        db.delete_column('antonym_word', 'status')

        # Deleting field 'Word.created'
        db.delete_column('antonym_word', 'created')


    models = {
        'antonym.word': {
            'Meta': {'object_name': 'Word'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'})
        },
        'antonym.wordresponse': {
            'Meta': {'object_name': 'WordResponse'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'response': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'session': ('django.db.models.fields.IntegerField', [], {}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'word': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['antonym.Word']"})
        }
    }

    complete_apps = ['antonym']
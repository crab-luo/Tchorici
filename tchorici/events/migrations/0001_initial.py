# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Event'
        db.create_table('events_event', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('date_start', self.gf('django.db.models.fields.DateField')()),
            ('date_end', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('events', ['Event'])

        # Adding M2M table for field people on 'Event'
        db.create_table('events_event_people', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm['events.event'], null=False)),
            ('person', models.ForeignKey(orm['people.person'], null=False))
        ))
        db.create_unique('events_event_people', ['event_id', 'person_id'])

        # Adding model 'Link'
        db.create_table('events_link', (
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(related_name='link', to=orm['events.Event'])),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=35)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=7)),
        ))
        db.send_create_signal('events', ['Link'])


    def backwards(self, orm):
        # Deleting model 'Event'
        db.delete_table('events_event')

        # Removing M2M table for field people on 'Event'
        db.delete_table('events_event_people')

        # Deleting model 'Link'
        db.delete_table('events_link')


    models = {
        'events.event': {
            'Meta': {'ordering': "['-date_start', 'name']", 'object_name': 'Event'},
            'date_end': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_start': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'people': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['people.Person']", 'symmetrical': 'False', 'blank': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        },
        'events.link': {
            'Meta': {'ordering': "['name', 'description']", 'object_name': 'Link'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'link'", 'to': "orm['events.Event']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'primary_key': 'True'})
        },
        'people.person': {
            'Meta': {'ordering': "['first_name', 'last_name']", 'unique_together': "(('first_name', 'last_name'),)", 'object_name': 'Person'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['events']
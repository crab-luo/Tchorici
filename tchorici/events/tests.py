"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from datetime import datetime

from django.conf import settings
from django.core.files import File
from django.test import TestCase

from events.models import Event

DATA_PATH = settings.FIXTURE_DIRS[0]


class EventsTestCase(TestCase):
	fixtures = ['events.json']

	def test_photo(self):
		photo = open(DATA_PATH + 'event_photo.jpg')
		event = Event(name='Test', photo=File(photo), date_start=datetime.now())
		event.save()

		print event.photo.width


class EventsViewsTestCase(TestCase):
	fixtures = ['events.json']

	def test_index(self):
		resp = self.client.get('/')
		self.assertEqual(resp.status_code, 200)

		events = resp.context['events']
		for i in range(events.paginator.num_pages):
			self.test_page(i + 1, 200)

	def test_page(self, i=1, status=200):
		page = self.client.get('/seznam/' + str(i) + '/')
		self.assertTrue('events' in page.context)
		self.assertEqual(page.status_code, status)

	def test_last_page(self):
		first_page = self.client.get('/seznam/1/')
		pages = first_page.context['events'].paginator.num_pages

		last_page = self.client.get('/seznam/' + str(pages) + '/').flush()
		next_page = self.client.get('/seznam/' + str(pages + 1) + '/').flush()

		self.assertEqual(last_page, next_page)

	def test_detail(self):
		events = Event.objects.all()

		for event in events:
			detail = self.client.get('/akce/' + event.slug + '.html')
			self.assertEqual(detail.status_code, 200)



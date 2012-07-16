from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap

from events.models import Event

sitemaps = {
	'flatpages': FlatPageSitemap,
	'events': GenericSitemap({
		'queryset': Event.objects.all(),
	}, priority=0.9, changefreq='monthly'),
}


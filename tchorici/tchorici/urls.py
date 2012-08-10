from django.conf.urls import patterns, include, url

from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.views.generic.simple import direct_to_template

from sitemaps import sitemaps

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#handler404 = 'tchorici.views.error404'
#handler500 = 'tchorici.views.error500'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tchorici.views.home', name='home'),
    # url(r'^tchorici/', include('tchorici.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^imperavi/', include('imperavi.urls')),

    url(r'^robots\.txt$', direct_to_template, {'template': 'robots.txt', 'mimetype': 'text/plain'}),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),

    url(r'^$', 'events.views.list', name='list'),
    url(r'^seznam/(?P<page>[0-9]+)/$', 'events.views.list'),
    url(r'^akce/(?P<id>\d+)-(?P<slug>[^/]+)\.html', 'events.views.detail', name='detail'),
    url(r'^tchori/$', 'people.views.list'),

    url(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/static/images/favicon.ico'}),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

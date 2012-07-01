from django.conf.urls import patterns, include, url

from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

handler404 = 'tchorici.views.error404'
handler500 = 'tchorici.views.error500'

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'tchorici.views.home', name='home'),
	# url(r'^tchorici/', include('tchorici.foo.urls')),

	# Uncomment the admin/doc line below to enable admin documentation:
	# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),

	url(r'^$', 'events.views.list', name='list'),
	url(r'^akce/(?P<slug>[^/]+)\.html', 'events.views.detail', name='detail'),
	url(r'^tchori/$', 'people.views.list'),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'pocketServ.views.home', name='home'),
    url(r'^ajax-gauge-update$', 'pocketServ.views.ajax_gauge_update', name='ajax_gauge_update'),
    # url(r'^pocketServ/', include('pocketServ.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

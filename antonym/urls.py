from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'antonym2.views.home', name='home'),
    # url(r'^antonym2/', include('antonym2.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'antonym.views.index'),
    url(r'^add$', 'antonym.views.add'),
    url(r'^respond/([a-z ]+)/([a-z ]+)$', 'antonym.views.respond'),
)

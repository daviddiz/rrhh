#encoding:utf-8
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rrhh.views.home', name='home'),
    # url(r'^rrhh/', include('rrhh.foo.urls')),
    url(r'^rrhh/registro/$', 'registro.views.index'),
#    url(r'^rrhh/registro/done/$', 'registro.views.done'),
    url(r'^rrhh/registro/done/(?P<usuari>\w+)/(?P<contrasenya>\w+)/(?P<lat>\W*\w+.\w+)/(?P<lng>\W*\w+.\w+)/$', 'registro.views.done'),
    url(r'^rrhh/registro/error_check/$', 'registro.views.error_check'),
#    url(r'^rrhh/registro/check/$', 'registro.views.checks'),
    url(r'^rrhh/registro/check/(?P<usuari>\w+)/(?P<contrasenya>\w+)/$', 'registro.views.checks'),
#    url(r'^rrhh/registro/dieta/$', 'registro.views.dietas'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    #url(r'^', include('registro.urls')),
    # Uncomment the next line to enable the admin:
#    url(r'^admin/', include(admin.site.urls)),
)

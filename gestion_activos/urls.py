from django.conf.urls import patterns, include, url


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gestion_activos.views.home', name='home'),
    # url(r'^gestion_activos/', include('gestion_activos.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^resumen/todos', 'activos.views.getResumenGral',{'cmd': 'todos'}),
    url(r'^resumen/noasegurables$', 'activos.views.getResumenSeg',{'cmd': 'noasegurables$'}),
    url(r'^resumen/seguro/todos$', 'activos.views.getResumenSeg'),
    url(r'^resumen/seguro/asegurables', 'activos.views.getResumenSeg',{'cmd': 'asegurables'}),
    url(r'^resumen/seguro/asegurados', 'activos.views.getResumenSeg',{'cmd': 'asegurados'}),
    url(r'^resumen/seguro/noasegurados$', 'activos.views.getResumenSeg',{'cmd': 'noasegurados'}),
    url(r'^resumen/seguro/sinvalorizar', 'activos.views.getResumenSeg',{'cmd': 'sinvalorizar'}),
    url(r'^resumen/seguro/asegurar', 'activos.views.getResumenSeg',{'cmd': 'asegurar'}),
    url(r'^tmp/', 'activos.views.tmp',)
)

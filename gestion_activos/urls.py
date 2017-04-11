from django.conf.urls import patterns, include, url


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^grappelli/',
        include('grappelli.urls')),  # grappelli URLS

    url(r'^admin/',
        include(admin.site.urls)),  # admin URLS

    url(r'^resumen/todos',
        'activos.views.getResumenGral'),
    url(r'^resumen/noasegurables$',
        'activos.views.getResumenSeg',
        {'cmd': 'noasegurables$'}),
    url(r'^resumen/seguro/todos$',
        'activos.views.getResumenSeg'),
    url(r'^resumen/seguro/asegurables',
        'activos.views.getResumenSeg',
        {'cmd': 'asegurables'}),
    url(r'^resumen/seguro/asegurados',
        'activos.views.getResumenSeg',
        {'cmd': 'asegurados'}),
    url(r'^resumen/seguro/noasegurados$',
        'activos.views.getResumenSeg',
        {'cmd': 'noasegurados'}),
    url(r'^resumen/seguro/sinvalorizar',
        'activos.views.getResumenSeg',
        {'cmd': 'sinvalorizar'}),
    url(r'^resumen/seguro/asegurar',
        'activos.views.getResumenSeg',
        {'cmd': 'asegurar'}),
    url(r'^tmp/',
        'activos.views.tmp',)
)

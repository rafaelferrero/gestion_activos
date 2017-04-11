from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from activos import views

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'activos.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),  # admin URLS
    url(r'^grappelli/', include('grappelli.urls')),  # grappelli URLS
    url(r'^resumen/(?:(?P<cmd>\w+)/)?$', views.getResumenSeg, name="resumen"),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

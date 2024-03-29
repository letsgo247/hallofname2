from django.conf.urls import url
from django.contrib import admin
from . import views

from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap


app_name = 'bnm'

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^generate.+$', views.generate, name = 'generate'),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')
]
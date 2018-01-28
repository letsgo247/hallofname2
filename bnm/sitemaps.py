from django.contrib import sitemaps
from django.urls import reverse

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.9
    changefreq = 'monthly'

    def items(self):
        return ['bnm:index', 'bnm:generate']

    def location(self, item):
        return reverse(item)
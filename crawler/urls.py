from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'crawler'

urlpatterns = [
    url(r'^crawler.+$', views.index, name = 'index'),
]
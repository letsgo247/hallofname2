from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'bnm'

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^generate.+$', views.generate, name = 'generate'),
]
# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns(
    'myproject.myapp.views',
    url(r'^list/$', 'list', name='list'),
    url(r'^downloadAsText/$', 'downloadAsText', name='downloadAsText'),
    url(r'^downloadAsCSV/$', 'downloadAsCSV', name='downloadAsCSV'),
    url(r'^downloadAsDoc/$', 'downloadAsDOC', name='downloadAsDOC'),
    url(r'^showText/$', 'showText', name='showText'),
    url(r'^contact/$', 'contact', name='contact'),
    url(r'^services/$', 'services', name='services'),
    url(r'^home/$', 'home', name='home'),
    url(r'^about/$', 'about', name='about'),
)

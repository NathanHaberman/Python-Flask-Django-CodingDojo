from django.conf.urls import url, include
from views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^(?P<user_id>[1-9][0-9]*)/$', user),
    url(r'^new/$', new),
    url(r'^create/$', create),
    url(r'^(?P<user_id>[1-9][0-9]*)/edit/$', edit),
    url(r'^(?P<user_id>[1-9][0-9]*)/update/$', update),
    url(r'^(?P<user_id>[1-9][0-9]*)/destroy$', destroy),
]
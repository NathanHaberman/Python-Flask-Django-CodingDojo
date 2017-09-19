from django.conf.urls import url, include
from views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^add/$', add),
    url(r'^check/(?P<course_id>[0-9][1-9]*)/$', check),
    url(r'^destroy/(?P<course_id>[0-9][1-9]*)/$', destroy),
]

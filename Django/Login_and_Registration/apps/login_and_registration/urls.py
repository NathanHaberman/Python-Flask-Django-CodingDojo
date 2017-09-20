from django.conf.urls import url, include
from views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^register/$', register),
    url(r'^login/$', login),
    url(r'^success/$', success),
]
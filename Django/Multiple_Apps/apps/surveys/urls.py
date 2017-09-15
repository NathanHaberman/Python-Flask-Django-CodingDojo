from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^/new$', new),
    url(r'^/$', index),
]
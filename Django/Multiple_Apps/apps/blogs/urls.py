from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^/new$', new_blog),
    url(r'^/create$', create_blog),
    url(r'^/(?P<number>\d+)$', blog),
    url(r'^', index),
]
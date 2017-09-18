from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^checkout', checkout),
    url(r'^buy', buy),
    url(r'^reset', reset),
]

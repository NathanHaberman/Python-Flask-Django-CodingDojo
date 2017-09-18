from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^gold$', gold),
    url(r'^reset$', reset),
]
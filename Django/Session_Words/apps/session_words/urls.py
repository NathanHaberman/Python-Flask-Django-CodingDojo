from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^session_add$', session_add),
]
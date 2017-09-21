from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', home),
    url(r'^add/$', add),
    url(r'^submit/$', submit),
    url(r'^(?P<book_id>[1-9][0-9]*)/$', book_page),
    url(r'^(?P<book_id>[1-9][0-9]*)/review/$', review),
    url(r'^(?P<review_id>[1-9][0-9]*)/delete/$', delete),
    url(r'^users/(?P<user_id>[1-9][0-9]*)/$', user_page),
]
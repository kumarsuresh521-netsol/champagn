'''app urls.py'''
from django.conf.urls import url
from frontendlogs import api

# pylint: disable=C0103
urlpatterns = [
    url(r'^(?i)submitErrorLog/$', api.FrontendLog.as_view()),
]

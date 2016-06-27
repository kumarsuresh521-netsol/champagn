'''cms urls.py'''
from django.conf.urls import url
from cms import views

# pylint: disable=C0103
urlpatterns = [
    url(r'^(?i)contactus/$', views.contactus, name='contactus'),
    url(r'^(?i)aboutus/$', views.aboutus, name='aboutus'),
    url(r'^(?i)privacy/$', views.privacy, name='privacy'),
    url(r'^(?i)termsofuse/$', views.termsofuse, name='termsofuse'),
    url(r'^(?i)mediacontact/$', views.mediacontact, name='mediacontact'),
    url(r'^(?i)appdevelopers/$', views.appdevelopers, name='appdevelopers'),
    url(r'^(?i)investers/$', views.investers, name='investers'),
]

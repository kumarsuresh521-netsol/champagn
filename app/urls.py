'''
for handling urls of master app
'''
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from app.views import preview_tempate
from app.api import SignUp, SignIn, SignOut, GetProfile, EditProfile, ChangePassword


urlpatterns = [
    url(r'^api/signup/$', SignUp.as_view()),
    url(r'^api/signin/$', SignIn.as_view()),
    url(r'^api/signout/$', SignOut.as_view()),      
    url(r'^api/getprofile/$', GetProfile.as_view()),
    url(r'^api/editprofile/$', EditProfile.as_view()),
    url(r'^api/changepassword/$', ChangePassword.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

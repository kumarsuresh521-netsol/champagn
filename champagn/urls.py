"""champagn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from app.password import password_reset, password_reset_complete, password_reset_confirm, password_reset_done
from app.views import view_site, preview_tempate, barcode

urlpatterns = [
# User Forgot Password URLs
    url(r'^(?i)user/password_reset/$', password_reset, name='password_reset'),
    url(r'^(?i)user/password_reset/done/$', password_reset_done, name='password_reset_done'),
    url(r'^(?i)user/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', password_reset_confirm, name='password_reset_confirm'),
    url(r'^(?i)user/reset/done/$', password_reset_complete, name='password_reset_complete'),

    url(r'^(?i)admin/login/', 'django.contrib.auth.views.login', {'template_name': 'admin/custom_login.html'}),
    url(r'^(?i)admin/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/admin/login/?next=/admin/'}),
    url(r'^(?i)accounts/login/$', 'django.contrib.auth.views.logout', {'next_page': '/admin/login/?next=/admin/', 'template_name': 'custom_login.html'}),

    url(r'^admin/password_reset/$', auth_views.password_reset, name='admin_password_reset'),
    url(r'^admin/password_reset/done/$', auth_views.password_reset_done, name='admin_password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', auth_views.password_reset_confirm, name='admin_password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='admin_password_reset_complete'),
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^master/', include('master.urls')),
    url(r'^app/', include('app.urls')),
    url(r'^product/', include('product.urls')),
    url(r'^$', view_site),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^logs/api/', include('frontendlogs.urls', namespace='frontendlogs')),
    url(r'^password/', include('password_reset.urls', namespace='passwordReset')),
    
    url(r'^previewtemplate/(?P<preview_id>[0-9]+)/$', preview_tempate, name='preview_detail'),
    url(r'^barcode/$', barcode)
]

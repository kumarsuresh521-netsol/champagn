'''
admin fro app
'''
from django.conf import settings
from django.contrib.admin import AdminSite
from django.contrib import admin
from app.models import User
from django.contrib.auth.models import Group
    
AdminSite.site_header = settings.ADMIN_SITE_HEADER
AdminSite.site_title = settings.ADMIN_SITE_TITLE
# Register your models here.

admin.site.register(User)

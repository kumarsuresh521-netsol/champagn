from django.contrib import admin
from django.conf import settings
from frontendlogs.models import FrontLog

#Register your models here.


class FrontLogAdmin(admin.ModelAdmin):
    list_display = ['exception', 'create_date']
    list_per_page = settings.ADMIN_PAGE_SIZE
    ordering = ['-id']
    search_fields = ['exception']
    list_filter = ['exception', 'create_date']

admin.site.register(FrontLog, FrontLogAdmin)

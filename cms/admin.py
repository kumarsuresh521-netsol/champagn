from django.contrib import admin
from models import CmsPage
from django.conf import settings
from cms import models
from django.core.urlresolvers import reverse
from tinymce.widgets import TinyMCE
# Register your models here.


class CmsPageAdmin(admin.ModelAdmin):
    """
    custom Admin Class for Privacy model
    """
    list_display = ['title', 'create_date']
    search_fields = ['title']
    list_per_page = settings.ADMIN_PAGE_SIZE
#     formfield_overrides = {
#         models.HTMLField: {'widget': TinyMCE(
#                         attrs={'rows': 0,
#                             'cols': 36,
#                             'style': 'height: 3em;'},
#                         #mce_attrs={'external_link_list_url': reverse('someapp.views.someview')}
#                     )},
#     }
    actions = None

    @classmethod
    def has_add_permission(self, request):
        return False

    @classmethod
    def has_delete_permission(self, request, obj=None):
        # Disable delete
        return False
admin.site.register(CmsPage, CmsPageAdmin)

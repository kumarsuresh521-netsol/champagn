from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models
# Register your models here.
from .models import Log
# admin.site.register(Log)
 
from django.contrib.admin import SimpleListFilter
 
 
class NullListFilter(SimpleListFilter):
 
    def lookups(self, request, model_admin):
        return (
            ('1', 'Success', ),
            ('0', 'Execption', ),
        )
 
    def queryset(self, request, queryset):
        if self.value() in ('0', '1'):
            kwargs = {
                '{0}__isnull'.format(self.parameter_name): self.value() == '1'}
            return queryset.filter(**kwargs)
        return queryset
 
 
def null_filter(field, title_=None):
    class NullListFieldFilter(NullListFilter):
        parameter_name = field
        title = title_ or parameter_name
    return NullListFieldFilter
 
 
class LogAdmin(admin.ModelAdmin):
 
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '20'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 20})},
    }
 
    your_fields = Log._meta.local_fields
    lst_of_field_names = [f.name for f in your_fields]
    lst_of_field_names.remove('request_content')
    lst_of_field_names.remove('response_content')
    list_display = ['method_type', 'method_name', 'short_request_content',
                    'short_response_content', 'short_exception_full_stack_trace', 'total_time_taken']
    list_per_page = 500
    list_filter = ('response_status_type', 'method_type',
                   null_filter('exception_full_stack_trace'),)
 
 
admin.site.register(Log, LogAdmin)

from django.contrib import admin
from models import Email
# Register your models here.
 
 
class EmailAdmin(admin.ModelAdmin):
    '''
    list columns of email
    '''
    list_display = [
        'from_email', 'to_email', 'subject', 'sent_status_type', 'sent_date']
 
admin.site.register(Email, EmailAdmin)

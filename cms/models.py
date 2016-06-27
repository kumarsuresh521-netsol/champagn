from django.db import models
from tinymce.models import HTMLField
from django_enumfield import enum
# Create your models here.


class CmsPage(models.Model):
    title = models.CharField(max_length=100)
    content = HTMLField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

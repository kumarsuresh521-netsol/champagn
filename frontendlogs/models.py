from django.db import models

# Create your models here.


class FrontLog(models.Model):
    '''
    Front Log Class
    '''
    exception = models.TextField(null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.exception

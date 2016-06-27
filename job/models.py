from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django_enumfield import enum
from champagn.enums import SentStatusType

# Create your models here.


class Email(models.Model):
    from_email = models.EmailField(
        max_length=255, default=settings.EMAIL_DEFAULT)
    to_email = models.EmailField(
        max_length=255, default=settings.EMAIL_DEFAULT)
    cc = ArrayField(models.EmailField(max_length=255), blank=True, null=True)
    subject = models.CharField(max_length=200, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    sent_status_type = enum.EnumField(
        SentStatusType, default=SentStatusType.PENDING)
    sent_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.to_email

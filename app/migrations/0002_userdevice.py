# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDevice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('device_token', models.CharField(max_length=200, blank=True)),
                ('device_id', models.CharField(max_length=500)),
                ('device_type', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=False, help_text=b'Designates whether the App User Device is active or not ')),
                ('is_device_token_valid', models.BooleanField(default=True, help_text=b'Designates whether theUser Device token is valid or not ')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(related_name='user_device', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

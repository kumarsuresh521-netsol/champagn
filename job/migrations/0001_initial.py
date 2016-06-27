# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('from_email', models.EmailField(default=b'suresh.kumar@netsolutions.in', max_length=255)),
                ('to_email', models.EmailField(default=b'suresh.kumar@netsolutions.in', max_length=255)),
                ('cc', django.contrib.postgres.fields.ArrayField(size=None, null=True, base_field=models.EmailField(max_length=255), blank=True)),
                ('subject', models.CharField(max_length=200, null=True, blank=True)),
                ('message', models.TextField(null=True, blank=True)),
                ('sent_status_type', models.IntegerField(default=0)),
                ('sent_date', models.DateTimeField(null=True, blank=True)),
            ],
        ),
    ]

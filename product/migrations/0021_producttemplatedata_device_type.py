# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0020_remove_producttemplatedata_device_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='producttemplatedata',
            name='device_type',
            field=models.IntegerField(default=0),
        ),
    ]

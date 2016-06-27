# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0019_auto_20160616_1755'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producttemplatedata',
            name='device_type',
        ),
    ]

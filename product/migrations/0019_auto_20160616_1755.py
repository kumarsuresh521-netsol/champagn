# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0018_auto_20160616_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producttemplatedata',
            name='device_type',
            field=models.IntegerField(default=b'0'),
        ),
    ]

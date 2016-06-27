# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20160531_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='occasion_end_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='occasion_start_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]

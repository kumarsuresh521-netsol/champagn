# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20160609_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='occasion_end_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='occasion_start_date',
            field=models.DateField(null=True, blank=True),
        ),
    ]

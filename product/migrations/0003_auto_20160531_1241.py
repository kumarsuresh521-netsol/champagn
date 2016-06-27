# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20160531_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='engaving_msg_price',
            field=models.IntegerField(),
        ),
    ]

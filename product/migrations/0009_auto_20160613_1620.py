# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20160613_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='amount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='capacity',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='engaving_msg_price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='productimages',
            name='is_active',
            field=models.BooleanField(default=False, help_text=b''),
        ),
        migrations.AlterField(
            model_name='producttemplate',
            name='is_active',
            field=models.BooleanField(default=False, help_text=b''),
        ),
    ]

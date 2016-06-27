# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_auto_20160614_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='producttemplate',
            name='category',
            field=models.ForeignKey(related_name='product_category_template', default=1, to='product.ProductCategory'),
            preserve_default=False,
        ),
    ]

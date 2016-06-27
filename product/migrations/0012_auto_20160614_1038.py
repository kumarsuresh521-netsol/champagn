# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_auto_20160614_1037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcategoryrelation',
            name='product_id',
        ),
        migrations.RemoveField(
            model_name='productcategoryrelation',
            name='productcategory_id',
        ),
        migrations.DeleteModel(
            name='ProductCategoryRelation',
        ),
    ]

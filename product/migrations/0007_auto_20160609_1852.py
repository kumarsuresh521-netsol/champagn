# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20160609_1721'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productimages',
            options={'verbose_name': 'product-image', 'verbose_name_plural': 'Product Images'},
        ),
        migrations.AlterModelOptions(
            name='producttemplate',
            options={'verbose_name': 'product-template', 'verbose_name_plural': 'Product Templates'},
        ),
        migrations.AlterModelOptions(
            name='producttemplatedata',
            options={'verbose_name': 'product-template-data', 'verbose_name_plural': 'Product Templates Data'},
        ),
        migrations.AlterField(
            model_name='product',
            name='amount',
            field=models.IntegerField(),
        ),
    ]

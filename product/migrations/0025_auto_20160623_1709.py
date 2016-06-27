# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0024_auto_20160623_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producttemplatedata',
            name='product_template',
            field=models.ForeignKey(related_name='template_data', to='product.ProductTemplate'),
        ),
    ]

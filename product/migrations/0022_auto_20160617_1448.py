# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0021_producttemplatedata_device_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producttemplatedata',
            old_name='product',
            new_name='product_template',
        ),
    ]

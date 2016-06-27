# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0026_producttemplatedataimage_producttemplatedatatext'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producttemplatedataimage',
            old_name='default_image',
            new_name='image',
        ),
    ]

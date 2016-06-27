# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_producttemplate_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producttemplatedata',
            name='bottom',
        ),
        migrations.RemoveField(
            model_name='producttemplatedata',
            name='right',
        ),
    ]

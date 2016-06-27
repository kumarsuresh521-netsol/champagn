# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0017_auto_20160616_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producttemplatedata',
            name='height',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='producttemplatedata',
            name='left',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='producttemplatedata',
            name='top',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='producttemplatedata',
            name='width',
            field=models.IntegerField(default=0),
        ),
    ]

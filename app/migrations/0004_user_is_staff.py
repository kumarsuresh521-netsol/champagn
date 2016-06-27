# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20160531_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=True, help_text=b'Designates whether                                        this user should be treated as                                        active. Unselect this instead                                        of deleting accounts.'),
        ),
    ]

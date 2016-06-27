# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0027_auto_20160624_1631'),
    ]

    operations = [
        migrations.CreateModel(
            name='EngraveMessage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('engrave_message', models.CharField(max_length=50)),
                ('sort_order', models.IntegerField()),
                ('is_active', models.BooleanField(default=False)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(related_name='engrave_category', to='product.ProductCategory')),
                ('product', models.ForeignKey(related_name='engrave_product', to='product.Product')),
            ],
            options={
                'verbose_name': 'Engrave Message',
                'verbose_name_plural': 'Engrave Message',
            },
        ),
    ]

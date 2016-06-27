# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20160609_0947'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name': 'Occasion', 'verbose_name_plural': 'Occasions'},
        ),
        migrations.AlterModelOptions(
            name='productimages',
            options={'verbose_name': 'productimage', 'verbose_name_plural': 'Product Images'},
        ),
        migrations.AlterModelOptions(
            name='producttemplate',
            options={'verbose_name': 'producttemplate', 'verbose_name_plural': 'Product Templates'},
        ),
        migrations.AlterModelOptions(
            name='producttemplatedata',
            options={'verbose_name': 'producttemplatedata', 'verbose_name_plural': 'Product Templates Data'},
        ),
        migrations.AlterField(
            model_name='product',
            name='amount',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='sort_order',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='productimages',
            name='sort_order',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='producttemplate',
            name='sort_order',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='producttemplatedata',
            name='default_text',
            field=models.CharField(max_length=50),
        ),
    ]

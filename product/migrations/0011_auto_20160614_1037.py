# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_auto_20160613_1916'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategoryRelation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_id', models.ForeignKey(to='product.Product')),
            ],
        ),
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name': 'Occasion', 'verbose_name_plural': 'Occasions'},
        ),
        migrations.AddField(
            model_name='productcategoryrelation',
            name='productcategory_id',
            field=models.ForeignKey(to='product.ProductCategory'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import champagn.validators


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0025_auto_20160623_1709'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductTemplateDataImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('left', models.IntegerField(default=0)),
                ('top', models.IntegerField(default=0)),
                ('height', models.IntegerField(default=0)),
                ('width', models.IntegerField(default=0)),
                ('default_image', models.ImageField(validators=[champagn.validators.validate_product_image], upload_to=b'product_template_data/', blank=True, help_text=b'Image Size                                      should not more than 300kb.', null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('product_template', models.ForeignKey(related_name='template_data_image', to='product.ProductTemplate')),
            ],
            options={
                'verbose_name': 'product-template-data',
                'verbose_name_plural': 'Product Templates Data',
            },
        ),
        migrations.CreateModel(
            name='ProductTemplateDataText',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('left', models.IntegerField(default=0)),
                ('top', models.IntegerField(default=0)),
                ('height', models.IntegerField(default=0)),
                ('width', models.IntegerField(default=0)),
                ('text', models.CharField(max_length=30, null=True, blank=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('product_template', models.ForeignKey(related_name='template_data_text', to='product.ProductTemplate')),
            ],
            options={
                'verbose_name': 'product-template-data',
                'verbose_name_plural': 'Product Templates Data',
            },
        ),
    ]

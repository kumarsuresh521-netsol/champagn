# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('desc', models.CharField(max_length=500)),
                ('amount', models.CharField(max_length=200)),
                ('capacity', models.IntegerField(max_length=200)),
                ('engaving_msg_price', models.IntegerField(max_length=200)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('logo_image', models.CharField(max_length=200, null=True, blank=True)),
                ('short_description', models.CharField(max_length=200)),
                ('sort_order', models.CharField(max_length=200)),
                ('occasion_start_date', models.DateTimeField(auto_now_add=True)),
                ('occasion_end_date', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=False, help_text=b'Designates whether the App User Device is active or not ')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image_name', models.CharField(max_length=200)),
                ('sort_order', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=False, help_text=b'Designates whether the App User Device is active or not ')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(related_name='product', to='product.Product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image_name', models.CharField(max_length=200)),
                ('sort_order', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=False, help_text=b'Designates whether the App User Device is active or not ')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(related_name='product1', to='product.Product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductTemplateData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('device_type', models.IntegerField(default=0)),
                ('left', models.IntegerField()),
                ('right', models.IntegerField()),
                ('top', models.IntegerField()),
                ('bottom', models.IntegerField()),
                ('height', models.IntegerField()),
                ('width', models.IntegerField()),
                ('default_text', models.CharField(max_length=200)),
                ('default_image', models.CharField(max_length=255, null=True, blank=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(related_name='product_template', to='product.ProductTemplate')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(related_name='product_category', to='product.ProductCategory'),
        ),
    ]

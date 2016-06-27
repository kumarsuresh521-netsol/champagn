# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import champagn.validators


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20160531_1310'),
        ('app', '0002_userdevice'),
    ]

    operations = [
        migrations.CreateModel(
            name='EngravingTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('amount', models.CharField(max_length=100)),
                ('user_shipping_address_id', models.IntegerField()),
                ('user_billing_address_id', models.IntegerField()),
                ('order_status', models.IntegerField()),
                ('payment_status', models.IntegerField()),
                ('image_name', models.ImageField(validators=[champagn.validators.validate_product_image], upload_to=b'user_template_data_images/', blank=True, help_text=b'Image Size                                      should not more than 24Mb.', null=True)),
                ('payment_details', models.CharField(max_length=500)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('qty', models.IntegerField()),
                ('amount', models.CharField(max_length=200)),
                ('template_id', models.IntegerField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(related_name='order_detail', to='app.Order')),
                ('product_id', models.ForeignKey(related_name='product_id', to='product.Product')),
            ],
        ),
        migrations.CreateModel(
            name='OrderEngraving',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order_detail_id', models.IntegerField()),
                ('engraving_template_id', models.IntegerField()),
                ('text', models.CharField(max_length=200)),
                ('image_name', models.CharField(max_length=200)),
                ('amount', models.CharField(max_length=200)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contact_name', models.CharField(max_length=200)),
                ('address_line1', models.CharField(max_length=200)),
                ('address_line2', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('country', models.IntegerField()),
                ('zip', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=30)),
                ('address_type', models.IntegerField()),
                ('is_active', models.BooleanField(default=True, help_text=b'Designates whether                                        this user should be treated as                                        active. Unselect this instead                                        of deleting accounts.')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField()),
                ('product_template_id', models.IntegerField()),
                ('is_active', models.BooleanField(default=False, help_text=b'Designates whether the App User Device is active or not ')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserTemplateData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_template_id', models.IntegerField()),
                ('text', models.CharField(max_length=500)),
                ('image_name', models.ImageField(validators=[champagn.validators.validate_product_image], upload_to=b'user_template_data_images/', blank=True, help_text=b'Image Size                                      should not more than 24Mb.', null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_staff',
        ),
        migrations.AddField(
            model_name='user',
            name='dob',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='useraddress',
            name='user',
            field=models.ForeignKey(related_name='user_address', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(related_name='user_order', to=settings.AUTH_USER_MODEL),
        ),
    ]

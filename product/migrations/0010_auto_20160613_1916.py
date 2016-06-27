# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import champagn.validators


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_auto_20160613_1620'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productcategory',
            options={},
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(to='product.ProductCategory'),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='logo_image',
            field=models.ImageField(help_text=b'Image Size                                      should not more than 24Mb.', upload_to=b'category_images/', validators=[champagn.validators.validate_product_image]),
        ),
        migrations.AlterField(
            model_name='productimages',
            name='image_name',
            field=models.ImageField(help_text=b'Image Size                                      should not more than 24Mb.', upload_to=b'product_images/', validators=[champagn.validators.validate_product_image]),
        ),
        migrations.AlterField(
            model_name='productimages',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='producttemplate',
            name='image_name',
            field=models.ImageField(help_text=b'Image Size                                      should not more than 24Mb.', upload_to=b'product_template_images/', validators=[champagn.validators.validate_product_image]),
        ),
        migrations.AlterField(
            model_name='producttemplate',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='producttemplatedata',
            name='default_image',
            field=models.ImageField(help_text=b'Image Size                                      should not more than 24Mb.', upload_to=b'product_template_data/', validators=[champagn.validators.validate_product_image]),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import champagn.validators


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20160531_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='logo_image',
            field=models.ImageField(validators=[champagn.validators.validate_product_image], upload_to=b'category_images/', blank=True, help_text=b'Image Size                                      should not more than 24Mb.', null=True),
        ),
        migrations.AlterField(
            model_name='productimages',
            name='image_name',
            field=models.ImageField(validators=[champagn.validators.validate_product_image], upload_to=b'product_images/', blank=True, help_text=b'Image Size                                      should not more than 24Mb.', null=True),
        ),
        migrations.AlterField(
            model_name='producttemplate',
            name='image_name',
            field=models.ImageField(validators=[champagn.validators.validate_product_image], upload_to=b'product_template_images/', blank=True, help_text=b'Image Size                                      should not more than 24Mb.', null=True),
        ),
        migrations.AlterField(
            model_name='producttemplatedata',
            name='default_image',
            field=models.ImageField(validators=[champagn.validators.validate_product_image], upload_to=b'product_template_data/', blank=True, help_text=b'Image Size                                      should not more than 24Mb.', null=True),
        ),
    ]

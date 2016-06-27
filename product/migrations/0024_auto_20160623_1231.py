# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc
import champagn.validators


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0023_auto_20160617_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='producttemplate',
            name='template_name',
            field=models.CharField(default=datetime.datetime(2016, 6, 23, 7, 1, 18, 594000, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='logo_image',
            field=models.ImageField(help_text=b'Image Size                                      should not more than 100kb.', upload_to=b'category_images/', validators=[champagn.validators.validate_category_image]),
        ),
        migrations.AlterField(
            model_name='productimages',
            name='image_name',
            field=models.ImageField(help_text=b'Image Size                                      should not more than 300kb.', upload_to=b'product_images/', validators=[champagn.validators.validate_product_image]),
        ),
        migrations.AlterField(
            model_name='producttemplate',
            name='image_name',
            field=models.ImageField(help_text=b'Image Size                                      should not more than 300kb.', upload_to=b'product_template_images/', validators=[champagn.validators.validate_product_image]),
        ),
        migrations.AlterField(
            model_name='producttemplatedata',
            name='default_image',
            field=models.ImageField(validators=[champagn.validators.validate_product_image], upload_to=b'product_template_data/', blank=True, help_text=b'Image Size                                      should not more than 300kb.', null=True),
        ),
    ]

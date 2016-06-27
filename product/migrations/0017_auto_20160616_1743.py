# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import champagn.validators


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0016_auto_20160615_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='producttemplatedata',
            name='default_image',
            field=models.ImageField(validators=[champagn.validators.validate_product_image], upload_to=b'product_template_data/', blank=True, help_text=b'Image Size                                      should not more than 24Mb.', null=True),
        ),
        migrations.AlterField(
            model_name='producttemplatedata',
            name='default_text',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='producttemplatedata',
            name='height',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='producttemplatedata',
            name='left',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='producttemplatedata',
            name='top',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='producttemplatedata',
            name='width',
            field=models.IntegerField(blank=True),
        ),
    ]

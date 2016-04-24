# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0030_auto_20160407_1201'),
    ]

    operations = [
        migrations.RenameField(
            model_name='galleryimages',
            old_name='bill_image',
            new_name='gallery_image',
        ),
        migrations.AlterField(
            model_name='billing',
            name='bill_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 7, 12, 2, 40, 611246)),
        ),
        migrations.AlterField(
            model_name='companybills',
            name='uploaded_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 7, 12, 2, 40, 612825)),
        ),
        migrations.AlterField(
            model_name='customers',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 7, 12, 2, 40, 610106)),
        ),
        migrations.AlterField(
            model_name='galleryimages',
            name='uploaded_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 7, 12, 2, 40, 613356)),
        ),
        migrations.AlterField(
            model_name='stockdetails',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 7, 12, 2, 40, 609299)),
        ),
    ]

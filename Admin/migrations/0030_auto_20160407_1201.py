# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0029_auto_20160406_1635'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryImages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bill_image', models.FileField(upload_to=b'static/static/upload_gallary_images/')),
                ('uploaded_at', models.DateTimeField(default=datetime.datetime(2016, 4, 7, 12, 1, 27, 241497))),
            ],
        ),
        migrations.AlterField(
            model_name='billing',
            name='bill_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 7, 12, 1, 27, 239347)),
        ),
        migrations.AlterField(
            model_name='companybills',
            name='uploaded_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 7, 12, 1, 27, 240832)),
        ),
        migrations.AlterField(
            model_name='customers',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 7, 12, 1, 27, 238186)),
        ),
        migrations.AlterField(
            model_name='stockdetails',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 7, 12, 1, 27, 237304)),
        ),
    ]

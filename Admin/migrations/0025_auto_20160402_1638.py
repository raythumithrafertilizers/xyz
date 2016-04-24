# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0024_auto_20160326_2014'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyBills',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company_name', models.CharField(max_length=300)),
                ('company_invoice_number', models.CharField(max_length=300)),
                ('bill_image', models.FileField(upload_to=b'uploads/')),
                ('uploaded_at', models.DateTimeField(default=datetime.datetime(2016, 4, 2, 16, 38, 55, 617663))),
            ],
        ),
        migrations.AlterField(
            model_name='billing',
            name='bill_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 2, 16, 38, 55, 616370)),
        ),
        migrations.AlterField(
            model_name='customers',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 2, 16, 38, 55, 615247)),
        ),
        migrations.AlterField(
            model_name='stockdetails',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 2, 16, 38, 55, 614573)),
        ),
    ]

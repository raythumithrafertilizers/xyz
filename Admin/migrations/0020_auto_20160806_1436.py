# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0019_auto_20160731_0948'),
    ]

    operations = [
        migrations.CreateModel(
            name='PiadAdvanceDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.FloatField(default=0.0)),
                ('paid_date', models.DateField(default=datetime.date(2016, 8, 6))),
                ('interest_rate', models.FloatField(default=0.0)),
                ('interest_money', models.FloatField(default=0.0)),
                ('farmer_paid_amount', models.FloatField(default=0.0)),
                ('final_total_with_interest', models.FloatField(default=0.0)),
                ('remarks', models.TextField(default=b'')),
            ],
        ),
        migrations.AlterField(
            model_name='advancedetails',
            name='paid_date',
            field=models.DateField(default=datetime.date(2016, 8, 6)),
        ),
        migrations.AlterField(
            model_name='billing',
            name='bill_date',
            field=models.DateField(default=datetime.date(2016, 8, 6)),
        ),
        migrations.AlterField(
            model_name='billing',
            name='month',
            field=models.CharField(default=b'August', max_length=100),
        ),
        migrations.AlterField(
            model_name='soldstockdetails',
            name='created_date',
            field=models.DateField(default=datetime.date(2016, 8, 6)),
        ),
        migrations.AlterField(
            model_name='stockdetails',
            name='month',
            field=models.CharField(default=b'August', max_length=100),
        ),
    ]

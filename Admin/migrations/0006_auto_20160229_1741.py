# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0005_store_wise_stamp_offers_store_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_log',
            name='get_new_stamps',
            field=models.CharField(default=b'---', max_length=10),
        ),
        migrations.AlterField(
            model_name='customer_log',
            name='get_new_stamps_date',
            field=models.CharField(default=b'---', max_length=30),
        ),
        migrations.AlterField(
            model_name='customer_log',
            name='no_of_stamps_reedeemed',
            field=models.CharField(default=b'---', max_length=10),
        ),
        migrations.AlterField(
            model_name='customer_log',
            name='reedeem_date',
            field=models.CharField(default=b'---', max_length=20),
        ),
        migrations.AlterField(
            model_name='store_wise_loyalty',
            name='loyality_card_no',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='store_wise_stamp_offers',
            name='stamp_offer_id',
            field=models.CharField(max_length=100),
        ),
    ]

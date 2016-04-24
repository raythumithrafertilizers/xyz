# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0003_auto_20160222_1732'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stamps_WRT_Bill2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bill_amount', models.CharField(max_length=8)),
                ('no_of_stamps', models.CharField(max_length=6)),
                ('is_active', models.BooleanField(default=False)),
                ('store_id', models.ForeignKey(to='Admin.StoreData')),
            ],
        ),
        migrations.RemoveField(
            model_name='stamps_wrt_bill',
            name='store_id',
        ),
        migrations.DeleteModel(
            name='Stamps_WRT_Bill',
        ),
    ]

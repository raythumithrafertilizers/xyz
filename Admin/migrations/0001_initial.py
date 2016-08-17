# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdvanceDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.FloatField(default=0.0)),
                ('paid_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=400)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('phone', models.CharField(max_length=100)),
                ('person_type', models.CharField(max_length=200)),
                ('isActive', models.BooleanField(default=True)),
                ('address', models.TextField()),
                ('advance_details', models.ManyToManyField(to='Admin.AdvanceDetails')),
            ],
        ),
        migrations.CreateModel(
            name='SoldStockDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.FloatField(default=0.0)),
                ('quality', models.FloatField(default=0.0)),
                ('farmer_rate_per_ton', models.FloatField(default=0.0)),
                ('farmer_payment', models.FloatField(default=0.0)),
                ('farmer_advance', models.FloatField(default=0.0)),
                ('harvester_payment', models.FloatField(default=0.0)),
                ('harvester_advance', models.FloatField(default=0.0)),
                ('harvester_rate_per_ton', models.FloatField(default=0.0)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('farmer', models.ForeignKey(related_name='farmer_data', to='Admin.Person')),
                ('harvester', models.ForeignKey(related_name='harvester_data', to='Admin.Person')),
            ],
        ),
        migrations.CreateModel(
            name='StockDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inital_stock', models.FloatField(null=True)),
                ('available_stock', models.FloatField(default=0.0)),
                ('create_date', models.DateField(auto_now_add=True, null=True)),
                ('month', models.CharField(default=b'June', max_length=100)),
                ('remarks', models.TextField()),
                ('isActive', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='StockNames',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=500)),
                ('isActive', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='stockdetails',
            name='item_name',
            field=models.ForeignKey(to='Admin.StockNames'),
        ),
    ]

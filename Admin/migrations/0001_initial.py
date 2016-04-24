# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessCategories',
            fields=[
                ('categoryId', models.AutoField(serialize=False, primary_key=True)),
                ('categoryName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CityList',
            fields=[
                ('cityId', models.AutoField(serialize=False, primary_key=True)),
                ('cityName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CountryList',
            fields=[
                ('countryId', models.AutoField(serialize=False, primary_key=True)),
                ('countryName', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Customer_Log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.CharField(max_length=15)),
                ('storeId', models.CharField(max_length=20)),
                ('no_of_stamps_reedeemed', models.CharField(default=b'N/A', max_length=10)),
                ('reedeem_date', models.CharField(default=b'N/A', max_length=20)),
                ('get_new_stamps', models.CharField(default=b'N/A', max_length=10)),
                ('get_new_stamps_date', models.CharField(default=b'N/A', max_length=30)),
                ('currentStamp', models.CharField(max_length=20)),
                ('reddemed_stamps_description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='LocalityList',
            fields=[
                ('localityId', models.AutoField(serialize=False, primary_key=True)),
                ('localityName', models.CharField(max_length=100)),
                ('cityId', models.ForeignKey(to='Admin.CityList')),
                ('countryId', models.ForeignKey(to='Admin.CountryList')),
            ],
        ),
        migrations.CreateModel(
            name='LoyaltyCards',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('loyaltyCardId', models.CharField(max_length=50)),
                ('loyaltyCardName', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=False)),
                ('storeId', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MembershipType',
            fields=[
                ('membershipId', models.AutoField(serialize=False, primary_key=True)),
                ('membershipType', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('notification_id', models.AutoField(serialize=False, primary_key=True)),
                ('store_id', models.CharField(max_length=10)),
                ('notification_name', models.CharField(max_length=50)),
                ('notification_description', models.CharField(max_length=500)),
                ('is_active', models.BooleanField(default=False)),
                ('createdDate', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reedeem_And_Get_Log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.CharField(max_length=15)),
                ('storeId', models.CharField(max_length=20)),
                ('no_of_stamps_reedeemed', models.CharField(max_length=10)),
                ('reedeem_date', models.CharField(max_length=20)),
                ('get_new_stamps', models.CharField(max_length=10)),
                ('get_new_stamps_date', models.DateTimeField()),
                ('stamp_validity', models.CharField(max_length=30)),
                ('expire_on', models.CharField(max_length=30)),
                ('totalStamp', models.IntegerField(default=0)),
                ('currentStamp', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='RegularOffers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('offerId', models.CharField(max_length=10)),
                ('offerName', models.CharField(max_length=25)),
                ('shortDesc', models.CharField(max_length=50)),
                ('longDesc', models.CharField(max_length=100)),
                ('offerFrom', models.DateTimeField()),
                ('offerTill', models.DateTimeField()),
                ('offerWeekDays', models.CharField(max_length=50)),
                ('offerTimeRange', models.CharField(max_length=10)),
                ('membershipType', models.ForeignKey(to='Admin.MembershipType')),
                ('storeId', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StampOffers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stampOfferId', models.CharField(max_length=50)),
                ('stampOfferNumber', models.CharField(max_length=10)),
                ('stampOffer', models.CharField(max_length=50)),
                ('shortDesc', models.CharField(max_length=100)),
                ('londDesc', models.CharField(max_length=250)),
                ('offerValidTill', models.DateTimeField()),
                ('storeId', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Stamps_WRT_Bill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bill_amount', models.CharField(max_length=10)),
                ('no_of_stamps', models.CharField(max_length=4)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='StateList',
            fields=[
                ('stateId', models.AutoField(serialize=False, primary_key=True)),
                ('stateName', models.CharField(max_length=50)),
                ('countryId', models.ForeignKey(to='Admin.CountryList')),
            ],
        ),
        migrations.CreateModel(
            name='Store_Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mobile', models.CharField(max_length=12)),
                ('userid', models.CharField(max_length=5)),
                ('store_id', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Store_Wise_Loyalty',
            fields=[
                ('store_id', models.CharField(max_length=10)),
                ('loyality_card_no', models.CharField(max_length=20)),
                ('loyality_id', models.AutoField(serialize=False, primary_key=True)),
                ('max_stamp', models.CharField(max_length=4)),
                ('is_active', models.BooleanField(default=False)),
                ('is_approved', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Store_Wise_Stamp_Offers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stamp_offer_id', models.CharField(max_length=15)),
                ('no_of_stamp', models.CharField(max_length=10)),
                ('stamp_description', models.TextField()),
                ('loyality_id', models.ForeignKey(to='Admin.Store_Wise_Loyalty')),
            ],
        ),
        migrations.CreateModel(
            name='StoreData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('storeName', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('locality', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('latitude', models.CharField(max_length=50)),
                ('langitude', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=100)),
                ('contactName', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=200)),
                ('membershipType', models.CharField(max_length=50)),
                ('store_con_id', models.CharField(max_length=50)),
                ('storeId', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='stamps_wrt_bill',
            name='store_id',
            field=models.ForeignKey(to='Admin.StoreData'),
        ),
        migrations.AddField(
            model_name='localitylist',
            name='stateId',
            field=models.ForeignKey(to='Admin.StateList'),
        ),
        migrations.AddField(
            model_name='citylist',
            name='countryId',
            field=models.ForeignKey(to='Admin.CountryList'),
        ),
        migrations.AddField(
            model_name='citylist',
            name='stateId',
            field=models.ForeignKey(to='Admin.StateList'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0006_auto_20160229_1741'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BusinessCategories',
        ),
        migrations.RemoveField(
            model_name='citylist',
            name='countryId',
        ),
        migrations.RemoveField(
            model_name='citylist',
            name='stateId',
        ),
        migrations.DeleteModel(
            name='Customer_Log',
        ),
        migrations.RemoveField(
            model_name='localitylist',
            name='cityId',
        ),
        migrations.RemoveField(
            model_name='localitylist',
            name='countryId',
        ),
        migrations.RemoveField(
            model_name='localitylist',
            name='stateId',
        ),
        migrations.RemoveField(
            model_name='loyaltycards',
            name='storeId',
        ),
        migrations.DeleteModel(
            name='Notifications',
        ),
        migrations.DeleteModel(
            name='Reedeem_And_Get_Log',
        ),
        migrations.RemoveField(
            model_name='regularoffers',
            name='membershipType',
        ),
        migrations.RemoveField(
            model_name='regularoffers',
            name='storeId',
        ),
        migrations.RemoveField(
            model_name='stampoffers',
            name='storeId',
        ),
        migrations.RemoveField(
            model_name='stamps_wrt_bill2',
            name='store_id',
        ),
        migrations.RemoveField(
            model_name='statelist',
            name='countryId',
        ),
        migrations.DeleteModel(
            name='Store_Customer',
        ),
        migrations.RemoveField(
            model_name='store_wise_stamp_offers',
            name='loyality_id',
        ),
        migrations.RemoveField(
            model_name='storedata',
            name='storeId',
        ),
        migrations.DeleteModel(
            name='CityList',
        ),
        migrations.DeleteModel(
            name='CountryList',
        ),
        migrations.DeleteModel(
            name='LocalityList',
        ),
        migrations.DeleteModel(
            name='LoyaltyCards',
        ),
        migrations.DeleteModel(
            name='MembershipType',
        ),
        migrations.DeleteModel(
            name='RegularOffers',
        ),
        migrations.DeleteModel(
            name='StampOffers',
        ),
        migrations.DeleteModel(
            name='Stamps_WRT_Bill2',
        ),
        migrations.DeleteModel(
            name='StateList',
        ),
        migrations.DeleteModel(
            name='Store_Wise_Loyalty',
        ),
        migrations.DeleteModel(
            name='Store_Wise_Stamp_Offers',
        ),
        migrations.DeleteModel(
            name='StoreData',
        ),
    ]

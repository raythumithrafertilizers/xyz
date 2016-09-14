from django.db import models
from datetime import datetime
import calendar

class AdvanceDetails(models.Model):
	amount = models.FloatField(default=0.0)
	paid_date = models.DateField(default=datetime.now().date())
	interest_rate = models.FloatField(default=0.0)
	interest_money = models.FloatField(default=0.0)
	purchase_id = models.IntegerField(default=0)
	bill_id = models.IntegerField(default=0)
	paid_details_id = models.IntegerField(default=0)
	remarks = models.TextField(default='')
	isCleared= models.BooleanField(default=False)
	cleared_date = models.DateField(null=True, blank=True)


class PiadAdvanceDetails(models.Model):
	amount = models.FloatField(default=0.0)
	farmer_paid_date = models.DateField(default=datetime.now().date())
	interest_rate = models.FloatField(default=0.0)
	interest_money = models.FloatField(default=0.0)
	farmer_paid_amount = models.FloatField(default=0.0)
	final_total_with_interest = models.FloatField(default=0.0)
	paid_farmer_id = models.IntegerField(default=0)
	remarks = models.TextField(default='')


class Expenditures(models.Model):
	amount = models.FloatField(default=0.0)
	create_date = models.DateField(default=datetime.now().date())
	remarks = models.TextField(default='')
	type= models.TextField(default='industrial')
	isActive = models.BooleanField(default=True)



class Person(models.Model):
	name = models.CharField(max_length=400)
	created_date = models.DateTimeField(null=True, auto_now_add=True)
	phone = models.CharField(max_length=100, default='', null=True)
	person_type = models.CharField(max_length=200)
	isActive = models.BooleanField(default=True)
	address = models.TextField(default='')
	advance_details = models.ManyToManyField(AdvanceDetails)


class StockNames(models.Model):
	name = models.CharField(max_length=500)
	isActive = models.BooleanField(default=True)


class SoldStockDetails(models.Model):

	quantity =models.FloatField(default=0.0)
	quality = models.FloatField(default=0.0)

	quantity_in_numbers = models.FloatField(default=0.0)

	farmer_rate_per_ton = models.FloatField(default=0.0)
	farmer_payment = models.FloatField(default=0.0)

	harvester_payment = models.FloatField(default=0.0)
	harvester_rate_per_ton = models.FloatField(default=0.0)

	created_date = models.DateField(default=datetime.now().date())
	farmer = models.ForeignKey(Person, related_name="farmer_data", default='')
	harvester = models.ForeignKey(Person, related_name="harvester_data", default='')
	remarks = models.TextField(default='')
	stock_object = models.ForeignKey(StockNames, default='', null=True)


	miscellaneous_detections = models.FloatField(default=0.0)




class StockDetails(models.Model):

	item_name = models.ForeignKey(StockNames)
	inital_stock = models.FloatField(null=True)
	available_stock = models.FloatField(default= 0.0)
	create_date = models.DateField(null=True)
	month = models.CharField( max_length=100, default=calendar.month_name[int(datetime.now().month)])
	remarks = models.TextField()
	isActive = models.BooleanField(default=True)

class AppendStockDetails(models.Model):
	stock = models.ForeignKey(StockDetails)
	create_date = models.DateField(null=True)
	append_count = models.FloatField(default=0.0)
	total_stock = models.FloatField(default=0.0)
	remarks = models.TextField()
	sold_stock_id = models.IntegerField(default=0)
	manual_create_or_append_stock_id = models.IntegerField(default=0)



class ProductsList(models.Model):
	product = models.ForeignKey(StockDetails,on_delete=models.CASCADE)
	quantity = models.FloatField(null=True)
	per_kg_price = models.FloatField(default=0.0)
	price = models.FloatField(null=True)
	isReturned = models.BooleanField(default=False)

class Billing(models.Model):
	customer = models.ForeignKey(Person, on_delete=models.CASCADE)
	products_list = models.ManyToManyField(ProductsList)
	total_price = models.FloatField(null=True)
	total_paid = models.FloatField(null=True)
	vat_percentage = models.FloatField(default=0.0)
	vat_money = models.FloatField(default=0.0)
	due = models.FloatField(null=True)
	total_quantity = models.FloatField(null=True)
	bill_date = models.DateField(default=datetime.now().date())
	description = models.TextField()
	month = models.CharField(max_length=100, default=calendar.month_name[int(datetime.now().month)])
	remarks = models.TextField(default='')
	vehicle_number = models.TextField(default='')
	contact_number = models.TextField(default='')












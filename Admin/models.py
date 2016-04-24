from django.db import models
from datetime import datetime
import calendar

class StockType(models.Model):
	type_name = models.CharField(max_length=500)

class Quantity(models.Model):
	quantity_name = models.CharField(max_length=500)

class RatePerType(models.Model):
	rate_per_type_name = models.CharField(max_length=500)

class StockDetails(models.Model):
	item_name = models.CharField(max_length=500)
	item_type = models.CharField(max_length=100)

	item_batch_number = models.CharField(max_length=500)
	item_lot_number = models.CharField(max_length= 500)

	expire_date = models.DateField()
	mfg_date = models.DateField(null=True)

	purchase_form = models.TextField()

	quantity_type = models.CharField(max_length=100)
	rate_per_type = models.CharField(max_length=100)

	item_cost = models.FloatField(null=True)
	quantity_weight = models.FloatField(null=True)

	available_stock = models.FloatField(default= 0.0)

	create_date = models.DateTimeField(default= datetime.now())
	isLegal = models.CharField(max_length=100, default='legal')
	month = models.CharField( max_length=100, default=calendar.month_name[int(datetime.now().month)])
	seen = models.BooleanField(default=False)

class Customers(models.Model):

	first_name = models.CharField(max_length=500)
	last_name = models.CharField(max_length=500)

	phone = models.CharField(max_length=30)
	address = models.TextField()
	create_date = models.DateTimeField(default= datetime.now())

class ProductsList(models.Model):
	product = models.ForeignKey(StockDetails,on_delete=models.CASCADE)
	quantity = models.FloatField(null=True)
	price = models.FloatField(null=True)
	isReturned = models.BooleanField(default=False)

class Billing(models.Model):

	customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
	products_list = models.ManyToManyField(ProductsList)

	total_price = models.FloatField(null=True)
	total_paid = models.FloatField(null=True)
	due = models.FloatField(null=True)
	total_quantity = models.FloatField(null=True)
	bill_date = models.DateTimeField(default= datetime.now())
	description = models.TextField()
	month = models.CharField( max_length=100, default=calendar.month_name[int(datetime.now().month)])



class CompanyBills(models.Model):
	company_name = models.CharField(max_length=300)
	company_invoice_number = models.CharField(max_length=300)
	bill_image = models.FileField(upload_to='static/static/uploads/')
	uploaded_at = models.DateTimeField(default=datetime.now())

class GalleryImages(models.Model):
	gallery_image = models.FileField(upload_to='static/static/upload_gallary_images/')
	uploaded_at = models.DateTimeField(default=datetime.now())












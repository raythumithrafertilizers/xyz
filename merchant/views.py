from django.shortcuts import render
from django.views.generic import View
import json
from django.contrib.auth.models import User
from django.conf import settings
import requests
import ast
import datetime
from random import randint

from models import *
from django.http import HttpResponse
from django.core import serializers
from requests_oauthlib import OAuth1
from urlparse import urlparse, parse_qsl
import random, string
from django.contrib.auth import authenticate
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template import Context, RequestContext
from django.template.loader import get_template
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from BaseApp.models import *
from Admin.models import *

def random_key(length):
	key = ''
	for i in range(length):
		key += random.choice(string.lowercase + string.uppercase + string.digits)
	return key

# Create your views here.
class DashBoard(APIView):
	def get(self,request):
		store_id=request.GET['store_id']
		store_customer_count=Store_Customer.objects.filter(store_id=store_id).count()
		

		return Response({'response':int(store_customer_count)},status=200)


class Get_Loyality_List(APIView):
	"""
	Class for getting all the loyality card information 

	"""
	def get(self,request):
		store_id=request.GET['store_id']
		cards=Store_Wise_Loyalty.objects.filter(store_id=store_id)
		card_ser_data=serializers.serialize("json",cards)
		return Response({"card_lis":card_ser_data},status=200)
 
	def post(self,request):
		
		getting_data=request.body.decode("utf-8");
		datas=json.loads(getting_data)
		print datas['store_id'],datas['loyalty_id']
		loyality_obj=Store_Wise_Loyalty.objects.filter(store_id=datas['store_id'],loyality_id=datas['loyalty_id'])
		if len(loyality_obj)>0:
			if loyality_obj[0].is_active==False and loyality_obj[0].is_approved==True:
				loyality_obj.update(is_active=True)
				return Response({'response':"Loyality Card Successfully activated"},status=200)
			elif loyality_obj[0].is_active==True and loyality_obj[0].is_approved==True:
				loyality_obj.update(is_active=False)
				return Response({'response':"Loyality Card Successfully deactivated"},status=200)

class Show_Stamps_Loyalty_Wise(APIView):
	def get(self,request):
		# store_id=request.GET['store_id']
		loyalty_id=request.GET['loyalty_id']
		stamps_in_loyalty=Store_Wise_Stamp_Offers.objects.filter(loyality_id=loyalty_id)
		datas=serializers.serialize("json",stamps_in_loyalty)
		return Response({"response":datas},status=200)

class GET_Current_Stamps_Offer_For_Each_Merchant(APIView):
	def get(self,request):
		if request.GET['store_id']!="":
			data_list=[]
			store_id=request.GET['store_id']
			stamp_data1=Store_Wise_Stamp_Offers.objects.filter(store_id=store_id)
			for i in stamp_data1:
				print i.loyality_id.loyality_id,type(i.loyality_id)
				store_wise_loyal=Store_Wise_Loyalty.objects.filter(loyality_id=i.loyality_id.loyality_id)
				dataa={}
				dataa['loyalitty_id']=store_wise_loyal[0].loyality_card_no
				dataa['stamp_offer_id']=i.stamp_offer_id
				dataa['no_of_stamp']=int(i.no_of_stamp)
				dataa['stamp_description']=i.stamp_description
				dataa['pk']=i.id
				data_list.append(dataa)
			print data_list
			stamp_data=data_list
			# stamp_data=serializers.serialize("json",data_list)
			return Response({"response":stamp_data},status=200)
		else:
			return Response({"Error":"No loyality card created please contact Admin"},status=302)


class Get_Customer_List_For_Merchant(APIView):
	"""This class is responsible for getting all the
		customer of particular store 
	"""
	def get(self,request):
		store_id=request.GET['store_id']
		loyalty_detail=Store_Wise_Loyalty.objects.filter(store_id=store_id,is_active=True,is_approved=True)
		loyalty_detail=serializers.serialize("json",loyalty_detail)
		all_customer=Store_Customer.objects.filter(store_id=store_id)
		if len(all_customer)!=0:
			user_data=serializers.serialize("json",all_customer)
			return Response({"user_list":user_data,'loyalty_detail':loyalty_detail},status=200)
		else:
			return Response({"response":"Error"},status=302)
class Reedeem_Stamps_From_Merchant(APIView):
	def get(self,request):
		customer_id=request.GET['customer_id']
		store_id=request.GET['store_id']
		stamp_idd=request.GET['stamp_id']
		
		getting_stamp_detail=Store_Wise_Stamp_Offers.objects.filter(id=stamp_idd)
		get_number_of_stamp=getting_stamp_detail[0].no_of_stamp
		getting_description_of_stamp=getting_stamp_detail[0].stamp_description
		redeem_obj=Customer_Log.objects.filter(user_id=customer_id,storeId=store_id).order_by('-pk')
		if request.GET['stamp_id']>=redeem_obj[0].currentStamp and redeem_obj[0].currentStamp!=0:
			stamp_after_reedeem=int(redeem_obj[0].currentStamp)-int(getting_stamp_detail[0].no_of_stamp)
			Customer_Log.objects.create(no_of_stamps_reedeemed=getting_stamp_detail[0].no_of_stamp,
				reedeem_date=datetime.now(),currentStamp=stamp_after_reedeem,storeId=store_id,
				reddemed_stamps_description=getting_description_of_stamp,
				user_id=customer_id)
			# Customer_Log.objects.create(user_id=customer_id,storeId=store_id,no_of_stamps_reedeemed=get_number_of_stamp,reedeem_date=datetime.now(),currentStamp=stamp_after_reedeem,reddemed_stamps_description=getting_description_of_stamp)
			return Response({"response":"Successfully redeemed"},status=200)
		else:
			return Response({"response":"no points to redeem"},status=200)
		

class Customer_History_For_Merchant(APIView):
	def get(self,request):
		store_id=request.GET['store_id']
		customer_id=request.GET['customer_id']
		customer_log=Customer_Log.objects.filter(storeId=store_id,user_id=customer_id).order_by('-pk')
		for i in customer_log:
			print i.currentStamp
		dataa=serializers.serialize("json",customer_log)
		return Response({"response":dataa},status=200)

class Add_Customer(APIView):
	"""This class is responsible for creating new user ast
		merchant place
	""" 
	def post(self,request):
		getting_form_value=request.body.decode("-utf-8")
		getting_form_value=json.loads(getting_form_value)
		try:
			chacking_user_exist_or_not=Store_Customer.objects.filter(mobile=str(getting_form_value['mobile']),store_id=str(getting_form_value['store_id']))
			if len(chacking_user_exist_or_not)==0:
				create_customer=Store_Customer.objects.create(mobile=str(getting_form_value['mobile']),store_id=str(getting_form_value['store_id']))
				# create_first_stamp=Reedeem_And_Get_Log.objects.create(user_id=getting_form_value['mobile'],get_new_stamps_date=datetime.now(),storeId=getting_form_value['store_id'],totalStamp=getting_form_value['no_of_stamp'],currentStamp=getting_form_value['no_of_stamp'],stamp_validity=datetime.now()+timedelta(days=365))
				# create_table_for_log=Customer_Log.objects.create(user_id=getting_form_value['mobile'],storeId=getting_form_value['store_id'])
				return Response({'success':'User Created Successfully'},status=200)
			else:
				return Response({'success':'User already Exist'},status=200)
		except Exception as e:
			print e 
			return Response({'Failed':'User already Exist'},status=400)

class Create_Loyality_Request(APIView):
	"""
	This class is responsible for requesting to create loyality
	from admin by merchants
	"""
	def get(self,request):
		store_id=request.GET['store_id']
		getting_store_con_name=StoreData.objects.filter(id=store_id)
		if getting_store_con_name:
			name=getting_store_con_name[0].store_con_id
			loyaltyid=str(name)+"-"+str(randint(1000,9999))
			return Response({'response_get':loyaltyid},status=200)
		else:
			return Response({'Error':"No Store_covention id please contact Administrator"},status=302)

	def post(self,request):
		getting_form_value=request.body.decode("-utf-8")
		getting_form_value=json.loads(getting_form_value)
		print getting_form_value
		# print getting_form_value['stamp_detail']['fields']
		loyalty_obj=Store_Wise_Loyalty.objects.create(loyality_card_no=getting_form_value['loyality_name'],
			store_id=getting_form_value['store_id'],
			max_stamp=getting_form_value['max_stamp'],
			)
		if loyalty_obj:
			for i in range(0,len(getting_form_value['stamp_detail']['fields']),1):
				offer_id=loyalty_obj.loyality_card_no+"-"+str(randint(1000,9999))
				store_wise_stamp=Store_Wise_Stamp_Offers.objects.create(stamp_offer_id=offer_id,loyality_id=loyalty_obj,no_of_stamp=getting_form_value['stamp_detail']['fields'][int(i)],
					stamp_description=getting_form_value['stamp_detail']['values'][int(i)],store_id=store_id)
		return Response({"response":"response"},status=200)


class Get_Stamp_Details(APIView):
	def get(self,request):
		customer_id=request.GET['customer_id']
		store_id=request.GET['store_id']
		loyalty_detail=Store_Wise_Loyalty.objects.filter(store_id=store_id)
		loyaltyid=""
		if loyalty_detail:
			loyaltyid=loyalty_detail[0].loyality_id
		store_customer=Customer_Log.objects.filter(storeId=store_id,user_id=customer_id).order_by('-pk')
		print store_customer
		if len(store_customer)>0:
			current_stamps=store_customer[0].currentStamp
		else:
			current_stamps=0
			# data=serializers.serialize("json",store_customer)
			# return Response({'response':data,'loyalty_detail':loyaltyid},status=200)
		return Response({'response':current_stamps,'loyalty_detail':loyaltyid},status=200)

class Add_Bill_Vs_Stamps(APIView):
	def post(self,request):
		bodyy=request.body.decode("utf-8")
		data=json.loads(bodyy)
		print data
		store_obj=StoreData.objects.get(id=data['store_id'])
		if len(data['bill_vs_stamps_list']['fields'])>0 and len(data['bill_vs_stamps_list']['values'])>0:
			Stamps_WRT_Bill2.objects.create(store_id=store_obj,
			bill_amount=data['bill_amount'],no_of_stamps=data['no_of_stamps'])
			
			list_length=len(data['bill_vs_stamps_list']['fields'])
			for i in range(0,list_length,1):
				Stamps_WRT_Bill2.objects.create(store_id=store_obj,bill_amount=data['bill_vs_stamps_list']['fields'][i],no_of_stamps=data['bill_vs_stamps_list']['values'][i])
			return Response({"response":str(list_length+1)+" entries added"},status=200)
		else:
			Stamps_WRT_Bill2.objects.create(store_id=store_obj,
			bill_amount=data['bill_amount'],no_of_stamps=data['no_of_stamps'])
			return Response({"response":"1 entries added"},status=200)
			

class View_Bill_Vs_Stamps(APIView):
	def get(self,request):
		store_id=request.GET['store_id']
		bill_data=Stamps_WRT_Bill2.objects.filter(store_id=store_id)
		bill_vs_stamp_data=serializers.serialize("json",bill_data)
		return Response({"bill_list":bill_vs_stamp_data},status=200)

	def post(self,request):
		boddyy=request.body.decode("utf-8")
		data=json.loads(boddyy)
		bill_data=Stamps_WRT_Bill2.objects.filter(store_id=data['store_id'],is_active=True)
		bill_vs_stamp_data=serializers.serialize("json",bill_data)
		return Response({"bill_list":bill_vs_stamp_data},status=200)

class Change_Bill_Status(APIView):
	def get(self,request):
		store_id=request.GET['store_id']
		bill_id=request.GET['bill_id']
		change_stamp_data=Stamps_WRT_Bill2.objects.filter(id=bill_id,store_id=store_id)
		if change_stamp_data[0].is_active==False:
			change_stamp_data.update(is_active=True)
			return Response({"response":"Status changed to acive"},status=200)
		elif change_stamp_data[0].is_active==True:
			change_stamp_data.update(is_active=False)
			return Response({"response":"Status changed to Inactive"},status=200)

	def post(self,request):
		boddyy=request.body.decode("utf-8")
		data=json.loads(boddyy)
		rem_data=Stamps_WRT_Bill2.objects.filter(id=data['bill_id'],store_id=data['store_id'])
		if rem_data:
			rem_data.delete()
			return Response({"response":"Bill detail Successfully removed"},status=200)

class Get_Stamp_Corresponding_To_Bill(APIView):
	def get(self,request):
		amount=request.GET['amount']
		store_id=request.GET['store_id']
		stamp_amount=Stamps_WRT_Bill2.objects.filter(is_active=True,store_id=store_id)
		price_list=[]
		for i in stamp_amount:
			price_list.append(i.bill_amount)
		return Response({"response":"Done"})

class Add_Stamp(APIView):
	def post(self,request):
		boddyy=request.body.decode("utf-8")
		data=json.loads(boddyy)
		getting_current_balance=Customer_Log.objects.filter(user_id=data['customer_id']).order_by('-pk')
		if len(getting_current_balance)>0:
			balance=int(getting_current_balance[0].currentStamp)+int(data['amount'])
			create_table_for_log=Customer_Log.objects.create(user_id=data['customer_id'],storeId=data['store_id'],get_new_stamps=data['amount'],get_new_stamps_date=datetime.now(),currentStamp=balance)
			return Response({'response':'Stamps Added successfully'})
		else:
			create_table_for_log=Customer_Log.objects.create(user_id=data['customer_id'],storeId=data['store_id'],get_new_stamps=data['amount'],get_new_stamps_date=datetime.now(),currentStamp=data['amount'])
			return Response({'response':'Starmps added successfully'})
		


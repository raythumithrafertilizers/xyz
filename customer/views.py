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


class Dashboard(APIView):
	def get(self,request):
		try:
			user_obj=UserDetails.objects.get(userKey_id=request.GET['user_id'])
			user_det=User.objects.get(id=request.GET['user_id'])
			user_data={}
			user_data['fullname']=user_det.first_name+ " " +user_det.last_name
			user_data['email']=user_det.email			
			user_data['phone']=user_obj.phone
			stamps_data = Customer_Log.objects.filter(user_id = str(user_obj.phone)).order_by("-pk")
			print "stampsdata: ", stamps_data[0].currentStamp
			user_data['currentstamp']= 0
			user_data['totalstamp']= 0
			all_atore_ids=Store_Customer.objects.filter(mobile=user_obj.phone)			
			store_list=[]
			for store in all_atore_ids:
				store_data={}
				store_details=StoreData.objects.filter(id=store.store_id)
				store_data=serializers.serialize("json",store_details)
				store_list.append(store_data)
			return Response({"user_details":user_data,"store_list":store_list},status=200)
		except Exception as e:
			return Response({"failed":"something went wrong"},status=401)


class StoreOffers(APIView):
	"""fetching Offers of respective store"""
	def get(self, request):
		storeid = request.GET['storeid']
		try:
			loyaltyobj = Store_Wise_Loyalty.objects.get(store_id = int(storeid), is_active = True)
			loyaltyoffersobj = Store_Wise_Stamp_Offers.objects.filter(loyality_id = loyaltyobj)
			loyaltycard =  serializers.serialize('json', [loyaltyobj])
			loyaltyoffers = serializers.serialize('json', loyaltyoffersobj)
			return Response({"loyaltycard": loyaltycard, "loyaltyoffers": loyaltyoffers}, status=200)
		except Exception, e:
			return Response({"response":"no data found"}, status = 401)



		
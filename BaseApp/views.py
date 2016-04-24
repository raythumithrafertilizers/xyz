from django.shortcuts import render
from django.views.generic import View
import json
from django.contrib.auth.models import User
from django.conf import settings
import requests
import ast
from models import *
from django.http import HttpResponse
from django.core import serializers
#from requests_oauthlib import OAuth1
from urlparse import urlparse, parse_qsl
import random, string
from django.contrib.auth import authenticate
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template import Context, RequestContext
from django.template.loader import get_template
#from push_notifications.models import APNSDevice, GCMDevice
# Create your views here.

def random_key(length):
	key = ''
	for i in range(length):
		key += random.choice(string.lowercase + string.uppercase + string.digits)
	return key



def json_response(response_dict, status=200):
	response = HttpResponse(json.dumps(response_dict),
							content_type="application/json", status=status)
	response['Access-Control-Allow-Origin'] = '*'
	response['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
	return response



class UserRegistration(View):
	"""User Registration"""

	def get(self, request):
		return HttpResponse("method not allowed")

	def post(self, request):
		body_unicode = request.body.decode('utf-8')
		body = json.loads(body_unicode)
		try:
			user = User.objects.get(email = str(body['email']))
			return json_response({"err" : "User already exists with this email id"}, status=401)
		except Exception, e:
			user = User.objects.create_user(str(body['email']), str(body['email']), str(body['password']))
			user.first_name = body['firstname']
			user.last_name = body['lastname']
			userobj = UserDetails()
			userobj.userKey = user
			userobj.phone =  str(body['phone'])
			act_code = random_key(16)
			userobj.activationCode =  str(act_code)
			userobj.role = "admin"
			userobj.save()
			user.save()

			content = Context({"firstname": str(body['firstname']), "lastname" : str(body['lastname']) ,"email": str(body['email']), "activationcode": act_code})
			pwdtemplate = get_template('registeremail.html')
			htmlt = pwdtemplate.render(content)
			to = [str(body['email'])]
			by = "no-reply@basemodule.me"
			subject = "Account Activation"
			msg = EmailMultiAlternatives(subject, "", by, to)
			msg.attach_alternative(htmlt, "text/html")
			msg.send()
			return json_response({"response":"success"}, status=200)


class UserLogin(View):
	"""User login class"""
	def get(self, request):
		print "fbsdbgbfj"
		return HttpResponse("method not allowed")

	def post(self, request):
		print "in login post"
		try:

			body_unicode =  request.body.decode('utf-8')
			body = json.loads(body_unicode)
			print body
			user =  authenticate(username = str(body['email']), password = str(body['password']))
			print user
			if user is not None:
				print user.is_active
				if user.is_active:
					userobj = UserDetails.objects.get(userKey = user)

					token, created  =  Token.objects.get_or_create(user = user)
					return json_response({"token":token.token, "role":userobj.role,"store_id":user.id}, status=200)
				else:
					return json_response({"response":"User is not active"}, status=401)
			else:
				return json_response({"response":"Invalid login credentials"}, status=401)
		except Exception as e:
			print e
			return HttpResponse('something went wrong..')
		



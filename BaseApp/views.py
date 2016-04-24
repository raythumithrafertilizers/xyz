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
from requests_oauthlib import OAuth1
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


class FacebookLogin(View):

	# def get(self, request):
	#     print "in get method"
	#     return HttpResponse("method not allowed")

	def post(self, request):
		body = json.loads(request.body)
		access_token_url = 'https://graph.facebook.com/v2.3/oauth/access_token'
		graph_api_url = 'https://graph.facebook.com/v2.3/me'
		params = {
			'client_id': body['clientId'],
			'redirect_uri': body['redirectUri'],
			'client_secret': settings.FACEBOOK_API_SECRET,
			'code': body['code']
		}

		# Step 1. Exchange authorization code for access token.
		r = requests.get(access_token_url, params=params)
		access_token = ast.literal_eval(r.text)
		print "access_token:", access_token

		# Step 2. Retrieve information about the current user.
		r = requests.get(graph_api_url, params=access_token)
		profile = json.loads(r.text)
		print profile

		print "adfasf: ", request.META.get('HTTP_AUTHORIZATION', '')

		user = User.objects.filter(username=profile['id'])

		if user:
			print "user found"
			token, created = Token.objects.get_or_create(user=user[0])
			return json_response({"token": token.token, "profile": serializers.serialize("json", user)}, status=200)

		if not user:
			userobj = User()
			userobj.username = profile['id']
			userobj.first_name = profile['first_name']
			userobj.last_name = profile['last_name']
			userobj.email = profile['email']
			userobj.save()
			user = User.objects.filter(email=profile['email'])
			token, created = Token.objects.get_or_create(user=user[0])
			return json_response({"token": token.token, "profile": serializers.serialize("json", user)}, status=200)


class Google(View):

	def get(self, request):
		print "in get method"
		return HttpResponse("method not allowed")

	def post(self, request):
		body = json.loads(request.body)

		access_token_url = 'https://accounts.google.com/o/oauth2/token'
		people_api_url = 'https://www.googleapis.com/plus/v1/people/me/openIdConnect'

		payload = dict(client_id=body['clientId'],
					   redirect_uri=body['redirectUri'],
					   client_secret=settings.GOOGLE_SECRET,
					   code=body['code'],
					   grant_type='authorization_code')

		# Step 1. Exchange authorization code for access token.
		r = requests.post(access_token_url, data=payload)
		token = json.loads(r.text)
		headers = {'Authorization': 'Bearer {0}'.format(token['access_token'])}
		# print "access_token:", headers

		# Step 2. Retrieve information about the current user.
		r = requests.get(people_api_url, headers=headers)
		profile = json.loads(r.text)
		print "user profile: ", profile

		user = User.objects.filter(username=str(profile['sub']))
		print "user data: ", user

		if user:
			print "user found"
			token, created = Token.objects.get_or_create(user=user[0])
			return json_response({"token": token.token, "profile": serializers.serialize("json", user)}, status=200)

		if not user:
			print "user not found"
			userobj = User()
			userobj.username = str(profile['sub'])
			userobj.first_name = str(profile['given_name'])
			userobj.last_name = str(profile['family_name'])
			userobj.email = str(profile['email'])
			userobj.save()
			user = User.objects.filter(email=str(profile['email']))
			token, created = Token.objects.get_or_create(user=user[0])
			return json_response({"token": token.token, "profile": serializers.serialize("json", user)}, status=200)


class Twitter(View):

	def post(self, request):
		body = json.loads(request.body)
		request_token_url = 'https://api.twitter.com/oauth/request_token'
		access_token_url = 'https://api.twitter.com/oauth/access_token'

		if body.get("oauth_token") and body.get("oauth_verifier"):
			print "in auth"
			auth = OAuth1(settings.TWITTER_CONSUMER_KEY,
						  client_secret=settings.TWITTER_CONSUMER_SECRET,
						  resource_owner_key=body.get('oauth_token'),
						  verifier=request.json.get('oauth_verifier')
						  )
			r = requests.post(access_token_url, auth=auth)
			profile = dict(parse_qsl(r.text))

			print "twitter profile: ", profile

			user = User.objects.filter(username=profile['user_id'])
			if user:
				token, created = Token.objects.get_or_create(user=user[0])
				return json_response(
					{"token": token.token,
					 "profile": serializers.serialize("json", user[0])},
					status=200)

			# else:
			#     userobj = User()
			#     userobj.username = str(profile['user_id'])
			#     userobj.first_name

		else:
			print "no auth"
			oauth = OAuth1(settings.TWITTER_CONSUMER_KEY,
						   client_secret=settings.TWITTER_CONSUMER_SECRET,
						   callback_uri=settings.TWITTER_CALLBACK_URL
						   )
			r = requests.post(request_token_url, auth=oauth)
			oauth_token = dict(parse_qsl(r.text))
			# print oauth_token['oauth_token']
			return json_response({"token": oauth_token['oauth_token']}, status=200)


class LinkedIn(View):

	def get(self, request):
		print "in get method"
		return HttpResponse("method not allowed")

	def post(self, request):
		body = json.loads(request.body)
		access_token_url = 'https://www.linkedin.com/uas/oauth2/accessToken'
		people_api_url = 'https://api.linkedin.com/v1/people/~:(id,first-name,last-name,email-address)'

		payload = dict(client_id=body['clientId'],
					   redirect_uri=body['redirectUri'],
					   client_secret=settings.LINKEDIN_SECRET,
					   code=body['code'],
					   grant_type='authorization_code')
		# Step 1. Exchange authorization code for access token.
		r = requests.post(access_token_url, data=payload)
		access_token = json.loads(r.text)
		params = dict(oauth2_access_token=access_token[
					  'access_token'], format='json')

		# Step 2. Retrieve information about the current user.
		r = requests.get(people_api_url, params=params)
		profile = json.loads(r.text)

		user = User.objects.filter(username=str(profile['id']))

		if user:
			token, created = Token.objects.get_or_create(user=user[0])
			return json_response({"token": token.token, "profile": serializers.serialize("json", user)}, status=200)

		if not user:
			userobj = User()
			userobj.username = str(profile['id'])
			userobj.first_name = str(profile['firstName'])
			userobj.last_name = str(profile['lastName'])
			userobj.email = str(profile['emailAddress'])
			userobj.save()
			user = User.objects.filter(username=str(profile['id']))
			token, created = Token.objects.get_or_create(user=user[0])
			return json_response({"token": token.token, "profile": serializers.serialize("json", user)}, status=200)


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
		



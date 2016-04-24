"""from django.shortcuts import render
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
import random
import string
from django.contrib.auth import authenticate
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template import Context, RequestContext
from django.template.loader import get_template
from rest_framework.renderers import JSONRenderer
import random
from BaseApp.models import *
from rest_framework.parsers import JSONParser"""
from rest_framework.response import Response
from rest_framework.views import APIView
from BaseApp.views import *
from django.db.models import Q
import datetime
from django.db.models import Sum, Count
from BaseModule.settings import *
import os



class GetStock(APIView):
    """docstring for ClassName"""

    def get(self, request):
        try:
            stocklist = StockDetails.objects.all()
            stockslist = serializers.serialize('json', stocklist)
            return Response({"stockslist": stockslist}, status=200)
        except Exception as e:
            print e
            return Response({"stockslist": e}, status=200)

class EditStock(APIView):

    def get(self, request):
        stockId = request.GET['stockId']
        print "stockId: ", stockId
        try:
            # fetching stock data and serializing it
            stockobj = StockDetails.objects.get(id=int(stockId))
            stockdata = serializers.serialize("json", [stockobj])

            return Response({"stockdata": stockdata}, status=200)
        except Exception, e:
            return Response({"response": "no data found"}, status=401)

    def post(self, request):
        """ Here we are checking for the existing stock data if exists we update else throw and error """
        body = request.body.decode("utf-8")
        body = json.loads(body)
        try:

            stock = StockDetails.objects.get(id = str(body['stockdata']['stockId']))

            expired_converted_date = datetime.datetime.strptime(str(body['stockdata']['expired_date']),"%d/%m/%Y").date()

            stock.item_name = body['stockdata']['stock_name']

            stock.item_type = body['stockdata']['stockType']

            stock.expire_date = expired_converted_date



            if 'isLegal' in body['stockdata']:
                print 'yes isLeagal',
                stock.isLegal = body['stockdata']['isLegal']

            if 'batch_number' in body['stockdata']:
                stock.item_batch_number = body['stockdata']['batch_number']
            if 'lot_number' in body['stockdata']:
                stock.item_lot_number = body['stockdata']['lot_number']

            if 'quantity' in body['stockdata']:
                stock.quantity_type = body['stockdata']['quantity']
            if 'quantity_rate' in body['stockdata']:
                stock.rate_per_type = body['stockdata']['quantity_rate']

            if 'quantity_count' in body['stockdata']:
                stock.quantity_weight = body['stockdata']['quantity_count']
            if 'rate' in body['stockdata']:
                stock.item_cost = body['stockdata']['rate']

            if 'mfg_date' in body['stockdata']:
                stock.mfg_date = datetime.datetime.strptime(str(body['stockdata']['mfg_date']),"%d/%m/%Y").date()

            if 'purchase_from' in body['stockdata']:
                stock.purchase_form = body['stockdata']['purchase_from']

            stock.save()

            return Response({"response": "Datasaved successfully"}, status=200)
        except Exception, e:
            print e
            return Response({"response": "no data found"}, status=401)


class EditUsers(APIView):

    def get(self, request):
        return Response({"response": "method not allowed "}, status=405)
    def post(self, request):
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            user = User.objects.get(id = str(body['user_id']))
            print body, '------------'
            if 'first_name' in body:
                user.first_name = body['first_name']
                print 'first name'

            if 'last_name' in body:
                user.last_name = body['last_name']
                print 'last name'


            if 'password' in body:
                user.set_password(body['password'])
                print 'password '

            user.save()
            if 'phone' in body:
                userDetailsObject = UserDetails.objects.get(userKey = user)
                userDetailsObject.phone = body['phone']
                print 'phone '
                userDetailsObject.save()


            return json_response({"status" : "successfully updated"}, status=200)
        except Exception as e:
            print e
            return json_response({"err" : "No User Found"}, status=401)

class EditCustomer(APIView):

    def get(self, request):
        return Response({"response": "method not allowed "}, status=405)
    def post(self, request):
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            user = Customers.objects.get(id = str(body['user_id']))
            print body, '------------'
            if 'first_name' in body:
                user.first_name = body['first_name']
                print 'first name'

            if 'last_name' in body:
                user.last_name = body['last_name']
                print 'last name'


            if 'address' in body:
                user.address = body['address']
                print 'password '


            if 'phone' in body:
                user.phone = body['phone']

            user.save()


            return json_response({"status" : "successfully updated"}, status=200)
        except Exception as e:
            print e
            return json_response({"err" : "No User Found"}, status=401)


class DeleteStock(APIView):

    def get(self, request):
        return Response({"response": "method not allowed "}, status=405)

    def post(self, request):
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            print body,'============='
            stockdata = StockDetails.objects.get(id = str(body['stockId']))
            stockdata.delete()
            return json_response({"status" : "successfully deleted"}, status=200)
        except Exception as e:
            print e
            return json_response({"err" : "No Stock Found"}, status=401)

class DeleteUser(APIView):

    def get(self, request):
        return Response({"response": "method not allowed "}, status=405)

    def post(self, request):
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            print body,'============='
            userdata = User.objects.get(id = str(body['user_id']))
            print userdata.id, userdata.first_name
            userdata.delete()
            return json_response({"status" : "successfully deleted"}, status=200)
        except Exception as e:
            print e
            return json_response({"err" : "No User Found"}, status=401)

class DeleteCustomer(APIView):

    def get(self, request):
        return Response({"response": "method not allowed "}, status=405)

    def post(self, request):
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            print body,'============='
            userdata = Customers.objects.get(id = str(body['user_id']))
            userdata.delete()
            return json_response({"status" : "successfully deleted"}, status=200)
        except Exception as e:
            print e
            return json_response({"err" : "No User Found"}, status=401)

class AddCustomer(View):

    def get(self, request):
        return HttpResponse("method not allowed")

    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        try:
            user = Customers.objects.get(phone = str(body['phone']))
            return json_response({"err" : "User already exists with this email id"}, status=401)
        except Exception, e:
            print e
            user = Customers(phone=body['phone'],
                             first_name = body['firstname'])
            if 'lastname' in body:
                user.last_name = body['lastname']
            if 'address' in body:
                user.address = body['address']
            user.save()
            return json_response({"response":"success"}, status=200)

class BillManagement(View):

    def get(self, request):
        try:

            # if billId is given return bill details
            if 'billId' in request.GET:
                print
                data = Billing.objects.get(id = request.GET['billId'])


                temp_data = data.products_list.all()
                product_list = []

                for temp in temp_data:
                    obj = {}
                    obj['product_name'] = temp.product.item_name
                    obj['product_id'] = temp.product.id
                    obj['product_price'] =temp.price
                    obj['product_quantity'] = temp.quantity
                    obj['bill_product_id'] = temp.id
                    obj['isReturned'] = temp.isReturned
                    product_list.append(obj)


                customers = serializers.serialize('json', Customers.objects.all())
                bill_info = serializers.serialize('json', [data])
                return json_response({"bill_info": bill_info, 'product_list': product_list, 'customers': customers}, status=200)

            # if customer Id is given return customer all bills
            elif 'customerId' in request.GET:
                customer = Customers.objects.get(id = request.GET['customerId'])
                data = Billing.objects.filter(customer = customer)
                bills_list = serializers.serialize('json', data)

                return json_response({"bills_list": bills_list}, status=200)

            else:
                return json_response({"response": 'customerid or bill id not found'}, status=400)


        except Exception as e:
            print e
            return HttpResponse({"response": e}, status=400)

    def put(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        try:
            # update the return, re-return status
            if 'status' in body:
                data = ProductsList.objects.get(id = body['bill_product_number'])
                data.isReturned = body['status']
                data.save()
                return json_response({"response":'successfully updated'}, status=200)
            else:

                # save related product information of specific bill
                for temp in body['product_details']:
                    data = ProductsList.objects.get(id = temp['bill_product_number'])
                    data.quantity = temp['product_quantity']
                    data.price = temp['product_price']
                    data.save()

                # save billing information
                customer = Customers.objects.get(id = body['bill_details']['customerId'])
                data = Billing.objects.get(id = body['bill_details']['bill_id'])
                data.customer = customer
                data.total_price = float(body['bill_details']['price'])
                data.total_quantity= float(body['bill_details']['quantity'])
                data.due = float(body['bill_details']['due'])
                data.total_paid = float(body['bill_details']['paid'])
                data.save()

                return json_response({"response":'successfully updated'}, status=200)
        except Exception, e:
            print e
            return json_response({"response":"failed to update"}, status=400)

    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        try:
            listOfProducts = []
            for temp in body['products']:
                print temp['id'], '========'
                prdct = ProductsList(price=temp['price'], quantity = temp['quantity'])
                specific_stock = StockDetails.objects.get(id = temp['id'])
                prdct.product = specific_stock
                prdct.save()
                listOfProducts.append(prdct)
                specific_stock.available_stock -= int(temp['quantity'])
                specific_stock.save()

            billingObject = Billing(due = body['due'])
            billingObject.total_paid = body['amount_paid']
            billingObject.total_quantity = body['total_quantity']
            billingObject.total_price = body['total_price']
            billingObject.customer = Customers.objects.get(id = body['customerId'])
            billingObject.save()
            billingObject.products_list.add(*listOfProducts)
            billingObject.save()

            print listOfProducts
            return HttpResponse('hellow')
        except Exception, e:
            print e
            return json_response({"response":"failed"}, status=401)



def deleteBill(request):
    try:
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        if 'bill_id' in body:
            bill = Billing.objects.get(id = str(body['bill_id']))
            bill.delete()
            return json_response({"status" : "successfully deleted"}, status=200)
        else:
            customer = Customers.objects.get(id = body['customer_id'])
            data = Billing.objects.filter(customer = customer).delete()
            return json_response({"status" : "successfully deleted"}, status=200)


    except Exception as e:
        print e
        return json_response({"err" : "No Stock Found"}, status=401)

def deleteCompanyBill(request):
    try:
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        bill = CompanyBills.objects.get(id = str(body['bill_id']))
        os.remove(BASE_DIR+'/'+str(bill.bill_image))
        bill.delete()
        return json_response({"status" : "successfully deleted"}, status=200)

    except Exception as e:
        print e
        return json_response({"err" : "No Stock Found"}, status=401)



class CompanyBillsManagement(View):

    def get(self, request):
        try:
            company_bills1 = CompanyBills.objects.all()
            company_bills = serializers.serialize('json', company_bills1)
            return json_response({"bills_list": company_bills}, status=200)
        except Exception as e:
            print e
            return Response({"stockslist": e}, status=405)

    def post(self, request):
        try:

            file_name = ''
            try:

                for filename, file in request.FILES.iteritems():
                    file_name = request.FILES[filename]

                data = json.loads(json.dumps(request.POST))
                if 'bill_id' in request.POST:
                    print 'yes update'
                    companyBill = CompanyBills.objects.get(id = data['bill_id'])
                    companyBill.company_name = data['company_name']
                    companyBill.company_invoice_number = data['company_invoice']
                    if file_name:
                        print 'yes pic'
                        companyBill.bill_image = file_name
                    companyBill.save()
                    return json_response({"response" : "data updated successfully"}, status=200)
                else:
                    companyBill = CompanyBills(company_name = data['company_name'])
                    companyBill.company_invoice_number = data['company_invoice']
                    companyBill.bill_image = file_name
                    companyBill.save()
                    return json_response({"response" : "data saved successfully"}, status=200)
            except Exception as e:
                print e
                return json_response({"error" : "unable to process data"}, status=200)
        except Exception as e:
            json_response({"err" : "User already exists with this email id"}, status=401)

    def put(self, request):
        try:

            file_name = ''
            try:

                for filename, file in request.FILES.iteritems():
                    file_name = request.FILES[filename]


                from django.http import QueryDict
                qd = QueryDict(request.body)
                put_dict = {k: v[0] if len(v)==1 else v for k, v in qd.lists()}
                print put_dict
                """"""
                return json_response({"response" : "data saved successfully"}, status=200)
            except Exception as e:
                print e
                return json_response({"error" : "unable to process data"}, status=405)
        except Exception as e:
            json_response({"err" : "User already exists with this email id"}, status=401)

class AddUser(View):
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
			userobj.role = "subadmin"
			userobj.save()
			user.save()

			"""content = Context({"firstname": str(body['firstname']), "lastname" : str(body['lastname']) ,"email": str(body['email']), "activationcode": act_code})
			pwdtemplate = get_template('registeremail.html')
			htmlt = pwdtemplate.render(content)
			to = [str(body['email'])]
			by = "no-reply@basemodule.me"
			subject = "Account Activation"
			msg = EmailMultiAlternatives(subject, "", by, to)
			msg.attach_alternative(htmlt, "text/html")
			msg.send()"""
			return json_response({"response":"success"}, status=200)



class AddStock(View):
    def get(self, request):
        return HttpResponse("method not allowed")
    def post(self, request):
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            print body

            expired_converted_date = datetime.datetime.strptime(str(body['stockdata']['expired_date']),"%d/%m/%Y").date()

            stock = StockDetails(item_name = body['stockdata']['stock_name'],
                                 item_type= body['stockdata']['stock_type']['name'],
                                 expire_date = expired_converted_date)

            if 'isLegal' in body['stockdata']:
                stock.isLegal = body['stockdata']['isLegal']['name']

            if 'batch_number' in body['stockdata']:
                stock.item_batch_number = body['stockdata']['batch_number']
            if 'lot_number' in body['stockdata']:
                stock.item_lot_number = body['stockdata']['lot_number']

            if 'quantity' in body['stockdata']:
                stock.quantity_type = body['stockdata']['quantity']['name']
            if 'quantity_rate' in body['stockdata']:
                stock.rate_per_type = body['stockdata']['quantity_rate']['name']

            if 'quantity_count' in body['stockdata']:
                stock.quantity_weight = float(body['stockdata']['quantity_count'])
                stock.available_stock = float(body['stockdata']['quantity_count'])

            if 'rate' in body['stockdata']:
                stock.item_cost = body['stockdata']['rate']

            if 'mfg_date' in body['stockdata']:
                stock.mfg_date = datetime.datetime.strptime(str(body['stockdata']['mfg_date']),"%d/%m/%Y").date()

            if 'purchase_from' in body['stockdata']:
                stock.purchase_form = body['stockdata']['purchase_from']

            stock.save()

            return json_response({"err" : "User already exists with this email id"}, status=200)
        except Exception as e:
            print e
            return json_response({"response":"success"}, status=405)


class GetUsersData(APIView):
    """fetching all customer data"""
    def get(self, request):
        users = UserDetails.objects.filter(Q(role = "admin") | Q(role = "subadmin"))
        userlist  = []
        for user in users:
            data ={}
            data['firstname'] = user.userKey.first_name
            data['lastname'] =  user.userKey.last_name
            data['email'] =  user.userKey.email
            data['phone'] = user.phone
            data['userid'] = user.id
            userlist.append(data)

        user_basic_data = json.dumps(userlist)
        return Response({'userdata' : user_basic_data}, status = 200)

class GetCustomerData(APIView):
    """fetching all customer data"""
    def get(self, request):
        try:
            users = Customers.objects.all()
            userlist  = []
            for user in users:
                data ={}
                data['firstname'] = user.first_name
                data['lastname'] =  user.last_name
                data['address'] =  user.address
                data['phone'] = user.phone
                data['userid'] = user.id
                userlist.append(data)

            user_basic_data = json.dumps(userlist)
            return Response({'userdata' : user_basic_data}, status = 200)
        except Exception as e:
            print e
            return Response({'error' : 'got error'}, status = 405)

class UserData(APIView):
    """fetching data of respective user"""

    def get(self, request):
        return Response({"response": "method not allowed"}, status=401)

    def post(self,request):
        body = request.body
        body = json.loads(body)
        print "userid:", body['userid']

        try:
            userdata =  UserDetails.objects.get(id = int(body['userid']))
            user_total_details =  {
            "firstname" : userdata.userKey.first_name,
            "lastname" : userdata.userKey.last_name,
            "email" :  userdata.userKey.email,
            "phone" : userdata.phone,
            }

            return Response({"userdata": json.dumps(user_total_details)}, status = 200)
        except Exception, e:
            return Response({"response": "userdata not found"},status = 401)

class CustomerData(APIView):
    """fetching data of respective user"""

    def get(self, request):
        return Response({"response": "method not allowed"}, status=401)
    def post(self, request):
        body =  request.body
        body =  json.loads(body)
        print "userid:", body['userid']

        try:
            userdata =  Customers.objects.get(id = int(body['userid']))
            user_total_details = {
                "firstname" : userdata.first_name,
                "lastname" : userdata.last_name,
                "address" :  userdata.address,
                "phone" : userdata.phone,
            }

            return Response({"userdata": json.dumps(user_total_details)}, status = 200)
        except Exception, e:
            return Response({"response": "userdata not found"},status = 405)

class GraphData(View):
    def get(self, request):
        return HttpResponse("method not allowed")

    def post(self, request):
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            if 'get_products_quantity' in body:
                print 'yes  in body'
                stocklist = StockDetails.objects.all()
                stockslist = serializers.serialize('json', stocklist)

                return json_response({"stockslist": stockslist}, status=200)

            elif 'paid_unpaid_month_wise' in body:
                print 'yes  in body paid_unpaid_month_wise'
                data = Billing.objects.values('month')\
                    .annotate(paid=Sum('total_paid'), due=Sum('due'), total_price=Sum('total_price'))

                final_data = []
                for temp in data:
                    obj = {}
                    obj['month'] = temp['month']
                    obj['paid']  = temp['paid']
                    obj['due'] = temp['due']
                    obj['total_price'] = temp['total_price']
                    final_data.append(obj)
                return json_response({"stockslist": final_data}, status=200)

            elif 'customers_credit_debit' in body:


                bills = Billing.objects.values('customer').annotate(paid=Sum('total_paid'), due=Sum('due'), total_price = Sum('total_price'))
                dummy_data = []
                for temp in bills:
                    obj = {}
                    customer_info = Customers.objects.filter(id = temp['customer'])
                    customer_information = serializers.serialize('json', customer_info)
                    customer_information = json.loads(customer_information)
                    name = customer_information[0]['fields']['first_name']+" "+customer_information[0]['fields']['last_name']
                    obj['total_price'] = temp['total_price']
                    obj['due'] = temp['due']
                    obj['paid'] = temp['paid']
                    obj['customer_name'] = name
                    dummy_data.append(obj)

                return json_response({'bills': dummy_data}, status=200)

            elif 'low_quantity_avaible_products' in body:

                try:
                    stocks = StockDetails.objects.all().order_by('available_stock').values_list('item_name','available_stock')
                    dummy_data = []
                    for temp in stocks:
                        obj = {}
                        obj['stock_name'] = temp[0]
                        obj['available_stock'] = temp[1]
                        dummy_data.append(obj)
                    return json_response({'stock': dummy_data}, status=200)
                except Exception as e:
                    print e
                    return json_response({'error': e}, status=405)

            elif 'counts_number' in body:

                try:
                    total_sold_quantity = StockDetails.objects.all().aggregate(total_quantiy=Sum('quantity_weight') - Sum('available_stock'))['total_quantiy']
                    paid_due = Billing.objects.all().aggregate(total_paid=Sum('total_paid'), due =  Sum('due'))
                    total_stock = StockDetails.objects.all()

                    total_sold_price = 0
                    for temp in total_stock:
                        sold_stock = temp.quantity_weight - temp.available_stock
                        total_sold_price += sold_stock * temp.item_cost

                    obj = {}
                    obj['total_sold_quantity'] = total_sold_quantity
                    obj['total_sold_price'] = total_sold_price
                    print 'due ------------------', paid_due
                    obj['paid'] = paid_due['total_paid']
                    obj['due'] = paid_due['due']
                    return json_response({'counts': obj}, status=200)
                except Exception as e:
                    print e
                    return json_response({'error': e}, status=405)




            elif 'notification_data' in body:
                print 'in notifications ...........'
                stocks = StockDetails.objects.all()
                dummy_data = []
                current = datetime.datetime.now().date()
                print 'current is', current
                for temp in stocks:

                    dummy_date_variable = temp.expire_date
                    days_left = (dummy_date_variable - current).days
                    if days_left < 30 and days_left > 0 and not temp.seen:

                        print 'in less than 30 and not seen'
                        obj = {}
                        obj['stock_id'] = temp.id
                        obj['stock_name'] = temp.item_name
                        obj['days_left'] = days_left
                        dummy_data.append(obj)

                return json_response({'info': dummy_data}, status=200)

            elif 'get_details_of_notifications' in body:
                print 'in notifications ...........'

                stocks = StockDetails.objects.all()
                dummy_data = []
                current = datetime.datetime.now().date()
                print 'current is', current
                for temp in stocks:

                    if 'notification_ids' in body and temp.id in body['notification_ids']:
                        temp.seen = True
                        temp.save()

                    dummy_date_variable = temp.expire_date
                    days_left = (dummy_date_variable - current).days

                    if days_left < 30 and days_left > 0:

                        print 'in less than 30 and not seen'

                        obj = {}
                        obj['stock_id'] = temp.id
                        obj['stock_name'] = temp.item_name
                        obj['days_left'] = days_left

                        dummy_data.append(obj)


                return json_response({'info': dummy_data}, status=200)





            elif 'expired_expiring_products' in body:

                stocks = StockDetails.objects.all()
                dummy_data = []
                current = datetime.datetime.now().date()
                print 'current is', current
                for temp in stocks:

                    dummy_date_variable = temp.expire_date
                    days_left = (dummy_date_variable - current).days


                    if days_left < 30 and days_left > 1:

                        print 'in less than 30'

                        obj = {}
                        obj['stock_name'] = temp.item_name
                        obj['quantity_type'] = temp.quantity_type

                        obj['quantity'] = temp.available_stock
                        obj['expired_date'] = str(temp.expire_date)
                        obj['days_left'] = days_left
                        obj['status'] = 'expiring'
                        dummy_data.append(obj)


                    elif days_left < 1 :
                        print 'in expired ----', temp.expire_date
                        obj = {}
                        obj['stock_name'] = temp.item_name
                        obj['quantity_type'] = temp.quantity_type

                        obj['quantity'] = temp.available_stock
                        obj['expired_date'] = str(temp.expire_date)
                        obj['days_left'] = days_left
                        obj['status'] = 'expired'
                        dummy_data.append(obj)

                    else:
                        print 'not expired'

                        obj = {}
                        obj['stock_name'] = temp.item_name
                        obj['quantity_type'] = temp.quantity_type

                        obj['quantity'] = temp.available_stock
                        obj['expired_date'] = str(temp.expire_date)
                        obj['days_left'] = days_left
                        obj['status'] = 'has days'
                        dummy_data.append(obj)



                return json_response({'info': dummy_data}, status=200)



        except Exception as e:
            print e
            return json_response({"error": "unable to get data"}, status=401)


class GalleryManagement(View):

    def get(self, request):
        try:
            gallery_images = GalleryImages.objects.all()
            images = serializers.serialize('json', gallery_images)
            return json_response({"gallery_images": images}, status=200)
        except Exception as e:
            print e
            return Response({"error": e}, status=405)

    def post(self, request):
        try:

            file_name = ''
            try:

                for filename, file in request.FILES.iteritems():
                    file_name = request.FILES[filename]

                data = json.loads(json.dumps(request.POST))
                if 'image_id' in request.POST:
                    print 'yes update', data['image_id']
                    tmp = GalleryImages.objects.get(id = data['image_id'])
                    if file_name:
                        print 'yes pic'
                        tmp.gallery_image = file_name
                        tmp.save()
                    return json_response({"response" : "data updated successfully"}, status=200)
                else:
                    image = GalleryImages(gallery_image = file_name)
                    image.save()
                    return json_response({"response" : "data saved successfully"}, status=200)
            except Exception as e:
                print e
                return json_response({"error" : "unable to process data"}, status=200)
        except Exception as e:
            return json_response({"error" : "unable to process"}, status=401)




def deleteGalleryImage(request):
    try:
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        image = GalleryImages.objects.get(id = str(body['image_id']))
        os.remove(BASE_DIR+'/'+str(image.gallery_image))
        image.delete()
        return json_response({"status" : "successfully deleted"}, status=200)

    except Exception as e:
        print e
        return json_response({"error" : "unable to delete image"}, status=401)


from django_cron import CronJobBase, Schedule

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1 # every 2 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'my_app.my_cron_job'    # a unique code

    def do(self):
        print 'hellooooooooooo'
        pass    # do your thing here
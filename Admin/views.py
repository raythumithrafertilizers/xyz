
from rest_framework.response import Response
from rest_framework.views import APIView
from BaseApp.views import *
from django.db.models import Q
import datetime
from django.db.models import Sum, Count
from BaseModule.settings import *
import os
import json, csv
from django.core.files import File

from django.utils.decorators import method_decorator

item_types = ["Seeds", "Pesticides", "Fertilizers", "Bio_Pesticides", "Bio_Fertilizers"]


class SpecificCustomerPayments(APIView):
    """docstring for ClassName"""

    @method_decorator(admin_login_required)
    def post(self, request):
        try:
            body = request.body.decode("utf-8")
            body = json.loads(body)

            if(body['get_data']):
                customer = Customers.objects.get(id=body['customer_id'])
                customer_payments = customer.customer_payments.all()
                serialized_customer_payments = serializers.serialize('json', customer_payments)
                return Response({"response": json.loads(serialized_customer_payments)}, status=200)
            else:
                print body
                customer_payment = CustomerPayments.objects.get(id=body['id'])
                customer_payment.paid_amount = body['paid_amount']
                customer_payment.save()
                return Response({"response": "successfully saved ... "}, status=200)



        except Exception as e:
            print e
            return Response({"stockslist": e}, status=200)


class AddPayment(APIView):
    """docstring for ClassName"""

    @method_decorator(admin_login_required)
    def post(self, request):
        try:
            body = request.body.decode("utf-8")
            body = json.loads(body)

            customer_payment = CustomerPayments(paid_amount=body['paid_amount'])
            customer_payment.save()

            customer = Customers.objects.get(id = body['customer_id'])
            customer.customer_payments.add(customer_payment)

            return Response({"response": 'successfully added'}, status=200)


        except Exception as e:
            print e,'============'
            return Response({"stockslist": e}, status=405)







class DailyLegalProudctCategoryReport(APIView):
    """docstring for ClassName"""

    def get(self, request):
        try:
            name = "legaltest.csv"
            f = open(name, 'r')
            myfile = File(f)
            response = HttpResponse(myfile, content_type='application/csv')
            response['Content-Disposition'] = 'attachment; filename=' + name
            return response
        except Exception as e:
            print e
            return HttpResponse('error')

    def post(self, request):
        try:
            body = request.body.decode("utf-8")
            body = json.loads(body)

            divided_start_date = body['start_date'].split("/")
            divided_end_date = body['end_date'].split("/")

            start_temp_date = datetime.datetime(int(divided_start_date[2]),int(divided_start_date[1]), int(divided_start_date[0]))
            end_temp_date = datetime.datetime(int(divided_end_date[2]),int(divided_end_date[1]),int(divided_end_date[0]))
            #print body, datetime(int(divided_start_date[2]),int(divided_start_date[1]), int(divided_start_date[0])), divided_end_date
            filter_args = {
                '{0}__{1}'.format('bill_date', 'gte'): start_temp_date,
                '{0}__{1}'.format('bill_date', 'lte'): datetime.datetime(int(divided_end_date[2]),int(divided_end_date[1]),int(divided_end_date[0]), 23, 59, 59)
            }

            stocklist = Billing.objects.filter(**filter_args)
            stockslist = serializers.serialize('json', stocklist)
            main_data = json.loads(stockslist)

            required_rows_list = []


            # contains all billing objects

            for temp in main_data:
                required_rows ={}
                required_rows['bill_date'] = temp['fields']['bill_date']

                # if billing object has products
                if(len(temp['fields']['products_list'])):

                    products_data = ProductsList.objects.filter(id__in=temp['fields']['products_list'])

                    products_data_temp = json.loads(serializers.serialize('json', products_data))

                    # repeat billing object stock list or products list
                    for tt in products_data_temp:
                        try:
                            # get each product info by id and legal
                            temp_product = StockDetails.objects.get(id = tt['fields']['product'], isLegal='legal')

                            # check in final results contains item type (seed , some thing...)
                            if temp_product.item_type in required_rows:
                                # if contains increase type quantity and replace any spaces in name to _
                                required_rows[(temp_product.item_type).replace (" ", "_")] +=  tt['fields']['price']
                            else:
                                # if does n't contains add type name as key and replace space as _
                                required_rows[(temp_product.item_type).replace (" ", "_")] = tt['fields']['price']
                        except Exception as e:
                            print e

                # append to required list
                required_rows_list.append(required_rows)

            # allocate zero for non existing categories
            for temp2 in item_types:
                for temp in required_rows_list:
                    if temp2 not in temp.keys():
                        temp[temp2] = 0

            # check continous date exists or not
            # if not there add date and fileds with value "--"
            from datetime import date, timedelta as td
            temparary_date = []
            d1 = start_temp_date
            d2 = end_temp_date
            delta = d2 - d1
            for i in range(delta.days + 1):
                isExits = False
                for temp in required_rows_list:
                    temp['bill_date'] = temp['bill_date'].split("T")[0]
                    if temp['bill_date'] == str(d1 + td(days=i)).split(" ")[0]:
                        isExits = True
                        break
                if not isExits:
                    obj = {}
                    obj['bill_date'] = str(d1 + td(days=i)).split(" ")[0]
                    obj['Seeds'] = '--'
                    obj['Pesticides'] = '--'
                    obj['Fertilizers'] = '--'
                    obj['Bio_Pesticides'] = '--'
                    obj['Bio_Fertilizers'] = '--'
                    temparary_date.append(obj)


            required_rows_list.extend(temparary_date)

            storing_data = required_rows_list

            obj = {}
            obj['bill_date'] = "Total"
            obj['Seeds'] = 0
            obj['Pesticides'] = 0
            obj['Fertilizers'] = 0
            obj['Bio_Pesticides'] = 0
            obj['Bio_Fertilizers'] = 0


            f = csv.writer(open("legaltest.csv", "wb+"))
            f.writerow(
                ["bill_date", "Seeds", "Pesticides", "Fertilizers", "Bio_Pesticides", "Bio_Fertilizers"])
            for x in storing_data:

                # add to get total
                if type(x["Seeds"]) != str:
                    obj['Seeds'] += x["Seeds"]
                if type(x["Pesticides"]) != str:
                    obj['Pesticides'] += x["Pesticides"]
                if type(x["Fertilizers"]) != str:
                    obj['Fertilizers'] += x["Fertilizers"]
                if type(x["Bio_Pesticides"]) != str:
                    obj['Bio_Pesticides'] += x["Bio_Pesticides"]
                if type(x["Bio_Fertilizers"]) != str:
                    obj['Bio_Fertilizers'] += x["Bio_Fertilizers"]

                f.writerow([x["bill_date"],
                            x["Seeds"],
                            x["Pesticides"],
                            x["Fertilizers"],
                            x["Bio_Pesticides"],
                            x["Bio_Fertilizers"]
                           ])


            f.writerow([obj["bill_date"],
                        obj["Seeds"],
                        obj["Pesticides"],
                        obj["Fertilizers"],
                        obj["Bio_Pesticides"],
                        obj["Bio_Fertilizers"]
                        ])
            storing_data.append(obj)
            return Response({"stocks_list": required_rows_list}, status=200)
        except Exception as e:
            print e
            return Response({"stockslist": e}, status=200)






class InvoiceReports(APIView):
    """docstring for ClassName"""

    def get(self, request):
        try:
            name = "test.csv"
            f = open(name, 'r')
            myfile = File(f)
            response = HttpResponse(myfile, content_type='application/csv')
            response['Content-Disposition'] = 'attachment; filename=' + name
            return response
        except Exception as e:
            print e
            return HttpResponse('error')

    def post(self, request):
        try:

            body = request.body.decode("utf-8")
            body = json.loads(body)

            divided_start_date = body['start_date'].split("/")
            divided_end_date = body['end_date'].split("/")

            #print body, datetime(int(divided_start_date[2]),int(divided_start_date[1]), int(divided_start_date[0])), divided_end_date
            filter_args = {
                '{0}__{1}'.format('invoice_date', 'gte'): datetime.datetime(int(divided_start_date[2]),int(divided_start_date[1]), int(divided_start_date[0])),
                '{0}__{1}'.format('invoice_date', 'lte'): datetime.datetime(int(divided_end_date[2]),int(divided_end_date[1]),int(divided_end_date[0]))
            }

            invoice_bills = CompanyBills.objects.filter(**filter_args)
            #serialized_invoice_bills = json.loads(serializers.serialize('json', invoice_bills))
            final_data = []
            # invoice bills repeat

            for invoice_bill in invoice_bills:

                obj ={}
                stock_details_temp = StockDetails.objects.filter(invoice_bill = invoice_bill).values('item_type').annotate(total_price = Sum("quantity_weight") * Sum("item_cost"))

                # if items types are more repeat and replace space with _
                for temp in stock_details_temp:
                    obj[temp['item_type'].replace (" ", "_")] = temp['total_price']

                obj['invoice_number'] =  invoice_bill.company_invoice_number
                obj['invoice_date'] = str(invoice_bill.invoice_date)
                obj['company_name'] = str(invoice_bill.company_name)
                obj['company_tin_number'] = str(invoice_bill.company_tin_number)
                final_data.append(obj)

            for key in item_types:
                for object in final_data:
                    if  key not in object.keys():
                        object[key] = 0

            storing_data = final_data

            obj1 = {}
            obj1['invoice_date'] = "Total"
            obj1["invoice_number"] = "--"
            obj1["company_name"] = '--'
            obj1["company_tin_number"] = '--'
            obj1['Seeds'] = 0
            obj1['Pesticides'] = 0
            obj1['Fertilizers'] = 0
            obj1['Bio_Pesticides'] = 0
            obj1['Bio_Fertilizers'] = 0

            f = csv.writer(open("test.csv", "wb+"))
            f.writerow(["invoice_date", "invoice_number", "company_name", "tin_number", "Seeds", "Pesticides", "Fertilizers", "Bio_Pesticides", "Bio_Fertilizers"])
            for x in storing_data:

                # add to get total
                if type(x["Seeds"]) != str:
                    obj1['Seeds'] += x["Seeds"]
                if type(x["Pesticides"]) != str:
                    obj1['Pesticides'] += x["Pesticides"]
                if type(x["Fertilizers"]) != str:
                    obj1['Fertilizers'] += x["Fertilizers"]
                if type(x["Bio_Pesticides"]) != str:
                    obj1['Bio_Pesticides'] += x["Bio_Pesticides"]
                if type(x["Bio_Fertilizers"]) != str:
                    obj1['Bio_Fertilizers'] += x["Bio_Fertilizers"]

                f.writerow( [x["invoice_date"],
                            x["invoice_number"],
                            x["company_name"],
                            x["company_tin_number"],
                            x["Seeds"],
                            x["Pesticides"],
                            x["Fertilizers"],
                            x["Bio_Pesticides"],
                            x["Bio_Fertilizers"]])

            f.writerow([obj1["invoice_date"],
                        obj1["invoice_number"],
                        obj1["company_name"],
                        obj1["company_tin_number"],
                        obj1["Seeds"],
                        obj1["Pesticides"],
                        obj1["Fertilizers"],
                        obj1["Bio_Pesticides"],
                        obj1["Bio_Fertilizers"]
                        ])
            #print obj1
            final_data.append(obj1)
            return Response({"invoice_final_report": final_data},status=200)
        except Exception as e:
            print e
            return Response({"stockslist": e}, status=200)


class Reports(APIView):
    """docstring for ClassName"""

    def post(self, request):
        try:
            body = request.body.decode("utf-8")
            body = json.loads(body)

            divided_start_date = body['start_date'].split("/")
            divided_end_date = body['end_date'].split("/")

            #print body, datetime(int(divided_start_date[2]),int(divided_start_date[1]), int(divided_start_date[0])), divided_end_date
            filter_args = {
                '{0}__{1}'.format('bill_date', 'gte'): datetime.datetime(int(divided_start_date[2]),int(divided_start_date[1]), int(divided_start_date[0])),
                '{0}__{1}'.format('bill_date', 'lte'): datetime.datetime(int(divided_end_date[2]),int(divided_end_date[1]),int(divided_end_date[0]), 23, 59, 59)
            }

            stocklist = Billing.objects.filter(**filter_args)
            stockslist = serializers.serialize('json', stocklist)
            main_data = json.loads(stockslist)

            result_products_list = []

            types_data = {}

            for temp in main_data:
                if(len(temp['fields']['products_list'])):
                    products_data = ProductsList.objects.filter(id__in=temp['fields']['products_list'])
                    products_data_temp = json.loads(serializers.serialize('json', products_data))
                    for tt in products_data_temp:
                        temp_product = StockDetails.objects.get(id = tt['fields']['product'])
                        tt['fields']['specific_product_data'] = json.loads(serializers.serialize('json', [temp_product]))

                        if hasattr(types_data, tt['fields']['specific_product_data'][0]['fields']['item_type']):
                            types_data[tt['fields']['specific_product_data'][0]['fields']['item_type']] += tt['fields']['price']
                        else:
                            types_data[tt['fields']['specific_product_data'][0]['fields']['item_type']] = tt['fields']['price']




                        result_products_list.append(tt)
                temp['fields']['products_data'] = products_data_temp
                print temp['fields']['customer']

            customer_aggregation = Billing.objects.filter(**filter_args).values('customer').annotate(total_price=Sum('total_price'),
                                                        total_paid=Sum('total_paid'),
                                                        due=Sum('due'))

            for t in customer_aggregation:
                print int(t['customer'])
                customer_details = Customers.objects.get(id = int(t['customer']))
                t['customer_name'] = customer_details.first_name+" "+customer_details.last_name


                cpal = 0
                cp = customer_details.customer_payments.all()
                scp = json.loads(serializers.serialize('json', cp))
                for tcp in scp:
                    cpal += tcp['fields']['paid_amount']

                    t['total_paid'] += cpal
                    t['due'] -= cpal


            return Response({"stocks_list": result_products_list, 'customer_details': customer_aggregation, 'types_data': types_data}, status=200)
        except Exception as e:
            print e
            return Response({"stockslist": e}, status=200)




class GetStock(APIView):
    """docstring for ClassName"""

    def get(self, request):
        try:
            stocklist = StockDetails.objects.all()
            stockslist = serializers.serialize('json', stocklist)
            main_data = json.loads(stockslist)

            for temp in main_data:
                data = CompanyBills.objects.get(id = temp['fields']['invoice_bill'])
                temp['fields']['company_invoice_number'] = data.company_invoice_number

                #temp_data = temp.invoice_bill.company_invoice_number
                #temp['temp_data'] = temp_data


            return Response({"stockslist": json.dumps(main_data)}, status=200)
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

            if 'invoice_bill' in body['stockdata']:
                try:
                    print body['stockdata']['invoice_bill'], '-------------------'
                    temp_invoice_bill = CompanyBills.objects.get(id=body['stockdata']['invoice_bill'])
                    stock.invoice_bill = temp_invoice_bill
                except Exception as e:
                    print e
                    return json_response({"err": "no invoice bill found ..."}, status=200)

            if 'batch_number' in body['stockdata']:
                stock.item_batch_number = body['stockdata']['batch_number']

            if 'available_stock' in body['stockdata']:
                stock.available_stock = body['stockdata']['available_stock']

            if 'invoice_price' in body['stockdata']:
                stock.invoice_cost = body['stockdata']['invoice_price']

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
            return json_response({"bill_pk":billingObject.id}, status=200)
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


def GetBillById(request):
    try:
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        if 'bill_id' in body:
            bill = Billing.objects.get(id = str(body['bill_id']))
            return json_response({"data" : "bill find successfully"}, status=200)

        return json_response({"error" : "no bill id found"}, status=400)


    except Exception as e:
        return json_response({"error" : "Bill Not Found ...."}, status=400)

def printBill(request):
    try:
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        if 'bill_id' in body:
            bill = Billing.objects.get(id = str(body['bill_id']))
            bill_details = {}
            bill_details['customer_name'] = bill.customer.first_name +" "+ bill.customer.last_name
            bill_details['total_price'] = bill.total_price
            bill_details['total_quantity'] = bill.total_quantity
            bill_details['due'] = bill.due
            bill_details['bill_id'] = bill.id


            products_all_list = bill.products_list.all()

            temp_product_details = []
            for t_product in products_all_list:

                product_details = {}
                product_details['product_name'] = t_product.product.item_name
                product_details['expired_date'] = str(t_product.product.expire_date)
                product_details['product_type'] = t_product.product.item_type
                product_details['legal_type'] =  t_product.product.isLegal


                if t_product.product.item_batch_number:
                    product_details['bt_no'] = t_product.product.item_batch_number
                elif t_product.product.item_lot_number:
                    product_details['bt_no'] = t_product.product.item_lot_number


                product_details['total_quantity'] = t_product.quantity
                product_details['total_price'] = t_product.price


                product_details['single_price'] = round(float(t_product.price)/float(t_product.quantity),3)
                temp_product_details.append(product_details)
            bill_details['p_details'] = temp_product_details

            return json_response({"data" : bill_details}, status=200)

        return json_response({"error" : "no bill id found"}, status=400)


    except Exception as e:
        print e
        return json_response({"error" : "No Stock Found"}, status=400)

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
                    companyBill.invoice_date = data['invoice_date']
                    companyBill.company_tin_number = data['tin_number']

                    if file_name:
                        print 'yes pic'
                        companyBill.bill_image = file_name
                    companyBill.save()
                    return json_response({"response" : "data updated successfully"}, status=200)
                else:
                    companyBill = CompanyBills(company_name = data['company_name'])
                    companyBill.company_invoice_number = data['company_invoice']
                    companyBill.company_tin_number = data['tin_number']
                    temp_invoice_date = datetime.datetime.strptime(str(data['invoice_date']),
                                                                        "%d/%m/%Y").date()
                    companyBill.invoice_date = temp_invoice_date
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

            temp_invoice_bill = CompanyBills.objects.get(id=body['stockdata']['invoice_bill'])
            isStockExits = StockDetails.objects.filter(invoice_bill = temp_invoice_bill, item_name = body['stockdata']['stock_name'])
            if len(isStockExits):
                return json_response({"response": "stock already saved with same invoice and name"}, status=405)

            expired_converted_date = datetime.datetime.strptime(str(body['stockdata']['expired_date']),"%d/%m/%Y").date()

            stock = StockDetails(item_name = body['stockdata']['stock_name'],
                                 item_type= body['stockdata']['stock_type']['name'],
                                 expire_date = expired_converted_date)

            if 'invoice_bill' in body['stockdata']:
                try:
                    #temp_invoice_bill = CompanyBills.objects.get(id = body['stockdata']['invoice_bill'])
                    stock.invoice_bill = temp_invoice_bill
                except Exception as e:
                    print e
                    return json_response({"err": "no invoice bill found ..."}, status=200)

            if 'isLegal' in body['stockdata']:
                stock.isLegal = body['stockdata']['isLegal']['name']

            if 'batch_number' in body['stockdata']:
                stock.item_batch_number = body['stockdata']['batch_number']

            if 'available_stock' in body['stockdata']:
                stock.available_stock = body['stockdata']['available_stock']

            if 'invoice_price' in body['stockdata']:
                stock.invoice_cost = body['stockdata']['invoice_price']
                
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

            return json_response({"err" : "stock saved successfully"}, status=200)
        except Exception as e:
            print e
            return json_response({"response":"unable to save stock"}, status=405)


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
                    cp = customer_info[0].customer_payments.all()

                    scp = json.loads(serializers.serialize('json', cp))

                    cpal = 0
                    for tcp in scp:
                        cpal += tcp['fields']['paid_amount']

                    customer_information = serializers.serialize('json', customer_info)
                    customer_information = json.loads(customer_information)

                    name = customer_information[0]['fields']['first_name']+" "+customer_information[0]['fields']['last_name']

                    phone = customer_information[0]['fields']['phone']
                    obj['customer_id'] = customer_information[0]['pk']
                    obj['total_price'] = temp['total_price']

                    obj['paid'] = temp['paid'] + cpal
                    obj['due'] = temp['total_price'] - obj['paid']
                    obj['customer_name'] = name
                    obj['phone'] = phone
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

                    all_customers = Customers.objects.all()
                    cpal = 0
                    for ac in all_customers:
                        cp = ac.customer_payments.all()
                        scp = json.loads(serializers.serialize('json', cp))
                        for tcp in scp:
                            cpal += tcp['fields']['paid_amount']

                    paid_due['total_paid'] += cpal
                    paid_due['due'] -= cpal

                    total_stock = StockDetails.objects.all()

                    total_sold_price = 0

                    for temp in total_stock:
                        sold_stock = temp.quantity_weight - temp.available_stock
                        total_sold_price += sold_stock * temp.item_cost

                    obj = {}

                    if total_sold_quantity:
                        obj['total_sold_quantity'] = total_sold_quantity
                    else:
                        obj['total_sold_quantity'] = 0.0


                    if total_sold_price:
                        obj['total_sold_price'] = total_sold_price
                    else:
                       obj['total_sold_price'] = 0.0

                    if paid_due['total_paid']:
                        obj['paid'] = paid_due['total_paid']
                    else:
                        obj['paid'] = 0.0

                    if paid_due['due']:
                        obj['due'] = paid_due['due']
                    else:
                        obj['due'] = 0.0

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
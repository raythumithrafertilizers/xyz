
from rest_framework.views import APIView
from BaseApp.views import *
from django.db.models import Q
import datetime
from django.db.models import Sum
import json, csv
from django.core.files import File
from BaseModule.settings import BASE_DIR
item_types = ["Seeds", "Pesticides", "Fertilizers", "Bio_Pesticides", "Bio_Fertilizers"]



class ExpenditureReports(APIView):
    """docstring for ClassName"""

    def post(self, request):
        try:
            body = request.body.decode("utf-8")
            body = json.loads(body)
            specific_farmer_id = False

            divided_start_date = body['start_date'].split("/")
            divided_end_date = body['end_date'].split("/")

            # bill date must be between start and end date
            filter_args = {
                '{0}__{1}'.format('create_date', 'gte'): datetime.datetime(int(divided_start_date[2]),int(divided_start_date[1]), int(divided_start_date[0])),
                '{0}__{1}'.format('create_date', 'lte'): datetime.datetime(int(divided_end_date[2]),int(divided_end_date[1]),int(divided_end_date[0]), 23, 59, 59),

            }


            if 'stock_id' in body:
                if body['stock_id']:
                    filter_args['type'] = body['stock_id']

            stocklist = Expenditures.objects.filter(**filter_args)


            file_path = BASE_DIR + "/Admin/report_files/expenditure_reports.csv"
            temp_data = []
            with open(file_path, 'w') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(["Expenditure Reports", ""])
                spamwriter.writerow(["", ""])
                spamwriter.writerow(["create date", "amount" ,"type", "remarks"])
                sum_of_amount = 0.0
                for temp in stocklist:
                        # increment advance due payment fields
                        obj = {}
                        obj['create_date'] = temp.create_date
                        obj['remarks'] = temp.remarks
                        obj['amount'] = temp.amount
                        obj['type'] = temp.type
                        sum_of_amount += obj['amount']
                        temp_data.append(obj)

                        spamwriter.writerow([
                            obj['create_date'],
                            obj['amount'],
                            obj['type'],
                            obj['remarks']
                        ])

                spamwriter.writerow([
                    "Total",
                    sum_of_amount,
                    " ",
                    " "

                ])

            return Response({"data": temp_data, "total": sum_of_amount},status=200)
        except Exception as e:
            return Response({"stockslist": e.message}, status=403)


class GetCompleteInfo(APIView):
    """docstring for ClassName"""

    def post(self, request):
        try:
            body = request.body.decode("utf-8")
            body = json.loads(body)
            print body
            if len(body['ids']):
                stock_details_data = []
                stock_names = StockNames.objects.filter(id__in=body['ids'])
                for temp in stock_names:
                    data = StockDetails.objects.get(item_name=temp)
                    obj = {}
                    obj['id'] = temp.id
                    obj['available_stock'] = data.available_stock
                    stock_details_data.append(obj)
                    return Response({"data": stock_details_data}, status=200)
            else:
                return Response({"data": []}, status=200)

        except Exception as e:
            print e
            return Response({"stockslist": e}, status=200)





def InterestDownloadView(request):
    try:
        name = BASE_DIR + "/Admin/report_files/farmer_interest_payments.csv"
        f = open(name, 'r')
        myfile = File(f)
        response = HttpResponse(myfile, content_type='application/csv')
        response['Content-Disposition'] = 'attachment; filename=' + name
        return response
    except Exception as e:
        print e
        return HttpResponse('error')

def PaidDownloadView(request):
    try:
        name = BASE_DIR + "/Admin/report_files/farmer_interest_paid_money.csv"
        f = open(name, 'r')
        myfile = File(f)
        response = HttpResponse(myfile, content_type='application/csv')
        response['Content-Disposition'] = 'attachment; filename=' + name
        return response
    except Exception as e:
        print e
        return HttpResponse('error')

def ExpenditureDownloadView(request):
    try:
        name = BASE_DIR + "/Admin/report_files/expenditure_reports.csv"
        f = open(name, 'r')
        myfile = File(f)
        response = HttpResponse(myfile, content_type='application/csv')
        response['Content-Disposition'] = 'attachment; filename=' + name
        return response
    except Exception as e:
        print e
        return HttpResponse('error')


class InterestReports(APIView):
    """docstring for ClassName"""

    def post(self, request):
        try:
            body = request.body.decode("utf-8")
            body = json.loads(body)
            farmer = False

            divided_start_date = body['start_date'].split("/")
            divided_end_date = body['end_date'].split("/")

            if 'farmer_id' in body:
                if body['farmer_id']:
                    farmer = Person.objects.get(id = body['farmer_id'])

            if farmer:
                filter_args = {
                    '{0}__{1}'.format('paid_date', 'gte'): datetime.datetime(int(divided_start_date[2]),int(divided_start_date[1]), int(divided_start_date[0])),
                    '{0}__{1}'.format('paid_date', 'lte'): datetime.datetime(int(divided_end_date[2]),int(divided_end_date[1]),int(divided_end_date[0]), 23, 59, 59),
                }

                data = farmer.advance_details.filter(**filter_args)
                interest_data = []
                file_path = BASE_DIR + "/Admin/report_files/farmer_interest_payments.csv"
                with open(file_path, 'w') as csvfile:

                    spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    spamwriter.writerow(
                        ["farmer Name", "amount", "paid_date", "interest_rate",
                         "interest_money", "remarks", "is_purchase_advance"])

                    for temp in data:
                        obj = {}
                        obj['farmer_name'] = farmer.name
                        obj['amount'] = temp.amount
                        obj['paid_date'] = temp.paid_date
                        obj['cleared_date'] = temp.cleared_date
                        obj['interest_rate'] = temp.interest_rate
                        obj['interest_money'] = temp.interest_money
                        obj['purchase_id'] = temp.purchase_id
                        obj['remarks'] = temp.remarks
                        interest_data.append(obj)
                        spamwriter.writerow([
                            obj['farmer_name'],
                            obj['amount'],
                            obj['paid_date'],
                            obj['interest_rate'],
                            obj['interest_money'],
                            obj['remarks'],
                            obj['purchase_id']
                        ])

                filter_args = {
                    '{0}__{1}'.format('farmer_paid_date', 'gte'): datetime.datetime(int(divided_start_date[2]),
                                                                             int(divided_start_date[1]),
                                                                             int(divided_start_date[0])),
                    '{0}__{1}'.format('farmer_paid_date', 'lte'): datetime.datetime(int(divided_end_date[2]),
                                                                             int(divided_end_date[1]),
                                                                             int(divided_end_date[0]), 23, 59, 59),
                }
                filter_args['paid_farmer_id'] = farmer.id

                data = PiadAdvanceDetails.objects.filter(**filter_args)
                paid_amounts = []
                file_path = BASE_DIR + "/Admin/report_files/farmer_interest_paid_money.csv"
                with open(file_path, 'w') as csvfile:

                    spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    spamwriter.writerow(
                        ["farmer Name", "paid_date","paid_amount",
                         "total_to_be_paid", "pending", "remarks"])
                    for temp in data:
                        obj = {}
                        obj['farmer_name'] = farmer.name
                        obj['paid_date'] = temp.farmer_paid_date
                        obj['paid_amount'] = temp.farmer_paid_amount
                        obj['total_to_be_paid'] = temp.final_total_with_interest
                        obj['pending'] = temp.final_total_with_interest - temp.farmer_paid_amount
                        obj['remarks'] = temp.remarks
                        paid_amounts.append(obj)
                        spamwriter.writerow([
                            obj['farmer_name'],
                            obj['paid_date'],
                            obj['paid_amount'],
                            obj['total_to_be_paid'],
                            obj['pending'],
                            obj['remarks']
                        ])
                return Response({"interest_data": interest_data, 'paid_amounts':paid_amounts}, status=200)

            else:
                return Response({"interest_data": [], 'paid_amounts':[]}, status=200)

        except Exception as e:
            print e
            return Response({"stockslist": e}, status=200)








class StockAppendReports(APIView):
    """docstring for ClassName"""

    def post(self, request):
        try:
            body = request.body.decode("utf-8")
            body = json.loads(body)
            specific_farmer_id = False

            divided_start_date = body['start_date'].split("/")
            divided_end_date = body['end_date'].split("/")

            # bill date must be between start and end date
            filter_args = {
                '{0}__{1}'.format('create_date', 'gte'): datetime.datetime(int(divided_start_date[2]),int(divided_start_date[1]), int(divided_start_date[0])),
                '{0}__{1}'.format('create_date', 'lte'): datetime.datetime(int(divided_end_date[2]),int(divided_end_date[1]),int(divided_end_date[0]), 23, 59, 59),

            }

            filter_args2 = {
                '{0}__{1}'.format('create_date', 'gte'): datetime.datetime(int(divided_start_date[2]),
                                                                           int(divided_start_date[1]),
                                                                           int(divided_start_date[0])),
                '{0}__{1}'.format('create_date', 'lte'): datetime.datetime(int(divided_end_date[2]),
                                                                           int(divided_end_date[1]),
                                                                           int(divided_end_date[0]), 23, 59, 59),

            }


            #-----------------calculating customer sold products------------------------
            print body['stock_id'], '00000000000000'
            stock_names_object_customer_sold = StockNames.objects.get(id=int(body['stock_id']))
            stock_details_object_customer_sold = StockDetails.objects.get(item_name=stock_names_object_customer_sold)
            filter_args3 = {
                '{0}__{1}'.format('bill_date', 'gte'): datetime.datetime(int(divided_start_date[2]),
                                                                         int(divided_start_date[1]),
                                                                         int(divided_start_date[0])),
                '{0}__{1}'.format('bill_date', 'lte'): datetime.datetime(int(divided_end_date[2]),
                                                                         int(divided_end_date[1]),
                                                                         int(divided_end_date[0]), 23, 59, 59),
                '{0}__{1}'.format('products_list', 'product'): stock_details_object_customer_sold
            }

            stocklist_customer_sold = Billing.objects.filter(**filter_args3)

            quantity_sum_c = 0.0
            response_c = []

            for temp in stocklist_customer_sold:
                product_info = temp.products_list.filter(product=stock_details_object_customer_sold)
                if len(product_info):
                    obj = {}
                    print product_info[0].quantity, '*****'
                    obj['create_date'] = temp.bill_date
                    obj['remarks'] = 'sold to ' + str(temp.customer.name)
                    obj['append_count'] = product_info[0].quantity
                    quantity_sum_c += product_info[0].quantity
                    response_c.append(obj)

            #-------------------------------------------

            temp_data = []
            stock_name = ""
            remain_stock = ""
            sum_of_manufacture_stock = 0.0
            sum_of_purchase_stock_farmers = 0.0
            available_stock = []

            if 'stock_id' in body:
                if body['stock_id']:
                    print body['stock_id'], '==================='
                    stock_name = StockNames.objects.get(id=body['stock_id'])

                    sold_stock_object = StockDetails.objects.get(item_name = stock_name)
                    stock_name = stock_name.name
                    remain_stock = sold_stock_object.available_stock
                    filter_args['stock'] = sold_stock_object
                    stocklist = AppendStockDetails.objects.filter(**filter_args)
                    file_path = BASE_DIR + "/Admin/report_files/append_stock_reports.csv"
                    with open(file_path, 'w') as csvfile:
                        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

                        spamwriter.writerow(["stock_name", stock_name])
                        spamwriter.writerow(["Remaining Stock Count", remain_stock])
                        spamwriter.writerow(["", ""])
                        spamwriter.writerow(["", ""])
                        spamwriter.writerow(["Debit Reports", ""])

                        spamwriter.writerow(["date", "quantity", "remarks"])

                        for temp in stocklist:

                                if temp.sold_stock_id:
                                    sum_of_purchase_stock_farmers += temp.append_count
                                else:
                                    sum_of_manufacture_stock += temp.append_count

                                print 'count of got stock'
                                # increment advance due payment fields
                                obj = {}
                                obj['stock_name'] = temp.stock.item_name.name
                                obj['remarks'] = temp.remarks
                                obj['create_date'] = temp.create_date
                                obj['append_count'] = temp.append_count
                                obj['total_stock'] = temp.total_stock

                                temp_data.append(obj)

                                spamwriter.writerow([
                                    obj['create_date'],
                                    obj['append_count'],
                                    obj['remarks']
                                ])
                        for tmp in response_c:
                            temp_data.append(tmp)
                            spamwriter.writerow([
                                str(tmp['create_date']),
                                float(tmp['append_count']),
                                tmp['remarks']
                            ])



            file_path = BASE_DIR + "/Admin/report_files/append_all_stock_reports.csv"
            sum_of_remaining = 0.0
            with open(file_path, 'w') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(["", ""])
                spamwriter.writerow(["Remain Stock Reports", ""])

                spamwriter.writerow([
                    'stock_name',
                    'remaining_stock'
                ])

                stocklist = StockDetails.objects.filter(**filter_args2)
                for temp in stocklist:
                    obj = {}
                    obj['stock_name'] = temp.item_name.name
                    obj['available_stock'] = temp.available_stock
                    sum_of_remaining += float(temp.available_stock)
                    available_stock.append(obj)
                    spamwriter.writerow([
                        obj['stock_name'],
                        obj['available_stock']

                    ])

                spamwriter.writerow(["Total", sum_of_remaining])

            # writing to single file
            base_path = BASE_DIR + "/Admin/report_files/"
            all_data_file = open(base_path + "stock_all_report_data.csv", "wb")
            all_data_file.write("Title,Stock Reports\r\n")
            # first file:

            for line in open(base_path + "append_stock_reports.csv"):
                all_data_file.write(line)

            for line in open(base_path + "append_all_stock_reports.csv"):
                all_data_file.write(line)


            all_data_file.close()


            return Response({"data": temp_data,
                             "remaining_all_stocks":available_stock,
                             "stock_name": stock_name,
                             "remain": remain_stock,
                             'sum_of_manufacture_stock': sum_of_manufacture_stock,
                             'sum_of_sold_farmer_stock': sum_of_purchase_stock_farmers,
                             'sum_of_sold_customer_stock': quantity_sum_c}
                            ,status=200)

        except Exception as e:
            print e
            return Response({"stockslist": e}, status=200)
class DeleteExpenditure(View):

    def post(self, request):
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            userdata = Expenditures.objects.get(id = str(body['id']))
            userdata.isActive = False
            userdata.save()
            return json_response({"status" : "successfully deleted"}, status=200)
        except Exception as e:
            print e
            return json_response({"err" : "No User Found"}, status=401)

class EditExpenditure(View):

    def post(self, request):
        """ Here we are checking for the existing stock data if exists we update else throw and error """
        body = request.body.decode("utf-8")
        body = json.loads(body)
        try:
            print body
            stock = Expenditures.objects.get(id=str(body['id']))

            converted_date = datetime.datetime.strptime(str(body['created_date']),"%d/%m/%Y").date()
            stock.create_date = converted_date

            if 'remarks' in body:
                stock.remarks = body['remarks']

            if 'amount' in body:
                stock.amount = body['amount']

            if 'type' in body:
                stock.type = body['type']

            stock.save()

            return HttpResponse("Datasaved successfully", status=200)
        except Exception, e:
            return HttpResponse("Data Failed", status=401)


class AddExpenditure(View):

    def get(self, request):

        try:
            expenditures_list = []
            data = Expenditures.objects.filter(isActive=True)
            for temp in data:
                obj = {}
                obj['id'] = temp.id
                obj['created_date'] = str(temp.create_date)
                obj['amount'] = temp.amount
                obj['type'] = temp.type
                obj['remarks'] = temp.remarks
                expenditures_list.append(obj)
            return json_response({"expenditures_list": expenditures_list}, status=200)
        except Exception as e:
            print e
            return HttpResponse({"response": e}, status=400)

    def post(self, request):
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            print body
            stock = Expenditures(type = body['stockdata']['stock_name'])

            if 'a_stock' in body['stockdata']:
                stock.amount = float(body['stockdata']['a_stock'])


            if 'remarks' in body['stockdata']:
                stock.remarks = body['stockdata']['remarks']

            if 'creation_date' in body['stockdata']:
                stock.create_date = datetime.datetime.strptime(str(body['stockdata']['creation_date']),"%d/%m/%Y").date()


            stock.save()

            return json_response({"err" : "stock saved successfully"}, status=200)
        except Exception as e:
            print e
            return json_response({"response":"unable to save stock"}, status=405)

class SaveInterest(APIView):
    def post(self, request):
        try:
            body = request.body.decode("utf-8")
            body = json.loads(body)
            farmer = Person.objects.get(id=body['farmer_id'])


            paid_advance_details = PiadAdvanceDetails(amount = body['total_advance'])
            if body['farmer_paid_date']:
                farmer_paid_date = datetime.datetime.strptime(str(body['farmer_paid_date']),"%d/%m/%Y").date()
                paid_advance_details.farmer_paid_date = farmer_paid_date
            paid_advance_details.interest_money = body['total_interest_money']
            paid_advance_details.interest_rate = body['interest_rate']
            paid_advance_details.farmer_paid_amount = body['farmer_paid_advance']
            paid_advance_details.final_total_with_interest = body['final_total_advance']
            paid_advance_details.remarks = body['remarks']
            paid_advance_details.paid_farmer_id = body['farmer_id']
            paid_advance_details.save()


            advance = AdvanceDetails(amount = body['final_total_advance'] - body['farmer_paid_advance'])
            if body['farmer_paid_date']:
                advance.paid_date = farmer_paid_date
            if 'remarks' in body:
                advance.remarks = body['remarks']
            advance.save()
            farmer.advance_details.add(advance)


            for temp in body['data']:
                advance = AdvanceDetails.objects.get(id=temp['id'])
                advance.paid_date = temp['paid_date']
                advance.interest_money = temp['interest_money']
                advance.amount = temp['amount']
                advance.sum_amount = temp['sum_amount']
                if 'closing_date' in temp:
                    c_date = datetime.datetime.strptime(str(temp['closing_date']), "%d/%m/%Y").date()
                    advance.cleared_date = c_date
                    print c_date
                advance.isCleared = True
                advance.paid_details_id = paid_advance_details.id
                advance.save()
            return Response({"success": 'successfully saved'},status=200)
        except Exception as e:
            print e
            return Response({"stockslist": e}, status=200)


class InterestsReport(APIView):
    def post(self, request):
        try:
            body = request.body.decode("utf-8")
            body = json.loads(body)
            advances_list = []
            if 'farmer_id' in body:
                if body['farmer_id']:
                    farmer = Person.objects.get(id = int(body['farmer_id']))
                    stocklist = farmer.advance_details.filter(isCleared = False)

                    stockslist = serializers.serialize('json', stocklist)
                    main_data = json.loads(stockslist)
                    row_id = 1
                    for key,temp in enumerate(main_data):
                        print key, temp
                        if row_id == 1:
                            print 'yes'
                            temp_dict = {}
                            temp_dict['id'] = temp['pk']
                            temp_dict['paid_date'] = temp['fields']['paid_date']
                            temp_dict['interest_rate'] = temp['fields']['interest_rate']
                            temp_dict['interest_money'] = temp['fields']['interest_money']
                            temp_dict['amount'] = temp['fields']['amount']
                            temp_dict['sum_amount'] = temp['fields']['amount']
                            advances_list.append(temp_dict)
                            row_id += 1
                        else:
                            temp_dict = {}
                            temp_dict['id'] = temp['pk']
                            temp_dict['paid_date'] = temp['fields']['paid_date']
                            temp_dict['interest_rate'] = temp['fields']['interest_rate']
                            temp_dict['interest_money'] = temp['fields']['interest_money']
                            temp_dict['amount'] = temp['fields']['amount']
                            temp_dict['sum_amount'] = advances_list[key - 1 ]['sum_amount'] + temp['fields']['amount']
                            advances_list.append(temp_dict)
                            row_id += 1



            return Response({"advances_list": advances_list},status=200)
        except Exception as e:
            print e
            return Response({"stockslist": e}, status=200)

def FarmerDownloadView(request, status):
    try:
        status = int(status)
        print status
        name = BASE_DIR + "/Admin/report_files/farmer_all_report_data.csv"
        f = open(name, 'r')
        myfile = File(f)
        response = HttpResponse(myfile, content_type='application/csv')
        response['Content-Disposition'] = 'attachment; filename=' + name

        return response
        """if status == 1:
            print status
            name = BASE_DIR + "/Admin/report_files/farmer_credits.csv"
            f = open(name, 'r')
            myfile = File(f)
            response = HttpResponse(myfile, content_type='application/csv')
            response['Content-Disposition'] = 'attachment; filename=' + name

            return response
        if status == 2:
            name = BASE_DIR + "/Admin/report_files/farmer_debits.csv"
            f = open(name, 'r')
            myfile = File(f)
            response = HttpResponse(myfile, content_type='application/csv')
            response['Content-Disposition'] = 'attachment; filename=' + name
            return response

        if status == 3:
            name = BASE_DIR + "/Admin/report_files/farmer_dues_sum.csv"
            f = open(name, 'r')
            myfile = File(f)
            response = HttpResponse(myfile, content_type='application/csv')
            response['Content-Disposition'] = 'attachment; filename=' + name
            return response"""


        return HttpResponse('wrong status given')
    except Exception as e:
        print e
        return HttpResponse('error')

def HarvesterDownloadView(request, status):
    try:
        status = int(status)
        name = BASE_DIR + "/Admin/report_files/harvester_all_report_data.csv"
        f = open(name, 'r')
        myfile = File(f)
        response = HttpResponse(myfile, content_type='application/csv')
        response['Content-Disposition'] = 'attachment; filename=' + name
        return response
        """if status == 1:
            print status
            name = BASE_DIR + "/Admin/report_files/harvester_debits.csv"
            f = open(name, 'r')
            myfile = File(f)
            response = HttpResponse(myfile, content_type='application/csv')
            response['Content-Disposition'] = 'attachment; filename=' + name

            return response
        if status == 2:
            name = BASE_DIR + "/Admin/report_files/harvester_credits.csv"
            f = open(name, 'r')
            myfile = File(f)
            response = HttpResponse(myfile, content_type='application/csv')
            response['Content-Disposition'] = 'attachment; filename=' + name
            return response

        if status == 3:
            name = BASE_DIR + "/Admin/report_files/harvester_dues_sum.csv"
            f = open(name, 'r')
            myfile = File(f)
            response = HttpResponse(myfile, content_type='application/csv')
            response['Content-Disposition'] = 'attachment; filename=' + name
            return response
        """
        return HttpResponse('wrong status given')
    except Exception as e:
        print e
        return HttpResponse('error')

def ProductSaleDownloadView(request, status):
    try:
        status = int(status)
        print status
        if status == 1:
            name = BASE_DIR + "/Admin/report_files/customer_credits.csv"
            f = open(name, 'r')
            myfile = File(f)
            response = HttpResponse(myfile, content_type='application/csv')
            response['Content-Disposition'] = 'attachment; filename=' + name
            return response


        return HttpResponse('wrong status given')

    except Exception as e:
        print e
        return HttpResponse('error')


def AppendDownloadView(request):
    try:
        name = BASE_DIR + "/Admin/report_files/stock_all_report_data.csv"
        f = open(name, 'r')
        myfile = File(f)
        response = HttpResponse(myfile, content_type='application/csv')
        response['Content-Disposition'] = 'attachment; filename=' + name
        return response
    except Exception as e:
        print e
        return HttpResponse('error')

def AppendDownloadView2(request):
    try:
        name = BASE_DIR + "/Admin/report_files/append_all_stock_reports.csv"
        f = open(name, 'r')
        myfile = File(f)
        response = HttpResponse(myfile, content_type='application/csv')
        response['Content-Disposition'] = 'attachment; filename=' + name
        return response
    except Exception as e:
        print e
        return HttpResponse('error')

def CustomerDownloadView(request, status):
    try:
        status = int(status)
        name = BASE_DIR + "/Admin/report_files/customer_all_report_data.csv"
        f = open(name, 'r')
        myfile = File(f)
        response = HttpResponse(myfile, content_type='application/csv')
        response['Content-Disposition'] = 'attachment; filename=' + name
        return response

        """print status
        if status == 1:
            print status
            name = BASE_DIR + "/Admin/report_files/customer_debits.csv"
            f = open(name, 'r')
            myfile = File(f)
            response = HttpResponse(myfile, content_type='application/csv')
            response['Content-Disposition'] = 'attachment; filename=' + name

            return response
        if status == 2:
            name = BASE_DIR + "/Admin/report_files/customer_reports_all_customers.csv"
            f = open(name, 'r')
            myfile = File(f)
            response = HttpResponse(myfile, content_type='application/csv')
            response['Content-Disposition'] = 'attachment; filename=' + name
            return response
        if status == 3:
            name = BASE_DIR + "/Admin/report_files/customer_dues_sum.csv"
            f = open(name, 'r')
            myfile = File(f)
            response = HttpResponse(myfile, content_type='application/csv')
            response['Content-Disposition'] = 'attachment; filename=' + name
            return response
        """

        return HttpResponse('wrong status given')

    except Exception as e:
        print e
        return HttpResponse('error')

class CustomersReport(APIView):
    """docstring for ClassName"""

    def post(self, request):
        try:
            body = request.body.decode("utf-8")
            body = json.loads(body)
            specific_farmer_id = False

            divided_start_date = body['start_date'].split("/")
            divided_end_date = body['end_date'].split("/")

            # bill date must be between start and end date
            filter_args = {
                '{0}__{1}'.format('bill_date', 'gte'): datetime.datetime(int(divided_start_date[2]),
                                                                            int(divided_start_date[1]),
                                                                            int(divided_start_date[0])),
                '{0}__{1}'.format('bill_date', 'lte'): datetime.datetime(int(divided_end_date[2]),
                                                                            int(divided_end_date[1]),
                                                                            int(divided_end_date[0]), 23, 59, 59),
            }

            paid_filter_args = {
                '{0}__{1}'.format('paid_date', 'gte'): datetime.datetime(int(divided_start_date[2]),
                                                                         int(divided_start_date[1]),
                                                                         int(divided_start_date[0])),
                '{0}__{1}'.format('paid_date', 'lte'): datetime.datetime(int(divided_end_date[2]),
                                                                         int(divided_end_date[1]),
                                                                         int(divided_end_date[0]), 23, 59, 59),
            }

            credits_file = BASE_DIR + "/Admin/report_files/customer_credits.csv"
            debits_file = BASE_DIR + "/Admin/report_files/customer_debits.csv"
            sum_of_dues_file = BASE_DIR + "/Admin/report_files/customer_dues_sum.csv"

            stocklist = Billing.objects.filter(**filter_args)

            all_farmers = Person.objects.filter(person_type='customer')
            farmer_details = {}
            for farmer in all_farmers:
                advances = farmer.advance_details.filter(**paid_filter_args)
                farmer_details[farmer.name] = 0.0
                for advance in advances:
                    farmer_details[farmer.name] += float(advance.amount)

            all_borrowers = []
            sum_of_due = 0.0
            sum_of_quantity = 0.0
            sum_of_debits_value = 0.0
            sum_of_credits_value = 0.0

            with open(sum_of_dues_file, 'w') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(["Harvester Name", "due"])
                for key in farmer_details.keys():
                    sum_of_due += farmer_details[key]
                    temp_dict = {}
                    temp_dict['name'] = key
                    temp_dict['due'] = farmer_details[key]
                    all_borrowers.append(temp_dict)
                    spamwriter.writerow([
                        temp_dict['name'],
                        temp_dict['due']
                    ])

                spamwriter.writerow([
                    "",
                    ""
                ])
                spamwriter.writerow([
                    "total",
                    sum_of_due
                ])

            if 'farmer_id' in body:
                if body['farmer_id']:
                    specific_farmer_id = body['farmer_id']

            specific_farmer_debits = []
            specific_farmer_credits = []
            all_farmers_stock_values = {}

            with open(credits_file, 'w') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                count = 0
                for temp in stocklist:

                    if temp.customer:
                        if temp.customer.name in all_farmers_stock_values:
                            all_farmers_stock_values[temp.customer.name] += temp.total_price
                        else:
                            all_farmers_stock_values[temp.customer.name] = temp.total_price

                    if temp.customer.id == specific_farmer_id:
                        if count == 0:


                            spamwriter.writerow([
                                "",
                                ""
                            ])
                            spamwriter.writerow(["Customer name", temp.customer.name])
                            spamwriter.writerow([
                                "",
                                ""
                            ])
                            spamwriter.writerow([
                                "Credit Reports",
                                ""
                            ])
                            spamwriter.writerow(["Date","Bill Number" , "Quantity", "Remarks", "Value"])
                            count += 1
                        obj = {}
                        obj['date'] = temp.bill_date
                        obj['bill_number'] = temp.id
                        obj['total_quantity'] = temp.total_quantity
                        obj['total_price'] = temp.total_price
                        obj['remarks'] = temp.remarks
                        specific_farmer_credits.append(obj)
                        spamwriter.writerow([
                            obj['date'],
                            obj['bill_number'],
                            obj['total_quantity'],
                            obj['remarks'],
                            obj['total_price']
                        ])
                        sum_of_quantity += obj['total_quantity']
                        sum_of_credits_value += obj['total_price']
                        count += 1

            if specific_farmer_id:
                person = Person.objects.get(id=specific_farmer_id)
                advances = person.advance_details.all()
                count = 0
                with open(credits_file, 'a') as csvfile2:
                    spamwriter = csv.writer(csvfile2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    with open(debits_file, 'w') as csvfile:
                        spamwriter2 = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

                        for temp in advances:
                            if temp.amount > 0:
                                obj = {}
                                obj['date'] = temp.paid_date
                                obj['bill_number'] = " "
                                obj['total_quantity'] = " "
                                obj['total_price'] = temp.amount
                                obj['remarks'] = temp.remarks
                                specific_farmer_credits.append(obj)
                                sum_of_credits_value += obj['total_price']
                                spamwriter.writerow([
                                    obj['date'],
                                    " ",
                                    " ",
                                    obj['remarks'],
                                    obj['total_price']
                                ])

                            elif temp.amount < 0 :
                                print 'write debits.................', temp.amount
                                if count == 0:

                                    spamwriter2.writerow([
                                        "",
                                        ""
                                    ])
                                    spamwriter2.writerow([
                                        "Debit Reports",
                                       ""
                                    ])
                                    spamwriter2.writerow([
                                        "date",
                                       "remarks",
                                        "value"
                                    ])
                                    count += 1

                                obj = {}
                                obj['date'] = temp.paid_date
                                obj['remarks'] = temp.remarks
                                obj['value'] = temp.amount
                                specific_farmer_debits.append(obj)
                                spamwriter2.writerow([
                                    obj['date'],
                                    obj['remarks'],
                                    obj['value']
                                ])
                                sum_of_debits_value += obj['value']



            # writing sum of all cols into files
            with open(credits_file, 'a') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                with open(debits_file, 'a') as csvfile:
                    spamwriter2 = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

                    spamwriter2.writerow([
                        " ",
                        " ",
                        ""

                    ])

                    spamwriter2.writerow([
                        "Total",
                        " ",
                        sum_of_debits_value
                    ])
                    spamwriter.writerow([
                        " ",
                        " ",
                        "",
                        ""
                        ""
                    ])
                    spamwriter.writerow([
                        "Total ",
                        " ",
                        sum_of_quantity,
                        " ",
                        sum_of_credits_value
                    ])
            all_keys = []
            all_borrowers = []
            sum_of_due = 0.0
            farmer_keys = farmer_details.keys()
            stock_keys = all_farmers_stock_values.keys()
            all_keys.extend(farmer_keys)
            all_keys.extend(stock_keys)

            print 'all keys are ', all_keys

            with open(sum_of_dues_file, 'w') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(["",""])
                spamwriter.writerow(["Customer Dues Report"])

                for key in list(set(all_keys)):

                    temp_dict = {}
                    temp_dict['name'] = key
                    temp_dict['due'] = 0.0

                    if key in farmer_details:
                        sum_of_due += farmer_details[key]
                        temp_dict['due'] += farmer_details[key]

                    if key in all_farmers_stock_values:
                        sum_of_due += all_farmers_stock_values[key]
                        temp_dict['due'] += all_farmers_stock_values[key]

                    all_borrowers.append(temp_dict)
                    spamwriter.writerow([
                        temp_dict['name'],
                        temp_dict['due']
                    ])

                spamwriter.writerow([
                    "",
                    ""
                ])
                spamwriter.writerow([
                    "Total",
                    sum_of_due
                ])

            # writing to single file
            base_path = BASE_DIR + "/Admin/report_files/"
            all_data_file = open(base_path + "customer_all_report_data.csv", "wb")
            all_data_file.write("Title,Customer Reports\r\n")
            # first file:

            for line in open(base_path + "customer_credits.csv"):
                all_data_file.write(line)

            for line in open(base_path + "customer_debits.csv"):
                all_data_file.write(line)

            for line in open(base_path + "customer_dues_sum.csv"):
                all_data_file.write(line)

            all_data_file.close()

            return Response({"debits": specific_farmer_debits,
                             'credits': specific_farmer_credits,
                             'specific_farmer_data': all_borrowers,
                             'sum_of_quantity': sum_of_quantity,
                             'sum_of_credits': sum_of_credits_value,
                             'sum_of_debits': sum_of_debits_value
                             },
                            status=200)
        except Exception as e:
            print e
            return Response({"stockslist": e}, status=200)
class HarvestersReport(APIView):
    """docstring for ClassName"""


    def post(self, request):
        try:
            body = request.body.decode("utf-8")
            body = json.loads(body)
            specific_farmer_id = False

            divided_start_date = body['start_date'].split("/")
            divided_end_date = body['end_date'].split("/")

            # bill date must be between start and end date
            filter_args = {
                '{0}__{1}'.format('created_date', 'gte'): datetime.datetime(int(divided_start_date[2]),int(divided_start_date[1]), int(divided_start_date[0])),
                '{0}__{1}'.format('created_date', 'lte'): datetime.datetime(int(divided_end_date[2]),int(divided_end_date[1]),int(divided_end_date[0]), 23, 59, 59),
            }

            paid_filter_args = {
                '{0}__{1}'.format('paid_date', 'gte'): datetime.datetime(int(divided_start_date[2]),
                                                                            int(divided_start_date[1]),
                                                                            int(divided_start_date[0])),
                '{0}__{1}'.format('paid_date', 'lte'): datetime.datetime(int(divided_end_date[2]),
                                                                            int(divided_end_date[1]),
                                                                            int(divided_end_date[0]), 23, 59, 59),
            }

            credits_file = BASE_DIR + "/Admin/report_files/harvester_credits.csv"
            debits_file =  BASE_DIR + "/Admin/report_files/harvester_debits.csv"
            sum_of_dues_file = BASE_DIR + "/Admin/report_files/harvester_dues_sum.csv"

            stocklist = SoldStockDetails.objects.filter(**filter_args)
            all_farmers = Person.objects.filter(person_type='harvester')
            farmer_details = {}
            for harvester in all_farmers:
                advances = harvester.advance_details.filter(**paid_filter_args)
                farmer_details[harvester.name] = 0.0
                for advance in advances:
                    farmer_details[harvester.name] += float(advance.amount)

            all_borrowers = []
            sum_of_due = 0.0
            sum_of_quantity = 0.0
            sum_of_debits_value = 0.0
            sum_of_credits_value = 0.0



            if 'farmer_id' in body:
                if body['farmer_id']:
                    specific_farmer_id = body['farmer_id']



            specific_farmer_debits = []
            specific_harvester_credits = []
            all_farmers_stock_values = {}


            with open(debits_file, 'w') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                count = 0
                for temp in stocklist:

                    if temp.harvester and temp.harvester != temp.farmer:
                        if temp.harvester.name in all_farmers_stock_values:
                            all_farmers_stock_values[temp.harvester.name] += temp.harvester_payment
                        else:
                            all_farmers_stock_values[temp.harvester.name] = temp.harvester_payment

                    if temp.harvester.id == specific_farmer_id:
                        if count == 0:
                            spamwriter.writerow(["", "", ""])
                            spamwriter.writerow(["Harvester name", temp.harvester.name])

                            spamwriter.writerow(["", "", ""])
                            spamwriter.writerow(["Debits Report", "", ""])
                            spamwriter.writerow(["date", "particulars_or_remarks", "quantity", "value"])
                            count += 1
                        obj = {}
                        obj['date'] = temp.created_date
                        if temp.stock_object:
                            obj['particulars_remarks'] = temp.stock_object.name
                        else:
                            obj['particulars_remarks'] = ""
                        obj['quantity'] = temp.quantity
                        obj['value'] = temp.harvester_payment
                        specific_farmer_debits.append(obj)
                        spamwriter.writerow([
                            obj['date'],
                            obj['particulars_remarks'],
                            obj['quantity'],
                            obj['value']
                        ])
                        sum_of_quantity += obj['quantity']
                        sum_of_debits_value += obj['value']
                        count += 1

            if specific_farmer_id:
                print "selected Harvester id is", specific_farmer_id
                person = Person.objects.get(id = specific_farmer_id)
                advances = person.advance_details.all()
                count = 0
                with open(credits_file, 'w') as csvfile2:
                    spamwriter = csv.writer(csvfile2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    with open(debits_file, 'a') as csvfile:
                        spamwriter2 = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

                        for temp in advances:
                            if temp.amount > 0:
                                print temp.amount,'&&&&'
                                if count == 0:
                                    spamwriter.writerow(["",""])
                                    spamwriter.writerow(["Credit Reports", ""])
                                    spamwriter.writerow(["date", "particulars", "value"])
                                    count += 1
                                obj = {}
                                obj['date'] = temp.paid_date
                                obj['particulars_remarks'] = temp.remarks
                                obj['value'] = temp.amount
                                specific_harvester_credits.append(obj)
                                spamwriter.writerow([
                                    obj['date'],
                                    obj['particulars_remarks'],
                                    obj['value']
                                ])
                                sum_of_credits_value += obj['value']
                                count +=1
                            elif temp.amount < 0:
                                print 'write debits.................', temp.amount
                                obj = {}
                                obj['date'] = temp.paid_date
                                obj['particulars_remarks'] = temp.remarks
                                obj['value'] = temp.amount
                                specific_farmer_debits.append(obj)
                                spamwriter2.writerow([
                                    obj['date'],
                                    obj['particulars_remarks'],
                                    obj['value']
                                ])
                                sum_of_debits_value += obj['value']

            # writing sum of all cols into files
            with open(credits_file, 'a') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                with open(debits_file, 'a') as csvfile:
                    spamwriter2 = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

                    spamwriter2.writerow([
                        "",
                        " ",
                        "",
                        ""
                    ])

                    spamwriter2.writerow([
                        "Total",
                        " ",
                        sum_of_quantity,
                        sum_of_debits_value
                    ])
                    spamwriter.writerow([
                        " ",
                        " ",
                        "",
                        ""
                    ])
                    spamwriter.writerow([
                        "Total ",
                        " ",
                        sum_of_credits_value
                    ])

            all_keys = []
            all_borrowers = []
            sum_of_due = 0.0
            farmer_keys = farmer_details.keys()
            stock_keys = all_farmers_stock_values.keys()
            all_keys.extend(farmer_keys)
            all_keys.extend(stock_keys)

            print 'all keys are ', all_keys

            with open(sum_of_dues_file, 'w') as csvfile:
                    spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    spamwriter.writerow(["", ""])
                    spamwriter.writerow(["Dues Report", ""])
                    spamwriter.writerow(["Harvester Name", "due"])

                    for key in list(set(all_keys)):

                        temp_dict = {}
                        temp_dict['name'] = key
                        temp_dict['due'] = 0.0

                        if key in farmer_details:
                            sum_of_due += farmer_details[key]
                            temp_dict['due'] += farmer_details[key]

                        if key in all_farmers_stock_values:
                            sum_of_due += all_farmers_stock_values[key]
                            temp_dict['due'] -= all_farmers_stock_values[key]

                        all_borrowers.append(temp_dict)
                        spamwriter.writerow([
                            temp_dict['name'],
                            temp_dict['due']
                        ])

                    spamwriter.writerow([
                        "",
                        ""
                    ])
                    spamwriter.writerow([
                        "total",
                        sum_of_due
                    ])

            # writing to single file
            base_path = BASE_DIR + "/Admin/report_files/"
            all_data_file = open(base_path + "harvester_all_report_data.csv", "wb")
            all_data_file.write("Title,Harvester Reports\r\n")
            # first file:
            for line in open(base_path + "harvester_debits.csv"):
                all_data_file.write(line)

            for line in open(base_path + "harvester_credits.csv"):
                all_data_file.write(line)

            for line in open(base_path + "harvester_dues_sum.csv"):
                all_data_file.write(line)

            all_data_file.close()

            return Response({"debits": specific_farmer_debits,
                             'credits': specific_harvester_credits,
                             'specific_farmer_data': all_borrowers,
                             'sum_of_quantity': sum_of_quantity,
                             'sum_of_credits': sum_of_credits_value,
                             'sum_of_debits': sum_of_debits_value
                             },
                                status=200)
        except Exception as e:
            print e
            return Response({"stockslist": e}, status=200)


class FarmersReport(APIView):
    """docstring for ClassName"""

    def post(self, request):
        try:
            body = request.body.decode("utf-8")
            body = json.loads(body)
            specific_farmer_id = False

            divided_start_date = body['start_date'].split("/")
            divided_end_date = body['end_date'].split("/")

            # bill date must be between start and end date
            filter_args = {
                '{0}__{1}'.format('created_date', 'gte'): datetime.datetime(int(divided_start_date[2]),int(divided_start_date[1]), int(divided_start_date[0])),
                '{0}__{1}'.format('created_date', 'lte'): datetime.datetime(int(divided_end_date[2]),int(divided_end_date[1]),int(divided_end_date[0]), 23, 59, 59),
            }

            paid_filter_args = {
                '{0}__{1}'.format('paid_date', 'gte'): datetime.datetime(int(divided_start_date[2]),
                                                                            int(divided_start_date[1]),
                                                                            int(divided_start_date[0])),
                '{0}__{1}'.format('paid_date', 'lte'): datetime.datetime(int(divided_end_date[2]),
                                                                            int(divided_end_date[1]),
                                                                            int(divided_end_date[0]), 23, 59, 59),
            }

            stocklist = SoldStockDetails.objects.filter(**filter_args)
            all_farmers = Person.objects.filter(person_type='farmer')
            farmer_details = {}
            for farmer in all_farmers:
                advances = farmer.advance_details.filter(**paid_filter_args)
                farmer_details[farmer.name] = 0.0
                for advance in advances:
                    farmer_details[farmer.name] += float(advance.amount)

            all_borrowers = []

            sum_of_due = 0.0
            sum_of_quantity = 0.0
            sum_of_debits_value = 0.0
            sum_of_credits_value = 0.0

            file_path = BASE_DIR + "/Admin/report_files/farmer_dues_sum.csv"
            with open(file_path, 'w') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(["", ""])
                spamwriter.writerow(["farmer Name", "due"])


                for key in farmer_details.keys():
                    sum_of_due += farmer_details[key]
                    temp_dict = {}
                    temp_dict['name'] = key
                    temp_dict['due'] = farmer_details[key]
                    all_borrowers.append(temp_dict)
                    spamwriter.writerow([
                        temp_dict['name'],
                        temp_dict['due']
                    ])

                spamwriter.writerow([
                    "",
                    ""
                ])
                spamwriter.writerow([
                    "total",
                    sum_of_due
                ])

            if 'farmer_id' in body:
                if body['farmer_id']:
                    specific_farmer_id = body['farmer_id']
                    #print 'farmer id is', specific_farmer_id



            all_farmers_stock_values = {}
            specific_farmer_debits1 = []
            specific_farmer_credits = []

            file_path = BASE_DIR + "/Admin/report_files/farmer_debits.csv"

            with open(file_path, 'w') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                count = 0
                print len(stocklist), "**** length of stock list***"
                for temp in stocklist:
                    if temp.farmer:
                        if temp.farmer.name in all_farmers_stock_values:
                            all_farmers_stock_values[temp.farmer.name] += temp.farmer_payment
                        else:
                            all_farmers_stock_values[temp.farmer.name] = temp.farmer_payment

                    if temp.farmer.id == specific_farmer_id:
                        if count == 0:
                            spamwriter.writerow(["Farmer Name", temp.farmer.name])
                            spamwriter.writerow(["", ""])
                            spamwriter.writerow(["Debits Report", ""])
                            spamwriter.writerow(["date", "particulars_or_remarks", "quantity", "value"])
                            count += 1
                        obj = {}
                        obj['date'] = temp.created_date
                        if temp.stock_object:
                            obj['particulars_remarks'] = temp.stock_object.name
                        else:
                            obj['particulars_remarks'] = ""
                        obj['quantity'] = temp.quantity
                        obj['value'] = temp.farmer_payment
                        specific_farmer_debits1.append(obj)
                        spamwriter.writerow([
                            obj['date'],
                            obj['particulars_remarks'],
                            obj['quantity'],
                            obj['value']
                        ])
                        sum_of_quantity += obj['quantity']
                        sum_of_debits_value += obj['value']
                        count += 1

            print specific_farmer_debits1

            if specific_farmer_id:
                person = Person.objects.get(id = specific_farmer_id)
                advances = person.advance_details.all()
                count = 0
                file_path = BASE_DIR + "/Admin/report_files/farmer_credits.csv"
                file_path1 = BASE_DIR + "/Admin/report_files/farmer_debits.csv"

                with open(file_path, 'w') as csvfile2:
                    spamwriter = csv.writer(csvfile2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    with open(file_path1, 'a') as csvfile:
                        spamwriter2 = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

                        for temp in advances:
                            if temp.amount > 0:
                                if count == 0:
                                    spamwriter.writerow(["", ""])
                                    spamwriter.writerow(["Credits Report", ""])
                                    spamwriter.writerow(["date", "particulars", "value"])

                                    count +=1
                                obj = {}
                                obj['date'] = temp.paid_date
                                obj['particulars_remarks'] = temp.remarks
                                obj['value'] = temp.amount
                                specific_farmer_credits.append(obj)
                                spamwriter.writerow([
                                    obj['date'],
                                    obj['particulars_remarks'],
                                    obj['value']
                                ])
                                sum_of_credits_value += obj['value']
                            elif temp.amount < 0 :
                                #print 'write debits.................', temp.amount
                                obj = {}
                                obj['date'] = temp.paid_date
                                obj['particulars_remarks'] = temp.remarks
                                obj['value'] = temp.amount

                                specific_farmer_debits1.append(obj)

                                spamwriter2.writerow([
                                    obj['date'],
                                    obj['particulars_remarks'],
                                    obj['value']
                                ])
                                sum_of_debits_value += obj['value']



            file_path = BASE_DIR + "/Admin/report_files/farmer_credits.csv"
            file_path1 = BASE_DIR + "/Admin/report_files/farmer_debits.csv"

            # writing sum of all cols into files
            with open(file_path, 'a') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                with open(file_path1, 'a') as csvfile:
                    spamwriter2 = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

                    spamwriter2.writerow([
                        " ",
                        " ",
                        "",
                        ""
                    ])

                    spamwriter2.writerow([
                        "Total",
                        " ",
                        sum_of_quantity,
                        sum_of_debits_value
                    ])
                    spamwriter.writerow([
                        " ",
                        " ",
                        "",
                        ""
                    ])
                    spamwriter.writerow([
                        "Total ",
                        " ",
                        sum_of_credits_value
                    ])

            all_keys = []
            all_borrowers = []
            sum_of_due =0.0
            farmer_keys = farmer_details.keys()
            stock_keys = all_farmers_stock_values.keys()
            all_keys.extend(farmer_keys)
            all_keys.extend(stock_keys)


            file_path = BASE_DIR + "/Admin/report_files/farmer_dues_sum.csv"
            with open(file_path, 'w') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(["", ""])
                spamwriter.writerow(["Farmer Dues", ""])

                spamwriter.writerow(["farmer Name", "due"])

                for key in list(set(all_keys)):
                    #print key
                    temp_dict = {}
                    temp_dict['name'] = key
                    temp_dict['due'] = 0.0

                    if key in farmer_details:
                        #print 'sum of due is', farmer_details[key]
                        sum_of_due += farmer_details[key]
                        temp_dict['due'] += farmer_details[key]

                    if key in all_farmers_stock_values:
                        #print 'sum of due is', all_farmers_stock_values[key]
                        sum_of_due += all_farmers_stock_values[key]
                        temp_dict['due'] -= all_farmers_stock_values[key]

                    all_borrowers.append(temp_dict)
                    spamwriter.writerow([
                        temp_dict['name'],
                        temp_dict['due']
                    ])

                spamwriter.writerow([
                    "",
                    ""
                ])
                spamwriter.writerow([
                    "Total",
                    sum_of_due
                ])

            # writing to single file
            base_path = BASE_DIR + "/Admin/report_files/"
            all_data_file = open(base_path+"farmer_all_report_data.csv", "wb")
            all_data_file.write("Title,Farmer Reports\r\n")
            # first file:
            for line in open(base_path+"farmer_debits.csv"):
                all_data_file.write(line)

            for line in open(base_path+"farmer_credits.csv"):
                    all_data_file.write(line)

            for line in open(base_path+"farmer_dues_sum.csv"):
                all_data_file.write(line)

            all_data_file.close()

            return Response({"debits": specific_farmer_debits1,
                             'credits': specific_farmer_credits,
                             'specific_farmer_data': all_borrowers,
                             'sum_of_quantity': sum_of_quantity,
                             'sum_of_credits': sum_of_credits_value,
                             'sum_of_debits': sum_of_debits_value
                             },
                                status=200)
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
            print 'stock is ', body['stock_id']
            # bill date must be between start and end date

            stock_names_object = StockNames.objects.get(id = int(body['stock_id']))
            stock_details_object = StockDetails.objects.get(item_name= stock_names_object)
            filter_args = {
                '{0}__{1}'.format('bill_date', 'gte'): datetime.datetime(int(divided_start_date[2]),
                                                                         int(divided_start_date[1]),
                                                                         int(divided_start_date[0])),
                '{0}__{1}'.format('bill_date', 'lte'): datetime.datetime(int(divided_end_date[2]),
                                                                         int(divided_end_date[1]),
                                                                         int(divided_end_date[0]), 23, 59, 59),
                '{0}__{1}'.format('products_list', 'product'): stock_details_object
            }

            stocklist = Billing.objects.filter(**filter_args)

            info = {}
            quantity_sum = 0.0
            price_sum = 0.0
            response = []

            for temp in stocklist:
                product_info = temp.products_list.get(product=stock_details_object)
                if temp.customer.name in info:
                    info[temp.customer.name]['value'] += product_info.price
                    info[temp.customer.name]['quantity'] += product_info.quantity
                else:
                    info[temp.customer.name] = {
                        'quantity': product_info.quantity,
                        'value': product_info.price
                    }
                quantity_sum += product_info.quantity
                price_sum += product_info.price

            file_path = BASE_DIR + "/Admin/report_files/customer_credits.csv"
            with open(file_path, 'w') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(["Title", "Sale Report"])
                spamwriter.writerow(["Product Name", stock_names_object.name])

                spamwriter.writerow(["", ""])
                spamwriter.writerow(["", ""])
                spamwriter.writerow(["", ""])

                spamwriter.writerow(["Customer Name", "Weight", "Value"])
                for key in info.keys():
                    obj = {}
                    obj['customer_name'] = key
                    obj['weight'] =  info[key]['quantity']
                    obj['value'] = info[key]['value']
                    response.append(obj)
                    spamwriter.writerow([key,
                                         obj['weight'],
                                         obj['value']])
                spamwriter.writerow(["",
                                 "",
                                 ""])
                spamwriter.writerow(["Total",
                                 quantity_sum,
                                 price_sum])




            return Response({"stocks_list": response, 'sum_of_quantity': quantity_sum
                             , 'sum_of_price': price_sum}, status=200)
            #return Response({"stocks_list": [], 'customer_details': [], 'types_data': []},
            #status=200)
        except Exception as e:
            print e
            return Response({"stockslist": e}, status=200)


class BillManagement(View):

    def get(self, request):
        try:

            # if billId is given return bill details
            if 'billId' in request.GET:

                data = Billing.objects.get(id = request.GET['billId'])
                temp_data = data.products_list.all()
                product_list = []

                for temp in temp_data:
                    obj = {}
                    obj['product_name'] = temp.product.item_name.name
                    obj['product_id'] = temp.product.id
                    obj['product_price'] =temp.price
                    obj['product_quantity'] = temp.quantity
                    obj['bill_product_id'] = temp.id
                    obj['per_kg_price'] = temp.per_kg_price
                    obj['isReturned'] = temp.isReturned
                    product_list.append(obj)


                customers = serializers.serialize('json', Person.objects.filter(person_type='customer'))
                bill_info = serializers.serialize('json', [data])
                return json_response({"bill_info": bill_info, 'product_list': product_list, 'customers': customers}, status=200)

            # if customer Id is given return customer all bills
            elif 'customerId' in request.GET:
                customer = Person.objects.get(id = request.GET['customerId'])
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
                customer = Person.objects.get(id = body['bill_details']['customerId'])
                data = Billing.objects.get(id = body['bill_details']['bill_id'])
                data.customer = customer
                data.total_price = float(body['bill_details']['price'])
                if 'bill_date' in body['bill_details']:
                    if body['bill_details']['bill_date']:
                        data.bill_date = datetime.datetime.strptime(str(body['bill_details']['bill_date']), '%d/%m/%Y')
                data.total_quantity= float(body['bill_details']['quantity'])
                data.due = float(body['bill_details']['due'])
                data.total_paid = float(body['bill_details']['paid'])


                data.contact_number = body['bill_details']['contact_number']
                data.vehicle_number = body['bill_details']['vehicle_number']
                data.remarks = body['bill_details']['remarks']

                data.vat_money = float(body['bill_details']['vat_money'])
                data.vat_percentage = float(body['bill_details']['vat_percentage'])

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
                prdct = ProductsList(price=temp['price'], quantity = temp['quantity'], per_kg_price = temp['kgrate'])
                stock_name_object = StockNames.objects.get(id = temp['id'])
                specific_stock = StockDetails.objects.get(item_name = stock_name_object)
                prdct.product = specific_stock
                prdct.save()
                listOfProducts.append(prdct)
                specific_stock.available_stock -= int(temp['quantity'])
                specific_stock.save()




            billingObject = Billing(due = body['due'])
            billingObject.total_paid = body['amount_paid']
            billingObject.vat_percentage = body['vat_percentage']
            billingObject.vat_money = body['vat_money']

            if 'bill_date' in body:
                if body['bill_date']:
                    billingObject.bill_date = datetime.datetime.strptime(body['bill_date'], '%d/%m/%Y')

            billingObject.total_quantity = body['total_quantity']
            billingObject.total_price = body['total_price']
            bill_related_customer = Person.objects.get(id = body['customerId'])
            billingObject.customer = bill_related_customer

            if 'contact_number' in body:
                billingObject.contact_number = body['contact_number']

            if 'vehicle_number' in body:
                billingObject.vehicle_number = body['vehicle_number']

            if 'remarks' in body:
                billingObject.remarks = body['remarks']

            billingObject.save()
            billingObject.products_list.add(*listOfProducts)
            billingObject.save()

            if float(body['amount_paid']):
                if float(body['amount_paid']) > 0:
                    saving_amount = -float(body['amount_paid'])
                else:
                    saving_amount = float(body['amount_paid'])
                ado = AdvanceDetails(amount = saving_amount)
                if 'bill_date' in body:
                    if body['bill_date']:
                        ado.paid_date = datetime.datetime.strptime(body['bill_date'], '%d/%m/%Y')
                ado.bill_id = billingObject.id
                if 'remarks' in body:
                    ado.remarks = str(body['remarks'])
                ado.save()
                bill_related_customer.advance_details.add(ado)

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
            products = bill.products_list.all()
            # increase available stock
            for temp in products:
                print temp.quantity
                temp.product.available_stock += temp.quantity
                temp.product.save()
                # removing product
                temp.delete()

            #advance_objects removing
            advance_objects = AdvanceDetails.objects.filter(bill_id = bill.id)
            for temp in advance_objects:
                temp.delete()

            # deleting bill
            bill.delete()
            return json_response({"status" : "successfully deleted"}, status=200)
        else:
            customer = Person.objects.get(id = body['customer_id'])
            data = Billing.objects.filter(customer = customer).delete()
            return json_response({"status" : "successfully deleted"}, status=200)


    except Exception as e:
        print e
        return json_response({"err" : "No Stock Found"}, status=401)


class DeleteStockNamesOperation(APIView):
    def post(self, request):
            try:
                body_unicode = request.body.decode('utf-8')
                body = json.loads(body_unicode)
                sn = StockNames.objects.get(id = body['id'])
                sn.isActive = False
                sn.save()
                return json_response({"status": "successfully done..."}, status=200)
            except Exception as e:
                print e
                return json_response({"err": "No User Found"}, status=401)


class BillingStockNamesOperation(APIView):
    def get(self, request):
        try:
            st_names = StockNames.objects.filter(isActive=True)
            stock_names = []
            for stock in st_names:
                isExists = StockDetails.objects.filter(item_name=stock)
                if len(isExists):
                    data = {}
                    data['name'] = stock.name
                    data['id'] = stock.id
                    stock_names.append(data)
            return Response({'stock_names': stock_names}, status=200)
        except Exception as e:
            print e
            return Response({'error': 'got error'}, status=405)


class StockNamesOperation(APIView):
    def get(self, request):
        try:
            st_names = StockNames.objects.filter(isActive=True)
            stock_names = []
            for stock in st_names:
                data = {}
                data['name'] = stock.name
                data['id'] = stock.id
                stock_names.append(data)
            return Response({'stock_names': stock_names}, status=200)
        except Exception as e:
            print e
            return Response({'error': 'got error'}, status=405)


    def post(self, request):
            try:
                body_unicode = request.body.decode('utf-8')
                body = json.loads(body_unicode)
                if body['update']:
                    sn = StockNames.objects.get(id = body['id'])
                    sn.name = body['name']
                    sn.save()
                else:
                    sn = StockNames(name = body['name'])
                    sn.isActive = True
                    sn.save()
                    stock_details = StockDetails(item_name=sn)
                    stock_details.save()


                return json_response({"status": "successfully done..."}, status=200)
            except Exception as e:
                print e
                return json_response({"err": "No User Found"}, status=401)


class SpecificPersonData(APIView):
    """fetching data of respective user"""

    def get(self, request, person_id):
        try:
            userdata = Person.objects.get(id=int(person_id))
            user_total_details = {
                "name": userdata.name,
                "address": userdata.address,
                "phone": userdata.phone,

            }

            return Response({"userdata": json.dumps(user_total_details)}, status=200)
        except Exception, e:
            return Response({"response": "userdata not found"}, status=405)



class addPersonPaymentDetails(APIView):


    def post(self, request):
        try:
            body = request.body.decode("utf-8")
            body = json.loads(body)

            customer_payment = AdvanceDetails(amount=body['paid_amount'])
            if 'remarks' in body:
                customer_payment.remarks = body['remarks']
            if 'paid_date' in body:
                if body['paid_date']:
                    customer_payment.paid_date = datetime.datetime.strptime(body['paid_date'], '%d/%m/%Y')

            customer_payment.save()

            farmer = Person.objects.get(id=body['person_id'])
            farmer.advance_details.add(customer_payment)

            return Response({"response": 'successfully added'}, status=200)
        except Exception as e:
            print e
            return Response({"error": "something went wrong..."}, status=405)





class SpecificPersonPayments(APIView):
    """docstring for ClassName"""


    def post(self, request):
        try:
            body = request.body.decode("utf-8")
            body = json.loads(body)

            print body

            if(body['get_data']):
                person = Person.objects.get(id=body['person_id'], person_type=body['person_type'])
                payments = person.advance_details.all()
                print 'found payments ', len(payments)
                serialized_payments_payments = serializers.serialize('json', payments)
                return Response({"response": json.loads(serialized_payments_payments)}, status=200)
            else:
                payment = AdvanceDetails.objects.get(id=body['id'])
                payment.amount = body['amount']

                if 'remarks' in body:
                    payment.remarks = body['remarks']
                if 'paid_date' in body:
                    if body['paid_date']:
                        payment.paid_date = datetime.datetime.strptime(body['paid_date'], '%d/%m/%Y')

                payment.save()
                return Response({"response": "successfully saved ... "}, status=200)
        except Exception as e:
            print e
            return Response({"stockslist": e}, status=200)

class GetPersonsData(APIView):
    """fetching all customer data"""
    def get(self, request, type):
        try:
            users = Person.objects.filter(person_type = type, isActive=True)
            userlist  = []
            for user in users:
                data ={}
                data['name'] = user.name
                data['address'] =  user.address
                data['phone'] = user.phone
                data['user_id'] = user.id
                data['user_type'] = type
                userlist.append(data)

            user_basic_data = userlist
            return Response({'userdata' : user_basic_data}, status = 200)
        except Exception as e:
            print e
            return Response({'error' : 'got error'}, status = 405)



class AddPerson(View):

    def get(self, request):
        return HttpResponse("method not allowed")

    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        try:
            user = Person.objects.filter(name = body['name'])
            if len(user):
                return json_response({"err" : "Farmer already exists with this email id"}, status=401)
            user = Person(name=body['name'], person_type=body['type'])
            if 'phone' in body:
                user.phone=body['phone']
            if 'address' in body:
                user.address = body['address']
            user.save()
            return json_response({"response": "success"}, status=200)
        except Exception as e:
            print e
            return json_response({"err": "something went wrong"}, status=401)

class DeletePerson(APIView):

    def get(self, request):
        return Response({"response": "method not allowed "}, status=405)

    def post(self, request):
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            print body,'============='
            userdata = Person.objects.get(id = str(body['user_id']))
            userdata.isActive = False
            userdata.save()
            return json_response({"status" : "successfully deleted"}, status=200)
        except Exception as e:
            print e
            return json_response({"err" : "No User Found"}, status=401)


class EditPerson(APIView):

    def get(self, request):
        return Response({"response": "method not allowed "}, status=405)
    def post(self, request):
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            user = Person.objects.get(id = str(body['user_id']))
            print body, '------------'
            if 'name' in body:
                user.name = body['name']

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


class GetStock(APIView):

    def get(self, request):
        try:
            labours = Person.objects.values_list('id', 'name', 'phone', 'address')
            dummy_data = []
            print int(labours[0][0])
            for labour in labours:
                obj = {}
                obj['farmer_id'] = int(labour[0])
                obj['farmer_name'] = labour[1]
                obj['farmer_phone'] = labour[2]
                obj['farmer_address'] =labour[3]
                dummy_data.append(obj)

            return json_response({'labours_list': dummy_data}, status=200)
        except Exception as e:
            print e
            return json_response({'error': "something went wrong"}, status=405)



# ------------ harvester payments --------------------
class SpecificHarvesterPayments(APIView):
    """docstring for ClassName"""


    def post(self, request):
        try:
            body = request.body.decode("utf-8")
            body = json.loads(body)

            if(body['get_data']):
                person = Person.objects.get(id=body['person_id'])
                payments = person.advance_details.all()
                serialized_payments_payments = serializers.serialize('json', payments)
                print serialized_payments_payments
                return Response({"response": json.loads(serialized_payments_payments)}, status=200)
            else:
                payment = AdvanceDetails.objects.get(id=body['id'])
                payment.amount = body['amount']
                payment.save()
                return Response({"response": "successfully saved ... "}, status=200)



        except Exception as e:
            print e
            return Response({"stockslist": e}, status=200)



class GetHarvesterDetails(APIView):

    def get(self, request):
        try:
            labours = Person.objects.values_list('id', 'name', 'phone', 'address')
            dummy_data = []
            for labour in labours:
                obj = {}
                obj['harvester_id'] = int(labour[0])
                obj['harvester_name'] = labour[1]
                obj['harvester_phone'] = labour[2]
                obj['harvester_address'] =labour[3]
                dummy_data.append(obj)

            return json_response({'harvesters_list': dummy_data}, status=200)
        except Exception as e:
            print e
            return json_response({'error': "something went wrong"}, status=405)

    def post(self, request):
        try:
            body = request.body.decode("utf-8")
            body = json.loads(body)

            customer_payment = AdvanceDetails(amount=body['paid_amount'])
            customer_payment.save()

            harvester = Person.objects.get(id=body['harvester_id'])
            harvester.advance_details.add(customer_payment)

            return Response({"response": 'successfully added'}, status=200)
        except Exception as e:
            print e
            return Response({"error": "something went wrong..."}, status=405)
# ------------ end of harvester payments -------------


class updateSpecificPurchase(View):

    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        print body
        try:
            harvester = Person.objects.get(id=body['harvester_id'])
            farmer = Person.objects.get(id=body['farmer_id'])

            purchase_item = SoldStockDetails.objects.get(id = body['purchase_id'])

            purchase_item.farmer = farmer
            purchase_item.harvester = harvester

            if 'remarks' in body:
                purchase_item.remarks = body['remarks']
            if 'purchase_date' in body:
                if body['purchase_date']:
                    purchase_item.created_date = datetime.datetime.strptime(body['purchase_date'], '%d/%m/%Y')

            if 'quantity' in body:
                purchase_item.quantity=body['quantity']

            if 'miscellaneous_detections' in body:
                purchase_item.miscellaneous_detections = body['miscellaneous_detections']
            if 'quality' in body:
                purchase_item.quality=body['quality']

            if 'farmer_rate_per_ton' in body:
                purchase_item.farmer_rate_per_ton=body['farmer_rate_per_ton']

            if 'farmer_total_payment' in body:
                purchase_item.farmer_payment=body['farmer_total_payment']

            #if 'farmer_advance' in body:
            #    purchase_item.farmer_advance=body['farmer_advance']

            if 'harvester_rate_per_ton'  in body:
                purchase_item.harvester_rate_per_ton=body['harvester_rate_per_ton']

            if 'harvester_total_payment' in body:
                purchase_item.harvester_payment=body['harvester_total_payment']

            #if 'harvester_advance' in body:
            #    purchase_item.harvester_advance=body['harvester_advance']
            purchase_item.save()

            if 'farmer_advance' in body:
                #t_amount = float(body['farmer_advance']) - float(body['farmer_total_payment'])
                t_amount = float(body['farmer_advance'])
                customer_payment = AdvanceDetails.objects.filter(purchase_id=purchase_item.id)
                if len(customer_payment):
                    customer_payment = customer_payment[0]
                    customer_payment.amount = t_amount
                    customer_payment.save()

                else:

                    customer_payment = AdvanceDetails(amount=float(body['farmer_advance']))
                    customer_payment.purchase_id = purchase_item.id
                    customer_payment.paid_date = purchase_item.created_date
                    customer_payment.save()
                    farmer.advance_details.add(customer_payment)

            return json_response({"response": "successfully updated"}, status=200)
        except Exception as e:
            print e
            return json_response({"error":"success"}, status=405)



class getSpecificPurchase(View):

    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        try:
            temp = SoldStockDetails.objects.get(id = body['purchase_id'])
            obj = {}
            obj['purchaseId'] = temp.id
            obj['quantity'] = temp.quantity
            obj['quality'] = temp.quality

            obj['farmer_amount'] = temp.farmer_payment
            obj['harvester_amount'] = temp.harvester_payment

            obj['farmer_rate_per_ton'] = temp.farmer_rate_per_ton
            obj['harvester_rate_per_ton'] = temp.harvester_rate_per_ton


            obj['miscellaneous_detections'] = temp.miscellaneous_detections

            obj['remarks'] = temp.remarks
            obj['purchased_date'] = str(temp.created_date)


            obj['farmer_name'] = temp.farmer.name
            obj['harvester_name'] = temp.harvester.name
            obj['farmer_id'] = temp.farmer.id
            obj['harvester_id'] = temp.harvester.id
            # getting append data values
            obj['need_to_append'] = True
            append_data = AppendStockDetails.objects.filter(sold_stock_id = temp.id)
            if len(append_data):
                obj['stock_id'] = append_data[0].stock.item_name.id
                obj['stock_name'] = append_data[0].stock.item_name.name


            farmer_advance_details = temp.farmer.advance_details.filter(purchase_id=temp.id)
            harvester_advance_details = temp.farmer.advance_details.filter(purchase_id=temp.id)


            if len(farmer_advance_details):
                obj['farmer_advance'] = farmer_advance_details[0].amount
            else:
                obj['farmer_advance'] = 0

            if len(harvester_advance_details):
                obj['harvester_advance'] = harvester_advance_details[0].amount
            else:

                obj['harvester_advance'] = 0

            # getting users
            harvesters = Person.objects.filter(person_type="harvester")
            harvester_list = []
            for user in harvesters:

                data = {}
                if obj['harvester_id'] == user.id:
                    data['ticked'] = True
                else:
                    data['ticked'] = False
                data['name'] = user.name
                data['address'] = user.address
                data['phone'] = user.phone
                data['userid'] = user.id
                data['type'] = 'harvester'
                harvester_list.append(data)

            farmers = Person.objects.filter(person_type="farmer")

            farmers_list = []
            for user in farmers:
                data = {}
                if obj['farmer_id'] == user.id:
                    data['ticked'] = True
                else:
                    data['ticked'] = False
                data['name'] = user.name
                data['address'] = user.address
                data['phone'] = user.phone
                data['userid'] = user.id
                data['type'] = 'farmer'
                farmers_list.append(data)

            harvester_list.extend(farmers_list)
            return json_response({"response": obj, 'users': harvester_list}, status=200)
        except Exception as e:
            print e
            return json_response({"error":"success"}, status=405)

class DeleteSoldStock(APIView):

    def get(self, request):
        return Response({"response": "method not allowed "}, status=405)

    def post(self, request):
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)

            userdata = SoldStockDetails.objects.get(id = body['purchase_id'])

            print body

            # deleting advance objects based on sold stock id
            advance_details = AdvanceDetails.objects.filter(purchase_id = userdata.id)
            for temp in advance_details:
                temp.delete()

            # append details objects removing
            append_details = AppendStockDetails.objects.filter(sold_stock_id = userdata.id)
            for temp in append_details:
                temp.delete()

            # decreasing available count
            print userdata.stock_object.id
            stock_names_object = userdata.stock_object
            stock_details_object = StockDetails.objects.get(item_name=stock_names_object)
            stock_details_object.available_stock -= userdata.quantity_in_numbers
            stock_details_object.save()

            # removing purvchase object
            userdata.delete()

            return json_response({"status" : "successfully deleted"}, status=200)
        except Exception as e:
            print e
            return json_response({"err" : "No User Found"}, status=401)

class AddPurchase(View):

    def get(self, request):
        try:
            soldStockDetailsObject = SoldStockDetails.objects.all()
            final_result = []
            for temp in soldStockDetailsObject:
                print temp.farmer.name, temp.harvester
                obj = {}
                obj['purchaseId'] = temp.id
                obj['date'] = str(temp.created_date)
                obj['quantity'] = temp.quantity
                obj['quality'] = temp.quality
                obj['farmer_amount'] = temp.farmer_payment
                obj['harvester_amount'] = temp.harvester_payment

                obj['farmer_name'] = temp.farmer.name
                obj['harvester_name'] = temp.harvester.name
                obj['farmer_id'] = temp.farmer.id
                obj['harvester_id'] = temp.harvester.id
                final_result.append(obj)

            return json_response({"response": final_result}, status=200)
        except Exception as e:
            print e
            return json_response({"error": "some thing went wrong"}, status=405)

    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        print body
        try:
            if body['harvester_id'] == body['farmer_id']:
                harvester = Person.objects.get(id = body['harvester_id'])
                farmer = harvester
            else:
                harvester = Person.objects.get(id=body['harvester_id'])
                farmer = Person.objects.get(id=body['farmer_id'])

            purchase_item = SoldStockDetails(quantity=body['quantity'],
                                             farmer_rate_per_ton = body['farmer_rate_per_ton'],
                                             farmer = farmer,
                                             harvester = harvester
                                             )

            if 'quality' in body:
                purchase_item.quality = body['quality']

            if 'quantity_in_numbers' in body:
                purchase_item.quantity_in_numbers = body['quantity_in_numbers']

            if 'miscellaneous_detections' in body:
                purchase_item.miscellaneous_detections = body['miscellaneous_detections']

            if 'harvester_rate_per_ton' in body:
                purchase_item.harvester_rate_per_ton = body['harvester_rate_per_ton']

            if 'remarks' in body:
                purchase_item.remarks = body['remarks']
            if 'purchase_date' in body:
                if body['purchase_date']:
                    purchase_item.created_date = datetime.datetime.strptime(body['purchase_date'], '%d/%m/%Y')
                    print datetime.datetime.strptime(body['purchase_date'], '%d/%m/%Y')

            if 'farmer_total_payment' in body:
                purchase_item.farmer_payment = body['farmer_total_payment']

            if 'harvester_total_payment' in body:
                if body['harvester_total_payment']:
                    purchase_item.harvester_payment = body['harvester_total_payment']
            purchase_item.save()
            # advance adding

            #t_amount = float(body['farmer_advance']) - float(body['farmer_total_payment'])
            if 'farmer_advance' in body:
                customer_payment = AdvanceDetails(amount=float(body['farmer_advance']))
                customer_payment.purchase_id = purchase_item.id
                customer_payment.paid_date = purchase_item.created_date
                customer_payment.save()
                farmer.advance_details.add(customer_payment)

            if 'harvester_advance' in body:
                if str(farmer.id) != str(harvester.id):
                    customer_payment = AdvanceDetails(amount=float(body['harvester_advance']))
                    customer_payment.purchase_id = purchase_item.id
                    customer_payment.paid_date = purchase_item.created_date
                    customer_payment.save()
                    harvester.advance_details.add(customer_payment)



            if 'need_to_append' in body:
                if body['need_to_append']:
                    if 'stock_name' in body:
                        stock = StockNames.objects.get(id=int(body['stock_name']))
                        if 'quantity_in_numbers' in body:

                            purchase_item.stock_object = stock
                            purchase_item.save()
                            stock_details = StockDetails.objects.filter(item_name = stock)
                            if len(stock_details):
                                stock_details_object = stock_details[0]
                                stock_details_object.available_stock += float(body['quantity_in_numbers'])
                                stock_details_object.save()
                            else:
                                stock_details_object = StockDetails(item_name = stock)
                                stock_details_object.available_stock = float(body['quantity_in_numbers'])
                                dd = datetime.datetime.strptime(body['purchase_date'], '%d/%m/%Y')
                                stock_details_object.create_date = dd
                                stock_details_object.month = calendar.month_name[int(dd.month)]
                                if 'remarks' in body:
                                    stock_details_object.remarks = body['remarks']
                                stock_details_object.save()

                            append_stock_object = AppendStockDetails(stock=stock_details_object)
                            append_stock_object.create_date = datetime.datetime.strptime(body['purchase_date'], '%d/%m/%Y')
                            append_stock_object.append_count = float(body['quantity_in_numbers'])
                            append_stock_object.total_stock = stock_details_object.available_stock
                            if 'remarks' in body:
                                append_stock_object.remarks = body['remarks']
                            append_stock_object.sold_stock_id = purchase_item.id
                            append_stock_object.save()

                        else:
                            stock_details = StockDetails.objects.filter(item_name=stock)
                            if not len(stock_details):
                                stock_details_object = StockDetails(item_name=stock)
                                stock_details_object.available_stock = 0.0
                                dd = datetime.datetime.strptime(body['purchase_date'], '%d/%m/%Y')
                                stock_details_object.create_date = dd
                                stock_details_object.month = calendar.month_name[int(dd.month)]
                                if 'remarks' in body:
                                    stock_details_object.remarks = body['remarks']
                                stock_details_object.save()

            return json_response({"response" : "successfully added"}, status=200)
        except Exception as e:

            print e
            return json_response({"error":"success"}, status=405)





class GetFarmersHarvesters(APIView):

    def get(self, request):
        return Response({"response": "method not allowed "}, status=405)

    def post(self, request):
        try:
            harvesters = Person.objects.filter(person_type="harvester")

            harvester_list = []
            for user in harvesters:
                data = {}
                data['name'] = user.name
                data['address'] = user.address
                data['phone'] = user.phone
                data['userid'] = user.id
                data['type'] = 'harvester'
                harvester_list.append(data)



            farmers = Person.objects.filter(person_type="farmer")

            farmers_list = []
            for user in farmers:
                data = {}
                data['name'] = user.name
                data['address'] = user.address
                data['phone'] = user.phone
                data['userid'] = user.id
                data['type'] = 'farmer'
                farmers_list.append(data)

            harvester_list.extend(farmers_list)

            users_basic_data = json.dumps(harvester_list)
            return json_response({"users": users_basic_data}, status=200)


        except Exception as e:
            print e
            return json_response({"err" : "No User Found"}, status=401)

class DeleteHarvester(APIView):

    def get(self, request):
        return Response({"response": "method not allowed "}, status=405)

    def post(self, request):
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            print body,'============='
            userdata = Person.objects.get(id = str(body['user_id']))
            userdata.delete()
            return json_response({"status" : "successfully deleted"}, status=200)
        except Exception as e:
            print e
            return json_response({"err" : "No User Found"}, status=401)

class EditHarvester(APIView):

    def get(self, request):
        return Response({"response": "method not allowed "}, status=405)
    def post(self, request):
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            user = Person.objects.get(id = str(body['user_id']))
            print body, '------------'
            if 'name' in body:
                user.name = body['name']



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


class HarvesterData(APIView):
    """fetching data of respective user"""

    def get(self, request):
        return Response({"response": "method not allowed"}, status=401)
    def post(self, request):
        body =  request.body
        body =  json.loads(body)
        print "userid:", body['userid']

        try:
            userdata =  Person.objects.get(id = int(body['userid']))
            user_total_details = {
                "name" : userdata.name,
                "address" :  userdata.address,
                "phone" : userdata.phone,
            }

            return Response({"userdata": json.dumps(user_total_details)}, status = 200)
        except Exception, e:
            return Response({"response": "userdata not found"},status = 405)


class GetHarvestersData(APIView):
    """fetching all customer data"""
    def get(self, request):
        try:
            users = Person.objects.all()
            userlist  = []
            for user in users:
                data ={}
                data['name'] = user.name
                data['address'] =  user.address
                data['phone'] = user.phone
                data['userid'] = user.id
                userlist.append(data)

            user_basic_data = json.dumps(userlist)
            return Response({'userdata' : user_basic_data}, status = 200)
        except Exception as e:
            print e
            return Response({'error' : 'got error'}, status = 405)

class AddHarvester(View):

    def get(self, request):
        return HttpResponse("method not allowed")

    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        try:
            user = Person.objects.get(phone = str(body['phone']))
            return json_response({"err" : "Farmer already exists with this email id"}, status=401)
        except Exception, e:
            print e
            user = Person(phone=body['phone'],
                             name = body['name'])

            if 'address' in body:
                user.address = body['address']
            user.save()
            return json_response({"response":"success"}, status=200)



class GetStorageStock(APIView):
    """docstring for ClassName"""

    def get(self, request):
        try:
            stocklist = StockDetails.objects.filter(isActive=True)
            stockslist = serializers.serialize('json', stocklist)
            main_data = json.loads(stockslist)

            for temp in main_data:
                stock_names_object = StockNames.objects.get(id = temp['fields']['item_name'])
                temp['fields']['stock_name'] = stock_names_object.name
            print main_data
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
            print body
            stock = StockDetails.objects.get(id = str(body['stockdata']['stockId']))
            print stock.id
            #expired_converted_date = datetime.datetime.strptime(str(body['stockdata']['created_date']),"%d/%m/%Y").date()
            #print expired_converted_date, '============='
            #stock.item_name = body['stockdata']['stock_name']


            #stock.creation_date = expired_converted_date




            if 'a_stock' in body['stockdata']:
                stock.available_stock = body['stockdata']['a_stock']

            if 'i_stock' in body['stockdata']:
                stock.inital_stock = body['stockdata']['i_stock']

            if 'created_date' in body['stockdata']:
                print 'creation data'
                stock.create_date = datetime.datetime.strptime(str(body['stockdata']['created_date']),"%d/%m/%Y").date()

            if 'remarks' in body['stockdata']:
                stock.remarks = body['stockdata']['remarks']

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

class DeleteStock(APIView):

    def get(self, request):
        return Response({"response": "method not allowed "}, status=405)

    def post(self, request):
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            stockdata = StockDetails.objects.get(id = str(body['stockId']))
            stockdata.isActive = False
            stockdata.save()
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
            print bill.bill_date, '=======', bill.id
            bill_details = {}
            bill_details['customer_name'] = bill.customer.name
            bill_details['bill_date'] = str(bill.bill_date)
            bill_details['total_price'] = bill.total_price
            bill_details['total_quantity'] = bill.total_quantity
            bill_details['due'] = bill.due
            bill_details['vat_percentage'] = bill.vat_percentage
            bill_details['vat_money'] = bill.vat_money
            bill_details['contact_number'] = bill.contact_number
            bill_details['vehicle_number'] = bill.vehicle_number
            bill_details['remarks'] = bill.remarks
            bill_details['bill_id'] = int(bill.id)
            products_all_list = bill.products_list.all()
            temp_product_details = []
            for t_product in products_all_list:
                product_details = {}

                product_details['product_name'] = t_product.product.item_name.name
                product_details['total_quantity'] = t_product.quantity
                product_details['total_price'] = t_product.price
                product_details['kgrate'] = t_product.per_kg_price
                product_details['single_price'] = round(float(t_product.price)/float(t_product.quantity),3)
                temp_product_details.append(product_details)
            bill_details['p_details'] = temp_product_details
            print bill_details

            return json_response({"data" : bill_details}, status=200)

        return json_response({"error" : "no bill id found"}, status=400)


    except Exception as e:
        print e, '==========='
        return json_response({"error" : "No Stock Found"}, status=400)


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


class AppendStock(View):

    def get(self, request):
        return HttpResponse("method not allowed")
    def post(self, request):
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            print body

            stock_name = StockNames.objects.get(id=int(body['stockdata']['stock_name']))

            stock = StockDetails.objects.filter(item_name = stock_name)

            if len(stock):
                stock = stock[0]
                if 'a_stock' in body['stockdata']:
                    stock.available_stock += float(body['stockdata']['a_stock'])
                stock.save()
            else:
                if 'a_stock' in body['stockdata']:
                    stock = StockDetails(item_name = stock_name,
                                         available_stock = float(body['stockdata']['a_stock']))
                    stock.save()


            append_stock_details = AppendStockDetails(stock=stock)
            if 'a_stock' in body['stockdata']:
                append_stock_details.append_count = float(body['stockdata']['a_stock'])
            if 'remarks' in body['stockdata']:
                append_stock_details.remarks = body['stockdata']['remarks']
            if 'creation_date' in body['stockdata']:
                append_stock_details.create_date = datetime.datetime.strptime(str(body['stockdata']['creation_date']),
                                                                              "%d/%m/%Y").date()
            append_stock_details.manual_create_or_append_stock_id = stock.id
            append_stock_details.save()


            return json_response({"err" : "stock saved successfully"}, status=200)
        except Exception as e:
            print e
            return json_response({"response":"unable to save stock"}, status=405)


class AddStock(View):
    def get(self, request):
        return HttpResponse("method not allowed")
    def post(self, request):
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)

            stock_name = StockNames.objects.get(id=int(body['stockdata']['stock_name']))

            isStockExits = StockDetails.objects.filter(item_name = stock_name, isActive=True)
            if len(isStockExits):
                return json_response({"response": "stock already saved with same invoice and name"}, status=405)

            stock = StockDetails(item_name = stock_name)

            if 'a_stock' in body['stockdata']:
                stock.available_stock = float(body['stockdata']['a_stock'])

            if 'i_stock' in body['stockdata']:
                stock.inital_stock = body['stockdata']['i_stock']

            if 'remarks' in body['stockdata']:
                stock.remarks = body['stockdata']['remarks']

            if 'creation_date' in body['stockdata']:
                stock.create_date = datetime.datetime.strptime(str(body['stockdata']['creation_date']),"%d/%m/%Y").date()


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


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
                spamwriter.writerow(["create date", "amount" ,"type", "remarks"])

                for temp in stocklist:
                        # increment advance due payment fields
                        obj = {}
                        obj['create_date'] = temp.create_date
                        obj['remarks'] = temp.remarks
                        obj['amount'] = temp.amount
                        obj['type'] = temp.type
                        temp_data.append(obj)

                        spamwriter.writerow([
                            obj['create_date'],
                            obj['amount'],
                            obj['type'],
                            obj['remarks']
                        ])

            return Response({"data": temp_data},status=200)
        except Exception as e:
            print e
            return Response({"stockslist": e}, status=200)


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


            if 'stock_id' in body:
                if body['stock_id']:
                    stock_name = StockNames.objects.get(id=body['stock_id'])
                    sold_stock_object = StockDetails.objects.get(item_name = stock_name)
                    filter_args['stock'] = sold_stock_object



            stocklist = AppendStockDetails.objects.filter(**filter_args)


            # billing information of start end dates in main_data variable



            file_path = BASE_DIR + "/Admin/report_files/append_stock_reports.csv"
            temp_data = []
            with open(file_path, 'w') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(["append_date", "stock_name" ,"append_count", "remarks"])

                for temp in stocklist:
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
                            obj['stock_name'],
                            obj['append_count'],
                            obj['remarks']
                        ])

            return Response({"data": temp_data},status=200)
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
        if status == 1:
            print status
            name = BASE_DIR + "/Admin/report_files/farmer_reports_specific_farmer_purchases.csv"
            f = open(name, 'r')
            myfile = File(f)
            response = HttpResponse(myfile, content_type='application/csv')
            response['Content-Disposition'] = 'attachment; filename=' + name

            return response
        if status == 2:
            name = BASE_DIR + "/Admin/report_files/farmer_reports_customer_purchase_details.csv"
            f = open(name, 'r')
            myfile = File(f)
            response = HttpResponse(myfile, content_type='application/csv')
            response['Content-Disposition'] = 'attachment; filename=' + name
            return response

        if status == 3:
            name = BASE_DIR + "/Admin/report_files/farmer_reports_all_borrowers.csv"
            f = open(name, 'r')
            myfile = File(f)
            response = HttpResponse(myfile, content_type='application/csv')
            response['Content-Disposition'] = 'attachment; filename=' + name
            return response


        return HttpResponse('wrong status given')
    except Exception as e:
        print e
        return HttpResponse('error')

def HarvesterDownloadView(request, status):
    try:
        status = int(status)
        print status
        if status == 1:
            print status
            name = BASE_DIR + "/Admin/report_files/harvester_reports_specific_farmer_purchases.csv"
            f = open(name, 'r')
            myfile = File(f)
            response = HttpResponse(myfile, content_type='application/csv')
            response['Content-Disposition'] = 'attachment; filename=' + name

            return response
        if status == 2:
            name = BASE_DIR + "/Admin/report_files/harvester_reports_all_purchases.csv"
            f = open(name, 'r')
            myfile = File(f)
            response = HttpResponse(myfile, content_type='application/csv')
            response['Content-Disposition'] = 'attachment; filename=' + name
            return response

        if status == 3:
            name = BASE_DIR + "/Admin/report_files/harvester_reports_all_borrowers.csv"
            f = open(name, 'r')
            myfile = File(f)
            response = HttpResponse(myfile, content_type='application/csv')
            response['Content-Disposition'] = 'attachment; filename=' + name
            return response

        return HttpResponse('wrong status given')
    except Exception as e:
        print e
        return HttpResponse('error')

def ProductSaleDownloadView(request, status):
    try:
        status = int(status)
        print status
        if status == 1:
            print status
            name = BASE_DIR + "/Admin/report_files/each_product_sale_report.csv"
            f = open(name, 'r')
            myfile = File(f)
            response = HttpResponse(myfile, content_type='application/csv')
            response['Content-Disposition'] = 'attachment; filename=' + name

            return response
        if status == 2:
            name = BASE_DIR + "/Admin/report_files/customer_purchase_amount_details.csv"
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
        name = BASE_DIR + "/Admin/report_files/append_stock_reports.csv"
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
        print status
        if status == 1:
            print status
            name = BASE_DIR + "/Admin/report_files/customer_reports_specific_person.csv"
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
            name = BASE_DIR + "/Admin/report_files/customer_reports_borrowers.csv"
            f = open(name, 'r')
            myfile = File(f)
            response = HttpResponse(myfile, content_type='application/csv')
            response['Content-Disposition'] = 'attachment; filename=' + name
            return response

        return HttpResponse('wrong status given')

    except Exception as e:
        print e
        return HttpResponse('error')

class CustomersReport(APIView):


    def post(self, request):
        try:
            body = request.body.decode("utf-8")
            body = json.loads(body)
            specific_customer_id = False

            divided_start_date = body['start_date'].split("/")
            divided_end_date = body['end_date'].split("/")

            # bill date must be between start and end date
            filter_args = {
                '{0}__{1}'.format('bill_date', 'gte'): datetime.datetime(int(divided_start_date[2]),int(divided_start_date[1]), int(divided_start_date[0])),
                '{0}__{1}'.format('bill_date', 'lte'): datetime.datetime(int(divided_end_date[2]),int(divided_end_date[1]),int(divided_end_date[0]), 23, 59, 59),
            }


            stocklist = Billing.objects.filter(**filter_args)
            stockslist = serializers.serialize('json', stocklist)


            # billing information of start end dates in main_data variable
            main_data = json.loads(stockslist)



            if 'customer_id' in body:
                if body['customer_id']:
                    specific_customer_id = body['customer_id']

            customer_details = {}
            specific_customer_data = []

            file_path = BASE_DIR + "/Admin/report_files/customer_reports_specific_person.csv"
            with open(file_path, 'wb+') as csvfile:
                spamwriter = csv.writer(csvfile)
                spamwriter.writerow(
                    ["bill number", "bill date", "total_quantity", "final_bill_total",
                     "paid", "due"])

                for temp in main_data:
                    # increment advance due payment fields
                    if str(temp['fields']['customer']) in customer_details:
                        customer_details[str(temp['fields']['customer'])]['total_price'] += temp['fields']['total_price']
                        customer_details[str(temp['fields']['customer'])]['total_quantity'] += temp['fields']['total_quantity']
                        customer_details[str(temp['fields']['customer'])]['due'] += temp['fields']['due']
                        customer_details[str(temp['fields']['customer'])]['total_paid'] += temp['fields']['total_paid']
                    # initialize fields
                    else:
                        customer_details[str(temp['fields']['customer'])] = {
                            'total_price': 0.0,
                            'total_quantity': 0.0,
                            'due': 0.0,
                            'total_paid':0.0
                        }

                        customer_details[str(temp['fields']['customer'])]['total_price'] = temp['fields']['total_price']
                        customer_details[str(temp['fields']['customer'])]['total_quantity']= temp['fields']['total_quantity']
                        customer_details[str(temp['fields']['customer'])]['due']= customer_details[str(temp['fields']['customer'])]['due']
                        customer_details[str(temp['fields']['customer'])]['total_paid'] = customer_details[str(temp['fields']['customer'])]['total_paid']

                    if specific_customer_id:
                        if temp['fields']['customer'] == specific_customer_id:
                            temp_specifc_data = {}
                            temp_specifc_data['bill_id'] = int(temp['pk'])
                            temp_specifc_data['total_price'] = int(temp['fields']['total_price'])
                            temp_specifc_data['total_quantity'] = int(temp['fields']['total_quantity'])
                            temp_specifc_data['total_paid'] = int(temp['fields']['total_paid'])
                            temp_specifc_data['due'] = int(temp['fields']['due'])
                            temp_specifc_data['bill_date'] = str(temp['fields']['bill_date'])
                            specific_customer_data.append(temp_specifc_data)

                            spamwriter.writerow([
                                temp_specifc_data['bill_id'],
                                temp_specifc_data['bill_date'],
                                temp_specifc_data['total_quantity'],
                                temp_specifc_data['total_paid'],
                                temp_specifc_data['due']
                            ])

            all_customers = []
            all_borrowers = []

            file_path = BASE_DIR + "/Admin/report_files/customer_reports_all_customers.csv"
            with open(file_path, 'wb+') as csvfile:
                spamwriter = csv.writer(csvfile)
                spamwriter.writerow(["Customer Name", "Paid", "Total", "due"])


                for key in customer_details.keys():
                    temp_dict = {}
                    temp_dict['name'] = Person.objects.get(id = int(key)).name
                    temp_dict['id'] = key,
                    temp_dict['total_price'] = customer_details[key]['total_price']
                    temp_dict['due'] = customer_details[key]['due']
                    temp_dict['total_quantity'] = customer_details[key]['total_quantity']
                    temp_dict['total_paid'] = customer_details[key]['total_paid']
                    all_customers.append(temp_dict)
                    if float(temp_dict['due']) > 0:
                        all_borrowers.append(temp_dict)
                    spamwriter.writerow([
                        temp_dict['name'],
                        temp_dict['total_paid'],
                        temp_dict['total_price'],
                        temp_dict['due'],
                    ])
            file_path = BASE_DIR + "/Admin/report_files/customer_reports_borrowers.csv"
            with open(file_path, 'wb+') as csvfile:
                spamwriter = csv.writer(csvfile)
                spamwriter.writerow(["Customer Name", "due"])
                for temp in all_borrowers:
                    spamwriter.writerow([temp['name'], temp['due']])

            return Response({"all_borrowers": all_borrowers,
                             'all_customers': all_customers,
                             'specific_bill_data': specific_customer_data},
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
            specific_harvester_id = False

            divided_start_date = body['start_date'].split("/")
            divided_end_date = body['end_date'].split("/")

            # bill date must be between start and end date
            filter_args = {
                '{0}__{1}'.format('created_date', 'gte'): datetime.datetime(int(divided_start_date[2]),int(divided_start_date[1]), int(divided_start_date[0])),
                '{0}__{1}'.format('created_date', 'lte'): datetime.datetime(int(divided_end_date[2]),int(divided_end_date[1]),int(divided_end_date[0]), 23, 59, 59),
                'harvester__person_type': 'harvester'
            }


            stocklist = SoldStockDetails.objects.filter(**filter_args)
            stockslist = serializers.serialize('json', stocklist)


            # billing information of start end dates in main_data variable
            main_data = json.loads(stockslist)


            if 'harvester_id' in body:
                if body['harvester_id']:

                    specific_harvester_id = body['harvester_id']

            harvester_details = {}
            specific_harvester_data = []

            file_path = BASE_DIR + "/Admin/report_files/harvester_reports_specific_farmer_purchases.csv"
            with open(file_path, 'w') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(
                    ["Harvester Name","rate_per_ton_harvester", "total_quantity", "total_quality",
                     "payment", "advance", "due"])

                for temp in main_data:
                    # increment advance due payment fields
                    if str(temp['fields']['harvester']) in harvester_details:
                        harvester_details[str(temp['fields']['harvester'])]['advance'] += temp['fields']['harvester_advance']
                        harvester_details[str(temp['fields']['harvester'])]['total_payment'] += temp['fields']['harvester_payment']
                    # initialize fields
                    else:
                        harvester_details[str(temp['fields']['harvester'])] = {
                            'total_payment': 0.0,
                            'advance': 0.0,
                            'due': 0.0
                        }

                        harvester_details[str(temp['fields']['harvester'])]['total_payment'] = temp['fields']['harvester_payment']
                        harvester_details[str(temp['fields']['harvester'])]['advance']= temp['fields']['harvester_advance']
                        harvester_details[str(temp['fields']['harvester'])]['due']= float(harvester_details[str(temp['fields']['harvester'])]['total_payment']) - float(harvester_details[str(temp['fields']['harvester'])]['advance'])

                    if specific_harvester_id:
                        if temp['fields']['harvester'] == specific_harvester_id:

                            temp['fields']['name'] = Person.objects.get(id=int(temp['fields']['harvester'])).name
                            temp['fields']['main_advance'] = temp['fields']['harvester_advance']
                            specific_harvester_data.append(temp['fields'])

                            spamwriter.writerow([
                                temp['fields']['name'],
                                temp['fields']['harvester_rate_per_ton'],
                                temp['fields']['quantity'],
                                temp['fields']['quality'],
                                temp['fields']['harvester_payment'],
                                temp['fields']['main_advance'],
                                temp['fields']['harvester_payment'] - temp['fields']['main_advance']
                            ])

            all_harvesters = []
            all_borrowers = []
            file_path = BASE_DIR + "/Admin/report_files/harvester_reports_all_purchases.csv"
            with open(file_path, 'w') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(["Harvester Name", "total_payment", "total_advance", "due"])

                for key in harvester_details.keys():
                    temp_dict = {}
                    temp_dict['name'] = Person.objects.get(id = int(key)).name
                    temp_dict['id'] = key,
                    temp_dict['advance'] = harvester_details[key]['advance']
                    temp_dict['due'] = harvester_details[key]['due']
                    temp_dict['total_payment'] = harvester_details[key]['total_payment']
                    all_harvesters.append(temp_dict)
                    if float(temp_dict['due']) < 0:
                        all_borrowers.append(temp_dict)

                    spamwriter.writerow([
                        temp_dict['name'],
                        temp_dict['total_payment'],
                        temp_dict['advance'],
                        temp_dict['due'],
                    ])

            file_path = BASE_DIR + "/Admin/report_files/harvester_reports_all_borrowers.csv"
            with open(file_path, 'w') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(["Harvester Name", "due"])
                for temp in all_borrowers:
                    spamwriter.writerow([temp['name'], temp['due']])

            return Response({"all_borrowers": all_borrowers,
                             'all_harvesters': all_harvesters,
                             'specific_harvester_data': specific_harvester_data},
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


            stocklist = SoldStockDetails.objects.filter(**filter_args)
            stockslist = serializers.serialize('json', stocklist)
            # billing information of start end dates in main_data variable
            main_data = json.loads(stockslist)
            if 'farmer_id' in body:
                if body['farmer_id']:
                    specific_farmer_id = body['farmer_id']

            farmer_details = {}
            specific_farmer_data = []

            file_path = BASE_DIR + "/Admin/report_files/farmer_reports_specific_farmer_purchases.csv"

            with open(file_path, 'w') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(["farmer Name", "rate_per_ton_farmer" ,"rate_per_ton_harvester", "total_quantity", "total_quality", "payment", "advance", "due"])

                for temp in main_data:
                    # increment advance due payment fields
                    if str(temp['fields']['farmer']) in farmer_details:
                        if temp['fields']['farmer_advance']:
                            farmer_details[str(temp['fields']['farmer'])]['advance'] += temp['fields']['farmer_advance']
                        else:
                            farmer_details[str(temp['fields']['farmer'])]['advance'] += temp['fields']['common_advance']
                        if temp['fields']['farmer_payment']:
                            farmer_details[str(temp['fields']['farmer'])]['total_payment'] += temp['fields']['farmer_payment']
                        farmer_details[str(temp['fields']['farmer'])]['due'] = float(farmer_details[str(temp['fields']['farmer'])]['total_payment']) - float(farmer_details[str(temp['fields']['farmer'])]['advance'])
                    # initialize fields
                    else:

                        farmer_details[str(temp['fields']['farmer'])] = {
                            'total_payment': 0.0,
                            'advance': 0.0,
                            'due': 0.0
                        }

                        farmer_details[str(temp['fields']['farmer'])]['total_payment'] = temp['fields']['farmer_payment']
                        if temp['fields']['farmer_advance']:
                            farmer_details[str(temp['fields']['farmer'])]['advance']= temp['fields']['farmer_advance']
                        else:
                            farmer_details[str(temp['fields']['farmer'])]['advance'] = temp['fields']['common_advance']
                        farmer_details[str(temp['fields']['farmer'])]['due']= float(farmer_details[str(temp['fields']['farmer'])]['total_payment']) - float(farmer_details[str(temp['fields']['farmer'])]['advance'])


                    if temp['fields']['farmer'] == specific_farmer_id:

                        temp['fields']['name'] = Person.objects.get(id=int(temp['fields']['farmer'])).name

                        if float(temp['fields']['farmer_advance']):
                            temp['fields']['main_advance'] = temp['fields']['farmer_advance']
                        else:
                            temp['fields']['main_advance'] = temp['fields']['common_advance']

                        if float(temp['fields']['farmer_payment']):
                            temp['fields']['main_payment'] = temp['fields']['farmer_payment']
                        else:
                            temp['fields']['main_payment'] = temp['fields']['common_payment']



                        specific_farmer_data.append(temp['fields'])

                        spamwriter.writerow([
                            temp['fields']['name'],
                            temp['fields']['farmer_rate_per_ton'],
                            temp['fields']['harvester_rate_per_ton'],
                            temp['fields']['quantity'],
                            temp['fields']['quality'],
                            temp['fields']['main_payment'],
                            temp['fields']['main_advance'],
                            temp['fields']['main_payment'] - temp['fields']['main_advance']
                        ])

            all_farmers = []
            all_borrowers = []

            file_path = BASE_DIR + "/Admin/report_files/farmer_reports_customer_purchase_details.csv"

            with open(file_path, 'w') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(["farmer Name", "total_payment", "total_advance","due"])

                for key in farmer_details.keys():
                    temp_dict = {}
                    temp_dict['name'] = Person.objects.get(id = int(key)).name
                    temp_dict['id'] = key,
                    temp_dict['advance'] = farmer_details[key]['advance']
                    temp_dict['due'] = farmer_details[key]['due']
                    temp_dict['total_payment'] = farmer_details[key]['total_payment']
                    all_farmers.append(temp_dict)
                    if float(temp_dict['due']) < 0:
                        all_borrowers.append(temp_dict)

                    spamwriter.writerow([
                        temp_dict['name'],
                        temp_dict['total_payment'],
                        temp_dict['advance'],
                        temp_dict['due'],
                    ])

            file_path = BASE_DIR + "/Admin/report_files/farmer_reports_all_borrowers.csv"

            with open(file_path, 'w') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(["farmer Name", "due"])
                for temp in all_borrowers:
                    spamwriter.writerow([temp['name'],temp['due']])

            return Response({"all_borrowers": all_borrowers,
                                 'all_farmers': all_farmers,
                                 'specific_farmer_data': specific_farmer_data},
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

            # bill date must be between start and end date
            filter_args = {
                '{0}__{1}'.format('bill_date', 'gte'): datetime.datetime(int(divided_start_date[2]),int(divided_start_date[1]), int(divided_start_date[0])),
                '{0}__{1}'.format('bill_date', 'lte'): datetime.datetime(int(divided_end_date[2]),int(divided_end_date[1]),int(divided_end_date[0]), 23, 59, 59)
            }

            stocklist = Billing.objects.filter(**filter_args)
            if len(stocklist):
                stockslist = serializers.serialize('json', stocklist)

                # billing information of start end dates in main_data variable
                main_data = json.loads(stockslist)

                result_products_list = []
                types_data = {}

                for temp in main_data:
                    if(len(temp['fields']['products_list'])):
                        products_data = ProductsList.objects.filter(id__in=temp['fields']['products_list'])
                        products_data_temp = json.loads(serializers.serialize('json', products_data))
                        customer_name = Person.objects.get(id = temp['fields']['customer']).name
                        date_to_bill = str(temp['fields']['bill_date'])
                        print customer_name, date_to_bill
                        for tt in products_data_temp:

                            temp_product = StockDetails.objects.select_related().filter(id = tt['fields']['product'])
                            tt['fields']['specific_product_data'] = json.loads(serializers.serialize('json', temp_product))
                            tt['fields']['specific_product_data'][0]['fields']['item_name'] =  temp_product[0].item_name.name
                            if tt['fields']['specific_product_data'][0]['fields']['item_name'] in types_data:
                                types_data[tt['fields']['specific_product_data'][0]['fields']['item_name']]['price'] += tt['fields']['price']
                                types_data[tt['fields']['specific_product_data'][0]['fields']['item_name']]['quantity'] += tt['fields']['quantity']

                            else:
                                types_data[tt['fields']['specific_product_data'][0]['fields']['item_name']] = {}
                                types_data[tt['fields']['specific_product_data'][0]['fields']['item_name']]['price'] = tt['fields']['price']
                                types_data[tt['fields']['specific_product_data'][0]['fields']['item_name']]['quantity'] = tt['fields']['quantity']

                                types_data[tt['fields']['specific_product_data'][0]['fields']['item_name']]['bill_date'] =  date_to_bill
                                types_data[tt['fields']['specific_product_data'][0]['fields']['item_name']]['customer_name'] = customer_name




                    temp['fields']['products_data'] = products_data_temp
                    print temp['fields']['customer']


                customer_aggregation = Billing.objects.filter(**filter_args).values('customer').annotate(total_price=Sum('total_price'),
                                                            total_paid=Sum('total_paid'),
                                                            due=Sum('due'))

                file_path = BASE_DIR + "/Admin/report_files/customer_purchase_amount_details.csv"
                with open(file_path, 'w') as csvfile:
                    spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    spamwriter.writerow(["Customer Name", "Total Bill Amount", "Total Paid Amount", "Due"])
                    for t in customer_aggregation:
                        customer_details = Person.objects.get(id = int(t['customer']))
                        t['customer_name'] = customer_details.name
                        cpal = 0
                        cp = customer_details.advance_details.all()
                        scp = json.loads(serializers.serialize('json', cp))
                        for tcp in scp:
                            cpal += tcp['fields']['paid_amount']
                            t['total_paid'] += cpal
                            t['due'] -= cpal
                        spamwriter.writerow([t['customer_name'],t['total_price'],t['total_paid'], t['due']])


                file_path = BASE_DIR+"/Admin/report_files/each_product_sale_report.csv"
                with open(file_path, 'w') as csvfile:
                    spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    spamwriter.writerow(["Customer Name", "Bill Date", "Stock Name", "Sold Quantity", "Sold Price"])
                    for key in types_data.keys():
                        temp_dict = {}
                        temp_dict['name'] = key
                        temp_dict['price'] = types_data[key]['price']
                        temp_dict['quantity'] = types_data[key]['quantity']
                        temp_dict['customer_name'] = types_data[key]['customer_name']
                        temp_dict['bill_date'] = types_data[key]['bill_date']
                        spamwriter.writerow([temp_dict['customer_name'],temp_dict['bill_date'], key, types_data[key]['price'],types_data[key]['quantity']])
                        result_products_list.append(temp_dict)
                return Response({"stocks_list": result_products_list, 'customer_details': customer_aggregation, 'types_data': types_data}, status=200)
            return Response({"stocks_list": [], 'customer_details': [], 'types_data': []},
            status=200)
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
                print temp['id'], '*****'
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
                    print 'yes bill date in body', str(datetime.datetime.strptime(body['bill_date'], '%d/%m/%Y'))

                    billingObject.bill_date = datetime.datetime.strptime(body['bill_date'], '%d/%m/%Y')

            billingObject.total_quantity = body['total_quantity']
            billingObject.total_price = body['total_price']
            billingObject.customer = Person.objects.get(id = body['customerId'])

            if 'contact_number' in body:
                billingObject.contact_number = body['contact_number']

            if 'vehicle_number' in body:
                billingObject.vehicle_number = body['vehicle_number']

            if 'remarks' in body:
                billingObject.remarks = body['remarks']

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
            user = Person.objects.get(phone = str(body['phone']))
            return json_response({"err" : "Farmer already exists with this email id"}, status=401)
        except Exception, e:
            print e
            user = Person(phone=body['phone'],
                             name = body['name'], person_type=body['type'])
            if 'address' in body:
                user.address = body['address']
            user.save()
            return json_response({"response":"success"}, status=200)

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

            if 'farmer_advance' in body:
                purchase_item.farmer_advance=body['farmer_advance']

            if 'harvester_rate_per_ton'  in body:
                purchase_item.harvester_rate_per_ton=body['harvester_rate_per_ton']

            if 'harvester_total_payment' in body:
                purchase_item.harvester_payment=body['harvester_total_payment']

            if 'harvester_advance' in body:
                purchase_item.harvester_advance=body['harvester_advance']

            t_amount = float(body['farmer_advance']) - float(body['farmer_total_payment'])
            customer_payment = AdvanceDetails.objects.get(purchase_id=purchase_item.id)
            customer_payment.amount = t_amount
            customer_payment.save()
            purchase_item.save()
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

            obj['farmer_advance'] = temp.farmer_advance
            obj['harvester_advance'] = temp.harvester_advance

            obj['miscellaneous_detections'] = temp.miscellaneous_detections

            obj['remarks'] = temp.remarks
            obj['purchased_date'] = str(temp.created_date)


            obj['farmer_name'] = temp.farmer.name
            obj['harvester_name'] = temp.harvester.name
            obj['farmer_id'] = temp.farmer.id
            obj['harvester_id'] = temp.harvester.id
            # getting append data values
            append_data = AppendStockDetails.objects.filter(sold_stock_id = temp.id)
            if len(append_data):
                obj['need_to_append'] = True
                obj['stock_id'] = append_data[0].stock.item_name.id
            else:
                obj['need_to_append'] = False

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
                                             quality = body['quality'],
                                             farmer_rate_per_ton = body['farmer_rate_per_ton'],
                                             farmer = farmer,
                                             harvester = harvester
                                             )
            if 'miscellaneous_detections' in body:
                purchase_item.miscellaneous_detections = body['miscellaneous_detections']
            if 'harvester_rate_per_ton' in body:
                purchase_item.harvester_rate_per_ton = body['harvester_rate_per_ton']

            if 'remarks' in body:
                purchase_item.remarks = body['remarks']
            if 'purchase_date' in body:
                if body['purchase_date']:
                    purchase_item.created_date =  datetime.datetime.strptime(body['purchase_date'], '%d/%m/%Y')

            if 'harvester_advance' in body:
                purchase_item.harvester_advance = body['harvester_advance']

            if 'farmer_advance' in body:
                purchase_item.farmer_advance = body['farmer_advance']
            if 'farmer_total_payment' in body:
                purchase_item.farmer_payment = body['farmer_total_payment']

            if 'harvester_total_payment' in body:
                if body['harvester_total_payment']:
                    purchase_item.harvester_payment = body['harvester_total_payment']

            purchase_item.save()
            # advance adding

            t_amount = float(body['farmer_advance']) - float(body['farmer_total_payment'])
            customer_payment = AdvanceDetails(amount=t_amount)
            customer_payment.save()

            farmer.advance_details.add(customer_payment)
            customer_payment.purchase_id = purchase_item.id
            customer_payment.save()

            if 'need_to_append' in body:
                if body['need_to_append']:
                    if 'stock_name' in body:
                        stock = StockNames.objects.get(id = int(body['stock_name']))
                        stock_details = StockDetails.objects.filter(item_name = stock)
                        if len(stock_details):
                            stock_details_object = stock_details[0]
                            stock_details_object.available_stock += float(body['quantity'])
                            stock_details_object.save()
                        else:
                            stock_details_object = StockDetails(item_name = stock)
                            stock_details_object.available_stock = float(body['quantity'])
                            dd = datetime.datetime.strptime(body['purchase_date'], '%d/%m/%Y')
                            stock_details_object.create_date = dd
                            stock_details_object.month = calendar.month_name[int(dd.month)]
                            stock_details_object.remarks = body['remarks']
                            stock_details_object.save()

                        append_stock_object = AppendStockDetails(stock=stock_details_object)
                        append_stock_object.create_date = datetime.datetime.strptime(body['purchase_date'], '%d/%m/%Y')
                        append_stock_object.append_count = float(body['quantity'])
                        append_stock_object.total_stock = stock_details_object.available_stock
                        append_stock_object.remarks = body['remarks']
                        append_stock_object.sold_stock_id = purchase_item.id
                        append_stock_object.save()

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

            stock = StockDetails.objects.get(item_name = stock_name)

            if 'a_stock' in body['stockdata']:
                stock.available_stock += float(body['stockdata']['a_stock'])

            stock.save()

            append_stock_details = AppendStockDetails(stock=stock)
            if 'a_stock' in body['stockdata']:
                append_stock_details.append_count = float(body['stockdata']['a_stock'])
            if 'remarks' in body['stockdata']:
                append_stock_details.remarks = body['stockdata']['remarks']
            if 'creation_date' in body['stockdata']:
                append_stock_details.create_date = datetime.datetime.strptime(str(body['stockdata']['creation_date']),"%d/%m/%Y").date()
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
            print body

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

from django_cron import CronJobBase, Schedule

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1 # every 2 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'my_app.my_cron_job'    # a unique code

    def do(self):
        print 'hellooooooooooo'
        pass    # do your thing here
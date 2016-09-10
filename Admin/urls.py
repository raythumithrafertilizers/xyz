from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.views.generic import TemplateView
from Admin.views import *

urlpatterns = patterns('Admin.views',

   # expenditures
   url(r'^add-expenditure', AddExpenditure.as_view()),
   url(r'^edit-expenditure', EditExpenditure.as_view()),
   url(r'^delete-expenditure', DeleteExpenditure.as_view()),

   # reports
   url(r'^products-sale-report', Reports.as_view()),
   url(r'^farmers-report', FarmersReport.as_view()),
   url(r'^harvesters-report', HarvestersReport.as_view()),
   url(r'^customers-report', CustomersReport.as_view()),
   url(r'^stock-append-reports', StockAppendReports.as_view()),
   url(r'^interest-reports', InterestReports.as_view()),
   url(r'^expenditure-reports', ExpenditureReports.as_view()),

   url(r'^get-interests', InterestsReport.as_view()),
   url(r'^save_interest', SaveInterest.as_view()),

   #downloading urls
   url(r'^download-customers-report/(?P<status>\w{0,50})/$', CustomerDownloadView),
   url(r'^download-append-reports$', AppendDownloadView),

    url(r'^download-remain-stock-reports$', AppendDownloadView2),
   url(r'^download-product-sale-report/(?P<status>\w{0,50})/$', ProductSaleDownloadView),
   url(r'^download-farmer-report/(?P<status>\w{0,50})/$', FarmerDownloadView),
   url(r'^download-harvester-report/(?P<status>\w{0,50})/$', HarvesterDownloadView),
   url(r'^download-interest-reports$', InterestDownloadView),
   url(r'^download-paid-reports$', PaidDownloadView),
   url(r'^download-expenditure-reports$', ExpenditureDownloadView),

    #purchase urls
    url(r'^get-farmers-harvesters', GetFarmersHarvesters.as_view()),
    url(r'^add-purchase-details', AddPurchase.as_view()),
    url(r'^delete-purchase-details', DeleteSoldStock.as_view()),
    url(r'^get-specific-purchase-details', getSpecificPurchase.as_view()),
    url(r'^update-specific-purchase-details', updateSpecificPurchase.as_view()),


    url(r'^add-farmer', AddPerson.as_view()),
    url(r'^persons-list/(?P<type>\w{0,50})', GetPersonsData.as_view()),
    url(r'^person-data/(?P<person_id>\w{0,50})', SpecificPersonData.as_view()),
    url(r'^edit-person', EditPerson.as_view()),
    url(r'^delete-person', DeletePerson.as_view()),
    url(r'^add-person-amount',addPersonPaymentDetails.as_view()),
    url(r'^get-specific-person-payments', SpecificPersonPayments.as_view()),

    # stock operation urls
    url(r'^stock-names', StockNamesOperation.as_view()),
    url(r'^billing-stock-names', BillingStockNamesOperation.as_view()),
    url(r'^delete-stock-name', DeleteStockNamesOperation.as_view()),
    url(r'^add-stock', AddStock.as_view()),
    url(r'^append-stock', AppendStock.as_view()),
    url(r'^stock-list', GetStorageStock.as_view()),
    url(r'^get-one-stock', EditStock.as_view()),
    url(r'^edit-stock', EditStock.as_view()),
    url(r'^delete-stock', DeleteStock.as_view()),
    url(r'^get_complete_stock_info', GetCompleteInfo.as_view()),

    url(r'^edit-user', EditUsers.as_view()),
    url(r'^delete-rythu-user', DeleteUser.as_view()),
    url(r'^add-users', AddUser.as_view()),
    url(r'^userlist', GetUsersData.as_view()),
    url(r'^userdata', UserData.as_view()),
    url(r'^bill-management', BillManagement.as_view()),
    url(r'^delete-bill', deleteBill),
    url(r'^print-bill', printBill),
    url(r'^get-bill-by-number', GetBillById),




)
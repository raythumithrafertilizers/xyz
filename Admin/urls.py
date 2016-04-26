from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.views.generic import TemplateView
from Admin.views import *

urlpatterns = patterns('Admin.views',

    url(r'^edit-user', EditUsers.as_view()),
    url(r'^delete-rythu-user', DeleteUser.as_view()),
    url(r'^add-users', AddUser.as_view()),
    url(r'^userlist', GetUsersData.as_view()),
    url(r'^userdata', UserData.as_view()),
    url(r'^add-stock', AddStock.as_view()),
    url(r'^stock-list', GetStock.as_view()),
    url(r'^get-one-stock', EditStock.as_view()),
    url(r'^edit-stock', EditStock.as_view()),
    url(r'^delete-stock', DeleteStock.as_view()),
    url(r'^add-customer', AddCustomer.as_view()),
    url(r'^customers-list', GetCustomerData.as_view()),
    url(r'^customer-data', CustomerData.as_view()),
    url(r'^edit-customer', EditCustomer.as_view()),
    url(r'^delete-rythu-customer', DeleteCustomer.as_view()),
    url(r'^get-graph-data', GraphData.as_view()),

    # billing view
    url(r'^bill-management', BillManagement.as_view()),
    url(r'^delete-bill', deleteBill),
    url(r'^company-bill', CompanyBillsManagement.as_view()),
    url(r'^delete-company-bill', deleteCompanyBill),
    url(r'^print-bill', printBill),

    url(r'^gallery-image', GalleryManagement.as_view()),
    url(r'^delete-gallery-image', deleteGalleryImage),





)
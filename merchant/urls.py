from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.views.generic import TemplateView
from Admin.views import *
from merchant.views import *

urlpatterns = patterns('merchant.views',
    
    url(r'^get_dashboard_details', DashBoard.as_view()),
    url(r'^create_loyality_request', Create_Loyality_Request.as_view()),
    url(r'^get_loyality_cards_for_store', Get_Loyality_List.as_view()),
    url(r'add_customer',Add_Customer.as_view()),
    url(r'^get_customer_list', Get_Customer_List_For_Merchant.as_view()),
    url(r'^view_stamp_detail', Get_Stamp_Details.as_view()),
    url(r'^get_stamps_as_per_loyalty', Show_Stamps_Loyalty_Wise.as_view()),
    url(r'^get_current_stamps', GET_Current_Stamps_Offer_For_Each_Merchant.as_view()),
    url(r'^reedeem_stamps', Reedeem_Stamps_From_Merchant.as_view()),
    url(r'^get_customer_history', Customer_History_For_Merchant.as_view()),
    url(r'^create_bill_vs_stamps', Add_Bill_Vs_Stamps.as_view()),
    url(r'^view_bill_vs_stamps', View_Bill_Vs_Stamps.as_view()),
    url(r'^change_bill_status', Change_Bill_Status.as_view()),
    url(r'^get_stampp_corresponding_to_bill', Get_Stamp_Corresponding_To_Bill.as_view()),
    url(r'^add_stamps', Add_Stamp.as_view()),

    
    )
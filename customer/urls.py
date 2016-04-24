from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.views.generic import TemplateView
from Admin.views import *
from customer.views import *

urlpatterns = patterns('customer.views',
    url(r'^dashboard', Dashboard.as_view()),
    url(r'^viewoffers', StoreOffers.as_view()),
    )

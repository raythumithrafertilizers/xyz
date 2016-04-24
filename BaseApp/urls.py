from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.views.generic import TemplateView
from BaseApp.views import *

urlpatterns = patterns('BaseApp.views',

    url(r'^facebook', FacebookLogin.as_view()),
    url(r'^google', Google.as_view()),
    url(r'^twitter', Twitter.as_view()),
    url(r'^linkedin', LinkedIn.as_view()),
    url(r'^signup', UserRegistration.as_view()),
    url(r'^login', UserLogin.as_view()),

    )

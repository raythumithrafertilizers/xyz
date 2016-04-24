from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.views.generic import TemplateView
from Admin import urls as SuperUserUrls
from BaseApp import urls as BaseUrls
from merchant import urls as merchantUrl
from customer import urls as customerUrl

urlpatterns = [

    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^auth/', include(BaseUrls)),

    url(r'^superuser/', include(SuperUserUrls)),

    url(r'^merchant/', include(merchantUrl)),
    url(r'^customer/', include(customerUrl)),
    
]
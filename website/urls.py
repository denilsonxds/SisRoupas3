from django.conf.urls import url, include
from django.urls import path
from .views import *


urlpatterns = [
    url(r'^$', home, name='website_home'),
    url(r'^sobre$', sobre, name='website_sobre'),
    url(r'^roupas_details$', roupas_details, name='website_roupas_details'),

]

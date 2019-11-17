from django.conf.urls import url, include
from django.urls import path
from .views import financeirohome


urlpatterns = [
    url(r'^$', financeirohome, name='financeiro_home')
]

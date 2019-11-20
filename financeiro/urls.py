from django.conf.urls import url, include
from django.urls import path
from .views import financeirohome, lista_alugueis


urlpatterns = [
    url(r'^$', financeirohome, name='financeiro_home'),
    url(r'^aluguel/$', lista_alugueis, name='financeiro_lista_alugueis')

]   

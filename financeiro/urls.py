from django.conf.urls import url, include
from django.urls import path
from .views import *


urlpatterns = [
    url(r'^$', financeirohome, name='financeiro_home'),
    
    url(r'^aluguel/$', lista_alugueis, name='financeiro_lista_alugueis'),
    url(r'^alugueis_novo/$', aluguel_novo, name='financeiro_aluguel_novo'), #formulario de cadastro
    url(r'^alugueis_update(?P<id>\d+)/$', aluguel_update, name='financeiro_aluguel_update'),
    url(r'^alugueis_delete(?P<id>\d+)/$', aluguel_delete, name='financeiro_aluguel_delete'),

    url(r'^taxa/$', lista_taxas, name='financeiro_lista_taxas'),
    url(r'^taxas_novo/$', taxa_novo, name='financeiro_taxa_novo'), #formulario de cadastro
    url(r'^taxas_update(?P<id>\d+)/$', taxa_update, name='financeiro_taxa_update'),
    url(r'^taxas_delete(?P<id>\d+)/$', taxa_delete, name='financeiro_taxa_delete'),
]   

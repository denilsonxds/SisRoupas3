from django.conf.urls import url, include
from django.urls import path
from .views import *


urlpatterns = [
    url(r'^$', cadastrohome, name='cadastro_home'),
    url(r'^funcionarios/$', lista_funcionarios, name='cadastro_lista_funcionarios'),
    url(r'^funcionarios_novo/$', funcionario_novo, name='cadastro_funcionario_novo'),
    url(r'^clientes/$', lista_clientes, name='cadastro_lista_clientes'),
    url(r'^roupas/$', lista_roupas, name='cadastro_lista_roupas'),
    
]

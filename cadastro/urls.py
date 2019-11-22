from django.conf.urls import url, include
from django.urls import path
from .views import *


urlpatterns = [
    url(r'^$', cadastrohome, name='cadastro_home'),
    #-------funcionarios-----------
    url(r'^funcionarios/$', lista_funcionarios, name='cadastro_lista_funcionarios'), #url para cadastrar clientes
    url(r'^funcionarios_novo/$', funcionario_novo, name='cadastro_funcionario_novo'), #formulario de cadastro
    #---------clientes--------------
    url(r'^clientes/$', lista_clientes, name='cadastro_lista_clientes'), #url para cadastrar clientes
    url(r'^clientes_novo/$', cliente_novo, name='cadastro_cliente_novo'), #formulario cadastro
    #--------roupas---------
    url(r'^roupas/$', lista_roupas, name='cadastro_lista_roupas'), #cadastro de roupa
    url(r'^roupas_novo/$', roupa_novo, name='cadastro_roupa_novo'),
    #----------MarcaRoupa-------
    url(r'^marcaroupas/$', lista_marcaroupas, name='cadastro_lista_marcaroupas'),
    url(r'^marcaroupas_novo/$', marcaroupa_novo, name='cadastro_marcaroupa_novo'),
    #---------TipoRoupa----------
    url(r'^tiporoupas/$', lista_tiporoupas, name='cadastro_lista_tiporoupas'),
    url(r'^tiporoupas_novo/$', tiporoupa_novo, name='cadastro_tiporoupa_novo'),
    #----------Sessao---------
    url(r'^sessao/$', lista_sessao, name='cadastro_lista_sessao'),
    url(r'^sessao_novo/$', sessao_novo, name='cadastro_sessao_novo'),

    
]

from django.conf.urls import url, include
from django.urls import path
from .views import *


urlpatterns = [
    url(r'^$', cadastrohome, name='cadastro_home'),
    #-------funcionarios-----------
    url(r'^funcionarios/$', lista_funcionarios, name='cadastro_lista_funcionarios'), #url para cadastrar clientes
    url(r'^funcionarios_novo/$', funcionario_novo, name='cadastro_funcionario_novo'), #formulario de cadastro
    url(r'^funcionarios_update(?P<id>\d+)/$', funcionario_update, name='cadastro_funcionario_update'),
    #---------clientes--------------
    url(r'^clientes/$', lista_clientes, name='cadastro_lista_clientes'), #url para cadastrar clientes
    url(r'^clientes_novo/$', cliente_novo, name='cadastro_cliente_novo'), #formulario cadastro
    url(r'^clientes_update(?P<id>\d+)/$', cliente_update, name='cadastro_cliente_update'),
    #--------roupas---------
    url(r'^roupas/$', lista_roupas, name='cadastro_lista_roupas'), #cadastro de roupa
    url(r'^roupas_novo/$', roupa_novo, name='cadastro_roupa_novo'),
    url(r'^roupas_update(?P<id>\d+)/$', roupa_update, name='cadastro_roupa_update'),
    #----------MarcaRoupa-------
    url(r'^marcaroupas/$', lista_marcaroupas, name='cadastro_lista_marcaroupas'),
    url(r'^marcaroupas_novo/$', marcaroupa_novo, name='cadastro_marcaroupa_novo'),
    url(r'^marcaroupas_update(?P<id>\d+)/$', marcaroupa_update, name='cadastro_marcaroupa_update'),
    #---------TipoRoupa----------
    url(r'^tiporoupas/$', lista_tiporoupas, name='cadastro_lista_tiporoupas'),
    url(r'^tiporoupas_novo/$', tiporoupa_novo, name='cadastro_tiporoupa_novo'),
    url(r'^tiporoupas_update(?P<id>\d+)/$', tiporoupa_update, name='cadastro_tiporoupa_update'),
    #----------Sessao---------
    url(r'^sessao/$', lista_sessao, name='cadastro_lista_sessao'),
    url(r'^sessao_novo/$', sessao_novo, name='cadastro_sessao_novo'),
    url(r'^sessao_update(?P<id>\d+)/$', sessao_update, name='cadastro_sessao_update'),

    
]

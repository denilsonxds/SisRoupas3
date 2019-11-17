from django.conf.urls import url, include
from django.urls import path
from .views import cadastrohome, lista_funcionarios


urlpatterns = [
    url(r'^$', cadastrohome, name='cadastro_home'),
    url(r'^funcionarios/$', lista_funcionarios, name='cadastro_lista_funcionarios'),

]

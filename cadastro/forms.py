from django.forms import ModelForm
from .models import *


class FuncionarioForm(ModelForm):
    class Meta:
        model = Funcionario
        fields = '__all__'


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


class RoupaForm(ModelForm):
    class Meta:
        model = Roupa
        fields = '__all__'


class MarcaRoupaForm(ModelForm):
    class Meta:
        model = MarcaRoupa
        fields = '__all__'


class TipoRoupaForm(ModelForm):
    class Meta:
        model = TipoRoupa
        fields = '__all__'


class SessaoForm(ModelForm):
    class Meta:
        model = Sessao
        fields = '__all__'


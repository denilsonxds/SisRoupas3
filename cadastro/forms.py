from django.forms import ModelForm
from .models import *

class FuncionarioForm(ModelForm):
    class Meta:
        model = Funcionario
        fields = '__all__'

    
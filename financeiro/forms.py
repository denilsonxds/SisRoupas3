from django.forms import ModelForm
from .models import *


class TaxasForm(ModelForm):
    class Meta:
        model = Taxas
        fields = '__all__'


class AluguelForm(ModelForm):
    class Meta:
        model = Aluguel
        fields = '__all__'
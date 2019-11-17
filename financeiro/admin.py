from django.contrib import admin
from .models import Aluguel

class AluguelAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'roupa', 'valor', 'data_retirada', 'data_devolucao', 'dias_totais', 'total',
    'pago')

admin.site.register(Aluguel, AluguelAdmin)
#admin.site.register(Taxas)

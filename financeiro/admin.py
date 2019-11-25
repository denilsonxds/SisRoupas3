from django.contrib import admin
from .models import Aluguel, Taxas

class AluguelAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'roupa', 'valor', 'data_retirada', 'data_devolucao', 'dias_totais', 'total',
    'pago')

class TaxaAdmin(admin.ModelAdmin):
    list_display = ('tipo_taxa', 'valor_taxa')

admin.site.register(Aluguel, AluguelAdmin)
admin.site.register(Taxas, TaxaAdmin)

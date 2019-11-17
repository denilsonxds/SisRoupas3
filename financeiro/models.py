from django.db import models
from cadastro.models import *
import math

"""
class Taxas(models.Model):

    tipo_taxa = models.CharField(max_length=30, blank=True, null=True)
    valor_taxa = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.tipo_taxa
 """       
class Aluguel(models.Model):

    cliente = models.ForeignKey(Cliente, on_delete='CASCADE')
    roupa = models.ForeignKey(Roupa, on_delete='CASCADE')
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    data_retirada = models.DateTimeField(auto_now=False)
    data_devolucao = models.DateTimeField(auto_now=False, blank=True, null=True)
    #taxa = models.ForeignKey(Taxas, on_delete="CASCADE")
    pago = models.BooleanField(default=False)

    def dias_totais(self):
        return math.ceil((self.data_devolucao - self.data_retirada).total_seconds() / 86400)

    def total(self):
        return self.valor * self.dias_totais()

    def __str__(self):
        return "Roupa " + self.roupa.nome_roupa + " Alugada"
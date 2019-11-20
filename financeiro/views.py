from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def financeirohome(request):
    context = {'mensagem' : 'Olá mundo...'}
    return render(request, 'financeiro/index.html', context)


def lista_alugueis(request):
    aluguel = Aluguel.objects.all()
    return render(request, 'financeiro/lista_aluguel.html', {'aluguel': aluguel})
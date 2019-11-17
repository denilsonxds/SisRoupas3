from django.shortcuts import render
from django.http import HttpResponse

def financeirohome(request):
    context = {'mensagem' : 'Olá mundo...'}
    return render(request, 'financeiro/index.html', context)

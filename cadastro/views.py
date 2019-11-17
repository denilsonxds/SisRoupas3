from django.shortcuts import render
from django.http import HttpResponse

def cadastrohome(request):
    context = {'mensagem' : 'Olá mundo2...'}
    return render(request, 'cadastro/index.html', context)

def lista_funcionarios(request):
    return render(request, 'cadastro/lista_funcionarios.html')

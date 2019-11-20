from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Funcionario, Cliente, Roupa
from .forms import FuncionarioForm


def cadastrohome(request):
    context = {'mensagem' : 'Olá mundo2...'}
    return render(request, 'cadastro/index.html', context)


def lista_funcionarios(request):
    funcionario = Funcionario.objects.all()
    form = FuncionarioForm()
    data = {'funcionario': funcionario, 'form': form}
    return render(request, 'cadastro/lista_funcionarios.html', data)


def funcionario_novo(request):
    form = FuncionarioForm(request.POST or None)
    if form.is_valid():
        form.save
    return redirect('cadastro_lista_funcionarios')

def lista_clientes(request):
    cliente = Cliente.objects.all()
    return render(request, 'cadastro/lista_clientes.html', {'cliente': cliente})


def lista_roupas(request):
    roupa = Roupa.objects.all()
    return render(request, 'cadastro/lista_roupas.html', {'roupa': roupa})


from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Funcionario, Cliente, Roupa
from .forms import *


def cadastrohome(request):
    context = {'mensagem' : 'Olá mundo2...'}
    return render(request, 'cadastro/index.html', context)

#-----------------Funcionarios------------------

def lista_funcionarios(request):
    funcionario = Funcionario.objects.all()
    form = FuncionarioForm()
    data = {'funcionario': funcionario, 'form': form}
    return render(request, 'cadastro/lista_funcionarios.html', data)


def funcionario_novo(request):
    form = FuncionarioForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('cadastro_lista_funcionarios')

#-------------Cliente----------------------


def cliente_novo(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('cadastro_lista_clientes')

def lista_clientes(request):
    cliente = Cliente.objects.all()
    form = ClienteForm()
    data = {'cliente' : cliente, 'form' : form}
    return render(request, 'cadastro/lista_clientes.html', data)

#----------Roupas --------------

def lista_roupas(request):
    roupa = Roupa.objects.all()
    form = RoupaForm()
    data = {'roupa' : roupa, 'form' : form}
    return render(request, 'cadastro/lista_roupas.html', data)

def roupa_novo(request):
    form = RoupaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('cadastro_lista_roupas')


#------------MarcaRoupas---------

def lista_marcaroupas(request):
    marcaroupa = MarcaRoupa.objects.all()
    form = MarcaRoupaForm()
    data = {'marcaroupa' : marcaroupa, 'form' : form}
    return render(request, 'cadastro/lista_marcaroupas.html', data)

def marcaroupa_novo(request):
    form = MarcaRoupaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('cadastro_lista_marcaroupas')

#-----------TipoRoupas----------

def lista_tiporoupas(request):
    tiporoupa = TipoRoupa.objects.all()
    form = TipoRoupaForm()
    data = {'tiporoupa' : tiporoupa, 'form' : form}
    return render(request, 'cadastro/lista_tiporoupas.html', data)

def tiporoupa_novo(request):
    form = TipoRoupaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('cadastro_lista_tiporoupas')

#--------Sessao--------------

def lista_sessao(request):
    sessao = Sessao.objects.all()
    form = SessaoForm()
    data = {'sessao' : sessao, 'form' : form}
    return render(request, 'cadastro/lista_sessao.html', data)

def sessao_novo(request):
    form = SessaoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('cadastro_lista_sessao')

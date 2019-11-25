from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

def financeirohome(request):
    context = {'mensagem' : 'Olá mundo...'}
    return render(request, 'financeiro/index.html', context)


@login_required
def lista_alugueis(request):
    aluguel = Aluguel.objects.all()
    form = AluguelForm()
    data = {'aluguel': aluguel, 'form': form}
    return render(request, 'financeiro/lista_aluguel.html', data)

@login_required
def aluguel_novo(request):
    form = AluguelForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('financeiro_lista_alugueis')

@login_required
def aluguel_update(request, id):
    data = {}
    aluguel = Aluguel.objects.get(id=id)
    form = AluguelForm(request.POST or None, instance=aluguel)
    data['aluguel'] = aluguel
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('financeiro_lista_alugueis')
    else:
        return render(request, 'financeiro/update_aluguel.html', data)

@login_required
def aluguel_delete(request, id):
    aluguel = Aluguel.objects.get(id=id)
    if request.method == 'POST':
        aluguel.delete()
        return redirect('financeiro_lista_alugueis')
    else:
        return render(request, 'financeiro/delete_confirm.html', {'obj': aluguel})


def lista_taxas(request):
    taxa = Taxas.objects.all()
    form = TaxasForm()
    data = {'taxa': taxa, 'form': form}
    return render(request, 'financeiro/lista_taxa.html', data)

@login_required
def taxa_novo(request):
    form = TaxasForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('financeiro_lista_taxas')

@login_required
def taxa_update(request, id):
    data = {}
    taxa = Taxas.objects.get(id=id)
    form = TaxasForm(request.POST or None, instance=taxa)
    data['taxa'] = taxa
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('financeiro_lista_taxas')
    else:
        return render(request, 'financeiro/update_taxa.html', data)

@login_required
def taxa_delete(request, id):
    taxa = Taxas.objects.get(id=id)
    if request.method == 'POST':
        taxa.delete()
        return redirect('financeiro_lista_taxas')
    else:
        return render(request, 'financeiro/delete_confirm.html', {'obj': taxa})
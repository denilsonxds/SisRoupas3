from django.shortcuts import render

def home(request):
    return render(request, 'website/index.html')

def sobre(request):
    return render(request, 'website/sobre.html')

def roupas_details(request):
    return render(request, 'website/roupas_details.html')

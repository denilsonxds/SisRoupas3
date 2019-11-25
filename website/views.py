from django.shortcuts import render

def home(request):
    return render(request, 'website/index.html')

def sobre(request):
    return render(request, 'website/sobre.html')

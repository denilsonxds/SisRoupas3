from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path

urlpatterns = [
    url(r'^financeiro/$', include('financeiro.urls')),
    url(r'^cadastro/$', include('cadastro.urls')),
    path('admin/', admin.site.urls),
]

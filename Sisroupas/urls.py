from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path

urlpatterns = [
    url(r'', include('cadastro.urls')),
    url(r'^financeiro/', include('financeiro.urls')),
    path('admin/', admin.site.urls),
]

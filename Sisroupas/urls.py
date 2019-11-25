from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin

urlpatterns = [
    url(r'^', include('website.urls')),
    url(r'^cadastro/', include('cadastro.urls')),
    url(r'^financeiro/', include('financeiro.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

]

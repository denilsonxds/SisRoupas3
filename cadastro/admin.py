from django.contrib import admin
from .models import(
    Cliente, Funcionario,
    MarcaRoupa, TipoRoupa,
    Roupa, Sessao  
)

class RoupaAdmin(admin.ModelAdmin):
    list_display = ('nome_roupa', 'marca', 'tipo_roupa', 'sessao', 'qtd_estoque', 'disponibilidade')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'telefone')

class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'cpf')

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(MarcaRoupa)
admin.site.register(TipoRoupa)
admin.site.register(Roupa, RoupaAdmin)
admin.site.register(Sessao)

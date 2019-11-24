from django.db import models

class Pessoas(models.Model):
    class Meta:
        abstract = True

    nome = models.CharField(max_length=60)
    rg = models.CharField(max_length=20)
    cpf = models.CharField(max_length=11)
    endereco = models.CharField(max_length=160)
    telefone = models.CharField(max_length=16)

class Cliente(Pessoas):
    nada = models.CharField(max_length=2)

    def __str__(self):
        return self.nome

class Funcionario(Pessoas):

    dia_nascimento = models.DateField(auto_now=False)
    email = models.EmailField()
    cargo = models.CharField(max_length=20)
    login = models.CharField(max_length=20)
    senha = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class MarcaRoupa(models.Model):

    marca = models.CharField(max_length=20)

    def __str__(self):
        return self.marca

class TipoRoupa(models.Model):

    tipo_roupa = models.CharField(max_length=30)

    def __str__(self):
        return self.tipo_roupa

class Sessao(models.Model):

    sessao = models.CharField(max_length=20)

    def __str__(self):
        return self.sessao

class Roupa(models.Model):

    nome_roupa = models.CharField(max_length=50)
    marca = models.ForeignKey(MarcaRoupa, on_delete="CASCADE")
    tipo_roupa = models.ForeignKey(TipoRoupa, on_delete="CASCADE")
    sessao = models.ForeignKey(Sessao, on_delete='CASCADE')
    qtd_estoque = models.IntegerField(default=0)
    img_roupa = models.ImageField(width_field=10,height_field=10, blank=True, null=True)
    disponivel = False

    def disponibilidade(self):
        if(self.qtd_estoque == 0):
            self.disponivel = False
            return "Indisponível"
        else:
            self.disponivel = True
            return "Disponivel"


    def __str__(self):
        return self.nome_roupa


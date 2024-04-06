from django.db import models
from core.models import Sistema, Unidade

class Categoria(models.Model):

    nome = models.CharField(max_length=50)
    ativo = models.BooleanField()
    sistema = models.ManyToManyField(Sistema)

    class Meta:
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nome

class Subcategoria(models.Model):

    nome = models.CharField(max_length=50)
    ativo = models.BooleanField()
    categoria = models.ManyToManyField(Categoria)

    class Meta:
        verbose_name_plural = "Subcategorias"

    def __str__(self):
        return self.nome

class Classificacao(models.Model):

    nome = models.CharField(max_length=50)
    ativo = models.BooleanField()
    subcategoria = models.ManyToManyField(Subcategoria)

    class Meta:
        verbose_name_plural = "Classificacoes"

    def __str__(self):
        return self.nome

class Operacao(models.Model):

    nome = models.CharField(max_length=50)
    ativo = models.BooleanField()
    classificacao = models.ManyToManyField(Classificacao)

    class Meta:
        verbose_name_plural = "Operacoes"

    def __str__(self):
        return self.nome

class Estado(models.Model):

    nome = models.CharField(max_length=50)
    ativo = models.BooleanField()
    pendencia = models.BooleanField()
    campo = models.BooleanField()
    encerrado = models.BooleanField()

    unidade = models.ManyToManyField(Unidade)

    class Meta:
        verbose_name_plural = "Estados"

    def __str__(self):
        return self.nome

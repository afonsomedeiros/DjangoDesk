from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

from core.models import Sistema
from accounts.models import User
from campos.models import Categoria, Subcategoria, Classificacao, Operacao

class GrupoConhecimento(models.Model):

    nome = models.CharField(max_length=100)
    sistema = models.ForeignKey(Sistema, on_delete=models.CASCADE)
    ativo = models.BooleanField()
    categoria = models.ForeignKey(Categoria, blank=True, null=True, on_delete=models.CASCADE)
    subcategoria = models.ForeignKey(Subcategoria, blank=True, null=True, on_delete=models.CASCADE)
    classificacao = models.ForeignKey(Classificacao, blank=True, null=True, on_delete=models.CASCADE)
    operacao = models.ForeignKey(Operacao, blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Grupos Conhecimento"

    def __str__(self):
        return self.nome

class Conhecimento(models.Model):

    criador = models.ForeignKey(User, on_delete=models.CASCADE)
    grupo = models.ForeignKey(GrupoConhecimento, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    resumo = models.TextField(max_length=300)
    #conteudo = models.TextField()
    conteudo = RichTextUploadingField()

    class Meta:
        verbose_name_plural = "Conhecimentos"

    def __str__(self):
        return self.titulo

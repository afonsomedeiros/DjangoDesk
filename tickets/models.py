from django.db import models
from accounts.models import User
from core.models import Empresa, Unidade
from campos.models import Categoria, Subcategoria, Classificacao, Operacao, Estado

class Ticket(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    assunto = models.CharField(max_length=100)
    contato = models.CharField(max_length=50)
    telefone_contato = models.CharField(max_length=20)
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    subcategoria = models.ForeignKey(Subcategoria, on_delete=models.CASCADE)
    classificacao = models.ForeignKey(Classificacao, on_delete=models.CASCADE)
    operacao = models.ForeignKey(Operacao, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    registrado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Tickets"

    def __str__(self):
        return self.assunto

class Interacao(models.Model):

    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    descricao = models.TextField()
    interagido_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Interacoes"

    def __str__(self):
        return self.descricao

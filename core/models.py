from django.db import models


class Unidade(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Unidades"

    def __str__(self):
        return self.nome


class Ramal(models.Model):
    setor = models.CharField(max_length=255)
    contato = models.CharField(max_length=70)
    numero = models.CharField(max_length=10)
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE)

    def __str__(self):
        return self.contato

    class Meta:
        verbose_name_plural = "Ramais"


class Sistema(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(max_length=500)
    ativo = models.BooleanField()
    cadastrado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Sistemas"

    def __str__(self):
        return self.nome


class Empresa(models.Model):
    escolhas = [
        ('ativo', 'Ativo'),
        ('inadimplente', 'Inadimplente'),
        ('cancelado', 'Cancelado')
    ]

    nome_fantasia = models.CharField(max_length=200)
    razao_social = models.CharField(max_length=200)
    CNPJ = models.CharField(max_length=20)
    email = models.EmailField(max_length=200)
    telefone = models.CharField(max_length=20)
    situacao = models.CharField(max_length=20, choices=escolhas)
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE)
    sistema = models.ForeignKey(Sistema, on_delete=models.CASCADE)
    cadastrado_em = models.DateTimeField(auto_now=True)
    atualizado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Empresas"

    def __str__(self):
        return self.nome_fantasia

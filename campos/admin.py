from django.contrib import admin
from .models import Categoria, Subcategoria, Classificacao, Operacao, Estado

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Subcategoria)
admin.site.register(Classificacao)
admin.site.register(Operacao)
admin.site.register(Estado)
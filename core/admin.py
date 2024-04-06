from django.contrib import admin

# Register your models here.
from core.models import *



admin.site.register(Unidade)
admin.site.register(Sistema)
admin.site.register(Empresa)

#admin.site.unregister(Categoria)
#admin.site.unregister(Subcategoria)
#admin.site.unregister(Classificacao)
#admin.site.unregister(Operacao)
#admin.site.unregister(Estado)

#admin.site.register(Ticket)
#admin.site.register(Interacao)
admin.site.register(Ramal)
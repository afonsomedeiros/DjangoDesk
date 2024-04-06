from django.contrib import admin
from django.urls import path

from . import views as v

urlpatterns = [
	path('', v.tickets, name="tickets"),
	path('novo/', v.novo_ticket, name="novo_ticket"),
	path('json/categorias/', v.JSON_categorias, name="JSON_categorias"),
	path('json/subcategorias/', v.JSON_subcategorias, name="JSON_subcategorias"),
	path('json/classificacoes/', v.JSON_classificacoes, name="JSON_classificacoes"),
	path('json/operacoes/', v.JSON_operacoes, name="JSON_operacoes"),
	path('json/estados/', v.JSON_estados, name="JSON_estados"),
	# Para filtrar os tickets
	path('categorias/', v.tickets_categoria, name="tickets_categoria"),
	path('subcategorias/', v.tickets_subcategoria, name="tickets_subcategorias"),
	path('classificacoes/', v.tickets_classificacao, name="tickets_classificacoes"),
	path('operacoes/', v.tickets_operacao, name="tickets_operacoes"),
	path('estados/', v.tickets_estado, name="tickets_estados"),
	path('sistemas/', v.tickets_sistema, name="tickets_sistemas"),
	path('unidades/', v.tickets_unidade, name="tickets_unidades"),
	path('users/', v.tickets_user, name="tickets_users"),
	# Return JSON
	path('json/<int:id>', v.JSON_ticket, name='JSON_ticket'),
	# Interacoes
	path('nova/interacao/<int:id>', v.nova_interacao, name='nova_interacao'),
]
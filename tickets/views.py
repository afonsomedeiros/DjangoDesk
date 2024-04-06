from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator
from django.db.models import Q

import json

from .models import Ticket, Interacao
from .VEIA import VEIAtickets as veia
from core.models import Empresa, Unidade
from campos.models import Categoria, Subcategoria, Classificacao, Operacao, Estado


@login_required
def tickets(request):
	return veia.listar(request, Interacao)


@login_required
def tickets_categoria(request):
	return veia.listar(request, Interacao, 'categoria')


@login_required
def tickets_subcategoria(request):
	return veia.listar(request, Interacao, 'subcategoria')


@login_required
def tickets_classificacao(request):
	return veia.listar(request, Interacao, 'classificacao')


@login_required
def tickets_operacao(request):
	return veia.listar(request, Interacao, 'operacao')
	

@login_required
def tickets_estado(request):
	return veia.listar(request, Interacao, 'estado')


@login_required
def tickets_sistema(request):
	return veia.listar(request, Interacao, 'sistema')


@login_required
def tickets_unidade(request):
	return veia.listar(request, Interacao, 'unidade')


@login_required
def tickets_user(request):
	return veia.listar(request, Interacao, 'user')


@login_required
def JSON_ticket(request, id):
	ticket = Ticket.objects.get(id=id)
	interacoes = Interacao.objects.filter(ticket_id=id).order_by('-id')
	data = {
		'id': ticket.id,
		'unidade_id': ticket.unidade.id,
		'unidade_nome': ticket.unidade.nome,
		'user_id': ticket.user.id,
		'user_name': ticket.user.nome,
		'empresa_id': ticket.empresa.id,
		'empresa_nome': ticket.empresa.nome_fantasia,
		'empresa_cnpj': ticket.empresa.CNPJ,
		'contato': ticket.contato,
		'telefone': ticket.telefone_contato,
		'categoria': ticket.categoria.nome,
		'subcategoria': ticket.subcategoria.nome,
		'classificacao': ticket.classificacao.nome,
		'operacao': ticket.operacao.nome,
		'estado': ticket.estado.nome,
		'interacoes': []
	}
	for interacao in interacoes:
		data['interacoes'].append({
			'interacao_id': interacao.id,
			'descricao': interacao.descricao,
			'data': interacao.interagido_em.strftime('%d/%m/%Y %H:%M')
		})
	return JsonResponse(data)


@login_required
def nova_interacao(request, id):
	ticket = get_object_or_404(Ticket, pk=id)
	data = request.POST
	if data['estados_ticket'] != 0:
		ticket.estado.id = data['estados_ticket']
	interacao = Interacao()
	interacao.ticket = ticket
	interacao.descricao = data['descricao_interacao']
	interacao.save()
	return redirect('/tickets')


@login_required
def novo_ticket(request):
	cliente_id = request.GET.get('cliente_id')
	if cliente_id:
		empresa = get_object_or_404(Empresa, pk=cliente_id)
		tickets = Ticket.objects.filter(empresa_id=cliente_id).order_by("-id")[:10]
		for i in tickets:
			i.registrado_em = i.registrado_em.strftime("%d-%m-%Y")
		return veia.save_ticket(request, Interacao, empresa, tickets)

@login_required
def JSON_categorias(request):
	sistema_id = request.GET.get("sistema")
	lista_categorias = serializers.serialize("json", Categoria.objects.filter(sistema__id=sistema_id))
	return HttpResponse(lista_categorias)


@login_required
def JSON_subcategorias(request):
	categoria_id = request.GET.get("categoria")
	lista_subcategorias = serializers.serialize("json", Subcategoria.objects.filter(categoria__id=categoria_id))
	return HttpResponse(lista_subcategorias)


@login_required
def JSON_classificacoes(request):
	subcategoria_id = request.GET.get("subcategoria")
	lista_classificacoes = serializers.serialize("json", Classificacao.objects.filter(subcategoria__id=subcategoria_id))
	return HttpResponse(lista_classificacoes)


@login_required
def JSON_operacoes(request):
	classificacao_id = request.GET.get("classificacao")
	lista_operacoes = serializers.serialize("json", Operacao.objects.filter(classificacao__id=classificacao_id))
	return HttpResponse(lista_operacoes)


@login_required
def JSON_estados(request):
	unidade_id = request.GET.get("unidade")
	lista_estados = serializers.serialize("json", Estado.objects.filter(unidade__id=unidade_id))
	return HttpResponse(lista_estados)
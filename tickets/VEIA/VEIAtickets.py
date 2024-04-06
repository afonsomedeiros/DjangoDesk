from django.core.paginator import Paginator
from django.forms.models import ModelFormMetaclass
from django.db.models.base import ModelBase
from django.http import HttpRequest
from django.shortcuts import redirect, render, get_object_or_404
from django.db.models import Q

from campos.models import Categoria, Subcategoria, Classificacao, Operacao, Estado
from core.models import Unidade, Empresa, Sistema
from accounts.models import User
from tickets.models import Ticket

def query_field(obj: ModelBase, search: str):
	return obj.objects.filter(Q(ticket__assunto__icontains=search) |
							  Q(descricao__icontains=search)).order_by('id')

def query_categoria(obj: ModelBase, search: str):
	return obj.objects.filter(ticket__categoria_id=search).order_by('id')


def query_subcategoria(obj: ModelBase, search: str):
	return obj.objects.filter(ticket__subcategoria_id=search).order_by('id')


def query_classificacao(obj: ModelBase, search: str):
	return obj.objects.filter(ticket__classificacao_id=search).order_by('id')


def query_operacao(obj: ModelBase, search: str):
	return obj.objects.filter(ticket__operacao_id=search).order_by('id')


def query_estado(obj: ModelBase, search: str):
	return obj.objects.filter(ticket__estado_id=search).order_by('id')


def query_sistema(obj: ModelBase, search: str):
	return obj.objects.filter(ticket__empresa__sistema_id=search).order_by('id')


def query_unidade(obj: ModelBase, search: str):
	return obj.objects.filter(ticket__unidade_id=search).order_by('id')


def query_user(obj: ModelBase, search: str):
	return obj.objects.filter(ticket__user_id=search).order_by('id')


def query_conteudo_campos(tickets, request):
	return {
		'tickets': tickets,
		'categorias': Categoria.objects.filter(ativo=True).order_by("nome"),
		'subcategorias': Subcategoria.objects.filter(ativo=True).order_by("nome"),
		'classificacoes': Classificacao.objects.filter(ativo=True).order_by("nome"),
		'operacoes': Operacao.objects.filter(ativo=True).order_by("nome"),
		'estados': Estado.objects.filter(ativo=True).order_by("nome"),
		'sistemas': Sistema.objects.filter(ativo=True).order_by("nome"),
		'unidades': Unidade.objects.all().order_by("nome"),
		'users': User.objects.filter(is_active=True).order_by("nome"),
		'param_busca': request.GET.get('search') if request.GET.get('search') else None
	}


def return_funcao_campo(func_field='', *param):
	func_campo = {
		'': query_field,
		'categoria': query_categoria, 
		'subcategoria': query_subcategoria,
		'classificacao': query_classificacao,
		'operacao': query_operacao,
		'estado': query_estado,
		'sistema': query_sistema,
		'unidade': query_unidade,
		'user': query_user
	}
	return func_campo[func_field](*param)


def listar(request: HttpRequest, obj: ModelBase, campo=''):
	search = request.GET.get(campo)
	lista_ticket = []
	if search:
		lista_interacao = return_funcao_campo(campo, obj, search)
		for interacao in lista_interacao:
			if interacao.ticket not in lista_ticket:
				lista_ticket.append(interacao.ticket)
	else:
		lista_ticket = Ticket.objects.all().order_by('-id')
	paginator = Paginator(lista_ticket, 10)
	page = request.GET.get('page')
	tickets = paginator.get_page(page)
	return_dict = query_conteudo_campos(tickets, request)
	return render(request, 'tickets/lista_tickets.html', return_dict)

def save_interacao(obj, ticket, data):
	interacao = obj()
	interacao.ticket = ticket
	interacao.descricao = data['descricao_ticket']
	interacao.save()

def save_ticket(request, obj, empresa, tickets):
	if request.method == 'POST':
		data = request.POST
		ticket = Ticket()
		ticket.user = request.user
		ticket.empresa = get_object_or_404(Empresa, pk=data['empresa_ticket'])
		ticket.assunto = data['assunto_ticket']
		ticket.contato = data['contato_ticket']
		ticket.telefone_contato = data['telefone_ticket']
		ticket.unidade = get_object_or_404(Unidade, pk=data['unidade_ticket'])
		ticket.categoria = get_object_or_404(Categoria, pk=data['categorias_ticket'])
		ticket.subcategoria = get_object_or_404(Subcategoria, pk=data['subcategorias_ticket'])
		ticket.classificacao = get_object_or_404(Classificacao, pk=data['classificacoes_ticket'])
		ticket.operacao = get_object_or_404(Operacao, pk=data['operacoes_ticket'])
		ticket.estado = get_object_or_404(Estado, pk=data['estados_ticket'])
		ticket.save()

		save_interacao(obj, ticket, data)
		
		return redirect("/tickets")
	else:
		return render(request, 'tickets/novo_ticket.html', {'empresa': empresa, 'tickets': tickets})
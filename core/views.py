#from datetime import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator
from django.db.models import Q
from django.utils import timezone

from tickets.models import Ticket
from .VEIA import VEIACore
from .dashboard.dashboard import *
from accounts.models import User
from .models import Unidade, Ramal, Sistema, Empresa
from .forms import UnidadeForm, RamalForm, SistemaForm, EmpresaForm


# Create your views here.
@login_required
def home(request):
    dash_info = {'meus': meus_tickets(request),'equipe': tickets_equipe(),'semana': tickets_semana(),
                 'mes': tickets_mes()}
    return render(request, "dashboard/index.html", dash_info)


# Visualizar e listar Usuários
@login_required
def usuarios(request):
    return VEIACore.visualizar(request, User, 'usuarios/lista_usuario.html', 'users')


@login_required
def visualizar_usuario(request, id):
    usuario = get_object_or_404(User, pk=id)
    return render(request, 'usuarios/visualizar.html', {'usuario': usuario})


# Unidades
@login_required
def unidades(request):
    return VEIACore.visualizar(request, Unidade, 'unidades/lista_unidades.html', 'unidades')


@login_required
def unidades_cadastrar(request):
    if request.user.is_admin or request.user.is_superuser:
        return VEIACore.cadastrar(request, UnidadeForm, 'unidades/cadastrar.html', '/unidades')
    else:
        return redirect('/')


@login_required
def unidades_atualizar(request, id):
    unidade = get_object_or_404(Unidade, pk=id)
    if request.user.is_admin or request.user.is_superuser:
        return VEIACore.atualizar(request, UnidadeForm, unidade, 'unidades/atualizar.html', '/unidades')
    else:
        return redirect('/')


@login_required
def unidades_deletar(request, id):
    unidade = get_object_or_404(Unidade, pk=id)
    if request.user.is_admin or request.user.is_superuser:
        unidade.delete()
        return redirect('/unidades')
    else:
        return redirect('/')


# Ramais
@login_required
def JSON_listar_ramais(request, id):
    unidade = serializers.serialize("json", Ramal.objects.filter(unidade__id=id))
    return HttpResponse(unidade)


@login_required
def ramais(request):
    return VEIACore.visualizar(request, Ramal, 'ramais/lista_ramais.html', 'ramais')


@login_required
def ramal_cadastrar(request):
    if request.user.is_admin or request.user.is_superuser:
        return VEIACore.cadastrar(request, RamalForm, 'ramais/cadastrar.html', '/ramais')
    else:
        return redirect('/')


@login_required
def ramal_atualizar(request, id):
    ramal = get_object_or_404(Ramal, pk=id)
    if request.user.is_admin or request.user.is_superuser:
        return VEIACore.atualizar(request, RamalForm, ramal, 'ramais/atualizar.html', '/ramais')
    else:
        return redirect('/')


@login_required
def ramal_deletar(request, id):
    ramal = get_object_or_404(Ramal, pk=id)
    if request.user.is_admin or request.user.is_superuser:
        ramal.delete()
        return redirect('/ramais')
    else:
        return redirect('/')


# Sistemas
@login_required
def sistemas(request):
    return VEIACore.visualizar(request, Sistema, 'sistemas/lista_sistemas.html', 'sistemas')


@login_required
def cadastrar_sistema(request):
    if request.user.is_admin or request.user.is_superuser:
        return VEIACore.cadastrar(request, SistemaForm, 'sistemas/cadastrar.html', '/sistemas')
    else:
        return redirect('/')


@login_required
def atualizar_sistema(request, id):
    sistema = get_object_or_404(Sistema, pk=id)
    if request.user.is_admin or request.user.is_superuser:
        return VEIACore.atualizar(request, SistemaForm, sistema, 'sistemas/atualizar.html', '/sistemas')
    else:
        return redirect('/')


@login_required
def sistema_deletar(request, id):
    sistema = get_object_or_404(Sistema, pk=id)
    if request.user.is_admin or request.user.is_superuser:
        sistema.delete()
        return redirect('/sistemas')
    else:
        return redirect('/')

@login_required
def JSON_qtd_por_sistema(request):
    query = tickets_sistema()
    data = []
    for i in query:
        data.append(i)
    return JsonResponse(data, safe=False)


@login_required
def JSON_qtd_top_5(request):
    query = tickets_top_5()
    data = []
    for i in query:
        data.append(i)
    return JsonResponse(data, safe=False)


@login_required
def JSON_por_dia_semana(request):
    query = tickets_por_dia_semana()
    data = []
    for i in query:
        data.append(i)
    return JsonResponse(data, safe=False)

# Empresas
@login_required
def empresas(request):
    return VEIACore.visualizar(request, Empresa, 'empresas/lista_empresas.html', 'empresas')


@login_required
def cadastrar_empresa(request):
    if request.user.is_admin or request.user.is_superuser:
        return VEIACore.cadastrar(request, EmpresaForm, 'empresas/cadastrar.html', '/empresas')
    else:
        return redirect('/')


@login_required
def atualizar_empresa(request, id):
    empresa = get_object_or_404(Empresa, pk=id)
    if request.user.is_admin or request.user.is_superuser:
        return VEIACore.atualizar(request, EmpresaForm, empresa, 'empresas/atualizar.html', '/empresas')
    else:
        return redirect('/')


@login_required
def empresa_deletar(request, id):
    empresa = get_object_or_404(Empresa, pk=id)
    if request.user.is_admin or request.user.is_superuser:
        empresa.delete()
        return redirect('/emrpesas')
    else:
        return redirect('/')

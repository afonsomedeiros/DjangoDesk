from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from campos.VEIA import VEIACampo
from .models import Categoria, Subcategoria, Classificacao, Operacao, Estado
from .forms import CategoriaForm, SubcategoriaForm, ClassificacaoForm, OperacaoForm, EstadoForm



def campos(request):
    return render(request, 'campos.html')


# Categorias
@login_required
def categorias(request):
    return VEIACampo.visualizar(request, Categoria, 'categorias/lista_categorias.html', 'categorias')


@login_required
def cadastrar_categoria(request):
    if request.user.is_admin or request.user.is_superuser:
        return VEIACampo.cadastrar(request, CategoriaForm, 'categorias/cadastrar.html', '/campos/categorias')
    else:
        return redirect('/')


@login_required
def atualizar_categoria(request, id):
    categoria = get_object_or_404(Categoria, pk=id)
    if request.user.is_admin or request.user.is_superuser:
        return VEIACampo.atualizar(request, CategoriaForm, categoria, 'categorias/cadastrar.html', '/campos/categorias')
    else:
        return redirect('/')


@login_required
def categoria_deletar(request, id):
    categoria = get_object_or_404(Categoria, pk=id)
    return VEIACampo.deletar(request, categoria, '/campos/categorias')


# Subcategorias
@login_required
def subcategorias(request):
    return VEIACampo.visualizar(request, Subcategoria, 'subcategorias/lista_subcategorias.html', 'subcategorias')


@login_required
def cadastrar_subcategoria(request):
    if request.user.is_admin or request.user.is_superuser:
        return VEIACampo.cadastrar(request, SubcategoriaForm, 'subcategorias/cadastrar.html', '/campos/subcategorias')
    else:
        return redirect('/')


@login_required
def atualizar_subcategoria(request, id):
    subcategoria = get_object_or_404(Subcategoria, pk=id)
    if request.user.is_admin or request.user.is_superuser:
        return VEIACampo.atualizar(request, SubcategoriaForm, subcategoria, 'subcategorias/atualizar.html', '/campos/subcategorias')
    else:
        return redirect('/')


@login_required
def subcategoria_deletar(request, id):
    subcategoria = get_object_or_404(Subcategoria, pk=id)
    return VEIACampo.deletar(request, subcategoria, '/campos/subcategorias')


# Classificacao
@login_required
def classificacoes(request):
    return VEIACampo.visualizar(request, Classificacao, 'classificacoes/lista_classificacoes.html', 'classificacoes')


@login_required
def cadastrar_classificacao(request):
    if request.user.is_admin or request.user.is_superuser:
        return VEIACampo.cadastrar(request, ClassificacaoForm, 'classificacoes/cadastrar.html', '/campos/classificacoes')
    else:
        return redirect('/')


@login_required
def atualizar_classificacao(request, id):
    classificacao = get_object_or_404(Classificacao, pk=id)
    if request.user.is_admin or request.user.is_superuser:
        return VEIACampo.atualizar(request, ClassificacaoForm, classificacao, 'classificacoes/atualizar.html',
                                   '/campos/classificacoes')
    else:
        return redirect('/')


@login_required
def classificacao_deletar(request, id):
    classificacao = get_object_or_404(Classificacao, pk=id)
    return VEIACampo.deletar(request, classificacao, '/campos/classificacoes')


# Operacao
@login_required
def operacoes(request):
    return VEIACampo.visualizar(request, Operacao, 'operacoes/lista_operacoes.html', 'operacoes')


@login_required
def cadastrar_operacao(request):
    if request.user.is_admin or request.user.is_superuser:
        return VEIACampo.cadastrar(request, OperacaoForm, 'operacoes/cadastrar.html', '/campos/operacoes')
    else:
        return redirect('/')


@login_required
def atualizar_operacao(request, id):
    operacao = get_object_or_404(Operacao, pk=id)
    if request.user.is_admin or request.user.is_superuser:
        return VEIACampo.atualizar(request, OperacaoForm, operacao, 'operacoes/atualizar.html', '/campos/operacoes')
    else:
        return redirect('/')


@login_required
def operacao_deletar(request, id):
    operacao = get_object_or_404(Operacao, pk=id)
    return VEIACampo.deletar(request, operacao, '/campos/operacoes')


# Estado
@login_required
def estados(request):
    return VEIACampo.visualizar(request, Estado, 'estados/lista_estados.html', 'estados')


@login_required
def cadastrar_estado(request):
    if request.user.is_admin or request.user.is_superuser:
        return VEIACampo.cadastrar(request, EstadoForm, 'estados/cadastrar.html', '/campos/estados')
    else:
        return redirect('/')


@login_required
def atualizar_estado(request, id):
    estado = get_object_or_404(Estado, pk=id)
    if request.user.is_admin or request.user.is_superuser:
        return VEIACampo.atualizar(request, EstadoForm, estado, 'estados/atualizar.html', '/campos/estados')
    else:
        return redirect('/')


@login_required
def estado_deletar(request, id):
    estado = get_object_or_404(Estado, pk=id)
    return VEIACampo.deletar(request, estado, '/campos/estados')
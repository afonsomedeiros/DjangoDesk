from django.core.paginator import Paginator
from django.forms.models import ModelFormMetaclass
from django.db.models.base import ModelBase
from django.http import HttpRequest
from django.shortcuts import redirect, render


def visualizar(request: HttpRequest, obj: ModelBase, template_name: str, ref_name: str):
    search = request.GET.get('search')
    if search:
        lista_estados = obj.objects.filter(nome__contains=search).order_by('id')
    else:
        lista_estados = obj.objects.all().order_by('id')
    paginator = Paginator(lista_estados, 10)
    page = request.GET.get('page')
    obj_page = paginator.get_page(page)
    return render(request, template_name, {ref_name: obj_page})


def cadastrar(request: HttpRequest, form: ModelFormMetaclass, template_path: str, redirect_url: str):
    if request.method == 'POST':
        form = form(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            form.save_m2m()
            return redirect(redirect_url)
    else:
        return render(request, template_path, {'form': form()})


def atualizar(request: HttpRequest, form: ModelFormMetaclass, categoria: ModelBase, template_name: str,
              redirect_url: str):
    if request.method == 'POST':
        form = form(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect(redirect_url)
    else:
        return render(request, template_name, {'form': form(instance=categoria)})


def deletar(request: HttpRequest, obj: ModelBase, redirect_url: str):
    if request.user.is_admin or request.user.is_superuser:
        obj.delete()
        return redirect(redirect_url)
    else:
        return redirect('/')

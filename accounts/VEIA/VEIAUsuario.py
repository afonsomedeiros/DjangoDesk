from django.forms.models import ModelFormMetaclass
from django.db.models.base import ModelBase
from django.http import HttpRequest
from django.shortcuts import redirect, render


def cadastrar(request: HttpRequest, form: ModelFormMetaclass):
    if request.user.is_admin:
        form = form(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            form.save_m2m()
            return redirect('/usuarios')
    else:
        return redirect('/')


def atualizar(request: HttpRequest, form: ModelFormMetaclass, usuario: ModelBase, template_name: str):
    form = form(request.POST, instance=usuario)
    if form.is_valid():
        form.save()
        return redirect('/usuarios')
    else:
        return render(request, template_name, {'error': form.errors, 'form': form})

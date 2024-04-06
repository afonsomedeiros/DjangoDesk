from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.detail import DetailView

from django.utils import timezone

from .models import Conhecimento, GrupoConhecimento



class GrupoConhecimentoListView(ListView):

    model = GrupoConhecimento
    paginate_by = 20
    template_name = "grupoconhecimento/grupoconhecimento_list.html"

    def get_queryset(self):
        if 'search' in self.request.GET:
            self.gruposconhecimentos = GrupoConhecimento.objects.filter(nome__icontains=self.request.GET['search']).order_by("-nome")
            return self.gruposconhecimentos
        else:
            return GrupoConhecimento.objects.all().order_by("-nome")



class GrupoConhecimentoCreateView(CreateView):

    model = GrupoConhecimento
    fields = ["nome", "sistema", "ativo", "categoria", "subcategoria",
              "classificacao", "operacao"]
    template_name = "grupoconhecimento/grupoconhecimento_form.html"
    success_url = "/conhecimento/grupoconhecimento"

    def form_valid(self, form):
        form.instance.criador = self.request.user
        return super().form_valid(form)



class GrupoConhecimentoDetailView(DetailView):

    model = GrupoConhecimento



def grupoconhecimento_deletar(request, id):
    GrupoConhecimento = get_object_or_404(GrupoConhecimento, pk=id)
    if request.user.is_admin or request.user.is_superuser:
        GrupoConhecimento.delete()
        return redirect('/grupoconhecimento/')
    else:
        return redirect('/')


class ConhecimentoListView(ListView):

    model = Conhecimento
    paginate_by = 20
    template_name = "conhecimento/conhecimento_list.html"

    def get_queryset(self):
        
        print(self.request.GET)
        if not self.request.GET:
            return self.model.objects.all().order_by("titulo")
        else:
            for key, value in self.request.GET.items():
                return ConhecimentoListView.__dict__[key](self, value)

    def filtro_search(self, param):
        self.conhecimento = self.model.objects.filter(Q(titulo__icontains=param)|
                                                      Q(resumo__icontains=param)).order_by("titulo")
        return self.conhecimento
        
    def filtro_grupo(self, param):
        self.conhecimento = self.model.objects.filter(grupo__nome__icontains=param).order_by("titulo")
        return self.conhecimento

    def filtro_categoria(self, param):
        self.conhecimento = self.model.objects.filter(grupo__categoria__nome__icontains=param).order_by("titulo")
        return self.conhecimento

    def filtro_subcategoria(self, param):
        self.conhecimento = self.model.objects.filter(grupo__subcategoria__nome__icontains=param).order_by("titulo")
        return self.conhecimento

    def filtro_classificacao(self, param):
        self.conhecimento = self.model.objects.filter(grupo__classificacao__nome__icontains=param).order_by("titulo")
        return self.conhecimento

    def filtro_operacao(self, param):
        self.conhecimento = self.model.objects.filter(grupo__operacao__nome__icontains=param).order_by("titulo")
        return self.conhecimento



class ConhecimentoCreateView(CreateView):

    model = Conhecimento
    fields = ["grupo", "titulo", "resumo", "conteudo"]
    success_url = "/conhecimento"

    def form_valid(self, form):
        form.instance.criador = self.request.user
        return super().form_valid(form)



class ConhecimentoDetailView(DetailView):

    model = Conhecimento



def conhecimento_deletar(request, id):
    conhecimento = get_object_or_404(Conhecimento, pk=id)
    if request.user.is_admin or request.user.is_superuser:
        conhecimento.delete()
        return redirect('/conhecimento/')
    else:
        return redirect('/')
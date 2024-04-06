from django.urls import include, path
from django.contrib.auth.decorators import login_required

from . import views as v

urlpatterns = [
	# Grupo Conhecimento
	path('grupoconhecimento', login_required(v.GrupoConhecimentoListView.as_view())),
    path('grupoconhecimento/novo/', login_required(v.GrupoConhecimentoCreateView.as_view())),
    path('grupoconhecimento/visualizar/<int:pk>', login_required(v.GrupoConhecimentoDetailView.as_view())),
    path('grupoconhecimento/deletar/<int:id>', login_required(v.grupoconhecimento_deletar)),

	# Conhecimento
    path('', login_required(v.ConhecimentoListView.as_view())),
    path('novo/', login_required(v.ConhecimentoCreateView.as_view())),
    path('visualizar/<int:pk>', login_required(v.ConhecimentoDetailView.as_view())),
    path('deletar/<int:id>', login_required(v.conhecimento_deletar)),

]
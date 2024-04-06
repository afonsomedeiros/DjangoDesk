from django.contrib import admin
from django.urls import path

from . import views as v

urlpatterns = [
    # Usuários
    path('usuarios/', v.usuarios, name='usuarios'),
    path('usuarios/visualizar/<int:id>/', v.visualizar_usuario),

    # Unidades
    path('unidades/', v.unidades, name='unidades'),
    path('unidades/cadastrar', v.unidades_cadastrar, name='cadastrar_unidades'),
    path('unidades/atualizar/<int:id>', v.unidades_atualizar, name='atualizar_unidades'),
    path('unidades/deletar/<int:id>', v.unidades_deletar, name='atualizar_unidades'),
    path('unidades/ramais/json/<int:id>', v.JSON_listar_ramais, name='listar_ramais'),

    # Ramais
    path('ramais/', v.ramais, name='ramais'),
    path('ramais/cadastrar', v.ramal_cadastrar, name='ramais'),
    path('ramais/atualizar/<int:id>', v.ramal_atualizar, name='ramais'),
    path('ramais/deletar/<int:id>', v.ramal_deletar, name='ramais'),

    # Sistemas
    path('sistemas/', v.sistemas, name='sistemas'),
    path('sistemas/cadastrar/', v.cadastrar_sistema, name='cadastrar_sistemas'),
    path('sistemas/atualizar/<int:id>', v.atualizar_sistema, name='atualizar_sistema'),
    path('sistemas/deletar/<int:id>', v.sistema_deletar, name='atualizar_sistema'),

    # Empresas
    path('empresas/', v.empresas, name='empresas'),
    path('empresas/cadastrar', v.cadastrar_empresa, name='empresas_cadastrar'),
    path('empresas/atualizar/<int:id>', v.atualizar_empresa, name='empresas_atualizar'),
    path('empresas/deletar/<int:id>', v.empresa_deletar, name='empresas_atualizar'),

    path('dashboard/grafico1/', v.JSON_qtd_por_sistema),
    path('dashboard/grafico2/', v.JSON_qtd_top_5),
    path('dashboard/grafico3/', v.JSON_por_dia_semana),

    # Raiz
    path('', v.home, name="home"),
]

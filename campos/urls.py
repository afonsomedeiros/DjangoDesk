from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.campos),

    path('categorias/', v.categorias, name="categorias"),
    path('categorias/cadastrar', v.cadastrar_categoria, name="cadastrar_categorias"),
    path('categorias/atualizar/<int:id>', v.atualizar_categoria, name="atualizar_categorias"),
    path('categorias/deletar/<int:id>', v.categoria_deletar, name="atualizar_categorias"),

    path('subcategorias/', v.subcategorias, name="subcategorias"),
    path('subcategorias/cadastrar', v.cadastrar_subcategoria, name="cadastrar_subcategoria"),
    path('subcategorias/atualizar/<int:id>', v.atualizar_subcategoria, name="atualizar_subcategoria"),
    path('subcategorias/deletar/<int:id>', v.subcategoria_deletar, name="atualizar_subcategoria"),

    path('classificacoes/', v.classificacoes, name="classificacao"),
    path('classificacoes/cadastrar', v.cadastrar_classificacao, name="cadastrar_classificacao"),
    path('classificacoes/atualizar/<int:id>', v.atualizar_classificacao, name="atualizar_classificacao"),
    path('classificacoes/deletar/<int:id>', v.classificacao_deletar, name="atualizar_classificacao"),

    path('operacoes/', v.operacoes, name="categorias"),
    path('operacoes/cadastrar', v.cadastrar_operacao, name="cadastrar_categorias"),
    path('operacoes/atualizar/<int:id>', v.atualizar_operacao, name="atualizar_categorias"),
    path('operacoes/deletar/<int:id>', v.operacao_deletar, name="atualizar_categorias"),

    path('estados/', v.estados, name="categorias"),
    path('estados/cadastrar', v.cadastrar_estado, name="cadastrar_categorias"),
    path('estados/atualizar/<int:id>', v.atualizar_estado, name="atualizar_categorias"),
    path('estados/deletar/<int:id>', v.estado_deletar, name="atualizar_categorias"),
]
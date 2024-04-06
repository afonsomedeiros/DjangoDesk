from django import forms

from .models import Categoria, Subcategoria, Classificacao, Operacao, Estado


class CategoriaForm(forms.ModelForm):

	class Meta:
		model = Categoria
		fields = ['nome', 'ativo', 'sistema']


class SubcategoriaForm(forms.ModelForm):

	class Meta:
		model = Subcategoria
		fields = ['nome', 'ativo', 'categoria']


class ClassificacaoForm(forms.ModelForm):

	class Meta:
		model = Classificacao
		fields = ['nome', 'ativo', 'subcategoria']


class OperacaoForm(forms.ModelForm):

	class Meta:
		model = Operacao
		fields = ['nome', 'ativo', 'classificacao']


class EstadoForm(forms.ModelForm):

	class Meta:
		model = Estado
		fields = ['nome', 'ativo', 'pendencia', 'encerrado', 'campo', 'unidade']
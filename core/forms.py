from django import forms

from .models import Unidade, Ramal, Sistema, Empresa


class UnidadeForm(forms.ModelForm):
	
	class Meta:
		model = Unidade
		fields = ['nome', 'endereco', 'telefone']


class RamalForm(forms.ModelForm):

	class Meta:
		model = Ramal
		fields = ['setor', 'contato', 'numero', 'unidade']

class SistemaForm(forms.ModelForm):

	class Meta:
		model = Sistema
		fields = ['nome', 'descricao', 'ativo']
		widgets = {
			'nome': forms.TextInput(attrs={'type':'text', 'class': 'col-12'}),
			'descricao': forms.Textarea(attrs={'type': 'text', 'class': 'col-12'}),
			'ativo': forms.CheckboxInput(attrs={'type':'checkbox'}),
		}

class EmpresaForm(forms.ModelForm):

	class Meta:
		model = Empresa
		fields = ['nome_fantasia', 'razao_social', 'CNPJ', 'email', 'telefone', 'situacao', 'unidade', 'sistema']
		widgets = {
			'nome_fantasia': forms.TextInput(attrs={'type':'text', 'class': 'col-12'}),
			'razao_social': forms.TextInput(attrs={'type':'text', 'class': 'col-12'}),
			'CNPJ': forms.TextInput(attrs={'type':'text', 'class': 'col-12'}),
			'email': forms.EmailInput(attrs={'type':'text', 'class': 'col-12'}),
			'telefone': forms.TextInput(attrs={'type':'text', 'class': 'col-12'}),
			'situacao': forms.Select(attrs={'class': 'col-12'}),
		}
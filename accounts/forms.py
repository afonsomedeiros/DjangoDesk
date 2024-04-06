from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from core.models import Unidade

User = get_user_model()


class SignupUserForm(UserCreationForm, forms.Form):
    unidade = forms.ModelMultipleChoiceField(Unidade.objects.all())

    class Meta:
        model = User
        fields = ('nome', 'sobrenome', 'email', 'nascimento', 'is_active', 'is_staff', 'is_admin',
                  'is_superuser' ,'password1', 'password2', 'unidade', 'user_permissions', 'groups')
        widgets = {
            'nome': forms.TextInput(attrs={'type': 'text'}),
            'sobrenome': forms.TextInput(attrs={'type': 'text'}),
            'email': forms.TextInput(attrs={'class': 'col-12', 'type': 'email', 'placeholder': 'Digite seu e-mail'}),
            'nascimento': forms.DateInput(attrs={'class': 'col-10'}, format='%d/%m/%Y'),
            'unidade': forms.CheckboxSelectMultiple(attrs={'class': 'col-12'})
        }


class UpdateUserForm(UserChangeForm, forms.Form):
    class Meta:
        model = User
        fields = ('nome', 'sobrenome', 'email', 'nascimento', 'is_active', 'is_staff', 'is_admin',
                  'unidade')
        widgets = {
            'nome': forms.TextInput(attrs={'type': 'text'}),
            'sobrenome': forms.TextInput(attrs={'type': 'text'}),
            'email': forms.TextInput(attrs={'class': 'col-12', 'type': 'email', 'placeholder': 'Digite seu e-mail'}),
            'nascimento': forms.DateInput(attrs={'class': 'col-10'}, format='%d/%m/%Y'),
            'unidade': forms.SelectMultiple(attrs={'class': 'col-12'})
        }

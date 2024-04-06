from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from accounts.forms import SignupUserForm, UpdateUserForm
from accounts.models import User
from accounts.VEIA import VEIAUsuario

@login_required
def signup(request):
    """

    Args:
        request (HttpRequest):
    """
    if request.method == 'POST':
        return VEIAUsuario.cadastrar(request, SignupUserForm)
    else:
        if not request.user.is_admin or request.user.is_superuser == False:
            return redirect('/')
        form = SignupUserForm()
        template_name = 'registration/register.html'
        return render(request, template_name, {'form': form})


@login_required
def updateuser(request, id):
    template_name = 'registration/atualizar.html'
    if request.method == 'POST':
        usuario = get_object_or_404(User, pk=id)
        return VEIAUsuario.atualizar(request, UpdateUserForm, usuario, template_name)
    else:
        usuario = get_object_or_404(User, pk=id)
        form = UpdateUserForm(instance=usuario)
        return render(request, template_name, {'form': form})


@login_required
def deleteuser(request, id):
    user = get_object_or_404(User, pk=id)
    if request.user.is_admin or request.user.is_superuser:
        user.delete()
        return redirect('/usuarios')
    else:
        return redirect('/')

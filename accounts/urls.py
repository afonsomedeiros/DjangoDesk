from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.signup, name='Signup'),
    path('atualizar/<int:id>', views.updateuser, name='atualizar'),
    path('deletar/<int:id>', views.deleteuser, name='atualizar'),
]
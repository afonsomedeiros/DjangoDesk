from django.contrib import admin
from django.contrib.auth.models import Group

from .models import User
from .forms import SignupUserForm, UpdateUserForm

class UserAdmin(admin.ModelAdmin):
    form = SignupUserForm
    add_form = UpdateUserForm
    search_fields = ['email']
    list_filter = ['is_admin', 'is_staff', 'is_active', 'unidade']
    list_display = ['nome', 'email', 'is_admin', 'is_superuser']
    class Meta:
        model = User

admin.site.register(User, UserAdmin)
#admin.site.register(Group)
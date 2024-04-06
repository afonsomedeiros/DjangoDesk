from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin, _user_has_perm)
from django.utils import timezone
from core.models import Unidade

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_staff=False, is_admin=False, is_active=True, is_superuser=False, nome='', sobrenome=''):
        if not email:
            raise ValueError("E-mail é obrigatório.")
        if not password:
            raise ValueError("Senha é obrigatória.")
        user_obj = self.model(
            email=self.normalize_email(email)
        )
        user_obj.set_password(password)
        user_obj.nome = nome
        user_obj.sobrenome = sobrenome
        user_obj.is_staff = is_staff
        user_obj.is_admin = is_admin
        user_obj.is_active = is_active
        user_obj.is_superuser = is_superuser
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, password=None):
        user = self.create_user(email, password, is_staff=True)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email, password, is_staff=True, is_admin=True, is_superuser=True)
        return user

class User(AbstractBaseUser, PermissionsMixin, models.Model):

    email = models.EmailField(max_length=255, unique=True)
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=100)
    nascimento = models.DateField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    unidade = models.ManyToManyField(Unidade)
    timestamp = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return f"{self.nome} {self.sobrenome}"

    def get_short_name(self):
        return self.nome

    def has_perm(self, perm, obj=None):
        if self.is_active and self.is_superuser:
            return True
        # Otherwise we need to check the backends.
        return _user_has_perm(self, perm, obj)

    def has_module_perms(self, app_label):
        return True

    class Meta:
        verbose_name_plural = "Usuários"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('nombre_usuario',)


class CustomUserChangeForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('nombre_usuario',)

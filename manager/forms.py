from django import forms
from django.contrib.auth.forms import UserCreationForm


# class registro_usuario(forms.ModelForm):

# class Meta:
# model = Usuario
# fields = ["nombre_usuario", "contraseña_usuario"]

class CustomUserCreationForm(UserCreationForm):
    pass

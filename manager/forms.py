from django import forms
from .models import Usuario
class registro_usuario(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ["nombre_usuario","contraseña_usuario","rol"]
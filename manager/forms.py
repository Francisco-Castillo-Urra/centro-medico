from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Paciente,Profesional,Agenda
from django.utils import timezone


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('email',)


class CustomUserChangeForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('email',)


class PacienteForm(forms.ModelForm):

    class Meta:
        model = Paciente
        fields = '__all__'
        exclude = ('usuario', 'fecha_registro_pac')
        widgets = {
            "fecha_nac": forms.SelectDateWidget(years=range(1920, timezone.now().year+1))
        }

class MedicoForm(forms.ModelForm):
    class Meta:
        model = Profesional
        fields = '__all__'
        exclude = ('usuario','fecha_registro_pro')

class AgendaForm(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = ('__all__')
        exclude = ('fecha_hora','tarifa')
        widgets = {
            "fecha_atencion": forms.SelectDateWidget()
        }

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Paciente, Profesional, Ciudad, Usuario, Prevision, Agenda, Bloque, Box, Contrato
from .forms import CustomUserCreationForm, CustomUserChangeForm
# Register your models here.
admin.site.register(Paciente)
admin.site.register(Profesional)
admin.site.register(Ciudad)
admin.site.register(Prevision)
admin.site.register(Agenda)
admin.site.register(Bloque)
admin.site.register(Box)
admin.site.register(Contrato)
admin.site.register(Usuario)

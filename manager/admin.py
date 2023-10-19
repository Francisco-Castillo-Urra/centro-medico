from django.contrib import admin
from .models import Paciente, Profesional, Ciudad, Rol, Usuario, Prevision
# Register your models here.
admin.site.register(Paciente)
admin.site.register(Profesional)
admin.site.register(Ciudad)
admin.site.register(Rol)
admin.site.register(Usuario)
admin.site.register(Prevision)

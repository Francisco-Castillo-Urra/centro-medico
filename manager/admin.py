from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Paciente, Profesional, Ciudad, Rol, Usuario, Prevision
from .forms import CustomUserCreationForm, CustomUserChangeForm
# Register your models here.
admin.site.register(Paciente)
admin.site.register(Profesional)
admin.site.register(Ciudad)
admin.site.register(Rol)
admin.site.register(Prevision)


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Usuario
    list_display = ('nombre_usuario', "is_staff", "is_active",)
    list_filter = ('nombre_usuario', "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("nombre_usuario", "password")}),
        ("Permissions", {"fields": ("is_staff",
         "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "nombre_usuario", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
         ),
    )
    search_fields = ("nombre_usuario",)
    ordering = ("nombre_usuario",)


admin.site.register(Usuario, CustomUserAdmin)

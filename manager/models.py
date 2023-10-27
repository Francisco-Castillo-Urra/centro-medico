from typing import Any
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
# Create your models here.


class Ciudad(models.Model):
    nombre_ciudad = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_ciudad


class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("No ha proporcionado un email valido")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)


class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(blank=True, default='', unique=True)
    is_active = models.BooleanField('Esta activo', default=True)
    is_superuser = models.BooleanField('Es super usuario', default=False)
    is_staff = models.BooleanField('Es staff', default=False)
    last_login = models.DateTimeField(
        'Ultimo inicio de sesion', blank=True, null=True)
    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    EMAIL_FIEL = "email"
    REQUIRED_FIELDS = []


class Profesional(models.Model):
    rut_pro = models.IntegerField('RUT', primary_key=True)
    primer_nombre_pro = models.CharField('Primer nombre', max_length=50)
    segundo_nombre_pro = models.CharField('Segundo nombre', max_length=50)
    apellido_paterno_pro = models.CharField('Apellido paterno', max_length=50)
    apellido_materno_pro = models.CharField('Apellido materno', max_length=50)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.PROTECT)
    direccion_pro = models.CharField('Direccion', max_length=50)
    celular_pro = models.IntegerField('Celular')
    tarifa = models.IntegerField('Tarifa')
    fecha_registro_pro = models.DateField(
        'Fecha de registro', default=timezone.now)

    usuario = models.OneToOneField(Usuario, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Profesional'
        verbose_name_plural = 'Profesionales'


class Prevision(models.Model):
    nombre_prevision = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_prevision


class Paciente(models.Model):
    rut_paciente = models.IntegerField('RUT', primary_key=True)
    primer_nombre_pac = models.CharField('Primer nombre', max_length=50)
    segundo_nombre_pac = models.CharField('Segundo nombre', max_length=50)
    apellido_paterno_pac = models.CharField('Apellido paterno', max_length=50)
    apellido_materno_pac = models.CharField('Apellido materno', max_length=50)
    orden_apellido = models.BooleanField(
        'Invertir el orden de los apellidos', default=False)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.PROTECT,null=True,blank=True)
    fecha_nac = models.DateField('Fecha de nacimiento')
    direccion_pac = models.CharField('Direccion', max_length=50)
    celular_pac = models.IntegerField('Celular')
    prevision = models.ForeignKey(Prevision, on_delete=models.PROTECT)
    fecha_registro_pac = models.DateField(
        'Fecha de registro', default=timezone.now)
    nombre_social = models.CharField(
        'Nombre social', max_length=50, blank=True, null=True)
    usuario = models.OneToOneField(
        Usuario, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.rut_paciente + ' ' + self.primer_nombre_pac + ' ' + self.apellido_paterno_pac


class Bloque(models.Model):
    descripcion = models.TextField()
    hora_ini = models.TimeField()
    hora_fin = models.TimeField()


class Agenda(models.Model):
    rut_pro = models.ForeignKey(Profesional, on_delete=models.PROTECT)
    rut_pa = models.ForeignKey(Paciente, on_delete=models.PROTECT)
    fecha_hora = models.DateField(default=timezone.now)
    fecha_atencion = models.DateField()
    bloque = models.ForeignKey(Bloque, on_delete=models.PROTECT)
    tarifa = models.IntegerField()


class Box(models.Model):
    descripcion = models.TextField()
    valor_mensual = models.IntegerField()


class Contrato(models.Model):
    fecha_contrato = models.DateField(default=timezone.now)
    rut_pro = models.ForeignKey(Profesional, on_delete=models.PROTECT)
    valor_mensual = models.IntegerField()
    fecha_ini = models.DateField()
    fecha_fin = models.DateField()

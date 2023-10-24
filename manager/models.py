from typing import Any
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager

# Create your models here.


class Ciudad(models.Model):
    nombre_ciudad = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class CustomUserManager(UserManager):
    def _create_user(self, password, **extra_fields):
        user = self.model(**extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(password, **extra_fields)

    def create_superuser(self, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(password, **extra_fields)


class Usuario(AbstractBaseUser, PermissionsMixin):
    
    nombre_usuario = models.CharField('Nombre de usuario', max_length=50, unique=True, blank=True, null=False)
    estado_usuario = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()
    USERNAME_FIELD = "nombre_usuario"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.nombre_usuario


class Profesional(models.Model):
    rut_pro = models.IntegerField('RUT', primary_key=True)
    primer_nombre_pro = models.CharField('Primer nombre', max_length=50)
    segundo_nombre_pro = models.CharField('Segundo nombre', max_length=50)
    apellido_paterno_pro = models.CharField('Apellido paterno', max_length=50)
    apellido_materno_pro = models.CharField('Apellido materno', max_length=50)
    direccion_pro = models.CharField('Direccion', max_length=50)
    celular_pro = models.IntegerField('Celular')
    email_pro = models.EmailField('Email', max_length=50)
    tarifa = models.IntegerField('Tarifa')
    estado_pro = models.BooleanField('Estado')
    fecha_registro_pro = models.DateField(
        'Fecha de registro', default=timezone.now)
    id_ciudad = models.ForeignKey(Ciudad, on_delete=models.PROTECT)
    id_usuario = models.ForeignKey(
        Usuario, null=True, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Profesional'
        verbose_name_plural = 'Profesionales'

    def __str__(self):
        return self.primer_nombre + self.segundo_nombre + self.apellido_paterno + self.apellido_paterno


class Prevision(models.Model):
    nombre_prevision = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_prevision


class Paciente(models.Model):
    rut_paciente = models.CharField('RUT', max_length=50, primary_key=True)
    primer_nombre_pac = models.CharField('Primer nombre', max_length=50)
    segundo_nombre_pac = models.CharField('Segundo nombre', max_length=50)
    apellido_paterno_pac = models.CharField('Apellido paterno', max_length=50)
    apellido_materno_pac = models.CharField('Apellido materno', max_length=50)
    orden_apellido = models.BooleanField(
        'Invertir el orden de los apellidos', default=False)
    fecha_nac = models.DateField('Fecha de nacimiento')
    direccion_pac = models.CharField('Direccion', max_length=50)
    celular_pac = models.IntegerField('Celular')
    email_pac = models.EmailField('Email', max_length=50)
    prevision = models.ForeignKey(Prevision, on_delete=models.PROTECT)
    estado_pac = models.BooleanField('Estado')
    fecha_registro_pac = models.DateField(
        'Fecha de registro', default=timezone.now)
    nombre_social = models.CharField(
        'Nombre social', max_length=50, blank=True, null=True)
    id_usuario = models.ForeignKey(
        Usuario, blank=True, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.primer_nombre_pac + ' ' + self.segundo_nombre_pac+' ' + self.apellido_paterno_pac + ' '+self.apellido_materno_pac


class Bloque(models.Model):
    descripcion = models.TextField()
    estado = models.BooleanField()
    hora_ini = models.TimeField()
    hora_fin = models.TimeField()

    def __str__(self):
        return self.descripcion


class Agenda(models.Model):
    rut_pro = models.ForeignKey(Profesional, on_delete=models.PROTECT)
    rut_pa = models.ForeignKey(Paciente, on_delete=models.PROTECT)
    fecha_hora = models.DateField(default=timezone.now)
    fecha_atencion = models.DateField()
    estado = models.BooleanField()
    bloque = models.ForeignKey(Bloque, on_delete=models.PROTECT)
    tarifa = models.IntegerField()


class Box(models.Model):
    descripcion = models.TextField()
    valor_mensual = models.IntegerField()

    def __str__(self):
        return self.descripcion


class Contrato(models.Model):
    fecha_contrato = models.DateField(default=timezone.now)
    rut_pro = models.ForeignKey(Profesional, on_delete=models.PROTECT)
    valor_mensual = models.IntegerField()
    estado = models.BooleanField()
    fecha_ini = models.DateField()
    fecha_fin = models.DateField()

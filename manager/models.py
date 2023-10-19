from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# Create your models here.


class Ciudad(models.Model):
    nombre_ciudad = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Rol(models.Model):
    nombre_rol = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_rol


class Usuario(models.Model):
    nombre_usuario = models.CharField('Nombre de usuario', max_length=50,unique=True,blank=False,null=False)
    contraseña_usuario = models.CharField('Contraseña', max_length=30, blank=False,null=False)
    estado_usuario = models.BooleanField(default=False)
    rol = models.ForeignKey(Rol, on_delete=models.PROTECT, default=1)
    fecha_ultimo_ingreso = models.DateField(blank=True, null=True)
    #USERNAME_FIELD = "nombre_usuario"
    #PASSWORD_FIELD = "contraseña_usuario"

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
    fecha_registro_pro = models.DateField('Fecha de registro', default=timezone.now())
    id_ciudad = models.ForeignKey(Ciudad, on_delete=models.PROTECT)
    id_usuario = models.ForeignKey(
        Usuario, null=True, on_delete=models.PROTECT)

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
    orden_apellido = models.BooleanField('Invertir el orden de los apellidos', default=False)
    fecha_nac = models.DateField('Fecha de nacimiento')
    direccion_pac = models.CharField('Direccion', max_length=50)
    celular_pac = models.IntegerField('Celular')
    email_pac = models.EmailField('Email', max_length=50)
    prevision = models.ForeignKey(Prevision, on_delete=models.PROTECT)
    estado_pac = models.BooleanField('Estado')
    fecha_registro_pac = models.DateField('Fecha de registro', default=timezone.now())
    nombre_social = models.CharField('Nombre social', max_length=50, blank=True, null=True)
    id_usuario = models.ForeignKey(Usuario, blank=True, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.primer_nombre_pac + ' ' + self.segundo_nombre_pac+' ' + self.apellido_paterno_pac + ' '+self.apellido_materno_pac

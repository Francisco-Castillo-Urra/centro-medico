from django.shortcuts import redirect, render
from .models import Ciudad
from .forms import CustomUserCreationForm, PacienteForm, MedicoForm, AgendaForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Agenda
from django.utils import timezone
from django.urls import reverse
from django.shortcuts import get_object_or_404
import requests
# Mostrar el home


def home(request):
    return render(request, 'manager/home.html')


### Datos pacientes###

# Registrar el usuario de un paciente
def registrousuariopaciente(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(
                username=formulario.cleaned_data["email"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to='datospaciente')
        else:
            data['form'] = formulario
    return render(request, 'registration/registrousuario.html', data)


# Registrar los datos del paciente
@login_required
def datos_paciente(request):
        usuario = request.user
        data = {
            'form': PacienteForm(),
        }
        formulario = PacienteForm(data=request.POST)
        if formulario.is_valid():
            formulario.instance.usuario = usuario
            formulario.save()
            messages.success(
                request, "Sus datos se han guardado correctamente")
            return redirect(to='home')

        else:
            data['form'] = formulario

        return render(request, 'manager/paciente.html', data)


### Datos medicos###

# Registrar el usuario de un medico
def registrousuariomedico(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.instance.is_staff = True
            formulario.save()
            user = authenticate(
                username=formulario.cleaned_data["email"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Medico registrado correctamente")
            return redirect(to='datosmedico')
        else:
            data['form'] = formulario
    return render(request, 'registration/registrousuario.html', data)


# Registrar los datos del medico
@login_required
def datos_medico(request):
    usuario = request.user
    data = {
        'form': MedicoForm(),
    }
    formulario = MedicoForm(data=request.POST)
    if formulario.is_valid():
        formulario.instance.usuario = usuario
        formulario.save()
        messages.success(
            request, "Los datos del medico han guardado correctamente")
        return redirect(to='home')

    else:
        data['form'] = formulario

    return render(request, 'manager/medico.html', data)


## Agenda de horas###

# Agendar hora
@login_required
def agendar_hora(request):
    usuario = request.user
    data = {
        'form': AgendaForm()
    }
    if request.method == 'POST':
        formulario = AgendaForm(data=request.POST)
        if formulario.is_valid():
            formulario.instance.paciente = usuario.paciente
            medico = formulario.cleaned_data['medico']
            formulario.instance.tarifa = medico.tarifa
            formulario.save()
            messages.success(request, "Hora registrada")
            return redirect(to='home')
        else:
            data['form'] = formulario
    return render(request, 'manager/agendar-hora.html', data)


# Listado de todas las atenciones
@login_required
def listar_por_atender(request):
    agenda = Agenda.objects.all()
    data = {
        'pacientes': agenda
    }
    return render(request, 'manager/lista-atencion-completa-medico.html', data)


@login_required
def listar_por_atender_secretaria(request):
    agenda = Agenda.objects.all()
    data = {
        'pacientes': agenda
    }
    return render(request, 'manager/lista-atencion-completa-secretaria.html', data)


# Listado de las atenciones pendientes del dia
@login_required
def listar_por_atender_hoy(request):
    fecha_actual = timezone.now().date()
    agenda = Agenda.objects.all()
    agenda_hoy = [a for a in agenda if a.fecha_atencion == fecha_actual]
    data = {
        'pacientes': agenda_hoy
    }
    return render(request, 'manager/lista-atencion.html', data)


# Marcar horas como atendidas
@login_required
def marcar_atendido(request, agenda_id):
    agenda = get_object_or_404(Agenda, id=agenda_id)
    agenda.atendido = True
    agenda.save()
    return redirect(reverse('poratender'))


# Marcar horas como pagadas
@login_required
def marcar_pagado(request, agenda_id):
    agenda = get_object_or_404(Agenda, id=agenda_id)
    agenda.pagado = True
    agenda.save()
    return redirect(reverse('listaagenda'))


### Secretaria###

# Registro de secretaria
@login_required
def registrousariosecretaria(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.instance.is_staff = True
            formulario.instance.is_superuser = True
            formulario.save()
            user = authenticate(
                username=formulario.cleaned_data["email"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Secretaria registrado correctamente")
            return redirect(to='home')
        else:
            data['form'] = formulario
    return render(request, 'registration/registrousuario.html', data)

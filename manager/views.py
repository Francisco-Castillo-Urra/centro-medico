from django.shortcuts import redirect, render
from .models import Paciente
from .forms import CustomUserCreationForm, PacienteForm, MedicoForm,AgendaForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Agenda
from django.utils import timezone
from datetime import datetime
# Create your views here.


def home(request):
    pacientes = Paciente.objects.all
    data = {
        'pacientes': pacientes
    }
    return render(request, 'manager/home.html', data)


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
        messages.success(request, "Sus datos se han guardado correctamente")
        return redirect(to='home')

    else:
        data['form'] = formulario

    return render(request, 'manager/paciente.html', data)


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
        messages.success(request, "Los datos del medico han guardado correctamente")
        return redirect(to='home')

    else:
        data['form'] = formulario

    return render(request, 'manager/medico.html', data)


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

@login_required
def listar_por_atender(request):
    fecha_actual = timezone.now().date()
    agenda = Agenda.objects.all()
    agenda_hoy = [a for a in agenda if a.fecha_atencion == fecha_actual]
    data = {
        'pacientes': agenda
    }
    return render(request, 'manager/lista-atencion.html',data)
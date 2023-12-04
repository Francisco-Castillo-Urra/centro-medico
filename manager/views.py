from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm, PacienteForm, MedicoForm, AgendaForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Agenda, Profesional
from django.utils import timezone
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from decouple import config
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
            subject = 'Hora registrada'
            message = f'Su hora fue registrada correctamente con los siguentes datos: Nombre del paciente {
                formulario.instance.paciente.primer_nombre_pac} Medico {
                formulario.instance.medico.primer_nombre_pro} Fecha {
                formulario.instance.fecha_atencion} Tarifa {
                formulario.instance.tarifa} '
            from_email = config('EMAIL_HOST_USER')
            recipient_list = [usuario.email]
            send_mail(subject, message, from_email, recipient_list)
            return redirect(to='home')
        else:
            data['form'] = formulario
    return render(request, 'manager/agendar-hora.html', data)


# Listado de todas las atenciones
@login_required
def listar_por_atender(request):
    usuario = request.user
    if usuario.is_staff == False or usuario.is_superuser == False:
        return redirect(reverse('home'))
    agenda = Agenda.objects.all()
    data = {
        'pacientes': agenda
    }
    return render(request, 'manager/lista-atencion-completa-medico.html', data)


@login_required
def listar_por_atender_secretaria(request):
    usuario = request.user
    if usuario.is_staff == False or usuario.is_superuser == False:
        return redirect(reverse('home'))
    agenda = Agenda.objects.all()
    data = {
        'pacientes': agenda
    }
    return render(request, 'manager/lista-atencion-completa-secretaria.html', data)


# Listado de las atenciones pendientes del dia
@login_required
def listar_por_atender_hoy(request):
    usuario = request.user
    if usuario.is_staff == False or usuario.is_superuser == False:
        return redirect(reverse('home'))
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
    usuario = request.user
    if usuario.is_staff == False:
        return redirect(reverse('home'))
    agenda = get_object_or_404(Agenda, id=agenda_id)
    agenda.atendido = True
    agenda.save()
    return redirect(reverse('poratender'))


# Marcar horas como pagadas
@login_required
def marcar_pagado(request, agenda_id):
    usuario = request.user
    if usuario.is_staff == False or usuario.is_superuser == False:
        return redirect(reverse('home'))
    agenda = get_object_or_404(Agenda, id=agenda_id)
    agenda.pagado = True
    agenda.save()
    return redirect(reverse('listasecretaria'))


### Secretaria###

# Registro de secretaria
@login_required
def registrousariosecretaria(request):
    usuario = request.user
    if usuario.is_staff == False or usuario.is_superuser == False:
        return redirect(reverse('home'))
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


@login_required
def informacion_medicos(request):
    usuario = request.user
    if usuario.is_staff == False or usuario.is_superuser == False:
        return redirect(reverse('home'))
    medicos = Profesional.objects.all()
    data = {
        'medicos': medicos
    }
    return render(request, 'manager/informacion-medicos.html', data)


@login_required
def generar_informe(request, medico_id):
    usuario = request.user
    if usuario.is_staff == False or usuario.is_superuser == False:
        return redirect(reverse('home'))
    medico = get_object_or_404(Profesional, rut_pro=medico_id)
    agendas = Agenda.objects.all()
    atenciones = [i for i in agendas if i.medico.rut_pro == medico.rut_pro]
    atenciones_del_mes = [i for i in atenciones if i.pagado == True and i.fecha_atencion.month == timezone.now(
    ).month and i.fecha_atencion.year == timezone.now().year]
    valores_atencion = []
    for i in atenciones_del_mes:
        valores_atencion.append(i.tarifa)
    total = sum(valores_atencion)
    data = {
        'atenciones': atenciones_del_mes,
        'total': total
    }
    return render(request, 'manager/informe.html', data)

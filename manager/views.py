from django.shortcuts import redirect, render
from .models import Paciente
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, get_user_model
# Create your views here.
User = get_user_model()


def home(request):
    pacientes = Paciente.objects.all
    data = {
        'pacientes': pacientes
    }
    return render(request, 'manager/home.html', data)


def registrousuario(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(
                username=formulario.cleaned_data["nombre_usuario"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to='home')
        else:
            data['form'] = formulario
    return render(request, 'registration/registrousuario.html', data)

def agendar_hora(request):
    return render(request,'manager/agendar-hora.html')
from django.shortcuts import redirect, render
from .models import Paciente
from .forms import registro_usuario, CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login
# Create your views here.


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
            user = authenticate(username=formulario.cleaned_data["username"],password= formulario.cleaned_data["password1"])
            login(request,user)
            messages.success(request,"Te has registrado correctamente")
            return redirect(to='home')
        else:
            data['form'] = formulario
    return render(request, 'registration/registrousuario.html',data)

from django.shortcuts import render
from .models import Paciente
from .forms import registro_usuario
# Create your views here.


def home(request):
    pacientes = Paciente.objects.all
    data = {
        'pacientes': pacientes
    }
    return render(request, 'manager/home.html', data)

def registro(request):
    data = {
        'form': registro_usuario()
    }
    if request.method == 'POST':
        formulario =  registro_usuario(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "usuario registrado correctamente"
        else:
            data["form"] = formulario
    return render(request,'manager/registro.html',data)
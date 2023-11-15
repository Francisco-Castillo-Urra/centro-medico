from django.urls import path
from .views import home, registrousuariopaciente, agendar_hora, datos_paciente, registrousuariomedico, datos_medico,listar_por_atender

urlpatterns = [
    path('', home, name='home'),
    path('registro-usuario/', registrousuariopaciente, name='registrousuario'),
    path('agendar-hora/', agendar_hora,name='agendarhora'),
    path('datos-paciente/', datos_paciente, name='datospaciente'),
    path('registro-medico', registrousuariomedico, name='registromedico'),
    path('datos-medico', datos_medico, name='datosmedico'),
    path('lista-atencion',listar_por_atender,name='poratender')
]

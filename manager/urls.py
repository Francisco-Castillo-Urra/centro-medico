from django.urls import path
from .views import home, registrousuario,agendar_hora

urlpatterns = [
    path('', home, name='home'),
    path('registro-usuario/',registrousuario, name='registrousuario'),
    path('agendar-hora/',agendar_hora, name='agendarhora'),
]
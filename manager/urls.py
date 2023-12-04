from django.urls import path
from .views import home, registrousuariopaciente, agendar_hora, datos_paciente, registrousuariomedico, datos_medico,listar_por_atender,marcar_atendido,listar_por_atender_hoy,registrousariosecretaria
from .views import marcar_pagado, listar_por_atender_secretaria,informacion_medicos,generar_informe

urlpatterns = [
    path('', home, name='home'),
    path('registro-usuario/', registrousuariopaciente, name='registrousuario'),
    path('agendar-hora/', agendar_hora,name='agendarhora'),
    path('datos-paciente/', datos_paciente, name='datospaciente'),
    path('registro-medico', registrousuariomedico, name='registromedico'),
    path('datos-medico', datos_medico, name='datosmedico'),
    path('lista-atencion',listar_por_atender_hoy,name='poratender'),
    path('marcar-atendido/<int:agenda_id>/', marcar_atendido, name='marcar_atendido'),
    path('lista-completa-atencion',listar_por_atender,name='listaatencion'),
    path('lista-secretaria',listar_por_atender_secretaria,name='listasecretaria'),
    path('registro-secretaria',registrousariosecretaria,name='registrosecretaria'),
    path('marcar-pagado/<int:agenda_id>/', marcar_pagado, name='marcar_pagado'),
    path('informacion-medicos',informacion_medicos,name='informacion_medicos'),
    path('informe/<int:medico_id>',generar_informe,name='informe')
]

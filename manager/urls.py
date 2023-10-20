from django.urls import path
from .views import home, registro, registrousuario

urlpatterns = [
    path('', home, name='home'),
    path('registro/', registro, name='registro'),
    path('registro-usuario/',registrousuario, name='registrousuario')
]
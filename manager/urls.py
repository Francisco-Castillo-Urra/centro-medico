from django.urls import path
from .views import home, registrousuario

urlpatterns = [
    path('', home, name='home'),
    path('registro-usuario/',registrousuario, name='registrousuario')
]
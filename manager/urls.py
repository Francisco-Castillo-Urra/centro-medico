from django.urls import path
from .views import home, registro

urlpatterns = [
    path('', home),
    path('registro/', registro)
]

from django.urls import path
from . import views
from .views import *

app_name="sorteo"

urlpatterns = [
    path('asignar/', asignar_docente, name='asignar_docente'),
    path('asignaciones/', lista_asignaciones, name='lista_asignaciones'),
]
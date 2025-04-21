from django.urls import path 
from centro.views import origen, facultad, listado_alumnos

urlpatterns = [
    path('', origen, name = 'origen'),
    path('facu/', listado_alumnos, name = 'listado_alumnos'),
    path('facultad/', facultad, name = 'facultad')
]

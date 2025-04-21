from django.urls import path 
from centro.views import origen, facultad, listado_alumnos, detalle_facultad, DetalleFacultad, ModificarFacultad, EliminarFacultad

urlpatterns = [
    path('', origen, name = 'origen'),
    path('facu/', listado_alumnos, name = 'listado_alumnos'),
    path('facultad/', facultad, name = 'facultad'),
    path('facultad/<int:pk>/eliminar/', EliminarFacultad.as_view(), name = 'eliminar_facultad'),
    path('facultad/<int:pk>/modificar/', ModificarFacultad.as_view(), name = 'modificar_facultad'),
    #path('facultad/<int:alumno_especifico>', detalle_facultad, name = 'detalle_facultad')
    path('facultad/<int:pk>', DetalleFacultad.as_view(), name = 'detalle_facultad')
]

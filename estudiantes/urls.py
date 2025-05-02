from django.urls import path
from estudiantes.views import login, registro, editar_perfil, PerfilEstudiante, listado_alumnos
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', LogoutView.as_view(template_name='estudiantes/logout.html'), name='logout'),
    path('registro/', registro, name='registro'),
    path('perfil/editar/', editar_perfil, name='editar_perfil'),
    path('perfil/estudiante/', PerfilEstudiante, name='PerfilEstudiante'),
    path('listado/alumnos/', listado_alumnos, name='listado_alumnnos'),
    ]

from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import login as django_login
from estudiantes.forms import formularioregistro, Formularioeditar, FormularioEst
from django.contrib.auth.decorators import login_required
from estudiantes.models import InfoExtra
from estudiantes.models import Estudiante
from django.contrib import messages

def login(request):
    
    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            
            estudiantes = formulario.get_user()
            
            django_login(request, estudiantes)
            
            InfoExtra.objects.get_or_create(user=estudiantes)
            
            return redirect("origen")
    else:
        formulario = AuthenticationForm
        
    return render(request, 'estudiantes/login.html',{'formulario': formulario})

def registro(request):
    if request.method == "POST":
        formulario = formularioregistro(request.POST)
        if formulario.is_valid():
            
            user = formulario.save()
            Estudiante.objects.create(user=user)
            return redirect("login")
    else:
        formulario = formularioregistro()
        
    return render(request, 'estudiantes/registro.html', {'formulario': formulario})

@login_required
def editar_perfil(request):
    InfoExtra = request.user.infoextra
    try:
        estudiante = Estudiante.objects.get(user=request.user)
    except Estudiante.DoesNotExist:
        estudiante = None  

    if request.method == "POST":
        formulario = Formularioeditar(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            if formulario.cleaned_data.get('imagen'):
                estudiante.imagen = formulario.cleaned_data.get('imagen')


            if formulario.cleaned_data.get('avatar'):
                InfoExtra.avatar = formulario.cleaned_data.get('avatar')

            InfoExtra.save()

            if estudiante:
                estudiante.biografia = formulario.cleaned_data.get('biografia')
                estudiante.save()
            else:
                Estudiante.objects.create(user=request.user, biografia=formulario.cleaned_data.get('biografia'))


            return redirect('listado_alumnos')

    else:
        formulario = Formularioeditar(instance=request.user, initial={
            'imagen': InfoExtra.imagen,
            'avatar': InfoExtra.avatar,
            'biografia': estudiante.biografia if estudiante else ''
        })

    return render(request, 'estudiantes/editar_perfil.html', {'formulario': formulario})


@login_required
def PerfilEstudiante(request):
    estudiante = request.user.estudiante
    form = Formularioeditar(instance=estudiante)

    if request.method == 'POST':
        form = Formularioeditar(request.POST, request.FILES, instance=estudiante)
        if form.is_valid():
            old_biografia = estudiante.biografia
            old_avatar = estudiante.avatar

            form.save()

            if old_biografia == estudiante.biografia and old_avatar == estudiante.avatar:
                messages.info(request, "No se realizaron cambios.")
                return redirect('perfil_guardado')

            messages.success(request, "Perfil actualizado correctamente.")
            return redirect('listado_alumnos') 

    return render(request, 'estudiantes/PerfilEstudiante.html', {'estudiante':estudiante})

def listado_alumnos(request):
    return render(request, 'centro/listado_alumnos.html')
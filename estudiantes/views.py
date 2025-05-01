from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as django_login
from estudiantes.forms import formularioregistro

def login(request):
    
    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            
            estudiantes = formulario.get_user()
            
            django_login(request, estudiantes)
            
            
            return redirect("origen")
    else:
        formulario = AuthenticationForm
        
    return render(request, 'estudiantes/login.html',{'formulario': formulario})

def registro(request):
    if request.method == "POST":
        formulario = formularioregistro(request.POST)
        if formulario.is_valid():
            
            formulario.save()
            
            return redirect("login")
    else:
        formulario = formularioregistro()
        
    return render(request, 'estudiantes/registro.html', {'formulario': formulario})


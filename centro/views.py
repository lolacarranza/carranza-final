from django.shortcuts import render, redirect
from django.http import HttpResponse
from centro.forms import crearFacu
from centro.models import Facu

def origen (request):
    return render (request, 'centro/origen.html')

def facultad (request):
    print('datos del GET', request.GET)
    print('datos del POST', request.POST)
    
    if request.method == "POST":
        formulario = crearFacu(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            facu = Facu(nombre=info.get('nombre'), legajo=info.get('legajo'))
            facu.save()
            return redirect ('listado_alumnos')
    else:
        formulario = crearFacu()    
    
    
    return render (request, 'centro/facultad.html', {'formulario':formulario})

def listado_alumnos(request):
    facul = Facu.objects.all()
    return render (request, 'centro/listado_alumnos.html', {'facul':facul})
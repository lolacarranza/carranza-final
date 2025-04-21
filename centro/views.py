from django.shortcuts import render, redirect
from django.http import HttpResponse
from centro.forms import crearFacu
from centro.models import Facu
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy

def origen (request):
    return render (request, 'centro/origen.html')

def facultad (request):
    print('datos del GET', request.GET)
    print('datos del POST', request.POST)
    
    if request.method == "POST":
        formulario = crearFacu(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            facu = Facu(nombre=info.get('nombre'), legajo=info.get('legajo'), fecha=info.get('fecha'))
            facu.save()
            return redirect ('listado_alumnos')
    else:
        formulario = crearFacu()    
    
    
    return render (request, 'centro/facultad.html', {'formulario':formulario})

def listado_alumnos(request):
    facul = Facu.objects.all()
    return render (request, 'centro/listado_alumnos.html', {'facul':facul})

def detalle_facultad(request, alumno_especifico):
    facu = Facu.objects.get(id=alumno_especifico)
    return render (request, 'centro/detalle_facultad.html', {'facu': facu })

class DetalleFacultad(DetailView):
    model = Facu
    template_name = "centro/detalle_facultad.html"

class ModificarFacultad(UpdateView):
    model = Facu
    template_name = "centro/modificar_facultad.html"
    fields = ["nombre", "legajo", "fecha"]
    success_url = reverse_lazy(listado_alumnos)
    
class EliminarFacultad(DeleteView):
    model = Facu
    template_name = "centro/eliminar_facultad.html"
    success_url = reverse_lazy(listado_alumnos)


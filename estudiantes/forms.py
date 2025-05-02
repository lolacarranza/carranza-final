from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView
from .models import Estudiante
        

class formularioregistro(UserCreationForm):
    username = forms.CharField(label="Usuario del estudiante")
    email = forms.EmailField()
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]
        help_texts = {field: "" for field in fields}


class Formularioeditar(forms.ModelForm):
    password = None 
    email = forms.EmailField(required=False)
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    imagen = forms.ImageField(required=False)
    biografia = forms.CharField(required=False, widget=forms.Textarea)
    avatar = forms.ImageField(required=False)

    class Meta:
        model = Estudiante 
        fields = ['biografia', 'avatar'] 

    def save(self, commit=True):
        estudiante = super().save(commit=False)
        if commit:
            estudiante.save() 
        return estudiante


class FormularioEst(DetailView):
    password = None
    email = 'Email'
    first_name ='Nombre'
    last_name = 'Apellido'
    imagen = 'Imagen'
    biografia = 'Biografia'
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "imagen", "biografia"]
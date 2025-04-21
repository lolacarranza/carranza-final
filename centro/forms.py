from django import forms

class crearFacu(forms.Form):
    nombre= forms.CharField(max_length=50)
    legajo= forms.CharField(max_length=6)
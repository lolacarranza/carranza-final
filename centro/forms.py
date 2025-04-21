from django import forms

class crearFacu(forms.Form):
    nombre= forms.CharField(max_length=50)
    legajo= forms.CharField(max_length=6)
    fecha = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
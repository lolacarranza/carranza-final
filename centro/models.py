from django.db import models

class Facu(models.Model):
    nombre = models.CharField(max_length=50)
    legajo = models.CharField(max_length=6)
    fecha = models.DateField(null=True)
    
    def __str__(self):
        return f'{self.nombre} - {self.legajo}'
    
    
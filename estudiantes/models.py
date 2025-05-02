from django.db import models
from django.contrib.auth.models import User

class InfoExtra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="imagenes", null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True) 
    biografia = models.TextField(null=True, blank=True)
    
class Estudiante(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="imagenes", null=True, blank=True)
    biografia = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
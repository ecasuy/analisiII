from django.db import models

# Create your models here.

class empleado(models.Model): 
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField
    telefono = models.IntegerField
    sexo = models.CharField(max_length=25)
    direccion = models.CharField(max_length=60)
    ciudad = models.CharField(max_length=50)

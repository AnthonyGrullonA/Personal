from django.db import models

# Create your models here.

class testModel(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    posicion = models.CharField(max_length=100)
    rango = models.CharField(max_length=100)
    
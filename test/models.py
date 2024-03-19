from django.db import models

# Create your models here.
class Cliente(models.Model):
    Nombre_Empresa = models.CharField(max_length=100)
    RNC_Empresa = models.CharField(max_length=100)
    #..etc
    
    
class User(models.Model):
    Nombre_Usuario = models.CharField(max_length=100)
    Apellido_Usuario = models.CharField(max_length=100)
    Empresa = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    
class Facturacion(models.Model):
    ''' ... FACTURACION'''
    Empresa = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    

#Demas modelos
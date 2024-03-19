from django.db import models
from clientdata import models as clientdata_models
    
class ACL(models.Model):
    Nombre = models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100)
    Empresa = models.ForeignKey(clientdata_models.Cliente, on_delete=models.CASCADE)
    Telefono = models.IntegerField(null=True)
    Celular = models.IntegerField(null=True)
    Identificacion = models.CharField(max_length=100)
    email = models.EmailField()
    fecha_entrada = models.DateField(null=True, blank=True)  
    fecha_salida = models.DateField(null=True, blank=True)   
    autorizado_nap = models.BooleanField(default=False)
    categoria = models.CharField(max_length=100, null=True)
    def __str__(self):
        return f'{self.Nombre} {self.Apellido}'
    
class Autorizador(models.Model):
    Nombre = models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100)
    Identificacion = models.CharField(max_length=100)
    Posicion = models.CharField(max_length=100)
    Empresa = models.ForeignKey(clientdata_models.Cliente, on_delete=models.CASCADE, null=True)  # Cambiado a ACL en lugar de Cliente
    def __str__(self):
        return f'{self.Nombre} {self.Apellido}'

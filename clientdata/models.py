from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_migrate
# Create your models here.

class Industria(models.Model):
    nombre_industria = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Industria"
        verbose_name_plural = "Industrias"    
    
    def __str__(self):
        return self.nombre_industria
    
    
class status(models.Model):
    status_name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estados"    
    
    def __str__(self):
        return self.status_name

      
class Operacion(models.Model):
    operacion = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Operacion"
        verbose_name_plural = "Operaciones"   
    
    def __str__(self):
        return self.operacion


class Sector(models.Model):
    nombre_sector = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Sector"
        verbose_name_plural = "Secotres"
            
    def __str__(self):
        return self.nombre_sector


class Localidad(models.Model):
    localidad = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Localidad"
        verbose_name_plural = "Localidades"    
    
    def __str__(self):
        return self.localidad
    
class Cliente(models.Model):

    id_cliente = models.AutoField(primary_key=True)
    fecha_registro = models.DateField(auto_now_add=True)
    nombre_empresa = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='imagenes/')
    fecha_inicio_contrato = models.DateField()
    direccion = models.CharField(max_length=200)
    rnc = models.CharField(max_length=30)
    status_cliente = models.ForeignKey(status, on_delete=models.PROTECT)
    tipo_operacion = models.ForeignKey(Operacion, on_delete=models.PROTECT)
    Sector = models.ForeignKey(Sector, on_delete=models.PROTECT)
    industria = models.ForeignKey(Industria, on_delete=models.PROTECT)
    site = models.ForeignKey(Localidad, on_delete=models.PROTECT)
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"    
    
    def __str__(self):
        return self.nombre_empresa
    
    
class Contacto(models.Model):
    id_contacto = models.AutoField(primary_key=True)
    fecha_registro = models.DateField(auto_now_add=True)
    nombre_contacto = models.CharField(max_length=100)
    apellido_contacto = models.CharField(max_length=100)
    identificacion = models.CharField(max_length=50)
    empresa = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=50)
    cargo = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"    

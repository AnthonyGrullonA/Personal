from django.db import models
from datetime import datetime
from clientdata import models as clientdata_models
from django.dispatch import receiver
from django.db.models.signals import post_migrate

class servicios(models.Model):
    id_servicios = models.AutoField(primary_key=True)
    fecha_registro = models.DateField(auto_now_add=True)
    nombre_servicio = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios" 
        
    def __str__(self):
        return self.nombre_servicio

class status(models.Model):
    status_name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Estado (Servicios)"
        verbose_name_plural = "Estados (Servicios)" 
    
    def __str__(self):
        return self.estado_status

@receiver(post_migrate)
def registros_status(sender, **kwargs):
    if sender.name == 'services':
        status.objects.get_or_create(status_name="Contratado")
        status.objects.get_or_create(status_name="En progreso")
        status.objects.get_or_create(status_name="No efectuado")

class Ordenes_De_Servicio(models.Model):
    id_ods = models.AutoField(primary_key=True)
    fecha_registro = models.DateField(auto_now_add=True)
    servicio_contratado = models.ForeignKey(servicios, on_delete=models.PROTECT)  
    nomeclatura_ods = models.CharField(max_length=100, blank=True)
    status = models.ForeignKey(status, on_delete=models.PROTECT)
    fecha_inicio = models.DateField(auto_now_add=True)
    Empresa = models.ForeignKey(clientdata_models.Cliente, on_delete=models.CASCADE, null=True)  

    def save(self, *args, **kwargs):
        if not self.id_ods:
            # Genera la parte de la nomenclatura
            ini = "NAPC"
            separator = "-"
            # Obtiene el ID de la industria desde el modelo Cliente
            sector_productivo = self.clientes.industria
            industria_id = sector_productivo.id_industria

            # Formatea el ID de la industria (agrega "C" si es mayor o igual a 10)
            if industria_id <= 10:
                industria_id_str = f'C{industria_id}'
            else:
                industria_id_str = str(industria_id)

            # Obtiene el último dígito del año actual
            now = datetime.now()
            year = now.year
            last_two_digits = str(year)[-2:]

            # Encuentra el número de secuencia para este cliente
            num_secuencia = Ordenes_De_Servicio.objects.filter(clientes=self.clientes).count() + 1
            num_secuencia_str = f"{num_secuencia:03}"  # Formato '001'

            # Construye la nomenclatura completa
            nomenclatura = f'{ini}{separator}{industria_id_str}{separator}{self.clientes.id_cliente}{separator}{last_two_digits}{separator}{num_secuencia_str}'
            self.nomeclatura_ods = nomenclatura
        super(Ordenes_De_Servicio, self).save(*args, **kwargs)

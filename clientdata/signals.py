from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.apps import apps
from .models import Sector

@receiver(post_migrate)
def registros_sector(sender, **kwargs):
    if sender.name == 'clientdata':  # Reemplaza 'nombre_de_tu_app' con el nombre real de tu app
        TuModelo = apps.get_model('clientdata', 'Sector')  # Reemplaza 'nombre_de_tu_app' y 'TuModelo' con los nombres reales de tu app y modelo

        # Verificar si los registros ya existen
        if not Sector.objects.filter(nombre_sector='Privado').exists():
            Sector.objects.create(nombre_sector='Privado')  # Reemplaza 'campo1', 'valor1', 'campo2', 'valor2' con los valores que desees

        if not Sector.objects.filter(nombre_sector='Publico').exists():
            Sector.objects.create(nombre_sector='Publico')  # Reemplaza 'campo1', 'valor3', 'campo2', 'valor4' con los valores que desees

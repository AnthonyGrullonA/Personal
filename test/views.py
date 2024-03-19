from django.shortcuts import render
from django.views.generic import ListView
from .models import Facturacion

class FacturacionListView(ListView):
    model = Facturacion
    template_name = 'facturacion_list.html'  # Asegúrate de especificar tu plantilla correcta aquí

    def get_queryset(self):
        # Filtra la consulta para incluir solo las facturaciones asociadas con la empresa del usuario
        return Facturacion.objects.filter(Empresa=self.request.user.Empresa)  # Asumiendo que el usuario tiene una relación directa con 'Empresa'

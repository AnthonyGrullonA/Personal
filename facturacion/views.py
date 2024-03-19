from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def Facturacion_Views(request):
    return render(request, "pages/facturas.html")
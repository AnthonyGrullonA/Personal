from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def Contratado_Views(request):
    return render(request, 'pages/contratados.html')


@login_required
def TakeService_Views(request):
    return render(request, 'pages/servicios.html')


@login_required
def Upgrades_Views(request):
    return render(request, 'pages/upgrade.html')
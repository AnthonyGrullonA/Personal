from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('Contratado/', views.Contratado_Views, name='Contratado'),
    path('Services/', views.TakeService_Views, name='Services'),
    path('Upgrades/', views.Upgrades_Views, name='Upgrades')
]

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('Facturacion/', views.Facturacion_Views, name='Facturacion'),
]

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('Incidente/', views.Incidente_Views, name='Incidente'),
]

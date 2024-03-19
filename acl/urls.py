from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('ACL/', views.ACL_Views, name='ACL'),
    path('Temporal/', views.ACL_Temporales_Views, name='Temporal'),
    path('Permanente_Form/', views.ACL_Form_View, name='Permanente_Form'),
    path('Temporal_Form/', views.ACL_Form_View_Temporal, name='Temporal_Form')

]

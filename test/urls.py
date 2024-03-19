# urls.py
from django.urls import path
from .views import FacturacionListView

urlpatterns = [
    path('', FacturacionListView.as_view(), name='facturaciones-list'),
]

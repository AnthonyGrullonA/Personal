from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.Login_View, name='login'),
    path('logout/', views.Logout_View, name='logout'),

]

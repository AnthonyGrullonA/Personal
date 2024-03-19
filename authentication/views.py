from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

# Create your views here.

def Login_View(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("Usuario autenticado correctamente")
            return redirect('/')  
        else:
            messages.error(request, 'Credenciales inválidas. Por favor, inténtalo de nuevo.')
            print("Error de autenticación")

    return render(request, 'auth/login.html')


def Logout_View(request):
    logout(request)
    return redirect('/')

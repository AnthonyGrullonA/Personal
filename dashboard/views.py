from django.shortcuts import render
from . import models
from django.http.response import JsonResponse
from authentication import models as auth_custom
from django.contrib.auth.decorators import login_required

@login_required
def Dashboard(request):

    if request.user.is_authenticated:
        # Obtiene el perfil del usuario autenticado usando el email
        perfil = auth_custom.CustomUser.objects.get(email=request.user.email)

        context ={
            'perfil': perfil,
        }
        return render(request, 'index.html', context)
    else:
        return render(request, 'index.html')

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms
from authentication.utils import obtener_empresa_del_usuario

@login_required
def ACL_Views(request):
    return render(request, 'pages/acl.html')

@login_required
def ACL_Temporales_Views(request):
    return render(request, 'pages/temporal.html')

@login_required
def ACL_Form_View(request):
    if request.method == 'POST':
        # Pasa el usuario como un kwarg al formulario
        form = forms.ACLForm(request.POST, user=request.user)
        if form.is_valid():
            acl = form.save(commit=False)
            acl.Empresa = obtener_empresa_del_usuario(request.user)
            acl.categoria = 'PERMANENTE'
            acl.save()
            return redirect('ACL')  # Asegúrate de usar el nombre correcto de tu URL
    else:
        form = forms.ACLForm(user=request.user)  # También pasa el usuario en solicitudes GET para lógica personalizada
    
    Banner = 'Formulario de cliente permanente'
    context = {
        'Titulo_Form' : Banner
    }
    return render(request, 'forms/add.html', {'form': form, **context})

@login_required
def ACL_Form_View_Temporal(request):
    if request.method == 'POST':
        # Pasa el usuario como un kwarg al formulario
        form = forms.ACLForm_Temporal(request.POST, user=request.user)
        if form.is_valid():
            acl = form.save(commit=False)
            acl.Empresa = obtener_empresa_del_usuario(request.user)
            acl.categoria = 'TEMPORAL'
            acl.save()
            return redirect('ACL')  # Asegúrate de usar el nombre correcto de tu URL
    else:
        form = forms.ACLForm_Temporal(user=request.user)  # También pasa el usuario en solicitudes GET para lógica personalizada
    
    Banner = 'Formulario de cliente temporal'
    context = {
        'Titulo_Form' : Banner
    }
    return render(request, 'forms/add.html', {'form': form, **context})

@login_required
def add_autorizador_view(request):
    if request.method == 'POST':
        form = forms.AutorizadorForm(request.POST)
        if form.is_valid():
            autorizador = form.save()
            return redirect('ACL')
    else:
        form = forms.AutorizadorForm()

    return render(request, 'forms/add.html', {'form': form})

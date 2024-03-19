from django import forms
from .models import ACL, Autorizador

class ACLForm_Temporal(forms.ModelForm):
    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        
    class Meta:
        model = ACL
        fields = ['Nombre', 'Apellido', 'Empresa', 'Telefono', 'Celular', 'Identificacion', 'email', 'fecha_entrada', 'fecha_salida', 'autorizado_nap', 'categoria']
        exclude = ['Empresa', 'categoria', 'autorizado_nap']
        widgets = {
            'Nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'Apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'Telefono': forms.NumberInput(attrs={'class': 'form-control'}),
            'Celular': forms.NumberInput(attrs={'class': 'form-control'}),
            'Identificacion': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'fecha_entrada': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_salida': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        
class ACLForm(forms.ModelForm):
    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        
    class Meta:
        model = ACL
        fields = ['Nombre', 'Apellido', 'Empresa', 'Telefono', 'Celular', 'Identificacion', 'email', 'fecha_entrada', 'fecha_salida', 'autorizado_nap', 'categoria']
        exclude = ['Empresa', 'categoria', 'autorizado_nap', 'fecha_salida', 'fecha_entrada']
        widgets = {
            'Nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'Apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'Telefono': forms.NumberInput(attrs={'class': 'form-control'}),
            'Celular': forms.NumberInput(attrs={'class': 'form-control'}),
            'Identificacion': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class AutorizadorForm(forms.ModelForm):
    class Meta:
        model = Autorizador
        fields = ['Nombre', 'Apellido', 'Identificacion', 'Posicion', 'Empresa']
        exclude = ['Empresa']
        widgets = {
            'Nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'Apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'Identificacion': forms.TextInput(attrs={'class': 'form-control'}),
            'Posicion': forms.TextInput(attrs={'class': 'form-control'}),
        }

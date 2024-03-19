from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.utils.html import format_html

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'nombre', 'is_staff', 'is_active', 'mostrar_imagen']
    
    def mostrar_imagen(self, obj):
        if obj.imagen_perfil:  
            return format_html('<img src="{}" width="50" height="50" />', obj.imagen_perfil.url)
        return "-"
    
    mostrar_imagen.allow_tags = True
    mostrar_imagen.short_description = 'Imagen'
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Información personal', {'fields': ('nombre', 'empresa', 'posicion', 'imagen_perfil')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Fechas importantes', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nombre', 'password1', 'password2', 'empresa'),
        }),
    )
    search_fields = ['email', 'nombre']
    ordering = ['email']

admin.site.register(CustomUser, CustomUserAdmin)

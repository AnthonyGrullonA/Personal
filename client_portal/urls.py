from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('', include('facturacion.urls')),
    path('', include('acl.urls')),
    path('', include('services.urls')),
    path('', include('report.urls')),
    path('', include('clientdata.urls')),
    path('', include('authentication.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('productos.urls')),  # Asegúrate de que esta línea esté presente
    path('productos_proximos/', include('productos.urls')),  # Cambiamos 'productos/' por 'productos_proximos/'
] 
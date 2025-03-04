from django.urls import path
from django.shortcuts import redirect
from . import views

def redirect_to_guardar(request):
    return redirect('agregar_producto')

urlpatterns = [
    path('', redirect_to_guardar, name='home'),  # Redirección desde la raíz
    path('productos_proximos/', views.productos_proximos, name='productos_proximos'),
    path('guardar_productos/', views.guardar_productos, name='agregar_producto'),
] 
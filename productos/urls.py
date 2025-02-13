from django.urls import path
from django.shortcuts import redirect
from . import views

def redirect_to_guardar(request):
    return redirect('agregar_producto')

urlpatterns = [
    path('', views.tu_vista, name='tu_vista'),
    path('productos_proximos/', views.productos_proximos, name='productos_proximos'),
    path('guardar_productos/', views.guardar_productos, name='agregar_producto'),
] 
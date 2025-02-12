from django.shortcuts import render, redirect
from .models import Producto
from datetime import datetime

def guardar_productos(request):
    if request.method == 'POST':
        codigo_barra = request.POST['codigo_barra']
        nombre = request.POST['nombre']
        fecha_vencimiento = request.POST['fecha_vencimiento']
        
        producto = Producto(
            codigo_barra=codigo_barra,
            nombre_producto=nombre,
            fecha_vencimiento=fecha_vencimiento
        )
        producto.save()
        return redirect('productos_proximos')
    
    return render(request, 'productos/guardar_productos.html')

def productos_proximos(request):
    productos = Producto.objects.all().order_by('fecha_vencimiento')
    return render(request, 'productos/productos_proximos.html', {'productos': productos}) 
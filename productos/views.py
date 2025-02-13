from django.shortcuts import render, redirect
from .models import Producto
from datetime import datetime, timedelta
from django.db import IntegrityError

def guardar_productos(request):
    if request.method == 'POST':
        codigo_barra = request.POST['codigo_barra']
        nombre = request.POST['nombre']
        fecha_vencimiento = request.POST['fecha_vencimiento']
        
        try:
            producto = Producto(
                codigo_barra=codigo_barra,
                nombre_producto=nombre,
                fecha_vencimiento=fecha_vencimiento
            )
            producto.save()
            return redirect('productos_proximos')
        except IntegrityError:
            # Manejar el error de duplicado
            error_message = "El código de barra ya existe. Por favor, ingrese uno diferente."
            return render(request, 'productos/guardar_productos.html', {'error_message': error_message})
    
    return render(request, 'productos/guardar_productos.html')

def productos_proximos(request):
    filtro = request.GET.get('filtro', None)
    productos = Producto.objects.all().order_by('fecha_vencimiento')

    if filtro:
        hoy = datetime.now().date()
        if filtro == 'vencido':
            productos = productos.filter(fecha_vencimiento__lt=hoy)
        elif filtro == 'rojo':
            productos = productos.filter(fecha_vencimiento__range=(hoy, hoy + timedelta(days=15)))
        elif filtro == 'amarillo':
            productos = productos.filter(fecha_vencimiento__range=(hoy + timedelta(days=16), hoy + timedelta(days=29)))
        elif filtro == 'verde':
            productos = productos.filter(fecha_vencimiento__gte=hoy + timedelta(days=30))

    return render(request, 'productos/productos_proximos.html', {'productos': productos})

def home(request):
    return render(request, 'productos/guardar_productos.html') 
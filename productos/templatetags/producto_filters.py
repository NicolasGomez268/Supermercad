from django import template
from datetime import datetime, timedelta

register = template.Library()

@register.filter(name='vencimiento_class')
def vencimiento_class(producto):
    hoy = datetime.now().date()
    dias_restantes = (producto.fecha_vencimiento - hoy).days

    if dias_restantes < 0:
        return 'vencido'
    elif dias_restantes <= 15:
        return 'rojo'
    elif dias_restantes <= 29:
        return 'amarillo'
    else:
        return 'verde' 
from django.db import models

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    codigo_barra = models.CharField(max_length=100)
    nombre_producto = models.CharField(max_length=200)
    fecha_vencimiento = models.DateField()

    class Meta:
        db_table = 'productos'

    def __str__(self):
        return self.nombre_producto 
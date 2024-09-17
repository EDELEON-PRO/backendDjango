# productos/models.py

from django.db import models
from authentification.models import User  # Importar el modelo de usuario personalizado

class TipoProducto(models.Model):
    id_tipoproducto = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=100)

class Producto(models.Model):
    codigo = models.CharField(max_length=100, unique=True)  # Código único para el producto
    codigo_tipo = models.ForeignKey(TipoProducto, on_delete=models.CASCADE, related_name='productos')
    nombre = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)  # Precio con dos decimales
    cantidad = models.PositiveIntegerField()  # Cantidad en stock
    imagen = models.ImageField(upload_to='imagenes/', blank=True, null=True)  # Permitir nulos
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Relación con el modelo User

    def __str__(self):
        return self.nombre
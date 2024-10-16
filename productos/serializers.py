# productos/serializers.py

from rest_framework import serializers
from .models import Producto,TipoProducto,Categoria

class TipoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoProducto
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields ='__all__' #['id', 'codigo', 'nombre', 'precio', 'cantidad', 'imagen','usuario']
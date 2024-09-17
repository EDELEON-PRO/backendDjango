# productos/views.py

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Producto,TipoProducto
from .serializers import ProductoSerializer,TipoProductoSerializer

class TipoProductoViewSet(viewsets.ModelViewSet):
    queryset = TipoProducto.objects.all()
    serializer_class = TipoProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated]  # Asegúrate de que solo los usuarios autenticados puedan acceder

    def perform_create(self, serializer):
        # Asignar el usuario autenticado al producto al crearlo
        serializer.save(usuario=self.request.user)

    def get_queryset(self):
        # Filtrar los productos para que solo el usuario autenticado vea sus propios productos
        return Producto.objects.filter(usuario=self.request.user)


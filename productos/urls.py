# productos/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet,TipoProductoViewSet,CategoriaSerializer

router = DefaultRouter()
router.register(r'productos', ProductoViewSet)
router.register(r'tipo-productos', TipoProductoViewSet)
router.register(r'categorias', CategoriaSerializer)

urlpatterns = [
    path('', include(router.urls)),
]
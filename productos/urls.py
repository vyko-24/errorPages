from django.urls import path, include 
from rest_framework.routers import SimpleRouter
from .views import ProductoViewSet, agregar_producto, prueba_view

router = SimpleRouter()
router.register(r'api', ProductoViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('agregar/', agregar_producto, name='agregar_producto'),
    path('prueba/', prueba_view, name='prueba')
]


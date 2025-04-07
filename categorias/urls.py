from django.urls import path
from .views import *

urlpatterns = [
    path('registrar/', agregar_categoria, name='registrar'),
    path('api/get/', lista_categorias, name='lista'),
    path('json/', json_view, name='json'),
    path('api/post/', registrar_categoria, name='post')
]
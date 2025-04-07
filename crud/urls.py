from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import *

router = SimpleRouter()
router.register(r'api',CrudViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('unCrud/', unCrud, name='unCrud')
]
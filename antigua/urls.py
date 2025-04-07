from django.urls import path
from .views import apiGet, apiPist

url_patterns=[
    path('api/get/', apiGet, name='apiGet'),
    path('api/post/', apiPist, name='apiPist')
]
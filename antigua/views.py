from django.shortcuts import render, redirect
from .forms import AntiguoForm
from .models import Antigua
from django.http import JsonResponse


import json
# Create your views here.
def apiGet(request):
    antiguo = Antigua.objects.all()
    data = [
        {
            'nombre':a.nombre,
            'descripcion':a.descripcion
        }
        for a in antiguo
    ]

    return JsonResponse(data, safe=False)

def apiPist(request):
    if request.method=='POST':
        try:
            data = json.loads(request.body)
            newData = Antigua.objects.create(
                nombre=data['nombre'],
                descripcion = data['descripcion']
            )
            return JsonResponse({
                'mensaje':'Registro exitoso',
                'id':newData.id
            }, status=200)
        except Exception as e:
            return JsonResponse({
                'error':str(e)
            }, status=400)
    return JsonResponse({
        'mensaje':'error este no es un POST'
    }, status=405)
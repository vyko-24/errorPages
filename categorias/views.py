from django.shortcuts import render, redirect
from .models import Categoria
from .forms import categoriaForm
from django.http import JsonResponse

#Agregar una categoria
def agregar_categoria(request):
    #Checamos como llegamos a esta funcion
    if request.method == 'POST':
        #Llegamos aqui por el envio del formulario
        form = categoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('json') #Esto redirige a la lista de categorias
    else:
        form = categoriaForm()
    return render(request, 'agregarCategoria.html', {'form':form})


#Devuelve el JSON
def lista_categorias(request):
    categorias = Categoria.objects.all()
    #Para enviar un JSON debemos escribir los datos en un diccionario usando llaves
    #Diccionario personalizado
    data = [
        {
            'nombre': c.nombre,
            'imagen': c.imagen,
        }
        for c in categorias
    ]

    return JsonResponse(data, safe=False)

def json_view(request):
    return render(request, 'jsonCategoria.html')

import json
#@csrf_exempt <- no es seguro hacer esto (no lo hagas)
def registrar_categoria(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            nuevo_categoria = Categoria.objects.create(
                nombre = data['nombre'],
                imagen = data['imagen']
            )
            return JsonResponse({
                'mensaje': 'Registro Exitoso',
                'id': nuevo_categoria.id
            },status = 201)
        except Exception as e:
            return JsonResponse({
                'error': str(e)
            },status=400)
    return JsonResponse({
        'error': 'Metodo no es POST'
    }, status = 405)
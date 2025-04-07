from .models import Alumnos
from .serializers import AlumnoSerializer
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from .forms import alumnoForm
from django.shortcuts import render
#from .forms 

class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumnos.objects.all()
    serializer_class = AlumnoSerializer
    renderer_classes = [JSONRenderer]

#def agregar_producto(request):
def agregar_alumno(request):
    form = alumnoForm()
    return render(request, 'Barrera_Víctor.html',{'form':form})
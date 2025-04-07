from django.shortcuts import render
from .serializers import CrudSerializer
from .models import Crud
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from .forms import crudForm

# Create your views here.
class CrudViewSet(viewsets.ModelViewSet):
    queryset = Crud.objects.all()
    serializer_class = CrudSerializer
    renderer_classes = [JSONRenderer]

def unCrud(request):
    form = crudForm()
    return render(request, 'crud.html',{'form':form})
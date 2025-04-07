from rest_framework import serializers
from .models import Alumnos

class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumnos
        fields = '__all__'
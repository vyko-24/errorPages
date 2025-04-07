from .models import Crud
from rest_framework import serializers

class CrudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crud
        fields = '__all__'
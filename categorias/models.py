from django.db import models

# Create your models here.
class Categoria(models.Model):
    #Definir los ateributos de clase
    nombre = models.CharField(max_length=100)
    imagen = models.URLField()

    def __str__(self):
        return self.nombre

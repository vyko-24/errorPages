from django.db import models

# Create your models here.
class Antigua(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=255)

    def __str__(self):
        return self.nombre
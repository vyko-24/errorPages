from django.db import models

class ErrorLog(models.Model):
    codigo = models.CharField(max_length=10)
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{codigo} - {mensaje}"

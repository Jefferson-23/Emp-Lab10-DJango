from django.db import models

# Create your models here.

class Producto(models.Model):
    codigo = models.IntegerField(unique=True)
    descripcion = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2) 
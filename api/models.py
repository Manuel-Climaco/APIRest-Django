from django.db import models

# Create your models here.

class Catalogo(models.Model):
    titulo = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    sinopsis = models.TextField()
    fecha_alta = models.DateTimeField(auto_now_add=True)
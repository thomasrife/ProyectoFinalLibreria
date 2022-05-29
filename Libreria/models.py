from concurrent.futures.process import _MAX_WINDOWS_WORKERS
from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    editorial = models.CharField(max_length=100)
    fecha_de_publicacion = models.DateField()
    isbn = models.IntegerField()

class Editorial(models.Model):
    nombre_editorial = models.CharField(max_length=100)
    pais_editorial = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
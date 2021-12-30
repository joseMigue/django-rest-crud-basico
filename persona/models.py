from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()

    def __str__(self):
        return self.nombre

class Pelicula(models.Model):
    titulo = models.CharField(max_length=50)
    año = models.IntegerField()

    def __str__(self):
        return self.titulo

class Alumno(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
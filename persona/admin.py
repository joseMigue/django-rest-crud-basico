from django.contrib import admin

from persona.models import Alumno, Pelicula, Persona

# Register your models here.
admin.site.register(Persona)
admin.site.register(Pelicula)
admin.site.register(Alumno)
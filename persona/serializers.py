from rest_framework import serializers
from persona.models import Alumno, Pelicula, Persona

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'

class PeliculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelicula
        fields = '__all__'
        
class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = '__all__'
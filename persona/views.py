from django.http import response
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import generics,status
from rest_framework.serializers import raise_errors_on_nested_writes
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from persona import models
from persona import serializers
from persona.models import Alumno, Pelicula, Persona
from persona.serializers import AlumnoSerializer, PeliculaSerializer, PersonaSerializer

# Create your views here.
class PersonaLista(generics.ListCreateAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    
class PersonaAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    
@api_view(['GET', 'POST'])
def peliculas_lista(request):
    if (request.method == 'GET'):
        peliculas = Pelicula.objects.all()
        serializer = PeliculaSerializer(peliculas,many=True)
        return Response(serializer.data)

    elif (request.method == 'POST'):
        serializer = PeliculaSerializer(data=request.data)
        if (serializer.is_valid()):
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def peliculas_detalle(request, pk):
    try:
        pelicula = Pelicula.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if (request.method == 'GET'):
        serializer = PeliculaSerializer(pelicula)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PeliculaSerializer(pelicula, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        pelicula.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AlumnoLista(APIView):
    def get(request):
        alumno = Alumno.objects.all()
        serializer = AlumnoSerializer(alumno,many=True)
        return Response(serializer.data)

    def post(request):
        serializers = AlumnoSerializer(data=request.data)
        if serializers.is_valid():
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class ALumnoDetalle(APIView):
    def get_object(self, pk):
        try:
            return Alumno.objects.get(pk=pk)
        except:
            raise response.Http404

    def get(self,request,pk,format=None):
        alumno = self.get_object(pk)
        serializer = AlumnoSerializer(alumno)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        alumno = self.get_object(pk)
        serializer = AlumnoSerializer(alumno, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request,pk, format=None):
        alumno = Alumno.objects.get(pk=pk)
        alumno.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


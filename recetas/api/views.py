from rest_framework import generics
from django.shortcuts import render
from .models import Usuario
#from .models import Receta
#from .models import Categoria
#from .models import Comentario
from .serializers import UsuarioSerializer
#from .serializers import RecetaSerializer



#Métodos usuarios
class UsuarioListCreate(generics.ListCreateAPIView):
    queryset = Usuario.objects.all() #Define el conjunto de datos que se utilizarán (todas las recetas)
    serializer_class = UsuarioSerializer #Especifica el serializer para convertir los datos a JSON


class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    
   
    
""" 
#Métodos recetas
class RecetaListCreate(generics.ListCreateAPIView):
    queryset = Receta.objects.all()
    serializer_class = RecetaSerializer


class RecetaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Receta.objects.all()
    serializer_class = RecetaSerializer   
       
#Métodos categorias

class CategoriaListCreate(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    

#Métodos comentarios

class ComentarioListCreate(generics.ListCreateAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer


class ComentarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

"""
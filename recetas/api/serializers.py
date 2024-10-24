#INFORMACIÓN QUE SE VA A USAR Y COMO SE VA A USAR
from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import Usuario
from .models import Receta
from .models import Categoria
from .models import Comentario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
    def validate_Nombre(self, value):
        if len(value) <= 2:
            raise serializers.ValidationError("El nombre debe tener más de 2 caracteres.")
        return value

    def validate_Apellido(self, value):
        if len(value) <= 2:
            raise serializers.ValidationError("El Apellido debe tener más de 2 caracteres.")
        return value    


class RecetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receta
        fields = '__all__'

    def validate_Nombre_Receta(self, value):
        if len(value) <= 5:
            raise serializers.ValidationError("El Nombre de la Receta debe tener más de 5 caracteres.")
        return value   

    def validate_Descripcion(self, value):
        if len(value) <= 20:
            raise serializers.ValidationError("La Descripción de la Receta debe tener más de 20 caracteres.")
        return value           
   

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
       
    def validate_Nombre_Categoria(self, value):
        if len(value) <= 5:
            raise serializers.ValidationError("El nombre de la Categoria debe tener más de 5 caracteres.")
        return value   

    def validate_Descripcion_Categoria(self, value):
        if len(value) <= 20:
            raise serializers.ValidationError("La Descripción de la Categoria debe tener más de 20 caracteres.")
        return value        


class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'

    def validate_Comentario(self, value):
        if len(value) <= 10:
            raise serializers.ValidationError("El comentario debe tener más de 10 caracteres.")
        return value  



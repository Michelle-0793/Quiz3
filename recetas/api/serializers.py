#INFORMACIÓN QUE SE VA A USAR Y COMO SE VA A USAR
from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import Usuario
#from .models import Receta
#from .models import Categoria
#from .models import Comentario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

        def clean(self):
             # Validar espacios vacios
             if not self.Nombre.strip() or not self.Apellido.strip() or not self.Correo.strip():
                raise ValidationError('Espacios Obligatorios')
   
"""
class RecetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receta
        fields = '__all__'

        def clean(self):
        # Validar campos vacios
         if not self.Nombre_Receta.strip() or not self.Descripcion.strip():
            raise ValidationError('Espacios Obligatorios')

        # Validar que no exista otra receta con el mismo Nombre
         if Receta.objects.filter(Nombre_Receta=self.Nombre_Receta).exists():
            raise ValidationError(f'Ya existe una receta con el nombre: {self.Nombre_Receta}')

     

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
       
# Validar campos vacios
        if not self.Nombre_Categoria.strip() or not self.Descripcion_Categoria.strip():
            raise ValidationError('Espacios Obligatorios')


class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentarios
        fields = '__all__'

# Validar campos vacios
        if not self.Comentario.strip()
         raise ValidationError('Espacios Obligatorios')


"""
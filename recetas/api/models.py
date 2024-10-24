from django.db import models


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100)
    Correo = models.EmailField(unique=True)

    def __str__(self):
         return str(self.nombre)
         

"""""
class Receta(models.Model):

    nombre_Receta = models.CharField(max_length=100)
    Descripcion = models.CharField(max_length=1000)
    id_Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
         return str(self.nombre_Receta)


class Categoria(models.Model):

    nombre_Categoria= models.CharField(max_length=100)
    Descripcion_Categoria = models.CharField(max_length=1000)
    id_Receta = models.ForeignKey(Receta, on_delete=models.CASCADE)

    def __str__(self):
         return str(self.nombre_Categoria)  



class Comentarios(models.Model):

    Comentario= models.CharField(max_length=100)
    id_Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_Receta = models.ForeignKey(Receta, on_delete=models.CASCADE)

    def __str__(self):
         return str(self.Comentario)        



"""
              
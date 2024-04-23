from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_categoria
    
class Curso(models.Model):
    curso = models.CharField(max_length=100)
    descripcion = models.TextField()
    link = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, related_name='categoria_curso')

    def __str__(self):
        return self.curso
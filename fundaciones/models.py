from django.db import models

# Create your models here.
class Fundacion(models.Model):
    nombre_fundacion = models.CharField(max_length=100)
    nombre_responsable = models.CharField(max_length=100)
    numero_celular = models.CharField(max_length=20)
    calle = models.CharField(max_length=100)
    numero = models.CharField(max_length=20)
    localidad = models.CharField(max_length=100, blank=True)  # Asumiendo que "Acacia" es una localidad
    codigo_postal = models.CharField(max_length=12)
    telefono = models.CharField(max_length=20, blank=True)
    pagina_web = models.URLField(max_length=200, blank=True)
    correo_electronico = models.EmailField(max_length=100, blank=True)

    def __str__(self):
        return self.nombre_fundacion
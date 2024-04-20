from django.db import models
from fundaciones.models import Fundacion

# Create your models here.
class Adolescente(models.Model):
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    nombres = models.CharField(max_length=200)
    edad = models.PositiveIntegerField()
    canalizada_por = models.CharField(max_length=200)
    escolaridad_actual = models.CharField(max_length=200)
    tutor_responsable_nombre = models.CharField(max_length=200)
    tutor_responsable_apellidos = models.CharField(max_length=200)
    tutor_responsable_telefono = models.CharField(max_length=15)
    nacionalidad = models.CharField(max_length=100)
    lugar_nacimiento = models.CharField(max_length=100)
    pertenece_etnia = models.BooleanField(default=False)
    tiene_discapacidad = models.BooleanField(default=False)
    discapacidad_detalle = models.CharField(max_length=200, blank=True)
    diagnostico_psicologico = models.BooleanField(default=False)
    diagnostico_detalle = models.CharField(max_length=200, blank=True)
    tiene_hijos = models.BooleanField(default=False)
    posee_acta_nacimiento = models.BooleanField(default=False)
    posee_seguro_social = models.BooleanField(default=False)
    posee_curp = models.BooleanField(default=False)
    estudia_actualmente = models.BooleanField(default=False)
    lugar_estudios = models.CharField(max_length=200, blank=True)
    trabaja_actualmente = models.BooleanField(default=False)
    lugar_trabajo = models.CharField(max_length=200, blank=True)
    impedimento_continuar_estudios = models.TextField(blank=True)
    fundacion = models.ForeignKey(Fundacion, on_delete=models.CASCADE, related_name='adolescentes_inscritas')


    def __str__(self):
        return f'{self.nombres} {self.apellido_paterno} {self.apellido_materno}'
    
   
from django.db import models
from fundaciones.models import Fundacion
from cursos.models import Curso
from Adolescentes.opciones_formulario import NACIONALIDAD_CHOICES, EDAD_CHOICES, SI_NO_OPCIONES, DISCAPACIDAD_CHOICES, TERMINADO, ESCOLARIDAD

# Create your models here.
class Adolescente(models.Model):
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    nombres = models.CharField(max_length=200)
    edad = models.PositiveSmallIntegerField(choices=EDAD_CHOICES)
    canalizada_por = models.CharField(max_length=200)
    escolaridad_actual = models.CharField(max_length=200, choices= ESCOLARIDAD, default='Secundaria')
    tutor_responsable_nombre = models.CharField(max_length=200)
    tutor_responsable_apellidos = models.CharField(max_length=200)
    tutor_responsable_telefono = models.CharField(max_length=15)
    nacionalidad = models.CharField(max_length=100, choices=NACIONALIDAD_CHOICES, default='MEXICANA')
    otra_nacionalidad = models.CharField(max_length=100, blank=True, null=True)
    lugar_nacimiento = models.CharField(max_length=100)
    pertenece_etnia = models.BooleanField(choices=SI_NO_OPCIONES, default=False)
    discapacidad = models.CharField(max_length=100, choices=DISCAPACIDAD_CHOICES, default='Ninguna')
    diagnostico_psicologico = models.BooleanField(choices=SI_NO_OPCIONES, default=False)
    diagnostico_detalle = models.CharField(max_length=200, blank=True)
    tiene_hijos = models.BooleanField(choices=SI_NO_OPCIONES, default=False)
    posee_acta_nacimiento = models.BooleanField(choices=SI_NO_OPCIONES, default=False)
    posee_seguro_social = models.BooleanField(choices=SI_NO_OPCIONES, default=False)
    posee_curp = models.BooleanField(choices=SI_NO_OPCIONES, default=False)
    estudia_actualmente = models.BooleanField(choices=SI_NO_OPCIONES, default=False)
    lugar_estudios = models.CharField(max_length=200, blank=True)
    trabaja_actualmente = models.BooleanField(choices=SI_NO_OPCIONES, default=False)
    lugar_trabajo = models.CharField(max_length=200, blank=True)
    impedimento_continuar_estudios = models.TextField(blank=True)
    fundacion = models.ForeignKey(Fundacion, on_delete=models.CASCADE, related_name='adolescentes_inscritas')
    cursos = models.ManyToManyField(Curso, through='CursosInscrito', blank=True),

    def __str__(self):
        return f'{self.nombres} {self.apellido_paterno} {self.apellido_materno}'
    

class CursosInscrito(models.Model):
    cursos = models.ForeignKey(Curso, on_delete=models.CASCADE, blank=True, null=True)
    adolescentes = models.ForeignKey(Adolescente, on_delete=models.CASCADE, blank=True, null=True)
    fecha_inscripcion = models.DateTimeField(auto_created=True)
    es_terminado = models.BooleanField(choices=TERMINADO, default=False)
    es_destacado = models.BooleanField(default=False)


    def __str__(self):
        return f'Alumno {self.adolescentes} inscrito en {self.cursos}'


class Progreso(models.Model):
    adolescente = models.ForeignKey(Adolescente, on_delete=models.CASCADE, related_name= 'Progreso_del_adolescente')
    Autoestima = models.BooleanField(choices=TERMINADO, default=False)
    Necesidades_e_intereses = models.BooleanField(choices=TERMINADO, default=False)
    Habilidades_sociales  = models.BooleanField(choices=TERMINADO, default=False)
    Derechos_humanos = models.BooleanField(choices=TERMINADO, default=False)

    def __str__(self):
        return "Progreso"
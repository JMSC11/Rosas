MEXICANA = 'MX'
OTRA = 'OT'
NACIONALIDAD_CHOICES = [
    (MEXICANA, 'Mexicana'),
    (OTRA, 'Otra'),
]

DISCAPACIDAD_CHOICES = [
    ('NINGUNA', 'Ninguna'),
    ('FISICA/MOTRIZ', 'Discapacidad Física/Motriz'),
    ('SENSORIAL', 'Discapacidad Sensorial'),
    ('INTELECTUAL', 'Discapacidad Intelectual'),
    ('PSÍQUICA', 'Discapacidad Psíquica'),
]

EDAD_CHOICES = [(edad, edad) for edad in range(13, 18)]

SI_NO_OPCIONES = [
    (True, 'Sí'),
    (False, 'No'),
]

TERMINADO = [
    (True, 'TERMINADO'),
    (False, 'PENDIENTE'),
]

ESCOLARIDAD = [
    ('Primaria', 'Primaria'),
    ('Secundaria', 'Secundaria'),
    ('Bachillerato', 'Bachillerato'),
    ('Licenciatura', 'Licenciatura'),
]
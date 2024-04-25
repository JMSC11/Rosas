# Generated by Django 5.0.4 on 2024-04-25 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adolescentes', '0003_progreso'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adolescente',
            name='discapacidad_detalle',
        ),
        migrations.RemoveField(
            model_name='adolescente',
            name='pertenece_etnia',
        ),
        migrations.RemoveField(
            model_name='adolescente',
            name='tiene_discapacidad',
        ),
        migrations.AddField(
            model_name='adolescente',
            name='discapacidad',
            field=models.CharField(choices=[('NINGUNA', 'Ninguna'), ('FISICA/MOTRIZ', 'Discapacidad Física/Motriz'), ('SENSORIAL', 'Discapacidad Sensorial'), ('INTELECTUAL', 'Discapacidad Intelectual'), ('PSÍQUICA', 'Discapacidad Psíquica'), ('OTRA', 'Otra')], default='NINGUNA', max_length=100),
        ),
        migrations.AddField(
            model_name='adolescente',
            name='etnia',
            field=models.CharField(choices=[('NINGUNA', 'Ninguna'), ('KILIWA', 'Kiliwa'), ('QUICHÉ', 'Quiché'), ('CHOL', 'Chol'), ('PIMA', 'Pima'), ('OTRA', 'Otra')], default='NINGUNA', max_length=100),
        ),
        migrations.AddField(
            model_name='adolescente',
            name='nacionalidad_otra',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='adolescente',
            name='edad',
            field=models.PositiveSmallIntegerField(choices=[(12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30)]),
        ),
        migrations.AlterField(
            model_name='adolescente',
            name='nacionalidad',
            field=models.CharField(choices=[('MX', 'Mexicana'), ('OT', 'Otra')], default='MEXICANA', max_length=100),
        ),
    ]
# Generated by Django 5.0.4 on 2024-04-25 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adolescentes', '0004_remove_adolescente_discapacidad_detalle_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adolescente',
            old_name='nacionalidad_otra',
            new_name='otra_nacionalidad',
        ),
        migrations.AlterField(
            model_name='adolescente',
            name='diagnostico_psicologico',
            field=models.BooleanField(choices=[(True, 'Sí'), (False, 'No')], default=False),
        ),
        migrations.AlterField(
            model_name='adolescente',
            name='edad',
            field=models.PositiveSmallIntegerField(choices=[(13, 13), (14, 14), (15, 15), (16, 16)]),
        ),
        migrations.AlterField(
            model_name='adolescente',
            name='estudia_actualmente',
            field=models.BooleanField(choices=[(True, 'Sí'), (False, 'No')], default=False),
        ),
        migrations.AlterField(
            model_name='adolescente',
            name='posee_acta_nacimiento',
            field=models.BooleanField(choices=[(True, 'Sí'), (False, 'No')], default=False),
        ),
        migrations.AlterField(
            model_name='adolescente',
            name='posee_curp',
            field=models.BooleanField(choices=[(True, 'Sí'), (False, 'No')], default=False),
        ),
        migrations.AlterField(
            model_name='adolescente',
            name='posee_seguro_social',
            field=models.BooleanField(choices=[(True, 'Sí'), (False, 'No')], default=False),
        ),
        migrations.AlterField(
            model_name='adolescente',
            name='tiene_hijos',
            field=models.BooleanField(choices=[(True, 'Sí'), (False, 'No')], default=False),
        ),
        migrations.AlterField(
            model_name='adolescente',
            name='trabaja_actualmente',
            field=models.BooleanField(choices=[(True, 'Sí'), (False, 'No')], default=False),
        ),
        migrations.AlterField(
            model_name='cursosinscrito',
            name='es_terminado',
            field=models.BooleanField(choices=[(True, 'Sí'), (False, 'No')], default=False),
        ),
        migrations.AlterField(
            model_name='progreso',
            name='cuarto_modulo',
            field=models.BooleanField(choices=[(True, 'Sí'), (False, 'No')], default=False),
        ),
        migrations.AlterField(
            model_name='progreso',
            name='primer_modulo',
            field=models.BooleanField(choices=[(True, 'Sí'), (False, 'No')], default=False),
        ),
        migrations.AlterField(
            model_name='progreso',
            name='segundo_modulo',
            field=models.BooleanField(choices=[(True, 'Sí'), (False, 'No')], default=False),
        ),
        migrations.AlterField(
            model_name='progreso',
            name='tercer_modulo',
            field=models.BooleanField(choices=[(True, 'Sí'), (False, 'No')], default=False),
        ),
    ]
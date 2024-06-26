# Generated by Django 5.0.4 on 2024-05-05 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fundaciones', '0002_fundacion_gestor'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fundacion',
            options={'verbose_name': 'Fundación', 'verbose_name_plural': 'Fundaciones'},
        ),
        migrations.AddField(
            model_name='fundacion',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fundacion',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='static/logo_fundacion'),
        ),
    ]

# Generated by Django 5.0.4 on 2024-04-20 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Adolescentes', '0002_adolescente_cursos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adolescente',
            name='cursos',
        ),
    ]

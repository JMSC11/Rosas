from django.contrib import admin
from .models import Adolescente, CursosInscrito
from cursos.models import Curso
# Register your models here.
class CursoInscritoInline(admin.TabularInline):
    model = CursosInscrito
    extra = 1
    autocomplete_fields = ['cursos']

class AdolescentesAdmin(admin.ModelAdmin):
    inlines = [CursoInscritoInline]
    list_display = ['apellido_paterno',
                    'apellido_materno',
                    'nombres',
                    'edad',
                    'fundacion',]
    search_fields = ['apellido_paterno', 'nombres']
    list_filter = []
    filter_horizontal = []

admin.site.register(Adolescente, AdolescentesAdmin)

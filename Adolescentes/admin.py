from django.contrib import admin
from .models import Adolescente, CursosInscrito, Progreso
from cursos.models import Curso
# Register your models here.
class CursoInscritoInline(admin.TabularInline):
    model = CursosInscrito
    extra = 1
    autocomplete_fields = ['cursos']

class ProgresoInline(admin.StackedInline): 
    model = Progreso
    can_delete = False
    extra = 0
class AdolescentesAdmin(admin.ModelAdmin):
    inlines = [CursoInscritoInline, ProgresoInline]
    list_display = ['apellido_paterno',
                    'apellido_materno',
                    'nombres',
                    'edad',
                    'fundacion',]
    search_fields = ['apellido_paterno', 'nombres']
    list_filter = []
    filter_horizontal = []

    def get_queryset(self, request):
            queryset = super().get_queryset(request)
            if not request.user.is_superuser:
                queryset = queryset.filter(fundacion__gestor=request.user)
            return queryset
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if not change:  # Si es una nueva adolescente
            Progreso.objects.get_or_create(adolescente=obj)

admin.site.register(Adolescente, AdolescentesAdmin)



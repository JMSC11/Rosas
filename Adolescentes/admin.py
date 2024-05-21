from django.contrib import admin
from .models import Adolescente, CursosInscrito, Progreso
from fundaciones.models import Fundacion
from cursos.models import Curso
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin
from django import forms
# Register your models here.

admin.site.unregister(Group)
#admin.site.unregister(User)
class CursoInscritoInline(admin.TabularInline):
    model = CursosInscrito
    extra = 1
    autocomplete_fields = ['cursos']

class ProgresoInline(admin.StackedInline): 
    model = Progreso
    can_delete = False
    extra = 0

class AdolescenteAdminForm(forms.ModelForm):

    
    class Meta:
        model = Adolescente
        fields = ('__all__')
        widgets = {
            'fundacion': forms.Select(),
        }
        

@admin.register(Adolescente)
class AdolescenteAdmin(admin.ModelAdmin):
    form = AdolescenteAdminForm
    inlines = [ProgresoInline, CursoInscritoInline]
    list_display = ('nombres', 'apellido_paterno', 'apellido_materno', 'fundacion')


    def get_queryset(self, request):
            queryset = super().get_queryset(request)
            if not request.user.is_superuser:
                queryset = queryset.filter(fundacion__gestor=request.user)
            return queryset
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if not change:  # Si es una nueva adolescente
            Progreso.objects.get_or_create(adolescente=obj)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if request.user.is_authenticated:
            try:
                gestor_fundacion = Fundacion.objects.get(gestor=request.user)
                if not obj:  # solo si es un nuevo objeto
                    form.base_fields['fundacion'].initial = gestor_fundacion
            except Fundacion.DoesNotExist:
                pass
        return form

    def get_readonly_fields(self, request, obj=None):
        if obj:  
            return ('fundacion',)
        return ()
    def has_module_permission(self, request):
        return not request.user.is_superuser

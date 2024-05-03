from django.contrib import admin
from .models import Adolescente, CursosInscrito, Progreso
from fundaciones.models import Fundacion
from cursos.models import Curso
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin
from django import forms
# Register your models here.

admin.site.unregister(Group)
admin.site.unregister(User)
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
        fields = '__all__'
        widgets = {
            'fundacion': forms.Select(attrs={'disabled': True}),
        }

@admin.register(Adolescente)
class AdolescenteAdmin(admin.ModelAdmin):
    form = AdolescenteAdminForm
    list_display = ('nombres', 'apellido_paterno', 'apellido_materno', 'fundacion')

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
        if obj:  # solo hacer fundacion readonly si el objeto ya existe
            return ('fundacion',)
        return ()

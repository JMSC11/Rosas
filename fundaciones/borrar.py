fundaciones/adolecentes

from django.contrib import admin
from Adolescentes.models import Adolescente, Fundacion
from django.utils.html import mark_safe

/*fundaciones admin*/
class AdolescenteInline(admin.TabularInline):
    model = Adolescente
    fields = ('nombres', 'apellido_paterno', 'apellido_materno')
    readonly_fields = ('nombres', 'apellido_paterno', 'apellido_materno')
    extra = 0
    can_delete = False
    show_change_link = True

class FundacionAdmin(admin.ModelAdmin):
    list_display = ('nombre_fundacion', 'imagen_preview', 'descripcion')
    inlines = [AdolescenteInline]

    def imagen_preview(self, obj):
        if obj.imagen:
            return mark_safe(f'<img src="{obj.imagen.url}" width="50" height="50" />')
        return "No image"
    imagen_preview.short_description = 'Imagen'

admin.site.register(Fundacion, FundacionAdmin)

"""adolescentes admin"""
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
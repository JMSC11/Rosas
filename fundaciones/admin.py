from django.contrib import admin
from Adolescentes.models import Adolescente, Fundacion
from django.utils.html import mark_safe

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

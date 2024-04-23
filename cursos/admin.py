from django.contrib import admin
from .models import Curso, Categoria 

# Register your models here.
class CursoAdmin(admin.ModelAdmin):
    list_display = ['curso', 'categoria', 'descripcion', 'link']
    list_filter = ['categoria']
    search_fields = ['curso']

admin.site.register(Curso, CursoAdmin)
admin.site.register(Categoria)


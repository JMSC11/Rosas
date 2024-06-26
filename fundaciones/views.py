from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Fundacion
from cursos.models import Categoria, Curso
from Adolescentes.models import Adolescente, Progreso, CursosInscrito
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.db.models import Count
from django.core.paginator import Paginator
class ListaFundaciones(ListView):
    model = Fundacion
    template_name = 'list_analytics.html'
    context_object_name = 'lista_fundaciones'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Cuenta todas las fundaciones y agrega el resultado al contexto
        context['total_fundaciones'] = Fundacion.objects.count()
        # Obtiene todas las categorías y las agrega al contexto
        context['lista_categorias'] = Categoria.objects.all()
        context['total_cursos'] = Curso.objects.count()
        context['total_adolescentes'] = Adolescente.objects.count()

        return context

    
class DetalleFundacion(DetailView):
    model = Fundacion
    template_name = 'fundation_details.html'
    context_object_name = 'detalle_fundacion'

    def get_object(self, queryset=None):
        id_ = self.kwargs.get('id')
        fundacion = get_object_or_404(Fundacion, id=id_)

        # Recuperar todos los adolescentes inscritos en esta fundación
        adolescentes = Adolescente.objects.filter(fundacion=fundacion)
        fundacion.total_adolescentes = adolescentes.count()

        # Filtrar adolescentes por nivel educativo
        fundacion.adolescentes_secundaria = adolescentes.filter(escolaridad_actual='Secundaria').count()
        fundacion.adolescentes_bachillerato = adolescentes.filter(escolaridad_actual='Bachillerato').count()

        # Adolescentes que tienen hijos
        fundacion.adolescentes_con_hijos = adolescentes.filter(tiene_hijos=True).count()

        # Adolescentes que les falta al menos un documento importante
        adolescentes_sin_papeles = adolescentes.filter(
            Q(posee_acta_nacimiento=False) |
            Q(posee_curp=False) |
            Q(posee_seguro_social=False)
        )


        fundacion.adolescentes_sin_papeles = adolescentes_sin_papeles.count()
        fundacion.lista_adolescentes_sin_papeles = adolescentes_sin_papeles

        # Filtrar adolescentes por progreso de lectura
        progresos = Progreso.objects.filter(adolescente__fundacion=fundacion)
        fundacion.adolescentes_autoestima = progresos.filter(Autoestima=True).count()
        fundacion.adolescentes_necesidades = progresos.filter(Necesidades_e_intereses=True).count()
        fundacion.adolescentes_habilidades = progresos.filter(Habilidades_sociales=True).count()
        fundacion.adolescentes_derechos = progresos.filter(Derechos_humanos=True).count()

        return fundacion

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_adolescentes'] = self.object.total_adolescentes
        context['adolescentes_secundaria'] = self.object.adolescentes_secundaria
        context['adolescentes_bachillerato'] = self.object.adolescentes_bachillerato
        context['adolescentes_con_hijos'] = self.object.adolescentes_con_hijos
        context['adolescentes_sin_papeles'] = self.object.adolescentes_sin_papeles
        context['lista_adolescentes_sin_papeles'] = self.object.lista_adolescentes_sin_papeles
        context.update({
            'total_adolescentes': self.object.total_adolescentes,
            'adolescentes_autoestima': self.object.adolescentes_autoestima,
            'adolescentes_necesidades': self.object.adolescentes_necesidades,
            'adolescentes_habilidades': self.object.adolescentes_habilidades,
            'adolescentes_derechos': self.object.adolescentes_derechos
        })
        return context


class DetalleCursoView(DetailView):
    model = Categoria
    template_name = 'curso_details.html'
    context_object_name = 'lista_cursos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categoria = self.object
        cursos = Curso.objects.filter(categoria=categoria).annotate(
            adolescentes_inscritos=Count('cursosinscrito__adolescentes', distinct=True),
            adolescentes_por_fundacion=Count('cursosinscrito__adolescentes__fundacion', distinct=True)
        )
        context['cursos'] = cursos

        # Añadiendo detalle de adolescentes por fundación para cada curso
        detalle_adolescentes_por_fundacion = {}
        adolescentes_destacados = {}
        for curso in cursos:

            # Obtener adolescentes por fundación
            adolescentes_por_fundacion = Adolescente.objects.filter(
                cursosinscrito__cursos=curso
            ).values('fundacion__nombre_fundacion').annotate(
                cantidad=Count('id')
            ).order_by('fundacion__nombre_fundacion')
            detalle_adolescentes_por_fundacion[curso.id] = list(adolescentes_por_fundacion)

            # Obtener adolescentes destacados
            destacados = CursosInscrito.objects.filter(
                cursos=curso,
                es_destacado=True
            ).select_related('adolescentes').select_related('adolescentes__fundacion')

            adolescentes_destacados[curso.id] = [
                {
                    'nombre_completo': f"{ad.adolescentes.nombres} {ad.adolescentes.apellido_paterno}",
                    'fundacion': ad.adolescentes.fundacion.nombre_fundacion
                }
                for ad in destacados
            ]

        context['detalle_adolescentes_por_fundacion'] = detalle_adolescentes_por_fundacion
        context['adolescentes_destacados'] = adolescentes_destacados
        context['nombre_categoria'] = categoria.nombre_categoria

        return context

    
    


 
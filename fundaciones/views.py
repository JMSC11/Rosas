from django.shortcuts import render
from .models import Fundacion

def analytics_fundaciones(request):
    fundaciones_list = Fundacion.objects.all()
    return render(request, 'fundation_details.html', {'fundaciones_list': fundaciones_list})
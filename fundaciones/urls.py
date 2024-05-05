# fundaciones/urls.py

from django.urls import path
from .views import ListaFundaciones

urlpatterns = [
    path('', ListaFundaciones.as_view(), name='lista_fundaciones'),
]

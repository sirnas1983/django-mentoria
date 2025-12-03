from django.contrib import admin
from django.urls import path

from app.mi_primer_app.views import AgregarArticulo, ListaArticulos, ModificarArticulo, VerArticulo

app_name = 'articulo'

urlpatterns = [
    path('', ListaArticulos.as_view() , name='ver-todos'),
    path('ver/<int:pk>/', VerArticulo.as_view(), name='detalle'),
    # path('eliminar/<int:pk>/', <vista>, name='eliminar'),
    path('agregar/', AgregarArticulo.as_view(), name='agregar'),
    path('modificar/<int:pk>/', ModificarArticulo.as_view(), name='modificar')
]
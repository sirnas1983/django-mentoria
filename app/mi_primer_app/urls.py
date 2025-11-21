from django.contrib import admin
from django.urls import path

app_name = 'articulo'

urlpatterns = [
    path('/', <vista>, name='ver-todos'),
    path('ver/<int:id>', <vista>, name='detalle')
    path('eliminar/<int:id>/', <vista>, name='eliminar'),
    path('agregar/', <vista>, name='agregar'),
    path('modificar/<int:id>/', <vista>, name='modificar')
]
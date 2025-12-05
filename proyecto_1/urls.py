from django.conf import settings # faltaban estas importaciones
from django.conf.urls.static import static # faltaban estas importaciones

from django.contrib import admin
from django.urls import include, path

from proyecto_1.views import LoginUsuario, RegistrarUsuario, con_contenido_dinamico, inicio


urlpatterns = [
    path('', inicio, name="inicio"),
    path('usuario/registro/', RegistrarUsuario.as_view(), name='registro'),
    path('usuario/login/', LoginUsuario.as_view(), name="login"),
    path('con/', con_contenido_dinamico, name="prueba_1"),
    path('articulo/', include('app.mi_primer_app.urls')),
     # agregamos las rutas de mi aplicacion
]

if settings.DEBUG:  
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# agregamos estas lineas para poder servir los archivos estaticos y de media con el servidor en modo desarrollo


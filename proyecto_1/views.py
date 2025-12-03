from django.shortcuts import render
from app.mi_primer_app.models import Articulo


def inicio(request):
    contexto = {
        "titulo": "Pagina de prueba",
        "nombre": "Darian",
        "articulos": Articulo.objects.all()
    }
    return render(request,"base/base.html", contexto)


def con_contenido_dinamico(request):
    contexto = {
        "titulo": "Pagina hijo",
        "nombre": "Darian",
        "articulos": Articulo.objects.all()
    }
    return render(request,"hijo.html", contexto)




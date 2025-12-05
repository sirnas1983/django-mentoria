from django.shortcuts import render
from django.urls import reverse_lazy
from app.mi_primer_app.models import Articulo
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib.auth.views import LoginView

from proyecto_1.forms import RegistrarUsuarioForm

def inicio(request):
    contexto = {
        "titulo": "Pagina de prueba",
        "nombre": "Darian",
        "articulos": Articulo.objects.all()
    }
    return render(request,"base/base.html", contexto)


class RegistrarUsuario(CreateView):
    template_name = 'usuario/registro.html'
    form_class = RegistrarUsuarioForm
    success_url = reverse_lazy("inicio")

    def form_valid(self, form):
        usuario = form.save()
        login(self.request, usuario)
        return super().form_valid(form)

class LoginUsuario(LoginView):

    template_name = 'usuario/login.html'
    success_url = reverse_lazy('inicio')
    



def con_contenido_dinamico(request):
    contexto = {
        "titulo": "Pagina hijo",
        "nombre": "Darian",
        "articulos": Articulo.objects.all()
    }
    return render(request,"hijo.html", contexto)




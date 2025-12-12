from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

from app.mi_primer_app.forms import ArticuloFormulario, ArticuloFormularioAdmin, ComentarioForm
from app.mi_primer_app.models import Articulo, Comentario

# Create your views here.

class ListaArticulos(ListView):
    model = Articulo
    template_name = 'hijo.html'
    context_object_name = 'articulos'

class VerArticulo(DetailView):
    model = Articulo
    template_name = 'detalle.html'
    context_object_name = 'articulo'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.articulo = self.object
            comentario.usuario = self.request.user
            comentario.save()
            return redirect("articulo:detalle", pk=self.object.pk)
        context = self.get_context_data()
        context["form_comentario"] = form
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_comentario'] = ComentarioForm()
        context['comentarios'] = self.object.comentarios.all()
        return context

class AgregarArticulo(UserPassesTestMixin, CreateView):
    model = Articulo
    template_name = 'agregar.html'
    form_class = ArticuloFormulario
    success_url = reverse_lazy('articulo:ver-todos')

    def test_func(self):
        return self.request.user.is_colaborador or self.request.user.is_superuser

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        titulo = form.instance.titulo
        if len(titulo) < 5:
            form.add_error("titulo", "El titulo debe tener al menos 5 caracteres")
            return self.form_invalid(form)
        return super().form_valid(form)

class ModificarArticulo(UserPassesTestMixin, UpdateView):

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_superuser or self.get_object().usuario == self.request.user)

    model = Articulo
    template_name = 'agregar.html'
    form_class = ArticuloFormularioAdmin
    success_url = reverse_lazy('articulo:ver-todos')
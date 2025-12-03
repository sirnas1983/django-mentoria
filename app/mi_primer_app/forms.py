from dataclasses import fields
from django import forms

from app.mi_primer_app.models import Articulo, Comentario


class ArticuloFormulario(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['titulo','subtitulo','contenido']

class ArticuloFormularioAdmin(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['titulo','subtitulo','contenido', 'habilitado']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['autor', 'contenido']
   



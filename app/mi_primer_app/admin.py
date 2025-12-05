from django.contrib import admin

from app.mi_primer_app.models import Articulo, Comentario

# Register your models here.
class ComentarioInline(admin.TabularInline):  # o admin.StackedInline
    model = Comentario
    extra = 1  # cuántos formularios vacíos muestra

@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ("id_articulo", "titulo", "subtitulo", "fecha_creacion", "usuario")
    search_fields = ("titulo", "subtitulo", "usuario")
    inlines = [ComentarioInline]

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ("id", "articulo", "autor", "fecha")

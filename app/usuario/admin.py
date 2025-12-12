from django.contrib import admin

from app.usuario.models import Usuario

# Register your models here.
@admin.register(Usuario)
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name")

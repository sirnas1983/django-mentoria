from django.db import models

# Create your models here.
class Articulo(models.Model):
    id_articulo = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=100)
    contenido = models.TextField(max_length=5000)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    habilitado = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.id_articulo} - Titulo: {self.titulo}"


class Comentario(models.Model):
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE, related_name="comentarios")
    autor = models.CharField(max_length=50, blank=True, null=True)
    contenido = models.TextField(max_length=1000)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.autor or 'Anónimo'} en {self.articulo.titulo}"
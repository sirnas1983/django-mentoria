from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):

    dni = models.CharField(max_length=8, null=True, blank=True)
    foto_perfil = models.ImageField(upload_to='usuario/perfil/', null=True, blank=True)
    colaborador = models.BooleanField(default=False)
    
    @property
    def is_colaborador(self):
        return self.colaborador
    @property
    def is_admin(self):
        return self.is_superuser

    def __str__(self):
        return self.username


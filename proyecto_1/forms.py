from dataclasses import fields
from os import name
from django import forms
from django.contrib.auth.forms import UserCreationForm

from app.usuario.models import Usuario


class RegistrarUsuarioForm(UserCreationForm):

    email = forms.EmailField(required=True)
    
    class Meta:
        model = Usuario
        fields = ['username', 'first_name','last_name', 'email', 'password1', 'password2', 'foto_perfil']
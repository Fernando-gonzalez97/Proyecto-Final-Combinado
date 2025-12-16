from .models import Usuario
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import authenticate, login

class RegistroUsuarioForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = None
        self.fields['password1'].help_text = 'Mínimo 8 caracteres'
        self.fields['password2'].help_text = None

    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
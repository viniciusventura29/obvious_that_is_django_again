from django import forms
from django.contrib.auth.models import User
from aluno.models import Aluno

class AlunoModelForm(forms.ModelForm):
    class Meta:
        model = Aluno
        #fields = '__all__'

        fields = [
            'nome','telefone'
        ]

class UsuarioModelForm(forms.ModelForm):
    class Meta:
        model = User
        #fields = '__all__'

        fields = [
            'username',
            "email",
            'password',
            'first_name',
            'last_name',
        ]
from random import choices
from django.db import models


class Categoria(models.Model):
    Categoria = models.CharField(max_length=30)


class Curso(models.Model):
    Categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    titulo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=100)
    preco = models.DecimalField(
        max_digits=8, decimal_places=2
    )

    ativo = models.CharField(max_length=5, choices=(
        ('A', 'Ativa'),
        ('I', 'Inativo'),
    ))

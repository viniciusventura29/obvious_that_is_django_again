from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=11)

    def __str__(self):
        return self.nome


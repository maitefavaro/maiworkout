import email
from django.db import models

# Create your models here.

class Treino(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    email = models.EmailField()



class Treino_pessoa(models.Model):
    exercicio = models.CharField(max_length=225)
    repeticoes = models.PositiveIntegerField()
    vezes_repeticoes = models.PositiveIntegerField()
    pausa = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    carga = models.PositiveIntegerField(blank=True, null=True)



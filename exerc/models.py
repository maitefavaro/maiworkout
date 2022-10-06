import email
from django.db import models

# Create your models here.





class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    email = models.EmailField()

    def __str__(self):
        return self.nome
    


class Treino(models.Model):
    
    pessoa = models.ForeignKey( Pessoa,on_delete=models.CASCADE)
    def __str__(self):
        return 'Treino da '+ str(self.pessoa)




    



class Treino_pessoa(models.Model):

    treino = models.ForeignKey( Treino ,on_delete=models.CASCADE)
    exercicio = models.CharField(max_length=225)
    repeticoes = models.PositiveIntegerField()
    vezes_repeticoes = models.PositiveIntegerField()
    pausa = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    carga = models.PositiveIntegerField(blank=True, null=True)



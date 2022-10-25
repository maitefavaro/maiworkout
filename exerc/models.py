from django.db import models
from django.contrib.auth.models import AbstractUser




# Create your models here.

class User(AbstractUser):
  #username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
  #email = models.EmailField( unique = True)
  #native_name = models.CharField(max_length = 5)
  #phone_no = models.CharField(max_length = 10)
  #USERNAME_FIELD = 'email'
  #REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
  peso = models.DecimalField(max_digits=5, decimal_places=2,verbose_name="Peso", null=True)
  altura = models.DecimalField(max_digits=5, decimal_places=2,verbose_name="Altura", null=True)
  data_nascimento = models.DateField( null=True)
  
  def __str__(self):
      return "{}".format(self.username)


'''class Pessoa(models.Model):

    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    email = models.EmailField()
    senha1 = models.CharField(max_length=100,verbose_name="Senha")
    senha2 = models.CharField(max_length=100,verbose_name="Confirma sua Senha")
    peso = models.DecimalField(max_digits=5, decimal_places=2,verbose_name="Peso")
    altura = models.DecimalField(max_digits=5, decimal_places=2,verbose_name="Altura")


    def __str__(self):
        return self.nome'''
    


class Treino(models.Model):
    
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE)
    nome_Treino = models.CharField(max_length=15)

    def __str__(self):
        return str(self.nome_Treino)+" - " + str(self.pessoa)



class Exercicio(models.Model):

    treino = models.ForeignKey( Treino ,on_delete=models.CASCADE)
    exercicio = models.CharField(max_length=225)
    repeticoes = models.PositiveIntegerField()
    vezes_repeticoes = models.PositiveIntegerField()
    pausa = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    carga = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.exercicio



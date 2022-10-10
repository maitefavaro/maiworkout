from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import auth, messages
from exerc.models import Exercicio


# Create your views here.

def index(request):
    return render(request, 'index.html')


def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username') 
        email = request.POST.get('email') 
        password = request.POST.get('password') 
        
        user = User.objects.filter(username=username).first()

        if user:
            messages.info(request ,'Usuário já existente')
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        messages.info(request ,'Usuário cadastrado com sucesso')
        return redirect('login')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user:
            auth.login(request, user)
            return redirect('treino')
        else:   
            messages.info(request ,'Email ou senha inválidos')
            return render(request, 'login.html')


def treino(request):
    return render(request, 'treino.html')



def cad_treino(request):
    if request.method == "GET":
        return render(request, 'cad_treino.html')

    else:
        treino = request.POST.get('treino')
        exercicio = request.POST.get('exercicio')
        serie = request.POST.get('serie')
        vezes_repeticoes = request.POST.get('vezes_repeticoes')
        pausa = request.POST.get('pausa')
        carga = request.POST.get('carga')


        treino = Exercicio.objects.create(
            exercicio = exercicio,
            serie = serie,
            vezes_repeticoes = vezes_repeticoes,
            pausa = pausa,
            carga = carga,
        )

        treino.save()
        return redirect('index')
    


def qtd_treino(request,qtd_exercicios):

    context = {
        "qtd_exercicios":qtd_exercicios,
    }

    return render(request, 'qtd.html',context)

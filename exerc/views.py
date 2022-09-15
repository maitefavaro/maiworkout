from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

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
            return HttpResponse('Usuário já existente')
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        return HttpResponse('Usuário cadastrado com sucesso')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return HttpResponse('Autenticado')
        else:
            return HttpResponse('Email ou senha inválidos')
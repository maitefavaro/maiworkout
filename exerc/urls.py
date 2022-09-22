from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name='index'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('treino/', views.treino, name='treino'),
    path('cadastro_do_treino/', views.cad_treino, name='cad_treino')
]

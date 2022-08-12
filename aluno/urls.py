from django.urls import path
from . import views

urlpatterns=[
    path('aluno_lista/', views.aluno_index, name='alunos_lista'),
    path('aluno_cadastro/', views.cadastrar_aluno, name='aluno_cadastro'),
    path('aluno_usuario/', views.cadastrar_aluno, name='aluno_usuario'),
]
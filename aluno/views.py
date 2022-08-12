from multiprocessing import context
from django.shortcuts import render

from aluno.models import Aluno
from aluno.form import AlunoModelForm,UsuarioModelForm
from django.contrib import messages

def aluno_index(request):
    aluno_sql=Aluno.objects.all()

    context={
        'alunos': aluno_sql
    }
    return render(request, 'aluno/index.html',context)

def cadastrar_aluno(request):

    if str(request.method)=="POST":
        aluno = AlunoModelForm(request.POST)
        if aluno.is_valid():
            aluno.save()
            messages.success(request,"salvo com sucesso!") 
        else:
            messages.error(request,"Erro ao salvar")

    else:
        aluno = AlunoModelForm()

    context = {
        'form': aluno
    }
    return render(request,'aluno/aluno_cadastro.html',context)

def cadastrar_aluno(request):

    if str(request.method)=="POST":
        aluno = AlunoModelForm(request.POST)
        if aluno.is_valid():
            aluno.save()
            messages.success(request,"salvo com sucesso!") 
        else:
            messages.error(request,"Erro ao salvar")

    else:
        usuario = UsuarioModelForm()

    context = {
        'form': usuario
    }
    return render(request,'aluno/aluno_usuario.html',context)



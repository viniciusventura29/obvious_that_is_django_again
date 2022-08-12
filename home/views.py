from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.core.validators import validate_email
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required


def home_index(request):
    return render(request, 'home/index.html')


def usuario_login(request):
    if str(request.method) !="POST":
        return render(request, 'home/login.html')

    else:
        usuario = request.POST.get('login')
        senha = request.POST.get('senha')
        user_login = auth.authenticate(
            username=usuario,
            password=senha,
        )
            
        if user_login:
            auth.login(request,user_login)
            return render(request, 'home/dashboard.html')

        else:
            messages.warning(request,"Nada a ver mano")
            return render(request, 'home/login.html')


def usuario_cadastro(request):
    if str(request.method) == 'POST':
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        primeiro = request.POST.get('primeiro')
        segundo = request.POST.get('segundo')
        senha1 = request.POST.get('senha1')
        senha2 = request.POST.get('senha2')

        try:
            validate_email(email)
        except:
            messages.error(request, 'Email Inválido')
            return render(request, 'home/cadastro.html')

        if len(senha1)<6:
            messages.error(request, 'Senha deve ter no mínimo 6 digitos')
            return render(request, 'home/cadastro.html')

        if senha2!=senha1:
            messages.error(request, 'Senhas diferentes! Tente novamente')
            return render(request, 'home/cadastro.html')

        if User.objects.filter(username=usuario).exists():
            messages.error(request, 'Nome de usuário ja cadastrado! Tente novamente')
            return render(request, 'home/cadastro.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email ja cadastrado! Tente novamente')
            return render(request, 'home/cadastro.html')

        novo_usuario = User.objects.create_user(
        username=usuario,
        first_name=primeiro,
        email=email,
        password=senha1
        )

        novo_usuario.save()
    return render(request, 'home/cadastro.html')

def sair(request):
    auth.logout(request)
    return redirect('usuario_login')

@login_required(redirect_field_name='usuario_login')
def dashboard(request):
    return render(request, 'home/dashboard.html')
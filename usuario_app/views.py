from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from usuario_app.forms import LoginForms , CadastroForms

def view_index(request):
    return render(request, "usuario_app/paginas/index.html", )

def view_login(request):
    formulario = LoginForms()

    if request.methodo == 'POST':
        formulario = LoginForms(request.POST)

        if formulario.is_valid():
            nome = formulario['nome_login'].value()
            senha = formulario['senha'].value()

            usuario = auth.authenticate(
                request,
                username = nome,
                password = senha
            )

            if usuario is not None:
                auth.login(request, usuario)
                return redirect ('home_app:index')
            else:
                return redirect('home_app:login')
            
    return render(request, "usuario_app/paginas/login.html", context = {'formulario':formulario})

def logout(request):
    auth.logout(request)
    return redirect('home_app:login')

def view_cadastro(request):
    formulario = CadastroForms()

    if formulario.is_valid():
        if formulario['senha_1'].value != formulario['senha_2'].value():
            return redirect ('usuario:cadastro')
        
        nome = formulario['nome_cadastro'].value()
        email = formulario['email_cadastro'].value()
        senha = formulario['senha_1'].value()

        if User.objects.filter(username=nome).exists():
            return redirect('usuario:cadastro')
    
        novo_usuario = User.objects.create_user(
            username= nome,
            email = email,
            password= senha
        )

        novo_usuario.save()
        return redirect('usuario:login')

    return render(request, "usuario_app/paginas/cadastro.html", context = {'formulario':formulario})

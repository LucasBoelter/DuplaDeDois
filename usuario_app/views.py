from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
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
                messages.success(request, f'usuario {nome} logado com sucesso!')
                return redirect ('home_app:index')
            else:
                messages.error(request, 'erro ao tentar logar!')
                return redirect('home_app:login')
            
    return render(request, "usuario_app/paginas/login.html", context = {'formulario':formulario})

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso!!')
    return redirect('home_app:login')

def view_cadastro(request):
    formulario = CadastroForms()

    if request.method == 'POST':
        formulario = CadastroForms(request.POST)

        if formulario.is_valid():
            if formulario['senha1'].value != formulario['senha2'].value():
                messages.error(request, 'as senhas não são iguais')
                return redirect ('usuario_app:cadastro')
            
            nome = formulario['nome_completo'].value()
            email = formulario['email'].value()
            senha = formulario['senha1'].value()

            if User.objects.filter(username=nome).exists():
                messages.error(request, 'o usuário já existe')
                return redirect('usuario_app:cadastro')
        
            novo_usuario = User.objects.create_user(
                username= nome,
                email = email,
                password= senha
            )

            novo_usuario.save()
            messages.success(request, 'cadastro realizado com sucesso')
            return redirect('usuario_app:login')

    return render(request, "usuario_app/paginas/cadastro.html", context = {'formulario':formulario})

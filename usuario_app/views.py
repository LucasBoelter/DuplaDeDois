from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from usuario_app.forms import LoginForms , CadastroForms
from usuario_app.models import ImagemUsuario
from usuario_app.forms import ImagemUsuarioForm

def view_index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return render(request, "usuario_app/paginas/login.html")
    
    return render(request, "home_app/paginas/index.html", context={})

#que seria a parte de imagem do sor
def view_perfil(request):
    #verificando se o usuario está logado, pra mostrar os dados...
    if not request.user.is_authenticated:
        messages.error(request, 'usuario não logado no perfil')
        return redirect ('usuario_app:login')

    else:
        # coletando user
        usuario = request.user

        # coletando img
        imagem = ImagemUsuario.objects.all()
        for item in imagem:
            if item.usuario == usuario:
                foto=item.foto
                id=item.id

                context={
                    'user':usuario,
                    'foto':foto,
                    'id':id
                    }

            else:
                context={
                    'user':usuario,
                    'foto':'',
                    'id':''
                    }
    return render(request, "usuario_app/paginas/perfil.html", context)

def view_login(request):
    formulario = LoginForms()

    if request.method == 'POST':
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
                messages.success(request, f'Olá {nome}')
                return redirect ('home_app:index')
            else:
                messages.error(request, 'erro ao tentar logar!')
                return redirect('home_app:login')
            
    return render(request, "usuario_app/paginas/login.html", context = {'formulario':formulario})

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso!!')
    return redirect('usuario_app:login')

def view_cadastro(request):
    formulario = CadastroForms()

    if request.method == 'POST':
        formulario = CadastroForms(request.POST)

        if formulario.is_valid():
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

def view_add_imagem(request):
    #verificando se o usuario está logado, pra mostrar os dados...
    if not request.user.is_authenticated:
        messages.error(request, 'usuario não logado no adiciona_imagem')
        return redirect ('usuario_app:login')
    
    formulario = ImagemUsuarioForm()
    if request.method == 'POST':
        formulario = ImagemUsuarioForm(request.POST, request.FILES)
        print(formulario)
        print(formulario.errors)
        print(formulario.is_valid())
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Nova imagem cadastrada!')
            return redirect('usuario_app:perfil')

    return render (request, 'usuario_app/paginas/adiciona_imagem.html', context={'formulario':formulario})

def view_edt_imagem(request, id_url):
    if not request.user.is_authenticated:
        messages.error(request, 'usuário não logado no usuario_app/editar')
        return redirect('usuario_app:login')
    
    imagem = ImagemUsuario.objects.filter(id=id_url)
    if not imagem:
        messages.error(request, 'Imagem não encontrada!')
        return redirect('home_app:index')

    imagem = imagem[0]
    formulario = ImagemUsuarioForm(instance=imagem)

    if request.method == 'POST':
        if 'delete_image' in request.POST:
            return view_apaga_imagem(request, id_url)

        formulario = ImagemUsuarioForm(request.POST, request.FILES, instance=imagem)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Imagem alterada')
            return redirect ('home_app:index')

    return render (request, 'usuario_app/paginas/edita_imagem.html', context={'formulario':formulario, 'id_url':id_url})


def view_deletar_imagem(request, id_url):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado no usuario_app/editar')
        return redirect('usuario_app:login')

    try:
        imagem = ImagemUsuario.objects.get(id=id_url)
        imagem.delete()
        messages.success(request, 'Imagem deletada')
    except ImagemUsuario.DoesNotExist:
        messages.error(request, 'Imagem não encontrada!')

    return redirect('home_app:index')

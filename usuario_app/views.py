from django.shortcuts import render
from usuario_app.forms import LoginForms , CadastroForms

def view_index(request):
    return render(request, "usuario_app/paginas/index.html", )

def view_login(request):
    formulario = LoginForms()
    return render(request, "usuario_app/paginas/login.html", context = {'formulario':formulario})

def view_cadastro(request):
    formulario = CadastroForms()
    return render(request, "usuario_app/paginas/cadastro.html", context = {'formulario':formulario})

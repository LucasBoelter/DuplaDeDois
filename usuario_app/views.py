from django.shortcuts import render

def view_index(request):
    return render(request, "usuario_app/paginas/index.html", )

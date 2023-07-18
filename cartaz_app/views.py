from django.shortcuts import render

def view_index(request):
    return render(request, "cartaz_app/paginas/index.html", )

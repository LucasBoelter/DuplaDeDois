from django.shortcuts import render
from . import models

def view_index(request):
    filmes = models.Cartaz.objects.all()
    return render(request, "cartaz_app/paginas/index.html", context={'imagens': filmes} )

def view_busca(request):
    filme = models.Cartaz.objects.all()

    if 'buscando' in request.GET:
        nome = request.GET['buscando']
        if nome:
            filme = filme.filter(nome__icontains=nome)
        else:
            filme = []

    return render(request, 'galeria/paginas/busca.html', context={'imagens':filme})

    # imagens = models.Cartaz.objects.filter()
    # return render(request, "cartaz_app/paginas/index.html", context={'imagens': imagens} )


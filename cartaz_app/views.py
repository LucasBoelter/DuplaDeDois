from django.shortcuts import render
from cartaz_app.models import Cartaz

def view_index(request):
    filmes = Cartaz.objects.all()
    # troquei para filmes a chave do dicionário pq n faz sentido usar imagem
    return render(request, "cartaz_app/paginas/index.html", context={'filmes' : filmes} )

def view_busca(request):
    filmes = Cartaz.objects.all()
    if 'buscando' in request.GET:
        nome = request.GET['buscando']
        if nome:
            filmes = filmes.filter(titulo__icontains=nome)
        else:
            filmes = []

    return render(request, 'cartaz_app/paginas/busca.html', context={'filmes':filmes})



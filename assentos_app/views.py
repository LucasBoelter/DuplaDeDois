from django.shortcuts import render, redirect
from django.contrib import messages
from cartaz_app.models import Cartaz
from datetime import datetime

def view_index(request):
    # para completar for dos botões de assentos
    array_fileiras = ['A', 'B', 'C', 'D']
    cadeiras_por_fileira = 7

    # resgatando nome do filme
    codigo_filme = request.GET['codigoFilme']

    context = {
        'fileiras' : array_fileiras,
        'quant_cadeiras' : range(1, cadeiras_por_fileira),
        'codigo_filme' : codigo_filme,
    } 

    return render(request, "assentos_app/paginas/index.html", context)

def view_pag(request):
    #validando o usuario
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return render(request, "usuario_app/paginas/login.html")
    
    # recebendo dados
    lugares_selecionados = request.GET.get('lugaresSelecionados[]').split(',')
    codigo_filme = request.GET.get('codigoFilme')
    print('codigo',codigo_filme)
    data_compra=datetime.now()

    # tratando dados
    lugares=''
    quant=0
    for lugar in lugares_selecionados:
        lugares+= lugar + ' '
        quant+=1

    valor=quant*35

    filmes = Cartaz.objects.all()
    filmes = filmes.filter(titulo__icontains=codigo_filme)
    print('obj',filmes)

    context = {
        'lugares_selecionados' : lugares,
        'codigo_filme' : filmes,
        'data_compra' : data_compra,
        'quant' : quant,
        'valor' : valor
    }

    return render (request, 'assentos_app/paginas/pagamento.html', context)
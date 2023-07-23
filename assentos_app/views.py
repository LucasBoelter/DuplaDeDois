from django.shortcuts import render
from cartaz_app.models import Cartaz

def view_index(request):
    array_fileiras = ['A', 'B', 'C', 'D']
    cadeiras_por_fileira = 7

    codigo_filme = request.GET['codigoFilme']
    print('filme: ', codigo_filme)

    context = {
        'fileiras' : array_fileiras,
        'quant_cadeiras' : range(1, cadeiras_por_fileira),
        'codigo_filme' : codigo_filme,
    } 

    return render(request, "assentos_app/paginas/index.html", context)

def view_pag(request):

    lugares_selecionados = request.GET.get('lugaresSelecionados[]').split(',')
    codigo_filme = request.GET.get('codigoFilme')
    context = {
        'lugares_selecionados' : lugares_selecionados,
        'codigo_filme' : codigo_filme
    }
    return render (request, 'assentos_app/paginas/pagamento.html', context)
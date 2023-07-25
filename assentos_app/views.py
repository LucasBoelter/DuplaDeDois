from django.shortcuts import render, redirect
from cartaz_app.models import Cartaz
from datetime import datetime
from django.contrib import messages
from assentos_app.models import Vendas
from assentos_app.forms import VendasForm

def view_index(request):
    # para completar for dos botões de assentos
    array_fileiras = ['A', 'B', 'C', 'D']
    cadeiras_por_fileira = 7

    # resgatando nome do filme
    codigo_filme = request.GET['codigoFilme']
    print(codigo_filme)
    assentos_ocupados= Vendas.objects.all()
    print('assentos antes if', assentos_ocupados)

    if codigo_filme:
        if assentos_ocupados:
            assentos_ocupados=assentos_ocupados.filter(filme__icontains =codigo_filme)
            print('assentos ', assentos_ocupados)

    # adicionando no python o filtro do que esta ocupado
    ocupados = []
    for item in assentos_ocupados:
        ocupados.append(item.assento)
    livres = []
    for fila in array_fileiras:
        for coluna in range(1, cadeiras_por_fileira):
            livres.append(fila + str(coluna))

    context = {
        #'fileiras' : array_fileiras,
        #'quant_cadeiras' : range(1, cadeiras_por_fileira),
        'livres': livres,
        'codigo_filme' : codigo_filme,
        'ocupados' : ocupados
    } 
    print(context)

    return render(request, "assentos_app/paginas/index.html", context)

def view_pag(request):
    #validando o usuario
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return render(request, "usuario_app/paginas/login.html")

    try: 
        # se dados coletados, salvando no banco
        if request.method == 'POST':
            codigo_filme = request.POST.get('filme')

            # limpando var, na arte da gambearra
            lugares_selecionados = request.POST.get('assento').replace("[", "").replace("]", "").replace(" ", "").replace("'", "").split(",")

            for lugar in lugares_selecionados:
                data = dict(request.POST)
                data['assento'] = lugar
                data['forma_pagamento'] = request.POST.get('forma_pagamento')
                data['filme'] = request.POST.get('filme')
                
                formulario = VendasForm(data)

                if formulario.is_valid():
                    formulario.save()

            messages.success(request, 'Compra efetuada com sucesso!')

            return redirect('home_app:index')

        else:
            # recebendo dados
            codigo_filme = request.GET.get('codigoFilme')
            lugares_selecionados = request.GET.get('lugaresSelecionados[]').split(',')
            filmes = Cartaz.objects.all()
            filmes = filmes.get(titulo__icontains=codigo_filme)

            formulario = VendasForm()
            formulario.initial['filme'] = filmes.titulo
            formulario.initial['assento'] = lugares_selecionados

    except Exception as erro:
        print(erro)

    data_compra=datetime.now()
    filmes = Cartaz.objects.all()
    filmes = filmes.get(titulo__icontains=codigo_filme)

    # tratando lugares
    lugares=''
    for lugar in lugares_selecionados:
        lugares+=' '+lugar

    context = {
        'lugares_selecionados' : lugares,
        'codigo_filme' : filmes.titulo or None,
        'horario' : filmes.horario2,
        'data_compra' : data_compra,
        'quant' : len(lugares_selecionados),
        'valor' : len(lugares_selecionados)*35,
        'formulario' : formulario
    }
    return render (request, 'assentos_app/paginas/pagamento.html', context)

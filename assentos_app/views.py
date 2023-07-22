from django.shortcuts import render

def view_index(request):
    array_fileiras = ['A', 'B', 'C', 'D']
    cadeiras_por_fileira = 7

    context = {
        'fileiras' : array_fileiras,
        'quant_cadeiras' : range(1, cadeiras_por_fileira)
    } 

    
    return render(request, "assentos_app/paginas/index.html", context)

def view_pag(request):
    buttons_clicked = request.GET.get('finalizar', '').split(',')
    print(buttons_clicked)
    return render (request, 'assentos_app/paginas/pagamento.html', context={})
from django.shortcuts import render

def view_index(request):
    # if 'btn_a1' in request.GET:
    #     assentos=request.GET['btn_a1']
    #     print(assentos)
    # if request.method == 'POST':
    #     if 'btn_a1' in request.POST:
    #         btn_id= 'btn_a1'
    #         print(btn_id)
        
    #     if 'finalizar' in request.POST:
    #         buttons_clicked = []
    #         for key in request.POST:
    #             if key.startswith('button'):
    #                 buttons_clicked.append(key)
    return render(request, "assentos_app/paginas/index.html")

def view_pag(request):
    buttons_clicked = request.GET.get('finalizar', '').split(',')
    print(buttons_clicked)
    return render (request, 'assentos_app/paginas/pagamento.html', context={})
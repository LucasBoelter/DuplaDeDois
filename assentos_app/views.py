from django.shortcuts import render

def view_index(request):
    return render(request, "assentos_app/paginas/index.html")

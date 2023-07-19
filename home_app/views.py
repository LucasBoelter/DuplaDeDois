from django.shortcuts import render
from . import models

def view_index(request):
    imagens = models.Home.objects.all()
    return render(request, "home_app/paginas/index.html", context={'imagens': imagens})

#tentando puxar os dados do bd
# def carrosel(request):
#     imagens = models.Home.objects.all()
#     return render(request, 'home_app/paginas/index.html', {'imagens': imagens})

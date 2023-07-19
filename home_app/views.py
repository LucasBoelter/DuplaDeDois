from django.shortcuts import render
from .models import Home

def view_index(request):
    return render(request, "home_app/paginas/index.html", )

#tentando puxar os dados do bd
def carrosel(request):
    imagens = Home.objects.all()
    return render(request, 'home_app/paginas/index.html', {'imagens': imagens})

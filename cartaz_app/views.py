from django.shortcuts import render
from . import models

def view_index(request):
    imagens = models.Cartaz.objects.all()
    return render(request, "cartaz_app/paginas/index.html", context={'imagens': imagens} )


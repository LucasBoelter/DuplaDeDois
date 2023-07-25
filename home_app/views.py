from django.shortcuts import render
from . import models

def view_index(request):
    imagens = models.Home.objects.all()
    return render(request, "home_app/paginas/index.html", context={'imagens': imagens})

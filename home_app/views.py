from django.shortcuts import render

def view_index(request):
    return render(request, "home_app/paginas/index.html", )

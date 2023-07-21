from django.contrib import admin
from django.urls import path
from . import views

app_name = "cartaz_app"

urlpatterns = [
    path('', views.view_index, name="index"),
    path('busca/', views.view_busca, name="busca"),
    path('adicionar-imagem/', views.view_add_imagem, name="adicionar_imagem"),
    path('editar-imagem/', views.view_edt_imagem, name="editar_imagem"),
    path('apagar-imagem/', views.view_apg_imagem, name="apagar_imagem"),
]

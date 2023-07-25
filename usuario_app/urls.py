from django.contrib import admin
from django.urls import path
from . import views

app_name = "usuario_app"

urlpatterns = [
    path('', views.view_index, name="index"),
    path('login/', views.view_login, name="login"),
    path('cadastro/', views.view_cadastro, name="cadastro"),
    path('logout/', views.logout, name="logout"),
    path('admin/', admin.site.urls, name='admin'),
    path('perfil/', views.view_perfil, name='perfil'),
    path('adicionar-imagem/', views.view_add_imagem, name="adicionar_imagem"),
    path('editar-imagem/<int:id_url>/', views.view_edt_imagem, name="editar_imagem"),
    path('deletar_imagem/<int:id_url>/', views.view_deletar_imagem, name='deletar_imagem')
]
